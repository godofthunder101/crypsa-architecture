# CrypSA Runtime Spec v0.1

## Purpose

This document defines the minimal runtime behavior of a CrypSA system.

It specifies how:

* local observer actions become candidate events
* candidate events are validated
* canonical truth is updated
* observers reconcile to canonical state

This is the minimum runtime contract required for CrypSA to be:

> technically reviewable and implementable

This is not a full production protocol.

---

## Visual Overview

For a high-level flow of the runtime:

👉 see `diagrams/CrypSA_Event_Flow.md`

---

## 1. Scope

This v0.1 runtime spec covers:

* observer action proposal
* candidate event structure
* server-side validation
* event acceptance and rejection
* canonical event recording
* canonical update distribution
* observer reconciliation
* snapshot-assisted reconstruction

This v0.1 spec does **not fully define**:

* combat adjudication
* advanced anti-cheat systems
* distributed shard coordination
* mergeable offline branches
* advanced partitioning strategies
* cryptographic trust proofs

---

## 2. Runtime Roles

### 2.1 Observer

A process that:

* reconstructs canonical objects locally
* simulates local experience
* proposes candidate events
* performs observer reconciliation

---

### 2.2 Canonical Server

A process that:

* receives candidate events
* validates them
* enforces invariants
* records accepted canonical events
* distributes canonical updates

The server does **not**:

* simulate the world
* predict outcomes
* control user experience

> The server controls truth, not simulation.

---

### 2.3 Canonical Truth Store

The persistent runtime store containing:

* canonical event history
* object identity registry
* genome references
* derived state (materialized view)
* snapshots

Canonical truth is defined by:

> canonical event history, not derived state

---

## 3. Core Runtime Principle

A player action does **not directly modify canonical truth**.

Instead:

```text
Local Action
→ Candidate Event
→ Server Validation
→ Accept or Reject
→ Canonical Event History Update
→ Observer Reconciliation
```

Only accepted events become canonical.

---

## 4. Event Classes

### 4.1 Local-Only Actions

Actions that do not affect canonical truth.

Examples:

* camera movement
* visual effects
* UI changes
* cosmetic previews

These never enter canonical event history.

---

### 4.2 Canonical Candidate Actions

Actions that may affect canonical truth.

Examples:

* mint object
* place structure
* destroy structure
* transfer ownership
* upgrade item
* consume resource

These must pass validation.

---

## 5. Candidate Event Structure

Each candidate event must contain:

```text
event_id
event_type
actor_id
target_ids
payload
client_time
precondition_refs
```

---

### 5.1 Field Definitions

**event_id**
Client-generated unique identifier.

Used for:

* idempotency
* retry safety
* reconciliation tracking

---

**event_type**
Defines the action.

---

**actor_id**
Canonical identity of acting entity.

---

**target_ids**
Canonical objects affected.

---

**payload**
Event-specific data describing the proposed state transition.

---

**client_time**
Client-local timestamp. Not authoritative.

---

**precondition_refs**
Explicit assumptions about canonical state.

---

### 5.2 Precondition Evaluation

* all preconditions must evaluate to `true`
* any failure → rejection

Preconditions must be:

* explicit
* deterministic
* verifiable

---

## 6. Event Ordering Model

CrypSA v0.1 uses:

> server-defined canonical ordering with scoped conflict resolution

---

### 6.1 Canonical Order

* server assigns `server_sequence`
* `server_sequence` defines authoritative ordering
* client order is not authoritative

---

### 6.2 Conflict Scope

Conflicts are resolved within:

* object
* tile
* inventory slot
* ownership target

---

### 6.3 Conflict Resolution

* first valid accepted event wins
* later conflicting events are rejected

---

### 6.4 Atomic Validation Requirement

Validation must be atomic within the conflict scope.

---

## 7. Validation Pipeline

Each candidate event passes through:

```mermaid
flowchart TD

A[Candidate Event] --> B[Schema Validation]

B -->|Fail| R1[Reject: invalid_schema]
B -->|Pass| C[Identity Validation]

C -->|Fail| R2[Reject: invalid_identity]
C -->|Pass| D[Precondition Validation]

D -->|Fail| R3[Reject: precondition_failed]
D -->|Pass| E[Invariant Validation]

E -->|Fail| R4[Reject: invariant_violation]
E -->|Pass| F[Rule Validation]

F -->|Fail| R5[Reject: rule_violation]
F -->|Pass| G[Accept Event]

G --> H[Canonical Event History Update]
```

---

## 7.7 Determinism Requirement

All accepted events must produce deterministic results.

---

## 8. Validation Outcomes

### Accepted

* event recorded
* derived state updated
* observers notified

---

### Rejected

* no canonical change
* rejection returned
* observer reconciles

---

### Rejection Codes

* invalid_schema
* invalid_identity
* precondition_failed
* invariant_violation
* rule_violation
* conflict_lost

---

## 9. Canonical Event Recording

Canonical event history is append-only.

Each event includes:

* canonical_event_id
* source_event_id
* server_sequence
* accepted_at

---

## 10. Derived State

Derived state is:

* a materialized view of canonical event history
* not independently authoritative

---

## 11. Snapshots

### Purpose

* reduce replay cost
* enable recovery

---

### Reconstruction Rule

> Snapshot + Event Tail → Current State

---

## 12. Observer Reconciliation

Observers must:

* detect accepted/rejected events
* correct local state
* rebuild from canonical truth

---

## 13. Networking Assumptions

System must handle:

* delays
* out-of-order delivery
* retries
* duplicates

---

## 14. Idempotency Requirement

The system must ensure:

* duplicate `event_id` submissions
* do not create duplicate canonical events

Each event must be processed exactly once.

---

## 15. Applicability

Best for:

* persistent worlds
* auditable systems

Not suited for:

* twitch combat
* physics-heavy simulation

---

## 16. v0.1 Non-Goals

Not defined:

* anti-cheat
* sharding
* cryptographic trust
* branch merging

---

## 17. Summary

CrypSA runtime:

* observers simulate locally
* server validates events
* canonical event history defines truth
* observers reconcile

---

## One Sentence Summary

CrypSA Runtime v0.1 defines how observer actions become validated canonical events and how shared reality emerges from event-driven canonical event history.
