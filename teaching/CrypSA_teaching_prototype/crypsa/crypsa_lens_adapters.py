from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .crypsa_action_requests import (
    CenterObserverNearCanonicalRequest,
    ClearCandidatesRequest,
    MintFromServerRequest,
    OpenMintEditorRequest,
    QueueBuildCandidateRequest,
    ReloadCatalogRequest,
    SelectHistoryEventRequest,
    SelectTimelineEventRequest,
    TryBeaconPathRequest,
)
from .crypsa_teaching_theme import ACCENT, GOOD, MUTED, TEXT, WARN
from .runtime_models import CanonicalEvent, ReplayBranchState, ReplayObjectRecord

# This module is the translation boundary between runtime/catalog state and the
# different UI lenses. Each builder shapes one narrow view model so the UI can
# render prepared data instead of reaching deeply back into the app object.
#
# Reading pattern:
# 1. find the UI surface you care about
# 2. find the matching build_*_lens() function here
# 3. follow only the helper stages used by that builder
#
# A useful rule in this file:
# - display-only shaping should happen here
# - if the lens needs to trigger a mutation, attach a small typed request
# - the UI should not have to rediscover selection policy or controller rules


@dataclass(frozen=True)
class GridLens:
    """Grid data shaped for one rendered lens."""

    objects: dict[str, ReplayObjectRecord]
    grid_size: int
    reserved_tiles: set[tuple[int, int]]
    observer_position: tuple[int, int] | None
    target_tile: tuple[int, int] | None


@dataclass(frozen=True)
class BannerLens:
    """Compact banner state for a pane header."""

    text: str
    fill: str
    outline: str
    text_color: str


@dataclass(frozen=True)
class CanonicalPaneLens:
    """All canonical-pane data translated for rendering."""

    summary_rows: list[tuple[str, str]]
    grid: GridLens
    banner: BannerLens | None


@dataclass(frozen=True)
class ObserverPaneLens:
    """All observer-pane data translated for rendering."""

    summary_rows: list[tuple[str, str]]
    summary_value_colors: dict[str, str]
    grid: GridLens
    divergence_banner: BannerLens | None
    context_hint: str | None
    auto_reconcile_enabled: bool
    auto_reconcile_help_text: str
    beacon_prompt: str


@dataclass(frozen=True)
class HistoryCardLens:
    """Pre-shaped data for one history card."""

    event_id: str
    header_fill: str
    header_text: str
    is_on_active_lineage: bool
    lines: list[str]
    select_request: SelectHistoryEventRequest


@dataclass(frozen=True)
class TimelineNodeLens:
    """Pre-shaped data for one timeline node."""

    event_id: str
    sequence_text: str
    event_type_text: str
    fill: str
    outline: str
    outline_width: int
    select_request: SelectTimelineEventRequest


@dataclass(frozen=True)
class TimelineRowLens:
    """Pre-shaped data for one displayed timeline row."""

    branch_name: str
    branch_label: str
    is_selected_branch: bool
    row_color: str
    line_color: str
    parent_label: str | None
    head_event_id: str | None
    connector_origin: tuple[str, str] | None
    connector_target_event_id: str | None
    nodes: list[TimelineNodeLens]


@dataclass(frozen=True)
class TimelineModalLens:
    """All pre-shaped timeline data needed by the modal."""

    rows: list[TimelineRowLens]
    selected_event_id: str | None
    inspector_lines: list[str]
    active_lineage_label: str
    recenter_request: CenterObserverNearCanonicalRequest


@dataclass(frozen=True)
class MintActionOptionLens:
    """Pre-shaped server-mint option row."""

    kind: str
    requires_causal_context: bool
    request: MintFromServerRequest


@dataclass(frozen=True)
class MintActionModalLens:
    """All translated data for the server Mint modal."""

    reload_request: ReloadCatalogRequest
    open_editor_request: OpenMintEditorRequest
    options: list[MintActionOptionLens]


