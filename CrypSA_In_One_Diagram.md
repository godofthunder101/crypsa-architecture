# CrypSA — In One Diagram

## Purpose

This diagram provides a complete, high-level view of the CrypSA architecture.

It shows how:

* observers simulate locally
* candidate events cross the invariant boundary
* the validator determines canonical truth
* canonical event history drives reconstruction

This is the **core mental model of CrypSA in a single view**.

---

## Diagram

```mermaid
flowchart LR

subgraph "Observer (Experience + Interpretation + Translation)"
    A[UI / Experience]
    B[Local Simulation]
    C[Adapters]
    D[Lenses]
end

subgraph "Invariant Boundary"
    E[Candidate Event]
end

subgraph "Truth Layer"
    V[Validator]
    F[Validation and Invariant Enforcement]
    G[Canonical Event History]
    H[Derived Canonical State]
end

A --> B
B --> C
C --> D
D --> A

B --> E
E --> V
V --> F

F -->|Accepted| G
F -->|Rejected| B

G --> H
H --> C
```

---

## How to Read This

### Observer Loop (Left Side)

The observer continuously:

* renders experience (UI)
* simulates locally
* prepares data (adapters)
* interprets meaning (lenses)

This loop is:

* fast
* responsive
* non-authoritative

---

### Invariant Boundary (Center)

The key decision:

> Does this action affect canonical event history?

If yes:

* it becomes a **candidate event**
* it must cross the invariant boundary

---

### Validator (Truth Authority)

The validator:

* evaluates candidate events
* enforces invariants
* accepts or rejects

It may run:

* locally
* or remotely

But:

> its role does not change

---

### Canonical Truth (Right Side)

If accepted:

* the event is appended to canonical event history
* canonical ordering (`server_sequence`) is assigned

Canonical event history is:

> the only source of truth

---

### Reconstruction Loop

From canonical event history:

* derived canonical state is reconstructed
* observers receive updates
* local state is corrected or confirmed

This ensures:

> all observers converge to the same reality

---

## Key Insight

> CrypSA does not synchronize state.
> It synchronizes validated events.

And:

> validation determines what becomes real

---

## The Entire System in One Sentence

Observers simulate locally, propose candidate events across the invariant boundary, the validator determines which events become canonical, and canonical event history drives reconstruction of shared reality.

---

## Why This Matters

This model enables:

* local responsiveness
* deterministic reconstruction
* clear authority boundaries
* replayable systems
* flexible deployment (local or remote validator)

---

## What Makes CrypSA Different

Traditional systems:

```text
Client → Server Simulation → State Sync
```

CrypSA:

```text
Observer → Validation → Canonical Event History → Reconstruction
```

---

## Summary

CrypSA separates:

* **Experience** → local simulation and UI
* **Interpretation** → lenses
* **Translation** → adapters
* **Truth** → validation and canonical event history

The invariant boundary and validator ensure that only valid events become part of shared reality.
