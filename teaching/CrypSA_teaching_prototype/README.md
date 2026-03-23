# Minimal CrypSA Teaching Prototype

## Purpose

This folder contains the minimal CrypSA teaching prototype.

If you want the fastest guided entrypoint into the project, start with `start_here.md`.

If you want the current artifact status and intended maintenance policy, read `STATUS.md`.

If you want the implementation-facing architecture anchor, start with:

- `implementation/CrypSA_Teaching_Prototype_Layers.md`
- `implementation/CrypSA_Data_Flow_Diagram.md`
- `implementation/CrypSA_Module_Map.md`
- `implementation/CrypSA_Refactor_Guardrails.md`

It is designed to demonstrate the core CrypSA model with as little extra game logic as possible:

- observer-local movement
- invariant-boundary candidate events
- canonical validation and reconciliation
- accepted canonical event history
- event-lineage branching
- replay-derived canonical state
- Mint-authored canonical object definitions

This is a completed teaching prototype, not a production runtime.

## CrypSA In Plain English

In this prototype:

- the right pane shows what the observer is doing locally
- the left pane shows what the world officially knows
- candidate events sit in between until canonical reconciliation
- accepted canonical events become canonical history
- canonical state is rebuilt by replaying that accepted canonical history

This is the shortest useful mental model for reading the UI.

This repository should now be read as a completed teaching artifact, not as an unfinished runtime path.

## What This Prototype Is Not

This project is intentionally narrow. It is:

- not a networking benchmark
- not a concurrency or distributed-systems test
- not a production anti-cheat implementation
- not a full game
- not a full production server architecture

Its job is to teach the CrypSA model clearly, not to simulate every runtime constraint.

If you need the broader CrypSA architecture, spec, or deployment model, leave this prototype and read the newer `repo/` folder. The prototype is the teaching front door, not the full runtime reference.

## Main Files

- `crypsa/crypsa_teaching_prototype.py`: the main teaching prototype UI
- `mint/mint_catalog_editor.py`: the external Mint editor
- `mint_catalog.json`: the shared Mint catalog
- `crypsa_teaching_prototype_state.json`: the saved runtime state for the prototype

## Supporting Modules

- `crypsa/crypsa_event_graph.py`: event replay and event-lineage derivation
- `crypsa/crypsa_lens_adapters.py`: runtime-to-UI translation layer for pane, history, timeline, and action-modal data
- `crypsa/crypsa_action_requests.py`: typed UI-intent handoff objects executed by the runtime controller
- `crypsa/runtime_store.py`: grouped in-memory runtime state for observer, canonical history, and inspection logs
- `crypsa/runtime_models.py`: typed runtime models for candidate events, accepted canonical events, and replay-derived canonical objects/state
- `crypsa/runtime_actions.py`: extracted observer-side action helpers such as target-tile calculation, candidate creation, and recentering
- `crypsa/validation.py`: canonical invariant-rule evaluation extracted from the controller
- `crypsa/reconciliation.py`: candidate reconciliation and server-mint acceptance flow extracted from the controller
- `crypsa/canonical_replay.py`: replay-derived canonical state helpers extracted from the controller
- `crypsa/canonical_apply.py`: canonical event creation and object-id allocation extracted from the controller
- `crypsa/app_shell.py`: Tk root, modal-shell, widget-lifecycle, and hotkey plumbing extracted from the controller
- `crypsa/controller_ui_actions.py`: controller-side UI coordination helpers such as catalog reload, Beacon-path prep, Mint editor launch, and observer recentering
- `crypsa/request_dispatch.py`: typed request routing extracted from the controller
- `crypsa/runtime_persistence.py`: runtime-store load/save coordination extracted from the controller
- `crypsa/teaching_example_loader.py`: fixture-backed loader for the built-in teaching scenario
- `crypsa/ui/crypsa_history_ui.py`: canonical history and timeline UI
- `crypsa/ui/crypsa_teaching_ui.py`: `How To Read`, `Walkthrough`, and model-note teaching dialogs
- `crypsa/ui/crypsa_action_ui.py`: Mint/build/candidate modal UI
- `crypsa/ui/crypsa_render_ui.py`: main window rendering, pane layout, and shared grid drawing
- `crypsa/crypsa_state_io.py`: low-level JSON I/O beneath the runtime persistence layer
- `crypsa/crypsa_teaching_theme.py`: shared UI constants and local paths
- `mint/mint_catalog_store.py`: Mint catalog validation and normalization
- `mint/mint_models.py`: typed shared Mint/runtime-definition structures used across the editor, store, and frozen-definition handoff
- `mint/mint_editor_ui.py`: Mint editor modal and field UI helpers
- `mint/mint_lens_adapters.py`: Mint detail-pane and modal starter-data translation layer

