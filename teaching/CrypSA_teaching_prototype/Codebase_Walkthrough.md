# CrypSA Codebase Walkthrough

## Purpose

This document is a guided tour of how the codebase works.

It is not a reference file and it is not a user manual.

Use it when you want to answer questions like:

- Where should I start reading?
- What happens when I click a button in the app?
- Which file owns runtime meaning vs UI drawing vs Mint validation?
- How do observer actions become canonical events?

If you want a file-by-file authority, use the `REFERENCE.md` files.
If you want the shortest project summary, use `README.md`.
If you want the current artifact status and maintenance posture, use `STATUS.md`.
If you want to follow the code as a system, use this walkthrough.
If you want the architecture-protection rules for future changes, read `implementation/CrypSA_Refactor_Guardrails.md`.
For the authoritative adapter and observer-model docs, see `../../architecture/CrypSA_Adaptor_Model.md` and `../../architecture/CrypSA_Client_Observer_Model.md`.

If you reach a question that sounds more like full CrypSA architecture or deployment than prototype behavior, pause here and read `Prototype_vs_Current_CrypSA_Model.md` before jumping into `repo/`.

## The Core Mental Model

The whole project is built around one teaching split:

1. The observer can do things locally.
2. Those actions are not automatically canonical.
3. Build and destroy actions become candidate events at the invariant boundary.
4. Canonical reconciliation checks those candidate events against canonical rules.
5. Accepted candidate events become canonical events in accepted canonical history.
6. Canonical state is rebuilt by replaying that accepted canonical history.

Almost every important file exists to support one part of that loop.

## The Best Reading Order

Read the code in this order:

1. `README.md`
   This gives the scope, non-goals, and top-level module map.
2. `STATUS.md`
   This explains that the prototype is considered complete for purpose and should be maintained as a teaching artifact.
3. `crypsa/crypsa_teaching_prototype.py`
   This is the application brain. Read it to understand what the app means.
4. `crypsa/runtime_store.py`
   This shows the grouped mutable runtime state owned by the prototype.
5. `crypsa/runtime_models.py`
   This shows the first typed runtime model layer, starting with candidate events.
6. `crypsa/runtime_actions.py`
   This shows the extracted helper layer for common observer-side actions and candidate-event construction.
7. `crypsa/validation.py`
   This shows the extracted invariant-rule evaluation step for candidate-event acceptance.
8. `crypsa/reconciliation.py`
   This shows the extracted candidate-reconciliation and server-mint flow that used to sit inline in the controller.
9. `crypsa/canonical_apply.py`
   This shows how accepted canonical records are created once a candidate event passes validation.
10. `crypsa/canonical_replay.py`
   This shows the extracted replay-derived canonical-state helpers used by the controller.
11. `crypsa/app_shell.py`
   This shows the extracted Tk app-shell layer for root creation, hotkeys, modal shell behavior, and widget cleanup.
12. `crypsa/controller_ui_actions.py`
   This shows the extracted controller-side UI coordination helpers such as catalog reload, Beacon-path setup, and observer recentering.
13. `crypsa/crypsa_lens_adapters.py`
   This shows the adapter/translation layer between runtime meaning and the specific UI lenses.
14. `crypsa/crypsa_action_requests.py`
   This shows the typed UI-intent objects handed back to the runtime controller.
15. `crypsa/request_dispatch.py`
   This shows the request-routing layer that keeps typed UI intent dispatch out of the controller body.
16. `crypsa/runtime_persistence.py`
   This shows the schema-aware runtime-store load/save boundary that keeps persistence coordination out of the controller body.
17. `crypsa/crypsa_event_graph.py`
   This explains how accepted canonical history becomes replay-derived state.
18. `crypsa/ui/crypsa_render_ui.py`
   This shows how the two-pane main window is painted.
19. `crypsa/ui/crypsa_history_ui.py`
   This shows how history and timeline inspection work.
20. `crypsa/ui/crypsa_action_ui.py`
   This shows how Mint, Build, and Candidates dialogs gather actions.
21. `crypsa/ui/crypsa_teaching_ui.py`
   This is the teaching-copy layer.
22. `mint/mint_catalog_editor.py`
   This is the standalone Mint editor orchestration layer.
23. `mint/mint_models.py`
   This shows the typed shared Mint structure layer used by the editor, store, and runtime-side frozen-definition handoff.
