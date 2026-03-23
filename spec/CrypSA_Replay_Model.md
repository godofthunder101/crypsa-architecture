# CrypSA Replay Model Spec v0.1

This document defines how CrypSA reconstructs world state from canonical event history.

Replay is the mechanism that turns:
- canonical events  
into  
- derived world state  

---

## Core Principle

In CrypSA:

> The world is not stored — it is reconstructed.

Canonical state is always derived by replaying events.

---

## Replay Overview

Replay is the process of:

1. Starting from a known base state (genesis or snapshot)
2. Applying canonical events in order
3. Producing a deterministic world state

---

## Replay Inputs

Replay requires:

- canonical event history  
- ordering information (`lineage_parent`, sequence)  
- event payloads  
- invariant rules  
- object definitions (Genomes / Mint)  

---

## Replay Base

Replay can begin from:

### 1. Genesis

- Empty or initial world state
- All events are applied

---

### 2. Snapshot (Recommended)

- Precomputed derived state at a known point
- Replay resumes from snapshot forward

---

## Replay Ordering

Replay order is defined by:

### 1. Lineage Chain

- Events follow their `lineage_parent`
- Defines the primary replay path

---

### 2. Scoped Sequence

- `canonical_sequence` ensures ordering within a scope
- Scope may be:
  - global
  - region
  - object

---

### 3. Deterministic Application

Events must be applied in a consistent order to ensure identical results.

---

## Event Application

Each event modifies state according to:

- its `event_type`
- its `payload`
- the current state
- invariant rules

---

### Requirements

Event application must be:

- deterministic  
- side-effect controlled  
- idempotent  

---

## Determinism Requirements

Replay must produce identical results given the same inputs.

This requires:

### 1. Deterministic Logic

- no randomness unless seeded
- no time-dependent logic
- no platform-dependent variation

---

### 2. Complete Payloads

Events must include all required data.

Avoid:
- hidden dependencies
- implicit state assumptions

---

### 3. Stable Definitions

- Genomes must be versioned or frozen
- historical events must use correct definitions

---

## Idempotency

Events may be replayed multiple times.

Therefore:

- applying the same event twice must not corrupt state
- event_id must uniquely identify the event
- systems must detect duplicates

---

## Partial Replay

Replay does not always require full history.

Possible strategies:

- replay from last snapshot
- replay a subset of events
- replay per partition or object

---

## Replay Scope

Replay can occur at different levels:

- full world replay  
- region replay  
- object-specific replay  

This depends on system design.

---

## Reconciliation

Observers use replay to reconcile:

- local predictions vs canonical state
- rejected candidate events
- late-arriving canonical events

---

### Reconciliation Process

1. Receive canonical event
2. Compare with local state
3. Correct divergence
4. Continue simulation

---

## Handling Divergence

Divergence occurs when:

- local simulation differs from canonical outcome
- events are rejected
- ordering differs

Replay ensures:

> canonical history overrides local assumptions

---

## Snapshot Integration

Snapshots improve replay performance.

### Requirements:

- snapshot must correspond to a specific event position
- snapshot must be reproducible from history
- replay after snapshot must match full replay

---

## Versioning and Evolution

Replay must handle:

- evolving event schemas
- changing object definitions (Genomes)

Strategies:

- versioned event types
- backward compatibility layers
- migration during replay

---

## Failure Modes

Replay systems must handle:

- missing events
- corrupted events
- inconsistent ordering
- partial snapshots

---

## Performance Considerations

Replay cost depends on:

- number of events
- complexity of event application
- frequency of snapshots

Optimization strategies:

- snapshotting
- incremental replay
- partitioned replay

---

## Security Considerations

Replay assumes:

- only canonical events are processed
- all events have passed validation

Replay does not:
- validate events again
- trust observer-local data

---

## Summary

CrypSA replay is:

- deterministic  
- event-driven  
- idempotent  
- reconstructive  

It ensures that:

> Given the same canonical history,  
> all observers derive the same world.

---
