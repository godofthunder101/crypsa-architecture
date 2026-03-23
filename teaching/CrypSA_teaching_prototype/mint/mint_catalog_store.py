from __future__ import annotations

import json
from pathlib import Path

from .mint_models import EntityDefinitions, EntityMetadata, Genome, InvariantRule, ActionTransition

CATALOG_PATH = Path(__file__).resolve().parent.parent / "mint_catalog.json"
DEFAULT_ENTITY_DEFINITIONS = {
    "Gateway": ("#f59e0b", "#fde68a"),
    "Relay": ("#22c55e", "#bbf7d0"),
    "Archive": ("#a78bfa", "#ddd6fe"),
    "Beacon": ("#38bdf8", "#bae6fd"),
}
MINT_ENTITY_DEFAULT_COLORS = [
    "#ef4444", "#f97316", "#f59e0b", "#eab308", "#84cc16", "#22c55e", "#10b981", "#14b8a6",
    "#06b6d4", "#0ea5e9", "#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#d946ef", "#ec4899",
    "#f43f5e", "#fb7185", "#fca5a5", "#fdba74", "#fcd34d", "#fde68a", "#bef264", "#86efac",
    "#6ee7b7", "#5eead4", "#67e8f9", "#7dd3fc", "#93c5fd", "#a5b4fc", "#c4b5fd", "#f9a8d4",
]
DEFAULT_RULE_TAGS = ["none", "navigation", "utility", "impassable"]
GENOME_ACTIONS = ["observe", "build", "destroy", "mint"]
INVARIANT_RULE_TYPES = [
    "deny_reserved_tiles",
    "deny_occupied_tiles",
    "require_owner",
    "require_parent_event_family",
    "require_context_event_family",
    "state_threshold",
]


def build_default_genome() -> Genome:
    return {
        "valid_states": ["idle", "placed", "destroyed"],
        "allowed_actions": list(GENOME_ACTIONS),
        "action_transitions": {
            "observe": {"from_states": ["idle", "placed", "destroyed"]},
            "mint": {"from_states": ["idle"], "to_state": "placed"},
            "build": {"from_states": ["idle"], "to_state": "placed"},
            "destroy": {"from_states": ["idle", "placed"], "to_state": "destroyed"},
        },
        "invariant_rules": [
            {"rule_type": "deny_reserved_tiles", "actions": ["build", "mint"], "enabled": True},
            {"rule_type": "deny_occupied_tiles", "actions": ["build", "mint"], "enabled": True},
        ],
        "initial_invariant_state": {"state": "idle"},
    }


def build_beacon_default_genome() -> Genome:
    genome = build_default_genome()
    genome["invariant_rules"].append(
        {
            "rule_type": "require_context_event_family",
            "actions": ["build", "mint"],
            "enabled": True,
            "message": "Beacon requires structural causal context before it can become canonical.",
            "required_context_event_family": "structural",
        }
    )
    return genome


def build_default_metadata(definitions: EntityDefinitions) -> dict[str, EntityMetadata]:
    metadata: dict[str, EntityMetadata] = {}
    for name in definitions:
        if name == "Beacon":
            metadata[name] = {
                "description": "Context-aware marker that requires an existing structural event in causal context.",
                "rule_tag": "utility",
                "rule_tags": ["utility"],
                "default_color": "#38bdf8",
                "genome": build_beacon_default_genome(),
            }
            continue
        metadata[name] = {
            "description": "",
            "rule_tag": "none",
            "rule_tags": ["none"],
            "default_color": "",
            "genome": build_default_genome(),
        }
    return metadata


def palette_for_entity_name(name: str) -> tuple[str, str]:
    seed = sum(ord(ch) for ch in name)
    fills = ["#f59e0b", "#22c55e", "#a78bfa", "#38bdf8", "#fb7185", "#f97316", "#14b8a6"]
    outlines = ["#fde68a", "#bbf7d0", "#ddd6fe", "#bae6fd", "#fecdd3", "#fed7aa", "#99f6e4"]
    index = seed % len(fills)
    return fills[index], outlines[index]


