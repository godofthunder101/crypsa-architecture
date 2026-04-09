# CrypSA Local → Remote Migration Guide

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This document provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details may vary based on product requirements.

This document illustrates one possible way to structure a system that conforms to CrypSA.

---

## Purpose

This document explains how to transition a CrypSA system from:

> a local validator → to a remote validator deployment

without changing the architecture.

The goal is to ensure that:

* the runtime model remains correct
* validation behavior remains identical
* canonical event history remains consistent
* canonical ordering remains consistent
* replay and reconciliation continue to function

This is a **deployment migration**, not an architectural change.

---

## Core Principle

> You are not changing how CrypSA works.
> You are only changing where the validator runs.

If your system behaves differently after moving to a remote validator:

> something is wrong with the implementation.

---

## Migration Overview

The transition should follow this progression:

```text
Local Validator
→ Process Separation
→ Transport Layer
→ Remote Validator
```

Each step introduces one new concern at a time.

---

## Stage 1 — Local Validator (Baseline)

**Before migrating, your system must already work locally.**

You must have:

* candidate event submission
* validation pipeline
* canonical event history (append-only, ordered via canonical_sequence)
* deterministic replay
* derived canonical state
* observer reconciliation

### Required Guarantee

```text
Same input → same canonical history (ordered via canonical_sequence) → same derived state
```

If this is not true locally:

> do not proceed to remote deployment

---

## Stage 2 — Process Separation

Split the system into two logical processes:

```text
Observer Process
Validator Process (local machine)
```

At this stage:

* communication may still be in-memory or local IPC
* no real networking yet
* validator still runs locally

### Goal

Prove that:

* observer and validator can run independently
* communication boundaries are clean
* validator does not depend on observer internals
* invariant boundary remains explicit and enforced

---

## Stage 3 — Introduce Transport

Replace direct calls with a transport layer.

Example:

```text
Observer → WebSocket → Validator
Validator → WebSocket → Observer
```

### Introduced Concepts

* message serialization
* asynchronous communication
* message ordering issues
* retries and idempotency

### Critical Requirements

You must now handle:

* out-of-order messages
* duplicate messages
* delayed messages

And critically:

* canonical ordering must only come from canonical_sequence, never from transport ordering

---

## Stage 4 — Remote Validator

Move the validator to a separate machine or environment.

```text
Observer → Network → Validator → Canonical Event History
```

At this stage:

* validator is fully remote
* multiple observers can connect
* canonical event history is shared and remains strictly ordered via canonical_sequence

---

## What Must NOT Change

The following must remain identical across all stages:

---

### 1. Event Structure

Candidate events must not change shape.

Canonical events must remain consistent.

---

### 2. Validation Behavior

Validation must produce the same result:

```text
same event + same state → same outcome
```

---

### 3. Canonical Event History

* append-only
* strictly ordered (`canonical_sequence`)
* identical regardless of deployment

---

### 4. Replay Behavior

Replay must produce identical derived state:

```text
same history (ordered via canonical_sequence) → same world
```

---

### 5. Invariant Boundary

The invariant boundary must remain explicit.

Observers must not bypass validation.

---

### 6. Observer Reconciliation

Observers must still:

* predict locally
* receive canonical updates
* reconcile differences

---

### 7. Canonical Ordering

Canonical ordering must remain defined exclusively by canonical_sequence.

---

## What Changes During Migration

Only **deployment concerns** should change.

---

### 1. Communication Method

| Local          | Remote           |
| -------------- | ---------------- |
| function calls | network messages |

---

### 2. Latency

* local: near zero
* remote: variable

Observers must tolerate delay.

---

### 3. Ordering

Transport may deliver messages:

* out of order
* late

Observers must reorder using:

```text
canonical_sequence
```

---

### 4. Reliability

You must now handle:

* retries
* dropped messages
* reconnects

---

## Common Pitfalls

---

### ❌ Changing Validation Logic

If validation changes between local and remote:

> the implementation no longer conforms to CrypSA

---

### ❌ Letting Transport Define Truth

Transport must not:

* decide ordering
* validate events
* define canonical state

---

### ❌ Letting Transport Reorder Reality

Transport delivery order must never define canonical ordering.

Only canonical_sequence defines ordering.

---

### ❌ Skipping Replay

Do not shortcut replay with direct state mutation.

Replay must remain the source of derived state.

---

### ❌ Tight Coupling Between Observer and Validator

The validator must not depend on:

* UI
* local simulation logic
* observer-specific state

---

### ❌ Assuming Ordered Delivery

Network transport is not guaranteed to be ordered.

Always rely on:

```text
canonical_sequence
```

---

## Testing the Migration

You should explicitly test:

---

### 1. Determinism

Run:

* local validator
* remote validator

Compare:

```text
canonical event history → identical  
derived state → identical  
```

---

### 2. Conflict Resolution

Submit conflicting events from multiple observers.

Verify:

* only one is accepted
* others are rejected
* results are consistent

---

### 3. Reconnect Flow

Simulate:

* disconnect
* reconnect

Verify:

* snapshot + event tail restores state
* no divergence remains

---

### 4. Idempotency

Send duplicate events.

Verify:

* only one canonical event is created

---

### 5. Ordering Integrity

Verify:

* canonical events are ordered consistently via canonical_sequence
* no transport-level ordering affects replay

---

## Migration Strategy (Recommended)

Do not jump directly to remote deployment.

Use this path:

```text
Local (single process)
→ Local (separate processes)
→ Local (transport enabled)
→ Remote validator
```

Each step should fully work before moving forward.

---

## Key Insight

> The validator moves. The architecture and canonical ordering model do not.

---

## Relationship to Other Docs

This document builds on:

* `CrypSA_Local_First_Development_Approach.md`
* `CrypSA_Minimal_Validator_v0.1.md`
* `architecture/CrypSA_Validator_Deployment_Model.md`
* `spec/` (authoritative behavior)

---

## Summary

Migrating from local to remote CrypSA is a deployment transition.

It should:

* preserve validation behavior
* preserve canonical event history
* preserve canonical ordering
* preserve replay correctness
* preserve observer reconciliation

Only transport and deployment should change.

---

## One Sentence Summary

CrypSA migration from local to remote moves the validator across a network boundary while preserving identical validation, canonical event history, canonical ordering, and replay behavior.
