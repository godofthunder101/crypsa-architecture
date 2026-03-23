from __future__ import annotations

import unittest

from crypsa.canonical_apply import create_canonical_event, mint_object_id
from crypsa.runtime_models import CanonicalEvent


class CanonicalApplyTests(unittest.TestCase):
    def test_mint_object_id_bumps_counter(self) -> None:
        object_id, next_counter = mint_object_id("Beacon", 7)

        self.assertEqual(object_id, "beacon-0007")
        self.assertEqual(next_counter, 8)

    def test_create_canonical_event_resolves_pending_branch_and_references(self) -> None:
        event, resolved_branch = create_canonical_event(
            next_sequence=4,
            branch_name="branch:evt-000001:pending",
            parent_event_id="evt-000001",
            event_type="build_object",
            event_family="structural",
            target_identity="beacon-0001",
            observer_identity="observer:alice",
            timestamp="2026-03-22T00:00:00Z",
            catalog_version=1,
            payload={"object_id": "beacon-0001"},
            existing_events={
                "evt-000001": CanonicalEvent(
                    sequence=1,
                    event_id="evt-000001",
                    event_family="structural",
                    event_type="mint_object",
                    target_identity="beacon-0000",
                    observer_identity="observer:alice",
                    timestamp="2026-03-22T00:00:00Z",
                    lineage_parent=None,
                    causal_references=[],
                    branch_hint="main",
                    catalog_version=1,
                    payload={"object_id": "beacon-0000"},
                )
            },
            causal_references=["evt-000001"],
        )

        self.assertEqual(event.event_id, "evt-000004")
        self.assertEqual(resolved_branch, "branch:evt-000001:evt-000004")
        self.assertEqual(event.branch_hint, resolved_branch)
        self.assertEqual(event.causal_references, ["evt-000001"])


if __name__ == "__main__":
    unittest.main()