## Module Map

If you are reading the code for the first time, this is the intended order:

1. `crypsa/crypsa_teaching_prototype.py`
   This is the orchestration layer. It owns app-level meaning, redraw timing, modal entry points, and coordination across the extracted runtime boundaries.
2. `crypsa/runtime_store.py`
   This is the grouped runtime-state layer. It shows the main mutable state groups before you follow mutations.
3. `crypsa/runtime_models.py`
   This is the typed runtime-vocabulary layer. It gives names to candidate events, accepted canonical events, replay-derived objects, and accepted payloads.
4. `crypsa/runtime_actions.py`
   This is the observer-side helper layer. It covers target-tile calculation, typed candidate creation, and observer recentering helpers.
5. `crypsa/validation.py`
   This is the canonical validation layer. It answers whether a candidate event can cross the invariant boundary.
6. `crypsa/reconciliation.py`
   This is the candidate-acceptance layer. It runs build, destroy, and server-mint flows through validation and accepted-record creation.
7. `crypsa/canonical_apply.py`
   This is the accepted-record creation layer. It allocates ids and creates accepted canonical event records.
8. `crypsa/canonical_replay.py`
   This is the replay-derived canonical-state layer. It turns accepted canonical history back into visible canonical state helpers.
9. `crypsa/app_shell.py`
   This is the app-shell layer. It keeps Tk root creation, hotkey plumbing, modal shell behavior, and widget cleanup separate from controller logic.
10. `crypsa/crypsa_lens_adapters.py`
   This is the runtime-to-lens adapter layer. It translates raw runtime/catalog state into narrow pane, history, timeline, and action-modal data shapes.
11. `crypsa/controller_ui_actions.py`
   This is the controller-side UI coordination layer. It keeps small redraw/modal/catalog helpers out of the main orchestration file.
12. `crypsa/crypsa_action_requests.py`
   This is the typed request layer. It defines the small intent objects that UI lenses hand back to the runtime controller.
13. `crypsa/request_dispatch.py`
   This is the request-routing layer. It keeps typed UI intent dispatch separate from the controller's mutation methods.
14. `crypsa/runtime_persistence.py`
   This is the runtime persistence layer. It hydrates and serializes the grouped runtime store using the current teaching-state schema.
15. `crypsa/crypsa_event_graph.py`
   This is the CrypSA event substrate layer. It handles replay, event ordering, branch-row derivation, and branch labels.
15. `crypsa/ui/crypsa_render_ui.py`
   This is the main window drawing layer. It renders the observer pane, canonical pane, grid, and shared main-window buttons.
16. `crypsa/ui/crypsa_history_ui.py`
   This is the canonical inspection layer. It renders history and timeline views over the canonical event graph.
17. `crypsa/ui/crypsa_action_ui.py`
   This is the action-modal layer. It renders Mint, Build, and invariant-boundary candidate dialogs.
18. `crypsa/ui/crypsa_teaching_ui.py`
   This is the teaching copy layer. It renders explanatory dialogs like `How To Read`, `Walkthrough`, and `Model Notes`.
19. `crypsa/crypsa_state_io.py`
   This is the low-level JSON I/O boundary. It reads and writes the current runtime state schema on disk.
