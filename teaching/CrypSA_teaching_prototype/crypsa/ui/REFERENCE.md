# CrypSA UI Reference

## Purpose

This folder contains the UI modules used by the CrypSA runtime.

These modules do not redefine the core model. They present it.

Use this document when you want to know which UI file is responsible for which part of the teaching experience.

If you want a guided tutorial for following the code across files, start with `codebase_walkthrough.md` in the project root first, then use this file as the UI-specific reference.

If you want the current artifact status and maintenance posture before reading UI internals, read `../STATUS.md` in the project root.

If you are validating interactive changes after reading the code, use `manual_regression_checklist.md` in the project root.

If you are lost in the UI layer, use this file to answer one question first: "am I looking at layout, translated data, or controller intent?"

If your question becomes "what would the full CrypSA runtime or deployment architecture do here?", step out of the UI layer and read `../prototype_vs_current_crypsa_model.md` before going into `../repo/`. These UI files teach the model; they do not try to mirror the full architecture.

## Folder Role

The `crypsa/ui` package owns:

- the main-window drawing layer
- history and timeline inspection dialogs
- build, candidate, and Mint action dialogs
- teaching and help dialogs

The orchestration still lives in `crypsa_teaching_prototype.py`. These modules are helpers that render one part of the interface each.

In the current architecture, most of these modules now sit behind a clearer handoff:

- runtime/controller builds lens data in `crypsa_lens_adapters.py`
- UI module renders that lens data
- UI module emits typed requests back to the controller when interaction happens

That handoff is deliberate architectural scaffolding, not just UI convenience code.

It exists to:

- keep each pane or modal lens from coupling too tightly to raw runtime state
- make the UI consume translated presentation-facing data instead of controller internals
- preserve a cleaner split between presentation logic here and runtime meaning elsewhere

The easiest codebase stack to keep in mind from the UI side is:

1. runtime/controller
2. replay/event graph
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

When you are reading one interactive path, the cleanest order is:

1. find the runtime entrypoint that opens the pane or modal
2. find the matching lens builder in `crypsa_lens_adapters.py`
3. read the UI renderer here
4. follow the emitted request type into `crypsa_action_requests.py`
5. follow request routing through `request_dispatch.py`, then the controller mutation method

## What This Folder Is Not

This package is not:

- the source of runtime truth
- the place where replay rules are defined
- the place where canonical acceptance rules live

These modules present the model. They do not define the model.

They also belong to a completed teaching artifact, not a future production UI path.

## Module Map

### `crypsa_render_ui.py`

This is the main-window rendering layer.

It draws:

- the background and pane shells
- the canonical pane
- the observer pane
- the shared grid
- bottom-row main-window buttons

It does not own the meaning of observer movement or reconciliation. It paints pane/grid lens data prepared by the runtime adapter layer.

Important functions:

- `draw_scene()`: redraws the full main window
- `draw_pane_shell()`: paints the shared visual frame for a pane
- `draw_server_pane()`: renders canonical state summary and canonical controls
- `draw_observer_pane()`: renders observer-local summary and observer controls
- `draw_grid()`: renders the tile map used by both panes

Recent readability note:

- the pane module now consumes pane/grid lens data instead of pulling as much state directly from the runtime object
- if you are tracing the main window, read the top-level pane function first, then the matching builder in `crypsa_lens_adapters.py`, then the small local helpers here

Helper-stage map:

- `_draw_summary_rows()`: shared two-column summary renderer used by both panes
- `_draw_canonical_banner()`: top-right teaching-state banner in the canonical pane
- `draw_server_pane()` / `draw_observer_pane()`: main pane render entrypoints that consume `CanonicalPaneLens` and `ObserverPaneLens`
- `draw_grid()`: shared grid renderer that consumes `GridLens`

### `crypsa_history_ui.py`

This is the canonical inspection layer.

It contains:

- the History modal
- the Timeline modal
- history-card rendering
- timeline inspector rendering
- event selection helpers

This file matters because the prototype teaches that history is the substrate of truth. If you want to inspect accepted events directly, start here.

Recent readability note:

- the modal now consumes history/timeline lens data and emits selection requests back to the controller
- branch matching, preferred-branch selection, and most event-graph translation now live primarily in `crypsa_lens_adapters.py`
- that leaves this file focused on modal layout, node-click wiring, and inspector rendering

Helper-stage map:

- `open_history_modal()`: render history cards from `HistoryCardLens`
- `open_timeline_modal()`: render timeline rows from `TimelineModalLens`
- `select_history_event()`: apply the adapter-chosen history selection back into runtime state
- `_render_timeline_inspector()`: right-hand event detail panel in the timeline modal

