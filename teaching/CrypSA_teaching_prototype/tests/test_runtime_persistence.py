from __future__ import annotations

import tempfile
import unittest
import json
from pathlib import Path

from crypsa.runtime_models import CandidateEvent, CanonicalEvent, PlacedObjectPayload
from crypsa.runtime_persistence import load_runtime_store, save_runtime_store
from crypsa.runtime_store import CanonicalHistoryState, InspectionState, ObserverState, RuntimeStore
from mint.mint_catalog_store import build_default_genome
from mint.mint_models import build_minted_definition


def _minted_definition(kind: str = "Beacon"):
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


class RuntimePersistenceTests(unittest.TestCase):
    def test_runtime_store_round_trips_through_disk_schema(self) -> None:
        store = RuntimeStore(
            observer=ObserverState(
                local_x=2,
                local_y=8,
                facing="east",
                build_selection="Beacon",
                auto_reconcile=True,
                observer_identity="observer:alice",
                invariant_boundary_candidates=[CandidateEvent(action="build_object", kind="Beacon", x=2, y=8)],
            ),
            canonical=CanonicalHistoryState(
                next_object_id=3,
                next_sequence=4,
                events={
                    "evt-000001": CanonicalEvent(
                        sequence=1,
                        event_id="evt-000001",
                        event_family="structural",
                        event_type="build_object",
                        target_identity="beacon-0001",
                        observer_identity="observer:alice",
                        timestamp="2026-03-23T00:00:00+00:00",
                        lineage_parent=None,
                        causal_references=[],
                        branch_hint="main",
                        catalog_version=1,
                        payload=PlacedObjectPayload(
                            object_id="beacon-0001",
                            kind="Beacon",
                            x=2,
                            y=8,
                            invariant_state={"state": "idle"},
                            minted_definition=_minted_definition("Beacon"),
                        ).to_dict(),
                    )
                },
                selected_branch="main",
                selected_canonical_event_id="evt-000001",
                teaching_example_loaded=True,
            ),
            inspection=InspectionState(
                server_log=["[S001] canonical event accepted"],
                observer_log=["[O001] candidate queued"],
                server_serial=1,
                observer_serial=1,
            ),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "state.json"
            save_runtime_store(path, store, catalog_version=7)
            rebuilt = load_runtime_store(path)

        self.assertEqual(rebuilt, store)

    def test_runtime_store_rejects_non_boolean_saved_flags(self) -> None:
        raw_state = {
            "observer": {
                "local_x": 2,
                "local_y": 8,
                "facing": "east",
                "build_selection": "Beacon",
                "auto_reconcile": "false",
                "observer_identity": "observer:alice",
                "invariant_boundary_candidates": [],
            },
            "mint": {"catalog_version": 1, "next_object_id": 1},
            "events": {"next_sequence": 1, "records": []},
            "selection": {"branch": "main", "event_id": None, "teaching_example_loaded": False},
            "logs": {"server": [], "observer": [], "server_serial": 0, "observer_serial": 0},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "state.json"
            path.write_text(json.dumps(raw_state), encoding="utf-8")
            rebuilt = load_runtime_store(path)

        self.assertIsNone(rebuilt)

    def test_runtime_store_rejects_malformed_saved_event_payload(self) -> None:
        raw_state = {
            "observer": {
                "local_x": 2,
                "local_y": 8,
                "facing": "east",
                "build_selection": "Beacon",
                "auto_reconcile": False,
                "observer_identity": "observer:alice",
                "invariant_boundary_candidates": [],
            },
            "mint": {"catalog_version": 1, "next_object_id": 1},
            "events": {
                "next_sequence": 2,
                "records": [
                    {
                        "sequence": 1,
                        "event_id": "evt-000001",
                        "event_family": "structural",
                        "event_type": "build_object",
                        "target_identity": "beacon-0001",
                        "observer_identity": "observer:alice",
                        "timestamp": "2026-03-23T00:00:00+00:00",
                        "lineage_parent": None,
                        "causal_references": [],
                        "branch_hint": "main",
                        "catalog_version": 1,
                        "payload": {"object_id": "beacon-0001", "kind": "Beacon"},
                    }
                ],
            },
            "selection": {"branch": "main", "event_id": "evt-000001", "teaching_example_loaded": False},
            "logs": {"server": [], "observer": [], "server_serial": 0, "observer_serial": 0},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "state.json"
            path.write_text(json.dumps(raw_state), encoding="utf-8")
            rebuilt = load_runtime_store(path)

        self.assertIsNone(rebuilt)


if __name__ == "__main__":
    unittest.main()
