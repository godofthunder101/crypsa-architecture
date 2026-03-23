from __future__ import annotations

from typing import Callable

from mint.mint_catalog_store import normalize_genome
from mint.mint_models import MintedDefinition
from .runtime_models import CanonicalEvent, ReplayBranchState


def evaluate_invariant_rules(
    minted_definition: MintedDefinition,
    action: str,
    tile: tuple[int, int] | None,
    canonical_state: ReplayBranchState,
    current_state: dict[str, object] | None,
    parent_event_id: str | None,
    causal_reference_ids: list[str] | None,
    *,
    events: dict[str, CanonicalEvent],
    observer_identity: str,
    server_reserved_tiles: set[tuple[int, int]],
    initial_state_for_definition: Callable[[MintedDefinition], dict[str, object]],
    tile_occupied: Callable[[int, int, ReplayBranchState], bool],
) -> tuple[bool, str]:
    """Apply genome-level invariant checks before accepting a canonical event."""

    # Keep validation separate from controller orchestration: this function
    # reads normalized genome rules plus current runtime context and returns a
    # pure accept/reject result with a reason string.
    genome = normalize_genome(minted_definition.get("genome"), minted_definition)
    state_source = current_state if current_state is not None else initial_state_for_definition(minted_definition)
    current_label = str(state_source.get("state", "idle"))
    for rule in genome["invariant_rules"]:
        if not isinstance(rule, dict) or not bool(rule.get("enabled", True)):
            continue
        actions = rule.get("actions", [])
        if isinstance(actions, list) and actions:
            if action not in {str(item).lower() for item in actions}:
                continue
        applies_to_states = rule.get("applies_to_states", [])
        if isinstance(applies_to_states, list) and applies_to_states:
            if current_label not in {str(item) for item in applies_to_states}:
                continue
        rule_type = str(rule.get("rule_type", "")).lower()
        if rule_type == "deny_reserved_tiles" and tile in server_reserved_tiles:
            return False, str(rule.get("message", "reserved tiles are not canonical build targets"))
        if rule_type == "deny_occupied_tiles" and tile is not None and tile_occupied(tile[0], tile[1], canonical_state):
            return False, str(rule.get("message", "occupied tiles cannot accept another canonical object"))
        if rule_type == "require_parent_event_family":
            if parent_event_id not in events:
                return False, str(rule.get("message", "a parent canonical event is required"))
            required_family = str(rule.get("required_parent_event_family", "")).lower()
            actual_family = events[parent_event_id].event_family.lower()
            if required_family and actual_family != required_family:
                return False, str(rule.get("message", f"parent event must be family {required_family}"))
        if rule_type == "require_context_event_family":
            reference_ids = [ref for ref in (causal_reference_ids or []) if ref in events]
            if not reference_ids:
                default_message = "missing causal context: no contextual canonical events are available for this submission"
                return False, str(rule.get("message", default_message))
            required_family = str(rule.get("required_context_event_family", "")).lower()
            context_families = {events[ref].event_family.lower() for ref in reference_ids}
            if required_family and required_family not in context_families:
                available_families = ", ".join(sorted(context_families)) or "none"
                default_message = (
                    f"missing causal context family '{required_family}' "
                    f"(available context families: {available_families})"
                )
                return False, str(rule.get("message", default_message))
        if rule_type == "require_owner":
            required_owner = str(rule.get("required_owner", "")).strip()
            if required_owner and required_owner != observer_identity:
                return False, str(rule.get("message", f"event requires observer {required_owner}"))
        if rule_type == "state_threshold":
            threshold_key = str(rule.get("threshold_key", ""))
            raw_value = (current_state or {}).get(threshold_key)
            if not isinstance(raw_value, (int, float)):
                return False, str(rule.get("message", f"state key {threshold_key} is not numeric"))
            min_value = rule.get("threshold_min")
            max_value = rule.get("threshold_max")
            if isinstance(min_value, (int, float)) and raw_value < min_value:
                return False, str(rule.get("message", f"{threshold_key} below minimum threshold"))
            if isinstance(max_value, (int, float)) and raw_value > max_value:
                return False, str(rule.get("message", f"{threshold_key} above maximum threshold"))
    return True, ""