def normalize_hex_color(raw_color: str) -> str:
    candidate = raw_color.strip()
    if not candidate:
        return ""
    if not candidate.startswith("#"):
        candidate = f"#{candidate}"
    if len(candidate) != 7:
        return ""
    try:
        int(candidate[1:], 16)
    except ValueError:
        return ""
    return candidate.lower()


def _normalize_rule_tag(raw_tag: str) -> str:
    cleaned = " ".join(part for part in raw_tag.strip().split() if part)
    return cleaned or "none"


def _clean_entity_name(raw_name: str) -> str:
    """Normalize one Mint kind name before validating it."""

    return " ".join(part for part in raw_name.strip().split() if part)


def normalize_rule_tags(raw_tags: object) -> list[str]:
    parsed_tags: list[str] = []
    if isinstance(raw_tags, list):
        for item in raw_tags:
            if not isinstance(item, str):
                continue
            normalized = _normalize_rule_tag(item)
            if normalized not in parsed_tags:
                parsed_tags.append(normalized)
    elif isinstance(raw_tags, str):
        normalized = _normalize_rule_tag(raw_tags)
        if normalized:
            parsed_tags.append(normalized)
    return parsed_tags or ["none"]


def _normalize_text_list(raw_values: object, fallback: list[str]) -> list[str]:
    parsed: list[str] = []
    if isinstance(raw_values, list):
        candidates = raw_values
    elif isinstance(raw_values, str):
        stripped = raw_values.strip()
        if not stripped:
            candidates = []
        else:
            try:
                decoded = json.loads(stripped)
            except json.JSONDecodeError:
                decoded = None
            if isinstance(decoded, list):
                candidates = decoded
            elif isinstance(decoded, str):
                candidates = [decoded]
            else:
                candidates = raw_values.split(",")
    else:
        candidates = []
    for item in candidates:
        if not isinstance(item, str):
            continue
        cleaned = " ".join(part for part in item.strip().split() if part)
        if cleaned and cleaned not in parsed:
            parsed.append(cleaned)
    return parsed or list(fallback)


def normalize_initial_invariant_state(raw_state: object, valid_states: list[str]) -> dict[str, object]:
    if isinstance(raw_state, str):
        parsed = json.loads(raw_state)
    else:
        parsed = raw_state
    if not isinstance(parsed, dict):
        raise ValueError("Initial invariant state must be a JSON object.")
    state = {str(key): value for key, value in parsed.items()}
    state_label = str(state.get("state", ""))
    if state_label not in valid_states:
        raise ValueError("Initial invariant state must reference a valid state.")
    return state


def _json_object_or_value(raw_value: object, error_message: str) -> object:
    """Parse JSON text when needed, then return the decoded value."""

    value = json.loads(raw_value) if isinstance(raw_value, str) else raw_value
    if value is None:
        raise ValueError(error_message)
    return value


def _normalized_action_name(action_name: object) -> str:
    """Normalize one genome action name and verify it is supported."""

    if not isinstance(action_name, str):
        raise ValueError("Action transition names must be strings.")
    normalized_action = action_name.strip().lower()
    if normalized_action not in GENOME_ACTIONS:
        raise ValueError(f"Unknown genome action: {action_name}")
    return normalized_action


def _normalized_transition(raw_transition: object, action_name: str, valid_states: list[str]) -> ActionTransition:
    """Normalize one action transition entry."""

    if not isinstance(raw_transition, dict):
        raise ValueError(f"Transition for {action_name} must be an object.")
    from_states = _normalize_text_list(raw_transition.get("from_states"), valid_states)
    invalid_from = [state for state in from_states if state not in valid_states]
    if invalid_from:
        raise ValueError(f"Transition for {action_name} references invalid from_states.")
    transition: ActionTransition = {"from_states": from_states}
    to_state = raw_transition.get("to_state")
    if to_state is not None:
        if not isinstance(to_state, str) or to_state.strip() not in valid_states:
            raise ValueError(f"Transition for {action_name} has invalid to_state.")
        transition["to_state"] = to_state.strip()
    return transition


