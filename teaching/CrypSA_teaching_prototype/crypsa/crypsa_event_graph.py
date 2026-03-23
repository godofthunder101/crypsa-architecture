from __future__ import annotations

from dataclasses import dataclass

from mint.mint_models import copy_invariant_state, copy_minted_definition

from .runtime_models import CanonicalEvent, ReplayBranchState, ReplayObjectRecord


@dataclass(frozen=True)
class BranchRecord:
    """A typed displayed event-lineage row derived from canonical history."""

    name: str
    head_event_id: str | None
    fork_from_event_id: str | None
    parent_branch: str | None


def baseline_state() -> ReplayBranchState:
    """The empty canonical state before any accepted canonical events."""

    return ReplayBranchState(objects={}, event_count=0, head_event_id=None)


def all_event_ids_sorted(events: dict[str, CanonicalEvent]) -> list[str]:
    """Return accepted event ids in stable sequence order."""

    return [event_id for event_id, _record in sorted(events.items(), key=lambda item: item[1].sequence)]


def all_events_sorted(events: dict[str, CanonicalEvent]) -> list[CanonicalEvent]:
    """Return accepted event records in stable sequence order."""

    return [events[event_id] for event_id in all_event_ids_sorted(events)]


def event_chain(events: dict[str, CanonicalEvent], head_event_id: str | None) -> list[CanonicalEvent]:
    """Follow replay lineage backwards, then return the chain in replay order."""

    ordered: list[CanonicalEvent] = []
    current = head_event_id
    while isinstance(current, str) and current in events:
        record = events[current]
        ordered.append(record)
        # Replay follows the lineage parent only. Broader causal references are
        # preserved elsewhere for inspection and future graph expansion.
        next_id = record.lineage_parent
        current = str(next_id) if isinstance(next_id, str) else None
    ordered.reverse()
    return ordered


def event_children(events: dict[str, CanonicalEvent]) -> dict[str | None, list[str]]:
    """Index accepted events by lineage parent for branch-row derivation."""

    children: dict[str | None, list[str]] = {}
    for event_id, record in events.items():
        parent_id = record.lineage_parent
        parent_key = str(parent_id) if isinstance(parent_id, str) else None
        children.setdefault(parent_key, []).append(event_id)
    for event_ids in children.values():
        event_ids.sort(key=lambda item: events[item].sequence)
    return children


def primary_descent_from(
    events: dict[str, CanonicalEvent],
    start_event_id: str,
    children: dict[str | None, list[str]],
) -> list[str]:
    """Choose the earliest-child replay path used as the main displayed row."""

    path: list[str] = []
    current = start_event_id
    while current in events:
        path.append(current)
        next_children = children.get(current, [])
        if not next_children:
            break
        current = next_children[0]
    return path


def build_branch_rows(events: dict[str, CanonicalEvent]) -> list[BranchRecord]:
    """Build human-facing event-lineage rows from replay lineage data."""

    # Read branch-row derivation in three stages:
    # 1. build the child index by lineage parent
    # 2. follow the earliest-child descent to define the main displayed row
    # 3. spin later siblings out into side rows for human inspection
    #
    # Important boundary: these rows are a teaching/inspection view over
    # accepted canonical history. They are not an extra source of truth beyond
    # the underlying accepted events and their lineage links.
    children = event_children(events)
    if not children.get(None):
        return [BranchRecord("main", None, None, None)]

    rows: list[BranchRecord] = []

    def branch_id(fork_from_event_id: str | None, first_event_id: str | None) -> str:
        if fork_from_event_id is None:
            return "main"
        if first_event_id is None:
            return f"branch:{fork_from_event_id}:pending"
        return f"branch:{fork_from_event_id}:{first_event_id}"

    def create_branch(prefix_to_parent: list[str], parent_name: str, fork_from_event_id: str | None, child_event_id: str) -> None:
        branch_path = prefix_to_parent + primary_descent_from(events, child_event_id, children)
        current_branch_id = branch_id(fork_from_event_id, child_event_id)
        rows.append(BranchRecord(current_branch_id, branch_path[-1], fork_from_event_id, parent_name))
        walk_side_branches(branch_path, current_branch_id)

    def walk_side_branches(path: list[str], row_name: str) -> None:
        prefix: list[str] = []
        parent_id: str | None = None
        for event_id in path:
            # The earliest accepted child stays on the current event-lineage row.
            # Later sibling events become separate event-lineage rows rooted at
            # the same lineage parent.
            siblings = children.get(parent_id, [])
            for child_id in siblings[1:]:
                if child_id != event_id:
                    create_branch(prefix, row_name, parent_id, child_id)
            prefix.append(event_id)
            parent_id = event_id

    main_path = primary_descent_from(events, children[None][0], children)
    rows.append(BranchRecord("main", main_path[-1], None, None))
    walk_side_branches(main_path, "main")
    return rows


def branch_record_by_name(events: dict[str, CanonicalEvent], branch_name: str) -> BranchRecord | None:
    """Look up one displayed branch row by its stable row name."""

    for branch in build_branch_rows(events):
        if branch.name == branch_name:
            return branch
    return None


def branch_label(events: dict[str, CanonicalEvent], branch_name: str | None) -> str:
    """Turn an internal branch-row name into human-facing timeline text."""

    if branch_name in {None, "main"}:
        return "Main"
    raw_name = str(branch_name)
    parts = raw_name.split(":")
    if len(parts) == 3 and parts[0] == "branch":
        fork_event_id = parts[1]
        first_event_id = parts[2]
        fork_seq = events[fork_event_id].sequence if fork_event_id in events else 0
        return f"Branch from seq {fork_seq} via {first_event_id}"
    return raw_name


def replay_branch_state(events: dict[str, CanonicalEvent], head_event_id: str | None) -> ReplayBranchState:
    """Reconstruct canonical state by replaying accepted canonical events."""

    objects: dict[str, ReplayObjectRecord] = {}
    event_count = 0
    current_head_event_id: str | None = None
    # Replay is intentionally simple in this prototype: walk the lineage chain
    # in order, apply each accepted event, and treat the resulting object map as
    # the visible canonical state for that selected history point.
    #
    # Reading tip: event replay is easier to follow if you split it mentally
    # into "find the ordered lineage chain" first and "apply each event payload"
    # second.
    #
    # This function is intentionally not a general CrypSA runtime. It is the
    # small teaching replay loop for this prototype's accepted canonical
    # history model.
    for record in event_chain(events, head_event_id):
        payload = dict(record.payload)
        event_type = record.event_type
        if event_type in {"mint_object", "build_object"}:
            object_id = str(payload["object_id"])
            objects[object_id] = ReplayObjectRecord(
                object_id=object_id,
                kind=str(payload["kind"]),
                x=int(payload["x"]),
                y=int(payload["y"]),
                invariant_state=copy_invariant_state(payload["invariant_state"]),
                minted_definition=copy_minted_definition(payload["minted_definition"]),
            )
        elif event_type == "destroy_object":
            objects.pop(str(payload["object_id"]), None)
        event_count = record.sequence
        current_head_event_id = record.event_id
    return ReplayBranchState(
        objects=objects,
        event_count=event_count,
        head_event_id=current_head_event_id,
    )
