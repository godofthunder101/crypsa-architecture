# Minimal CrypSA Teaching Prototype

## Purpose

This folder contains the minimal CrypSA teaching prototype.

This folder is authoritative for the teaching system itself, but it does not define the full CrypSA runtime architecture.

For the authoritative adapter and observer-model docs, see:

- `../../architecture/CrypSA_Adaptor_Model.md`
- `../../architecture/CrypSA_Client_Observer_Model.md`

If you want the fastest guided entrypoint into the project, start with `Start_Here.md`.

If you want the authoritative artifact status and intended maintenance policy, read `STATUS.md`.

If you want the implementation-facing architecture anchor, start with:

- `implementation/CrypSA_Teaching_Prototype_Layers.md`
- `implementation/CrypSA_Data_Flow_Diagram.md`
- `implementation/CrypSA_Module_Map.md`
- `implementation/CrypSA_Refactor_Guardrails.md`

---

## ⚠️ Important Scope Note

This prototype includes concepts (such as event lineage visualization and branching-style timelines) that are useful for teaching but are **not part of the CrypSA v0.1 runtime model**.

In v0.1:

* canonical event history is append-only  
* ordering is defined by `server_sequence`  
* branching is not part of the runtime model  

---

## What This Prototype Demonstrates

This prototype is designed to demonstrate the core CrypSA model with minimal extra game logic.

It shows:

- observer-local simulation  
- invariant-boundary candidate events  
- canonical validation and observer reconciliation  
- accepted canonical event history  
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
- candidate events sit in between until observer reconciliation  
- accepted canonical events become canonical event history  
- derived canonical state is rebuilt by replaying that canonical event history  

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

- `crypsa/crypsa_event_graph.py`: event lineage and replay substrate (prototype-specific)  
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

---

## Teaching Model

This prototype teaches:

- observer-local vs canonical state  
- candidate events at the invariant boundary  
- canonical validation and acceptance  
- replay-derived canonical state  
- Mint definitions freezing into canonical objects  

The timeline UI visualizes lineage for human understanding, but this visualization is **not part of the CrypSA v0.1 runtime model**.

---

## Summary

This teaching prototype provides a minimal, inspectable implementation of CrypSA.

It demonstrates how:

* canonical event history defines truth  
* adapters translate data  
* lenses interpret meaning  
* observers experience and simulate the world  

It is complete for its purpose and is not intended to evolve into a production runtime.
