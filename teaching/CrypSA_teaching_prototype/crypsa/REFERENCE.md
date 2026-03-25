# CrypSA Runtime Reference

## Purpose

This folder contains the runtime side of the CrypSA Teaching Prototype.

It answers one main question:

"How does observer-local intent become canonical event history, and how does that history become visible state?"

This runtime reference is descriptive, not authoritative.

It demonstrates how the teaching prototype behaves, but it does not define canonical CrypSA behavior.

Authoritative behavior is defined in:

* `../../../spec/`
* `../../../architecture/`

Use this document when you want the architecture explained in prose before reading the code.

If you want a guided tutorial for following the code across files, start with `Codebase_Walkthrough.md` in the project root first, then return here for package-level reference detail.

If you want the current artifact status and maintenance posture before diving into runtime details, read `../STATUS.md` in the project root.

If you want the quickest repeatable smoke test after changing runtime/UI behavior, use `Manual_Regression_Checklist.md` in the project root.

If you are lost while reading the runtime, come back to this file after each major source file. It is meant to be a map, not a one-time introduction.

If your question turns into "how would this work across a real deployed CrypSA runtime?", leave this package and read `../Prototype_vs_Current_CrypSA_Model.md`, then the newer `../../../architecture/` and `../../../spec/` material. This package teaches the runtime loop, not the full deployment shape.

---

## Folder Role

This runtime operates as a single-process teaching model.

It simulates both observer and server responsibilities within one application for clarity.

The `crypsa` package owns:

- app startup and orchestration  
- runtime state held in memory  
- candidate-event validation, acceptance, and replay  
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
2. canonical event history / replay (event graph)  
3. adapters  
4. lenses and typed requests  
5. UI modules  
6. Mint modules  

---

## What This Folder Is Not

This package is not:

- a real network authority  
- a distributed runtime  
- a production anti-cheat implementation  
- a concurrency or deployment testbed  

This runtime demonstrates the canonical validation loop, but it does not define canonical event history itself.

Its job is to teach the runtime model clearly inside one local teaching prototype.

It should now be read as a completed teaching artifact, not as an open-ended runtime architecture sandbox.

---

## Main Runtime Flow

The runtime follows this loop:

1. Load the Mint catalog.  
2. Load saved runtime state, if a state file exists.  
3. Draw the main two-pane window.  
4. Let the observer move locally or queue invariant-boundary candidate events.  
5. Validate and reconcile queued candidate events into canonical events, assigning `server_sequence` and appending to canonical event history.  
6. Replay accepted canonical event history to produce visible derived canonical state.  
7. Save runtime state when the app closes or resets.  

This is a teaching model of CrypSA's canonical validation loop, not a deployed network authority.

---

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
- canonical event history  
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

---

### `validation.py`

This is the invariant-rule evaluation layer.

It answers:

> does this candidate event satisfy invariants and validation rules?

---

### `reconciliation.py`

This is the canonical acceptance layer.

It:

- processes candidate events  
- coordinates validation + acceptance  
- routes accepted events into canonical event history  

---

### `canonical_replay.py`

This module answers:

> what does canonical event history become?

It reconstructs:

- derived canonical state  
- object placement  
- world structure  

---

### `crypsa_lens_adapters.py`

This is the translation boundary between runtime and UI.

It:

- converts runtime data into lens-ready structures  
- prevents UI from reaching into runtime internals  
- preserves separation between meaning and presentation  

---

## Runtime State Groups

### Observer-local state

Local simulation, prediction, and input state.

### Canonical-history state

Accepted canonical event history and current selection.

### Candidate state

Pending non-canonical events.

### Teaching/inspection state

Logs and debug state (non-authoritative).

---

## Important CrypSA Ideas In This Package

### Observer-local vs canonical

Local simulation is not authoritative.  
Canonical event history defines what is real.

---

### Reconciliation

Candidate events are:

- validated  
- accepted or rejected  
- appended to canonical event history if accepted  

---

### Replay-derived canonical state

State is not stored as truth.

Instead:

- canonical event history is authoritative  
- derived canonical state is produced via replay  

---

### Lineage vs causal references

- lineage → drives replay  
- causal references → influence validation  

---

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

---

## Beginner Notes

- `_` prefix = internal  
- canonical event = accepted event record  
- branch = lineage through canonical event history  
- redraws are frequent (normal for teaching UI)  
- runtime is centralized intentionally for clarity  
- read flow first, helpers second  

---

## One Sentence Summary

This runtime demonstrates how observer actions become validated canonical events and how canonical event history is replayed into derived canonical state, without defining authoritative CrypSA behavior.