@dataclass(frozen=True)
class BuildActionCardLens:
    """Pre-shaped observer build card data."""

    kind: str
    is_selected: bool
    rule_tags_text: str
    actions_summary_text: str
    context_hint: str | None
    beacon_hint: str | None
    request: QueueBuildCandidateRequest


@dataclass(frozen=True)
class BuildActionModalLens:
    """All translated data for the observer build modal."""

    target_tile: tuple[int, int]
    teaching_example_loaded: bool
    reload_request: ReloadCatalogRequest
    try_beacon_request: TryBeaconPathRequest
    cards: list[BuildActionCardLens]


@dataclass(frozen=True)
class CandidateQueueLens:
    """Pre-shaped queue data for the candidates modal."""

    lines: list[str]
    clear_request: ClearCandidatesRequest


def _canonical_banner(app: Any) -> BannerLens | None:
    if app.teaching_example_loaded:
        return BannerLens(
            text="PLAYGROUND READY  |  Teaching Example Loaded",
            fill="#3b2b11",
            outline="#b38b2e",
            text_color="#fde68a",
        )
    if not app.events:
        return BannerLens(
            text="START HERE  |  Open How To Read, then load the teaching example",
            fill="#10233c",
            outline="#315f93",
            text_color="#93c5fd",
        )
    if not app.invariant_boundary_candidates:
        return BannerLens(
            text="IN SYNC  |  Local view and world state match",
            fill="#102b21",
            outline="#2d7d53",
            text_color="#86efac",
        )
    return None


def _observer_beacon_prompt(app: Any) -> str:
    if app.teaching_example_loaded:
        return "Suggested next move: click Try Beacon, reconcile it, then compare the result in History or Timeline."
    return "Suggested next move: load the teaching example, then click Try Beacon to see context-sensitive validation."


def _observer_context_hint(
    app: Any,
    selected_genome: dict[str, object] | None,
    visible_state: ReplayBranchState,
) -> str | None:
    # This hint stays in the adapter because it is teaching-facing translation
    # of runtime/catalog state, not a runtime rule by itself.
    if not isinstance(selected_genome, dict):
        return None
    context_rules = [rule for rule in selected_genome["invariant_rules"] if str(rule.get("rule_type", "")) == "require_context_event_family"]
    if not context_rules:
        return None
    context_family = str(context_rules[0].get("required_context_event_family", "")).lower() or "required"
    available_families = {record.event_family.lower() for record in app._event_chain(app._selected_head_event_id())}
    hint = f"Context rule: requires causal context with event family '{context_family}'."
    if context_family not in available_families:
        hint += " Current viewed lineage does not expose it yet."
    elif not app._tile_occupied(*app._tile_in_front(), visible_state):
        hint += f" Context is available, so {app.observer_build_selection} can pass this rule."
    return hint


def _matching_branches_for_event(app: Any, event_id: str) -> list[str]:
    matching_branches: list[str] = []
    for branch in app._branch_rows():
        event_ids = {branch_record.event_id for branch_record in app._timeline_events_for_branch(branch)}
        if event_id in event_ids:
            matching_branches.append(branch.name)
    return matching_branches


def _preferred_branch_for_event(app: Any, event_id: str, matching_branches: list[str]) -> str | None:
    preferred_branch = None
    hinted_branch = ""
    if event_id in app.events:
        hinted_branch = app.events[event_id].branch_hint
    if app.selected_branch in matching_branches:
        preferred_branch = app.selected_branch
    elif hinted_branch in matching_branches:
        preferred_branch = hinted_branch
    elif matching_branches:
        preferred_branch = matching_branches[0]
    return preferred_branch


def _timeline_event_fill(record: CanonicalEvent) -> str:
    event_type = record.event_type
    if event_type == "mint_object":
        return "#15803d"
    if event_type == "destroy_object":
        return "#b91c1c"
    if record.event_family == "structural":
        return "#1d4ed8"
    return "#475569"


