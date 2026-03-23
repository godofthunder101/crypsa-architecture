from __future__ import annotations

from pathlib import Path


WIDTH = 1120
HEIGHT = 700

BG = "#09111f"
PANEL = "#111b31"
CARD = "#0c1428"
TEXT = "#e6eefc"
MUTED = "#8ea1c7"
ACCENT = "#6ee7f9"
GOOD = "#22c55e"
WARN = "#f59e0b"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = PROJECT_ROOT / "crypsa_teaching_prototype_state.json"
MINT_EDITOR_START_PATH = PROJECT_ROOT / "start-mint-editor.cmd"
TEACHING_EXAMPLE_PATH = PROJECT_ROOT / "fixtures" / "teaching_example.json"
