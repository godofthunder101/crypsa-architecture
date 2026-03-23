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

---

## What This Prototype Demonstrates

This prototype is designed to demonstrate the core CrypSA model with minimal extra game logic.

It shows:

- observer-local simulation  
- invariant-boundary candidate events  
- canonical validation and reconciliation  
- accepted canonical event history  
- event-lineage branching  
- replay-derived canonical state  
- Mint-authored canonical object definitions  

It also demonstrates a key architectural separation:

- **truth** (canonical events, validation, replay)  
- **translation** (adapters shaping runtime data)  
- **interpretation** (lenses defining observer meaning)  
- **experience** (UI and local simulation)  

This separation is central to understanding CrypSA.

---

## CrypSA In Plain English

In this prototype:

- the right pane shows what the observer is doing locally  
- the left pane shows what the world officially knows  
- candidate events sit in between until canonical reconciliation  
- accepted canonical events become canonical history  
- canonical state is rebuilt by replaying that accepted canonical history  

This is the shortest useful mental model for reading the UI.

---

## Status

This is a **completed teaching prototype**, not a production runtime.

It is:

- complete for its intended purpose  
- stable and internally consistent  
- frozen except for bug fixes and documentation updates  

It should be treated as a finished teaching artifact, not as an evolving runtime implementation.

---

## What This Prototype Is Not

This project is intentionally narrow. It is:

- not a networking benchmark  
- not a concurrency or distributed-systems test  
- not a production anti-cheat implementation  
- not a full game  
- not a full production server architecture  

Its job is to teach the CrypSA model clearly, not to simulate every runtime constraint.

If you need the broader CrypSA architecture, spec, or deployment model, leave this prototype and read the main repository docs.

---

## Main Files

- `crypsa/crypsa_teaching_prototype.py`: main teaching prototype UI  
- `mint/mint_catalog_editor.py`: external Mint editor  
- `mint_catalog.json`: shared Mint catalog  
- `crypsa_teaching_prototype_state.json`: saved runtime state  

---

## Supporting Modules

- `crypsa/crypsa_event_graph.py`: event lineage and replay substrate  
- `crypsa/crypsa_lens_adapters.py`: runtime-to-UI translation layer  
- `crypsa/crypsa_action_requests.py`: typed UI intent objects  
- `crypsa/runtime_store.py`: grouped runtime state  
- `crypsa/runtime_models.py`: typed runtime models  
- `crypsa/runtime_actions.py`: observer-side action helpers  
- `crypsa/validation.py`: canonical invariant validation  
- `crypsa/reconciliation.py`: candidate reconciliation and acceptance flow  
- `crypsa/canonical_replay.py`: replay-derived canonical state  
- `crypsa/canonical_apply.py`: canonical event creation  
- `crypsa/app_shell.py`: UI shell and lifecycle  
- `crypsa/controller_ui_actions.py`: controller UI coordination  
- `crypsa/request_dispatch.py`: request routing  
- `crypsa/runtime_persistence.py`: save/load logic  
- `crypsa/teaching_example_loader.py`: fixture-backed scenario loader  

UI modules:

- `crypsa/ui/crypsa_render_ui.py`  
- `crypsa/ui/crypsa_history_ui.py`  
- `crypsa/ui/crypsa_action_ui.py`  
- `crypsa/ui/crypsa_teaching_ui.py`  

Mint modules:

- `mint/mint_models.py`  
- `mint/mint_lens_adapters.py`  
- `mint/mint_editor_ui.py`  
- `mint/mint_catalog_store.py`  

---

## Module Map (How to Read the Code)

The easiest architecture stack to keep in mind is:

1. runtime/controller  
2. replay/event graph  
3. adapters  
4. lenses and typed requests  
5. UI modules  
6. Mint modules  

The UI handoff pattern is:

1. runtime/controller owns meaning and mutation  
2. adapters translate raw state into lens-ready data  
3. UI renders that data  
4. UI emits typed requests  
5. runtime/controller executes the requests  

Adapters are intentional architectural scaffolding, not just UI helpers.

They exist to:

- keep lenses decoupled from runtime internals  
- shape data before presentation  
- preserve separation between runtime meaning and UI  

---

## Teaching Model

This prototype teaches:

- observer-local vs canonical state  
- candidate events at the invariant boundary  
- canonical validation and acceptance  
- replay-derived canonical state  
- event-lineage branching  
- Mint definitions freezing into canonical objects  

The timeline UI visualizes lineage for human understanding, but rows are not canonical truth.

The built-in scenario lives in:

- `fixtures/teaching_example.json`  
- loaded via `crypsa/teaching_example_loader.py`  

---

## What This Teaches vs What It Does Not

### Teaches

- observer vs canonical separation  
- candidate → validation → canonical flow  
- replay-based state reconstruction  
- lineage branching  
- Mint integration  

### Does Not Teach

- networking or distributed deployment  
- concurrency handling  
- large-scale performance  
- production server architecture  
- full gameplay systems  

---

## How To Read The Prototype

Use this mental model:

- `Observer Representation` = local simulation  
- `Candidates` = pending events  
- `Canonical Representation` = replay-derived state  
- `History` = canonical truth  
- `Timeline` = lineage visualization  

---

## Launch

Run the prototype:

```powershell
.\start-crypsa-teaching-prototype.cmd
````

Run the Mint editor:

```powershell
.\start-mint-editor.cmd
```

---

## Best First Path

1. Launch the prototype
2. Click `How To Read`
3. Click `Load Teaching Example`
4. Open `History`
5. Open `Timeline`
6. Queue a build
7. Reconcile
8. Compare observer vs canonical

---

## Summary

This teaching prototype provides a minimal, inspectable implementation of CrypSA.

It demonstrates how:

* canonical events define truth
* adapters translate data
* lenses interpret meaning
* observers experience and simulate the world

It is complete for its purpose and is not intended to evolve into a production runtime.