def _connector_target_event_id(nodes: list[TimelineNodeLens], fork_event_id: str | None) -> str | None:
    """Choose the first visually divergent node for a branch connector."""

    for node in nodes:
        if node.event_id != fork_event_id:
            return node.event_id
    return nodes[0].event_id if nodes else None


def build_history_card_lenses(app: Any) -> list[HistoryCardLens]:
    """Translate runtime history into card-oriented view data."""

    # History cards are pre-expanded here so the modal can render lines and a
    # select request without needing branch-matching logic of its own. The
    # request also carries the preferred branch choice so the UI and runtime
    # do not each have to recompute that policy separately.
    lenses: list[HistoryCardLens] = []
    for record in reversed(app._all_events_sorted()):
        event_id = record.event_id
        event_type = record.event_type
        header_fill = {"mint_object": "#14532d", "build_object": "#1d4ed8", "destroy_object": "#7f1d1d"}.get(event_type, "#334155")
        matching_branches = _matching_branches_for_event(app, event_id)
        preferred_branch = _preferred_branch_for_event(app, event_id, matching_branches)
        lines = [
            f"target={record.target_identity}",
            f"observer={record.observer_identity}",
            f"lineage_parent={record.lineage_parent or 'root'}",
            f"causal_references={', '.join(record.causal_references) or 'none'}",
            f"lineage_view={app._branch_label(record.branch_hint)}",
            f"preferred_lineage={app._branch_label(preferred_branch) if preferred_branch is not None else 'none'}",
            f"catalog=v{record.catalog_version}",
        ]
        if len(matching_branches) > 1:
            lines.append("shared_ancestor=yes")
            lines.append("lineages=" + ", ".join(app._branch_label(branch_name) for branch_name in matching_branches))
            lines.append("note=this canonical event is shared by multiple event lineages; reconciliation uses the preferred lineage shown above")
        for key, value in dict(record.payload).items():
            if isinstance(value, (str, int, float)):
                lines.append(f"{key}={value}")
        lenses.append(
            HistoryCardLens(
                event_id=event_id,
                header_fill=header_fill,
                header_text=f"seq {record.sequence} | {event_type} | {event_id}",
                is_on_active_lineage=app.selected_branch in matching_branches,
                lines=lines,
                select_request=SelectHistoryEventRequest(event_id=event_id, preferred_branch_name=preferred_branch),
            )
        )
    return lenses


def build_timeline_modal_lens(app: Any) -> TimelineModalLens:
    """Translate runtime graph state into timeline-row view data."""

    # The timeline modal is the densest inspection lens, so its builder does
    # the structural work up front: row choice, node styling, inspector text,
    # and the requests needed when the user clicks a node or recenter action.
    rows: list[TimelineRowLens] = []
    for branch in app._branch_rows():
        is_selected_branch = branch.name == app.selected_branch
        nodes: list[TimelineNodeLens] = []
        for record in app._timeline_events_for_branch(branch):
            event_id = record.event_id
            is_selected = event_id == app._selected_head_event_id()
            is_branch_head = event_id == branch.head_event_id
            nodes.append(
                TimelineNodeLens(
                    event_id=event_id,
                    sequence_text=str(record.sequence),
                    event_type_text=record.event_type.replace("_object", "").replace("_", "\n"),
                    fill=_timeline_event_fill(record),
                    outline="#f8fafc" if is_selected else ("#67e8f9" if is_branch_head or is_selected_branch else "#dbeafe"),
                    outline_width=3 if is_selected or is_branch_head else 2,
                    select_request=SelectTimelineEventRequest(branch_name=branch.name, event_id=event_id),
                )
            )
        rows.append(
            TimelineRowLens(
                branch_name=branch.name,
                branch_label=app._branch_label(branch.name) + ("  <- active lineage" if is_selected_branch else ""),
                is_selected_branch=is_selected_branch,
                row_color=ACCENT if is_selected_branch else TEXT,
                line_color="#67e8f9" if is_selected_branch else "#1f3357",
                parent_label=(app._branch_label(branch.parent_branch) if branch.parent_branch is not None else None),
                head_event_id=branch.head_event_id,
                connector_origin=app._timeline_connector_origin(branch),
                connector_target_event_id=_connector_target_event_id(nodes, branch.fork_from_event_id),
                nodes=nodes,
            )
        )

    inspector_lines: list[str]
    event_id = app._selected_head_event_id()
    if not isinstance(event_id, str) or event_id not in app.events:
        inspector_lines = ["Select an event node to inspect it."]
    else:
        record = app.events[event_id]
        payload = dict(record.payload)
        inspector_lines = [
            f"event_id: {record.event_id}",
            f"sequence: {record.sequence}",
            f"type: {record.event_type}",
            f"family: {record.event_family}",
            f"target: {record.target_identity}",
            f"observer: {record.observer_identity}",
            f"lineage_parent: {record.lineage_parent or 'root'}",
            f"causal_references: {', '.join(record.causal_references) or 'none'}",
            "",
            "note: replay follows lineage_parent. causal_references do not drive replay, but they can influence invariant validation.",
            f"catalog: v{record.catalog_version}",
            "",
            "payload:",
        ]
        for key, value in payload.items():
            if isinstance(value, (dict, list)):
                inspector_lines.append(f"{key}: {value}")
            else:
                inspector_lines.append(f"{key}: {value}")
    return TimelineModalLens(
        rows=rows,
        selected_event_id=event_id,
        inspector_lines=inspector_lines,
        active_lineage_label=app._branch_label(app.selected_branch),
        recenter_request=CenterObserverNearCanonicalRequest(),
    )