24. `mint/mint_lens_adapters.py`
   This shows the Mint-side translation boundary between catalog state and UI-friendly detail/modal data.
25. `mint/mint_editor_ui.py`
   This is the Mint modal presentation layer.
26. `mint/mint_catalog_store.py`
    This is the schema and persistence boundary for Mint.

That order goes from app meaning, to replay rules, to UI presentation, to Mint authoring.

If that full order feels too large, use this shorter first pass:

1. `README.md`
2. `STATUS.md`
3. `crypsa/crypsa_teaching_prototype.py`
4. `crypsa/runtime_store.py`
5. `crypsa/runtime_actions.py`
6. `crypsa/validation.py`
7. `crypsa/reconciliation.py`
8. `crypsa/canonical_apply.py`
9. `crypsa/canonical_replay.py`
10. `crypsa/app_shell.py`
11. `crypsa/crypsa_lens_adapters.py`
12. `crypsa/request_dispatch.py`
13. `crypsa/runtime_persistence.py`
14. `crypsa/ui/crypsa_action_ui.py`
15. `mint/mint_catalog_editor.py`

That shorter pass is usually enough to understand the project shape before you dive into replay details or schema validation.

If you are debugging one specific kind of question, use this shortcut instead:

- accepted/rejected candidate event question -> `crypsa/validation.py`, then `crypsa/reconciliation.py`
- accepted canonical record question -> `crypsa/canonical_apply.py`
- replay-derived visible state question -> `crypsa/canonical_replay.py`, then `crypsa/crypsa_event_graph.py`
- root window / modal / hotkey question -> `crypsa/app_shell.py`
- UI click / button intent question -> `crypsa/crypsa_action_requests.py`, then `crypsa/request_dispatch.py`
- UI display-shaping question -> `crypsa/crypsa_lens_adapters.py`
- Mint schema / normalization question -> `mint/mint_catalog_store.py`

## How The Project Is Split

The cleanest high-level stack is:

1. runtime/controller
2. replay/event graph
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

### Runtime meaning

`crypsa/crypsa_teaching_prototype.py` owns the runtime orchestration and the app-level decisions.

This file answers questions like:

- What state does the app keep in memory?
- Which extracted runtime helper should run next?
- What happens when a build or destroy candidate event is queued?
- How are candidates reconciled?
- How are canonical events accepted and replayed?

When you want to know what the prototype means, start here.

In the current structure, the runtime file is also the controller:

- UI lenses emit typed requests
- the runtime executes those requests
- the runtime rebuilds lens data for the next redraw

If you are ever asking "who is actually in charge here?", the answer is almost always this file.

The main exceptions now live in small runtime boundary modules:

- `crypsa/runtime_store.py`: grouped mutable runtime state
- `crypsa/runtime_actions.py`: common observer-side actions and typed candidate creation
- `crypsa/validation.py`: candidate-event acceptance checks
- `crypsa/reconciliation.py`: candidate reconciliation and server-mint acceptance flow
- `crypsa/canonical_apply.py`: accepted canonical record creation
- `crypsa/canonical_replay.py`: replay-derived canonical state helpers
- `crypsa/app_shell.py`: Tk app-shell and hotkey/widget lifecycle helpers
- `crypsa/controller_ui_actions.py`: controller-side UI coordination helpers that still need logs, redraws, or modal coordination
- `crypsa/request_dispatch.py`: typed UI request routing
- `crypsa/runtime_persistence.py`: schema-aware runtime-store load/save coordination

So the controller still owns orchestration, but it no longer has to own every step inline.

### Event replay

`crypsa/crypsa_event_graph.py` owns replay and lineage helpers.

This file answers:

- How are events ordered?
- How do we walk backward through lineage?
- How is visible canonical state reconstructed?
- How are human-facing branch rows derived?

This file is the cleanest expression of the event-first model.

Read it in this order:

1. stable ordering helpers
2. lineage-walk helpers
3. branch-row derivation
4. replay back into visible state

### UI drawing

The `crypsa/ui` folder owns presentation, not runtime meaning.

Use these files like this:

- `crypsa_render_ui.py`: the main two-pane window
- `crypsa_history_ui.py`: history and timeline inspection
- `crypsa_action_ui.py`: Mint/build/candidate modals
- `crypsa_teaching_ui.py`: explanatory teaching dialogs

If you are reading a UI file and asking "but where does this state come from?", the answer is usually "back in `crypsa_teaching_prototype.py`".