20. `mint/mint_catalog_editor.py`
   This is the Mint editor orchestration layer. It owns catalog state, the list/detail view, save behavior, and tag mutation.
21. `mint/mint_models.py`
   This is the typed Mint vocabulary layer. It gives names to genomes, invariant rules, entity metadata, and the frozen definitions attached to accepted canonical objects.
22. `mint/mint_lens_adapters.py`
   This is the Mint translation layer. It shapes the right-hand detail pane data and the create/edit modal starter values.
23. `mint/mint_editor_ui.py`
   This is the Mint editor modal layer. It renders the Mint-kind authoring popup, tag-manager popup, and shared field helpers.
24. `mint/mint_catalog_store.py`
   This is the Mint schema boundary. It validates, normalizes, loads, and saves the Mint catalog that future canonical objects are frozen from.

This split is intentional: runtime behavior, event logic, rendering, modal UI, teaching text, and Mint authoring are separated so the prototype is easier to teach and maintain.

The easiest architecture stack to keep in mind is:

1. runtime/controller
2. replay/event graph
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

The current UI handoff pattern is:

1. runtime/controller owns meaning and mutation
2. adapter modules translate raw state into lens-specific data
3. UI modules render that lens data
4. UI modules emit typed requests
5. runtime/controller executes the requests and redraws

The adapter layer is intentional architectural scaffolding, not just a UI-helper convenience.

Adapters are used to:

- keep individual lenses from coupling too tightly to runtime internals
- shape runtime data into narrow lens/UI-facing forms before presentation code sees it
- preserve the separation between runtime meaning and presentation logic

That matters because this prototype is not only teaching CrypSA concepts. It is also testing a real architectural idea:

- runtime meaning should stay readable on its own
- UI lenses should consume translated data instead of reaching deeply into controller state
- presentation changes should not require rewriting core runtime behavior

A good reading pattern across the repo is:

1. read the top-level flow first
2. identify the helper stages it calls
3. only then drop into the lower-level validation or rendering details

The walkthrough and package reference docs now call out those helper-stage maps explicitly.

Fast debugging shortcut:

- event accepted/rejected unexpectedly -> `validation.py`, then `reconciliation.py`
- replay-derived state looks wrong -> `canonical_replay.py`, then `crypsa_event_graph.py`
- button renders but does the wrong thing -> `crypsa_action_requests.py`, then `request_dispatch.py`
- small modal/catalog/recenter UI helper question -> `controller_ui_actions.py`
- modal/hotkey/window behavior is wrong -> `app_shell.py`
- saved state loads or saves incorrectly -> `runtime_persistence.py`, then `crypsa_state_io.py`
- Mint schema or save behavior is wrong -> `mint/mint_catalog_store.py`

If you are using the docs as a reading guide, the cleanest progression is:

1. `README.md` for scope and file map
2. `codebase_walkthrough.md` for end-to-end flows
3. `prototype_vs_current_crypsa_model.md` for the prototype-vs-full-model boundary
4. package `REFERENCE.md` files for module-level helper-stage maps
5. `manual_regression_checklist.md` if you changed interactive behavior and need a repeatable smoke test

If you are still unsure where to start, use this fallback:

1. read `CrypSA In Plain English`
2. read `Best First Path`
3. open `codebase_walkthrough.md`
4. only then open individual source files

If you changed code and want the fastest confidence check:

1. run `python -m unittest`
2. use `manual_regression_checklist.md` for Tk/manual flows

## Launch

Run the prototype with:

```powershell
.\start-crypsa-teaching-prototype.cmd
```

Run the Mint editor with:

```powershell
.\start-mint-editor.cmd
```

## Best First Path

If you are opening the prototype for the first time, use this order:

1. Launch the prototype.
2. Click `How To Read`.
3. Click `Load Teaching Example`.
4. Open `History`.
5. Open `Timeline`.
6. Queue a build from the observer side.
7. Reconcile the candidate.
8. Return to `History` and compare the accepted event history against the observer view.

This path shows the core teaching loop with minimal setup.

## Teaching Model

