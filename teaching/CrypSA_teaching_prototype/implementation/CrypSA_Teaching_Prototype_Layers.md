> Scope note: This document reflects the teaching prototype implementation at the time it was completed.
>
> It may not match the current CrypSA specification.
>
> The prototype is preserved as a teaching artifact and is not updated to reflect ongoing architectural changes.
>
> For current system behavior, refer to `../../../spec/`.

# CrypSA Teaching Prototype — Layer Model

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

---

## Purpose

This document defines the architectural layers of the CrypSA teaching prototype.

It is not a file-by-file reference.

It is a boundary document that answers:

> Where does each responsibility live?

This document exists to prevent architectural drift as the system evolves.

For guardrails on how to preserve these boundaries, see:

- `implementation/CrypSA_Refactor_Guardrails.md`

For current artifact status and maintenance posture, see:

- `STATUS.md`

---

## Core Principle

The teaching prototype is structured as a layered system where:

- canonical event history defines what has happened  
- derived canonical state is reconstructed via replay  
- interpretation is separate from data shaping  
- presentation is separate from meaning  

Each layer has a clear and non-overlapping responsibility.

---

## Layer Overview

The system is organized into the following layers:

1. Runtime / Controller  
2. Validation / Apply / Reconciliation  
3. Replay / Event Graph  
4. Adapter Layer (Translation)  
5. Lens + Request Layer (Interpretation + Intent)  
6. UI Layer (Experience)  
7. Mint Layer (Structure)  

These layers are directional:

- downward → canonical event history becomes experience  
- upward → user intent becomes candidate events and canonical updates  

---

## Layer 1 — Runtime / Controller

### Responsibility

The runtime/controller layer owns:

- orchestration  
- candidate event creation  
- coordination of runtime actions  
- triggering validation and replay  
- high-level application flow  

### Key Modules

- `crypsa/crypsa_teaching_prototype.py`
- `crypsa/runtime_store.py`
- `crypsa/runtime_actions.py`
- `crypsa/controller_ui_actions.py`

### Rules

- This layer coordinates what happens.  
- It does not define canonical truth directly.  
- It does not shape UI data.  
- It does not implement replay logic.  

---

## Layer 2 — Validation / Apply / Reconciliation

### Responsibility

This layer defines how candidate events become canonical events.

It owns:

- validation (schema → identity → preconditions → invariants → rules)  
- acceptance or rejection of candidate events  
- assignment of `server_sequence`  
- canonical event creation and append to canonical event history  

### Key Modules

- `crypsa/validation.py`
- `crypsa/reconciliation.py`
- `crypsa/canonical_apply.py`

### Rules

- This layer defines what becomes canonical.  
- It must not perform replay.  
- It must not shape UI data.  
- It must not contain presentation logic.  

---

## Layer 3 — Replay / Event Graph

### Responsibility

This layer derives state from canonical event history.

It owns:

- replay of canonical events  
- event ordering and lineage  
- deterministic reconstruction of derived canonical state  

### Key Modules

- `crypsa/canonical_replay.py`
- `crypsa/crypsa_event_graph.py`

### Rules

- Input: canonical event history  
- Output: derived canonical state  
- No validation  
- No UI interaction  
- No mutation outside replay state  

---

## Layer 4 — Adapter Layer (Translation)

### Responsibility

Adapters translate runtime and canonical data into structured forms.

They:

- reshape canonical and observer data  
- combine multiple data sources  
- produce lens-ready or UI-ready structures  

### Key Modules

- `crypsa/crypsa_lens_adapters.py`
- `mint/mint_lens_adapters.py`

### Rules

- Adapters translate; they do not define truth.  
- They do not mutate canonical event history.  
- They do not enforce rules or validation.  
- They produce structured outputs only.  

---

## Layer 5 — Lens + Request Layer (Interpretation + Intent)

### Responsibility

This layer defines:

- how data is interpreted  
- how user intent enters the system  

---

### Lenses

Lenses answer:

> What does this mean for this observer?

They may:

- interpret state  
- determine visibility  
- define interaction meaning  

They must not:

- mutate runtime state  
- validate events  
- define canonical truth  

---

### Requests

Requests represent user intent entering the system.

Examples:

- submit candidate event  
- select branch  
- select history point  
- reload catalog  

Requests:

- carry structured intent  
- are routed through dispatch  
- trigger controller-side logic  

They must not:

- contain business logic  
- validate themselves  
- mutate state directly  

---

### Key Modules

- `crypsa/crypsa_action_requests.py`
- `crypsa/request_dispatch.py`
- runtime and Mint lens dataclasses  

---

## Layer 6 — UI Layer (Experience)

### Responsibility

The UI layer handles:

- rendering  
- interaction  
- input capture  
- feedback  

### Key Modules

- `crypsa/ui/crypsa_render_ui.py`
- `crypsa/ui/crypsa_history_ui.py`
- `crypsa/ui/crypsa_action_ui.py`
- `crypsa/ui/crypsa_teaching_ui.py`
- `mint/mint_editor_ui.py`

### Rules

- UI consumes adapter + lens outputs.  
- UI emits typed requests.  
- UI must not:
  - validate events  
  - mutate canonical event history  
  - perform replay  
  - enforce invariants  

UI is presentation only.

---

## Layer 7 — Mint Layer (Structure)

### Responsibility

The Mint layer defines:

- object schemas (genomes)  
- invariant inputs  
- allowed transitions  
- metadata  

### Key Modules

- `mint/mint_models.py`
- `mint/mint_catalog_editor.py`
- `mint/mint_catalog_store.py`

### Rules

- Mint defines what is possible.  
- Runtime determines what becomes canonical.  
- Mint must not:
  - mutate canonical event history  
  - bypass validation  
  - act as runtime execution  

---

## Data Flow

### Downward (Canonical Event History → Experience)

```text
Canonical Event History
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI
````

---

### Upward (Intent → Canonical Event History)

```text
UI Interaction
-> Typed Request
-> Request Dispatch
-> Controller / Runtime Action
-> Validation
-> Canonical Apply
-> Canonical Event
-> Canonical Event History
-> Replay
```

---

## Boundary Rules

### Runtime

* owns orchestration
* does not own truth directly

### Validation

* defines canonical acceptance
* must remain deterministic

### Replay

* pure derivation
* no side effects

### Adapters

* no mutation
* no validation
* no decision-making

### Requests

* intent only
* no logic

### UI

* presentation only
* no canonical mutation

### Mint

* defines structure
* does not execute runtime behavior

---

## What This Prototype Is

This is:

* a teaching implementation
* a concept-validation artifact
* a structured demonstration of CrypSA principles

---

## What This Prototype Is Not

This is not:

* a networked runtime
* a distributed system
* a production server
* a scalability proof
* a security model

---

## Key Insight

> Canonical event history defines what has happened.
> Replay defines what currently exists.
> All other layers interpret, shape, or present that reality.

---

## One Sentence Summary

The CrypSA teaching prototype is a layered system where canonical event history defines truth, validation controls acceptance, replay derives state, adapters shape data, lenses interpret meaning, and UI presents the result while user intent flows back through typed requests into the runtime.