### `crypsa_action_ui.py`

This is the action-modal layer.

It contains:

- the server Mint modal
- the observer Build modal
- the invariant-boundary Candidates modal

This is where users see the difference between direct canonical minting and queued observer-side submission.

Recent readability note:

- the action modals are easier to read if you treat them by teaching purpose rather than by widget detail
- the file separates "server-side direct mint", "observer-side candidate-event submission", and "candidate inspection" into distinct modal entrypoints
- the modal buttons now emit typed action requests instead of calling runtime mutation methods directly
- the modal bodies now render lens data from `crypsa_lens_adapters.py` rather than assembling option/card/queue summaries inline

Helper-stage map:

- `open_mint_modal()`: direct canonical minting flow used from the canonical pane
- `open_build_modal()`: observer-side build submission flow, including the Beacon teaching prompt
- `open_candidate_modal()`: inspection and management view for queued invariant-boundary candidates

### `crypsa_teaching_ui.py`

This is the teaching-copy layer.

It contains:

- `How To Read`
- `Walkthrough`
- `Model Notes`
- `Hotkeys`
- pane-specific help popups

If the rest of the UI shows behavior, this file explains behavior in plain language.

Recent readability note:

- the teaching module is now easiest to read as three layers: broad mental model, procedural walkthrough, and targeted quick-help popups
- that keeps longer teaching copy out of the main layout while still leaving short pane help nearby

Helper-stage map:

- `open_teaching_modal()`: broad "what is this model?" entrypoint
- `open_walkthrough_modal()`: step-by-step reading order for exploring the prototype
- `open_model_notes_modal()`: shorter conceptual summary after the walkthrough
- `open_hotkeys_modal()`: keyboard-only reference
- `open_pane_help_modal()`: quick glossary-style clarification for one pane at a time

## UI Design Rules In This Folder

These modules follow a simple split:

- runtime meaning stays in the app
- translation into lens-specific data stays in `crypsa_lens_adapters.py`
- pane/modal rendering stays in the UI helpers
- UI-originated intent returns through typed requests
- teaching explanations stay in the teaching UI module

That separation makes the prototype easier to maintain because:

- layout changes do not need event-logic edits
- teaching-copy edits do not need replay-logic edits
- new dialogs can be added without growing the main runtime file too quickly
- lenses can stay narrower because adapters shape the data before it reaches widget code

It also gives you a clearer debug path:

1. if the meaning is wrong, start in the runtime controller
2. if the data shape is wrong, inspect the matching lens builder
3. if the layout is wrong, inspect the UI module
4. if a click does the wrong thing, inspect the request type and `request_dispatch.py`

Reading shortcut:

- layout problem -> stay in `crypsa/ui`
- wrong text or wrong summary values -> inspect `crypsa_lens_adapters.py`
- wrong behavior after a click -> inspect `crypsa_action_requests.py`, then `request_dispatch.py`, then the controller

## Main Window Anatomy

The main window has two panes:

### Canonical pane

This pane shows replay-derived official state.

It includes:

- branch and selected-event summary
- canonical object grid
- history and timeline controls
- Mint and teaching/help controls

### Observer pane

This pane shows local observer state.

It includes:

- local position and facing
- target tile
- current build kind
- pending canonical-event count
- observer-side grid
- auto-submit toggle
- build, destroy, reconcile, and candidate controls

## Modal Strategy

Most explanatory or detail-heavy content lives in modals instead of the main window.

That is intentional. The main panes stay focused on comparison, while:

- detailed teaching copy
- event history inspection
- timeline inspection
- build lists
- candidate lists

can use their own space without overloading the main layout.

## Beginner Notes

- `open_*_modal()` functions create and populate dialogs.
- Most UI helpers still accept `app`, but the important data should usually arrive through a lens object rather than fresh deep runtime lookups.
- If a UI file feels too magical, stop and ask: "what lens built this view?" before reading more widget code.
- If a UI string changes the meaning of the model, the matching top-level docs should usually be updated too.
- If a pane label mentions a concept that is not obvious, the matching explanation should live in `crypsa_teaching_ui.py`.
- In the larger UI modules, prefer reading the high-level `draw_*` or `open_*_modal` function first, then the nearby helper functions that prepare text, labels, or inspector content.
- In `crypsa_teaching_ui.py`, read the broadest teaching modal first, then the narrower walkthrough or pane-help popups second.
