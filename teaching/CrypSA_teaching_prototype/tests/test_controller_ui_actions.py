from __future__ import annotations

import unittest
from unittest.mock import patch

from crypsa.controller_ui_actions import center_observer_near_canonical_state, reload_catalog, try_beacon_path
from crypsa.runtime_models import CandidateEvent
from crypsa.runtime_models import ReplayBranchState


class ControllerUiActionsTests(unittest.TestCase):
    def test_reload_catalog_preserves_selection_when_kind_still_exists(self) -> None:
        class FakeRoot:
            def winfo_width(self) -> int:
                return 1000

            def winfo_height(self) -> int:
                return 700

        class FakeApp:
            def __init__(self) -> None:
                self.root = FakeRoot()
                self.observer_build_selection = "Beacon"
                self.entity_definitions = {"Beacon": ("#1", "#2")}
                self.entity_metadata = {"Beacon": {}}
                self.catalog_version = 1
                self.rule_tags = ["none"]
                self.logs: list[str] = []
                self.draw_calls = 0

            def _push_observer_log(self, message: str) -> None:
                self.logs.append(message)

            def _draw_scene(self, width: int, height: int) -> None:
                self.draw_calls += 1

        app = FakeApp()

        with patch(
            "crypsa.controller_ui_actions.load_catalog",
            return_value=({"Beacon": ("#a", "#b"), "Gateway": ("#c", "#d")}, {"Beacon": {}, "Gateway": {}}, 7, ["none", "utility"]),
        ):
            reload_catalog(app)

        self.assertEqual(app.observer_build_selection, "Beacon")
        self.assertEqual(app.catalog_version, 7)
        self.assertIn("catalog reloaded -> v7", app.logs)
        self.assertEqual(app.draw_calls, 1)

    def test_reload_catalog_resets_runtime_when_removed_kind_is_still_used(self) -> None:
        class FakeRoot:
            def winfo_width(self) -> int:
                return 1000

            def winfo_height(self) -> int:
                return 700

        class FakeEvent:
            def __init__(self, kind: str) -> None:
                self.payload = {"kind": kind}

        class FakeApp:
            def __init__(self) -> None:
                self.root = FakeRoot()
                self.observer_build_selection = "Beacon"
                self.entity_definitions = {"Beacon": ("#1", "#2"), "Gateway": ("#3", "#4")}
                self.entity_metadata = {"Beacon": {}, "Gateway": {}}
                self.catalog_version = 1
                self.rule_tags = ["none"]
                self.invariant_boundary_candidates = [CandidateEvent(action="build_object", kind="Beacon", x=2, y=2)]
                self.events = {"evt-1": FakeEvent("Beacon")}
                self.logs: list[str] = []
                self.server_logs: list[str] = []
                self.draw_calls = 0
                self.reset_calls = 0
                self.save_calls = 0

            def _push_observer_log(self, message: str) -> None:
                self.logs.append(message)

            def _push_server_log(self, message: str) -> None:
                self.server_logs.append(message)

            def _draw_scene(self, width: int, height: int) -> None:
                self.draw_calls += 1

            def _reset_runtime_state(self) -> None:
                self.reset_calls += 1
                self.invariant_boundary_candidates.clear()
                self.events = {}

            def _save_state(self) -> None:
                self.save_calls += 1

        app = FakeApp()

        with patch(
            "crypsa.controller_ui_actions.load_catalog",
            return_value=({"Gateway": ("#c", "#d")}, {"Gateway": {}}, 7, ["none", "utility"]),
        ):
            reload_catalog(app)

        self.assertEqual(app.reset_calls, 1)
        self.assertEqual(app.save_calls, 1)
        self.assertEqual(app.observer_build_selection, "Gateway")
        self.assertIn("catalog reloaded -> v7", app.logs)
        self.assertIn("teaching world reset to baseline", app.logs[-1])
        self.assertIn("runtime reset to baseline", app.server_logs[-1])

    def test_try_beacon_path_loads_example_then_opens_build_modal(self) -> None:
        class FakeRoot:
            def winfo_width(self) -> int:
                return 1000

            def winfo_height(self) -> int:
                return 700

        class FakeApp:
            def __init__(self) -> None:
                self.root = FakeRoot()
                self.teaching_example_loaded = False
                self.observer_build_selection = "Gateway"
                self.logs: list[str] = []
                self.draw_calls = 0
                self.loaded = 0
                self.opened = 0

            def _load_teaching_example(self, modal=None) -> None:
                self.loaded += 1
                self.teaching_example_loaded = True

            def _preferred_kind(self, preferred_names: list[str]) -> str:
                return preferred_names[0]

            def _push_observer_log(self, message: str) -> None:
                self.logs.append(message)

            def _draw_scene(self, width: int, height: int) -> None:
                self.draw_calls += 1

            def _open_build_modal(self) -> None:
                self.opened += 1

        app = FakeApp()

        try_beacon_path(app)

        self.assertEqual(app.loaded, 1)
        self.assertEqual(app.opened, 1)
        self.assertEqual(app.observer_build_selection, "Beacon")
        self.assertIn("teaching path prepared -> build chooser focused on Beacon", app.logs)

    def test_center_observer_near_canonical_state_updates_position(self) -> None:
        class FakeRoot:
            def winfo_width(self) -> int:
                return 1000

            def winfo_height(self) -> int:
                return 700

        class FakeApp:
            def __init__(self) -> None:
                self.root = FakeRoot()
                self.grid_size = 10
                self.observer_local_x = 0
                self.observer_local_y = 0
                self.logs: list[str] = []
                self.draw_calls = 0

            def _visible_canonical_state(self) -> ReplayBranchState:
                return ReplayBranchState(objects={}, event_count=0, head_event_id=None)

            def _push_observer_log(self, message: str) -> None:
                self.logs.append(message)

            def _draw_scene(self, width: int, height: int) -> None:
                self.draw_calls += 1

        app = FakeApp()

        center_observer_near_canonical_state(app)

        self.assertEqual((app.observer_local_x, app.observer_local_y), (4, 4))
        self.assertEqual(app.draw_calls, 1)
        self.assertIn("observer view recentered near the selected canonical state -> (4, 4)", app.logs)


if __name__ == "__main__":
    unittest.main()
