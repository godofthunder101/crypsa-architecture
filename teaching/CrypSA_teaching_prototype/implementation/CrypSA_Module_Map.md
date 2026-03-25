> Scope note: This document reflects the teaching prototype implementation at the time it was completed.
>
> It may not match the current CrypSA specification.
>
> The prototype is preserved as a teaching artifact and is not updated to reflect ongoing architectural changes.
>
> For current system behavior, refer to `../../../spec/`.

# CrypSA Teaching Prototype — Module Map

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

---

## Purpose

This document maps the main modules of the CrypSA teaching prototype to the architectural layers they belong to.

It is intended to answer:

> Which file is responsible for what?

It is a practical companion to:

- `CrypSA_Teaching_Prototype_Layers.md`
- `CrypSA_Data_Flow_Diagram.md`
- `CrypSA_Refactor_Guardrails.md`

If you want the current status and maintenance posture before reading the layer map, start with `STATUS.md`.

---

## Layer 1 — Runtime / Controller

These modules coordinate runtime behavior and application flow.

- `crypsa/crypsa_teaching_prototype.py`  
  Main orchestration layer.

- `crypsa/app_shell.py`  
  App lifecycle and window shell.

- `crypsa/controller_ui_actions.py`  
  UI-triggered controller coordination helpers.

---

## Layer 2 — Runtime State and Actions

- `crypsa/runtime_store.py`  
  In-memory runtime state.

- `crypsa/runtime_models.py`  
  Typed runtime records.

- `crypsa/runtime_actions.py`  
  Observer-side action helpers.

- `crypsa/request_dispatch.py`  
  Routes typed requests into controller mutation paths.

- `crypsa/crypsa_action_requests.py`  
  Typed request definitions representing observer intent.

---

## Layer 3 — Validation / Apply / Reconciliation

These modules define how candidate events become canonical events.

- `crypsa/validation.py`  
  Candidate-event validation (invariants, rules, identity, preconditions).

- `crypsa/canonical_apply.py`  
  Creation of accepted canonical event records and assignment of `server_sequence`.

- `crypsa/reconciliation.py`  
  Coordinates validation, acceptance, and canonical application.

---

## Layer 4 — Replay / Event Graph

These modules define how canonical event history becomes derived canonical state.

- `crypsa/canonical_replay.py`  
  Replay boundary for reconstructing derived canonical state.

- `crypsa/crypsa_event_graph.py`  
  Event lineage, ordering, and history structure.

---

## Layer 5 — Persistence / Fixtures

- `crypsa/runtime_persistence.py`  
  Runtime save/load coordination.

- `crypsa/crypsa_state_io.py`  
  Low-level JSON persistence boundary.

- `crypsa/teaching_example_loader.py`  
  Fixture loading for teaching scenarios.

- `fixtures/teaching_example.json`  
  Seeded example canonical event history.

---

## Layer 6 — Adapter Layer (Translation)

- `crypsa/crypsa_lens_adapters.py`  
  Runtime-side adapters.

- `mint/mint_lens_adapters.py`  
  Mint-side adapters.

Adapters:

- shape canonical and observer data  
- prepare lens-ready structures  
- aggregate inputs  

Adapters must not:

- mutate canonical event history  
- perform validation  
- define interpretation  

---

## Layer 7 — UI Layer (Experience)

- `crypsa/ui/crypsa_render_ui.py`
- `crypsa/ui/crypsa_history_ui.py`
- `crypsa/ui/crypsa_action_ui.py`
- `crypsa/ui/crypsa_teaching_ui.py`
- `mint/mint_editor_ui.py`

The UI layer:

- consumes lens data  
- renders observer experience  
- emits typed requests  

It does not:

- define canonical truth  
- perform validation  
- access raw runtime state deeply  

---

## Layer 8 — Mint Layer (Structural Definition)

- `mint/mint_models.py`  
  Typed Mint-side structures.

- `mint/mint_catalog_editor.py`  
  Mint editor orchestration.

- `mint/mint_catalog_store.py`  
  Mint normalization, validation, and persistence.

Mint defines:

- object structure (genomes)  
- invariant schemas  
- allowed transitions  

Mint does not:

- define canonical event history  
- affect past canonical events  
- perform runtime validation  

---

## Layer 9 — Tests

The test suite protects the architecture with focused non-UI tests, including:

- runtime models  
- canonical replay  
- canonical apply  
- validation  
- reconciliation  
- runtime persistence  
- request dispatch  
- runtime actions  
- teaching example loading  
- timeline lens behavior  
- app shell behavior  
- controller UI actions  
- Mint normalization  
- adapter output contracts  

---

## Current Architectural Pressure Point

`crypsa/crypsa_teaching_prototype.py` remains the central orchestration layer.

This is no longer an architectural risk, but it is still:

> the primary concentration of coordination responsibility

---

## Key Insight

> Each layer has a single responsibility:
>
> - runtime controls flow  
> - validation controls acceptance  
> - canonical event history defines what happened  
> - replay defines what exists  
> - adapters shape data  
> - lenses interpret meaning  
> - UI presents experience  
> - Mint defines structure  

---

## One Sentence Summary

The CrypSA teaching prototype is organized into distinct layers for runtime orchestration, validation, canonical event history, replay, adapters, UI, Mint authoring, and testing, with each module serving a clearly separated architectural responsibility.
