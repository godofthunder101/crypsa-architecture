---
# CrypSA Minimal Server v0.1

## Purpose

This document defines the smallest practical standalone server that can prove CrypSA’s core runtime model.

The goal of the minimal server is not production readiness.

The goal is to prove that CrypSA can function as a real runtime system with:

- independent server authority
- candidate event submission
- validation
- canonical event recording
- canonical update distribution
- observer reconciliation support

This server is a technical proof step between the teaching prototype and a more complete runtime.

---

## 1. Goals

CrypSA Minimal Server v0.1 should prove the following:

1. observers can submit candidate events to an independent server
2. the server can validate those events
3. the server can accept or reject them
4. accepted events become canonical history
5. derived canonical state can be updated from accepted events
6. clients can receive canonical updates and reconcile
7. late join or reconnect can be supported through snapshot + event tail

---

## 2. Non-Goals

CrypSA Minimal Server v0.1 does not attempt to prove:

- large-scale scalability
- advanced anti-cheat systems
- distributed shard coordination
- combat adjudication
- heavy physics validation
- branch merging
- offline branch merging
- cryptographic trust proofs
- production-grade persistence guarantees
- production-grade account/auth systems

This server should remain intentionally small.

---

## 3. What This Server Must Demonstrate

The minimal server must demonstrate the CrypSA runtime loop:

Local Observer Action
→ Candidate Event Submission
→ Server Validation
→ Accept or Reject
→ Canonical Log Update
→ Derived State Update
→ Observer Notification
→ Client Reconciliation

If this loop works cleanly, the server succeeds.

---

## 4. Recommended Scope

The minimal server should focus on a very small world model.

Recommended feature slice:

- one shared map or tile grid
- one player identity model
- structure placement
- structure destruction
- one inventory/resource requirement
- one conflict scenario
- one reconnect / late-join path

This is enough to prove the architecture.

---

## 5. Recommended Example Use Case

The best first use case is:

## Structure Placement

Why:

- easy to understand
- easy to validate
- easy to conflict
- easy to reconcile
- naturally demonstrates canonical truth

Optional second use case:

## Item Transfer

Why:

- demonstrates ownership invariants
- demonstrates target references
- demonstrates rejection and acceptance clearly

---

## 6. Minimal Runtime Components

CrypSA Minimal Server v0.1 should contain the following components.

### 6.1 Transport Layer

Responsible for:

- receiving candidate event submissions
- returning acceptance/rejection results
- sending canonical updates to connected observers

This may use:

- WebSocket
- TCP
- local IPC
- HTTP + polling (acceptable for early prototype, but less ideal)

Recommended:
- WebSocket for bidirectional simplicity

---

### 6.2 Event Intake Layer

Responsible for:

- accepting incoming candidate events
- parsing payloads
- checking required fields
- normalizing event structure

This is the first boundary before validation.

---

### 6.3 Validation Pipeline

Responsible for:

- schema validation
- identity validation
- precondition validation
- invariant validation
- event-type-specific rule validation

This is the heart of the server.

---

### 6.4 Conflict Scope Resolver

Responsible for:

- determining which objects/tiles/resources are affected
- ensuring atomic validation within the conflict scope
- rejecting losing conflicting proposals

This can be simple in v0.1.

Example conflict scopes:

- tile ID
- object ID
- inventory slot
- ownership target

---

### 6.5 Canonical Event Log

Responsible for:

- recording accepted events
- assigning canonical sequence metadata
- acting as the append-only source of truth

This may initially be:

- in-memory with optional JSON persistence
- file-backed append log
- lightweight embedded database

---

### 6.6 Derived Canonical State Store

Responsible for maintaining materialized canonical state for fast validation and querying.

Examples:

- current tile occupancy
- current object ownership
- current resource count
- current object lifecycle state

This state must always be derivable from canonical history.

---

### 6.7 Snapshot Generator

Responsible for:

- periodically capturing derived state
- associating snapshots with canonical sequence position
- enabling reconnect / late-join reconstruction

This can be very basic in v0.1.

---

### 6.8 Observer Session Manager

Responsible for:

- tracking connected observers
- tracking each observer’s last known canonical position
- sending updates or resync data on reconnect

---

## 7. Minimal Data Flow

The minimal server should follow this flow.

### 7.1 Candidate Submission

Observer sends candidate event with:

- event_id
- event_type
- actor_id
- target_ids
- payload
- client_time
- branch_id
- precondition_refs

---

### 7.2 Intake

Server:

- parses event
- verifies basic shape
- checks for duplicate event_id

---

### 7.3 Validation

Server validates:

- schema
- identity
- branch
- preconditions
- invariants
- event-specific rules

---

### 7.4 Decision

If valid:

- assign canonical sequence
- assign canonical event ID
- append to canonical log
- update derived state

If invalid:

- return rejection result
- do not mutate canonical state

---

### 7.5 Distribution

For accepted events, server sends canonical update to relevant observers.

For rejected events, server sends rejection outcome to submitting observer.

---

### 7.6 Reconnect / Late Join

Observer provides last known canonical position.

Server responds with:

- snapshot, if available and appropriate
- canonical event tail after snapshot/position

Observer reconstructs current canonical state.

---

