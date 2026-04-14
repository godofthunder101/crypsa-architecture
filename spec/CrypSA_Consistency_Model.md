# CrypSA Consistency Model v0.1

This document defines how CrypSA maintains consistency across observers, the validator, and canonical event history.

Consistency determines:

* how events are ordered
* how conflicts are resolved
* how observers converge on shared truth

For a conceptual overview of how consistency emerges within the system runtime, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Core Principle

CrypSA does not rely on global state synchronization.

Instead:

> Consistency is achieved through agreement on canonical event history and deterministic replay.
> Canonical event history is the source of truth.

Observers may temporarily diverge, but must eventually converge on the same canonical event history.

---

> Canonical event history is the source of truth.
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## Consistency Goals

CrypSA provides:

* **Canonical Consistency**
  All observers agree on canonical events

* **Replay Consistency**
  Given the same canonical event history and the same interpretation logic, observers derive equivalent derived canonical state

* **Eventual Convergence**
  Temporary divergence is allowed, but must resolve

CrypSA does **not guarantee**:

* immediate consistency across observers
* perfectly synchronized real-time state
* zero divergence

---

## Consistency Model

This model operates within the runtime described in:

→ ../architecture/CrypSA_Runtime_Model.md

CrypSA uses validator-defined canonical consistency with observer-local flexibility.

---

### 1. Event-Level Authority

* The validator is authoritative over event acceptance
* All candidate events must cross the invariant boundary before becoming canonical
* If accepted, an event becomes canonical and is appended to canonical event history
* Canonical event history is the source of truth

---

### 2. Observer-Level Flexibility

* Observers simulate locally
* Observers may temporarily diverge
* Observers reconcile when canonical events are received

---

### 3. Eventual Convergence

* All observers converge once canonical event history is aligned
* Divergence is temporary and expected

---

## Ordering Model

### Canonical Ordering

Canonical event history is strictly ordered by:

* `canonical_sequence`

This ordering is:

* authoritative
* defined by the validator
* used for replay and reconstruction

> `canonical_sequence` defines a total canonical order across canonical events.

---

### Scoped Reasoning (Optional)

Implementations may reason about events within scopes such as:

* per object
* per region

However:

> canonical ordering remains defined by validator-assigned `canonical_sequence`.

---

## Replay Relationship

Consistency is maintained by:

* aligning canonical event history
* replaying canonical events in `canonical_sequence` order
* reconstructing equivalent derived canonical state

---

## Conflict Model

Conflicts occur when:

* multiple candidate events target the same object or resource
* events cannot both satisfy invariants

---

### Conflict Resolution

The validator resolves conflicts during validation:

* events are evaluated atomically within the relevant conflict scope
* only valid outcomes can become canonical
* If accepted, an event becomes canonical and is appended to canonical event history
* rejected events do not become canonical and do not enter canonical event history

---

### Deterministic Resolution

Given:

* the same canonical event history
* the same candidate event
* the same validation rules

the result must be:

> identical (accept or reject) given identical inputs

---

## Consistency by Action Type

| Action Type      | Consistency Requirement |
| ---------------- | ----------------------- |
| Local simulation | Observer-only           |
| UI interaction   | Minimal                 |
| Canonical events | Validator-enforced      |

All canonical events require validation.

---

## Partitioning

Implementations may partition the world into independent scopes:

* regions
* zones
* object groups

Within a partition:

* stronger coordination may be enforced

Across partitions:

* consistency may be eventual

---

## Cross-Partition Consistency

When events span partitions:

* coordination may be required
* validation may involve multiple scopes
* temporary inconsistency is expected during reconciliation

Possible strategies include:

* coordination protocols
* staged validation
* compensating events

These are implementation strategies, not core consistency requirements.

---

## Observer Reconciliation

Observers reconcile as part of the runtime model by:

* applying canonical events from canonical event history in `canonical_sequence` order
* updating derived canonical state via replay

Reconciliation may also involve:

* correcting local state
* re-running simulation
* discarding invalid predictions

---

## Snapshot Consistency

Snapshots represent derived canonical state at a specific `canonical_sequence`.

To remain consistent:

* a snapshot must correspond to a specific `canonical_sequence`
* replaying events after that snapshot must produce the same result as full replay

---

## Idempotency Requirement

The system must ensure:

* duplicate candidate events do not produce duplicate canonical events

Repeated submission of the same `event_id` must not result in more than one canonical event.

---

## Failure Modes

The system must handle:

* delayed events
* out-of-order delivery
* missing events
* conflicting submissions
* incomplete observer history (missing canonical events)

Observers must recover consistency by:

* obtaining missing canonical events
* replaying canonical event history

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
* validator-defined canonical authority
* canonically ordered
* eventually convergent

> Observers may disagree temporarily,
> but canonical event history ensures they eventually agree.

---

## One Sentence Summary

CrypSA ensures consistency through validator-controlled event acceptance, canonical ordering, and deterministic replay, allowing temporary divergence while guaranteeing eventual convergence on equivalent derived canonical state.
