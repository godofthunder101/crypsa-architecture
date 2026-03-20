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
Client-local timestamp.  
Not authoritative.

---

**branch_id**  
The branch/timeline context the observer is operating in.

---

**precondition_refs**  
Explicit assumptions about canonical state.

Examples:

- tile is empty  
- actor owns object  
- item exists  
- resource is available  

---

### 5.2 Precondition Evaluation

Preconditions are evaluated as **boolean assertions** against canonical state.

- All preconditions must evaluate to `true`
- If any precondition fails → event is rejected

Preconditions must be:
- explicit  
- deterministic  
- verifiable from canonical state  

---

## 6. Event Ordering Model

CrypSA v0.1 uses:

> server-defined canonical ordering with per-object conflict resolution

---

### 6.1 Canonical Order

- The server assigns authoritative ordering
- Client submission order is not authoritative

---

### 6.2 Conflict Scope

Conflicts are resolved within a defined scope:

- object  
- tile  
- inventory slot  
- ownership target  

---

### 6.3 Conflict Resolution

- First valid accepted event wins  
- Later conflicting events are rejected  

---

### 6.4 Atomic Validation Requirement

Validation must be **atomic within the conflict scope**.

The server must ensure:

- no two conflicting events are accepted simultaneously  
- validation operates on a consistent view of canonical state  

---

### 6.5 No Global Strong Ordering

CrypSA does not require global total ordering.

Ordering is only required where invariants depend on it.

---

## 7. Validation Pipeline

Each candidate event passes through:

---

### 7.1 Schema Validation

Reject if:
- missing fields  
- invalid types  
- malformed payload  

---

### 7.2 Identity Validation

Reject if:
- actor does not exist  
- target does not exist  
- invalid branch  

---

### 7.3 Precondition Validation

Reject if:
- any precondition evaluates to false  

---

### 7.4 Invariant Validation

Reject if event would violate:

- uniqueness constraints  
- ownership rules  
- spatial rules  
- impossible states  

---

### 7.5 Rule Validation

Event-specific rules:

- resource requirements  
- upgrade paths  
- permissions  
- genome constraints  

---

### 7.6 Acceptance

If all checks pass:

- event is accepted  
- event enters canonical history  
- derived state updates  
- observers are notified  

---

### 7.7 Determinism Requirement

All accepted events must produce **deterministic state transitions**.

Given the same canonical history:

> all observers must derive identical state

---

## 8. Validation Outcomes

### 8.1 Accepted

Server:

- assigns canonical metadata  
- appends event to log  
- updates derived state  
- broadcasts update  

---

### 8.2 Rejected

Server:

- returns rejection result  
- does not modify canonical state  
- provides rejection reason  

Observer must reconcile.

---

### 8.3 Rejection Codes

Minimum set:

- invalid_schema  
- invalid_identity  
- invalid_branch  
- precondition_failed  
- invariant_violation  
- rule_violation  
- conflict_lost  

---

## 9. Canonical Event Recording

Accepted events are stored in an append-only log.

Each event includes:

---

canonical_event_id
source_event_id
server_sequence
accepted_at
branch_id
validation_result = accepted

---

Historical correction occurs via new events or branching.

---

## 10. Derived Canonical State

Derived state is a **materialized view of canonical history**.

It is:

- not independently authoritative  
- always reconstructable from events  
- used for performance and validation  

Examples:

- ownership  
- inventory  
- world state  
- structure placement  

---

## 11. Snapshots

Snapshots are first-class runtime features.

---

### 11.1 Purpose

- reduce replay cost  
- support late join  
- enable fast recovery  
- assist debugging  

---

### 11.2 Contents

- branch identifier  
- canonical sequence position  
- derived state (scoped)  
- object registry  

---

### 11.3 Reconstruction Rule

---

Snapshot + Event Tail → Current State

---

---

## 12. Observer Reconciliation

Observers must reconcile when canonical updates arrive.

---

### 12.1 Match Case

- confirm local state  
- clear pending markers  

---

### 12.2 Divergence Case

- correct local state  
- remove invalid objects  
- rebuild from canonical truth  

---

### 12.3 Minimum Requirements

Observers must:

- track proposal outcomes  
- rebuild affected objects  
- update UI and simulation  

---

## 13. Networking Assumptions (v0.1)

CrypSA v0.1 assumes:

- events may be delayed  
- events may arrive out of order  
- clients may retry submissions  
- duplicate submissions may occur  

System must ensure:

- idempotency via `event_id`  
- correct reconciliation regardless of delivery timing  

---

## 14. Worked Example: Structure Placement

### 14.1 Local Action

Observer attempts to place `mining_station` on `tile_42`.

---

### 14.2 Candidate Event

---

event_type = place_structure
actor_id = player_A
target_ids = [tile_42]
payload = { structure_type: mining_station }
precondition_refs = { tile_42_empty: true }
branch_id = main

---

---

### 14.3 Server Validation

Checks:

- actor exists  
- tile exists  
- tile empty  
- placement valid  
- resources available  

---

### 14.4 Accepted Path

- event appended  
- tile updated  
- resources consumed  
- observers notified  

---

### 14.5 Rejected Path

- event rejected  
- no canonical change  
- observer removes local prediction  

---

## 15. Applicability

Best suited for:

- persistent worlds  
- auditable systems  
- object-driven simulation  
- replayable systems  

Not suited (v0.1):

- twitch combat  
- frame-perfect PvP  
- heavy physics simulation  

---

## 16. v0.1 Non-Goals

Not defined:

- anti-cheat protocols  
- shard coordination  
- cryptographic validation  
- branch merging  
- deterministic combat  

---

## 17. Summary

CrypSA v0.1 runtime:

- observers simulate locally  
- actions become candidate events  
- server validates events  
- accepted events define canonical truth  
- observers reconcile via event updates  

---

## One Sentence Summary

CrypSA Runtime v0.1 defines how observer actions become validated canonical events, how those events are recorded and ordered, and how observers reconstruct and reconcile shared event-driven truth.
```

Tht’s the hard part.