More specifically, the current handoff usually looks like:

1. runtime/controller prepares lens data in `crypsa_lens_adapters.py`
2. UI module renders that lens data
3. UI module emits typed requests from `crypsa_action_requests.py`
4. runtime/controller executes the request

That adapter/request split is now the main way to read the UI architecture.

## One Concrete Adapter Flow

If you want to understand the new boundary pattern quickly, trace one button from start to finish.

The cleanest example is `Submit Build Candidate` in the Build modal.

### Stage 1: runtime opens the modal

`crypsa/crypsa_teaching_prototype.py` owns `_open_build_modal()`.

That method does not build the widget tree itself. It delegates to `crypsa/ui/crypsa_action_ui.py`.

### Stage 2: runtime prepares a lens

Before the modal renders, the UI asks the runtime for `_build_action_modal_lens()`.

That forwards into `crypsa/crypsa_lens_adapters.py`, specifically `build_build_action_modal_lens()`.

This builder translates raw runtime/catalog state into:

- target tile text
- teaching-example state
- one card lens per Mint kind
- one typed request per card

At this stage, the Build modal no longer needs to ask questions like:

- what kind is selected?
- which hints should be shown?
- what request should this button fire?

That work is already done.

### Stage 3: UI renders the lens

`crypsa/ui/crypsa_action_ui.py` reads the `BuildActionModalLens` and renders cards.

Each card already has:

- summary strings
- context hints
- Beacon hint, if relevant
- a `QueueBuildCandidateRequest`

So the UI code stays focused on layout and button wiring.

### Stage 4: UI emits a typed request

When the user clicks `Submit Build Candidate`, the button does not call `_queue_build_candidate()` directly.

Instead, it hands the card's `QueueBuildCandidateRequest` back through:

`app._execute_action_request(req, modal)`

That is the key boundary.

The UI says:

- "the user wants to queue this kind"

It does not say:

- "call this runtime mutation method with these internal assumptions"

### Stage 5: runtime routes and executes the request

Back in `crypsa/crypsa_teaching_prototype.py`, `_execute_action_request()` delegates into `crypsa/request_dispatch.py`, which matches the request type and routes it to the correct controller mutation.

For `QueueBuildCandidateRequest`, it calls `_queue_build_candidate(request.kind, modal)`.

That is where runtime mutation still lives:

- figure out the tile in front of the observer
- record the candidate
- log the action
- redraw the app

### Stage 6: redraw rebuilds fresh lens data

After the mutation, the runtime redraws the main window.

That redraw rebuilds pane lenses from current state, so the observer pane and candidate count update from fresh translated data rather than stale UI-local state.

### Why this matters

This split keeps responsibilities cleaner:

- runtime/controller owns meaning and mutation
- adapter layer owns translation
- UI layer owns rendering and event wiring
- request types make user intent explicit

When you add a new interactive UI feature, the best pattern is usually:

1. add or extend a lens
2. add a request type if mutation is needed
3. render the lens in the UI module
4. route the request through `request_dispatch.py`
5. handle the mutation in the targeted controller method

### Mint authoring

The `mint` folder owns the standalone Mint editor and the catalog schema.

Use these files like this:

- `mint_catalog_editor.py`: editor orchestration, list/detail view, save actions
- `mint_editor_ui.py`: edit modal and tag-manager UI
- `mint_catalog_store.py`: load/save, normalization, validation, defaults

The runtime reads from Mint. The editor writes to Mint.

## Read The History And Timeline UI As Layers

`crypsa/ui/crypsa_history_ui.py` is easier to follow if you read each modal as a staged view instead of one large Tk block.

### History modal

Read it in this order:

1. modal shell and framing text
2. scrollable container
3. one history card per accepted event
4. selection callback

Each history card combines:

- the accepted event record
- the lineage context that explains where that event appears in branch rows

### Timeline modal

Read it in this order:

1. heading and legend
2. scrollable row canvas
3. right-hand event inspector
4. click handler that updates runtime selection

That file becomes much easier once you treat the helper functions as part of the modal structure instead of as unrelated utilities.

## Read The Action Modals By Teaching Purpose

`crypsa/ui/crypsa_action_ui.py` contains three different kinds of modal, and they are easier to understand if you read them by purpose.

### Server Mint

This is the short contrast case.

It shows direct canonical creation with very little ceremony.

### Build

This is the teaching-heavy action list.

