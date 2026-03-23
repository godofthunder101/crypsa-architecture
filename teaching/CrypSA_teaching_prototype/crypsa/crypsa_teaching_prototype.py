from __future__ import annotations

from datetime import datetime, timezone
import tkinter as tk
from typing import Callable

# This file orchestrates a completed teaching implementation of CrypSA.
# It is intentionally still the coordination center, but it is not a
# production runtime and should not be treated like the future runtime path.
#
# Import groups reflect the current controller boundary:
# - requests describe UI intent
# - runtime/canonical modules own specific behavior slices
# - UI modules render or open dialogs
# - this file still orchestrates those pieces and owns the overall app flow
from .crypsa_action_requests import ActionRequest
from .canonical_replay import (
    find_object_at_tile,
    first_open_canonical_tile,
    tile_occupied,
    visible_canonical_state,
)
from .canonical_apply import create_canonical_event, mint_object_id
from .controller_ui_actions import (
    center_observer_near_canonical_state,
    clear_candidates,
    open_mint_editor,
    reload_catalog,
    try_beacon_path,
)
from .crypsa_event_graph import (
    BranchRecord,
    all_event_ids_sorted,
    all_events_sorted,
    baseline_state,
    branch_label,
    branch_record_by_name,
    build_branch_rows,
    event_chain,
)
from .crypsa_lens_adapters import (
    BuildActionModalLens,
    CandidateQueueLens,
    CanonicalPaneLens,
    GridLens,
    HistoryCardLens,
    MintActionModalLens,
    ObserverPaneLens,
    TimelineModalLens,
    build_build_action_modal_lens,
    build_canonical_pane_lens,
    build_candidate_queue_lens,
    build_history_card_lenses,
    build_mint_action_modal_lens,
    build_observer_pane_lens,
    build_timeline_modal_lens,
)
from .ui.crypsa_action_ui import open_build_modal, open_candidate_modal, open_mint_modal
from .app_shell import (
    bind_main_window_hotkeys,
    clear_widgets,
    create_root_window,
    handle_escape,
    main_window_hotkeys_enabled,
    open_modal,
    run_main_window_hotkey,
)
from .crypsa_teaching_theme import BG, HEIGHT, STATE_PATH, TEACHING_EXAMPLE_PATH, WIDTH
from .teaching_example_loader import load_teaching_example_plan
from .ui.crypsa_history_ui import open_history_modal, open_timeline_modal, select_history_event
from .ui.crypsa_render_ui import add_widget, draw_grid, draw_observer_pane, draw_scene, draw_pane_shell, draw_server_pane, make_button
from .runtime_persistence import load_runtime_store, save_runtime_store
from .runtime_store import RuntimeStore
from .runtime_models import CandidateEvent, CanonicalEvent, PlacedObjectPayload, ReplayBranchState, ReplayObjectRecord
from .runtime_actions import (
    queue_build_candidate,
    queue_destroy_candidate,
    tile_in_front,
)
from .reconciliation import (
    accept_build_candidate,
    accept_destroy_candidate,
    mint_from_server,
    reconcile_invariant_boundary_candidates,
)
from .request_dispatch import dispatch_action_request
from .validation import evaluate_invariant_rules
from .ui.crypsa_teaching_ui import open_hotkeys_modal, open_model_notes_modal, open_pane_help_modal, open_teaching_modal, open_walkthrough_modal
from mint.mint_models import EntityMetadata, Genome, InvariantState, MintedDefinition, build_minted_definition
from mint.mint_catalog_store import load_catalog, normalize_genome, normalize_rule_tags