def build_canonical_pane_lens(app: Any) -> CanonicalPaneLens:
    """Translate runtime state into canonical-pane render data."""

    # Pane lenses keep the main render module focused on layout rather than
    # replay queries or summary assembly.
    state = app._visible_canonical_state()
    branch = app._current_branch_record()
    lineage_families = sorted({record.event_family.lower() for record in app._event_chain(app._selected_head_event_id())})
    summary_rows = [
        ("Branch / Lineage", app._branch_label(app.selected_branch)),
        ("Selected Event", app._selected_head_event_id() or "root"),
        ("Branch Head", branch.head_event_id or "root"),
        ("Canonical Events", str(len(app.events))),
        ("Objects", str(len(state.objects))),
        ("Catalog", f"v{app.catalog_version}"),
        ("Event Families", ", ".join(lineage_families) if lineage_families else "none"),
    ]
    return CanonicalPaneLens(
        summary_rows=summary_rows,
        grid=GridLens(
            objects=dict(state.objects),
            grid_size=app.grid_size,
            reserved_tiles=set(app.server_reserved_tiles),
            observer_position=None,
            target_tile=None,
        ),
        banner=_canonical_banner(app),
    )


def build_observer_pane_lens(app: Any) -> ObserverPaneLens:
    """Translate runtime state into observer-pane render data."""

    # The observer pane intentionally receives precomputed prompts and summary
    # strings so UI wording can evolve without pulling more runtime logic into
    # the render layer.
    status = "Ready To Reconcile" if app.invariant_boundary_candidates else "Local Exploration"
    selected_meta = app.entity_metadata.get(app.observer_build_selection)
    selected_genome = app._metadata_genome(selected_meta) if isinstance(selected_meta, dict) else None
    visible_state = app._visible_canonical_state()
    divergence_banner = None
    if app.invariant_boundary_candidates:
        divergence_banner = BannerLens(
            text="LOCAL CHANGES WAITING  |  Reconcile To Compare",
            fill="#35161e",
            outline="#9e3348",
            text_color="#fca5a5",
        )
    return ObserverPaneLens(
        summary_rows=[
            ("Local Position", f"({app.observer_local_x}, {app.observer_local_y})"),
            ("Facing", app.observer_facing),
            ("Target Tile", f"{app._tile_in_front()}"),
            ("Build Kind", app.observer_build_selection),
            ("Pending Submissions", str(len(app.invariant_boundary_candidates))),
            ("Status", status),
        ],
        summary_value_colors={"Status": WARN if app.invariant_boundary_candidates else GOOD},
        grid=GridLens(
            objects=dict(visible_state.objects),
            grid_size=app.grid_size,
            reserved_tiles=set(app.server_reserved_tiles),
            observer_position=(app.observer_local_x, app.observer_local_y),
            target_tile=app._tile_in_front(),
        ),
        divergence_banner=divergence_banner,
        context_hint=_observer_context_hint(app, selected_genome, visible_state),
        auto_reconcile_enabled=bool(app.observer_auto_reconcile),
        auto_reconcile_help_text="On sends build/destroy straight to review. Off keeps them queued so you can compare before reconciling.",
        beacon_prompt=_observer_beacon_prompt(app),
    )


