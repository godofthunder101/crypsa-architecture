from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any

from .mint_catalog_store import GENOME_ACTIONS, MINT_ENTITY_DEFAULT_COLORS, build_default_genome, normalize_hex_color
from .mint_models import EntityMetadata, Genome, InvariantRule

# This module is the Mint-side translation boundary. It prepares read-only
# detail data and modal starter values so the editor and modal UI do not have
# to reconstruct those shapes directly from raw catalog dictionaries.
#
# Reading pattern:
# 1. start in mint_catalog_editor.py to see which action triggered the view
# 2. find the matching build_*_lens() function here
# 3. only then open mint_editor_ui.py if you need the widget layout details


@dataclass(frozen=True)
class MintDetailLens:
    """Pre-shaped read-only detail data for one selected Mint kind."""

    kind: str | None
    summary_text: str
    palette_fill: str
    palette_outline: str
    default_color: str
    detail_text: str


@dataclass(frozen=True)
class MintEntityModalLens:
    """Pre-shaped initial data for the Mint create/edit modal."""

    title: str
    original_kind: str | None
    name_value: str
    description_value: str
    quick_start_text: str | None
    rule_tags: list[str]
    default_color: str
    genome_json_fields: dict[str, str]


def _detail_rule_summary(rule: InvariantRule) -> str:
    summary = str(rule["rule_type"])
    actions = rule.get("actions", [])
    if actions:
        summary += f" | actions={', '.join(actions)}"
    if "required_parent_event_family" in rule:
        summary += f" | parent={rule['required_parent_event_family']}"
    if "required_context_event_family" in rule:
        summary += f" | context={rule['required_context_event_family']}"
    if "threshold_key" in rule:
        summary += f" | threshold={rule['threshold_key']}"
    return summary


def _detail_summary_text(meta: EntityMetadata, genome: Genome, rule_tags: list[str]) -> str:
    return (
        f"Tags: {', '.join(rule_tags)}\n"
        f"States: {', '.join(genome['valid_states'])}\n"
        f"Allowed Actions: {', '.join(genome['allowed_actions'])}"
    )


def _detail_text(meta: EntityMetadata, genome: Genome) -> str:
    lines = [
        f"Description: {str(meta.get('description', '')).strip() or 'None'}",
        "",
        "Action Transitions:",
    ]
    for action_name in GENOME_ACTIONS:
        transition = genome["action_transitions"][action_name]
        lines.append(
            f"- {action_name}: from [{', '.join(transition['from_states'])}]"
            + (f" -> {transition['to_state']}" if "to_state" in transition else "")
        )
    lines.append("")
    lines.append("Invariant Rules:")
    for rule in genome["invariant_rules"]:
        lines.append(f"- {_detail_rule_summary(rule)}")
    lines.append("")
    lines.append(f"Initial Invariant State: {json.dumps(genome['initial_invariant_state'])}")
    return "\n".join(lines)


def build_mint_detail_lens(app: Any, kind: str | None) -> MintDetailLens:
    """Translate selected editor state into detail-pane render data."""

    # Keep the right-hand detail pane as a pure render target: selection logic
    # lives in the editor, but summary/detail shaping lives here.
    if kind is None:
        return MintDetailLens(
            kind=None,
            summary_text="No Mint kinds available.",
            palette_fill="#101938",
            palette_outline="",
            default_color="#0f172a",
            detail_text="",
        )
    raw_meta = app.entity_metadata[kind]
    genome = app._meta_genome(raw_meta)
    fill, outline = app.entity_definitions[kind]
    rule_tags = list(app._meta_rule_tags(raw_meta))
    return MintDetailLens(
        kind=kind,
        summary_text=_detail_summary_text(raw_meta, genome, rule_tags),
        palette_fill=fill,
        palette_outline=outline,
        default_color=str(raw_meta.get("default_color", "")) or "#0f172a",
        detail_text=_detail_text(raw_meta, genome),
    )


def build_mint_entity_modal_lens(app: Any, title: str, original_kind: str | None = None) -> MintEntityModalLens:
    """Translate editor state into create/edit modal starter data."""

    # The create/edit modal starts from one stable handoff object so the modal
    # can focus on widgets and callbacks instead of catalog-shape lookups. The
    # genome JSON strings are prepared here too, so the modal does not have to
    # know how to serialize the store's normalized genome shape. That keeps the
    # modal focused on editing, while this adapter owns "what should the user
    # see first?" translation.
    meta = app.entity_metadata.get(original_kind or "", {})
    genome = app._meta_genome(meta) if meta else build_default_genome()
    return MintEntityModalLens(
        title=title,
        original_kind=original_kind,
        name_value=original_kind or "",
        description_value=str(meta.get("description", "")),
        quick_start_text=(
            "Quick start: enter a name, keep the default preset if you want a normal buildable kind, "
            "or use Beacon Example if you want the context-sensitive teaching pattern."
            if original_kind is None
            else None
        ),
        rule_tags=(list(app._meta_rule_tags(meta)) if meta else ["none"]),
        default_color=normalize_hex_color(str(meta.get("default_color", ""))) or MINT_ENTITY_DEFAULT_COLORS[0],
        genome_json_fields={
            "valid_states": json.dumps(genome["valid_states"], indent=2),
            "allowed_actions": json.dumps(genome["allowed_actions"], indent=2),
            "action_transitions": json.dumps(genome["action_transitions"], indent=2),
            "invariant_rules": json.dumps(genome["invariant_rules"], indent=2),
            "initial_invariant_state": json.dumps(genome["initial_invariant_state"], indent=2),
        },
    )
