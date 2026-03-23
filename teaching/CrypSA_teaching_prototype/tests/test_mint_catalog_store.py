from __future__ import annotations

import unittest

from mint.mint_catalog_store import _normalize_text_list, normalize_genome
from mint.mint_models import build_minted_definition


class MintCatalogStoreTests(unittest.TestCase):
    def test_normalize_text_list_accepts_json_array_and_json_string(self) -> None:
        self.assertEqual(_normalize_text_list('["build", "mint"]', []), ["build", "mint"])
        self.assertEqual(_normalize_text_list('"build"', []), ["build"])
        self.assertEqual(_normalize_text_list("build, mint", []), ["build", "mint"])

    def test_normalize_genome_rejects_unknown_allowed_actions(self) -> None:
        with self.assertRaisesRegex(ValueError, "Allowed actions contain unknown action names."):
            normalize_genome(
                {
                    "valid_states": ["idle"],
                    "allowed_actions": ["build", "unknown"],
                    "action_transitions": {
                        "observe": {"from_states": ["idle"], "to_state": "idle"},
                        "build": {"from_states": ["idle"], "to_state": "idle"},
                        "destroy": {"from_states": ["idle"], "to_state": "idle"},
                        "mint": {"from_states": ["idle"], "to_state": "idle"},
                    },
                    "invariant_rules": [],
                    "initial_invariant_state": {"state": "idle"},
                }
            )

    def test_build_minted_definition_freezes_expected_fields(self) -> None:
        genome = normalize_genome(
            {
                "valid_states": ["idle"],
                "allowed_actions": ["observe", "build", "destroy", "mint"],
                "action_transitions": {
                    "observe": {"from_states": ["idle"], "to_state": "idle"},
                    "build": {"from_states": ["idle"], "to_state": "idle"},
                    "destroy": {"from_states": ["idle"], "to_state": "idle"},
                    "mint": {"from_states": ["idle"], "to_state": "idle"},
                },
                "invariant_rules": [],
                "initial_invariant_state": {"state": "idle"},
            }
        )
        frozen = build_minted_definition(
            kind="Beacon",
            catalog_version=7,
            palette=("#38bdf8", "#bae6fd"),
            metadata={
                "description": "Context marker",
                "rule_tag": "utility",
                "rule_tags": ["utility"],
                "default_color": "#38bdf8",
                "genome": genome,
            },
        )

        self.assertEqual(frozen["kind"], "Beacon")
        self.assertEqual(frozen["catalog_version"], 7)
        self.assertEqual(frozen["palette"], ["#38bdf8", "#bae6fd"])
        self.assertEqual(frozen["rule_tags"], ["utility"])


if __name__ == "__main__":
    unittest.main()
