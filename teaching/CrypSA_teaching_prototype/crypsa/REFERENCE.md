# CrypSA Runtime Reference

## Purpose

This folder contains the runtime side of the CrypSA Teaching Prototype.

It answers one main question:

"How does observer-local intent become canonical event history, and how does that history become visible state?"

Use this document when you want the architecture explained in prose before reading the code.

If you want a guided tutorial for following the code across files, start with `Codebase_Walkthrough.md` in the project root first, then return here for package-level reference detail.

If you want the current artifact status and maintenance posture before diving into runtime details, read `../../STATUS.md` in the project root.

If you want the quickest repeatable smoke test after changing runtime/UI behavior, use `Manual_Regression_Checklist.md` in the project root.

If you are lost while reading the runtime, come back to this file after each major source file. It is meant to be a map, not a one-time introduction.

If your question turns into "how would this work across a real deployed CrypSA runtime?", leave this package and read `../../Prototype_vs_Current_CrypSA_Model.md`, then the newer `../../architecture/` and `../../spec/` material. This package teaches the runtime loop, not the full deployment shape.

## Folder Role

The `crypsa` package owns:

- app startup and orchestration
- runtime state held in memory
- candidate-event acceptance and replay
- adapter/request handoff boundaries for UI lenses
- persistence of runtime state
- shared visual theme constants
- the main Tk window

The `crypsa/ui` subfolder contains the secondary UI modules used by this package.

The adapter/request split in this package is intentional architectural scaffolding.

It exists to:

- keep individual UI lenses from coupling too tightly to runtime internals
- shape runtime data into narrow lens-facing forms before presentation code sees it
- preserve the separation between runtime meaning and presentation logic

That matters because this prototype is not only demonstrating CrypSA concepts. It is also testing a real codebase boundary: runtime meaning should stay readable on its own, while UI modules should mostly render translated data and emit typed intent.

The easiest way to picture the codebase stack is:

1. runtime/controller
2. replay/event graph
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

## What This Folder Is Not

This package is not:

- a real network authority
- a distributed runtime
- a production anti-cheat implementation
- a concurrency or deployment testbed

Its job is to teach the runtime model clearly inside one local teaching prototype.

It should now be read as a completed teaching artifact, not as an open-ended runtime architecture sandbox.

## Main Runtime Flow

The runtime follows this loop:

1. Load the Mint catalog.
2. Load saved runtime state, if a state file exists.
3. Draw the main two-pane window.
4. Let the observer move locally or queue invariant-boundary candidate events.
5. Reconcile queued candidate events into canonical events.
6. Replay accepted canonical history to produce visible canonical state.
7. Save runtime state when the app closes or resets.

This is a teaching model of CrypSA's canonical validation loop, not a deployed network authority.

## Core Modules

### `crypsa_teaching_prototype.py`

This is the orchestration layer.

It owns:

- app-level orchestration across the extracted runtime boundaries
- controller-side mutation methods that typed requests eventually route into
- redraw timing and modal entry points
- observer-local position and facing
- the currently selected Mint kind
- invariant-boundary candidate events
- canonical event records
- branch selection and selected canonical event
- server and observer logs

When reading this file, think of it as the "application brain." It does not draw every widget directly anymore, but it still decides what the app means.

Important responsibilities:

- startup and shutdown
- shell and persistence handoff into extracted boundaries
- observer-local movement
- build and destroy candidate queuing
- reconciliation entry points into canonical events
- teaching-example seeding
- Mint catalog reload behavior
- main-window redraw triggers
- request execution for UI-originated intent

Recent readability note:

- reconciliation, server-mint, persistence, request routing, Tk shell behavior, and smaller UI coordination helpers now live behind extracted modules
- this keeps the file centralized while making the main control-flow methods easier to scan top-down
- the file still owns the mutation methods that UI-originated typed requests eventually route into

Reading tip:

- start with the state groups below so you know what the app is holding in memory
- remember that the grouped mutable state now lives in `runtime_store.py`, even though this file still exposes compatibility properties for the rest of the prototype
- then read one top-level action such as reconcile, queue build, or load teaching example
- only after that drop into the helper-stage map
- if you are debugging a UI-triggered action, pair this file with `ui/REFERENCE.md` so you can see both sides of the handoff

Helper-stage map:

