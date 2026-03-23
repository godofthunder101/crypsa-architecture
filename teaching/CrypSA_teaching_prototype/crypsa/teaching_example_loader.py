from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TeachingExampleStep:
    step_id: str
    branch_source: str
    parent_step_id: str | None
    tile: tuple[int, int]
    event_type: str
    action_name: str
    kind_preferences: list[str]


@dataclass(frozen=True)
class TeachingExampleFinalState:
    selected_branch: str
    selected_head_step_id: str
    observer_position: tuple[int, int]
    observer_facing: str
    build_selection_step_id: str


@dataclass(frozen=True)
class TeachingExamplePlan:
    steps: list[TeachingExampleStep]
    final_state: TeachingExampleFinalState


def load_teaching_example_plan(path: Path) -> TeachingExamplePlan:
    """Load and normalize the fixture-backed teaching example plan."""

    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Teaching example fixture root must be an object.")
    raw_preferences = raw.get("kind_preferences")
    raw_steps = raw.get("steps")
    raw_final_state = raw.get("final_state")
    if not isinstance(raw_preferences, dict) or not isinstance(raw_steps, list) or not isinstance(raw_final_state, dict):
        raise ValueError("Teaching example fixture must define kind_preferences, steps, and final_state.")

    steps: list[TeachingExampleStep] = []
    for item in raw_steps:
        if not isinstance(item, dict):
            raise ValueError("Teaching example steps must be objects.")
        step_id = str(item.get("step_id", "")).strip()
        branch_source = str(item.get("branch_source", "")).strip()
        parent_step_id = item.get("parent_step_id")
        raw_tile = item.get("tile")
        event_type = str(item.get("event_type", "")).strip()
        action_name = str(item.get("action_name", "")).strip()
        if (
            not step_id
            or not branch_source
            or not isinstance(raw_tile, list)
            or len(raw_tile) != 2
            or not all(isinstance(value, int) for value in raw_tile)
            or not event_type
            or not action_name
        ):
            raise ValueError("Teaching example step is missing required fields.")
        preferences = raw_preferences.get(step_id, [])
        if not isinstance(preferences, list) or not all(isinstance(name, str) for name in preferences):
            raise ValueError(f"Teaching example step {step_id} has invalid kind preferences.")
        steps.append(
            TeachingExampleStep(
                step_id=step_id,
                branch_source=branch_source,
                parent_step_id=(str(parent_step_id) if isinstance(parent_step_id, str) and parent_step_id.strip() else None),
                tile=(raw_tile[0], raw_tile[1]),
                event_type=event_type,
                action_name=action_name,
                kind_preferences=[name for name in preferences if name.strip()],
            )
        )

    selected_branch = str(raw_final_state.get("selected_branch", "")).strip()
    selected_head_step_id = str(raw_final_state.get("selected_head_step_id", "")).strip()
    raw_observer_position = raw_final_state.get("observer_position")
    observer_facing = str(raw_final_state.get("observer_facing", "")).strip()
    build_selection_step_id = str(raw_final_state.get("build_selection_step_id", "")).strip()
    if (
        not selected_branch
        or not selected_head_step_id
        or not isinstance(raw_observer_position, list)
        or len(raw_observer_position) != 2
        or not all(isinstance(value, int) for value in raw_observer_position)
        or not observer_facing
        or not build_selection_step_id
    ):
        raise ValueError("Teaching example final_state is missing required fields.")

    return TeachingExamplePlan(
        steps=steps,
        final_state=TeachingExampleFinalState(
            selected_branch=selected_branch,
            selected_head_step_id=selected_head_step_id,
            observer_position=(raw_observer_position[0], raw_observer_position[1]),
            observer_facing=observer_facing,
            build_selection_step_id=build_selection_step_id,
        ),
    )
