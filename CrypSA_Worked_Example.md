# CrypSA Worked Example

> Illustrative note: This document is illustrative.
>
> For authoritative behavior, see `spec/`.

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

This document illustrates how the system behaves.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

This document walks through a complete runtime example of CrypSA.

It shows how:

* a local action becomes a candidate event
* the validator evaluates that event
* canonical event history is updated
* observers reconcile their local state

---

## 📊 Runtime Flow Overview

```mermaid
flowchart LR

A[Player Action] --> B[Local Simulation]
B --> C[Create Candidate Event]
C --> D[Submit to Validator]

D --> E[Validation Pipeline]

E -->|Accepted| F[Canonical Event History]
E -->|Rejected| G[Rejection Result]

F --> H[Replay]
H --> I[Derived Canonical State]
I --> J[Broadcast]

J --> K[Observer Reconciliation]
G --> K
```

---

## Scenario

A player places a mining station on an empty tile.

---

## Initial Canonical State

Derived canonical state (via replay):

* tile_42 → empty
* player_A → resources = 100

Observers have reconstructed this state locally.

---

## Phase 1 — Local Action (Observer)

The player performs:

> Place mining station on tile_42

The observer:

* applies a **local prediction**
* shows the structure immediately
* marks the action as **pending**

At this point:

* local state ≠ canonical state
* no shared change has occurred yet

---

## Phase 2 — Candidate Event Creation

The observer creates a candidate event:

```
event_type = place_structure
actor_id = player_A
target_ids = [tile_42]

payload = {
  structure_type: mining_station,
  cost: 50
}

precondition_refs = {
  tile_42_empty: true,
  player_resources_sufficient: true
}

event_id = evt_001
```

This event represents an **intent**, not a canonical change.

---

## Phase 3 — Submission

The observer submits the event to the validator.

State at this moment:

| Layer     | State                             |
| --------- | --------------------------------- |
| Local     | mining_station placed (predicted) |
| Canonical | tile_42 still empty               |

---

## Phase 4 — Validation Pipeline (Validator)

The validator evaluates the event.

### 4.1 Schema Validation

✅ pass

### 4.2 Identity Validation

✅ pass

### 4.3 Precondition Validation

✅ pass

### 4.4 Invariant Validation

✅ pass

### 4.5 Rule Validation

✅ pass

---

## Phase 5 — Acceptance

The validator accepts the event.

Canonical metadata assigned:

```
canonical_event_id = canon_1203
canonical_sequence = 1203
accepted_at = timestamp
```

The event is appended to canonical event history.

---

## Phase 6 — Replay and Derived State

Replay applies canonical events in `canonical_sequence` order.

Derived canonical state updates:

* tile_42 → mining_station
* player_A resources → 50

Derived canonical state now reflects the change.

---

## Phase 7 — Broadcast

The canonical event is propagated to observers.

---

## Phase 8 — Observer Reconciliation

Each observer compares:

* local predicted state
* canonical update

---

### Case A — Prediction Matches

* no visible change
* pending marker cleared

---

### Case B — Prediction Differs

* local state is corrected
* invalid objects removed
* canonical state applied

---

### Adapter and Lens Interpretation

After reconciliation:

* adapters reshape canonical and observer data
* lenses interpret meaning and context
* UI renders the result

```text id="0r9l4k"
Canonical Update → Adapter → Lens → UI
```

---

## Alternative Scenario — Conflict

Two players attempt to place on tile_42.

---

### Validator Behavior

* evaluates both candidate events
* accepts the first valid event
* rejects the second

---

### Rejection Result

```
result = rejected
reason = precondition_failed
```

---

### Observer Reconciliation

Rejected observer:

* removes predicted structure
* updates to canonical state

---

## What This Demonstrates

* actions are proposals, not guarantees
* validation determines reality
* canonical event history defines what is true
* observers may temporarily diverge
* reconciliation restores consistency

---

## Relationship to Specs

This example corresponds to:

* Runtime Model → overall flow
* Event Model → candidate event structure
* Validation Model → validation stages
* Consistency Model → reconciliation
* Replay Model → reconstruction

---

## One Sentence Summary

A local action becomes a candidate event, the validator evaluates it, accepted events are appended to canonical event history, and observers reconcile their local simulation to that shared history.

---

## Next Step

Continue to:

👉 `architecture/`
