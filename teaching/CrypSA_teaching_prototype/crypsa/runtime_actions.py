from __future__ import annotations

from .runtime_models import CandidateEvent, ReplayBranchState

# This module owns a small set of observer-side "do the thing" helpers.
#
# Read it in this order:
# 1. tile_in_front() for target-tile calculation
# 2. queue_build_candidate() / queue_destroy_candidate() for typed candidate creation
# 3. recentered_observer_position() for observer repositioning near visible canonical state
#
# Keep canonical validation, accepted-record creation, and replay outside this
# module. This file exists to keep common observer-side action mechanics out of
# the main controller body.


def tile_in_front(
    observer_x: int,
    observer_y: int,
    facing: str,
    grid_size: int,
) -> tuple[int, int]:
    """Return the bounded tile directly in front of the observer."""

    dx, dy = {"north": (0, -1), "south": (0, 1), "west": (-1, 0), "east": (1, 0)}.get(facing, (0, -1))
    return (
        max(0, min(grid_size - 1, observer_x + dx)),
        max(0, min(grid_size - 1, observer_y + dy)),
    )


def queue_build_candidate(
    selected_kind: str,
    tile: tuple[int, int],
) -> CandidateEvent:
    """Create one typed observer-side build candidate."""

    return CandidateEvent(action="build_object", kind=selected_kind, x=tile[0], y=tile[1])


def queue_destroy_candidate(tile: tuple[int, int]) -> CandidateEvent:
    """Create one typed observer-side destroy candidate."""

    return CandidateEvent(action="destroy_object", x=tile[0], y=tile[1])


def recentered_observer_position(
    canonical_state: ReplayBranchState,
    grid_size: int,
    *,
    fallback: tuple[int, int] = (4, 4),
) -> tuple[int, int]:
    """Choose an observer position near the visible canonical state."""

    if not canonical_state.objects:
        return fallback
    x_values = [obj.x for obj in canonical_state.objects.values()]
    y_values = [obj.y for obj in canonical_state.objects.values()]
    return (
        max(0, min(grid_size - 1, round(sum(x_values) / len(x_values)))),
        max(0, min(grid_size - 1, round(sum(y_values) / len(y_values)))),
    )