The prototype teaches these CrypSA ideas directly:

- the observer has a local view and local movement
- canonical truth lives in accepted canonical history
- build and destroy actions first become candidate events at the invariant boundary
- reconciling from older canonical history creates a new event lineage
- canonical state is reconstructed by replaying accepted canonical history
- canonical objects keep frozen Mint definitions after acceptance
- if a Mint catalog reload removes a kind that is still used by queued or accepted objects, the teaching world resets to baseline instead of attempting a migration

The timeline UI is a visualization of event lineage. Its rows help humans inspect forks, but the rows themselves are not canonical truth.

This minimal prototype also makes one teaching simplification explicit:

- `lineage_parent` drives replay and visible event-lineage forks
- `causal_references` do not drive replay, but they can now participate in invariant validation rules for contextual checks

The built-in teaching scenario is also no longer hard-coded inline in the controller. Its content now lives in `fixtures/teaching_example.json` and is loaded through `crypsa/teaching_example_loader.py`.

## What This Teaches vs What It Does Not

This prototype is meant to answer:

- what the CrypSA observer/local vs canonical split looks like
- what happens when candidate events wait at the invariant boundary
- how accepted canonical history becomes replay-derived state
- how reconciling from historical selection can fork event lineage
- how Mint definitions freeze into accepted canonical objects

It is not meant to answer:

- how a real networked authority would be deployed
- how concurrency, latency, or hostile clients would be handled in production
- how a distributed or independent server architecture would scale
- how a full game would layer richer mechanics onto the model

## How To Read The Prototype

Use the app with this mental model:

- `Observer Representation` shows observer-local state
- `Candidates` shows candidate events waiting for canonical validation
- `Canonical Representation` shows replay-derived canonical state
- `History` shows accepted canonical events, which are the real substrate of truth
- `Timeline` shows event-lineage visualization for forks and historical selection

The app also includes a `How To Read` button in the canonical pane for first-time users.

That modal also includes `Load Teaching Example`, which seeds a small canonical history with a fork so users can inspect event lineage immediately, and `Reset To Fresh Install`, which returns the prototype to an empty baseline.

There is also a `Walkthrough` button in the canonical pane that gives a short guided reading order for the prototype.

The built-in `Beacon` Mint kind is the concrete example of contextual validation through `causal_references`.

## Glossary

- `Observer Representation`: the observer-local view and movement state
- `Canonical Representation`: the replay-derived state built from accepted canonical events
- `Candidate Event`: an observer-side submission waiting for canonical validation at the invariant boundary
- `Invariant Boundary`: the point where local intent must be validated before becoming canonical
- `Event Lineage`: the replay-driving chain formed through `lineage_parent`
- `Mint`: the authored definition that future accepted canonical objects freeze from

## Guides

- `codebase_walkthrough.md`: tutorial-style guide for following the architecture and main code paths
- `prototype_vs_current_crypsa_model.md`: crosswalk between this teaching prototype and the newer `repo/` CrypSA model
- `runtime_schema.md`: explains the saved runtime state
- `mint_editor_usage.md`: explains how to use the Mint editor
- `manual_regression_checklist.md`: repeatable manual validation steps for the interactive Tk flows
- `crypsa/REFERENCE.md`: explains the runtime package in prose
- `crypsa/ui/REFERENCE.md`: explains the UI package and dialog split
- `mint/REFERENCE.md`: explains the Mint editor, schema, and save flow

## Notes

- This prototype is intentionally minimal and teaching-oriented.
- It uses CrypSA terminology in both code and UI wherever practical.
- It is not intended to be a full game or full production server.
- Many of the larger files now read best as staged flows with nearby helper functions, rather than as one long linear implementation.
- The adapter/request split is now central enough that UI debugging usually goes: runtime meaning -> lens builder -> UI renderer -> request type -> request dispatch -> controller mutation.
- If a file feels confusing, do not keep drilling downward immediately; return to the walkthrough or the relevant `REFERENCE.md` first and re-enter with one specific flow in mind.
