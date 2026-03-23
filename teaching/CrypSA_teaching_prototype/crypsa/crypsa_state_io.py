from __future__ import annotations

import json
from pathlib import Path


def load_runtime_state(path: Path) -> dict[str, object] | None:
    """Read the current-schema runtime state from disk."""

    if not path.exists():
        return None
    # Keep persistence boring on purpose: read one JSON object, verify the root
    # shape, and hand the rest back to the runtime orchestration layer.
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("State root must be an object.")
    return data


def save_runtime_state(path: Path, data: dict[str, object]) -> None:
    """Persist the runtime state exactly as the prototype currently uses it."""

    # The runtime owns schema meaning. This module only serializes the exact
    # structure it is given so state I/O stays easy to audit. If save/load
    # behavior feels confusing, read Runtime_Schema.md first and then return to
    # this file; this module is intentionally the boring boundary.
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