def _required_string_rule_fields(raw_rule: dict[str, object], normalized: InvariantRule) -> None:
    """Copy the supported string-valued invariant rule fields after validation."""

    for key in ("threshold_key", "message", "required_parent_event_family", "required_context_event_family", "required_owner"):
        value = raw_rule.get(key)
        if value is None:
            continue
        if not isinstance(value, str):
            raise ValueError(f"Invariant rule field {key} must be a string.")
        cleaned = " ".join(part for part in value.strip().split() if part)
        if cleaned:
            normalized[key] = cleaned


def _required_numeric_rule_fields(raw_rule: dict[str, object], normalized: InvariantRule) -> None:
    """Copy the supported numeric invariant rule fields after validation."""

    for key in ("threshold_min", "threshold_max"):
        value = raw_rule.get(key)
        if value is None:
            continue
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invariant rule field {key} must be numeric.")
        normalized[key] = value


def normalize_action_transitions(raw_transitions: object, valid_states: list[str]) -> dict[str, ActionTransition]:
    source = _json_object_or_value(raw_transitions, "Action transitions must be a JSON object.")
    if not isinstance(source, dict):
        raise ValueError("Action transitions must be a JSON object.")
    parsed: dict[str, ActionTransition] = {}
    for action_name, raw_transition in source.items():
        normalized_action = _normalized_action_name(action_name)
        parsed[normalized_action] = _normalized_transition(raw_transition, str(action_name), valid_states)
    for action_name in GENOME_ACTIONS:
        if action_name not in parsed:
            raise ValueError(f"Missing transition for required action: {action_name}")
    return parsed


def _normalize_invariant_rule_entry(raw_rule: object, valid_states: list[str]) -> InvariantRule:
    if not isinstance(raw_rule, dict):
        raise ValueError("Invariant rules must be objects.")
    rule_type = str(raw_rule.get("rule_type", "")).strip()
    if rule_type not in INVARIANT_RULE_TYPES:
        raise ValueError(f"Unknown invariant rule type: {rule_type}")
    normalized: InvariantRule = {
        "rule_type": rule_type,
        "enabled": bool(raw_rule.get("enabled", True)),
    }
    actions = _normalize_text_list(raw_rule.get("actions"), [])
    if actions:
        invalid_actions = [action for action in actions if action.lower() not in GENOME_ACTIONS]
        if invalid_actions:
            raise ValueError(f"Invariant rule {rule_type} references unknown actions.")
        normalized["actions"] = [action.lower() for action in actions]
    applies_to_states = _normalize_text_list(raw_rule.get("applies_to_states"), [])
    if applies_to_states:
        invalid_states = [state for state in applies_to_states if state not in valid_states]
        if invalid_states:
            raise ValueError(f"Invariant rule {rule_type} references invalid states.")
        normalized["applies_to_states"] = applies_to_states
    _required_string_rule_fields(raw_rule, normalized)
    _required_numeric_rule_fields(raw_rule, normalized)
    return normalized


def normalize_invariant_rules(raw_rules: object, valid_states: list[str]) -> list[InvariantRule]:
    source = _json_object_or_value(raw_rules, "Invariant rules must be a JSON array.")
    if not isinstance(source, list):
        raise ValueError("Invariant rules must be a JSON array.")
    parsed: list[InvariantRule] = []
    for raw_rule in source:
        normalized = _normalize_invariant_rule_entry(raw_rule, valid_states)
        if normalized not in parsed:
            parsed.append(normalized)
    return parsed


