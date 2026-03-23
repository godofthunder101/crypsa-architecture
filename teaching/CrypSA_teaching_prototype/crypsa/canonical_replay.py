from __future__ import annotations

from .crypsa_event_graph import replay_branch_state
from .runtime_models import CanonicalEvent, ReplayBranchState, ReplayObjectRecord

# This module owns the small replay-derived canonical-state boundary used by the
# controller and reconciliation helpers.
#
# Read it in this order:
# 1. visible_canonical_state() for the main replay entrypoint
# 2. tile_occupied() / find_object_at_tile() for replay-derived queries
# 3. first_open_canonical_tile() for server-side placement scans
#
# Keep the deeper event-substrate machinery in crypsa_event_graph.py. This file
# exists so the rest of the runtime can ask higher-level replay questions
# without reaching directly into event-graph details each time.


def visible_canonical_state(
    events: dict[str, CanonicalEvent],
    head_event_id: str | None,
) -> ReplayBranchState:
    """Build typed visible canonical state for one selected history point."""

    return replay_branch_state(events, head_event_id)


def tile_occupied(x: int, y: int, canonical_state: ReplayBranchState) -> bool:
    """Return whether the replay-derived canonical state occupies one tile."""

    return any(obj.x == x and obj.y == y for obj in canonical_state.objects.values())


def find_object_at_tile(
    tile: tuple[int, int],
    canonical_state: ReplayBranchState,
) -> ReplayObjectRecord | None:
    """Return the canonical object on a tile, if one exists."""

    for obj in canonical_state.objects.values():
        if obj.x == tile[0] and obj.y == tile[1]:
            return obj
    return None


def first_open_canonical_tile(
    canonical_state: ReplayBranchState,
    grid_size: int,
    reserved_tiles: set[tuple[int, int]],
) -> tuple[int, int] | None:
    """Scan top-left to bottom-right for the first open canonical tile."""

    for y in range(grid_size):
        for x in range(grid_size):
            if (x, y) in reserved_tiles:
                continue
            if not tile_occupied(x, y, canonical_state):
                return x, y
    return None
