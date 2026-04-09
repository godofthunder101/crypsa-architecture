# CrypSA — In One Diagram

## Purpose

This diagram provides a complete, high-level view of the CrypSA architecture.

It shows how:

* observers simulate locally
* candidate events cross the invariant boundary
* the validator determines what becomes canonical
* canonical event history drives reconstruction via replay

This is the **core mental model of CrypSA in a single view**.

---

## Diagram

```mermaid
flowchart LR

subgraph "Observer (Experience + Translation + Interpretation)"
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
    F[Validation Pipeline]
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

G -->|Replay| H
H --> C
```

---

## How to Read This

### Observer Loop (Left Side)

The observer continuously:

* renders experience (UI)
* simulates locally
* shapes data through adapters
* interprets meaning through lenses

This loop is:

* fast
* responsive
* non-authoritative

It is allowed to feel immediate even when canonical truth has not yet changed.

---

### Invariant Boundary (Center)

The key decision is:

> Does this action affect canonical event history?

If no:

* it remains local

If yes:

* it becomes a **candidate event**
* it must cross the invariant boundary
* it must be validated before becoming canonical

If accepted:

* If accepted, an event becomes canonical and is appended to canonical event history

---

### Validator (Truth Authority)

The validator:

* evaluates candidate events
* enforces invariants
* determines whether an event becomes canonical

It may run:

* **locally**, within the observer environment
* **remotely**, as a separate system

But:

> its role does not change

CrypSA defines the validator as an architectural role, not a fixed machine location.

---

### Canonical Truth (Right Side)

If accepted:

* If accepted, an event becomes canonical and is appended to canonical event history
* `canonical_sequence` is assigned by the validator

Canonical event history is:

> the only source of truth

Derived canonical state is useful, but it is reconstructed from canonical event history via replay and is not independently authoritative.

---

### Reconstruction Loop

From canonical event history:

* derived canonical state is reconstructed via replay
* observers receive canonical updates
* local state is corrected or confirmed

This ensures:

> all observers converge toward equivalent derived canonical state

---

## Key Insight

> CrypSA does not synchronize state.
> It synchronizes validated events.

And:

> validation determines what becomes canonical

---

## The Entire System in One Sentence

Observers simulate locally, propose candidate events across the invariant boundary, the validator determines which events become canonical, and canonical event history drives reconstruction of derived canonical state via replay.

---

## Why This Matters

This model enables:

* local responsiveness
* deterministic reconstruction
* clear authority boundaries
* replayable systems
* flexible deployment (local or remote validator)
* persistent worlds defined by canonical event history

---

## What Makes CrypSA Different

Traditional systems:

```text
Clients → Central Authority → State Synchronization
```

CrypSA:

```text
Observer → Validation → Canonical Event History → Replay → Reconstruction
```

---

## Related Reading

For deployment-specific clarification, see:

* `architecture/CrypSA_Validator_Deployment_Model.md`
* `diagrams/CrypSA_Local_vs_Remote_Validator.md`

---

## Summary

CrypSA separates:

* **Experience** → UI and local simulation
* **Translation** → adapters
* **Interpretation** → lenses
* **Truth** → validation and canonical event history

The invariant boundary and validator ensure that only valid events become part of canonical event history.
