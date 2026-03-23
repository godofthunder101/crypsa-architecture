from __future__ import annotations

import unittest
from dataclasses import dataclass

from crypsa.reconciliation import reconcile_invariant_boundary_candidates
from crypsa.runtime_models import CandidateEvent, ReplayBranchState
from mint.mint_catalog_store import build_default_genome
from mint.mint_models import build_minted_definition


class ReconciliationTests(unittest.TestCase):
    def test_reconcile_processes_known_actions_and_keeps_unknown_ones(self) -> None:
        class FakeRoot:
            def winfo_width(self) -> int:
                return 1000

            def winfo_height(self) -> int:
                return 700

        @dataclass(frozen=True)
        class FakeEvent:
            event_id: str

        class FakeApp:
            def __init__(self) -> None:
                self.root = FakeRoot()
                self.selected_branch = "main"
                self.invariant_boundary_candidates = [
                    CandidateEvent(action="build_object", kind="Beacon", x=2, y=8),
                    CandidateEvent(action="observe", x=0, y=0),
                ]
                self.server_logs: list[str] = []
                self.draw_calls = 0
                self.context_calls = 0
                self.accepted_payload_kinds: list[str] = []

            def _push_observer_log(self, message: str) -> None:
                pass

            def _push_server_log(self, message: str) -> None:
                self.server_logs.append(message)

            def _draw_scene(self, width: int, height: int) -> None:
                self.draw_calls += 1

            def _ensure_writable_branch(self) -> tuple[str, str | None]:
                return "main", None

            def _replay_branch_state(self, _head_event_id: str | None) -> ReplayBranchState:
                return ReplayBranchState(objects={}, event_count=0, head_event_id=None)

            def _current_causal_context_ids(self) -> list[str]:
                self.context_calls += 1
                return []

            def _catalog_minted_definition(self, kind: str) -> dict[str, object]:
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

            def _validate_and_transition_action(self, *args, **kwargs):
                return True, "", {"state": "idle"}

            def _mint_object_id(self, kind: str) -> str:
                return f"{kind.lower()}-0001"

            def _accept_canonical_event(self, branch_name, parent_event_id, event_type, event_family, target_identity, payload, causal_references=None):
                self.accepted_payload_kinds.append(str(payload["kind"]))
                return FakeEvent(event_id="evt-000001")

        app = FakeApp()

        reconcile_invariant_boundary_candidates(app)

        self.assertEqual(app.accepted_payload_kinds, ["Beacon"])
        self.assertEqual(len(app.invariant_boundary_candidates), 1)
        self.assertEqual(app.invariant_boundary_candidates[0].action, "observe")
        self.assertEqual(app.context_calls, 2)
        self.assertIn("reconcile complete -> accepted 1, rejected 0", app.server_logs)
        self.assertEqual(app.draw_calls, 1)


if __name__ == "__main__":
    unittest.main()
