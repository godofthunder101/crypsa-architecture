from __future__ import annotations

import unittest

from crypsa.runtime_actions import (
    queue_build_candidate,
    queue_destroy_candidate,
    recentered_observer_position,
    tile_in_front,
)
from crypsa.runtime_models import ReplayBranchState, ReplayObjectRecord


class RuntimeActionsTests(unittest.TestCase):
    def test_tile_in_front_clamps_to_grid(self) -> None:
        self.assertEqual(tile_in_front(0, 0, "north", 10), (0, 0))
        self.assertEqual(tile_in_front(9, 9, "east", 10), (9, 9))
        self.assertEqual(tile_in_front(4, 4, "south", 10), (4, 5))

    def test_queue_candidate_helpers_return_typed_candidates(self) -> None:
        build = queue_build_candidate("Beacon", (2, 8))
        destroy = queue_destroy_candidate((2, 8))

        self.assertEqual(build.action, "build_object")
        self.assertEqual(build.kind, "Beacon")
        self.assertEqual(destroy.action, "destroy_object")
        self.assertIsNone(destroy.kind)

    def test_recentered_observer_position_uses_fallback_for_empty_state(self) -> None:
        self.assertEqual(recentered_observer_position(ReplayBranchState(objects={}, event_count=0, head_event_id=None), 10), (4, 4))

    def test_recentered_observer_position_averages_visible_objects(self) -> None:
        state = ReplayBranchState(
            objects={
                "a": ReplayObjectRecord("a", "Relay", 1, 1, {}, {}),
                "b": ReplayObjectRecord("b", "Beacon", 5, 5, {}, {}),
            },
            event_count=2,
            head_event_id="evt-000002",
        )

        self.assertEqual(recentered_observer_position(state, 10), (3, 3))


if __name__ == "__main__":
    unittest.main()
