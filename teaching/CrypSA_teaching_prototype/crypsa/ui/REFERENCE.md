# CrypSA UI Reference

## Purpose

This folder contains the UI modules used by the CrypSA runtime.

These modules do not redefine the core model. They present it.

Use this document when you want to know which UI file is responsible for which part of the teaching experience.

If you want a guided tutorial for following the code across files, start with `Codebase_Walkthrough.md` in the project root first, then use this file as the UI-specific reference.

If you want the current artifact status and maintenance posture before reading UI internals, read `../../STATUS.md` in the project root.

If you are validating interactive changes after reading the code, use `Manual_Regression_Checklist.md` in the project root.

If you are lost in the UI layer, use this file to answer one question first:

> "Am I looking at layout, translated data, or controller intent?"

If your question becomes "what would the full CrypSA runtime or deployment architecture do here?", step out of the UI layer and read `../../Prototype_vs_Current_CrypSA_Model.md` before going into the core documentation (`../../../../architecture/` and `../../../../spec/`).

These UI files teach the model. They do not define the model.

---

## Folder Role

The `crypsa/ui` package owns:

- the main-window rendering layer
- history and timeline inspection dialogs
- build, candidate, and Mint action dialogs
- teaching and help dialogs

The orchestration still lives in `crypsa_teaching_prototype.py`.

These modules:

- render lens data
- emit typed requests
- do not own runtime meaning or canonical truth

---

## Architectural Position

UI modules sit strictly in the **experience layer**.

They operate after:

```text
Canonical Event History → Derived Canonical State → Adapters → Lenses → UI
````

They:

* consume lens data (already translated and interpreted)
* render observer-visible output
* emit typed intent back to the runtime

They must not:

* define canonical truth
* access raw runtime state deeply
* perform validation
* enforce invariants
* mutate canonical event history directly

---

## UI Handoff Model

The current UI follows a strict boundary:

1. runtime/controller builds lens data via `crypsa_lens_adapters.py`
2. UI modules render that lens data
3. UI emits typed requests
4. requests are routed via `request_dispatch.py`
5. controller executes mutations and triggers redraw

This separation is intentional.

It ensures:

* UI does not depend on internal runtime structure
* adapters control data shape
* lenses control meaning
* UI remains purely presentational

---

## Codebase Stack (UI Perspective)

1. runtime/controller
2. canonical event history / replay (event graph)
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

---

## What This Folder Is Not

This package is not:

* the source of canonical truth
* the place where replay rules are defined
* the place where canonical validation occurs

These modules present the system.

They do not define it.

They belong to a completed teaching artifact, not a production UI system.

---

## Module Map

### `crypsa_render_ui.py`

Main-window rendering layer.

Draws:

* pane shells
* canonical pane (derived canonical state)
* observer pane (local simulation state)
* shared grid
* bottom controls

Consumes:

* `CanonicalPaneLens`
* `ObserverPaneLens`
* `GridLens`

Important functions:

* `draw_scene()`
* `draw_pane_shell()`
* `draw_server_pane()`
* `draw_observer_pane()`
* `draw_grid()`

Key rule:

> This file renders state. It does not define it.

---

### `crypsa_history_ui.py`

Canonical inspection layer.

Provides:

* History modal
* Timeline modal
* Event inspection tools

Focus:

* canonical event history
* replay lineage
* branch visualization

Consumes:

* `HistoryCardLens`
* `TimelineModalLens`

Emits:

* selection requests

---

### `crypsa_action_ui.py`

Action modal layer.

Provides:

* server-side Mint modal (direct canonical events)
* observer Build modal (candidate events)
* candidate queue modal

Teaches:

* difference between canonical events and candidate events

Consumes:

* action lens data

Emits:

* typed action requests

---

### `crypsa_teaching_ui.py`

Teaching and explanation layer.

Provides:

* mental model explanations
* walkthrough
* hotkeys
* contextual help

Important:

> This file explains the model, not the implementation.

---

## UI Design Rules

All UI modules follow this separation:

| Responsibility | Location             |
| -------------- | -------------------- |
| Truth          | runtime + validation |
| Translation    | adapters             |
| Interpretation | lenses               |
| Experience     | UI                   |

UI modules:

* render only
* do not compute meaning
* do not perform validation

---

## Debug Path (Very Important)

When something is wrong:

1. Wrong behavior → controller
2. Wrong data shape → adapters
3. Wrong meaning → lenses
4. Wrong layout → UI
5. Wrong click result → requests → dispatch → controller

---

## Main Window Anatomy

### Canonical Pane

Shows:

* derived canonical state
* canonical event history context
* branch and event selection

---

### Observer Pane

Shows:

* local simulation state
* prediction
* pending candidate events

---

## Modal Strategy

Heavy information is moved into modals:

* history
* timeline
* candidate queue
* teaching content

This keeps the main UI focused and readable.

---

## Key Insight

> The UI shows both:
>
> * predicted local state
> * canonical reconstructed state

This dual view is essential to understanding CrypSA.

---

## Beginner Notes

* `open_*_modal()` creates dialogs
* always ask: *what lens built this?*
* UI should never reach deep into runtime state
* if UI logic grows → it belongs in adapters or lenses instead
* if UI text changes meaning → update docs too

---

## One Sentence Summary

The CrypSA UI renders lens-interpreted data derived from canonical event history and local simulation, while emitting typed requests back to the runtime without defining truth or validation.
