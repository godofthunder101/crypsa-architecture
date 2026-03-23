from __future__ import annotations

import tkinter as tk
from typing import Any

from .runtime_models import CandidateEvent, PlacedObjectPayload, DestroyedObjectPayload, ReplayBranchState

# This module owns the staged candidate-event acceptance loop.
# Read it in this order:
# 1. one build acceptance
# 2. one destroy acceptance
# 3. the top-level reconcile loop
# 4. direct server mint
#
# The controller still owns surrounding orchestration, but the acceptance flow
# itself now lives here instead of inline in the main app class.
#
# The easiest mental split is:
# - validation.py answers "can this candidate event pass?"
# - this module answers "run the staged acceptance loop"
# - canonical_apply.py answers "create the accepted canonical record"
# - canonical_replay.py answers "what visible canonical state exists after that?"


def accept_build_candidate(
    app: Any,
    branch_name: str,
    parent_event_id: str | None,
    causal_context_ids: list[str],
    canonical_state: ReplayBranchState,
    action: CandidateEvent,
) -> tuple[bool, str | None, ReplayBranchState]:
    """Try to turn one queued build candidate into a canonical event."""

    # This is the full build path in one place:
    # validate -> create typed payload -> accept canonical event -> replay next state.
    kind = str(action.kind)
    tile = (int(action.x), int(action.y))
    minted_definition = app._catalog_minted_definition(kind)
    allowed, reason, next_state = app._validate_and_transition_action(
        minted_definition,
        "build",
        tile,
        canonical_state,
        parent_event_id=parent_event_id,
        causal_context_ids=causal_context_ids,
    )
    if not allowed:
        app._push_server_log(f"reject build {kind} @ ({tile[0]}, {tile[1]}) -> {reason}")
        app._push_observer_log(f"reconciliation denied -> {reason}")
        return False, parent_event_id, canonical_state
    object_id = app._mint_object_id(kind)
    record = app._accept_canonical_event(
        branch_name,
        parent_event_id,
        "build_object",
        "structural",
        object_id,
        PlacedObjectPayload(
            object_id=object_id,
            kind=kind,
            x=tile[0],
            y=tile[1],
            invariant_state=next_state,
            minted_definition=minted_definition,
        ).to_dict(),
        causal_references=causal_context_ids,
    )
    next_parent_event_id = record.event_id
    next_canonical_state = app._replay_branch_state(next_parent_event_id)
    app._push_server_log(f"canonical event accepted -> build {object_id} ({kind}) @ ({tile[0]}, {tile[1]})")
    app._push_observer_log(f"observer view converged with canonical state -> {object_id}")
    if kind == "Beacon":
        app._push_observer_log("Beacon accepted -> open History or Timeline to inspect how causal context affected acceptance")
    return True, next_parent_event_id, next_canonical_state


def accept_destroy_candidate(
    app: Any,
    branch_name: str,
    parent_event_id: str | None,
    causal_context_ids: list[str],
    canonical_state: ReplayBranchState,
    action: CandidateEvent,
) -> tuple[bool, str | None, ReplayBranchState]:
    """Try to turn one queued destroy candidate into a canonical event."""

    # Destroy follows the same acceptance shape as build, but starts from a
    # replay-derived object instead of a catalog-selected kind.
    tile = (int(action.x), int(action.y))
    target_object = app._find_object_at_tile(tile, canonical_state)
    if target_object is None:
        app._push_server_log(f"reject destroy @ ({tile[0]}, {tile[1]}) -> no canonical object")
        app._push_observer_log("reconciliation denied -> no canonical object on target tile")
        return False, parent_event_id, canonical_state
    minted_definition = target_object.minted_definition
    current_state = dict(target_object.invariant_state)
    allowed, reason, next_state = app._validate_and_transition_action(
        minted_definition,
        "destroy",
        tile,
        canonical_state,
        current_state=current_state,
        parent_event_id=parent_event_id,
        causal_context_ids=causal_context_ids,
    )
    if not allowed:
        app._push_server_log(f"reject destroy {target_object.object_id} -> {reason}")
        app._push_observer_log(f"reconciliation denied -> {reason}")
        return False, parent_event_id, canonical_state
    record = app._accept_canonical_event(
        branch_name,
        parent_event_id,
        "destroy_object",
        "structural",
        target_object.object_id,
        DestroyedObjectPayload(
            object_id=target_object.object_id,
            kind=target_object.kind,
            x=tile[0],
            y=tile[1],
            prior_invariant_state=current_state,
            next_invariant_state=next_state,
        ).to_dict(),
        causal_references=causal_context_ids,
    )
    next_parent_event_id = record.event_id
    next_canonical_state = app._replay_branch_state(next_parent_event_id)
    app._push_server_log(f"canonical event accepted -> destroy {target_object.object_id} @ ({tile[0]}, {tile[1]})")
    app._push_observer_log(f"observer view converged with canonical state -> removed {target_object.object_id}")
    return True, next_parent_event_id, next_canonical_state


