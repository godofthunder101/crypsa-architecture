from __future__ import annotations

import os
import tkinter as tk
from typing import Any

from .crypsa_teaching_theme import MINT_EDITOR_START_PATH
from .runtime_actions import recentered_observer_position
from mint.mint_catalog_store import load_catalog

# This module keeps a small set of UI-facing controller actions out of the main
# orchestration file. These helpers are still controller-side because they
# coordinate logs, redraws, modal behavior, and catalog/runtime state together,
# but they do not need to live inline in the main app class.
#
# Reading tip:
# 1. catalog reload / editor launch
# 2. small queue-management helpers
# 3. Beacon teaching-path setup
# 4. observer recentering for timeline/history inspection


def _removed_kinds_still_used(app: Any, removed_kinds: set[str]) -> bool:
    """Return whether removed Mint kinds still appear in runtime state."""

    if not removed_kinds:
        return False
    for candidate in app.invariant_boundary_candidates:
        if isinstance(candidate.kind, str) and candidate.kind in removed_kinds:
            return True
    for record in app.events.values():
        kind = record.payload.get("kind")
        if isinstance(kind, str) and kind in removed_kinds:
            return True
    return False


def open_mint_editor(app: Any) -> None:
    """Launch the standalone Mint editor from the teaching prototype."""

    if not MINT_EDITOR_START_PATH.exists():
        app._push_observer_log("mint editor launch failed -> start-mint-editor.cmd missing")
        app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
        return
    try:
        os.startfile(str(MINT_EDITOR_START_PATH))
        app._push_observer_log(f"mint editor opened -> {MINT_EDITOR_START_PATH.name}")
    except OSError:
        app._push_observer_log("mint editor launch failed -> OS refused start command")
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())


def reload_catalog(app: Any, modal: tk.Toplevel | None = None) -> None:
    """Reload Mint catalog state while preserving the current build selection when possible."""

    previous_definitions = set(app.entity_definitions)
    previous_selection = app.observer_build_selection
    app.entity_definitions, app.entity_metadata, app.catalog_version, app.rule_tags = load_catalog()
    removed_kinds = previous_definitions - set(app.entity_definitions)
    reset_for_removed_kind = _removed_kinds_still_used(app, removed_kinds)
    if reset_for_removed_kind:
        app._reset_runtime_state()
    if previous_selection in app.entity_definitions:
        app.observer_build_selection = previous_selection
    else:
        app.observer_build_selection = next(iter(app.entity_definitions))
    app._push_observer_log(f"catalog reloaded -> v{app.catalog_version}")
    if reset_for_removed_kind:
        app._push_server_log(
            "catalog reload removed kinds still referenced by the teaching world -> runtime reset to baseline"
        )
        app._push_observer_log(
            "catalog reload removed a kind used by queued or canonical objects -> teaching world reset to baseline"
        )
        if hasattr(app, "_save_state"):
            app._save_state()
    if isinstance(modal, tk.Toplevel) and modal.winfo_exists():
        modal.destroy()
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())


def clear_candidates(app: Any, modal: tk.Toplevel) -> None:
    """Clear queued invariant-boundary candidates from the observer side."""

    app.invariant_boundary_candidates.clear()
    app._push_observer_log("invariant-boundary candidates cleared")
    modal.destroy()
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())


def try_beacon_path(app: Any, modal: tk.Toplevel | None = None) -> None:
    """Prepare the built-in Beacon teaching path and reopen the build chooser."""

    if not app.teaching_example_loaded:
        app._load_teaching_example(modal)
    elif isinstance(modal, tk.Toplevel) and modal.winfo_exists():
        modal.destroy()
    app.observer_build_selection = app._preferred_kind(["Beacon", "NPC", "Hut", "Relay", "Gateway"])
    app._push_observer_log(f"teaching path prepared -> build chooser focused on {app.observer_build_selection}")
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
    app._open_build_modal()


def center_observer_near_canonical_state(app: Any, modal: tk.Toplevel | None = None) -> None:
    """Move the observer view near the currently selected canonical state."""

    state = app._visible_canonical_state()
    app.observer_local_x, app.observer_local_y = recentered_observer_position(state, app.grid_size)
    app._push_observer_log(
        f"observer view recentered near the selected canonical state -> ({app.observer_local_x}, {app.observer_local_y})"
    )
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
