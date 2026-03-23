from __future__ import annotations

import tkinter as tk
from typing import Any

from .crypsa_action_requests import (
    ActionRequest,
    CenterObserverNearCanonicalRequest,
    ClearCandidatesRequest,
    MintFromServerRequest,
    OpenMintEditorRequest,
    QueueBuildCandidateRequest,
    ReloadCatalogRequest,
    SelectHistoryEventRequest,
    SelectTimelineEventRequest,
    TryBeaconPathRequest,
)


def dispatch_action_request(app: Any, request: ActionRequest, modal: tk.Toplevel | None = None) -> None:
    """Translate one typed UI request into the matching controller action."""

    # Keep request dispatch separate from controller orchestration so the
    # request boundary stays explicit: UI emits intent objects, this module
    # routes them, and the controller remains the owner of the mutation
    # methods themselves.
    #
    # This boundary is now part of a completed teaching artifact. The goal is
    # to keep routing boring and explicit, not to turn dispatch into a second
    # controller or a clever abstraction layer.
    #
    # Reading tip:
    # - start with the request type definition in crypsa_action_requests.py
    # - if a button renders incorrectly, inspect the lens builder first
    # - if the button renders correctly but does the wrong thing, inspect this
    #   router second and the targeted controller mutation third

    if isinstance(request, ReloadCatalogRequest):
        app._reload_catalog(modal)
        return
    if isinstance(request, OpenMintEditorRequest):
        app._open_mint_editor()
        return
    if isinstance(request, MintFromServerRequest):
        app._mint_from_server(request.kind, modal)
        return
    if isinstance(request, QueueBuildCandidateRequest):
        app._queue_build_candidate(request.kind, modal)
        return
    if isinstance(request, TryBeaconPathRequest):
        app._try_beacon_path(modal)
        return
    if isinstance(request, ClearCandidatesRequest):
        if modal is None:
            raise ValueError("ClearCandidatesRequest requires the originating modal")
        app._clear_candidates(modal)
        return
    if isinstance(request, SelectHistoryEventRequest):
        if modal is None:
            raise ValueError("SelectHistoryEventRequest requires the originating modal")
        app._select_history_event(request.event_id, request.preferred_branch_name, modal)
        return
    if isinstance(request, SelectTimelineEventRequest):
        app._select_timeline_event(request.branch_name, request.event_id)
        return
    if isinstance(request, CenterObserverNearCanonicalRequest):
        app._center_observer_near_canonical_state(modal)
        return
    raise TypeError(f"Unhandled action request: {type(request).__name__}")
