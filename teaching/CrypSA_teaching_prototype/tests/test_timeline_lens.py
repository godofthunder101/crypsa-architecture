from __future__ import annotations

import unittest

from crypsa.crypsa_event_graph import build_branch_rows
from crypsa.crypsa_lens_adapters import TimelineNodeLens, _connector_target_event_id, build_timeline_modal_lens
from crypsa.crypsa_action_requests import SelectTimelineEventRequest
from crypsa.runtime_models import CanonicalEvent


class TimelineLensTests(unittest.TestCase):
    def test_branch_rows_include_forked_lineage(self) -> None:
        events = {
            "evt-000001": CanonicalEvent(1, "evt-000001", "structural", "mint_object", "obj-1", "observer:alice", "t1", None, [], "main", 1, {}),
            "evt-000002": CanonicalEvent(2, "evt-000002", "structural", "build_object", "obj-2", "observer:alice", "t2", "evt-000001", [], "main", 1, {}),
            "evt-000003": CanonicalEvent(3, "evt-000003", "structural", "build_object", "obj-3", "observer:alice", "t3", "evt-000002", [], "main", 1, {}),
            "evt-000004": CanonicalEvent(4, "evt-000004", "structural", "build_object", "obj-4", "observer:alice", "t4", "evt-000001", [], "branch:evt-000001:evt-000004", 1, {}),
        }

        rows = build_branch_rows(events)

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].name, "main")
        self.assertEqual(rows[1].fork_from_event_id, "evt-000001")

    def test_connector_targets_first_divergent_event(self) -> None:
        nodes = [
            TimelineNodeLens(
                event_id="evt-000001",
                sequence_text="1",
                event_type_text="build",
                fill="#1d4ed8",
                outline="#f8fafc",
                outline_width=2,
                select_request=SelectTimelineEventRequest(branch_name="branch:evt-000001:evt-000004", event_id="evt-000001"),
            ),
            TimelineNodeLens(
                event_id="evt-000004",
                sequence_text="4",
                event_type_text="build",
                fill="#1d4ed8",
                outline="#67e8f9",
                outline_width=2,
                select_request=SelectTimelineEventRequest(branch_name="branch:evt-000001:evt-000004", event_id="evt-000004"),
            ),
        ]

        self.assertEqual(_connector_target_event_id(nodes, "evt-000001"), "evt-000004")

    def test_build_timeline_modal_lens_includes_branch_rows(self) -> None:
        class FakeApp:
            def __init__(self) -> None:
                self.selected_branch = "main"
                self.events = {
                    "evt-000001": CanonicalEvent(1, "evt-000001", "structural", "mint_object", "obj-1", "observer:alice", "t1", None, [], "main", 1, {}),
                    "evt-000002": CanonicalEvent(2, "evt-000002", "structural", "build_object", "obj-2", "observer:alice", "t2", "evt-000001", ["evt-000001"], "main", 1, {}),
                    "evt-000003": CanonicalEvent(3, "evt-000003", "structural", "build_object", "obj-3", "observer:alice", "t3", "evt-000001", ["evt-000001"], "branch:evt-000001:evt-000003", 1, {}),
                }

            def _branch_rows(self):
                return build_branch_rows(self.events)

            def _timeline_events_for_branch(self, branch):
                head = branch.head_event_id
                chain = []
                while isinstance(head, str) and head in self.events:
                    record = self.events[head]
                    chain.append(record)
                    head = record.lineage_parent
                chain.reverse()
                return chain

            def _timeline_connector_origin(self, branch):
                if branch.parent_branch is None or branch.fork_from_event_id is None:
                    return None
                return branch.parent_branch, branch.fork_from_event_id

            def _branch_label(self, branch_name):
                if branch_name in {None, "main"}:
                    return "Main"
                return str(branch_name)

            def _selected_head_event_id(self):
                return "evt-000002"

        lens = build_timeline_modal_lens(FakeApp())

        self.assertEqual(len(lens.rows), 2)
        self.assertEqual(lens.rows[1].connector_target_event_id, "evt-000003")


if __name__ == "__main__":
    unittest.main()