def normalize_genome(raw_genome: object, metadata: dict[str, object] | None = None) -> Genome:
    metadata = metadata or {}
    if not isinstance(raw_genome, dict):
        raise ValueError("Genome must be an object.")
    # Read genome normalization as five fixed stages: states, actions,
    # transitions, invariant rules, then the initial invariant state. Keeping
    # that order stable makes the editor, defaults, and runtime easier to
    # compare mentally.
    default_genome = build_default_genome()
    valid_states = _normalize_text_list(raw_genome.get("valid_states"), list(default_genome["valid_states"]))
    allowed_actions = _normalize_text_list(raw_genome.get("allowed_actions"), list(GENOME_ACTIONS))
    normalized_actions = [action.lower() for action in allowed_actions]
    invalid_actions = [action for action in normalized_actions if action not in GENOME_ACTIONS]
    if invalid_actions:
        raise ValueError("Allowed actions contain unknown action names.")
    return {
        "valid_states": valid_states,
        "allowed_actions": normalized_actions,
        "action_transitions": normalize_action_transitions(raw_genome.get("action_transitions"), valid_states),
        "invariant_rules": normalize_invariant_rules(raw_genome.get("invariant_rules"), valid_states),
        "initial_invariant_state": normalize_initial_invariant_state(raw_genome.get("initial_invariant_state"), valid_states),
    }


def _normalize_catalog_metadata(name: str, meta: object) -> EntityMetadata:
    if not isinstance(meta, dict):
        raise ValueError(f"Entity metadata for {name} must be an object.")
    rule_tags = normalize_rule_tags(meta["rule_tags"])
    genome = normalize_genome(meta["genome"], meta)
    return {
        "description": str(meta.get("description", "")).strip(),
        "rule_tag": rule_tags[0],
        "rule_tags": rule_tags,
        "default_color": normalize_hex_color(str(meta.get("default_color", ""))),
        "genome": genome,
    }


def _default_catalog(version: int = 1) -> tuple[EntityDefinitions, dict[str, EntityMetadata], int, list[str]]:
    """Return the fallback catalog used for missing or empty on-disk state."""

    definitions = dict(DEFAULT_ENTITY_DEFINITIONS)
    return definitions, build_default_metadata(definitions), max(1, version), list(DEFAULT_RULE_TAGS)


def _load_catalog_root(path: Path) -> dict[str, object]:
    """Read and validate the raw catalog root object from disk."""

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Catalog root must be an object.")
    return data


def _load_entity_definitions(raw_definitions: object) -> EntityDefinitions:
    """Normalize the entity_definitions map from the catalog file."""

    if not isinstance(raw_definitions, dict):
        raise ValueError("entity_definitions must be an object.")
    definitions: EntityDefinitions = {}
    for name, palette in raw_definitions.items():
        if not isinstance(name, str) or not isinstance(palette, list) or len(palette) != 2:
            raise ValueError("Each entity definition must map a name to a two-color palette.")
        definitions[name] = (str(palette[0]), str(palette[1]))
    return definitions


def _load_entity_metadata(
    definitions: EntityDefinitions,
    raw_metadata: object,
    rule_tags: list[str],
) -> dict[str, EntityMetadata]:
    """Normalize entity metadata and merge any metadata-defined tags into the tag list."""

    if not isinstance(raw_metadata, dict):
        raise ValueError("entity_metadata must be an object.")
    metadata: dict[str, EntityMetadata] = {}
    for name in definitions:
        if name not in raw_metadata:
            raise ValueError(f"Missing metadata for {name}.")
        metadata[name] = _normalize_catalog_metadata(name, raw_metadata[name])
        for tag in metadata[name]["rule_tags"]:
            if tag not in rule_tags:
                rule_tags.append(tag)
    return metadata


