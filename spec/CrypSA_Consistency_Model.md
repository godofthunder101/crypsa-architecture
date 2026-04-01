# CrypSA Consistency Model v0.1

This document defines how CrypSA maintains consistency across observers, the validator, and canonical event history.

Consistency determines:

* how events are ordered
* how conflicts are resolved
* how observers converge on shared truth

---

## Core Principle

CrypSA does not rely on global state synchronization.

Instead:

> Consistency is achieved through agreement on canonical event history and deterministic replay.

Observers may temporarily diverge, but must eventually converge on the same canonical history.

---

## Consistency Goals

CrypSA provides:

* **Canonical Consistency**
  All observers agree on accepted canonical events

* **Replay Consistency**
  Given the same canonical event history, all observers derive the same state

* **Eventual Convergence**
  Temporary divergence is allowed, but must resolve

CrypSA does **not guarantee**:

* immediate consistency across observers
* perfectly synchronized real-time state
* zero divergence

---

## Consistency Model

CrypSA uses a hybrid consistency model:

### 1. Event-Level Authority

* The validator is authoritative over event acceptance
* Only accepted events enter canonical event history
* Canonical event history defines shared truth

---

### 2. Observer-Level Flexibility

* Observers simulate locally
* Observers may temporarily diverge
* Observers reconcile when canonical updates are received

---

### 3. Eventual Convergence

* All observers converge once canonical history is aligned
* Divergence is temporary and expected

---

## Ordering Model

### Canonical Ordering

Canonical event history is strictly ordered by:

* `server_sequence`

This ordering is:

* authoritative
* global within a validator instance
* used for replay and reconstruction

> `server_sequence` is assigned by the validator and defines canonical ordering.

---

### Scoped Reasoning (Optional)

Implementations may reason about events within scopes such as:

* per object
* per region

However:

> canonical ordering remains defined by validator-assigned sequence

---

## Conflict Model

Conflicts occur when:

* multiple candidate events target the same object or resource
* events cannot both satisfy invariants

---

### Conflict Resolution

The validator resolves conflicts during validation:

* events are evaluated atomically within the conflict scope
* only one valid outcome is accepted
* rejected events do not enter canonical event history

---

### Deterministic Resolution

Given:

* the same canonical event history
* the same candidate event
* the same validation rules

The result must be:

> identical (accept or reject)

---

## Consistency by Action Type

| Action Type      | Consistency Requirement |
| ---------------- | ----------------------- |
| Local simulation | Observer-only           |
| UI interaction   | Minimal                 |
| Canonical events | Strong (validated)      |

All canonical events require validation.

---

## Partitioning

CrypSA may partition the world into independent scopes:

* regions
* zones
* object groups

Within a partition:

* stronger consistency can be enforced

Across partitions:

* consistency may be eventual

---

## Cross-Partition Consistency

When events span partitions:

* coordination may be required
* validation may involve multiple scopes
* temporary inconsistency may occur

Possible strategies include:

* coordination protocols
* staged validation
* compensating events

---

## Observer Reconciliation

Observers reconcile when:

* canonical events differ from local prediction
* rejected events invalidate assumptions

Reconciliation may involve:

* correcting local state
* re-running simulation
* discarding invalid predictions

---

## Snapshot Consistency

Snapshots represent derived state at a specific canonical sequence.

To remain consistent:

* snapshots must correspond to a specific `server_sequence`
* replaying events after the snapshot must produce the same result as full replay

---

## Idempotency Requirement

The system must ensure:

* duplicate candidate events do not produce duplicate canonical events

Each `event_id` must be processed exactly once.

---

## Failure Modes

The system must handle:

* delayed events
* out-of-order delivery
* missing events
* conflicting submissions
* partial history

Consistency must still converge under these conditions.

---

## Tradeoffs

CrypSA prioritizes:

### Advantages

* flexible observer simulation
* reduced synchronization overhead
* scalable partitioning
* strong auditability

---

### Costs

* temporary divergence
* validation complexity
* reconciliation overhead
* cross-partition complexity

---

## Summary

CrypSA consistency is:

* event-driven
* validator-controlled
* globally ordered (by canonical sequence)
* eventually convergent

> Observers may disagree temporarily,
> but canonical event history ensures they eventually agree.

---

## One Sentence Summary

CrypSA ensures consistency through validator-controlled event acceptance, canonical ordering, and deterministic replay, allowing temporary divergence while guaranteeing eventual convergence.
