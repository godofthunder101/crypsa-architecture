# CrypSA Architecture

## Purpose

This section explains how CrypSA works as a system.

It focuses on **structure and relationships**, not step-by-step execution.

This folder is part of the **authoritative architecture layer**.

Other documents should not redefine the concepts described here.

For exact runtime behavior, see `../spec/`.

---

## Core Idea

CrypSA separates multiplayer systems into:

* **canonical event history and validation**
* **observer simulation** (local reconstruction and prediction)

Rather than synchronizing full world state, CrypSA synchronizes:

> **validated canonical events**

---

## Four Responsibilities (Mental Model)

CrypSA can be understood through four responsibilities:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining meaning
* **Experience** — UI and local simulation

These responsibilities define the architecture.

---

## Key Architectural Ideas

### Event-Based Truth

The system is event-driven:

* actions → candidate events
* validation → canonical events
* canonical events → shared reality

Canonical event history defines what is true.

---

### Observer-Side Simulation

Observers:

* reconstruct canonical state
* simulate the world locally
* respond immediately to input
* reconcile when canonical updates arrive

This provides responsiveness without sacrificing consistency.

---

### Validation as Authority

The server operates in the **truth layer**.

It:

* validates candidate events
* enforces invariants
* determines what becomes canonical

> The server controls truth, not simulation.

---

### Replay as State

World state is not the primary source of truth.

Instead:

* canonical event history is authoritative
* state is derived from that history

Replay enables reconstruction, debugging, and verification.

---

### Adapters (Translation Layer)

Adapters:

* reshape canonical and runtime data
* prepare structured outputs
* isolate internal state from interpretation

They belong to the **translation layer**.

---

### Lenses (Interpretation Layer)

Lenses:

* interpret translated data
* determine visibility and interaction
* produce observer-specific meaning

They belong to the **interpretation layer**.

---

### Experience Layer

The experience layer:

* renders the world
* handles input
* provides feedback

This is where players interact with the system.

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

Separating responsibilities enables:

* deterministic reconstruction
* responsive local simulation
* clear debugging via event history
* multiple observer perspectives
* independent evolution of layers

---

## Where to Go Next

* `../CrypSA_Architecture_Overview.md` — system overview
* `../spec/CrypSA_Event_Model.md` — event structure
* `../spec/CrypSA_Validation_Model.md` — invariant enforcement
* `../spec/CrypSA_Replay_Model.md` — state reconstruction
