from __future__ import annotations

import tkinter as tk
from typing import Any, Callable

# This module is the Tk-only shell boundary.
# Keep runtime meaning out of here:
# - this file wires windows, modals, focus checks, and hotkeys
# - the controller still decides what each action does
# - this is part of a completed teaching artifact, not a production UI shell
#
# Reading tip:
# 1. root creation
# 2. hotkey binding
# 3. modal shell creation
# 4. widget/hotkey lifecycle helpers


def create_root_window(
    *,
    title: str,
    width: int,
    height: int,
    min_width: int,
    min_height: int,
    background: str,
) -> tk.Tk:
    """Create the shared Tk root window used by the teaching prototype."""

    root = tk.Tk()
    root.title(title)
    root.geometry(f"{width}x{height}")
    root.minsize(min_width, min_height)
    root.configure(bg=background)
    return root


def bind_main_window_hotkeys(app: Any) -> None:
    """Attach the shared main-window hotkeys to one teaching app instance."""

    # The hotkeys stay listed here so a reader can scan all main-window input
    # bindings in one place without also reading runtime mutation details.
    app.root.bind("<Configure>", app._on_resize)
    app.root.bind("<Escape>", lambda _event: app._handle_escape())
    app.root.bind_all("<KeyPress-w>", lambda _event: app._run_main_window_hotkey(lambda: app._move_observer_locally(0, -1, "north")))
    app.root.bind_all("<KeyPress-s>", lambda _event: app._run_main_window_hotkey(lambda: app._move_observer_locally(0, 1, "south")))
    app.root.bind_all("<KeyPress-a>", lambda _event: app._run_main_window_hotkey(lambda: app._move_observer_locally(-1, 0, "west")))
    app.root.bind_all("<KeyPress-d>", lambda _event: app._run_main_window_hotkey(lambda: app._move_observer_locally(1, 0, "east")))
    app.root.bind_all("<Return>", lambda _event: app._run_main_window_hotkey(app._reconcile_invariant_boundary_candidates))
    app.root.bind_all("<KeyPress-b>", lambda _event: app._run_main_window_hotkey(app._open_build_modal))
    app.root.bind_all("<KeyPress-f>", lambda _event: app._run_main_window_hotkey(app._queue_destroy_candidate))
    app.root.bind_all("<F12>", lambda _event: app._run_main_window_hotkey(app._wipe_to_fresh_start))
    app.root.protocol("WM_DELETE_WINDOW", app._close)


def open_modal(root: tk.Tk, title: str, geometry: str, background: str) -> tk.Toplevel:
    """Create the shared transient modal shell used across the teaching app."""

    modal = tk.Toplevel(root)
    modal.title(title)
    modal.geometry(geometry)
    modal.configure(bg=background)
    modal.transient(root)
    modal.grab_set()
    modal.bind("<Escape>", lambda _event: modal.destroy())
    return modal


def clear_widgets(widgets: list[tk.Widget]) -> None:
    """Destroy all canvas-backed widgets from the previous draw pass."""

    for widget in widgets:
        widget.destroy()
    widgets.clear()


def main_window_hotkeys_enabled(root: tk.Tk) -> bool:
    """Return whether global runtime hotkeys should currently mutate state."""

    # Modal dialogs keep their own keyboard behavior. The main window should
    # only react when its own toplevel owns focus.
    focus_widget = root.focus_get()
    if focus_widget is None:
        return True
    return focus_widget.winfo_toplevel() is root


def run_main_window_hotkey(root: tk.Tk, action: Callable[[], None]) -> None:
    """Run one hotkey action only when the main window currently owns focus."""

    if not main_window_hotkeys_enabled(root):
        return
    action()


def handle_escape(root: tk.Tk, close_callback: Callable[[], None]) -> None:
    """Close the app on Escape only when the main window owns focus."""

    if main_window_hotkeys_enabled(root):
        close_callback()
