from __future__ import annotations

import tkinter as tk
from typing import Any

from ..crypsa_lens_adapters import CanonicalPaneLens, ObserverPaneLens, GridLens
from ..crypsa_teaching_theme import ACCENT, BG, CARD, GOOD, MUTED, PANEL, TEXT, WARN


def add_widget(app: Any, x: float, y: float, widget: tk.Widget, anchor: str = "nw") -> None:
    """Attach a Tk widget to the canvas-backed teaching layout."""

    app.widgets.append(widget)
    app.canvas.create_window(x, y, anchor=anchor, window=widget)


def make_button(app: Any, label: str, command: object) -> tk.Button:
    """Create the shared bordered action button style used across the main window."""

    return tk.Button(
        app.root,
        text=label,
        command=command,
        bg="#1f3357",
        fg=TEXT,
        activebackground="#29467a",
        activeforeground=TEXT,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#33578f",
        highlightcolor=ACCENT,
        font=("Segoe UI", 10),
        padx=10,
        pady=5,
        cursor="hand2",
    )


def add_button_row(app: Any, center_x: float, y: float, buttons: list[tuple[str, object]], spacing: float = 108) -> None:
    """Place a row of buttons centered around a shared x position."""

    offset_origin = (len(buttons) - 1) / 2
    for index, (label, command) in enumerate(buttons):
        x = center_x + (index - offset_origin) * spacing
        add_widget(app, x, y, make_button(app, label, command), anchor="n")


def fitted_button_spacing(inner_width: float, button_count: int, preferred: float, min_spacing: float = 92) -> float:
    """Keep centered button rows inside narrow panes without hard clipping."""

    if button_count <= 1:
        return preferred
    max_spacing = (inner_width - 140) / (button_count - 1)
    return max(min_spacing, min(preferred, max_spacing))


def draw_scene(app: Any, width: int, height: int) -> None:
    """Redraw the full two-pane teaching layout from current runtime state."""

    app.canvas.delete("all")
    app.canvas.configure(width=width, height=height)
    app._clear_widgets()
    app.canvas.create_rectangle(0, 0, width, height, fill=BG, outline="")
    app.canvas.create_oval(-160, -140, width * 0.42, height * 0.58, fill="#0d1730", outline="")
    app.canvas.create_oval(width * 0.56, height * 0.12, width + 200, height + 150, fill="#101630", outline="")
    app.canvas.create_polygon(
        width * 0.08,
        height * 0.10,
        width * 0.24,
        height * 0.04,
        width * 0.36,
        height * 0.18,
        width * 0.18,
        height * 0.24,
        fill="#0c1a33",
        outline="",
        smooth=True,
    )
    app.canvas.create_polygon(
        width * 0.70,
        height * 0.78,
        width * 0.88,
        height * 0.70,
        width * 0.96,
        height * 0.90,
        width * 0.76,
        height * 0.96,
        fill="#0b1830",
        outline="",
        smooth=True,
    )
    gap = 20
    margin = 28
    pane_w = (width - margin * 2 - gap) / 2
    pane_h = height - margin * 2
    draw_server_pane(app, margin, margin, pane_w, pane_h)
    draw_observer_pane(app, margin + pane_w + gap, margin, pane_w, pane_h)
    add_widget(app, width - 294, height - 42, make_button(app, "Hotkeys", app._open_hotkeys_modal))
    add_widget(app, width - 180, height - 42, make_button(app, "Model Notes", app._open_model_notes_modal))


def draw_pane_shell(app: Any, x: float, y: float, w: float, h: float, title: str) -> tuple[float, float, float, float]:
    """Draw the shared pane framing used by observer and canonical views."""

    app.canvas.create_rectangle(x + 6, y + 10, x + w + 6, y + h + 10, fill="#08101f", outline="")
    app.canvas.create_rectangle(x, y, x + w, y + h, fill=PANEL, outline="#203052", width=2)
    app.canvas.create_rectangle(x + 18, y + 16, x + 228, y + 46, fill="#132847", outline="#32557f", width=1)
    app.canvas.create_oval(x + w - 96, y + 14, x + w - 26, y + 42, fill="#10223e", outline="#294c73", width=1)
    app.canvas.create_text(x + w - 61, y + 28, text="Live View", anchor="c", fill="#b6d7ff", font=("Segoe UI", 8, "bold"))
    app.canvas.create_text(x + 32, y + 31, text=title, anchor="w", fill=TEXT, font=("Segoe UI Semibold", 18))
    subtitle = ""
    if title == "Canonical Representation":
        subtitle = "the shared world story the model has accepted"
    elif title == "Observer Representation":
        subtitle = "your local sandbox before the world agrees"
    if subtitle:
        app.canvas.create_text(x + 32, y + 54, text=subtitle, anchor="w", fill=MUTED, font=("Segoe UI", 9, "italic"))
    app.canvas.create_line(x + 18, y + 66, x + w - 18, y + 66, fill="#203052", width=1)
    app.canvas.create_rectangle(x + 18, y + 74, x + w - 18, y + h - 18, fill=CARD, outline="#243d6b", width=2)
    return x + 18, y + 74, x + w - 18, y + h - 18


