# CrypSA Architecture

## Purpose

This section explains how CrypSA works as a system.

It focuses on **structure and relationships**, not step-by-step execution.

This folder is part of the **authoritative architecture layer**.

Other documents must not redefine the concepts described here.

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Core Idea

CrypSA separates multiplayer systems into:

* canonical event history (truth)
* validation (authority)
* observer simulation (local reconstruction and prediction)

Rather than synchronizing full world state, CrypSA synchronizes:

> **validated canonical events as canonical event history**

---

## Four Responsibilities (Mental Model)

CrypSA can be understood through four responsibilities:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining meaning
* **Experience** — UI and local simulation

These responsibilities define the architecture.

---

## Key Architectural Ideas

### Event-Based Truth

The system is event-driven:

* actions → candidate events
* validation → canonical events (assigned canonical ordering via `canonical_sequence`)
* canonical events → canonical event history

Canonical event history defines what is true.

---

### Observer-Side Simulation

Observers:

* reconstruct derived canonical state
* simulate the world locally
* respond immediately to input
* reconcile when canonical updates arrive

This provides responsiveness without sacrificing consistency.

---

### Validation as Authority

The **validator** operates in the **truth layer**.

It:

* validates candidate events
* enforces invariants
* determines what becomes canonical

> The validator controls truth, not simulation.

---

### Replay as State

World state is not the primary source of truth.

Instead:

* canonical event history is authoritative
* derived state is reconstructed from that history

Replay enables deterministic reconstruction, debugging, and verification.

---

### Adapters (Translation Layer)

Adapters:

* reshape canonical and observer/runtime data
* prepare structured data for downstream layers
* isolate internal state from interpretation

They belong to the **translation layer**.

---

### Lenses (Interpretation Layer)

Lenses:

* interpret translated data
* determine visibility and interaction relevance
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

```mermaid id="3k7d2n"
flowchart LR

A[Canonical Event History] --> B[Derived Canonical State]
B --> C[Adapters]
C --> D[Lenses]
D --> E[UI / Experience]
```

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

* `CrypSA_Architecture_Overview.md` — system overview
* `../spec/CrypSA_Event_Model.md` — event structure
* `../spec/CrypSA_Validation_Model.md` — invariant enforcement
* `../spec/CrypSA_Replay_Model.md` — state reconstruction
