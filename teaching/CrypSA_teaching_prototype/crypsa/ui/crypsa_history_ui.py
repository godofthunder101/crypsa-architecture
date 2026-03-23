from __future__ import annotations

import tkinter as tk
from typing import Any

from ..crypsa_teaching_theme import ACCENT, BG, MUTED, PANEL, TEXT


def _render_timeline_inspector(inspector_text: tk.Text, lines: list[str]) -> None:
    """Render the right-hand event inspector for the timeline modal."""

    inspector_text.configure(state="normal")
    inspector_text.delete("1.0", "end")
    inspector_text.insert("1.0", "\n".join(lines))
    inspector_text.configure(state="disabled")


def open_history_modal(app: Any) -> None:
    """Show canonical events as the primary substrate of truth."""

    modal = app._open_modal("Canonical Event History", "760x620")
    # History/Timeline now render lens data plus request objects. That keeps
    # the modal code focused on presentation while runtime selection logic
    # stays back in the controller.
    # Read the History modal in three layers: framing text, scrollable event
    # list, then one card per accepted event in reverse sequence order.
    tk.Label(modal, text="Canonical Event History", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text="Canonical history is the substrate of truth. This view shows all accepted canonical events across the current event graph. In this minimal prototype, lineage_parent drives replay while causal_references provide contextual links that can also influence invariant validation. Selecting an older event changes the viewed canonical state. Reconciling from there forks a new event lineage.",
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=700,
    ).pack(anchor="w", padx=18, pady=(0, 12))
    canvas = tk.Canvas(modal, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(modal, orient="vertical", command=canvas.yview)
    content = tk.Frame(canvas, bg=BG)
    content.bind("<Configure>", lambda _event, c=canvas: c.configure(scrollregion=c.bbox("all")))
    canvas.create_window((0, 0), window=content, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=(18, 0), pady=(0, 18))
    scrollbar.pack(side="right", fill="y", padx=(0, 18), pady=(0, 18))
    for lens in app._history_card_lenses():
        _history_card(app, content, lens, modal)


def _history_card(app: Any, parent: tk.Misc, lens: Any, modal: tk.Toplevel) -> None:
    """Render one accepted canonical event with lineage context."""

    card = tk.Frame(parent, bg=PANEL, highlightbackground="#243d6b", highlightthickness=1)
    card.pack(fill="x", pady=6)
    top = tk.Frame(card, bg=lens.header_fill)
    top.pack(fill="x")
    tk.Label(top, text=lens.header_text, bg=lens.header_fill, fg="#f8fafc", anchor="w", font=("Consolas", 10, "bold")).pack(side="left", padx=10, pady=8)
    tk.Button(top, text="Select", command=lambda req=lens.select_request, m=modal: app._execute_action_request(req, m), bg="#0f172a", fg=TEXT, activebackground="#1e293b", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 9), cursor="hand2").pack(side="right", padx=8, pady=5)
    if lens.is_on_active_lineage:
        tk.Label(top, text="ACTIVE LINEAGE", bg=lens.header_fill, fg="#a7f3d0", anchor="e", font=("Consolas", 9, "bold")).pack(side="right", padx=(0, 8), pady=5)
    # The body of each card mixes raw event details with lineage context so a
    # learner can answer both "what happened?" and "where does this event sit
    # in the currently viewed history?" from the same block.
    tk.Label(card, text="\n".join(lens.lines), bg=PANEL, fg=TEXT, justify="left", anchor="w", font=("Consolas", 10)).pack(fill="x", padx=10, pady=(10, 10))


def select_history_event(app: Any, event_id: str, preferred_branch_name: str | None, modal: tk.Toplevel) -> None:
    """Select a canonical event using the branch preference chosen by the adapter layer."""

    # The request already carries the preferred branch chosen during lens
    # translation, so this helper only applies that decision and redraws.
    app.selected_canonical_event_id = event_id
    if preferred_branch_name is not None:
        app.selected_branch = preferred_branch_name
    app._push_observer_log(f"canonical event selected -> {app._branch_label(app.selected_branch)} / {event_id}")
    modal.destroy()
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())