def build_mint_action_modal_lens(app: Any) -> MintActionModalLens:
    """Translate catalog/runtime state into server-mint option rows."""

    # Action-oriented lenses carry both display data and the typed requests the
    # UI should hand back when a button is pressed.
    options: list[MintActionOptionLens] = []
    for kind in sorted(app.entity_definitions):
        meta = app.entity_metadata[kind]
        genome = app._metadata_genome(meta)
        options.append(
            MintActionOptionLens(
                kind=kind,
                requires_causal_context=any(str(rule.get("rule_type", "")) == "require_context_event_family" for rule in genome["invariant_rules"]),
                request=MintFromServerRequest(kind=kind),
            )
        )
    return MintActionModalLens(
        reload_request=ReloadCatalogRequest(),
        open_editor_request=OpenMintEditorRequest(),
        options=options,
    )


def build_build_action_modal_lens(app: Any) -> BuildActionModalLens:
    """Translate catalog/runtime state into observer build-card data."""

    # Build cards are shaped here so the modal can stay a pure chooser: each
    # card already knows its summary strings, hints, and submit request.
    cards: list[BuildActionCardLens] = []
    for kind in sorted(app.entity_definitions):
        meta = app.entity_metadata[kind]
        genome = app._metadata_genome(meta)
        context_hint = None
        beacon_hint = None
        context_rules = [rule for rule in genome["invariant_rules"] if str(rule.get("rule_type", "")) == "require_context_event_family"]
        if context_rules:
            context_family = str(context_rules[0].get("required_context_event_family", "")).lower() or "required"
            context_hint = f"Context rule: requires causal context with event family '{context_family}'."
            if kind == "Beacon":
                beacon_hint = "Beacon is the built-in context-sensitive teaching example. Load Teaching Example first if this rule seems unclear."
        cards.append(
            BuildActionCardLens(
                kind=kind,
                is_selected=(kind == app.observer_build_selection),
                rule_tags_text=f"tags={', '.join(app._metadata_rule_tags(meta))}",
                actions_summary_text=f"actions={', '.join(genome['allowed_actions'])} | rules={len(genome['invariant_rules'])}",
                context_hint=context_hint,
                beacon_hint=beacon_hint,
                request=QueueBuildCandidateRequest(kind=kind),
            )
        )
    return BuildActionModalLens(
        target_tile=app._tile_in_front(),
        teaching_example_loaded=bool(app.teaching_example_loaded),
        reload_request=ReloadCatalogRequest(),
        try_beacon_request=TryBeaconPathRequest(),
        cards=cards,
    )


def build_candidate_queue_lens(app: Any) -> CandidateQueueLens:
    """Translate queued invariant-boundary candidates into display lines."""

    lines: list[str] = []
    for index, action in enumerate(app.invariant_boundary_candidates, start=1):
        if action.action == "build_object":
            lines.append(f"{index:02d}. build {action.kind} @ ({action.x}, {action.y})")
        else:
            lines.append(f"{index:02d}. destroy @ ({action.x}, {action.y})")
    if not lines:
        lines.append("No invariant-boundary candidates queued.")
    return CandidateQueueLens(lines=lines, clear_request=ClearCandidatesRequest())
