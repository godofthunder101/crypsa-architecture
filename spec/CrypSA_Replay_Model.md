# CrypSA Replay Model Spec v0.1

This document defines how CrypSA reconstructs derived canonical state from canonical event history.

Replay is the mechanism that turns:

* canonical events
  into
* derived canonical state

---

## Core Principle

In CrypSA:

> Canonical event history is the source of truth.
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

Derived canonical state is reconstructed by replaying canonical event history.

---

## Replay Authority

Replay is authoritative for derived canonical state.

All derived canonical state must be produced via replay from canonical event history.

Any optimization must produce results equivalent to replay.

---

## Replay Overview

Replay is the process of:

1. starting from a known derived canonical state (genesis or snapshot state)
2. applying canonical events in order
3. producing a deterministic derived canonical state

---

## Replay Inputs

Replay requires:

* canonical event history
* authoritative ordering defined by `canonical_sequence`
* event payloads
* interpretation logic used to derive canonical state

---

## Replay Base

Replay can begin from:

---

### 1. Genesis

* empty or initial derived canonical state
* all events are applied

---

### 2. Snapshot (Recommended)

* precomputed derived canonical state at a known `canonical_sequence`
* replay resumes from snapshot forward

---

## Replay Ordering

Replay order is defined by:

---

### Canonical Ordering

* events must be applied strictly in `canonical_sequence` order
* no reordering is permitted
* this ordering is authoritative
* all observers must use the same ordering

> `canonical_sequence` defines a total canonical order across canonical events.

---

## Event Application

Each canonical event modifies derived canonical state according to:

* its `event_type`
* its `payload`
* the current derived canonical state
* interpretation logic

---

### Requirements

Event application must be:

* deterministic
* side-effect free (with respect to external systems)
* purely derived from canonical inputs

Event application must only affect:

> derived canonical state constructed from canonical event history

---

## Determinism Requirements

Replay must produce equivalent derived canonical state given the same:

* canonical event history
* interpretation logic

---

### 1. Deterministic Logic

* no unseeded randomness
* no time-dependent logic
* no platform-dependent variation

---

### 2. Complete Payloads

Events must include all required data.

Avoid:

* hidden dependencies
* implicit state assumptions

---

### 3. Stable Definitions

* object definitions must be versioned or frozen
* historical events must resolve against correct definitions

---

## Idempotency vs Replay Safety

Replay must be safe under repeated or partial application.

---

### Requirements

* canonical events must produce the same result when applied at the same `canonical_sequence`
* event identity must uniquely identify each canonical event
* replay systems must prevent duplicate application within the same sequence

---

### Clarification

Replay is not defined as arbitrary reapplication.

Instead:

> replay is the deterministic application of a canonical sequence

Idempotency ensures robustness in:

* recovery
* partial replay
* distributed systems

---

## Replay Scope

Replay can occur at different levels:

* full world replay
* region replay
* object-specific replay

Replay scope does not change correctness requirements.

All scoped replay must produce results equivalent to full replay for the same canonical event history subset.

---

## Partial Replay

Replay does not always require full history.

Possible strategies:

* replay from last snapshot
* replay a subset of events
* replay per partition or object

---

## Observer Reconciliation

Observers reconcile by:

* applying canonical events from canonical event history in `canonical_sequence` order
* updating derived canonical state via replay

Reconciliation may also involve:

* correcting local state
* re-running simulation
* discarding invalid predictions

---

## Handling Divergence

Divergence occurs when:

* local simulation differs from canonical outcome
* events are rejected
* canonical events arrive after local prediction

Replay ensures:

> canonical event history overrides local assumptions

---

## Snapshot Integration

Snapshots improve replay performance.

---

### Requirements

* snapshot must correspond to a specific `canonical_sequence`
* snapshot must be reproducible from canonical event history via deterministic replay
* replay after snapshot must produce identical results to full replay

---

## Versioning and Evolution

Replay must handle:

* evolving event schemas
* changing object definitions

---

### Strategies

* versioned event types
* backward compatibility layers
* explicit migration events

---

## Failure Modes

Replay systems must handle:

* missing events
* corrupted events
* inconsistent ordering
* partial snapshots

Recovery from failure requires:

* restoring canonical event history
* replaying canonical events to reconstruct derived canonical state

---

## Performance Considerations

Replay cost depends on:

* number of events
* complexity of event application
* frequency of snapshots

---

### Optimization Strategies

* snapshotting
* incremental replay
* partitioned replay

---

### Correctness Requirement

All replay optimizations must preserve correctness.

Optimized replay must produce results equivalent to full replay from canonical event history.

---

## Security Considerations

Replay assumes:

* only canonical events are processed
* all events have already passed validation

Replay does not:

* perform validation again
* trust observer-local data

---

## Summary

CrypSA replay is:

* deterministic
* event-driven
* reconstructive
* validator-defined canonical ordering

It ensures that:

> given the same canonical event history and the same interpretation logic,
> all observers derive equivalent derived canonical state

---

## One Sentence Summary

CrypSA replay reconstructs derived canonical state deterministically by applying canonical events in validator-defined order, ensuring consistent results across all observers.