- `_ensure_writable_branch()`: decide whether reconciliation continues on the active lineage or forks a new one
- `_current_causal_context_ids()`: collect the accepted events that provide contextual validation input
- `_validate_and_transition_action()`: shared acceptance pipeline for runtime actions
- `_seed_teaching_event()`: build teaching-example history through the same rule path the live runtime uses
- `_execute_action_request()`: controller-side handoff into `request_dispatch.py`

Reading shortcut:

- for acceptance-flow detail, jump from this file into `reconciliation.py`
- for request-execution detail, jump from this file into `request_dispatch.py`
- for load/save detail, jump from this file into `runtime_persistence.py`

### `teaching_example_loader.py`

This is the fixture-backed teaching-example loader.

It owns:

- loading the built-in teaching scenario from `fixtures/teaching_example.json`
- validating the fixture shape
- returning a normalized execution plan for the controller

This keeps the example content out of the controller while still letting the controller execute the same real acceptance path.

### `runtime_store.py`

This is the grouped runtime-state layer.

It owns:

- observer-local state
- accepted canonical history and current historical selection
- teaching/inspection logs

This is the first step away from having the main controller own every mutable field directly. The current controller still exposes compatibility properties, but the mutable runtime state now has one explicit home.

Reading tip:

- if you are asking "what state does the prototype actually own?", read this file before following mutations in `crypsa_teaching_prototype.py`
- if you are asking "what behavior changes this state?", return to the controller after reading this file

### `runtime_models.py`

This is the first typed runtime-model layer.

It currently owns:

- `CandidateEvent`, the typed invariant-boundary queue item
- `CanonicalEvent`, the typed accepted canonical-history record
- `ReplayObjectRecord`, the typed replay-derived canonical object
- `ReplayBranchState`, the typed replay-derived visible canonical state
- `PlacedObjectPayload`, the typed payload for build/mint object placement
- `DestroyedObjectPayload`, the typed payload for destroy-object acceptance

This is intentionally staged. The goal is to replace the highest-value anonymous dicts first without forcing a full schema rewrite all at once.

Reading tip:

- if you are debugging the invariant-boundary queue shape, start here
- if you are debugging accepted canonical history or replay-derived object state, stay here before dropping into replay code
- if you are debugging event payload shape, read `PlacedObjectPayload` / `DestroyedObjectPayload` before dropping into reconciliation

### `runtime_actions.py`

This is the observer-side action helper layer.

It currently owns:

- target-tile calculation in front of the observer
- typed build/destroy candidate creation
- observer recentering based on visible canonical state

This file keeps common observer-side action logic out of the controller while staying separate from canonical validation, accepted-record creation, and replay.

### `validation.py`

This is the extracted invariant-rule evaluation layer.

It owns:

- genome-rule checks that decide whether a candidate event can cross the invariant boundary
- contextual checks that need accepted canonical history
- accept/reject reason strings for the controller

This module is intentionally narrower than full canonical acceptance. It answers "is this candidate event allowed?" while the controller still owns transition, event creation, logging, and redraw behavior.

Reading tip:

- if you want the allow/reject logic, start here
- if you want to know what happens after acceptance, return to `crypsa_teaching_prototype.py`

### `reconciliation.py`

This is the extracted candidate-reconciliation and server-mint layer.

It owns:

- build-candidate acceptance
- destroy-candidate acceptance
- the top-level invariant-boundary reconcile loop
- server-side mint acceptance

This sits between validation/canonical-apply helpers and the controller:

- `validation.py` answers whether the candidate can pass
- `reconciliation.py` runs the candidate through the acceptance flow
- `canonical_apply.py` creates the accepted record
- the controller still owns surrounding orchestration and redraw timing

Reading tip:

- if a candidate event is accepted or rejected unexpectedly, start here before returning to the controller
- this is now the clearest place to trace build, destroy, and server-mint acceptance without Tk/UI noise

### `app_shell.py`

This is the extracted Tk app-shell layer.

It owns:

- root-window creation
- global hotkey binding
- shared modal shell creation
- widget cleanup between draw passes
- focus-gated main-window hotkey behavior

This keeps Tk window plumbing separate from runtime meaning:

- the controller still decides what actions exist
- `app_shell.py` handles how the window and hotkeys are wired

Reading tip:

- if you are debugging window creation, hotkeys, modal shell behavior, or widget cleanup, start here before reading the controller

### `controller_ui_actions.py`

This is the controller-side UI coordination layer.

It owns:

- Mint editor launch
- Mint catalog reload coordination
- candidate-queue clearing
- Beacon teaching-path preparation
- observer recentering from timeline/history inspection

This file sits between pure runtime helpers and pure UI modules:

