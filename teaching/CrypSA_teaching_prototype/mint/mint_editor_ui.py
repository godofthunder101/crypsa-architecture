from __future__ import annotations

import json
import tkinter as tk
from tkinter import messagebox
from typing import Any

from .mint_catalog_store import (
    MINT_ENTITY_DEFAULT_COLORS,
    build_beacon_default_genome,
    build_default_genome,
    normalize_hex_color,
)


def create_popup(app: Any, title: str, geometry: str) -> tk.Toplevel:
    """Create a standard modal shell for Mint editor workflows."""

    modal = tk.Toplevel(app.root)
    modal.title(title)
    modal.configure(bg=app.BG)
    modal.transient(app.root)
    modal.grab_set()
    modal.bind("<Escape>", lambda _event: modal.destroy())
    requested_width, requested_height = (int(part) for part in geometry.lower().split("x", 1))
    screen_width = modal.winfo_screenwidth()
    screen_height = modal.winfo_screenheight()
    width = min(requested_width, max(720, screen_width - 120))
    height = min(requested_height, max(560, screen_height - 120))
    x = max(40, (screen_width - width) // 2)
    y = max(40, (screen_height - height) // 2)
    modal.geometry(f"{width}x{height}+{x}+{y}")
    modal.minsize(min(width, 680), min(height, 560))
    return modal


def labeled_entry(app: Any, parent: tk.Misc, label: str, value: str) -> tk.Entry:
    """Render a labeled single-line field using the Mint editor palette."""

    tk.Label(parent, text=label, bg=app.BG, fg=app.ACCENT, font=("Consolas", 10), anchor="w").pack(fill="x", pady=(0, 4))
    entry = tk.Entry(parent, bg="#101938", fg=app.TEXT, insertbackground=app.TEXT, relief="flat", font=("Consolas", 11))
    entry.pack(fill="x", pady=(0, 12))
    if value:
        entry.insert(0, value)
    return entry


def labeled_textbox(app: Any, parent: tk.Misc, label: str, value: str, height: int) -> tk.Text:
    """Render a labeled multiline field using the Mint editor palette."""

    tk.Label(parent, text=label, bg=app.BG, fg=app.ACCENT, font=("Consolas", 10), anchor="w").pack(fill="x", pady=(0, 4))
    text = tk.Text(parent, bg="#101938", fg=app.TEXT, insertbackground=app.TEXT, relief="flat", font=("Consolas", 10), height=height, wrap="word")
    text.pack(fill="x", pady=(0, 12))
    if value:
        text.insert("1.0", value)
    return text


def build_color_swatch_grid(app: Any, parent: tk.Misc, color_var: tk.StringVar) -> None:
    """Render the fixed prototype color palette used by Mint kinds."""

    shell = tk.Frame(parent, bg=app.BG)
    shell.pack(fill="x", pady=(0, 12))
    for index, color_hex in enumerate(MINT_ENTITY_DEFAULT_COLORS):
        row = index // 8
        col = index % 8
        swatch = tk.Radiobutton(
            shell,
            variable=color_var,
            value=color_hex,
            text="",
            width=2,
            indicatoron=False,
            selectcolor=color_hex,
            bg=color_hex,
            activebackground=color_hex,
            relief="flat",
            bd=1,
            padx=0,
            pady=8,
            cursor="hand2",
        )
        swatch.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)


def _build_scrollable_modal_body(app: Any, modal: tk.Toplevel) -> tuple[tk.Frame, tk.Frame]:
    """Build the two-column scrollable body used by the Mint kind editor."""

    shell = tk.Frame(modal, bg=app.BG)
    shell.pack(fill="both", expand=True, padx=20, pady=(0, 0))
    shell.rowconfigure(0, weight=1)
    shell.columnconfigure(0, weight=1)

    canvas = tk.Canvas(shell, bg=app.BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(shell, orient="vertical", command=canvas.yview)
    body = tk.Frame(canvas, bg=app.BG)
    body.bind("<Configure>", lambda _event, c=canvas: c.configure(scrollregion=c.bbox("all")))
    canvas.create_window((0, 0), window=body, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")
    body.columnconfigure(0, weight=1)
    body.columnconfigure(1, weight=1)

    left = tk.Frame(body, bg=app.BG)
    left.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
    right = tk.Frame(body, bg=app.BG)
    right.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
    return left, right


def _build_tag_selector(app: Any, parent: tk.Misc, tag_vars: list[tk.StringVar]) -> None:
    """Render the editable list of tag dropdown rows for a Mint kind."""

    tk.Label(parent, text="Rule Tags", bg=app.BG, fg=app.ACCENT, font=("Consolas", 10), anchor="w").pack(fill="x", pady=(0, 4))
    tags_frame = tk.Frame(parent, bg=app.BG)
    tags_frame.pack(fill="x", pady=(0, 12))

    def render_tag_rows() -> None:
        for child in tags_frame.winfo_children():
            child.destroy()
        for index, tag_var in enumerate(tag_vars):
            row = tk.Frame(tags_frame, bg=app.BG)
            row.pack(fill="x", pady=2)
            option = tk.OptionMenu(row, tag_var, *app.rule_tags)
            option.configure(bg="#101938", fg=app.TEXT, activebackground="#24304f", activeforeground=app.TEXT, relief="flat", font=("Consolas", 10), highlightthickness=0)
            option["menu"].configure(bg="#101938", fg=app.TEXT, activebackground="#24304f", activeforeground=app.TEXT, font=("Consolas", 10))
            option.pack(side="left", fill="x", expand=True)
            tk.Button(row, text="-", command=lambda selected=index: remove_tag(selected), bg="#24304f", fg=app.TEXT, activebackground="#34508a", activeforeground=app.TEXT, relief="flat", cursor="hand2").pack(side="left", padx=(8, 0))

    def add_tag() -> None:
        tag_vars.append(tk.StringVar(value="none"))
        render_tag_rows()

    def remove_tag(index: int) -> None:
        if len(tag_vars) > 1:
            tag_vars.pop(index)
        else:
            tag_vars[0].set("none")
        render_tag_rows()

    render_tag_rows()
    tk.Button(parent, text="+ Tag", command=add_tag, bg="#24304f", fg=app.TEXT, activebackground="#34508a", activeforeground=app.TEXT, relief="flat", cursor="hand2").pack(anchor="w", pady=(0, 12))


def _build_genome_editor(app: Any, parent: tk.Misc, genome: dict[str, object]) -> dict[str, tk.Text]:
    """Render the advanced JSON genome editor and return its text widgets."""

    genome_card = tk.Frame(parent, bg=app.PANEL, highlightbackground="#24304f", highlightthickness=1)
    genome_card.pack(fill="both", expand=True)
    tk.Label(genome_card, text="Genome (Advanced JSON)", bg=app.PANEL, fg=app.ACCENT, font=("Consolas", 12, "bold"), anchor="w").pack(fill="x", padx=12, pady=(12, 6))
    tk.Label(
        genome_card,
        text=(
            "Edit the deterministic genome directly. These fields define valid states,\n"
            "allowed actions, transition rules, and invariant checks for future canonical events."
        ),
        bg=app.PANEL,
        fg=app.MUTED,
        justify="left",
        wraplength=300,
        anchor="w",
        font=("Segoe UI", 10),
    ).pack(fill="x", padx=12, pady=(0, 12))
    tk.Label(
        genome_card,
        text=(
            "Quick guide:\n"
            "Valid States = the names this Mint can be in.\n"
            "Allowed Actions = which actions the runtime may ask of it.\n"
            "Action Transitions = how each action changes state.\n"
            "Invariant Rules = extra acceptance checks, such as occupancy or context requirements.\n"
            "Initial Invariant State = the starting structured state for future accepted objects."
        ),
        bg=app.PANEL,
        fg=app.MUTED,
        justify="left",
        wraplength=300,
        anchor="w",
        font=("Segoe UI", 9),
    ).pack(fill="x", padx=12, pady=(0, 12))
    tk.Label(
        genome_card,
        text=(
            "Suggested starting points:\n"
            "Default Structure = normal buildable object.\n"
            "Beacon Example = context-sensitive teaching example."
        ),
        bg=app.PANEL,
        fg="#cbd5e1",
        justify="left",
        wraplength=300,
        anchor="w",
        font=("Segoe UI", 9),
    ).pack(fill="x", padx=12, pady=(0, 12))

    genome_fields = tk.Frame(genome_card, bg=app.PANEL)
    genome_fields.pack(fill="both", expand=True, padx=12, pady=(0, 12))
    fields = {
        "valid_states": labeled_textbox(app, genome_fields, "Valid States JSON", json.dumps(genome["valid_states"], indent=2), 4),
        "allowed_actions": labeled_textbox(app, genome_fields, "Allowed Actions JSON", json.dumps(genome["allowed_actions"], indent=2), 4),
        "action_transitions": labeled_textbox(app, genome_fields, "Action Transitions JSON", json.dumps(genome["action_transitions"], indent=2), 10),
        "invariant_rules": labeled_textbox(app, genome_fields, "Invariant Rules JSON", json.dumps(genome["invariant_rules"], indent=2), 10),
        "initial_invariant_state": labeled_textbox(app, genome_fields, "Initial Invariant State JSON", json.dumps(genome["initial_invariant_state"], indent=2), 5),
    }
    preset_row = tk.Frame(genome_card, bg=app.PANEL)
    preset_row.pack(fill="x", padx=12, pady=(0, 12))

    def apply_genome_preset(preset_genome: dict[str, object]) -> None:
        mapping = {
            "valid_states": preset_genome["valid_states"],
            "allowed_actions": preset_genome["allowed_actions"],
            "action_transitions": preset_genome["action_transitions"],
            "invariant_rules": preset_genome["invariant_rules"],
            "initial_invariant_state": preset_genome["initial_invariant_state"],
        }
        for key, value in mapping.items():
            fields[key].delete("1.0", "end")
            fields[key].insert("1.0", json.dumps(value, indent=2))

    tk.Label(preset_row, text="Presets:", bg=app.PANEL, fg=app.MUTED, font=("Segoe UI", 9)).pack(side="left")
    tk.Button(
        preset_row,
        text="Default Structure",
        command=lambda: apply_genome_preset(build_default_genome()),
        bg="#24304f",
        fg=app.TEXT,
        activebackground="#34508a",
        activeforeground=app.TEXT,
        relief="flat",
        cursor="hand2",
    ).pack(side="left", padx=(8, 8))
    tk.Button(
        preset_row,
        text="Beacon Example",
        command=lambda: apply_genome_preset(build_beacon_default_genome()),
        bg="#24304f",
        fg=app.TEXT,
        activebackground="#34508a",
        activeforeground=app.TEXT,
        relief="flat",
        cursor="hand2",
    ).pack(side="left")
    return fields


def open_entity_modal(app: Any, title: str, original_kind: str | None = None) -> None:
    """Open the Mint kind editor for creating or editing one deterministic Mint."""

    modal = create_popup(app, title, "820x680")
    lens = app._mint_entity_modal_lens(title, original_kind)
    genome = {
        "valid_states": json.loads(lens.genome_json_fields["valid_states"]),
        "allowed_actions": json.loads(lens.genome_json_fields["allowed_actions"]),
        "action_transitions": json.loads(lens.genome_json_fields["action_transitions"]),
        "invariant_rules": json.loads(lens.genome_json_fields["invariant_rules"]),
        "initial_invariant_state": json.loads(lens.genome_json_fields["initial_invariant_state"]),
    }

    header = tk.Frame(modal, bg=app.BG)
    header.pack(fill="x", padx=20, pady=(16, 10))
    header.columnconfigure(0, weight=1)
    tk.Label(header, text=lens.title, bg=app.BG, fg=app.TEXT, font=("Segoe UI Semibold", 18), anchor="w").grid(row=0, column=0, sticky="w")
    status_var = tk.StringVar(value="")
    tk.Label(header, textvariable=status_var, bg=app.BG, fg=app.ACCENT, font=("Segoe UI", 10), anchor="w", justify="left", wraplength=520).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 0))

    # The modal is split into "identity and tags" on the left and "genome"
    # on the right so readers can separate descriptive metadata from the
    # structured behavior definition.
    left, right = _build_scrollable_modal_body(app, modal)

    name_entry = labeled_entry(app, left, "Kind Name", lens.name_value)
    desc_entry = labeled_entry(app, left, "Description", lens.description_value)
    if lens.quick_start_text is not None:
        tk.Label(
            left,
            text=lens.quick_start_text,
            bg=app.BG,
            fg=app.MUTED,
            justify="left",
            wraplength=320,
            font=("Segoe UI", 9),
        ).pack(fill="x", pady=(0, 12))
    tag_vars = [tk.StringVar(value=tag) for tag in lens.rule_tags] or [tk.StringVar(value="none")]
    _build_tag_selector(app, left, tag_vars)

    tk.Label(left, text="Default Color", bg=app.BG, fg=app.ACCENT, font=("Consolas", 10), anchor="w").pack(fill="x", pady=(0, 6))
    color_var = tk.StringVar(value=lens.default_color)
    build_color_swatch_grid(app, left, color_var)

    genome_fields = _build_genome_editor(app, right, genome)
    app._action_button(
        header,
        "Save",
        lambda: app._submit_entity_modal(
            original_kind,
            name_entry.get(),
            desc_entry.get(),
            [tag_var.get() for tag_var in tag_vars],
            color_var.get(),
            genome_fields["valid_states"].get("1.0", "end").strip(),
            genome_fields["allowed_actions"].get("1.0", "end").strip(),
            genome_fields["invariant_rules"].get("1.0", "end").strip(),
            genome_fields["initial_invariant_state"].get("1.0", "end").strip(),
            genome_fields["action_transitions"].get("1.0", "end").strip(),
            status_var,
            modal,
        ),
    ).grid(row=0, column=1, sticky="e")


def open_tag_manager_modal(app: Any) -> None:
    """Open the tag manager used for Mint annotations."""

    modal = create_popup(app, "Manage Tags", "420x440")
    tk.Label(modal, text="Manage Tags", bg=app.BG, fg=app.TEXT, font=("Segoe UI Semibold", 18), anchor="w").pack(fill="x", padx=20, pady=(18, 8))
    tk.Label(modal, text="Tags are Mint annotations. They help categorize kinds but do not replace genome rules.", bg=app.BG, fg=app.MUTED, font=("Segoe UI", 10), justify="left", wraplength=340).pack(fill="x", padx=20, pady=(0, 12))

    list_frame = tk.Frame(modal, bg=app.BG)
    list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 12))
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")
    tag_list = tk.Listbox(list_frame, bg="#101938", fg=app.TEXT, selectbackground="#24304f", selectforeground=app.TEXT, relief="flat", font=("Consolas", 10), exportselection=False, yscrollcommand=scrollbar.set)
    tag_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=tag_list.yview)

    def refresh_tags() -> None:
        tag_list.delete(0, "end")
        for tag in app.rule_tags:
            tag_list.insert("end", tag)

    refresh_tags()
    entry = labeled_entry(app, modal, "Tag Name", "")
    actions = tk.Frame(modal, bg=app.BG)
    actions.pack(pady=(0, 18))
    app._action_button(actions, "Add Tag", lambda: app._add_rule_tag(entry.get(), refresh_tags)).pack(side="left", padx=6)
    app._action_button(actions, "Rename Tag", lambda: app._rename_rule_tag(tag_list, entry.get(), refresh_tags)).pack(side="left", padx=6)


def require_selected_kind(app: Any) -> bool:
    """Prompt if edit was requested without a selected Mint kind."""

    if app.selected_kind is None:
        messagebox.showinfo("Mint Editor", "Select a Mint kind to edit.")
        return False
    return True
