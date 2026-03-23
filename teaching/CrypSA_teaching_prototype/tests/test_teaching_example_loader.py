from __future__ import annotations

import unittest

from crypsa.crypsa_teaching_theme import TEACHING_EXAMPLE_PATH
from crypsa.teaching_example_loader import load_teaching_example_plan


class TeachingExampleLoaderTests(unittest.TestCase):
    def test_fixture_loads_expected_shape(self) -> None:
        plan = load_teaching_example_plan(TEACHING_EXAMPLE_PATH)

        self.assertEqual(len(plan.steps), 5)
        self.assertEqual(plan.steps[0].step_id, "main_1")
        self.assertEqual(plan.steps[-1].step_id, "fork_2")
        self.assertEqual(plan.final_state.selected_head_step_id, "main_3")
        self.assertEqual(plan.final_state.build_selection_step_id, "fork_2")


if __name__ == "__main__":
    unittest.main()