def load_catalog(path: Path = CATALOG_PATH) -> tuple[EntityDefinitions, dict[str, EntityMetadata], int, list[str]]:
    if not path.exists():
        return _default_catalog()
    # The load path stays intentionally linear: read the root object, normalize
    # top-level tags, load visible definitions, then load metadata that depends
    # on those definitions.
    try:
        data = _load_catalog_root(path)
        version = int(data["catalog_version"])
        raw_tags = data["rule_tags"]
        if not isinstance(raw_tags, list):
            raise ValueError("rule_tags must be an array.")
        rule_tags = normalize_rule_tags(raw_tags)
        definitions = _load_entity_definitions(data["entity_definitions"])
        if not definitions:
            return _default_catalog(version)
        metadata = _load_entity_metadata(definitions, data["entity_metadata"], rule_tags)
        if "none" not in rule_tags:
            rule_tags.insert(0, "none")
        return definitions, metadata, version, rule_tags
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return _default_catalog()


def save_catalog(
    definitions: EntityDefinitions,
    metadata: dict[str, EntityMetadata],
    rule_tags: list[str],
    path: Path = CATALOG_PATH,
    version: int | None = None,
) -> int:
    if version is not None:
        next_version = max(1, int(version))
    elif path.exists():
        try:
            next_version = int(_load_catalog_root(path)["catalog_version"]) + 1
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            next_version = 1
    else:
        next_version = 1
    normalized_tags = normalize_rule_tags(rule_tags)
    normalized_metadata = {name: _normalize_catalog_metadata(name, metadata[name]) for name in definitions}
    for meta in normalized_metadata.values():
        for tag in meta["rule_tags"]:
            if tag not in normalized_tags:
                normalized_tags.append(tag)
    data = {
        "catalog_version": next_version,
        "rule_tags": normalized_tags,
        "entity_definitions": {name: [palette[0], palette[1]] for name, palette in definitions.items()},
        "entity_metadata": normalized_metadata,
    }
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return next_version


def sanitize_entry(raw_name: str, raw_description: str, raw_rule_tag: str, raw_default_color: str) -> tuple[bool, str, dict[str, str]]:
    cleaned = _clean_entity_name(raw_name)
    if not cleaned:
        return False, "Enter an entity name.", {}
    if len(cleaned) > 24:
        return False, "Keep the name under 25 characters.", {}
    normalized_tag = _normalize_rule_tag(raw_rule_tag)
    return True, "", {
        "name": cleaned,
        "description": raw_description.strip(),
        "rule_tag": normalized_tag,
        "rule_tags": [normalized_tag],
        "default_color": normalize_hex_color(raw_default_color),
    }


def sanitize_entity_definition(
    raw_name: str,
    raw_description: str,
    raw_rule_tags: object,
    raw_default_color: str,
    raw_valid_states: object,
    raw_allowed_actions: object,
    raw_invariant_rules: object,
    raw_initial_invariant_state: object,
    raw_action_transitions: object,
) -> tuple[bool, str, dict[str, object]]:
    cleaned = _clean_entity_name(raw_name)
    if not cleaned:
        return False, "Enter an entity name.", {}
    if len(cleaned) > 24:
        return False, "Keep the name under 25 characters.", {}
    rule_tags = normalize_rule_tags(raw_rule_tags)
    try:
        genome = normalize_genome(
            {
                "valid_states": raw_valid_states,
                "allowed_actions": raw_allowed_actions,
                "invariant_rules": raw_invariant_rules,
                "initial_invariant_state": raw_initial_invariant_state,
                "action_transitions": raw_action_transitions,
            },
            {"rule_tags": rule_tags, "rule_tag": rule_tags[0]},
        )
    except (ValueError, json.JSONDecodeError) as exc:
        return False, str(exc), {}
    return True, "", {
        "name": cleaned,
        "description": raw_description.strip(),
        "rule_tag": rule_tags[0],
        "rule_tags": rule_tags,
        "default_color": normalize_hex_color(raw_default_color),
        "genome": genome,
    }
