from __future__ import annotations

import unittest

from crypsa.runtime_models import CandidateEvent, CanonicalEvent, DestroyedObjectPayload, PlacedObjectPayload
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


class RuntimeModelsTests(unittest.TestCase):
    def test_candidate_event_round_trips_through_dict(self) -> None:
        candidate = CandidateEvent(action="build_object", kind="Beacon", x=2, y=8)

        raw = candidate.to_dict()
        rebuilt = CandidateEvent.from_dict(raw)

        self.assertEqual(rebuilt, candidate)

    def test_candidate_event_rejects_missing_required_fields(self) -> None:
        self.assertIsNone(CandidateEvent.from_dict({"action": "build_object", "x": 1}))

    def test_canonical_event_round_trips_through_dict(self) -> None:
        event = CanonicalEvent(
            sequence=1,
            event_id="evt-000001",
            event_family="structural",
            event_type="build_object",
            target_identity="relay-0001",
            observer_identity="observer:alice",
            timestamp="2026-03-23T00:00:00+00:00",
            lineage_parent=None,
            causal_references=[],
            branch_hint="main",
            catalog_version=1,
            payload=PlacedObjectPayload(
                object_id="relay-0001",
                kind="Relay",
                x=3,
                y=4,
                invariant_state={"state": "idle"},
                minted_definition=_minted_definition("Relay"),
            ).to_dict(),
        )

        raw = event.to_dict()
        rebuilt = CanonicalEvent.from_dict(raw)

        self.assertEqual(rebuilt, event)

    def test_canonical_event_rejects_malformed_structural_payload(self) -> None:
        raw = {
            "sequence": 1,
            "event_id": "evt-000001",
            "event_family": "structural",
            "event_type": "build_object",
            "target_identity": "relay-0001",
            "observer_identity": "observer:alice",
            "timestamp": "2026-03-23T00:00:00+00:00",
            "lineage_parent": None,
            "causal_references": [],
            "branch_hint": "main",
            "catalog_version": 1,
            "payload": {"object_id": "relay-0001", "kind": "Relay"},
        }

        self.assertIsNone(CanonicalEvent.from_dict(raw))

    def test_payload_helpers_serialize_to_expected_shapes(self) -> None:
        placed = PlacedObjectPayload(
            object_id="beacon-0001",
            kind="Beacon",
            x=2,
            y=8,
            invariant_state={"state": "idle"},
            minted_definition=_minted_definition("Beacon"),
        )
        destroyed = DestroyedObjectPayload(
            object_id="beacon-0001",
            kind="Beacon",
            x=2,
            y=8,
            prior_invariant_state={"state": "idle"},
            next_invariant_state={"state": "spent"},
        )

        self.assertEqual(placed.to_dict()["kind"], "Beacon")
        self.assertEqual(destroyed.to_dict()["next_invariant_state"], {"state": "spent"})


if __name__ == "__main__":
    unittest.main()
