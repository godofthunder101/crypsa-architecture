# CrypSA Minimal Validator v0.1

> This document outlines the smallest practical standalone validator for proving the CrypSA runtime model.
> For authoritative runtime behavior, refer to `../spec/`.

---

## Purpose

This document describes the smallest practical standalone validator that can prove CrypSA’s core runtime model.

The goal is not production readiness.

The goal is to prove that CrypSA functions as a real runtime system with:

* independent validation authority
* candidate event submission
* validation
* canonical event history
* canonical event distribution
* observer reconciliation support

This validator is a **technical proof step** between the teaching prototype and a full runtime system.

---

## Critical Positioning

> The minimal validator is a **valid CrypSA deployment**, not a testing tool.

CrypSA defines validation as a **role**, not a machine.

This means:

* the validator can run locally alongside an observer
* the validator can run as a host
* the validator can run as a dedicated remote system

The minimal validator is:

> the **smallest complete implementation of the validator role**

It is not a reduced model — it is the full model in its simplest form.

---

## Relationship to Local-First Development

This document assumes a **local-first development approach**.

You should:

1. run the validator locally
2. prove validation + replay
3. then move to remote deployment later

👉 See:

```
CrypSA_Local_First_Development_Approach.md
```

> First prove CrypSA locally. Then move the validator, not the architecture.

---

## Validator Deployment (Minimal Context)

The minimal validator supports multiple deployment configurations **without changing behavior**.

---

### Local Deployment (Recommended Starting Point)

```mermaid
flowchart LR

A[Observer] --> B[Local Validator]
B --> C[canonical event history]

C --> A
```

In this configuration:

* observer and validator run in the same environment
* canonical event history is maintained locally
* no network is required

> This is a recommended starting point for implementations

---

### Remote Deployment (Later Stage)

```mermaid
flowchart LR

A[Observer] -->|Candidate Event| B[Network]
B --> C[Validator]

C --> D[canonical event history]
D -->|canonical event| B
B --> A
```

In this configuration:

* observers communicate with a remote validator
* canonical event history is shared
* transport and latency must be handled

---

## Key Insight

> Deployment changes where validation runs, not how validation works.

---

## Quick Start — Local Validator (5 Steps)

This is the **core proof loop**.

---

### Step 1 — Start Validator

Create a validator that:

* initializes empty canonical event history
* initializes derived canonical state
* listens for candidate events

```text
canonical event history = []
derived canonical state = initial
```

---

### Step 2 — Connect Observer

Create an observer that:

* reconstructs derived canonical state
* can submit candidate events
* optionally runs in the same process

---

### Step 3 — Submit Candidate Event

Example:

```json
{
  "event_id": "evt_001",
  "event_type": "place_structure",
  "actor_id": "player_A",
  "target_ids": ["tile_1"],
  "payload": {
    "structure_type": "basic_node"
  },
  "precondition_refs": {
    "tile_1_empty": true
  }
}
```

---

### Step 4 — Validation and Decision

The validator evaluates the candidate event:

* schema validation
* identity validation
* precondition validation
* invariant validation
* rule validation

Decision:

* If accepted, an event becomes canonical and is appended to canonical event history
* If rejected, the event does not become canonical and does not enter canonical event history

---

### Step 5 — Broadcast and Reconcile

The validator broadcasts the canonical event.

Observers:

* replay canonical events
* update derived canonical state
* reconcile local prediction

```text
canonical event history = [event_1]
derived canonical state = updated
```

---

## What This Proves

If this loop works:

* validation is correct
* canonical event history works
* replay works
* reconciliation works

> This is a complete CrypSA runtime loop.

---

## Key Insight

> If it works locally, it will work remotely — provided transport does not define ordering and canonical_sequence remains authoritative.

---

## 1. Goals

The minimal validator should demonstrate:

1. observers submit candidate events
2. validator validates events
3. events are accepted or rejected
4. If accepted, an event becomes canonical and is appended to canonical event history
5. derived canonical state updates via replay
6. observers reconcile correctly
7. reconnect works via snapshot + event tail

---

## 2. Non-Goals

This validator intentionally excludes:

* scalability
* anti-cheat
* distributed shards
* complex physics
* combat systems
* branch merging
* cryptographic trust
* production persistence
* account systems

> Keep it small and focused.

---

## 3. Core Runtime Loop

```text
Observer Action
→ Candidate Event
→ Invariant Boundary
→ Validation
→ Decision
→ If accepted, an event becomes canonical and is appended to canonical event history
→ Assign canonical_sequence
→ Broadcast canonical event
→ Replay
→ Observer Reconciliation
```

---

## 4. Validator Responsibility (Critical)

The validator:

* validates candidate events
* enforces invariants
* maintains canonical event history

The validator does **not**:

* simulate the world
* predict outcomes
* manage UI or experience

> The validator controls truth, not simulation. Derived canonical state is reconstructed via replay.

---

## 5. Recommended Scope

Start extremely small:

* one tile grid
* one player
* structure placement
* one resource
* one conflict case
* one reconnect path

---

## 6. Minimal Components

### Submission and Distribution Layer

Handles:

* receiving candidate events
* sending validation results
* broadcasting canonical events

(Local-first: this can be in-process)

---

### Event Intake

* parse event
* validate structure
* normalize

---

### Validation Pipeline

* schema
* identity
* preconditions
* invariants
* rules

---

### Conflict Resolver

* define conflict scope
* enforce atomic validation
* reject losing events

---

### Canonical Event History

* append-only
* assign `canonical_sequence`
* source of truth

---

### Derived Canonical State Cache

* materialized state
* updated via replay
* used for validation + queries

---

### Snapshot System

* capture state at sequence
* support reconnect

---

### Session Manager

* track observers
* track sequence
* deliver updates

---

## 7. Minimal Data Structures

### Candidate Event

* `event_id`
* `event_type`
* `actor_id`
* `target_ids`
* `payload`
* `precondition_refs`
* optional `observer_time`

---

### Canonical Event

* candidate event fields
* `canonical_event_id`
* `canonical_sequence`
* `accepted_at`

---

### Canonical Event History

* append-only ordered sequence of canonical events
* authoritative source of truth

---

### Derived Canonical State

* reconstructed via replay
* not authoritative
* used for validation and queries

---

### Validation Result

* accepted or rejected
* optional rejection reason
* canonical metadata if accepted

---

## 8. Idempotency Rule (Critical)

* each `event_id` must be processed exactly once
* duplicates must not create duplicate canonical events

If a duplicate `event_id` is received:

* return the original result (accepted or rejected)
* do not create a new canonical event
* do not modify canonical event history

---

## 9. Atomicity Requirement

Within a conflict scope:

* validation and decision must be atomic
* conflicting events must not both become canonical

---

## 10. Persistence

Minimal approach:

* append-only event log
* in-memory derived canonical state
* periodic snapshots

---

## 11. Success Criteria

The validator can be considered complete when:

* runs independently
* supports multiple observers
* validates correctly
* appends canonical events in canonical_sequence order
* updates derived canonical state via replay
* supports reconnect
* enforces idempotency

---

## 12. Development Order

1. validator process
2. event intake
3. canonical event history
4. derived canonical state
5. validation
6. broadcast
7. reconnect
8. conflict testing

---

## 13. Summary

This validator proves:

* observers do not define truth
* events must be validated
* canonical event history defines reality
* observers reconstruct via replay

---

## One Sentence Summary

CrypSA Minimal Validator v0.1 is the smallest complete implementation of the validator role, proving that if accepted, an event becomes canonical and is appended to canonical event history, and shared reality is reconstructed via deterministic replay.
