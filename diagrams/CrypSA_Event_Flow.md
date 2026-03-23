# CrypSA Event Flow

This diagram shows how a local player action becomes canonical truth in CrypSA.

It represents the full runtime loop from:

local simulation → validation → canonical history → reconciliation

---

```mermaid
flowchart LR

A[Player Action] --> B[Local Simulation]
B --> C[Create Candidate Event]
C --> D[Send to Server]

D --> E[Validation Pipeline]

E -->|Accepted| F[Append to Canonical Log]
E -->|Rejected| G[Return Rejection Result]

F --> H[Update Derived State]
H --> I[Broadcast Canonical Event]

I --> J[Observer Reconciliation]

G --> J

J --> K[Final Local State]

````

---

## How to Read This

### 1. Local Phase

* the player performs an action
* the observer simulates it immediately
* a candidate event is created

At this point:

> the change is **not yet canonical**

---

### 2. Validation Phase

* the event is sent to the server
* the validation pipeline decides:

→ accept
or
→ reject

---

### 3. Canonical Phase

If accepted:

* event is recorded in canonical history
* derived state is updated
* observers are notified

---

### 4. Reconciliation Phase

Observers:

* compare local prediction vs canonical truth
* correct if needed

---

## Key Insight

> Actions do not directly change reality.
> Validated events define reality.

---

## Relationship to Specs

This diagram maps directly to:

* Runtime Spec → overall flow
* Event Model → candidate event creation
* Validation Model → decision process
* Consistency Model → reconciliation

---

## One Sentence Summary

A player action becomes a candidate event, the server validates it, accepted events define canonical history, and all observers reconcile to that shared truth.
