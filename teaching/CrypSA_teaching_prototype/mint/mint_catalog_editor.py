from __future__ import annotations

import json
import tkinter as tk
from tkinter import messagebox

from .mint_lens_adapters import build_mint_detail_lens, build_mint_entity_modal_lens
from .mint_editor_ui import open_entity_modal, open_tag_manager_modal, require_selected_kind
from .mint_catalog_store import (
    CATALOG_PATH,
    GENOME_ACTIONS,
    load_catalog,
    normalize_genome,
    normalize_rule_tags,
    palette_for_entity_name,
    save_catalog,
    sanitize_entity_definition,
)


BG = "#0b1020"
PANEL = "#141b34"
TEXT = "#e6eefc"
MUTED = "#94a3b8"
ACCENT = "#67e8f9"


def _meta_rule_tags(meta: dict[str, object]) -> list[str]:
    return normalize_rule_tags(meta.get("rule_tags", ["none"]))


def _meta_genome(meta: dict[str, object]) -> dict[str, object]:
    return normalize_genome(meta["genome"], meta)


def _detail_summary_text(meta: dict[str, object], genome: dict[str, object]) -> str:
    """Return the short Mint summary shown above the detail pane."""

    tags = _meta_rule_tags(meta)
    return (
        f"Tags: {', '.join(tags)}\n"
        f"States: {', '.join(genome['valid_states'])}\n"
        f"Allowed Actions: {', '.join(genome['allowed_actions'])}"
    )


def _detail_rule_summary(rule: dict[str, object]) -> str:
    """Return one compact line describing an invariant rule."""

    summary = str(rule["rule_type"])
    actions = rule.get("actions", [])
    if actions:
        summary += f" | actions={', '.join(actions)}"
    if "required_parent_event_family" in rule:
        summary += f" | parent={rule['required_parent_event_family']}"
    if "required_context_event_family" in rule:
        summary += f" | context={rule['required_context_event_family']}"
    if "threshold_key" in rule:
        summary += f" | threshold={rule['threshold_key']}"
    return summary


def _detail_lines(meta: dict[str, object], genome: dict[str, object]) -> list[str]:
    """Return the detailed Mint description shown in the right-hand text pane."""

    lines = [
        f"Description: {str(meta.get('description', '')).strip() or 'None'}",
        "",
        "Action Transitions:",
    ]
    for action_name in GENOME_ACTIONS:
        transition = genome["action_transitions"][action_name]
        lines.append(
            f"- {action_name}: from [{', '.join(transition['from_states'])}]"
            + (f" -> {transition['to_state']}" if "to_state" in transition else "")
        )
    lines.append("")
    lines.append("Invariant Rules:")
    for rule in genome["invariant_rules"]:
        lines.append(f"- {_detail_rule_summary(rule)}")
    lines.append("")
    lines.append(f"Initial Invariant State: {json.dumps(genome['initial_invariant_state'])}")
    return lines


