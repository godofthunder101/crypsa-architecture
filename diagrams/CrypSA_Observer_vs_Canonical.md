# Observer vs Canonical State

## Purpose

This diagram shows the relationship between:

* local observer simulation
* the validator’s role in defining canonical truth

It explains how CrypSA separates:

> what is predicted
> from
> what is real

For the authoritative conceptual flow of the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Diagram

> This diagram illustrates the relationship between observer state and canonical state within the CrypSA runtime model.
> It does not define runtime behavior or event flow.
> For the authoritative conceptual flow, see:
> → ../architecture/CrypSA_Runtime_Model.md

```mermaid
flowchart LR

subgraph "Observer"
    A[Observer Local State]
    B[Local Simulation]
    C[Predicted State]
end

subgraph "Truth and Reconstruction"
    D[Validation and Invariant Enforcement]
    E[Canonical Event History]
    F[Derived Canonical State]
end

A --> B
B --> C
C --> D

D -->|Accepted| E
D -->|Rejected| A

E --> F
F --> A
````

---

## How to Read This

### Observer Side

The observer maintains:

* observer local state
* local simulation
* predicted state

These enable:

* responsiveness
* immediate feedback

However:

> observer local state is not authoritative

---

### Truth and Reconstruction

This side includes:

* validation and invariant enforcement
* canonical event history
* derived canonical state

Canonical event history defines what is real.

Accepted events are ordered via `canonical_sequence` and appended to canonical event history.

Derived canonical state is a computed view, not the source of truth.

The validator may run locally or remotely, but its role does not change.

---

### Interaction Flow

1. the observer performs an action
2. the observer applies local prediction
3. a candidate event is submitted to the validator
4. the validator evaluates the event

---

### Outcomes

#### Accepted

* the event is assigned `canonical_sequence`
* the event is appended to canonical event history
* canonical events are made available to observers

---

#### Rejected

* canonical event history does not change
* the observer corrects local prediction

---

### Reconciliation

Observers update local state based on derived canonical state reconstructed from canonical event history.

This ensures:

> all observers converge toward canonical truth

---

## Key Insight

> The observer simulates freely.
> The validator determines what becomes real.
> Canonical event history corrects local state.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → validation and canonical event history
* **Experience** → local simulation and prediction

Adapters and lenses operate within the observer before and after this flow.

---

## Relationship to Specs

This diagram connects to:

* Runtime Spec — observer and validator roles
* Validation Model — invariant enforcement
* Consistency Model — reconciliation
* Replay Model — canonical reconstruction

---

## One Sentence Summary

Observers simulate locally and predict outcomes, but only validated events are ordered via `canonical_sequence`, appended to canonical event history, and used to reconcile all observers toward canonical truth.
