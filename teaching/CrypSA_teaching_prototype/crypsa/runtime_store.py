from __future__ import annotations

from dataclasses import dataclass, field

from .runtime_models import CandidateEvent, CanonicalEvent


DEFAULT_OBSERVER_ID = "observer:alice"


@dataclass
class ObserverState:
    """Observer-local state plus pending candidate events."""

    local_x: int = 4
    local_y: int = 4
    facing: str = "north"
    build_selection: str = ""
    auto_reconcile: bool = False
    observer_identity: str = DEFAULT_OBSERVER_ID
    invariant_boundary_candidates: list[CandidateEvent] = field(default_factory=list)


@dataclass
class CanonicalHistoryState:
    """Accepted canonical history plus current selection within it."""

    next_object_id: int = 1
    next_sequence: int = 1
    events: dict[str, CanonicalEvent] = field(default_factory=dict)
    selected_branch: str = "main"
    selected_canonical_event_id: str | None = None
    teaching_example_loaded: bool = False


@dataclass
class InspectionState:
    """Teaching-facing logs and their sequence counters."""

    server_log: list[str] = field(default_factory=list)
    observer_log: list[str] = field(default_factory=list)
    server_serial: int = 0
    observer_serial: int = 0


@dataclass
class RuntimeStore:
    """Single mutable home for the prototype's current runtime state."""

    observer: ObserverState = field(default_factory=ObserverState)
    canonical: CanonicalHistoryState = field(default_factory=CanonicalHistoryState)
    inspection: InspectionState = field(default_factory=InspectionState)

    def reset_to_baseline(self, build_selection: str) -> None:
        """Return the runtime store to the fresh-install teaching baseline."""

        self.observer = ObserverState(build_selection=build_selection)
        self.canonical = CanonicalHistoryState()
        self.inspection = InspectionState()
