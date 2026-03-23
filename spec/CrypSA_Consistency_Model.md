# CrypSA Consistency Model v0.1

This document defines how CrypSA maintains consistency across observers, the server, and canonical history.

Consistency determines:
- how events are ordered
- how conflicts are resolved
- how multiple observers converge on the same reality

---

## Core Principle

CrypSA does not require global state synchronization.

Instead:

> Consistency is achieved through canonical event agreement and replay.

Observers may temporarily diverge, but must eventually converge on the same canonical history.

---

## Consistency Goals

CrypSA aims to provide:

- **Canonical Consistency**  
  All observers agree on accepted canonical events

- **Replay Consistency**  
  Given the same event history, all observers derive the same state

- **Eventual Convergence**  
  Temporary divergence is allowed, but must resolve

CrypSA does **not guarantee**:

- full real-time synchronization  
- global total ordering across all events  
- immediate consistency across all observers  

---

## Consistency Model

CrypSA follows a hybrid consistency approach:

### 1. Event-Level Authority

- The server is authoritative over which events are accepted
- Only canonical events define shared truth

---

### 2. Observer-Level Flexibility

- Observers simulate locally
- Observers may temporarily diverge
- Observers reconcile when canonical events are received

---

### 3. Eventual Convergence

- All observers converge once canonical history is aligned
- Divergence is temporary and expected

---

## Ordering Model

CrypSA does not enforce a single global ordering.

Instead, ordering is defined through:

---

### Lineage Ordering

- Each event references a `lineage_parent`
- Defines replay sequence for a chain of events

---

### Scoped Sequencing

Events may be ordered within a defined scope:

- per object
- per region
- per shard

Implementation may choose the scope.

---

### Causal Relationships

- `causal_references` link related events
- Provide context but do not enforce ordering

---

## Conflict Model

Conflicts occur when:

- multiple events target the same object or resource
- events cannot both satisfy invariants

---

### Conflict Resolution

CrypSA resolves conflicts through validation:

- server evaluates candidates
- only one valid outcome is accepted
- rejected events do not enter canonical history

---

### Deterministic Resolution

Where possible:

- conflict outcomes should be deterministic
- consistent rules should produce consistent results

---

## Consistency Levels by Action

Different actions require different consistency guarantees:

| Action Type            | Consistency Model              |
|-----------------------|--------------------------------|
| Local movement        | None (observer-only)           |
| UI interaction        | Minimal                        |
| Object placement      | Strong within scope            |
| Item transfer         | Strong within scope            |
| Critical actions      | Strict validation required     |

---

## Partitioning

CrypSA may partition the world into independent scopes:

- regions
- zones
- object groups

Within a partition:
- stronger consistency can be enforced

Across partitions:
- consistency may be eventual

---

## Cross-Partition Consistency

When events span partitions:

- coordination may be required
- validation may involve multiple scopes
- temporary inconsistency may occur

Strategies may include:

- coordination protocols
- staged validation
- compensating events

---

## Reconciliation

Observers reconcile when:

- canonical events differ from local state
- rejected events invalidate local assumptions

Reconciliation may involve:

- correcting local state
- re-running simulation
- discarding invalid predictions

---

## Snapshot Consistency

Snapshots represent derived state at a point in history.

To remain consistent:

- snapshots must correspond to a specific event position
- replay from snapshot must produce the same result as full replay

---

## Failure Modes

Consistency systems must handle:

- delayed events
- out-of-order events
- missing events
- conflicting submissions
- partial history

---

## Tradeoffs

CrypSA’s consistency model prioritizes:

### Advantages

- flexibility in client simulation  
- reduced need for full synchronization  
- scalable partitioning  
- strong auditability  

---

### Costs

- temporary divergence  
- more complex validation design  
- reconciliation overhead  
- complexity in cross-partition coordination  

---

## Summary

CrypSA consistency is:

- event-driven  
- server-validated  
- eventually convergent  
- scoped rather than globally strict  

> Observers may disagree temporarily,  
> but canonical history ensures they eventually agree.

---
