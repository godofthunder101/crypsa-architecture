# CrypSA Runtime Spec v0.1

## Purpose

This document defines the minimal runtime behavior of a CrypSA system.

It specifies how:
- local observer actions become candidate events  
- candidate events are validated  
- canonical truth is updated  
- observers reconcile to canonical state  

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

- observer action proposal  
- candidate event structure  
- server-side validation  
- event acceptance and rejection  
- canonical event recording  
- canonical update distribution  
- observer reconciliation  
- per-object ordering  
- snapshot-assisted reconstruction  

This v0.1 spec does **not fully define**:

- combat adjudication  
- advanced anti-cheat systems  
- distributed shard coordination  
- mergeable offline branches  
- advanced partitioning strategies  
- cryptographic trust proofs  

---

## 2. Runtime Roles

### 2.1 Observer

A process that:

- reconstructs canonical objects locally  
- simulates local experience  
- proposes candidate events  
- reconciles local state with canonical truth  

In most games, this is the client.

---

### 2.2 Canonical Server

A process that:

- receives candidate events  
- validates them  
- enforces invariants  
- records accepted canonical events  
- distributes canonical updates  

---

### 2.3 Canonical Truth Store

The persistent runtime store containing:

- canonical event log  
- object identity registry  
- genome references  
- derived canonical state  
- snapshots  

---

## 3. Core Runtime Principle

A player action does **not directly modify canonical truth**.

Instead:

---

Local Action  
→ Candidate Event  
→ Server Validation  
→ Accept or Reject  
→ Canonical Log Update  
→ Observer Reconciliation  

---

Only accepted events become canonical.

---

## 4. Event Classes

### 4.1 Local-Only Actions

Actions that do not affect canonical truth.

Examples:

- camera movement  
- visual effects  
- UI changes  
- cosmetic previews  

These never enter canonical history.

---

### 4.2 Canonical Candidate Actions

Actions that may affect canonical truth.

Examples:

- mint object  
- place structure  
- destroy structure  
- transfer ownership  
- upgrade item  
- consume resource  

These must pass validation.

---

## 5. Candidate Event Structure

Each candidate event must contain:

---

event_id  
event_type  
actor_id  
target_ids  
payload  
client_time  
branch_id  
precondition_refs  

---

### 5.1 Field Definitions

**event_id**  
Client-generated unique identifier.  

Used for:
- deduplication  
- retry safety  
- reconciliation tracking  

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

**branch_id**  
The branch/timeline context the observer is operating in.

---

**precondition_refs**  
Explicit assumptions about canonical state.

---

### 5.2 Precondition Evaluation

- All preconditions must evaluate to `true`
- Any failure → rejection

Preconditions must be:
- explicit  
- deterministic  
- verifiable  

---

## 6. Event Ordering Model

CrypSA v0.1 uses:

> server-defined canonical ordering with per-object conflict resolution

---

### 6.1 Canonical Order

- server assigns ordering  
- client order is not authoritative  

---

### 6.2 Conflict Scope

Conflicts are resolved within:

- object  
- tile  
- inventory slot  
- ownership target  

---

### 6.3 Conflict Resolution

- first valid accepted event wins  
- later conflicting events are rejected  

---

### 6.4 Atomic Validation Requirement

Validation must be atomic within the conflict scope.

---

### 6.5 No Global Strong Ordering

Only local ordering is required where invariants depend on it.

---

## 7. Validation Pipeline

Each candidate event passes through:

---

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

G --> H[Canonical Log Update]

````

---

### 7.1 Schema Validation

Reject if malformed.

---

### 7.2 Identity Validation

Reject if invalid references.

---

### 7.3 Precondition Validation

Reject if assumptions fail.

---

### 7.4 Invariant Validation

Reject if rules would be violated.

---

### 7.5 Rule Validation

Reject if event-specific rules fail.

---

### 7.6 Acceptance

If all checks pass:

* event becomes canonical
* derived state updates
* observers notified

---

### 7.7 Determinism Requirement

All accepted events must produce deterministic results.

---

## 8. Validation Outcomes

### 8.1 Accepted

* event recorded
* state updated
* observers notified

---

### 8.2 Rejected

* no canonical change
* rejection returned
* observer reconciles

---

### 8.3 Rejection Codes

* invalid_schema
* invalid_identity
* invalid_branch
* precondition_failed
* invariant_violation
* rule_violation
* conflict_lost

---

## 9. Canonical Event Recording

Append-only log.

Each event includes:

* canonical_event_id
* source_event_id
* server_sequence
* accepted_at
* branch_id

---

## 10. Derived Canonical State

Materialized view of event history.

Not independently authoritative.

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
* out-of-order events
* retries
* duplicates

---

## 14. Worked Example

See:

👉 `CrypSA_WORKED_EXAMPLE.md`

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
* canonical history defines truth
* observers reconcile

---

## One Sentence Summary

CrypSA Runtime v0.1 defines how observer actions become validated canonical events and how shared reality emerges from event-driven canonical history.