- it still coordinates logs, redraws, and modal behavior
- but it no longer needs to sit inline in `crypsa_teaching_prototype.py`

Reading tip:

- if a UI-facing action is more than a one-line wrapper but still clearly controller-side, check here before assuming it belongs back in the main controller

### `canonical_replay.py`

This is the extracted replay-derived canonical-state helper layer.

It owns:

- rebuilding visible canonical state from accepted canonical history
- checking tile occupancy in replay-derived state
- finding canonical objects on tiles
- finding the first open canonical tile for server-side placement

This module is still intentionally small. It is not a full runtime substrate; it is the next step toward keeping replay-derived state logic out of the main controller.

Reading tip:

- if you are asking "what does accepted canonical history become?", start here
- if you are asking "who decided to accept or reject the event first?", start in `validation.py` or the controller

### `request_dispatch.py`

This is the extracted request-routing layer.

It owns:

- matching typed UI-intent requests to controller mutation methods
- keeping request-type dispatch logic out of `crypsa_teaching_prototype.py`

This keeps the request boundary a little stricter:

- UI emits typed intent
- request dispatch routes that intent
- controller methods still own the mutations

### `runtime_persistence.py`

This is the extracted runtime-store persistence layer.

It owns:

- reading the current saved teaching-state schema into `RuntimeStore`
- serializing `RuntimeStore` back into that schema
- keeping schema-hydration details out of `crypsa_teaching_prototype.py`

This sits above `crypsa_state_io.py`:

- `runtime_persistence.py` knows the state schema
- `crypsa_state_io.py` only reads/writes JSON objects

### `canonical_apply.py`

This is the extracted accepted-canonical-event creation layer.

It owns:

- canonical object-id allocation
- canonical event-id allocation
- canonical event record creation
- branch-hint resolution for newly accepted events

This sits after validation and before replay. It is the "the candidate event is allowed, now create the accepted canonical record" step.

### `crypsa_lens_adapters.py`

This is the runtime-to-lens translation layer.

It owns:

- pane view models
- history/timeline view models
- action-modal view models
- request-bearing lens data for UI interactions

This file matters because it is the main "adapter" boundary between raw runtime state and the narrower data shapes each UI lens needs.

The intended handoff is:

- runtime/controller owns meaning
- this adapter layer shapes lens-specific data
- UI modules render the lens data
- UI modules emit typed requests back to the controller

This is a deliberate separation-of-concerns boundary, not just a formatting convenience:

- adapters keep UI lenses from reaching deeply into controller state
- adapters give each lens the narrowest useful data shape
- runtime meaning can evolve without forcing presentation code to mirror every internal detail

Helper-stage map:

- `build_canonical_pane_lens()` / `build_observer_pane_lens()`: main window pane translation
- `build_history_card_lenses()` / `build_timeline_modal_lens()`: canonical inspection translation
- `build_mint_action_modal_lens()` / `build_build_action_modal_lens()` / `build_candidate_queue_lens()`: action-modal translation

### `crypsa_action_requests.py`

This is the UI-intent request layer.

It contains the typed request objects that UI lenses emit back to the runtime controller instead of calling mutation methods directly.

This keeps intent handoff explicit:

- UI lens emits request
- runtime controller executes request
- runtime redraws lenses as needed

Reading tip:

- keep these requests small and user-intent-oriented
- if a UI surface needs a new mutation path, add a request here and route it through `request_dispatch.py`
- if a request starts carrying too much display or selection policy, that is usually a sign the adapter layer should own more translation work instead

### `crypsa_event_graph.py`

This is the event-substrate layer.

It owns:

- replay over accepted canonical events
- stable event ordering
- branch lookup helpers
- branch-row derivation for the timeline
- branch labels and event chains

This file matters because the prototype teaches that canonical state is replay-derived, not stored as the primary source of truth.

If the runtime file is "what the app does," this file is "how canonical history becomes state."

Helper-stage map:

- `all_event_ids_sorted()` / `all_events_sorted()`: stable accepted-event ordering
- `event_chain()`: replay lineage walk from a selected head event back to root
- `event_children()`: child index keyed by lineage parent
- `primary_descent_from()`: choose the earliest-child path used as the main displayed lineage row
- `build_branch_rows()`: derive human-facing branch rows for the timeline UI
- `replay_branch_state()`: reconstruct visible canonical state from accepted history

### `crypsa_state_io.py`

This is the persistence boundary.

It reads and writes `crypsa_teaching_prototype_state.json`.

