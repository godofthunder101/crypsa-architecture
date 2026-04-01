# CrypSA Replay Model Spec v0.1

This document defines how CrypSA reconstructs world state from canonical event history.

Replay is the mechanism that turns:

* canonical events
  into
* derived canonical state

---

## Core Principle

In CrypSA:

> The world is not stored — it is reconstructed.

Canonical state is always derived by replaying canonical event history.

---

## Replay Overview

Replay is the process of:

1. starting from a known base state (genesis or snapshot)
2. applying canonical events in order
3. producing a deterministic derived canonical state

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

* precomputed derived canonical state at a known sequence
* replay resumes from snapshot forward

---

## Replay Ordering

Replay order is defined by:

### Canonical Ordering

* events must be applied strictly in `server_sequence` order
* this ordering is authoritative
* all observers must use the same ordering

> `server_sequence` is assigned by the validator and defines canonical ordering.

---

## Event Application

Each canonical event modifies derived canonical state according to:

* its `event_type`
* its `payload`
* the current derived canonical state
* invariant rules

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

Replay must produce identical results given the same inputs.

This requires:

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

* genomes must be versioned or frozen
* historical events must resolve against correct definitions

---

## Idempotency vs Replay Safety

Replay must be safe under repeated or partial application.

---

### Requirements

* canonical events must not produce different results if applied multiple times in the same sequence position
* event identity must uniquely identify each canonical event
* replay systems must prevent duplicate application within the same sequence

---

### Clarification

Replay is not defined as arbitrary reapplication.

Instead:

> replay is deterministic application of a canonical sequence

Idempotency ensures robustness in:

* recovery
* partial replay
* distributed systems

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

---

### Requirements

* snapshot must correspond to a specific `server_sequence`
* snapshot must be reproducible from canonical event history
* replay after snapshot must produce identical results to full replay

---

## Versioning and Evolution

Replay must handle:

* evolving event schemas
* changing object definitions (genomes)

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
* validator-aligned

It ensures that:

> given the same canonical event history,
> all observers derive the same world

---

## One Sentence Summary

CrypSA replay reconstructs derived canonical state deterministically by applying canonical events in validator-defined order, ensuring consistent results across all observers.

---

## 🔍 What changed (quick review)

* Replaced **server → validator**
* Clarified **derived canonical state terminology**
* Fixed **idempotency vs replay semantics (important)**
* Strengthened **determinism guarantees**
* Tightened **event application definition**
* Improved consistency with other specs
