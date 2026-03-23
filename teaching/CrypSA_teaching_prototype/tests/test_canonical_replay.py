from __future__ import annotations

import unittest

from crypsa.canonical_replay import (
    find_object_at_tile,
    first_open_canonical_tile,
    tile_occupied,
    visible_canonical_state,
)
from crypsa.runtime_models import CanonicalEvent, ReplayBranchState, ReplayObjectRecord
from mint.mint_catalog_store import build_default_genome
from mint.mint_models import build_minted_definition


def _minted_definition(kind: str = "Relay"):
    return build_minted_definition(
        kind=kind,
        catalog_version=1,
        palette=("#38bdf8", "#bae6fd"),
        metadata={
            "description": f"{kind} definition",
            "rule_tag": "utility",
            "rule_tags": ["utility"],
            "default_color": "#38bdf8",
            "genome": build_default_genome(),
        },
    )


class CanonicalReplayTests(unittest.TestCase):
    def test_visible_canonical_state_replays_build_and_destroy(self) -> None:
        events = {
            "evt-000001": CanonicalEvent(
                sequence=1,
                event_id="evt-000001",
                event_family="structural",
                event_type="build_object",
                target_identity="obj-1",
                observer_identity="observer:alice",
                timestamp="2026-03-23T00:00:00+00:00",
                lineage_parent=None,
                causal_references=[],
                branch_hint="main",
                catalog_version=1,
                payload={
                    "object_id": "obj-1",
                    "kind": "Relay",
                    "x": 2,
                    "y": 3,
                    "invariant_state": {"state": "idle"},
                    "minted_definition": _minted_definition("Relay"),
                },
            ),
            "evt-000002": CanonicalEvent(
                sequence=2,
                event_id="evt-000002",
                event_family="structural",
                event_type="destroy_object",
                target_identity="obj-1",
                observer_identity="observer:alice",
                timestamp="2026-03-23T00:00:01+00:00",
                lineage_parent="evt-000001",
                causal_references=["evt-000001"],
                branch_hint="main",
                catalog_version=1,
                payload={"object_id": "obj-1"},
            ),
        }

        state = visible_canonical_state(events, "evt-000002")

        self.assertEqual(state.event_count, 2)
        self.assertEqual(state.head_event_id, "evt-000002")
        self.assertEqual(state.objects, {})

    def test_tile_helpers_work_on_replay_state(self) -> None:
        canonical_state = ReplayBranchState(
            objects={
                "obj-1": ReplayObjectRecord(
                    object_id="obj-1",
                    kind="Relay",
                    x=1,
                    y=1,
                    invariant_state={},
                    minted_definition=_minted_definition("Relay"),
                ),
                "obj-2": ReplayObjectRecord(
                    object_id="obj-2",
                    kind="Beacon",
                    x=2,
                    y=2,
                    invariant_state={},
                    minted_definition=_minted_definition("Beacon"),
                ),
            },
            event_count=2,
            head_event_id="evt-000002",
        )

        self.assertTrue(tile_occupied(1, 1, canonical_state))
        self.assertFalse(tile_occupied(0, 0, canonical_state))
        self.assertEqual(find_object_at_tile((2, 2), canonical_state).object_id, "obj-2")
        self.assertEqual(first_open_canonical_tile(canonical_state, 4, {(0, 0)}), (1, 0))


if __name__ == "__main__":
    unittest.main()