It should stay small and boring. Its job is schema-safe file I/O, not game logic.

Helper-stage map:

- `load_runtime_state()`: read one JSON object and verify that the root is an object
- `save_runtime_state()`: serialize the already-normalized runtime state exactly as the app provides it

### `crypsa_teaching_theme.py`

This is the shared UI constants module.

It owns:

- color constants
- window size defaults
- the runtime state path
- the Mint editor launcher path

Keeping these values here prevents UI code from scattering magic numbers and file paths across multiple modules.

## Runtime State Groups

The app state in `crypsa_teaching_prototype.py` is easiest to understand in groups:

### Observer-local state

- `observer_local_x`
- `observer_local_y`
- `observer_facing`
- `observer_build_selection`
- `observer_auto_reconcile`
- `observer_identity`

These values describe what the observer is doing locally right now.

### Canonical-history state

- `events`
- `next_sequence`
- `selected_branch`
- `selected_canonical_event_id`

These values describe accepted canonical history and what part of that history the user is currently viewing.

### Candidate state

- `invariant_boundary_candidates`
- `next_object_id`

These values describe submissions that are not canonical yet, plus the identifier source for newly accepted objects.

### Teaching and inspection state

- `teaching_example_loaded`
- `server_log`
- `observer_log`
- `server_serial`
- `observer_serial`

These values are for learning and inspection, not for defining truth.

These state groups are also the easiest bridge into `Runtime_Schema.md`, because the saved schema mirrors them closely.

## Important CrypSA Ideas In This Package

### Observer-local vs canonical

Observer movement changes only the observer pane.

Build and destroy do not become canonical immediately. They become candidate events at the invariant boundary first.

### Reconciliation

Reconciliation is where candidate events are canonically validated and, if accepted, converted into canonical events.

### Replay-derived canonical state

The app does not treat the left pane as the primitive source of truth.

Instead:

- accepted canonical history is the substrate of truth
- replay produces canonical state
- selecting a different historical event changes what replay produces

### `lineage_parent` vs `causal_references`

The prototype keeps this distinction intentionally explicit:

- `lineage_parent` drives replay and visible lineage forks
- `causal_references` do not drive replay, but can still matter to invariant validation

The built-in `Beacon` teaching example exists to demonstrate that second point.

## Recommended Reading Order

1. `crypsa_teaching_prototype.py`
2. `runtime_store.py`
3. `runtime_models.py`
4. `runtime_actions.py`
5. `validation.py`
6. `reconciliation.py`
7. `canonical_replay.py`
8. `canonical_apply.py`
9. `app_shell.py`
10. `crypsa_lens_adapters.py`
11. `crypsa_action_requests.py`
12. `request_dispatch.py`
13. `runtime_persistence.py`
14. `crypsa_event_graph.py`
15. `crypsa_state_io.py`
16. `crypsa_teaching_theme.py`
17. `ui/REFERENCE.md`

That order goes from app meaning to replay rules to persistence and presentation.

If you only need one runtime concept, use this shortcut:

- replay question -> `crypsa_event_graph.py`
- mutation question -> `crypsa_teaching_prototype.py`
- state-ownership question -> `runtime_store.py`
- typed queue-model question -> `runtime_models.py`
- observer-side action helper question -> `runtime_actions.py`
- accept/reject rule question -> `validation.py`
- reconcile/server-mint flow question -> `reconciliation.py`
- replay-derived state question -> `canonical_replay.py`
- accepted-record creation question -> `canonical_apply.py`
- root/hotkey/modal-shell question -> `app_shell.py`
- UI data-shape question -> `crypsa_lens_adapters.py`
- button/click intent question -> `crypsa_action_requests.py`
- request-routing question -> `request_dispatch.py`
- runtime-state load/save question -> `runtime_persistence.py`
- scope-boundary question -> `../../Prototype_vs_Current_CrypSA_Model.md`

## Beginner Notes

- If a function name starts with `_`, it is meant to be internal to the app class or module.
- A "canonical event" here means an accepted history record.
- A "branch" means a viewed lineage through that event graph.
- Redraws happen often. That is normal for this simple Tk teaching app.
- The runtime is intentionally centralized in one app class because that is easier to teach than a heavily abstracted architecture.
- When a runtime method feels long, look for nearby helper functions first; several of the busiest flows were recently split into smaller named stages to make the file easier to follow.
- A good reading pattern for the runtime file is: top-level action first, helper stages second, low-level validation details last.
