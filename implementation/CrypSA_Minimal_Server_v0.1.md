# CrypSA Minimal Server v0.1

> Scope note: This document describes implementation strategy for a minimal server proof step.
> For authoritative runtime behavior, refer to `../spec/`.

---

## Purpose

This document defines the smallest practical standalone server that can prove CrypSA’s core runtime model.

The goal is not production readiness.

The goal is to prove that CrypSA functions as a real runtime system with:

* independent server authority
* candidate event submission
* validation
* canonical event history
* canonical update distribution
* observer reconciliation support

This server is a technical proof step between the teaching prototype and a real runtime.

---

## 1. Goals

CrypSA Minimal Server v0.1 should prove:

1. observers can submit candidate events
2. the server validates events
3. events are accepted or rejected
4. accepted events become canonical event history
5. derived state is updated by applying accepted events
6. observers receive canonical updates and reconcile
7. late join is supported via snapshot + event tail

---

## 2. Non-Goals

This server does not attempt:

* scalability
* anti-cheat systems
* distributed shards
* combat systems
* physics validation
* branch merging
* cryptographic trust
* production persistence
* account systems

Keep it small.

---

## 3. Core Runtime Loop

```text
Observer Action
→ Candidate Event Submission
→ Server Validation
→ Accept or Reject
→ Assign server_sequence
→ Append to Canonical Event History
→ Derived State Update
→ Observer Notification
→ Observer Reconciliation
```

If this loop works, the system works.

---

## 4. Server Responsibility (Critical)

The server:

* validates candidate events
* enforces invariants
* maintains canonical event history

The server does **not**:

* simulate the world
* predict outcomes
* own UI or experience

> The server controls truth, not simulation.

---

## 5. Recommended Scope

Keep the world extremely small:

* one tile grid
* simple player identity
* structure placement/destruction
* one resource
* one conflict scenario
* one reconnect path

---

## 6. Minimal Components

### Transport Layer

Handles:

* receiving candidate events
* sending results
* broadcasting canonical events

Recommended: WebSocket

---

### Event Intake

* parse event
* check required fields
* normalize structure

---

### Validation Pipeline

* schema
* identity
* preconditions
* invariants
* event rules

---

### Conflict Scope Resolver

* determine affected scope
* ensure atomic validation
* reject losing conflicts

---

### Canonical Event History

* append accepted events
* assign `server_sequence`
* act as source of truth

---

### Derived Canonical State Cache

* materialized view of state
* updated by applying accepted events
* used for validation + queries

---

### Snapshot Generator

* capture derived state at sequence
* support reconnect

---

### Session Manager

* track observers
* track last known sequence
* send updates

---

## 7. Minimal Data Flow

### Submission

```json
{
  "type": "candidate_event",
  "event": {
    "event_id": "evt_client_001",
    "event_type": "place_structure",
    "actor_id": "player_A",
    "target_ids": ["tile_42"],
    "payload": {
      "structure_type": "mining_station"
    },
    "client_time": 1234567890,
    "precondition_refs": {
      "tile_42_empty": true
    }
  }
}
```

Note:

* `client_time` is informational only
* server sequence defines ordering

---

### Acceptance

```json
{
  "type": "event_result",
  "source_event_id": "evt_client_001",
  "result": "accepted",
  "canonical_event_id": "canon_00014",
  "server_sequence": 14
}
```

---

### Rejection

```json
{
  "type": "event_result",
  "source_event_id": "evt_client_001",
  "result": "rejected",
  "reason": "conflict_lost"
}
```

---

### Canonical Update

```json
{
  "type": "canonical_event",
  "event": {
    "canonical_event_id": "canon_00014",
    "source_event_id": "evt_client_001",
    "server_sequence": 14,
    "event_type": "place_structure",
    "actor_id": "player_A",
    "target_ids": ["tile_42"],
    "payload": {
      "structure_type": "mining_station"
    },
    "accepted_at": 1234567900
  }
}
```

---

## 8. Idempotency Rule (Critical)

The server must ensure:

* duplicate `event_id` submissions
* do not create duplicate canonical events

Each `event_id` must be processed exactly once.

---

## 9. Atomicity Requirement

Validation and acceptance must be atomic within conflict scope.

For v0.1:

* lock affected scope
* validate + accept atomically
* reject conflicts

---

## 10. Persistence

Minimal approach:

* append-only event file
* in-memory derived canonical state
* periodic snapshot files

---

## 11. Success Criteria

The server is successful if:

* runs independently
* supports multiple observers
* validates correctly
* maintains canonical event history
* updates derived state correctly
* supports reconnect
* enforces idempotency

---

## 12. Development Order

1. server process
2. event intake
3. canonical event history
4. derived state
5. validation
6. broadcasting
7. reconnect
8. conflict tests

---

## 13. Summary

This server proves:

* observers do not define truth
* events must be validated
* canonical event history defines reality
* observers reconstruct from history

---

## One Sentence Summary

CrypSA Minimal Server v0.1 proves that validated candidate events can be recorded as canonical event history and distributed to observers as shared truth.

👉 **Event Schema v0.1 (code-level, no ambiguity)**
