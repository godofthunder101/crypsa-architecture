# CrypSA Teaching Prototype - Layer Model

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

## Purpose

This document defines the architectural layers of the CrypSA teaching prototype.

It is not a file-by-file reference.

It is a boundary document that answers:

Where does each responsibility live?

This document exists to prevent architectural drift as the system evolves.

For the companion document that describes what future refactors should avoid blurring, see:

- `implementation/CrypSA_Refactor_Guardrails.md`

For the current artifact-status and maintenance posture, also see:

- `STATUS.md`

## Core Principle

The teaching prototype is structured as a layered system where:

- truth is event-driven
- state is derived
- interpretation is separate from data
- presentation is separate from meaning

Each layer has a clear responsibility.

## Layer Overview

The system is organized into the following layers:

1. Runtime / Controller
2. Replay / Event Graph
3. Adapter Layer
4. Lens + Request Layer
5. UI Layer
6. Mint Layer

These layers are directional.

Data flows downward for presentation and upward for intent.

## Layer 1 - Runtime / Controller

### Responsibility

The runtime/controller layer owns:

- canonical event handling
- validation coordination
- event acceptance and rejection
- replay triggering
- orchestration of runtime actions
- high-level application flow

### Key Modules

- `crypsa/crypsa_teaching_prototype.py`
- `crypsa/runtime_store.py`
- `crypsa/runtime_actions.py`
- `crypsa/validation.py`
- `crypsa/reconciliation.py`
- `crypsa/canonical_apply.py`
- `crypsa/controller_ui_actions.py`

### Rules

- This layer defines what happens.
- It owns meaning and decisions.
- It does not shape UI data directly.
- It does not perform rendering.

## Layer 2 - Replay / Event Graph

### Responsibility

This layer derives canonical state from history.

It owns:

- canonical replay
- event ordering
- lineage traversal
- branch-aware reconstruction

### Key Modules

- `crypsa/canonical_replay.py`
- `crypsa/crypsa_event_graph.py`

### Rules

- Input: canonical events
- Output: derived canonical state
- No UI knowledge
- No validation logic
- No mutation outside replay state

## Layer 3 - Adapter Layer

### Responsibility

Adapters translate runtime state into structured data for interpretation.

They:

- reshape data
- combine runtime and observer state
- produce lens-ready or UI-ready models

### Key Modules

- `crypsa/crypsa_lens_adapters.py`
- `mint/mint_lens_adapters.py`

### Rules

- Adapters translate; they do not decide truth.
- They do not mutate canonical state.
- They do not enforce rules.
- They do not perform validation.
- They produce structured outputs for consumers.

## Layer 4 - Lens + Request Layer

### Responsibility

This layer defines:

- how data is interpreted for specific UI surfaces
- how user intent is expressed back to the runtime

### Key Modules

- `crypsa/crypsa_action_requests.py`
- `crypsa/request_dispatch.py`
- runtime and Mint lens dataclasses

### Lenses

Lenses answer:

What does this data mean for this observer or this UI surface?

They may:

- interpret state
- shape interaction options
- provide read-only presentation structure

They must not:

- mutate runtime state
- enforce canonical truth

### Requests

Requests represent user intent entering the system.

Examples:

- submit candidate
- select branch
- select history point
- reload catalog

Requests:

- are routed through dispatch
- trigger controller-side mutation paths
- do not contain business logic

## Layer 5 - UI Layer

### Responsibility

The UI layer handles:

- rendering
- interaction
- input capture

### Key Modules

- `crypsa/ui/crypsa_render_ui.py`
- `crypsa/ui/crypsa_history_ui.py`
- `crypsa/ui/crypsa_action_ui.py`
- `crypsa/ui/crypsa_teaching_ui.py`
- `mint/mint_editor_ui.py`

### Rules

- UI consumes lens or adapted data.
- UI emits requests.
- UI does not:
  - validate events
  - mutate canonical state
  - perform replay
  - enforce invariants

UI is presentation only.

## Layer 6 - Mint Layer

### Responsibility

The Mint layer defines:

- object schemas
- invariant rules
- transitions
- metadata

It is the authoring system for runtime definitions.

### Key Modules

- `mint/mint_models.py`
- `mint/mint_catalog_editor.py`
- `mint/mint_catalog_store.py`

### Rules

- Mint defines what is possible.
- Runtime decides what actually becomes canonical.
- Mint must not directly mutate canonical state.
- Mint must not bypass validation or replay.

## Data Flow

### Downward (Truth -> Experience)

```text
Canonical Events
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI
```

### Upward (Intent -> Truth)

```text
UI Interaction
-> Typed Request
-> Request Dispatch
-> Controller / Runtime Action
-> Validation
-> Canonical Apply
-> Canonical Event
-> Replay
```

## Boundary Rules

### Runtime

- Owns truth decisions
- Must not depend on UI layout details

### Replay

- Pure derivation
- No side effects

### Adapters

- No mutation
- No validation
- No truth decisions

### Requests

- Intent only
- No business logic

### UI

- Presentation only
- No canonical mutation

### Mint

- Defines structures
- Does not execute runtime behavior

## What This Prototype Is

This is:

- a teaching implementation
- a concept-validation artifact
- a structured demonstration of CrypSA principles

## What This Prototype Is Not

This is not:

- a networked runtime
- a distributed system
- a production server
- a scalability proof
- a security model

## One Sentence Summary

The CrypSA teaching prototype is a layered system where canonical events define truth, replay derives state, adapters shape data, lenses interpret meaning, and UI presents the result while user intent flows back through typed requests into the runtime.