def open_timeline_modal(app: Any) -> None:
    """Show the human-facing event-lineage view derived from canonical history."""

    modal = app._open_modal("Canonical Timeline", "920x560")
    # Read the Timeline modal in four stages: title/legend, scrollable canvas,
    # right-hand inspector, then the click handler that syncs runtime
    # selection back into the main window.
    tk.Label(modal, text="Canonical Timeline", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text="Scrub canonical event lineage by event-lineage row. Selecting an older event changes the viewed canonical state. The highlighted lineage is the current fork target if you reconcile from a shared ancestor. Reconciling from there forks a new event lineage.",
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=860,
    ).pack(anchor="w", padx=18, pady=(0, 10))

    legend = tk.Frame(modal, bg=BG)
    legend.pack(fill="x", padx=18, pady=(0, 10))
    tk.Label(legend, text="Legend:", bg=BG, fg=ACCENT, font=("Consolas", 10, "bold")).pack(side="left")
    tk.Label(legend, text="active lineage", bg=BG, fg=ACCENT, font=("Consolas", 9)).pack(side="left", padx=(10, 12))
    tk.Label(legend, text="selected event", bg=BG, fg="#f8fafc", font=("Consolas", 9)).pack(side="left", padx=(0, 12))
    tk.Label(legend, text="branch head", bg=BG, fg="#67e8f9", font=("Consolas", 9)).pack(side="left", padx=(0, 12))
    tk.Label(legend, text="green=mint", bg=BG, fg="#86efac", font=("Consolas", 9)).pack(side="left", padx=(0, 12))
    tk.Label(legend, text="blue=build", bg=BG, fg="#93c5fd", font=("Consolas", 9)).pack(side="left", padx=(0, 12))
    tk.Label(legend, text="red=destroy", bg=BG, fg="#fca5a5", font=("Consolas", 9)).pack(side="left")

    shell = tk.Frame(modal, bg=BG)
    shell.pack(fill="both", expand=True, padx=18, pady=(0, 10))
    shell.columnconfigure(0, weight=1)
    shell.columnconfigure(1, weight=0)
    shell.rowconfigure(0, weight=1)

    timeline_shell = tk.Frame(shell, bg=BG)
    timeline_shell.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
    timeline_shell.rowconfigure(0, weight=1)
    timeline_shell.columnconfigure(0, weight=1)

    canvas = tk.Canvas(timeline_shell, bg="#0b1326", highlightthickness=1, highlightbackground="#243d6b")
    hbar = tk.Scrollbar(timeline_shell, orient="horizontal", command=canvas.xview)
    vbar = tk.Scrollbar(timeline_shell, orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    vbar.grid(row=0, column=1, sticky="ns")
    hbar.grid(row=1, column=0, sticky="ew")

    inspector = tk.Frame(shell, bg=PANEL, highlightbackground="#243d6b", highlightthickness=1, width=240)
    inspector.grid(row=0, column=1, sticky="ns")
    inspector.grid_propagate(False)
    inspector.columnconfigure(0, weight=1)
    tk.Label(inspector, text="Event Inspector", bg=PANEL, fg=TEXT, font=("Segoe UI Semibold", 14), anchor="w").grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 8))
    inspector_text = tk.Text(inspector, bg="#0b1326", fg=TEXT, insertbackground=TEXT, relief="flat", wrap="word", font=("Consolas", 10), width=28, height=22)
    inspector_text.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))
    inspector.rowconfigure(1, weight=1)

    row_h = 72
    left_pad = 170
    top_pad = 36
    event_gap = 86
    radius = 10
    active_lineage_var = tk.StringVar(value="")
    row_map: dict[str, Any] = {}

    def render_timeline(lens: Any) -> None:
        # Re-render the open modal from a fresh lens after selection changes so
        # the canvas highlights, active-lineage label, and inspector all stay
        # in sync with the main window's current history selection.
        nonlocal row_map
        rows = lens.rows
        positions: dict[tuple[str, str], tuple[float, float]] = {}
        row_map = {row.branch_name: row for row in rows}
        canvas.delete("all")
        max_events = max((len(row.nodes) for row in rows), default=0)
        content_w = max(760, left_pad + max(1, max_events) * event_gap + 160)
        content_h = max(320, top_pad + len(rows) * row_h + 60)
        canvas.configure(scrollregion=(0, 0, content_w, content_h))

        for row_index, row in enumerate(rows):
            y = top_pad + row_index * row_h
            canvas.create_text(24, y, text=row.branch_label, anchor="w", fill=row.row_color, font=("Consolas", 12, "bold" if row.is_selected_branch else "normal"))
            if row.parent_label is not None:
                canvas.create_text(24, y + 18, text=f"from {row.parent_label}", anchor="w", fill=(ACCENT if row.is_selected_branch else MUTED), font=("Consolas", 9))
            canvas.create_line(left_pad - 30, y, content_w - 40, y, fill=row.line_color, width=(3 if row.is_selected_branch else 2))
            for event_index, node in enumerate(row.nodes):
                x = left_pad + event_index * event_gap
                positions[(row.branch_name, node.event_id)] = (x, y)
                canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=node.fill, outline=node.outline, width=node.outline_width, tags=(f"event:{node.event_id}", f"branch:{row.branch_name}"))
                canvas.create_text(x, y - 18, text=node.sequence_text, fill=(ACCENT if row.is_selected_branch else TEXT), font=("Consolas", 8))
                canvas.create_text(x, y + 20, text=node.event_type_text, fill=(ACCENT if row.is_selected_branch else MUTED), font=("Consolas", 7), justify="center")

        for row in rows:
            origin = row.connector_origin
            if origin is None:
                continue
            parent_name, fork_event_id = origin
            parent_pos = positions.get((parent_name, fork_event_id))
            if parent_pos is None or not row.nodes:
                continue
            target_event_id = row.connector_target_event_id or row.nodes[0].event_id
            child_pos = positions.get((row.branch_name, target_event_id))
            if child_pos is None:
                continue
            connector_color = ACCENT if row.is_selected_branch else "#67e8f9"
            canvas.create_line(parent_pos[0], parent_pos[1], child_pos[0], child_pos[1], fill=connector_color, width=2, dash=(5, 4))

        _render_timeline_inspector(inspector_text, lens.inspector_lines)
        active_lineage_var.set(f"Active lineage for reconciliation: {lens.active_lineage_label}")

    def on_click(_event: tk.Event) -> None:
        current = canvas.find_withtag("current")
        if not current:
            return
        tags = canvas.gettags(current[0])
        selected_branch = None
        selected_event = None
        for tag in tags:
            if tag.startswith("branch:"):
                selected_branch = tag.split(":", 1)[1]
            if tag.startswith("event:"):
                selected_event = tag.split(":", 1)[1]
        if selected_branch and selected_event:
            row = row_map.get(selected_branch)
            if row is None:
                return
            node_request = None
            for node in row.nodes:
                if node.event_id == selected_event:
                    node_request = node.select_request
                    break
            if node_request is None:
                return
            app._execute_action_request(node_request)
            app._push_observer_log(f"canonical timeline selection -> {app._branch_label(app.selected_branch)} / {app.selected_canonical_event_id}")
            render_timeline(app._timeline_modal_lens())
            app._draw_scene(app.root.winfo_width(), app.root.winfo_height())

    canvas.bind("<Button-1>", on_click)
    render_timeline(app._timeline_modal_lens())

    actions = tk.Frame(modal, bg=BG)
    actions.pack(fill="x", padx=18, pady=(0, 18))
    tk.Label(actions, textvariable=active_lineage_var, bg=BG, fg=ACCENT, font=("Segoe UI", 10), anchor="w").pack(side="left")
    tk.Button(actions, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left")
    tk.Button(actions, text="Center Observer View Near Canonical State", command=lambda: app._execute_action_request(app._timeline_modal_lens().recenter_request), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="right")
