from __future__ import annotations

import unittest

from crypsa.crypsa_action_requests import (
    ClearCandidatesRequest,
    QueueBuildCandidateRequest,
    SelectHistoryEventRequest,
    SelectTimelineEventRequest,
)
from crypsa.request_dispatch import dispatch_action_request


class RequestDispatchTests(unittest.TestCase):
    def test_dispatch_routes_build_request_to_controller_method(self) -> None:
        class FakeApp:
            def __init__(self) -> None:
                self.calls: list[tuple[str, object]] = []

            def _queue_build_candidate(self, kind, modal) -> None:
                self.calls.append(("build", kind))

        app = FakeApp()

        dispatch_action_request(app, QueueBuildCandidateRequest(kind="Beacon"))

        self.assertEqual(app.calls, [("build", "Beacon")])

    def test_dispatch_routes_timeline_selection_without_modal(self) -> None:
        class FakeApp:
            def __init__(self) -> None:
                self.calls: list[tuple[str, str]] = []

            def _select_timeline_event(self, branch_name: str, event_id: str) -> None:
                self.calls.append((branch_name, event_id))

        app = FakeApp()

        dispatch_action_request(app, SelectTimelineEventRequest(branch_name="main", event_id="evt-000001"))

        self.assertEqual(app.calls, [("main", "evt-000001")])

    def test_dispatch_rejects_clear_candidates_without_modal(self) -> None:
        class FakeApp:
            def _clear_candidates(self, modal) -> None:
                raise AssertionError("should not be called")

        with self.assertRaisesRegex(ValueError, "requires the originating modal"):
            dispatch_action_request(FakeApp(), ClearCandidatesRequest())

    def test_dispatch_rejects_history_selection_without_modal(self) -> None:
        class FakeApp:
            def _select_history_event(self, event_id: str, preferred_branch_name: str | None, modal) -> None:
                raise AssertionError("should not be called")

        with self.assertRaisesRegex(ValueError, "requires the originating modal"):
            dispatch_action_request(
                FakeApp(),
                SelectHistoryEventRequest(event_id="evt-000001", preferred_branch_name="main"),
            )

    def test_dispatch_rejects_unknown_request_type(self) -> None:
        class FakeRequest:
            pass

        with self.assertRaisesRegex(TypeError, "Unhandled action request"):
            dispatch_action_request(object(), FakeRequest())  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