def reconcile_invariant_boundary_candidates(app: Any) -> None:
    """Reconcile the observer-side invariant-boundary queue into canonical history."""

    # Read the top-level loop as:
    # choose writable lineage -> replay current state -> refresh causal context
    # per candidate -> accept/reject -> redraw.
    #
    # Keep in mind that the queue is typed as CandidateEvent, but each accepted
    # result becomes a CanonicalEvent only after validation and canonical apply.
    if not app.invariant_boundary_candidates:
        app._push_observer_log("no invariant-boundary candidates to reconcile")
        app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
        return
    branch_name, parent_event_id = app._ensure_writable_branch()
    canonical_state = app._replay_branch_state(parent_event_id)
    accepted = 0
    rejected = 0
    remaining: list[CandidateEvent] = []
    for action in app.invariant_boundary_candidates:
        action_type = str(action.action)
        causal_context_ids = app._current_causal_context_ids()
        if action_type == "build_object":
            was_accepted, parent_event_id, canonical_state = accept_build_candidate(
                app,
                branch_name,
                parent_event_id,
                causal_context_ids,
                canonical_state,
                action,
            )
            if was_accepted:
                accepted += 1
            else:
                rejected += 1
            continue
        if action_type == "destroy_object":
            was_accepted, parent_event_id, canonical_state = accept_destroy_candidate(
                app,
                branch_name,
                parent_event_id,
                causal_context_ids,
                canonical_state,
                action,
            )
            if was_accepted:
                accepted += 1
            else:
                rejected += 1
            continue
        remaining.append(action)
    app.invariant_boundary_candidates = remaining
    app._push_server_log(f"reconcile complete -> accepted {accepted}, rejected {rejected}")
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())


def mint_from_server(app: Any, kind: str, modal: tk.Toplevel | None = None) -> None:
    """Mint one canonical object directly from the server-side teaching action."""

    # Server mint reuses the same validation/acceptance shape as reconciliation,
    # but it chooses the first open canonical tile itself.
    branch_name, parent_event_id = app._ensure_writable_branch()
    causal_context_ids = app._current_causal_context_ids()
    canonical_state = app._replay_branch_state(parent_event_id)
    open_tile = app._first_open_canonical_tile(canonical_state)
    if open_tile is None:
        app._push_server_log("server mint denied -> no canonical tile available")
        app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
        return
    minted_definition = app._catalog_minted_definition(kind)
    allowed, reason, next_state = app._validate_and_transition_action(
        minted_definition,
        "mint",
        open_tile,
        canonical_state,
        parent_event_id=parent_event_id,
        causal_context_ids=causal_context_ids,
    )
    if not allowed:
        app._push_server_log(f"server mint denied {kind} -> {reason}")
        app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
        return
    object_id = app._mint_object_id(kind)
    record = app._accept_canonical_event(
        branch_name,
        parent_event_id,
        "mint_object",
        "structural",
        object_id,
        PlacedObjectPayload(
            object_id=object_id,
            kind=kind,
            x=open_tile[0],
            y=open_tile[1],
            invariant_state=next_state,
            minted_definition=minted_definition,
        ).to_dict(),
        causal_references=causal_context_ids,
    )
    app.selected_canonical_event_id = record.event_id
    app._push_server_log(f"server mint -> {object_id} ({kind}) @ ({open_tile[0]}, {open_tile[1]})")
    if kind == "Beacon":
        app._push_observer_log("Beacon minted -> open History or Timeline to inspect its accepted causal context")
    app._draw_scene(app.root.winfo_width(), app.root.winfo_height())
    if isinstance(modal, tk.Toplevel) and modal.winfo_exists():
        modal.destroy()
