# CrypSA Teaching Prototype - Module Map

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

## Purpose

This document maps the main modules of the CrypSA teaching prototype to the architectural layers they belong to.

It is intended to answer:

Which file is responsible for what?

It is a practical companion to:

- `CrypSA_Teaching_Prototype_Layers.md`
- `CrypSA_Data_Flow_Diagram.md`
- `CrypSA_Refactor_Guardrails.md`

If you want the current status and maintenance posture before reading the layer map, start with `STATUS.md`.

## Layer 1 - Runtime / Controller

These modules coordinate runtime behavior and application flow.

- `crypsa/crypsa_teaching_prototype.py`
  Main teaching prototype orchestration file.

- `crypsa/app_shell.py`
  App/window lifecycle and shell-level setup.

- `crypsa/controller_ui_actions.py`
  Smaller UI-facing controller coordination helpers.

## Layer 2 - Runtime State And Actions

- `crypsa/runtime_store.py`
  In-memory runtime state home.

- `crypsa/runtime_models.py`
  Typed runtime records and shared runtime seams.

- `crypsa/runtime_actions.py`
  Observer-side action helpers.

- `crypsa/request_dispatch.py`
  Routes typed requests into controller mutation paths.

- `crypsa/crypsa_action_requests.py`
  Typed request definitions representing user intent.

## Layer 3 - Validation / Apply / Reconciliation

- `crypsa/validation.py`
  Candidate-event validation.

- `crypsa/canonical_apply.py`
  Accepted canonical record creation.

- `crypsa/reconciliation.py`
  Candidate reconciliation and server-mint acceptance.

## Layer 4 - Replay / Event Graph

- `crypsa/canonical_replay.py`
  Higher-level replay boundary for rebuilding derived canonical state.

- `crypsa/crypsa_event_graph.py`
  Lower-level lineage, ordering, and event-graph mechanics.

## Layer 5 - Persistence / Fixtures

- `crypsa/runtime_persistence.py`
  Runtime save/load and persistence coordination.

- `crypsa/crypsa_state_io.py`
  Low-level JSON read/write boundary.

- `crypsa/teaching_example_loader.py`
  Loads fixture-backed teaching examples.

- `fixtures/teaching_example.json`
  Seeded teaching scenario content.

## Layer 6 - Adapter Layer

- `crypsa/crypsa_lens_adapters.py`
  Runtime-side adapters.

- `mint/mint_lens_adapters.py`
  Mint-side adapters.

Adapters should shape data and aggregate inputs.
Adapters should not mutate truth or perform validation.

## Layer 7 - UI Layer

- `crypsa/ui/crypsa_render_ui.py`
- `crypsa/ui/crypsa_history_ui.py`
- `crypsa/ui/crypsa_action_ui.py`
- `crypsa/ui/crypsa_teaching_ui.py`
- `mint/mint_editor_ui.py`

The UI layer should consume adapted data, render it, and emit typed requests.

## Layer 8 - Mint Layer

- `mint/mint_models.py`
  Typed Mint-side shared structures.

- `mint/mint_catalog_editor.py`
  Mint editor orchestration.

- `mint/mint_catalog_store.py`
  Mint normalization, validation, and persistence.

Mint defines possible structures.
Runtime decides what actually becomes canonical.

## Layer 9 - Tests

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

## Current Architectural Pressure Point

`crypsa/crypsa_teaching_prototype.py` still remains the main orchestration center.

This is no longer an architectural crisis, but it is still the primary remaining concentration of responsibility.

## One Sentence Summary

The CrypSA teaching prototype is organized into clear layers for runtime orchestration, replay, adapters, requests, UI, Mint authoring, and tests, with each module serving a specific architectural role.

It should now be maintained as a completed teaching artifact, not as an open-ended architecture refactor target.
