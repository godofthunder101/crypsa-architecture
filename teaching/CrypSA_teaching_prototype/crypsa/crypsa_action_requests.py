from __future__ import annotations

from dataclasses import dataclass


# These request objects are the small handoff contract from UI lenses back to
# the runtime controller. The UI emits intent; the runtime decides how to
# execute it. Keep them narrow and lens-facing: they should describe "what the
# user is trying to do", not leak controller implementation details.
#
# Reading tip:
# - if the UI needs to mutate runtime state, start by asking whether that
#   interaction deserves a new request type here
# - if the request starts carrying lots of display-only data, move that data
#   back into the lens adapter instead
# - if a request needs branch-choice or selection policy, prefer letting the
#   adapter decide it first and then carry the chosen result here

@dataclass(frozen=True)
class ReloadCatalogRequest:
    pass


@dataclass(frozen=True)
class OpenMintEditorRequest:
    pass


@dataclass(frozen=True)
class MintFromServerRequest:
    kind: str


@dataclass(frozen=True)
class QueueBuildCandidateRequest:
    kind: str


@dataclass(frozen=True)
class TryBeaconPathRequest:
    pass


@dataclass(frozen=True)
class ClearCandidatesRequest:
    pass


@dataclass(frozen=True)
class SelectHistoryEventRequest:
    # History selection carries the already-chosen preferred branch so the UI
    # and controller do not re-decide the branch policy in two places.
    event_id: str
    preferred_branch_name: str | None


@dataclass(frozen=True)
class SelectTimelineEventRequest:
    branch_name: str
    event_id: str


@dataclass(frozen=True)
class CenterObserverNearCanonicalRequest:
    pass


ActionRequest = (
    ReloadCatalogRequest
    | OpenMintEditorRequest
    | MintFromServerRequest
    | QueueBuildCandidateRequest
    | TryBeaconPathRequest
    | ClearCandidatesRequest
    | SelectHistoryEventRequest
    | SelectTimelineEventRequest
    | CenterObserverNearCanonicalRequest
)

# Read this file together with:
# - crypsa_lens_adapters.py, which attaches these requests to rendered lens data
# - crypsa_teaching_prototype.py::_execute_action_request(), which executes them