class MintCatalogEditor:
    def __init__(self) -> None:
        # Load the catalog first so the root window can immediately reflect the
        # current saved Mint state in both the list and detail panes. This file
        # stays as the Mint-side coordinator: actions happen here, while read-
        # only detail/modal shaping lives in mint_lens_adapters.py.
        self.BG = BG
        self.PANEL = PANEL
        self.TEXT = TEXT
        self.MUTED = MUTED
        self.ACCENT = ACCENT
        self.entity_definitions, self.entity_metadata, self.catalog_version, self.rule_tags = load_catalog()

        self.root = tk.Tk()
        self.root.title("CrypSA Mint Editor")
        self.root.geometry("1040x700")
        self.root.minsize(940, 620)
        self.root.configure(bg=BG)

        self.selected_kind: str | None = None
        self.status_var = tk.StringVar(value=f"Mint Catalog: {CATALOG_PATH.name} | v{self.catalog_version}")

        shell = tk.Frame(self.root, bg=BG)
        shell.pack(fill="both", expand=True, padx=18, pady=18)

        header = tk.Frame(shell, bg=BG)
        header.pack(fill="x", pady=(0, 14))
        tk.Label(header, text="CrypSA Mint Editor", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 22), anchor="w").pack(fill="x")
        tk.Label(
            header,
            text="Minted kinds define immutable identities, deterministic genomes, and invariant validation rules for future canonical events.",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 11),
            anchor="w",
            justify="left",
            wraplength=960,
        ).pack(fill="x", pady=(4, 0))

        body = tk.Frame(shell, bg=BG)
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=0)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        self._build_list_panel(body)
        self._build_detail_panel(body)

        footer = tk.Frame(shell, bg=BG)
        footer.pack(fill="x", pady=(12, 0))
        tk.Label(footer, textvariable=self.status_var, bg=BG, fg=ACCENT, font=("Segoe UI", 10), anchor="w").pack(side="left")

        self.root.bind("<Escape>", lambda _event: self.root.destroy())
        self._refresh_list()

    def _build_list_panel(self, parent: tk.Misc) -> None:
        # The left side is the action-and-selection surface: choose a kind,
        # then trigger add/edit/remove/tag/reload operations from here.
        panel = tk.Frame(parent, bg=PANEL, highlightbackground="#24304f", highlightthickness=1)
        panel.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
        panel.rowconfigure(1, weight=1)

        tk.Label(panel, text="Mint Kinds", bg=PANEL, fg=TEXT, font=("Segoe UI Semibold", 16), anchor="w").grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 10))

        list_frame = tk.Frame(panel, bg=PANEL)
        list_frame.grid(row=1, column=0, sticky="nsew", padx=16)
        list_frame.rowconfigure(0, weight=1)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.kind_list = tk.Listbox(
            list_frame,
            bg="#101938",
            fg=TEXT,
            selectbackground="#24304f",
            selectforeground=TEXT,
            relief="flat",
            font=("Consolas", 11),
            exportselection=False,
            yscrollcommand=scrollbar.set,
            width=24,
        )
        self.kind_list.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.kind_list.yview)
        self.kind_list.bind("<<ListboxSelect>>", self._on_kind_selected)

        actions = tk.Frame(panel, bg=PANEL)
        actions.grid(row=2, column=0, sticky="ew", padx=16, pady=16)
        self._action_button(actions, "Add", self._open_create_modal).pack(side="left")
        self._action_button(actions, "Edit", self._open_edit_modal).pack(side="left", padx=(8, 0))
        self._action_button(actions, "Remove", self._remove_selected_kind).pack(side="left", padx=(8, 0))
        self._action_button(actions, "Tags", self._open_tag_manager_modal).pack(side="left", padx=(8, 0))
        self._action_button(actions, "Reload", self._reload_catalog, alt=True).pack(side="right")

    def _build_detail_panel(self, parent: tk.Misc) -> None:
        # The right side is intentionally read-only. It acts as a live summary
        # of the currently selected Mint kind rather than another edit surface.
        panel = tk.Frame(parent, bg=PANEL, highlightbackground="#24304f", highlightthickness=1)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.columnconfigure(0, weight=1)

        tk.Label(panel, text="Mint Definition", bg=PANEL, fg=TEXT, font=("Segoe UI Semibold", 16), anchor="w").pack(fill="x", padx=18, pady=(16, 10))

        self.detail_name = tk.Label(panel, text="", bg=PANEL, fg=ACCENT, font=("Consolas", 18), anchor="w")
        self.detail_name.pack(fill="x", padx=18)
        self.detail_summary = tk.Label(panel, text="", bg=PANEL, fg=MUTED, font=("Segoe UI", 11), anchor="w", justify="left", wraplength=640)
        self.detail_summary.pack(fill="x", padx=18, pady=(8, 0))

        self.palette_canvas = tk.Canvas(panel, width=168, height=56, bg="#101938", highlightthickness=0)
        self.palette_canvas.pack(anchor="w", padx=18, pady=(16, 0))

        self.detail_text = tk.Text(
            panel,
            bg="#101938",
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            wrap="word",
            font=("Consolas", 10),
            state="disabled",
        )
        self.detail_text.pack(fill="both", expand=True, padx=18, pady=(14, 18))

    def _action_button(self, parent: tk.Misc, label: str, command: object, alt: bool = False) -> tk.Button:
        return tk.Button(
            parent,
            text=label,
            command=command,
            bg=("#1d2845" if alt else "#24304f"),
            fg=TEXT,
            activebackground="#34508a",
            activeforeground=TEXT,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#34508a",
            highlightcolor=ACCENT,
            font=("Segoe UI", 10),
            padx=14,
            pady=6,
            cursor="hand2",
        )

    def _refresh_list(self) -> None:
        # Keep list refresh logic centralized so save, reload, and selection
        # changes all reuse the same "restore selection if possible" behavior.
        selected = self.selected_kind
        ordered = sorted(self.entity_definitions)
        self.kind_list.delete(0, "end")
        for kind in ordered:
            self.kind_list.insert("end", kind)
        if selected in self.entity_definitions:
            index = ordered.index(selected)
            self.kind_list.selection_set(index)
            self.kind_list.see(index)
            self._set_selected_kind(selected)
        elif ordered:
            self.kind_list.selection_set(0)
            self._set_selected_kind(ordered[0])
        else:
            self._set_selected_kind(None)

    def _set_selected_kind(self, kind: str | None) -> None:
        self.selected_kind = kind
        self.palette_canvas.delete("all")
        self.palette_canvas.create_rectangle(0, 0, 168, 56, fill="#101938", outline="")
        self.detail_text.configure(state="normal")
        self.detail_text.delete("1.0", "end")
        self.detail_text.configure(state="disabled")
        lens = self._mint_detail_lens(kind)
        if lens.kind is None:
            self.detail_name.configure(text="")
            self.detail_summary.configure(text=lens.summary_text)
            return
        # Detail rendering happens in three layers: header text, palette
        # preview, then the longer genome/rule body below.
        self.detail_name.configure(text=lens.kind)
        self.detail_summary.configure(text=lens.summary_text)
        self.palette_canvas.create_rectangle(14, 12, 54, 44, fill=lens.palette_fill, outline=lens.palette_outline, width=3)
        self.palette_canvas.create_rectangle(86, 12, 126, 44, fill=lens.default_color, outline="#cbd5e1", width=2)
        self.palette_canvas.create_text(106, 48, text="default", fill=MUTED, font=("Segoe UI", 8))

        self.detail_text.configure(state="normal")
        self.detail_text.insert("1.0", lens.detail_text)
        self.detail_text.configure(state="disabled")

    def _on_kind_selected(self, _event: tk.Event) -> None:
        selection = self.kind_list.curselection()
        if selection:
            self._set_selected_kind(self.kind_list.get(selection[0]))

    def _reload_catalog(self) -> None:
        self.entity_definitions, self.entity_metadata, self.catalog_version, self.rule_tags = load_catalog()
        self.status_var.set(f"Reloaded {CATALOG_PATH.name} | v{self.catalog_version}")
        self._refresh_list()

    def _save_catalog(self, action: str) -> None:
        self.catalog_version = save_catalog(self.entity_definitions, self.entity_metadata, self.rule_tags)
        self.status_var.set(f"{action} -> {CATALOG_PATH.name} | v{self.catalog_version}")
        self._refresh_list()

    def _meta_rule_tags(self, meta: dict[str, object]) -> list[str]:
        return _meta_rule_tags(meta)

    def _meta_genome(self, meta: dict[str, object]) -> dict[str, object]:
        return _meta_genome(meta)

    def _mint_detail_lens(self, kind: str | None):
        # The editor stays as the coordinator; the adapter owns the read-only
        # data shape used by the right-hand detail pane.
        return build_mint_detail_lens(self, kind)

    def _mint_entity_modal_lens(self, title: str, original_kind: str | None = None):
        # Create/edit modals start from a pre-shaped lens so the modal UI can
        # focus on widgets instead of catalog lookups and JSON serialization.
        return build_mint_entity_modal_lens(self, title, original_kind)

    def _open_create_modal(self) -> None:
        open_entity_modal(self, "Create Mint Kind")

    def _open_edit_modal(self) -> None:
        if not require_selected_kind(self):
            return
        open_entity_modal(self, "Edit Mint Kind", self.selected_kind)

    def _remove_selected_kind(self) -> None:
        if not require_selected_kind(self):
            return
        if len(self.entity_definitions) <= 1:
            messagebox.showinfo("Remove Mint Kind", "At least one Mint kind must remain in the catalog.")
            return
        assert self.selected_kind is not None
        kind = self.selected_kind
        confirmed = messagebox.askyesno(
            "Remove Mint Kind",
            f"Remove Mint kind '{kind}' from the catalog?",
        )
        if not confirmed:
            return
        self.entity_definitions.pop(kind, None)
        self.entity_metadata.pop(kind, None)
        self.selected_kind = None
        self._save_catalog(f"Removed Mint kind '{kind}'")

    def _submit_entity_modal(
        self,
        original_kind: str | None,
        raw_name: str,
        raw_description: str,
        raw_rule_tags: list[str],
        raw_default_color: str,
        raw_valid_states: str,
        raw_allowed_actions: str,
        raw_invariant_rules: str,
        raw_initial_invariant_state: str,
        raw_action_transitions: str,
        status_var: tk.StringVar,
        modal: tk.Toplevel,
    ) -> None:
        valid, message, entry = sanitize_entity_definition(
            raw_name,
            raw_description,
            raw_rule_tags,
            raw_default_color,
            raw_valid_states,
            raw_allowed_actions,
            raw_invariant_rules,
            raw_initial_invariant_state,
            raw_action_transitions,
        )
        if not valid:
            status_var.set(message)
            modal.bell()
            return
        cleaned = entry["name"]
        if original_kind is None:
            if cleaned in self.entity_definitions:
                status_var.set("That Mint kind already exists.")
                modal.bell()
                return
            self.entity_definitions[cleaned] = palette_for_entity_name(cleaned)
        else:
            if cleaned != original_kind and cleaned in self.entity_definitions:
                status_var.set("That Mint kind already exists.")
                modal.bell()
                return
            palette = self.entity_definitions.pop(original_kind)
            self.entity_metadata.pop(original_kind, None)
            self.entity_definitions[cleaned] = palette
        self.entity_metadata[cleaned] = {
            "description": entry["description"],
            "rule_tag": entry["rule_tag"],
            "rule_tags": entry["rule_tags"],
            "default_color": entry["default_color"],
            "genome": entry["genome"],
        }
        self.selected_kind = cleaned
        self._save_catalog("Saved Mint catalog")
        modal.destroy()

    def _open_tag_manager_modal(self) -> None:
        open_tag_manager_modal(self)

    def _add_rule_tag(self, raw_name: str, refresh: object) -> None:
        normalized = " ".join(part for part in raw_name.strip().split() if part) or "none"
        if normalized in self.rule_tags:
            return
        self.rule_tags.append(normalized)
        self.rule_tags = sorted(dict.fromkeys(self.rule_tags), key=str.lower)
        self._save_catalog("Saved Mint catalog")
        refresh()

    def _rename_rule_tag(self, tag_list: tk.Listbox, raw_name: str, refresh: object) -> None:
        selection = tag_list.curselection()
        if not selection:
            messagebox.showinfo("Manage Tags", "Select a tag to rename.")
            return
        old_tag = tag_list.get(selection[0])
        new_tag = " ".join(part for part in raw_name.strip().split() if part) or "none"
        if new_tag == old_tag:
            return
        if new_tag in self.rule_tags:
            messagebox.showinfo("Manage Tags", "That tag already exists.")
            return
        self.rule_tags = [new_tag if tag == old_tag else tag for tag in self.rule_tags]
        self.rule_tags = sorted(dict.fromkeys(self.rule_tags), key=str.lower)
        for meta in self.entity_metadata.values():
            tags = [new_tag if tag == old_tag else tag for tag in _meta_rule_tags(meta)]
            meta["rule_tags"] = normalize_rule_tags(tags)
            meta["rule_tag"] = meta["rule_tags"][0]
        self._save_catalog("Saved Mint catalog")
        refresh()

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    MintCatalogEditor().run()


if __name__ == "__main__":
    main()