def _draw_summary_rows(
    app: Any,
    inner_x1: float,
    start_y: float,
    summary: list[tuple[str, str]],
    value_color_by_label: dict[str, str] | None = None,
) -> float:
    """Draw a two-column pane summary and return the next free y position."""

    value_color_by_label = value_color_by_label or {}
    row_y = start_y
    for label, value in summary:
        app.canvas.create_text(inner_x1 + 18, row_y, text=label, anchor="w", fill=ACCENT, font=("Consolas", 10, "bold"))
        app.canvas.create_text(
            inner_x1 + 170,
            row_y,
            text=value,
            anchor="w",
            fill=value_color_by_label.get(label, TEXT),
            font=("Consolas", 10),
        )
        row_y += 24
    return row_y


def _draw_canonical_banner(app: Any, lens: CanonicalPaneLens, inner_x1: float, inner_x2: float, inner_y1: float) -> None:
    """Draw the top-right canonical status banner that explains the current teaching state."""

    if lens.banner is None:
        return
    banner_width = min(max(244, len(lens.banner.text) * 6 + 34), 336)
    app.canvas.create_rectangle(inner_x2 - banner_width, inner_y1 - 18, inner_x2 - 18, inner_y1 + 4, fill=lens.banner.fill, outline=lens.banner.outline, width=1)
    app.canvas.create_text(inner_x2 - 30, inner_y1 - 7, text=lens.banner.text, anchor="e", fill=lens.banner.text_color, font=("Consolas", 9, "bold"))


def draw_server_pane(app: Any, x: float, y: float, w: float, h: float) -> None:
    """Render replay-derived canonical state and canonical navigation tools."""

    inner_x1, inner_y1, inner_x2, inner_y2 = draw_pane_shell(app, x, y, w, h, "Canonical Representation")
    # Read the canonical pane in three stages: summarize the currently viewed
    # lineage, show the state banner, then draw the replay-derived grid and
    # controls beneath it.
    lens = app._canonical_pane_lens()
    row_y = _draw_summary_rows(app, inner_x1, inner_y1 + 18, lens.summary_rows)
    _draw_canonical_banner(app, lens, inner_x1, inner_x2, inner_y1)
    draw_grid(app, inner_x1 + 18, row_y + 18, inner_x2 - 18, inner_y2 - 130, lens.grid)
    controls_y = inner_y2 - 86
    center_x = (inner_x1 + inner_x2) / 2
    button_spacing = fitted_button_spacing(inner_x2 - inner_x1, 3, 108)
    add_button_row(
        app,
        center_x,
        controls_y,
        [
            ("History", app._open_history_modal),
            ("Timeline", app._open_timeline_modal),
            ("Mint", app._open_mint_modal),
        ],
        spacing=button_spacing,
    )
    add_button_row(
        app,
        center_x,
        controls_y + 40,
        [
            ("Pane Help", app._open_canonical_pane_help_modal),
            ("How To Read", app._open_teaching_modal),
            ("Walkthrough", app._open_walkthrough_modal),
        ],
        spacing=button_spacing,
    )