It spends more space on context hints, Beacon guidance, and per-kind summaries because observer-side build is the main teaching path.

### Candidates

This is just a queue inspector.

It does not create new actions. It shows pending candidate events and lets the user clear them.

## Follow One Common Flow: Queue And Reconcile A Build

This is the single best flow to understand the codebase.

### Step 1: the user opens Build

The observer-side button is rendered in `crypsa/ui/crypsa_render_ui.py`.

That button calls back into `app._open_build_modal()`, which lives in `crypsa/crypsa_teaching_prototype.py` and delegates to `crypsa/ui/crypsa_action_ui.py`.

This is the standard pattern in the project:

- the runtime owns meaning and callbacks
- the UI module renders the dialog

More recent adapter note:

- the action modal now renders pre-shaped build/mint/candidate lens data
- button clicks emit typed requests back to the runtime controller instead of calling mutation methods directly

### Step 2: the build candidate is queued

When the user submits a build in the modal, the runtime ends up in `_queue_build_candidate()` in `crypsa/crypsa_teaching_prototype.py`.

That method:

- figures out the tile in front of the observer
- records a candidate in `invariant_boundary_candidates`
- logs what happened
- redraws the UI

At this point, a candidate event exists, but nothing canonical has been accepted yet.

### Step 3: reconciliation begins

When the user presses `Reconcile` or `Enter`, the runtime goes into `_reconcile_invariant_boundary_candidates()`.

Read that method top-down as a staged flow:

1. Choose the writable branch.
2. Collect causal context.
3. Replay the canonical state for that branch head.
4. Try each candidate event one at a time.
5. Accept or reject each candidate event.
6. Redraw the UI.

This method is now mostly a controller entry point. The heavy acceptance detail lives in `crypsa/reconciliation.py`.

### Step 4: validation and transition happen

The shared acceptance helper is `_validate_and_transition_action()`.

That helper first calls `_evaluate_invariant_rules()` and then `_transition_invariant_state()`.

That split matters:

- validation decides whether the candidate event is allowed
- transition decides what invariant state the accepted object should move into

The first part now lives behind `crypsa/validation.py`. The candidate acceptance flow now lives in `crypsa/reconciliation.py`, while canonical record creation lives in `crypsa/canonical_apply.py`.

### Step 5: a canonical event is accepted

If canonical validation passes, the runtime eventually calls `_accept_canonical_event()`.

That method creates the accepted canonical event record and stores it in `events`.

This is the point where the action becomes canonical history.

### Step 6: canonical state is replayed

Later, when the UI needs visible canonical state, the runtime calls back into `crypsa/crypsa_event_graph.py`, especially `replay_branch_state()`.

That function rebuilds visible state from accepted canonical history.

The codebase is teaching a specific idea here:

- accepted canonical history is the substrate of truth
- visible canonical state is replay-derived

## Follow Another Flow: Select A Historical Event

This is the second most useful flow to read.

### Step 1: the user opens History or Timeline

The main window buttons live in `crypsa/ui/crypsa_render_ui.py`.

The History and Timeline modals themselves live in `crypsa/ui/crypsa_history_ui.py`.

### Step 2: the user selects an older event

Selection requests originate in `crypsa/ui/crypsa_history_ui.py` and are executed by the runtime controller.

That code updates:

- `selected_branch`
- `selected_canonical_event_id`

### Step 3: the viewed canonical state changes

The left pane does not keep a separate stored state object as truth.

Instead, the runtime asks for `_visible_canonical_state()`, which replays from the selected head event.

This is why picking older history changes the visible canonical world.

### Step 4: reconciliation can fork lineage

If you reconcile from a historical selection that is not the current branch head, `_ensure_writable_branch()` in `crypsa/crypsa_teaching_prototype.py` moves reconciliation onto a forked lineage.

That is the key teaching reason the Timeline view exists.

## Follow The Mint Side

The Mint side is simpler if you read it as a three-layer stack.

### Layer 1: editor orchestration

`mint/mint_catalog_editor.py` owns:

- the root window
- the list of Mint kinds
- the detail pane
- add/edit/remove/tag/reload actions
- saving

Read this file when you want to know what the editor does.

### Layer 2: modal presentation

`mint/mint_editor_ui.py` owns:

- popup creation
- field widgets
- the Mint kind edit modal
- the tag-manager modal

Read this file when you want to know how the editor gathers user input.

### Layer 3: schema and persistence

`mint/mint_catalog_store.py` owns:

