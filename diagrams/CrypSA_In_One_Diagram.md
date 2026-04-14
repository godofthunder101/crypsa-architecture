# CrypSA Universe Lifecycle (Full System View)

## Purpose

This document presents a unified view of how a CrypSA universe operates over time.

It combines:

* observer interaction
* event flow
* validation
* canonical event history
* replay and reconstruction
* observer reconciliation

into a single lifecycle model.

This is an **illustrative system view**, not an authoritative specification.

For the authoritative conceptual flow of the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Diagram

> This diagram illustrates the CrypSA runtime model.
> It does not define runtime behavior.
> For the authoritative conceptual flow, see:
> → ../architecture/CrypSA_Runtime_Model.md

```mermaid
flowchart LR

subgraph Observer
A[Observer Reconstruction]
B[Local Simulation]
C[User Action]
D[Candidate Event Creation]
end

subgraph Boundary
E[Invariant Boundary]
end

subgraph Validator
F[Validation Pipeline]
G[Accept or Reject]
H[Canonical Event History]
end

subgraph Distribution
I[Canonical Events Available to Observers]
end

subgraph Reconstruction
J[Replay]
K[Derived Canonical State]
end

A --> B
B --> C
C --> D
D --> E

E -->|Affects Canonical| F
E -->|Local Only| B

F --> G

G -->|Accepted| H
G -->|Rejected| B

H --> I
I --> J
J --> K
K --> A
````

---

## How to Read This

---

### 1. Observer Reconstruction

Observers begin by reconstructing the world:

* from canonical event history
* via replay
* producing derived canonical state

This forms the baseline for all interaction.

---

### 2. Local Simulation (Experience Layer)

Observers simulate:

* movement
* prediction
* UI feedback
* temporary effects

This ensures responsiveness and fluid interaction.

---

### 3. Action and Candidate Event Creation

When a user interacts:

* the observer performs local simulation
* a candidate event is created if needed

This represents **intent**, not truth.

---

### 4. Invariant Boundary

The invariant boundary determines:

> Does this action affect canonical event history?

* No → remains local
* Yes → must be validated

This is the critical separation between:

* local experience
* shared reality

---

### 5. Validation (Truth Layer)

A **validator** evaluates candidate events using the validation pipeline:

* schema validation
* identity validation
* preconditions
* invariant enforcement
* rule validation

---

### 6. Acceptance or Rejection

#### Accepted:

* assigned `canonical_sequence`
* appended to canonical event history

#### Rejected:

* no canonical change
* observer corrects local simulation

---

### 7. Canonical Event History

Canonical event history is:

* append-only
* ordered via `canonical_sequence`
* authoritative

It defines:

> what has actually happened

---

### 8. Distribution

Canonical events may be delivered to observers as a stream:

* may be delayed
* may arrive out of order (ordering resolved via `canonical_sequence`)
* may contain duplicates

Observers must:

* reorder by `canonical_sequence`
* discard duplicates

---

### 9. Replay and Reconstruction

Observers:

* replay canonical events
* reconstruct derived canonical state

This ensures:

> all observers converge on the same world

---

### 10. Observer Reconciliation

Observers compare:

* local prediction
* canonical outcome

They:

* correct divergence
* confirm valid predictions
* continue simulation

---

## Full Lifecycle Summary

```text
Reconstruct → Simulate → Act → Check Boundary → Validate → Append to Canonical Event History → Distribute → Replay → Reconcile → Repeat
```

---

## Key Insight

> CrypSA is not a simulation loop — it is a validation and reconstruction loop.

The system advances through:

* validated events
* canonical ordering (via `canonical_sequence`)
* deterministic replay

---

## Relationship to Architecture

This diagram spans all four responsibilities:

* **Truth** → validation + canonical event history
* **Translation** → adapters shape data during reconstruction and reconciliation
* **Interpretation** → lenses interpret reconstructed and adapted data
* **Experience** → local simulation and UI

---

## Relationship to Specs

This lifecycle connects:

* Event Model → candidate + canonical events
* Validation Model → validation pipeline
* Consistency Model → convergence
* Replay Model → reconstruction
* Transport Model → event distribution
* Identity Model → object continuity

---

## Why This Matters

This unified model explains:

* how CrypSA operates end-to-end
* how all subsystems connect
* why the architecture is coherent

It is the **mental model that ties everything together**.

---

## One Sentence Summary

CrypSA operates as a continuous lifecycle where observers simulate locally, candidate events are validated, accepted events extend canonical event history (ordered via `canonical_sequence`), and all observers reconstruct and reconcile through deterministic replay.