## 8. Minimum Event Types

CrypSA Minimal Server v0.1 should support only a very small set of event types.

Recommended minimum set:

- `mint_object`
- `place_structure`
- `destroy_structure`

Optional fourth:
- `transfer_object`

Anything beyond this risks unnecessary complexity.

---

## 9. Minimum Validation Rules

To keep v0.1 small, validation should focus on obvious canonical rules.

### For `place_structure`

Validate:

- actor exists
- target tile exists
- tile is empty
- tile is buildable
- actor has required resources
- placement does not violate occupancy invariant

### For `destroy_structure`

Validate:

- target exists
- target is destroyable
- actor has permission
- target has not already been destroyed

### For `mint_object`

Validate:

- proposed identity is unique
- genome or object type exists
- initial state is valid

---

## 10. Atomicity Requirement

Validation and acceptance must be atomic within conflict scope.

For v0.1, this can be implemented simply:

- lock affected tile/object/resource during validation + acceptance
- do not allow two conflicting candidate events to validate simultaneously against the same scope

This is enough for the first real server.

---

## 11. Minimal Persistence Model

The minimal server does not need a production database.

Recommended v0.1 persistence:

- append-only event log file
- derived state stored in memory
- periodic snapshot files

This keeps the system inspectable and easy to debug.

---

## 12. Recommended Internal Model

A simple internal server structure could look like this:

- `transport/`
- `event_intake/`
- `validation/`
- `conflict_scope/`
- `canonical_log/`
- `derived_state/`
- `snapshots/`
- `sessions/`

Or in one smaller prototype:

- `server.py`
- `validation.py`
- `state.py`
- `events.py`
- `snapshots.py`
- `protocol.py`

Both are acceptable. Simplicity is preferred.

---

## 13. Recommended Observer Capabilities

The minimal client or observer only needs to do a few things.

### Must Support

- local action triggering
- candidate event submission
- pending proposal tracking
- acceptance/rejection handling
- canonical update application
- rebuild from snapshot + event tail

### Does Not Need

- advanced prediction
- fancy interpolation
- advanced rollback systems
- sophisticated visual reconciliation

Keep it plain and inspectable.

---

## 14. Required Demo Scenarios

The minimal server is successful if it can demonstrate these scenarios.

### Scenario 1 — Valid Placement

- client places structure on empty tile
- server accepts
- canonical event recorded
- all connected observers update

### Scenario 2 — Conflicting Placement

- two clients attempt same tile
- one accepted
- one rejected with `conflict_lost`
- rejected client reconciles

### Scenario 3 — Invalid Placement

- client attempts illegal placement
- server rejects with meaningful code
- canonical state unchanged

### Scenario 4 — Late Join

- new observer connects
- receives snapshot + event tail
- reconstructs current state correctly

### Scenario 5 — Retry Safety

- same candidate event submitted twice
- server processes once
- duplicate does not create duplicate canonical event

These scenarios matter more than visual polish.

---

## 15. Recommended Debug Visibility

The minimal server should expose enough visibility to make debugging easy.

Useful debug outputs:

- received candidate events
- validation stage results
- rejection codes
- accepted canonical events
- current derived state summary
- snapshot creation points
- observer sync positions

A simple console log is enough for v0.1.

---

## 16. Suggested Network Contract

The server does not need a full formal protocol yet, but should use a small, consistent message shape.

### Candidate Submission

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
    "branch_id": "main",
    "precondition_refs": {
      "tile_42_empty": true
    }
  }
}
````

### Acceptance Result

```json
{
  "type": "event_result",
  "source_event_id": "evt_client_001",
  "result": "accepted",
  "canonical_event_id": "canon_00014",
  "server_sequence": 14
}
```

### Rejection Result

```json
{
  "type": "event_result",
  "source_event_id": "evt_client_001",
  "result": "rejected",
  "reason": "conflict_lost"
}
```

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
    "accepted_at": 1234567900,
    "branch_id": "main"
  }
}
```

---

## 17. Minimal Technical Success Criteria

CrypSA Minimal Server v0.1 is successful if:

* it runs as an independent process
* at least two observers can connect
* candidate events can be submitted
* validation can accept and reject correctly
* canonical log persists accepted events
* derived state updates correctly
* reconnect or late-join reconstruction works
* duplicate submissions are idempotent

If all of these work, CrypSA has crossed from concept into runtime proof.

---

## 18. Recommended Development Priorities

Build in this order:

1. independent server process
2. candidate event intake
3. append-only canonical log
4. derived canonical state
5. validation pipeline
6. canonical update delivery
7. reconnect / snapshot support
8. second observer / conflict test

Do not start with:

* graphics
* combat
* advanced prediction
* complex content systems

Start with truth flow.

---

## 19. Summary

CrypSA Minimal Server v0.1 is the smallest standalone server that can prove:

* observers do not define shared truth
* candidate events must be validated
* accepted events become canonical history
* canonical state can be reconstructed and distributed
* multiple observers can converge on the same event-defined reality

---

## One Sentence Summary

CrypSA Minimal Server v0.1 is a small standalone server designed to prove that observer-submitted candidate events can be validated, recorded as canonical history, and distributed back to clients as shared event-driven truth.

```
