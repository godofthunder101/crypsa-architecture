# CrypSA Event Flow

## Purpose

This diagram shows how a local observer action becomes canonical truth in CrypSA.

It represents the runtime loop:

> local simulation → validation → canonical history → observer reconciliation

---

## Diagram

```mermaid
flowchart LR

A[Player Action] --> B[Local Simulation]
B --> C[Create Candidate Event]
C --> D[Send to Server]

D --> E[Validation (Invariant Enforcement)]

E -->|Accepted| F[Append to Canonical Event History]
E -->|Rejected| G[Return Rejection Result]

F --> H[Observers Receive Canonical Update]

H --> J[Observer Reconciliation]

G --> J

J --> K[Updated Local State]
```

---

## How to Read This

### 1. Local Phase

* the player performs an action
* the observer simulates it immediately
* a candidate event is created

At this point:

> the result is **not yet canonical**

---

### 2. Validation Phase

* the event is sent to the server
* the server validates it against invariants

Result:

* accepted
  or
* rejected

---

### 3. Canonical Phase

If accepted:

* the event is appended to canonical history
* canonical truth is updated
* observers are notified

---

### 4. Reconciliation Phase

Observers:

* compare local prediction with canonical truth
* correct or confirm local state
* continue simulation

---

## Key Insight

> Actions do not directly change reality.
> Validated canonical events define reality.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → validation and canonical events
* **Experience** → local simulation
* **Reconciliation** → convergence of observers

Adapters and lenses operate within the observer before and after this flow.

---

## Relationship to Specs

This diagram maps to:

* Runtime Spec — overall flow
* Event Model — candidate event creation
* Validation Model — invariant enforcement
* Consistency Model — reconciliation

---

## One Sentence Summary

A player action becomes a candidate event, the server validates it against canonical truth, accepted events are recorded in canonical history, and all observers reconcile to that shared reality.
