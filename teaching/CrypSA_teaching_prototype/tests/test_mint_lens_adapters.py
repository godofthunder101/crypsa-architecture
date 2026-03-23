from __future__ import annotations

import json
import unittest

from mint.mint_catalog_store import build_beacon_default_genome, build_default_genome
from mint.mint_lens_adapters import build_mint_detail_lens, build_mint_entity_modal_lens


class _FakeMintApp:
    def __init__(self) -> None:
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

    def _meta_genome(self, meta: dict[str, object]) -> dict[str, object]:
        return meta["genome"]

    def _meta_rule_tags(self, meta: dict[str, object]) -> list[str]:
        raw_tags = meta.get("rule_tags", [])
        return list(raw_tags) if isinstance(raw_tags, list) else ["none"]


class MintLensAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = _FakeMintApp()

    def test_detail_lens_summarizes_selected_kind(self) -> None:
        lens = build_mint_detail_lens(self.app, "Beacon")

        self.assertEqual(lens.kind, "Beacon")
        self.assertIn("Tags: utility", lens.summary_text)
        self.assertIn("Allowed Actions:", lens.summary_text)
        self.assertIn("context=structural", lens.detail_text)
        self.assertEqual(lens.palette_fill, "#38bdf8")

    def test_create_modal_lens_uses_quick_start_and_default_genome_json(self) -> None:
        lens = build_mint_entity_modal_lens(self.app, "Create Mint Kind")

        self.assertEqual(lens.name_value, "")
        self.assertIsNotNone(lens.quick_start_text)
        self.assertEqual(lens.rule_tags, ["none"])
        self.assertEqual(json.loads(lens.genome_json_fields["valid_states"]), ["idle", "placed", "destroyed"])
        self.assertEqual(json.loads(lens.genome_json_fields["initial_invariant_state"]), {"state": "idle"})

    def test_edit_modal_lens_uses_selected_kind_values(self) -> None:
        lens = build_mint_entity_modal_lens(self.app, "Edit Mint Kind", original_kind="Beacon")

        self.assertEqual(lens.original_kind, "Beacon")
        self.assertEqual(lens.name_value, "Beacon")
        self.assertIsNone(lens.quick_start_text)
        self.assertEqual(lens.default_color, "#38bdf8")
        self.assertEqual(json.loads(lens.genome_json_fields["allowed_actions"]), ["observe", "build", "destroy", "mint"])


if __name__ == "__main__":
    unittest.main()
