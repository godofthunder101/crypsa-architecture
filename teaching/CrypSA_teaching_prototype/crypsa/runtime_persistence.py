from __future__ import annotations

import json
from pathlib import Path

from .crypsa_state_io import load_runtime_state, save_runtime_state
from .runtime_models import CandidateEvent, CanonicalEvent
from .runtime_store import CanonicalHistoryState, InspectionState, ObserverState, RuntimeStore

# This module is the schema-aware persistence boundary for RuntimeStore.
# Read it in two stages:
# 1. load_runtime_store(): on-disk schema -> typed runtime store
# 2. save_runtime_store(): typed runtime store -> on-disk schema
#
# Keep low-level JSON file I/O in crypsa_state_io.py. This file knows the saved
# teaching schema; crypsa_state_io.py should stay boring.


def _required_bool(value: object) -> bool:
    """Accept only real booleans from saved state."""

    if not isinstance(value, bool):
        raise TypeError("saved boolean field must be a real bool")
    return value


def load_runtime_store(path: Path) -> RuntimeStore | None:
    """Load a runtime store from the current on-disk teaching schema."""

    try:
        data = load_runtime_state(path)
        if data is None:
            return None
        # Read the saved file back in the same broad groups used by the schema
        # docs: observer, mint counters, accepted canonical events, selection,
        # then teaching/inspection logs.
        observer_local_x = int(data["observer"]["local_x"])
        observer_local_y = int(data["observer"]["local_y"])
        observer_facing = str(data["observer"]["facing"])
        observer_build_selection = str(data["observer"]["build_selection"])
        observer_auto_reconcile = _required_bool(data["observer"]["auto_reconcile"])
        observer_identity = str(data["observer"]["observer_identity"])
        invariant_boundary_candidates: list[CandidateEvent] = []
        for item in data["observer"]["invariant_boundary_candidates"]:
            if not isinstance(item, dict):
                raise TypeError("saved candidate record must be an object")
            candidate = CandidateEvent.from_dict(item)
            if candidate is not None:
                invariant_boundary_candidates.append(candidate)
                continue
            raise ValueError("saved candidate record is malformed")

        next_object_id = int(data["mint"]["next_object_id"])
        next_sequence = int(data["events"]["next_sequence"])
        events: dict[str, CanonicalEvent] = {}
        for item in data["events"]["records"]:
            if not isinstance(item, dict):
                raise TypeError("saved event record must be an object")
            record = CanonicalEvent.from_dict(item)
            if record is not None:
                events[record.event_id] = record
                continue
            raise ValueError("saved event record is malformed")

        selected_branch = str(data["selection"]["branch"])
        raw_selected = data["selection"]["event_id"]
        selected_canonical_event_id = str(raw_selected) if raw_selected is not None else None
        teaching_example_loaded = _required_bool(data["selection"]["teaching_example_loaded"])

        server_log = [str(line) for line in data["logs"]["server"][:60]]
        observer_log = [str(line) for line in data["logs"]["observer"][:60]]
        server_serial = int(data["logs"]["server_serial"])
        observer_serial = int(data["logs"]["observer_serial"])
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        # Return a clean "no usable saved state" signal instead of leaving the
        # controller with a partially hydrated runtime store.
        return None

    return RuntimeStore(
        observer=ObserverState(
            local_x=observer_local_x,
            local_y=observer_local_y,
            facing=observer_facing,
            build_selection=observer_build_selection,
            auto_reconcile=observer_auto_reconcile,
            observer_identity=observer_identity,
            invariant_boundary_candidates=invariant_boundary_candidates,
        ),
        canonical=CanonicalHistoryState(
            next_object_id=next_object_id,
            next_sequence=next_sequence,
            events=events,
            selected_branch=selected_branch,
            selected_canonical_event_id=selected_canonical_event_id,
            teaching_example_loaded=teaching_example_loaded,
        ),
        inspection=InspectionState(
            server_log=server_log,
            observer_log=observer_log,
            server_serial=server_serial,
            observer_serial=observer_serial,
        ),
    )


def save_runtime_store(path: Path, store: RuntimeStore, *, catalog_version: int) -> None:
    """Persist a runtime store into the current on-disk teaching schema."""

    # Keep save layout parallel with load layout so the saved file remains easy
    # to compare against runtime_schema.md and the RuntimeStore state groups.
    data = {
        "observer": {
            "local_x": store.observer.local_x,
            "local_y": store.observer.local_y,
            "facing": store.observer.facing,
            "build_selection": store.observer.build_selection,
            "auto_reconcile": store.observer.auto_reconcile,
            "observer_identity": store.observer.observer_identity,
            "invariant_boundary_candidates": [candidate.to_dict() for candidate in store.observer.invariant_boundary_candidates[:40]],
        },
        "mint": {"catalog_version": catalog_version, "next_object_id": store.canonical.next_object_id},
        "events": {
            "next_sequence": store.canonical.next_sequence,
            "records": [store.canonical.events[event_id].to_dict() for event_id in sorted(store.canonical.events, key=lambda item: store.canonical.events[item].sequence)],
        },
        "selection": {
            "branch": store.canonical.selected_branch,
            "event_id": store.canonical.selected_canonical_event_id,
            "teaching_example_loaded": store.canonical.teaching_example_loaded,
        },
        "logs": {
            "server": store.inspection.server_log[:60],
            "observer": store.inspection.observer_log[:60],
            "server_serial": store.inspection.server_serial,
            "observer_serial": store.inspection.observer_serial,
        },
    }
    save_runtime_state(path, data)
