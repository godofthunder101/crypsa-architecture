from __future__ import annotations

import unittest

from crypsa.runtime_models import CanonicalEvent, ReplayBranchState
from crypsa.validation import evaluate_invariant_rules


def _initial_state(_minted_definition: dict[str, object]) -> dict[str, object]:
    return {"state": "idle"}


def _tile_occupied(x: int, y: int, canonical_state: ReplayBranchState) -> bool:
    return any(obj.x == x and obj.y == y for obj in canonical_state.objects.values())


class ValidationTests(unittest.TestCase):
    def test_reserved_tile_rule_rejects_candidate(self) -> None:
        minted_definition = {
            "genome": {
                "valid_states": ["idle"],
                "allowed_actions": ["build", "destroy", "mint", "observe"],
                "action_transitions": {
                    "observe": {"from_states": ["idle"], "to_state": "idle"},
                    "build": {"from_states": ["idle"], "to_state": "idle"},
                    "destroy": {"from_states": ["idle"], "to_state": "idle"},
                    "mint": {"from_states": ["idle"], "to_state": "idle"},
                },
                "invariant_rules": [{"rule_type": "deny_reserved_tiles", "enabled": True}],
                "initial_invariant_state": {"state": "idle"},
            }
        }

        allowed, reason = evaluate_invariant_rules(
            minted_definition,
            "build",
            (2, 2),
            ReplayBranchState(objects={}, event_count=0, head_event_id=None),
            None,
            None,
            [],
            events={},
            observer_identity="observer:alice",
            server_reserved_tiles={(2, 2)},
            initial_state_for_definition=_initial_state,
            tile_occupied=_tile_occupied,
        )

        self.assertFalse(allowed)
        self.assertIn("reserved", reason)

    def test_context_family_rule_accepts_when_context_exists(self) -> None:
        minted_definition = {
            "genome": {
                "valid_states": ["idle"],
                "allowed_actions": ["build", "destroy", "mint", "observe"],
                "action_transitions": {
                    "observe": {"from_states": ["idle"], "to_state": "idle"},
                    "build": {"from_states": ["idle"], "to_state": "idle"},
                    "destroy": {"from_states": ["idle"], "to_state": "idle"},
                    "mint": {"from_states": ["idle"], "to_state": "idle"},
                },
                "invariant_rules": [
                    {
                        "rule_type": "require_context_event_family",
                        "required_context_event_family": "structural",
                        "enabled": True,
                    }
                ],
                "initial_invariant_state": {"state": "idle"},
            }
        }
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
                payload={},
            ),
        }

        allowed, reason = evaluate_invariant_rules(
            minted_definition,
            "build",
            (4, 4),
            ReplayBranchState(objects={}, event_count=0, head_event_id=None),
            None,
            None,
            ["evt-000001"],
            events=events,
            observer_identity="observer:alice",
            server_reserved_tiles=set(),
            initial_state_for_definition=_initial_state,
            tile_occupied=_tile_occupied,
        )

        self.assertTrue(allowed)
        self.assertEqual(reason, "")

    def test_empty_current_state_does_not_fallback_to_initial_state(self) -> None:
        minted_definition = {
            "genome": {
                "valid_states": ["idle", "armed"],
                "allowed_actions": ["build", "destroy", "mint", "observe"],
                "action_transitions": {
                    "observe": {"from_states": ["idle", "armed"], "to_state": "idle"},
                    "build": {"from_states": ["idle", "armed"], "to_state": "idle"},
                    "destroy": {"from_states": ["idle", "armed"], "to_state": "idle"},
                    "mint": {"from_states": ["idle", "armed"], "to_state": "idle"},
                },
                "invariant_rules": [
                    {
                        "rule_type": "deny_reserved_tiles",
                        "enabled": True,
                        "applies_to_states": ["armed"],
                    }
                ],
                "initial_invariant_state": {"state": "armed"},
            }
        }

        allowed, reason = evaluate_invariant_rules(
            minted_definition,
            "build",
            (2, 2),
            ReplayBranchState(objects={}, event_count=0, head_event_id=None),
            {},
            None,
            [],
            events={},
            observer_identity="observer:alice",
            server_reserved_tiles={(2, 2)},
            initial_state_for_definition=lambda _definition: {"state": "armed"},
            tile_occupied=_tile_occupied,
        )

        self.assertTrue(allowed)
        self.assertEqual(reason, "")


if __name__ == "__main__":
    unittest.main()
