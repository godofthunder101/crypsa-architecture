from __future__ import annotations

from types import SimpleNamespace
import unittest

from crypsa.crypsa_action_requests import MintFromServerRequest, QueueBuildCandidateRequest
from crypsa.crypsa_lens_adapters import (
    build_build_action_modal_lens,
    build_candidate_queue_lens,
    build_canonical_pane_lens,
    build_mint_action_modal_lens,
    build_observer_pane_lens,
)
from crypsa.runtime_models import CandidateEvent, CanonicalEvent, ReplayBranchState, ReplayObjectRecord
from mint.mint_catalog_store import build_beacon_default_genome, build_default_genome
from mint.mint_models import build_minted_definition


class _FakeRuntimeApp:
    def __init__(self) -> None:
        self.grid_size = 10
        self.server_reserved_tiles = {(0, 0)}
        self.selected_branch = "main"
        self.catalog_version = 3
        self.observer_local_x = 1
        self.observer_local_y = 1
        self.observer_facing = "east"
        self.observer_build_selection = "Beacon"
        self.observer_auto_reconcile = False
        self.teaching_example_loaded = True
        self.entity_definitions = {
            "Beacon": ("#38bdf8", "#bae6fd"),
            "Gateway": ("#f59e0b", "#fde68a"),
        }
        self.entity_metadata = {
            "Beacon": {
                "description": "Context marker",
                "rule_tag": "utility",
                "rule_tags": ["utility"],
                "default_color": "#38bdf8",
                "genome": build_beacon_default_genome(),
            },
            "Gateway": {
                "description": "Default structure",
                "rule_tag": "none",
                "rule_tags": ["none"],
                "default_color": "#f59e0b",
                "genome": build_default_genome(),
            },
        }
        self.invariant_boundary_candidates = [
            CandidateEvent(action="build_object", x=2, y=1, kind="Beacon"),
            CandidateEvent(action="destroy_object", x=4, y=4),
        ]
        self.frozen_gateway = build_minted_definition(
            kind="Gateway",
            catalog_version=3,
            palette=self.entity_definitions["Gateway"],
            metadata=self.entity_metadata["Gateway"],
        )
        payload = {
            "object_id": "obj-1",
            "kind": "Gateway",
            "x": 3,
            "y": 3,
            "invariant_state": {"state": "placed"},
            "minted_definition": self.frozen_gateway,
        }
        self.events = {
            "evt-1": CanonicalEvent(
                sequence=1,
                event_id="evt-1",
                event_family="structural",
                event_type="build_object",
                target_identity="obj-1",
                observer_identity="observer:alice",
                timestamp="t1",
                lineage_parent=None,
                causal_references=[],
                branch_hint="main",
                catalog_version=3,
                payload=payload,
            )
        }

    def _visible_canonical_state(self) -> ReplayBranchState:
        return ReplayBranchState(
            objects={
                "obj-1": ReplayObjectRecord(
                    object_id="obj-1",
                    kind="Gateway",
                    x=3,
                    y=3,
                    invariant_state={"state": "placed"},
                    minted_definition=self.frozen_gateway,
                )
            },
            event_count=1,
            head_event_id="evt-1",
        )

    def _current_branch_record(self) -> SimpleNamespace:
        return SimpleNamespace(head_event_id="evt-1")

    def _event_chain(self, event_id: str | None) -> list[CanonicalEvent]:
        return [self.events["evt-1"]] if event_id else []

    def _selected_head_event_id(self) -> str | None:
        return "evt-1"

    def _branch_label(self, branch_name: str | None) -> str:
        return "Main" if branch_name in {None, "main"} else str(branch_name)

    def _tile_in_front(self) -> tuple[int, int]:
        return (2, 1)

    def _tile_occupied(self, x: int, y: int, state: ReplayBranchState) -> bool:
        return any(record.x == x and record.y == y for record in state.objects.values())

    def _metadata_genome(self, meta: dict[str, object]) -> dict[str, object]:
        return meta["genome"]

    def _metadata_rule_tags(self, meta: dict[str, object]) -> list[str]:
        return list(meta["rule_tags"])


class LensAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = _FakeRuntimeApp()

    def test_canonical_pane_lens_shapes_summary_and_banner(self) -> None:
        lens = build_canonical_pane_lens(self.app)

        self.assertEqual(lens.summary_rows[0], ("Branch / Lineage", "Main"))
        self.assertIn(("Canonical Events", "1"), lens.summary_rows)
        self.assertIn(("Event Families", "structural"), lens.summary_rows)
        self.assertEqual(lens.banner.text, "PLAYGROUND READY  |  Teaching Example Loaded")

    def test_observer_pane_lens_shapes_divergence_and_context_hint(self) -> None:
        lens = build_observer_pane_lens(self.app)

        self.assertEqual(lens.summary_rows[4], ("Pending Submissions", "2"))
        self.assertEqual(lens.summary_rows[5], ("Status", "Ready To Reconcile"))
        self.assertIsNotNone(lens.divergence_banner)
        self.assertIn("requires causal context", lens.context_hint or "")
        self.assertIn("Beacon can pass this rule", lens.context_hint or "")
        self.assertIn("Try Beacon", lens.beacon_prompt)

    def test_build_modal_lens_emits_typed_requests_and_beacon_hint(self) -> None:
        lens = build_build_action_modal_lens(self.app)

        self.assertEqual(lens.target_tile, (2, 1))
        self.assertTrue(lens.teaching_example_loaded)
        beacon_card = next(card for card in lens.cards if card.kind == "Beacon")
        self.assertIsInstance(beacon_card.request, QueueBuildCandidateRequest)
        self.assertTrue(beacon_card.is_selected)
        self.assertIsNotNone(beacon_card.context_hint)
        self.assertIsNotNone(beacon_card.beacon_hint)

    def test_mint_action_modal_lens_marks_context_sensitive_kinds(self) -> None:
        lens = build_mint_action_modal_lens(self.app)

        beacon_option = next(option for option in lens.options if option.kind == "Beacon")
        gateway_option = next(option for option in lens.options if option.kind == "Gateway")
        self.assertIsInstance(beacon_option.request, MintFromServerRequest)
        self.assertTrue(beacon_option.requires_causal_context)
        self.assertFalse(gateway_option.requires_causal_context)

    def test_candidate_queue_lens_formats_build_and_destroy_lines(self) -> None:
        lens = build_candidate_queue_lens(self.app)

        self.assertEqual(lens.lines[0], "01. build Beacon @ (2, 1)")
        self.assertEqual(lens.lines[1], "02. destroy @ (4, 4)")


if __name__ == "__main__":
    unittest.main()