def draw_observer_pane(app: Any, x: float, y: float, w: float, h: float) -> None:
    """Render observer-local state and invariant-boundary submission controls."""

    inner_x1, inner_y1, inner_x2, inner_y2 = draw_pane_shell(app, x, y, w, h, "Observer Representation")
    # Read the observer pane in the same layered order as the runtime model:
    # local state summary first, then context-sensitive hints, then the grid
    # and action controls that cross the invariant boundary.
    lens = app._observer_pane_lens()
    row_y = _draw_summary_rows(app, inner_x1, inner_y1 + 18, lens.summary_rows, lens.summary_value_colors)
    if lens.divergence_banner is not None:
        app.canvas.create_rectangle(inner_x2 - 282, inner_y1 - 18, inner_x2 - 18, inner_y1 + 4, fill=lens.divergence_banner.fill, outline=lens.divergence_banner.outline, width=1)
        app.canvas.create_text(inner_x2 - 30, inner_y1 - 7, text=lens.divergence_banner.text, anchor="e", fill=lens.divergence_banner.text_color, font=("Consolas", 9, "bold"))
    if lens.context_hint is not None:
        app.canvas.create_text(inner_x1 + 18, row_y + 8, text=lens.context_hint, anchor="w", fill="#fde68a", font=("Segoe UI", 9), width=(inner_x2 - inner_x1 - 36))
        grid_top = row_y + 38
    else:
        grid_top = row_y + 18
    draw_grid(app, inner_x1 + 18, grid_top, inner_x2 - 18, inner_y2 - 162, lens.grid)
    toggle_var = tk.BooleanVar(value=lens.auto_reconcile_enabled)
    checkbox = tk.Checkbutton(
        app.root,
        text="Auto-submit invariant-boundary candidates",
        variable=toggle_var,
        command=lambda var=toggle_var: app._set_auto_reconcile(var.get()),
        bg=CARD,
        fg=MUTED,
        activebackground=CARD,
        activeforeground=TEXT,
        selectcolor="#15233d",
        highlightthickness=0,
        bd=0,
        cursor="hand2",
    )
    add_widget(app, inner_x1 + 18, inner_y2 - 142, checkbox)
    app.canvas.create_text(inner_x1 + 42, inner_y2 - 120, text=lens.auto_reconcile_help_text, anchor="w", fill=MUTED, font=("Segoe UI", 9))
    app.canvas.create_text(inner_x1 + 18, inner_y2 - 102, text=lens.beacon_prompt, anchor="w", fill="#fde68a", font=("Segoe UI", 9), width=(inner_x2 - inner_x1 - 36))
    observer_controls_y = inner_y2 - 86
    observer_center_x = (inner_x1 + inner_x2) / 2
    observer_button_spacing = fitted_button_spacing(inner_x2 - inner_x1, 3, 108)
    add_button_row(
        app,
        observer_center_x,
        observer_controls_y,
        [
            ("Build", app._open_build_modal),
            ("Destroy", app._queue_destroy_candidate),
            ("Reconcile", app._reconcile_invariant_boundary_candidates),
        ],
        spacing=observer_button_spacing,
    )
    add_button_row(
        app,
        observer_center_x,
        observer_controls_y + 40,
        [
            ("Candidates", app._open_candidate_modal),
            ("Try Beacon", app._try_beacon_path),
            ("Pane Help", app._open_observer_pane_help_modal),
        ],
        spacing=fitted_button_spacing(inner_x2 - inner_x1, 3, 108),
    )


def draw_grid(
    app: Any,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    lens: GridLens,
) -> None:
    """Draw the shared grid view for canonical and observer representations."""

    app.canvas.create_rectangle(x1, y1, x2, y2, fill="#0b1326", outline="#315286", width=2)
    cell_w = (x2 - x1) / lens.grid_size
    cell_h = (y2 - y1) / lens.grid_size
    for gy in range(lens.grid_size):
        for gx in range(lens.grid_size):
            tx1 = x1 + gx * cell_w
            ty1 = y1 + gy * cell_h
            tx2 = tx1 + cell_w
            ty2 = ty1 + cell_h
            fill = "#0e1730"
            outline = "#1f3357"
            if (gx, gy) in lens.reserved_tiles:
                fill = "#2b1221"
                outline = "#6b2137"
            app.canvas.create_rectangle(tx1, ty1, tx2, ty2, fill=fill, outline=outline)
    target_tile = lens.target_tile
    if target_tile is not None:
        # The observer pane always shows the current invariant-boundary target
        # so canonical submissions are visually unambiguous before reconciliation.
        tx1 = x1 + target_tile[0] * cell_w
        ty1 = y1 + target_tile[1] * cell_h
        tx2 = tx1 + cell_w
        ty2 = ty1 + cell_h
        app.canvas.create_rectangle(tx1 + 2, ty1 + 2, tx2 - 2, ty2 - 2, outline="#facc15", width=3, dash=(4, 3))
        app.canvas.create_text((tx1 + tx2) / 2, ty1 + 10, text="TARGET", fill="#fde68a", font=("Consolas", 7, "bold"))
    for obj in lens.objects.values():
        definition = dict(obj.minted_definition)
        palette = definition["palette"]
        ox1 = x1 + obj.x * cell_w + cell_w * 0.18
        oy1 = y1 + obj.y * cell_h + cell_h * 0.18
        ox2 = ox1 + cell_w * 0.64
        oy2 = oy1 + cell_h * 0.64
        app.canvas.create_oval(ox1, oy1, ox2, oy2, fill=palette[0], outline=palette[1], width=2)
        app.canvas.create_text((ox1 + ox2) / 2, oy2 + 7, text=obj.kind[:1], fill=TEXT, font=("Consolas", 8, "bold"))
    if lens.observer_position is not None:
        px1 = x1 + lens.observer_position[0] * cell_w + cell_w * 0.22
        py1 = y1 + lens.observer_position[1] * cell_h + cell_h * 0.22
        px2 = px1 + cell_w * 0.56
        py2 = py1 + cell_h * 0.56
        app.canvas.create_rectangle(px1, py1, px2, py2, fill="#38bdf8", outline="#bae6fd", width=2)