class CrypSATeachingPrototype:
    """Minimal teaching prototype for observer-local state vs canonical history."""

    def __init__(self) -> None:
        # Keep startup centralized here: this class still owns runtime meaning,
        # while rendering and modal detail live in the UI and adapter modules.
        # The main controller is still intentionally visible because this is a
        # teaching prototype, but several high-pressure areas now live in
        # extracted modules: runtime_store, runtime_actions, validation,
        # reconciliation, canonical_apply, canonical_replay, app_shell,
        # request_dispatch, runtime_persistence, and
        # teaching_example_loader.
        self.entity_definitions, self.entity_metadata, self.catalog_version, self.rule_tags = load_catalog()
        self.server_reserved_tiles: set[tuple[int, int]] = {(2, 2), (2, 3), (7, 6), (7, 7)}
        self.grid_size = 10
        # Runtime state now has an explicit store object. The controller still
        # exposes thin compatibility properties so the rest of the teaching
        # prototype can move over in smaller refactor steps.
        self.store = RuntimeStore()
        self.store.reset_to_baseline(next(iter(self.entity_definitions)))
        self._load_state()

        # Tk shell and global bindings.
        self.root = create_root_window(
            title="CrypSA Teaching Prototype",
            width=WIDTH,
            height=HEIGHT,
            min_width=900,
            min_height=620,
            background=BG,
        )

        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.widgets: list[tk.Widget] = []

        bind_main_window_hotkeys(self)

        self._draw_scene(WIDTH, HEIGHT)

    # ------------------------------------------------------------------
    # State Persistence
    # ------------------------------------------------------------------

    @property
    def observer_identity(self) -> str:
        return self.store.observer.observer_identity

    @observer_identity.setter
    def observer_identity(self, value: str) -> None:
        self.store.observer.observer_identity = value

    @property
    def observer_local_x(self) -> int:
        return self.store.observer.local_x

    @observer_local_x.setter
    def observer_local_x(self, value: int) -> None:
        self.store.observer.local_x = value

    @property
    def observer_local_y(self) -> int:
        return self.store.observer.local_y

    @observer_local_y.setter
    def observer_local_y(self, value: int) -> None:
        self.store.observer.local_y = value

    @property
    def observer_facing(self) -> str:
        return self.store.observer.facing

    @observer_facing.setter
    def observer_facing(self, value: str) -> None:
        self.store.observer.facing = value

    @property
    def observer_build_selection(self) -> str:
        return self.store.observer.build_selection

    @observer_build_selection.setter
    def observer_build_selection(self, value: str) -> None:
        self.store.observer.build_selection = value

    @property
    def observer_auto_reconcile(self) -> bool:
        return self.store.observer.auto_reconcile

    @observer_auto_reconcile.setter
    def observer_auto_reconcile(self, value: bool) -> None:
        self.store.observer.auto_reconcile = value

    @property
    def invariant_boundary_candidates(self) -> list[CandidateEvent]:
        return self.store.observer.invariant_boundary_candidates

    @invariant_boundary_candidates.setter
    def invariant_boundary_candidates(self, value: list[CandidateEvent]) -> None:
        self.store.observer.invariant_boundary_candidates = value

    @property
    def next_object_id(self) -> int:
        return self.store.canonical.next_object_id

    @next_object_id.setter
    def next_object_id(self, value: int) -> None:
        self.store.canonical.next_object_id = value

    @property
    def next_sequence(self) -> int:
        return self.store.canonical.next_sequence

    @next_sequence.setter
    def next_sequence(self, value: int) -> None:
        self.store.canonical.next_sequence = value

    @property
    def events(self) -> dict[str, CanonicalEvent]:
        return self.store.canonical.events

    @events.setter
    def events(self, value: dict[str, CanonicalEvent]) -> None:
        self.store.canonical.events = value

    @property
    def selected_branch(self) -> str:
        return self.store.canonical.selected_branch

    @selected_branch.setter
    def selected_branch(self, value: str) -> None:
        self.store.canonical.selected_branch = value

    @property
    def selected_canonical_event_id(self) -> str | None:
        return self.store.canonical.selected_canonical_event_id

    @selected_canonical_event_id.setter
    def selected_canonical_event_id(self, value: str | None) -> None:
        self.store.canonical.selected_canonical_event_id = value

    @property
    def teaching_example_loaded(self) -> bool:
        return self.store.canonical.teaching_example_loaded

    @teaching_example_loaded.setter
    def teaching_example_loaded(self, value: bool) -> None:
        self.store.canonical.teaching_example_loaded = value

    @property
    def server_log(self) -> list[str]:
        return self.store.inspection.server_log

    @server_log.setter
    def server_log(self, value: list[str]) -> None:
        self.store.inspection.server_log = value

    @property
    def observer_log(self) -> list[str]:
        return self.store.inspection.observer_log

    @observer_log.setter
    def observer_log(self, value: list[str]) -> None:
        self.store.inspection.observer_log = value

    @property
    def server_serial(self) -> int:
        return self.store.inspection.server_serial

    @server_serial.setter
    def server_serial(self, value: int) -> None:
        self.store.inspection.server_serial = value

    @property
    def observer_serial(self) -> int:
        return self.store.inspection.observer_serial

    @observer_serial.setter
    def observer_serial(self, value: int) -> None:
        self.store.inspection.observer_serial = value

    def _baseline_state(self) -> dict[str, object]:
        return baseline_state()

    def _load_state(self) -> None:
        """Load current-schema runtime state if a saved file exists."""

        loaded_store = load_runtime_store(STATE_PATH)
        if loaded_store is None:
            return
        # Keep controller-side post-load checks here: the persistence module
        # should understand saved schema, while the controller still decides
        # whether loaded selections make sense for the current catalog/runtime.
        self.store = loaded_store
        if self._branch_record_by_name(self.selected_branch) is None:
            self.selected_branch = "main"
        if self.observer_build_selection not in self.entity_definitions:
            self.observer_build_selection = next(iter(self.entity_definitions))

    def _save_state(self) -> None:
        """Persist only the state this prototype actively uses."""

        save_runtime_store(STATE_PATH, self.store, catalog_version=self.catalog_version)

    def _close(self) -> None:
        self._save_state()
        self.root.destroy()

    def _reset_runtime_state(self) -> None:
        """Return the prototype to an empty baseline without UI side effects."""

        self.store.reset_to_baseline(next(iter(self.entity_definitions)))

    def _wipe_to_fresh_start(self) -> None:
        self._reset_runtime_state()
        self._push_server_log("fresh install reset -> canonical event graph cleared")
        self._push_observer_log("fresh install reset -> observer returned to baseline state")
        self._save_state()
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())

    # ------------------------------------------------------------------
    # Event Graph Views
    # ------------------------------------------------------------------

    def _all_event_ids_sorted(self) -> list[str]:
        return all_event_ids_sorted(self.events)

    def _all_events_sorted(self) -> list[CanonicalEvent]:
        return all_events_sorted(self.events)

    def _event_timestamp(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _current_branch_record(self) -> BranchRecord:
        branch = self._branch_record_by_name(self.selected_branch)
        return branch if branch is not None else BranchRecord("main", None, None, None)

    def _selected_head_event_id(self) -> str | None:
        if self.selected_canonical_event_id in self.events:
            return self.selected_canonical_event_id
        return self._current_branch_record().head_event_id

    def _event_chain(self, head_event_id: str | None) -> list[CanonicalEvent]:
        return event_chain(self.events, head_event_id)

    def _build_branch_rows(self) -> list[BranchRecord]:
        return build_branch_rows(self.events)

    def _branch_record_by_name(self, branch_name: str) -> BranchRecord | None:
        return branch_record_by_name(self.events, branch_name)

    def _branch_label(self, branch_name: str | None) -> str:
        return branch_label(self.events, branch_name)

    def _replay_branch_state(self, head_event_id: str | None) -> ReplayBranchState:
        return visible_canonical_state(self.events, head_event_id)

    def _visible_canonical_state(self) -> ReplayBranchState:
        # This is the main runtime-to-replay bridge used by the UI. The left
        # pane never owns truth directly; it always asks replay for the visible
        # state at the currently selected history point.
        return self._replay_branch_state(self._selected_head_event_id())

    # ------------------------------------------------------------------
    # Log Streams
    # ------------------------------------------------------------------

    def _push_server_log(self, message: str) -> None:
        self.server_serial += 1
        self.server_log.insert(0, f"[S{self.server_serial:03d}] {message}")
        self.server_log = self.server_log[:60]

    def _push_observer_log(self, message: str) -> None:
        self.observer_serial += 1
        self.observer_log.insert(0, f"[O{self.observer_serial:03d}] {message}")
        self.observer_log = self.observer_log[:60]

    def _metadata_rule_tags(self, meta: EntityMetadata) -> list[str]:
        return normalize_rule_tags(meta["rule_tags"])

    def _metadata_genome(self, meta: EntityMetadata) -> Genome:
        return normalize_genome(meta["genome"], meta)

    def _catalog_minted_definition(self, kind: str) -> MintedDefinition:
        palette = self.entity_definitions[kind]
        meta = self.entity_metadata[kind]
        return build_minted_definition(
            kind=kind,
            catalog_version=self.catalog_version,
            palette=palette,
            metadata=meta,
            genome=self._metadata_genome(meta),
        )

    def _initial_state_for_definition(self, minted_definition: MintedDefinition) -> InvariantState:
        return dict(normalize_genome(minted_definition.get("genome"), minted_definition)["initial_invariant_state"])

    def _tile_occupied(self, x: int, y: int, canonical_state: ReplayBranchState) -> bool:
        return tile_occupied(x, y, canonical_state)

    # ------------------------------------------------------------------
    # Genome Validation And Canonical Acceptance
    # ------------------------------------------------------------------

    def _evaluate_invariant_rules(
        self,
        minted_definition: MintedDefinition,
        action: str,
        tile: tuple[int, int] | None,
        canonical_state: dict[str, object],
        current_state: InvariantState | None = None,
        parent_event_id: str | None = None,
        causal_reference_ids: list[str] | None = None,
    ) -> tuple[bool, str]:
        """Apply genome-level invariant checks before accepting a canonical event."""

        return evaluate_invariant_rules(
            minted_definition,
            action,
            tile,
            canonical_state,
            current_state,
            parent_event_id,
            causal_reference_ids,
            events=self.events,
            observer_identity=self.observer_identity,
            server_reserved_tiles=self.server_reserved_tiles,
            initial_state_for_definition=self._initial_state_for_definition,
            tile_occupied=self._tile_occupied,
        )

    def _transition_invariant_state(
        self,
        minted_definition: MintedDefinition,
        action: str,
        current_state: InvariantState | None = None,
    ) -> tuple[bool, str, InvariantState]:
        """Apply the genome transition for one accepted invariant action."""

        genome = normalize_genome(minted_definition.get("genome"), minted_definition)
        allowed_actions = {str(item).lower() for item in genome["allowed_actions"]}
        if action not in allowed_actions:
            return False, f"genome denies {action}", {}
        state = dict(current_state) if isinstance(current_state, dict) else self._initial_state_for_definition(minted_definition)
        valid_states = [str(item) for item in genome["valid_states"]]
        current_label = str(state.get("state", "idle"))
        if current_label not in valid_states:
            return False, f"invalid invariant state {current_label}", {}
        transition = dict(genome["action_transitions"].get(action, {}))
        allowed_from = transition.get("from_states", valid_states)
        if isinstance(allowed_from, list) and allowed_from and current_label not in {str(item) for item in allowed_from}:
            return False, f"{action} is not allowed from {current_label}", {}
        next_state = dict(state)
        target_state = transition.get("to_state")
        if isinstance(target_state, str) and target_state:
            next_state["state"] = target_state
        if str(next_state.get("state", "")) not in valid_states:
            return False, "transition produced an invalid invariant state", {}
        return True, "", next_state

    def _branch_name_for_fork(self, fork_event_id: str | None) -> str:
        if isinstance(fork_event_id, str) and fork_event_id in self.events:
            return f"branch:{fork_event_id}:pending"
        return "main"

    def _ensure_writable_branch(self) -> tuple[str, str | None]:
        active = self._current_branch_record()
        base_event_id = self._selected_head_event_id()
        if base_event_id == active.head_event_id:
            return active.name, active.head_event_id
        branch_name = self._branch_name_for_fork(base_event_id)
        self.selected_branch = branch_name
        self.selected_canonical_event_id = base_event_id
        self._push_server_log(f"event-lineage fork accepted -> {self._branch_label(branch_name)}")
        return branch_name, base_event_id

    def _mint_object_id(self, kind: str) -> str:
        object_id, self.next_object_id = mint_object_id(kind, self.next_object_id)
        return object_id

    def _current_causal_context_ids(self) -> list[str]:
        """Return the canonical events that provide context for the next submission."""

        fork_context_event_id = self._selected_head_event_id()
        active_branch_head = self._current_branch_record().head_event_id
        return [
            event_id
            for event_id in (fork_context_event_id, active_branch_head)
            if isinstance(event_id, str)
        ]

    def _preferred_kind(self, preferred_names: list[str]) -> str:
        for name in preferred_names:
            if name in self.entity_definitions:
                return name
        return next(iter(self.entity_definitions))

    def _accept_canonical_event(
        self,
        branch_name: str,
        parent_event_id: str | None,
        event_type: str,
        event_family: str,
        target_identity: str,
        payload: dict[str, object],
        causal_references: list[str] | None = None,
    ) -> CanonicalEvent:
        """Append one accepted canonical event to history and update selection."""

        # Canonical apply stays separate from validation: by the time we get
        # here, the event is already allowed. This step only creates the
        # accepted canonical record and updates controller-owned selection.
        record_model, resolved_branch_name = create_canonical_event(
            next_sequence=self.next_sequence,
            branch_name=branch_name,
            parent_event_id=parent_event_id,
            event_type=event_type,
            event_family=event_family,
            target_identity=target_identity,
            observer_identity=self.observer_identity,
            timestamp=self._event_timestamp(),
            catalog_version=self.catalog_version,
            payload=payload,
            existing_events=self.events,
            causal_references=causal_references,
        )
        self.events[record_model.event_id] = record_model
        self.next_sequence += 1
        self.selected_branch = resolved_branch_name
        self.selected_canonical_event_id = record_model.event_id
        return record_model

    # ------------------------------------------------------------------
    # Teaching Example Seeding
    # ------------------------------------------------------------------

    def _seed_teaching_event(
        self,
        branch_name: str,
        parent_event_id: str | None,
        kind: str,
        tile: tuple[int, int],
        event_type: str,
        action_name: str,
    ) -> tuple[str, str]:
        """Create one guaranteed-valid canonical event for the teaching example."""

        # The teaching example should exercise the exact same acceptance path as
        # live runtime actions. Seeding stays honest by reusing replay, rule
        # validation, and invariant-state transition helpers instead of writing
        # event records directly.
        canonical_state = self._replay_branch_state(parent_event_id)
        minted_definition = self._catalog_minted_definition(kind)
        allowed, reason = self._evaluate_invariant_rules(
            minted_definition,
            action_name,
            tile,
            canonical_state,
            parent_event_id=parent_event_id,
            causal_reference_ids=[parent_event_id] if isinstance(parent_event_id, str) else [],
        )
        if not allowed:
            raise ValueError(f"Teaching example rejected for {kind}: {reason}")
        allowed, reason, next_state = self._transition_invariant_state(minted_definition, action_name)
        if not allowed:
            raise ValueError(f"Teaching example transition failed for {kind}: {reason}")
        object_id = self._mint_object_id(kind)
        record = self._accept_canonical_event(
            branch_name,
            parent_event_id,
            event_type,
            "structural",
            object_id,
            PlacedObjectPayload(
                object_id=object_id,
                kind=kind,
                x=tile[0],
                y=tile[1],
                invariant_state=next_state,
                minted_definition=minted_definition,
            ).to_dict(),
            causal_references=[parent_event_id] if isinstance(parent_event_id, str) else [],
        )
        return record.event_id, record.branch_hint

    def _load_teaching_example(self, modal: tk.Toplevel | None = None) -> None:
        """Seed a small event graph with one fork for first-time exploration."""

        self._reset_runtime_state()
        plan = load_teaching_example_plan(TEACHING_EXAMPLE_PATH)
        event_ids_by_step: dict[str, str] = {}
        branch_names_by_step: dict[str, str] = {}

        for step in plan.steps:
            kind = self._preferred_kind(step.kind_preferences)
            if step.branch_source == "main":
                branch_name = "main"
            elif step.branch_source.startswith("fork:"):
                fork_step_id = step.branch_source.split(":", 1)[1]
                branch_name = self._branch_name_for_fork(event_ids_by_step[fork_step_id])
            else:
                branch_name = branch_names_by_step[step.branch_source]
            parent_event_id = event_ids_by_step.get(step.parent_step_id) if step.parent_step_id else None
            event_id, resolved_branch_name = self._seed_teaching_event(
                branch_name,
                parent_event_id,
                kind,
                step.tile,
                step.event_type,
                step.action_name,
            )
            event_ids_by_step[step.step_id] = event_id
            branch_names_by_step[step.step_id] = resolved_branch_name

        self.selected_branch = plan.final_state.selected_branch
        self.selected_canonical_event_id = event_ids_by_step[plan.final_state.selected_head_step_id]
        self.teaching_example_loaded = True
        self.observer_local_x, self.observer_local_y = plan.final_state.observer_position
        self.observer_facing = plan.final_state.observer_facing
        self.observer_build_selection = self._preferred_kind(
            next(step.kind_preferences for step in plan.steps if step.step_id == plan.final_state.build_selection_step_id)
        )
        self._push_server_log(
            "teaching example loaded -> main lineage plus forked lineage from the first canonical event"
        )
        self._push_observer_log(
            "teaching example ready -> "
            f"main head {event_ids_by_step[plan.final_state.selected_head_step_id]}, "
            f"fork head {event_ids_by_step[plan.final_state.build_selection_step_id]}, "
            f"selected build kind {self.observer_build_selection}"
        )
        self._save_state()
        if isinstance(modal, tk.Toplevel) and modal.winfo_exists():
            modal.destroy()
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())

    # ------------------------------------------------------------------
    # Observer-Local Interaction
    # ------------------------------------------------------------------

    def _move_observer_locally(self, dx: int, dy: int, facing: str) -> None:
        self.observer_local_x = max(0, min(self.grid_size - 1, self.observer_local_x + dx))
        self.observer_local_y = max(0, min(self.grid_size - 1, self.observer_local_y + dy))
        self.observer_facing = facing
        self._push_observer_log(f"observer-local movement -> ({self.observer_local_x}, {self.observer_local_y}) facing {facing}")
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())

    def _tile_in_front(self) -> tuple[int, int]:
        return tile_in_front(self.observer_local_x, self.observer_local_y, self.observer_facing, self.grid_size)

    def _find_object_at_tile(
        self,
        tile: tuple[int, int],
        canonical_state: ReplayBranchState,
    ) -> ReplayObjectRecord | None:
        """Return the canonical object on a tile, if one exists."""

        return find_object_at_tile(tile, canonical_state)

    def _first_open_canonical_tile(self, canonical_state: ReplayBranchState) -> tuple[int, int] | None:
        """Scan the grid top-left to bottom-right for the first open canonical tile."""

        return first_open_canonical_tile(canonical_state, self.grid_size, self.server_reserved_tiles)

    def _queue_build_candidate(self, kind: str | None = None, modal: tk.Toplevel | None = None) -> None:
        tile = self._tile_in_front()
        selected_kind = kind or self.observer_build_selection
        if selected_kind not in self.entity_definitions:
            selected_kind = next(iter(self.entity_definitions))
        self.observer_build_selection = selected_kind
        self.invariant_boundary_candidates.append(queue_build_candidate(selected_kind, tile))
        self._push_observer_log(f"invariant-boundary candidate -> build {selected_kind} @ ({tile[0]}, {tile[1]})")
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())
        if isinstance(modal, tk.Toplevel) and modal.winfo_exists():
            modal.destroy()
        if self.observer_auto_reconcile:
            self._reconcile_invariant_boundary_candidates()

    def _queue_destroy_candidate(self) -> None:
        tile = self._tile_in_front()
        self.invariant_boundary_candidates.append(queue_destroy_candidate(tile))
        self._push_observer_log(f"invariant-boundary candidate -> destroy @ ({tile[0]}, {tile[1]})")
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())
        if self.observer_auto_reconcile:
            self._reconcile_invariant_boundary_candidates()

    # ------------------------------------------------------------------
    # Invariant-Boundary Reconciliation
    # ------------------------------------------------------------------

    def _validate_and_transition_action(
        self,
        minted_definition: MintedDefinition,
        action_name: str,
        tile: tuple[int, int],
        canonical_state: ReplayBranchState,
        current_state: dict[str, object] | None = None,
        parent_event_id: str | None = None,
        causal_context_ids: list[str] | None = None,
    ) -> tuple[bool, str, dict[str, object]]:
        """Run invariant checks, then apply the matching genome transition."""

        # Read this helper as the shared acceptance pipeline used by build,
        # destroy, and server-mint flows: first validate against canonical
        # context, then compute the next invariant state if validation passes.
        allowed, reason = self._evaluate_invariant_rules(
            minted_definition,
            action_name,
            tile,
            canonical_state,
            current_state=current_state,
            parent_event_id=parent_event_id,
            causal_reference_ids=causal_context_ids,
        )
        if not allowed:
            return False, reason, {}
        return self._transition_invariant_state(minted_definition, action_name, current_state)

    def _accept_build_candidate(
        self,
        branch_name: str,
        parent_event_id: str | None,
        causal_context_ids: list[str],
        canonical_state: ReplayBranchState,
        action: CandidateEvent,
    ) -> tuple[bool, str | None, ReplayBranchState]:
        """Try to turn one queued build candidate into a canonical event."""

        return accept_build_candidate(self, branch_name, parent_event_id, causal_context_ids, canonical_state, action)

    def _accept_destroy_candidate(
        self,
        branch_name: str,
        parent_event_id: str | None,
        causal_context_ids: list[str],
        canonical_state: ReplayBranchState,
        action: CandidateEvent,
    ) -> tuple[bool, str | None, ReplayBranchState]:
        """Try to turn one queued destroy candidate into a canonical event."""

        return accept_destroy_candidate(self, branch_name, parent_event_id, causal_context_ids, canonical_state, action)

    def _reconcile_invariant_boundary_candidates(self) -> None:
        reconcile_invariant_boundary_candidates(self)

    def _mint_from_server(self, kind: str, modal: tk.Toplevel | None = None) -> None:
        mint_from_server(self, kind, modal)

    # ------------------------------------------------------------------
    # Canvas And Layout
    # ------------------------------------------------------------------

    def _on_resize(self, event: tk.Event) -> None:
        if event.widget is self.root:
            self._draw_scene(max(900, event.width), max(620, event.height))

    def _clear_widgets(self) -> None:
        clear_widgets(self.widgets)

    def _main_window_hotkeys_enabled(self) -> bool:
        return main_window_hotkeys_enabled(self.root)

    def _run_main_window_hotkey(self, action: Callable[[], None]) -> None:
        run_main_window_hotkey(self.root, action)

    def _handle_escape(self) -> None:
        handle_escape(self.root, self._close)

    def _add_widget(self, x: float, y: float, widget: tk.Widget, anchor: str = "nw") -> None:
        add_widget(self, x, y, widget, anchor)

    def _button(self, label: str, command: object) -> tk.Button:
        return make_button(self, label, command)

    # ------------------------------------------------------------------
    # Main Pane Rendering
    # ------------------------------------------------------------------

    def _draw_scene(self, width: int, height: int) -> None:
        """Redraw the two-pane teaching layout from current runtime state."""

        draw_scene(self, width, height)

    def _draw_pane_shell(self, x: float, y: float, w: float, h: float, title: str) -> tuple[float, float, float, float]:
        return draw_pane_shell(self, x, y, w, h, title)

    def _draw_server_pane(self, x: float, y: float, w: float, h: float) -> None:
        """Render replay-derived canonical state and canonical navigation tools."""

        draw_server_pane(self, x, y, w, h)

    def _draw_observer_pane(self, x: float, y: float, w: float, h: float) -> None:
        """Render observer-local state and invariant-boundary submission controls."""

        draw_observer_pane(self, x, y, w, h)

    def _set_auto_reconcile(self, enabled: bool) -> None:
        self.observer_auto_reconcile = bool(enabled)
        self._push_observer_log(f"auto reconciliation -> {'on' if enabled else 'off'}")
        self._draw_scene(self.root.winfo_width(), self.root.winfo_height())

    def _canonical_pane_lens(self) -> CanonicalPaneLens:
        """Build the data handed from runtime into the canonical render lens."""

        # These one-line lens helpers are the explicit handoff points from the
        # runtime/controller into the narrower UI-facing adapter layer.
        return build_canonical_pane_lens(self)

    def _observer_pane_lens(self) -> ObserverPaneLens:
        """Build the data handed from runtime into the observer render lens."""

        return build_observer_pane_lens(self)

    def _history_card_lenses(self) -> list[HistoryCardLens]:
        """Build history-card data handed from runtime into the history lens."""

        return build_history_card_lenses(self)

    def _timeline_modal_lens(self) -> TimelineModalLens:
        """Build timeline data handed from runtime into the timeline lens."""

        return build_timeline_modal_lens(self)

    def _mint_action_modal_lens(self) -> MintActionModalLens:
        """Build server-mint modal data handed from runtime into the action lens."""

        return build_mint_action_modal_lens(self)

    def _build_action_modal_lens(self) -> BuildActionModalLens:
        """Build observer build-modal data handed from runtime into the action lens."""

        return build_build_action_modal_lens(self)

    def _candidate_queue_lens(self) -> CandidateQueueLens:
        """Build queued-candidate modal data handed from runtime into the action lens."""

        return build_candidate_queue_lens(self)

    def _draw_grid(self, x1: float, y1: float, x2: float, y2: float, lens: GridLens) -> None:
        draw_grid(self, x1, y1, x2, y2, lens)

    # ------------------------------------------------------------------
    # Modal Helpers
    # ------------------------------------------------------------------

    def _open_modal(self, title: str, geometry: str) -> tk.Toplevel:
        return open_modal(self.root, title, geometry, BG)

    def _open_mint_editor(self) -> None:
        open_mint_editor(self)

    def _reload_catalog(self, modal: tk.Toplevel | None = None) -> None:
        reload_catalog(self, modal)

    def _execute_action_request(self, request: ActionRequest, modal: tk.Toplevel | None = None) -> None:
        """Execute one action request handed back from an action-oriented UI lens."""

        # This is the controller-side boundary for UI intent. Lenses emit
        # typed requests, and the runtime translates those requests into the
        # existing mutation methods here. If a new button or click target needs
        # to mutate runtime state, prefer adding a request type and handling it
        # here instead of wiring the UI directly into runtime internals.
        #
        # Debugging tip:
        # - if a button renders incorrectly, inspect the lens builder first
        # - if the button renders correctly but does the wrong thing, inspect
        #   the request type and this dispatch method second
        dispatch_action_request(self, request, modal)

    # ------------------------------------------------------------------
    # Server / Observer Action Modals
    # ------------------------------------------------------------------

    def _open_mint_modal(self) -> None:
        """Open the server-side mint chooser."""

        open_mint_modal(self)

    def _open_build_modal(self) -> None:
        """Open the observer-side build chooser."""

        open_build_modal(self)

    def _open_candidate_modal(self) -> None:
        """Open the queue of observer-side invariant-boundary candidates."""

        open_candidate_modal(self)

    def _clear_candidates(self, modal: tk.Toplevel) -> None:
        clear_candidates(self, modal)

    # ------------------------------------------------------------------
    # Teaching Modals
    # ------------------------------------------------------------------

    def _open_teaching_modal(self) -> None:
        """Open the teaching-oriented overview of the prototype."""

        open_teaching_modal(self)

    def _open_walkthrough_modal(self) -> None:
        """Open the step-by-step walkthrough for exploring CrypSA ideas."""

        open_walkthrough_modal(self)

    def _open_model_notes_modal(self) -> None:
        """Open the compact summary of the model this prototype teaches."""

        open_model_notes_modal(self)

    def _open_hotkeys_modal(self) -> None:
        """Open the keyboard shortcuts reference for the prototype."""

        open_hotkeys_modal(self)

    def _open_canonical_pane_help_modal(self) -> None:
        """Open the canonical-pane help popup."""

        open_pane_help_modal(self, "canonical")

    def _open_observer_pane_help_modal(self) -> None:
        """Open the observer-pane help popup."""

        open_pane_help_modal(self, "observer")

    def _try_beacon_path(self, modal: tk.Toplevel | None = None) -> None:
        """Prepare the built-in Beacon teaching path and open the build chooser."""

        try_beacon_path(self, modal)

    # ------------------------------------------------------------------
    # Timeline / History Hooks
    # ------------------------------------------------------------------

    def _open_history_modal(self) -> None:
        open_history_modal(self)

    def _select_history_event(self, event_id: str, preferred_branch_name: str | None, modal: tk.Toplevel) -> None:
        select_history_event(self, event_id, preferred_branch_name, modal)

    def _branch_rows(self) -> list[BranchRecord]:
        rows = self._build_branch_rows()

        def branch_depth(branch_name: str) -> int:
            depth = 0
            row_map = {branch.name: branch for branch in rows}
            current = row_map[branch_name].parent_branch
            while isinstance(current, str) and current in row_map:
                depth += 1
                current = row_map[current].parent_branch
            return depth

        return sorted(
            rows,
            key=lambda branch: (branch_depth(branch.name), branch.name.lower()),
        )

    def _timeline_events_for_branch(self, branch: BranchRecord) -> list[CanonicalEvent]:
        return self._event_chain(branch.head_event_id)

    def _select_timeline_event(self, branch_name: str, event_id: str) -> None:
        if self._branch_record_by_name(branch_name) is not None:
            self.selected_branch = branch_name
        if event_id in self.events:
            self.selected_canonical_event_id = event_id

    def _timeline_connector_origin(self, branch: BranchRecord) -> tuple[str, str] | None:
        if branch.parent_branch is None or branch.fork_from_event_id is None:
            return None
        return branch.parent_branch, branch.fork_from_event_id

    def _open_timeline_modal(self) -> None:
        open_timeline_modal(self)

    def _center_observer_near_canonical_state(self, modal: tk.Toplevel | None = None) -> None:
        center_observer_near_canonical_state(self, modal)

def main() -> None:
    app = CrypSATeachingPrototype()
    app.root.mainloop()


if __name__ == "__main__":
    main()
