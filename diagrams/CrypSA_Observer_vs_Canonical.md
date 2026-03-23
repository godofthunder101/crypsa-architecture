# Observer vs Canonical State

This diagram shows the relationship between:

- local observer simulation  
- canonical server truth  

It explains how CrypSA separates:

> what is predicted  
vs  
> what is real  

---

```mermaid
flowchart LR

subgraph Observer
A[Local State]
B[Local Simulation]
C[Predicted Actions]
end

subgraph Server
D[Validation Pipeline]
E[Canonical Event Log]
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

### Observer Side (Client)

The observer maintains:

* local state
* local simulation
* predicted actions

These allow:

* responsiveness
* immediate feedback

However:

> this state is not authoritative

---

### Server Side (Canonical)

The server maintains:

* validation pipeline
* canonical event log
* derived canonical state

This defines:

> what is actually real

---

### The Interaction

1. The observer performs an action
2. The action becomes a candidate event
3. The server validates the event

---

### Two Possible Outcomes

#### Accepted

* event enters canonical history
* derived state updates
* observers receive canonical update

---

#### Rejected

* canonical state remains unchanged
* observer must correct its local prediction

---

### Reconciliation

The observer updates its local state based on canonical truth.

This ensures:

> all observers converge on the same reality

---

## Key Insight

> The observer simulates freely.
> The server decides what becomes real.
> Canonical history corrects local state.

---

## Relationship to Specs

This diagram connects:

* Runtime Spec → observer/server roles
* Validation Model → decision boundary
* Consistency Model → reconciliation
* Replay Model → canonical reconstruction

---

## One Sentence Summary

Observers simulate locally and predict outcomes, but only server-validated events become canonical truth, and all observers reconcile to that shared state.