- defaults
- normalization
- validation
- load/save

Read this file when you want to know what a valid Mint catalog actually is.

The easiest reading pattern for the Mint side is:

1. editor action in `mint_catalog_editor.py`
2. detail/modal translation in `mint_lens_adapters.py`
3. modal input gathering in `mint_editor_ui.py`
4. schema truth in `mint_catalog_store.py`

There is now also a narrower Mint translation layer:

- `mint_lens_adapters.py` prepares detail-pane and modal starter data so the Mint UI can render prepared values instead of pulling everything directly from editor state

## The Most Important Runtime State

If you get lost in `crypsa/crypsa_teaching_prototype.py`, group the state like this.

### Observer-local state

- `observer_local_x`
- `observer_local_y`
- `observer_facing`
- `observer_build_selection`
- `observer_auto_reconcile`

### Candidate state

- `invariant_boundary_candidates`

### Canonical-history state

- `events`
- `next_sequence`
- `selected_branch`
- `selected_canonical_event_id`

### Teaching and inspection state

- `teaching_example_loaded`
- `server_log`
- `observer_log`

That grouping usually makes the large app file much easier to parse.

## How To Read The Helper Functions

Several files were recently cleaned up to use more nearby helper functions.

That means the best reading style is now:

1. Read the top-level method first.
2. Identify the named helper stages it calls.
3. Only drop into those helpers when you need more detail.

Examples:

- In `crypsa_teaching_prototype.py`, read `_reconcile_invariant_boundary_candidates()` before the per-action helpers.
- In `crypsa/ui/crypsa_render_ui.py`, read `draw_server_pane()` and `draw_observer_pane()` before the summary/banner helpers.
- In `crypsa/ui/crypsa_history_ui.py`, read `open_timeline_modal()` before the branch-selection or inspector helpers.
- In `mint/mint_editor_ui.py`, read `open_entity_modal()` before the scrollable-body, tag-selector, or genome-editor helpers.
- In `mint/mint_catalog_store.py`, read `load_catalog()` and `normalize_genome()` before the smaller parsing helpers.

There is now a parallel reading pattern for UI boundaries:

1. read the top-level runtime action or redraw entrypoint
2. read the matching lens builder in an adapter module
3. read the UI renderer or modal that consumes that lens
4. read the request type and `request_dispatch.py` path if the UI is interactive

## The One Teaching Example To Keep In Mind

The built-in `Beacon` Mint kind is the clearest concrete example of the model.

It demonstrates that:

- `lineage_parent` drives replay
- `causal_references` do not drive replay
- `causal_references` can still matter for validation

If you want one end-to-end feature to follow through the codebase, Beacon is the best one.

## Which Doc To Use When

Use the docs like this:

- `README.md`: project scope and top-level map
- `STATUS.md`: artifact status, maintenance posture, and scope freeze
- `summary.txt`: current handoff state
- `Codebase_Walkthrough.md`: guided reading tutorial
- `implementation/CrypSA_Refactor_Guardrails.md`: architecture-protection rules for future refactors
- `Prototype_vs_Current_CrypSA_Model.md`: scope boundary between this teaching prototype and the broader CrypSA model in `repo/`
- `Runtime_Schema.md`: runtime save-file shape
- `Mint_Editor_Usage.md`: how to use the Mint editor as a user
- `Manual_Regression_Checklist.md`: repeatable smoke test for Tk flows and Mint save/reload paths
- `crypsa/REFERENCE.md`: runtime package reference
- `crypsa/ui/REFERENCE.md`: UI package reference
- `mint/REFERENCE.md`: Mint package reference

Fast rule:

- use `README.md` for scope
- use `STATUS.md` for artifact status and maintenance posture
- use `Codebase_Walkthrough.md` for flow
- use `implementation/CrypSA_Refactor_Guardrails.md` for refactor discipline
- use `Prototype_vs_Current_CrypSA_Model.md` when you need the teaching-boundary reminder
- use `REFERENCE.md` files for file ownership
- use `Manual_Regression_Checklist.md` for validation

## Final Advice

If the code feels large, do not try to read every file linearly in one pass.

Instead:

1. Pick one flow.
2. Follow it across files.
3. Return to the reference docs when you need orientation.

For this project, the best first flow is still:

1. load the teaching example
2. queue a build
3. reconcile it
4. inspect History and Timeline
5. trace the matching code path

That one loop exposes almost the entire architecture.

