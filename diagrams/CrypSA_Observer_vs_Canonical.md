# Observer vs Canonical State

## Purpose

This diagram shows the relationship between:

* local observer simulation
* the server’s truth-layer role

It explains how CrypSA separates:

> what is predicted
> vs
> what is real

---

## Diagram

```mermaid
flowchart LR

subgraph "Observer"
    A[Local State]
    B[Local Simulation]
    C[Predicted Actions]
end

subgraph "Server (Truth Layer)"
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

* local state
* local simulation
* predicted actions

These enable:

* responsiveness
* immediate feedback

However:

> this state is not authoritative

---

### Server Side (Truth Layer)

The server maintains:

* validation and invariant enforcement
* canonical event history
* derived canonical state

Canonical event history defines what is real.

Derived state is a computed view, not the source of truth.

---

### Interaction Flow

1. the observer performs an action
2. the action becomes a candidate event
3. the server validates the event

---

### Outcomes

#### Accepted

* event is appended to canonical event history
* canonical truth changes
* observers receive updates

---

#### Rejected

* canonical truth does not change
* observer corrects its local prediction

---

### Reconciliation

Observers update local state based on canonical truth.

This ensures:

> all observers converge on the same reality

---

## Key Insight

> The observer simulates freely.
> The server determines what becomes real.
> Canonical event history corrects local state.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → server validation and canonical events
* **Experience** → local simulation and prediction

Adapters and lenses operate within the observer before and after this flow.

---

## Relationship to Specs

This diagram connects to:

* Runtime Spec — observer/server roles
* Validation Model — invariant enforcement
* Consistency Model — reconciliation
* Replay Model — canonical reconstruction

---

## One Sentence Summary

Observers simulate locally and predict outcomes, but only validated canonical events become part of canonical event history, and all observers reconcile to that shared reality.
