# CrypSA Architecture

This section explains how CrypSA works as a system.

It focuses on structure and relationships, not step-by-step flow.

This folder is part of the authoritative system-explanation layer for CrypSA.

Other documents in the repository should not redefine the concepts described here.

For exact runtime behavior, pair it with `../spec/`.

---

## Core Idea

CrypSA separates multiplayer systems into:

- canonical truth (events and invariants)  
- observer simulation (local reconstruction and prediction)  

Rather than synchronizing full world state, CrypSA synchronizes **validated events**.

---

## Four Responsibilities (Mental Model)

A useful way to understand the architecture is through four responsibilities:

- **Truth** — canonical events and validation  
- **Translation** — adapters shaping runtime data  
- **Interpretation** — lenses determining observer meaning  
- **Experience** — UI and local simulation  

These responsibilities map across the architecture described below.

---

## Key Architectural Ideas

### Event-Based Truth

The system is driven by events, not state.

- actions → candidate events  
- validation → canonical events  
- canonical events → shared reality  

---

### Observer-Side Simulation

Observers:

- simulate the world locally  
- respond immediately to input  
- reconcile when canonical updates arrive  

This provides responsive experience while preserving shared truth.

---

### Validation as Authority

The server enforces invariants.

It decides:

- what is allowed  
- what becomes canonical  

This is the core of the **truth layer**.

---

### Replay as State

World state is not stored directly.

It is:

- derived from canonical history  
- reconstructed via replay  

This keeps truth explicit and debuggable.

---

### Adapters (Translation Layer)

Adapters:

- reshape canonical and observer data  
- prepare structured outputs  
- isolate raw runtime state from interpretation  

They belong to the **translation layer**.

---

### Lenses (Interpretation Layer)

Lenses:

- interpret adapted data  
- define visibility and interaction  
- shape observer-specific meaning  

They belong to the **interpretation layer**.

---

### UI / Experience Layer

The UI:

- renders the world  
- handles input  
- provides local feedback  

This is the **experience layer**.

---

## Layer Relationship (Simplified)

```mermaid
flowchart LR

A[Canonical Events] --> B[Derived State]
B --> C[Adapters]
C --> D[Lenses]
D --> E[UI / Experience]
````

---

## Why This Architecture Exists

Separating responsibilities allows:

* deterministic reconstruction
* flexible client behavior
* clean debugging via event history
* multiple observer perspectives
* independent evolution of layers

---

## Where to Go Next

* `../CrypSA_Architecture_Overview.md` — system map
* `CrypSA_Event_Model.md` — event structure
* `CrypSA_Validation_Model.md` — invariant enforcement
* `CrypSA_Replay_Model.md` — state reconstruction
