from __future__ import annotations

from .runtime_models import CanonicalEvent

# This module owns accepted-canonical-record creation.
# Read it in this order:
# 1. mint_object_id() for object-id allocation
# 2. create_canonical_event() for accepted event-id creation and branch-hint resolution
#
# Keep validation and replay outside this module:
# - validation.py decides whether the candidate event can pass
# - this module creates the accepted canonical record once it can
# - canonical_replay.py and crypsa_event_graph.py determine what visible state
#   that accepted record produces later


def mint_object_id(kind: str, next_object_id: int) -> tuple[str, int]:
    """Allocate one canonical object id and return the bumped counter."""

    return f"{kind.lower()}-{next_object_id:04d}", next_object_id + 1


def create_canonical_event(
    *,
    next_sequence: int,
    branch_name: str,
    parent_event_id: str | None,
    event_type: str,
    event_family: str,
    target_identity: str,
    observer_identity: str,
    timestamp: str,
    catalog_version: int,
    payload: dict[str, object],
    existing_events: dict[str, CanonicalEvent],
    causal_references: list[str] | None = None,
) -> tuple[CanonicalEvent, str]:
    """Create one accepted canonical event and resolve its branch label."""

    # This is the narrow "candidate event passed, now create the accepted
    # canonical record" boundary. Keep the record envelope and branch-hint
    # policy here so reconciliation can stay focused on the staged acceptance
    # loop instead of record-construction detail.
    event_id = f"evt-{next_sequence:06d}"
    resolved_branch_name = branch_name
    if branch_name.endswith(":pending") and isinstance(parent_event_id, str):
        resolved_branch_name = f"branch:{parent_event_id}:{event_id}"

    reference_list: list[str] = []
    if isinstance(parent_event_id, str) and parent_event_id in existing_events:
        reference_list.append(parent_event_id)
    for reference_id in causal_references or []:
        if isinstance(reference_id, str) and reference_id in existing_events and reference_id not in reference_list:
            reference_list.append(reference_id)

    return (
        CanonicalEvent(
            sequence=next_sequence,
            event_id=event_id,
            event_family=event_family,
            event_type=event_type,
            target_identity=target_identity,
            observer_identity=observer_identity,
            timestamp=timestamp,
            lineage_parent=parent_event_id,
            causal_references=reference_list,
            branch_hint=resolved_branch_name,
            catalog_version=catalog_version,
            payload=dict(payload),
        ),
        resolved_branch_name,
    )
