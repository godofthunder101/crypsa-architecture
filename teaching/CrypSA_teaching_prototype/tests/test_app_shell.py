from __future__ import annotations

import unittest

from crypsa.app_shell import clear_widgets, handle_escape, main_window_hotkeys_enabled, run_main_window_hotkey


class AppShellTests(unittest.TestCase):
    def test_clear_widgets_destroys_widgets_and_empties_list(self) -> None:
        class FakeWidget:
            def __init__(self) -> None:
                self.destroyed = False

            def destroy(self) -> None:
                self.destroyed = True

        widgets = [FakeWidget(), FakeWidget()]

        clear_widgets(widgets)

        self.assertEqual(widgets, [])

    def test_main_window_hotkeys_enabled_checks_focus_owner(self) -> None:
        class FakeFocus:
            def __init__(self, owner) -> None:
                self._owner = owner

            def winfo_toplevel(self):
                return self._owner

        class FakeRoot:
            def __init__(self, focus) -> None:
                self._focus = focus

            def focus_get(self):
                return self._focus

        root = FakeRoot(None)
        self.assertTrue(main_window_hotkeys_enabled(root))

        foreign_owner = object()
        root = FakeRoot(FakeFocus(foreign_owner))
        self.assertFalse(main_window_hotkeys_enabled(root))

        root = FakeRoot(None)
        root._focus = FakeFocus(root)
        self.assertTrue(main_window_hotkeys_enabled(root))

    def test_run_hotkey_and_escape_only_fire_when_enabled(self) -> None:
        class FakeFocus:
            def __init__(self, owner) -> None:
                self._owner = owner

            def winfo_toplevel(self):
                return self._owner

        class FakeRoot:
            def __init__(self) -> None:
                self._focus = None

            def focus_get(self):
                return self._focus

        root = FakeRoot()
        calls: list[str] = []

        run_main_window_hotkey(root, lambda: calls.append("hotkey"))
        handle_escape(root, lambda: calls.append("escape"))

        self.assertEqual(calls, ["hotkey", "escape"])

        foreign_owner = object()
        root._focus = FakeFocus(foreign_owner)
        run_main_window_hotkey(root, lambda: calls.append("blocked-hotkey"))
        handle_escape(root, lambda: calls.append("blocked-escape"))

        self.assertEqual(calls, ["hotkey", "escape"])


if __name__ == "__main__":
    unittest.main()
