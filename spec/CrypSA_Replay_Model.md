# CrypSA Replay Model Spec v0.1

This document defines how CrypSA reconstructs world state from canonical event history.

Replay is the mechanism that turns:

* canonical events
  into
* derived world state

---

## Core Principle

In CrypSA:

> The world is not stored — it is reconstructed.

Canonical state is always derived by replaying canonical event history.

---

## Replay Overview

Replay is the process of:

1. Starting from a known base state (genesis or snapshot)
2. Applying canonical events in order
3. Producing a deterministic world state

---

## Replay Inputs

Replay requires:

* canonical event history
* authoritative ordering (`server_sequence`)
* event payloads
* invariant rules
* object definitions (genomes / mint)

---

## Replay Base

Replay can begin from:

### 1. Genesis

* empty or initial world state
* all events are applied

---

### 2. Snapshot (Recommended)

* precomputed derived state at a known sequence
* replay resumes from snapshot forward

---

## Replay Ordering

Replay order is defined by:

### Canonical Ordering

* events must be applied strictly in `server_sequence` order
* this ordering is authoritative
* all observers must use the same ordering

---

## Event Application

Each event modifies derived state according to:

* its `event_type`
* its `payload`
* the current derived state
* invariant rules

---

### Requirements

Event application must be:

* deterministic
* idempotent
* free of external side effects

Event application must only affect:

> derived state constructed from canonical event history

---

## Determinism Requirements

Replay must produce identical results given the same inputs.

This requires:

### 1. Deterministic Logic

* no randomness unless explicitly seeded
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

* genomes must be versioned or frozen
* historical events must use correct definitions

---

## Idempotency

Replay systems must tolerate repeated application attempts.

Therefore:

* canonical events must not produce different results if re-applied
* event identity must uniquely identify each event
* duplicate application must not corrupt derived state

---

## Partial Replay

Replay does not always require full history.

Possible strategies:

* replay from last snapshot
* replay a subset of events
* replay per partition or object

---

## Replay Scope

Replay can occur at different levels:

* full world replay
* region replay
* object-specific replay

This depends on system design.

---

## Observer Reconciliation

Observers use replay to reconcile:

* local predictions vs canonical state
* rejected candidate events
* late-arriving canonical events

---

### Reconciliation Process

1. receive canonical event
2. compare with local state
3. correct divergence
4. continue simulation

---

## Handling Divergence

Divergence occurs when:

* local simulation differs from canonical outcome
* events are rejected
* canonical updates arrive after local prediction

Replay ensures:

> canonical event history overrides local assumptions

---

## Snapshot Integration

Snapshots improve replay performance.

### Requirements:

* snapshot must correspond to a specific `server_sequence`
* snapshot must be reproducible from canonical event history
* replay after snapshot must produce identical results to full replay

---

## Versioning and Evolution

Replay must handle:

* evolving event schemas
* changing object definitions (genomes)

Strategies:

* versioned event types
* backward compatibility layers
* migration during replay

---

## Failure Modes

Replay systems must handle:

* missing events
* corrupted events
* inconsistent ordering
* partial snapshots

---

## Performance Considerations

Replay cost depends on:

* number of events
* complexity of event application
* frequency of snapshots

Optimization strategies:

* snapshotting
* incremental replay
* partitioned replay

---

## Security Considerations

Replay assumes:

* only canonical events are processed
* all events have already passed validation

Replay does not:

* validate events again
* trust observer-local data

---

## Summary

CrypSA replay is:

* deterministic
* event-driven
* idempotent
* reconstructive

It ensures that:

> given the same canonical event history,
> all observers derive the same world
