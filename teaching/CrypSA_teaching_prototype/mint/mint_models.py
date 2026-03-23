from __future__ import annotations

from typing import TypeAlias, TypeGuard, TypedDict


# Typed shared Mint structures live here so the editor, store, and runtime
# can talk about the same catalog shapes without each layer inventing its own
# anonymous dict conventions. Read top-to-bottom: genome pieces first, then
# editor/runtime-facing metadata, then the frozen accepted-object definition.
#
# This file is intentionally selective about what it types. The goal is to
# name the Mint shapes that cross real boundaries, not to force every inner
# authoring detail into a heavier model than the teaching artifact needs.

Palette: TypeAlias = tuple[str, str]
EntityDefinitions: TypeAlias = dict[str, Palette]
InvariantState: TypeAlias = dict[str, object]


class ActionTransition(TypedDict, total=False):
    from_states: list[str]
    to_state: str


class InvariantRule(TypedDict, total=False):
    rule_type: str
    enabled: bool
    actions: list[str]
    applies_to_states: list[str]
    threshold_key: str
    message: str
    required_parent_event_family: str
    required_context_event_family: str
    required_owner: str
    threshold_min: int | float
    threshold_max: int | float


class Genome(TypedDict):
    valid_states: list[str]
    allowed_actions: list[str]
    action_transitions: dict[str, ActionTransition]
    invariant_rules: list[InvariantRule]
    initial_invariant_state: InvariantState


class EntityMetadata(TypedDict):
    description: str
    rule_tag: str
    rule_tags: list[str]
    default_color: str
    genome: Genome


class MintedDefinition(TypedDict):
    kind: str
    catalog_version: int
    palette: list[str]
    description: str
    rule_tag: str
    rule_tags: list[str]
    default_color: str
    genome: Genome


def is_minted_definition(value: object) -> TypeGuard[MintedDefinition]:
    """Return whether a value matches the frozen Mint-definition envelope."""

    if not isinstance(value, dict):
        return False
    palette = value.get("palette")
    rule_tags = value.get("rule_tags")
    return all(
        [
            isinstance(value.get("kind"), str),
            isinstance(value.get("catalog_version"), int),
            isinstance(palette, list),
            len(palette) == 2,
            all(isinstance(color, str) for color in palette),
            isinstance(value.get("description"), str),
            isinstance(value.get("rule_tag"), str),
            isinstance(rule_tags, list),
            all(isinstance(tag, str) for tag in rule_tags),
            isinstance(value.get("default_color"), str),
            isinstance(value.get("genome"), dict),
        ]
    )


def is_invariant_state(value: object) -> TypeGuard[InvariantState]:
    """Return whether a value matches the teaching prototype's invariant-state map."""

    return isinstance(value, dict) and all(isinstance(key, str) for key in value.keys())


def copy_invariant_state(value: InvariantState) -> InvariantState:
    """Copy one invariant-state map for runtime handoff."""

    return dict(value)


def copy_minted_definition(value: MintedDefinition) -> MintedDefinition:
    """Copy the frozen Mint-definition envelope for runtime handoff."""

    return MintedDefinition(
        kind=value["kind"],
        catalog_version=value["catalog_version"],
        palette=list(value["palette"]),
        description=value["description"],
        rule_tag=value["rule_tag"],
        rule_tags=list(value["rule_tags"]),
        default_color=value["default_color"],
        genome=value["genome"],
    )


def build_minted_definition(
    *,
    kind: str,
    catalog_version: int,
    palette: Palette,
    metadata: EntityMetadata,
    genome: Genome | None = None,
) -> MintedDefinition:
    """Build the frozen Mint definition attached to accepted canonical objects."""

    resolved_genome = genome if genome is not None else metadata["genome"]
    return MintedDefinition(
        kind=kind,
        catalog_version=catalog_version,
        palette=[palette[0], palette[1]],
        description=metadata["description"],
        rule_tag=metadata["rule_tag"],
        rule_tags=list(metadata["rule_tags"]),
        default_color=metadata["default_color"],
        genome=resolved_genome,
    )
