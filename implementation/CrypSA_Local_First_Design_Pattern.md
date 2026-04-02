# Local-First CrypSA Design Pattern

## Purpose

This document describes a practical design pattern for building CrypSA systems **local-first**.

The idea is simple:

* start with a local validator
* keep the validator boundary explicit
* preserve the same truth model as the system grows
* later move to host-based or remote validator deployments without changing the architecture

This is a design pattern, not a runtime specification.

---

## Core Principle

> Build CrypSA around the validator boundary from the start, even when everything runs locally.

A local-first design keeps the architecture stable across different deployment stages.

This means the system can evolve from:

```text
Local Validator → Host-Based Validator → Dedicated Remote Validator
```

without redefining:

* truth
* validation
* canonical event history
* observer reconciliation

---

## Why Local-First Matters

A local-first CrypSA design has three major advantages.

### 1. Architectural Continuity

The same model works in:

* offline development
* single-observer systems
* local testing
* multiplayer expansion
* fully remote deployment

The validator remains the same role throughout.

---

### 2. Resilience

If validation can run locally, the system is less fragile under:

* network interruptions
* offline scenarios
* degraded connectivity
* partial deployment environments

This does not eliminate all networking challenges, but it avoids making the architecture depend on permanent remote connectivity from the beginning.

---

### 3. Practical Development

A local validator allows developers to:

* test the real event flow early
* validate replay and canonical event history locally
* debug the invariant boundary without networking complexity
* evolve toward multiplayer incrementally

This makes CrypSA easier to implement and verify.

---

## The Pattern

The local-first CrypSA pattern is:

### Step 1 — Define the Validator Boundary

Design the system so that:

* observers propose candidate events
* a validator evaluates them
* canonical event history is updated only through validation

This boundary must exist even if the validator runs in the same process as the observer.

---

### Step 2 — Run the Validator Locally

In the first implementation:

* the observer and validator may run in one application
* candidate events still flow through validation
* canonical event history is still distinct from local simulation

This is not a shortcut or fake mode.

It is a valid CrypSA deployment.

---

### Step 3 — Keep Canonical Truth Separate from Experience

Even in a local-only implementation:

* local simulation must not directly define truth
* canonical event history must remain the source of truth
* derived canonical state must remain reconstructable by replay

This preserves the architecture.

---

### Step 4 — Introduce Networked Deployment Later

Once the local validator model works:

* move the validator to a host process
* or move it to a dedicated remote system
* keep the same event model, validation rules, and replay model

Deployment changes.

The truth model does not.

---

## What Must Stay the Same

A system is following the local-first CrypSA pattern only if these remain stable across deployment stages:

* candidate events are always validated
* canonical event history is always the source of truth
* observers always reconcile to canonical outcomes
* replay remains deterministic
* the invariant boundary remains explicit

If these change between local and remote modes, the architecture is drifting.

---

## What May Change

These things may change as the system grows:

* process boundaries
* networking transport
* event distribution mechanisms
* snapshot delivery
* authentication and security layers
* infrastructure scaling strategy

These are deployment and implementation concerns, not changes to the core CrypSA model.

---

## Example Progression

### Stage 1 — Local-Only Prototype

* observer and validator in one app
* local canonical event history
* replay and snapshots tested locally

Useful for:

* proving the architecture
* debugging validation
* testing replay correctness

---

### Stage 2 — Host-Based Multiplayer

* one observer runs the validator
* other observers connect to it
* shared canonical event history introduced

Useful for:

* small-scale multiplayer
* LAN or cooperative testing
* early networked validation

---

### Stage 3 — Dedicated Remote Validator

* validator runs independently
* observers connect over a network
* canonical truth is maintained remotely

Useful for:

* persistent worlds
* scalable multiplayer
* infrastructure-backed deployments

---

## Design Rules for Local-First CrypSA

### 1. Never bypass validation just because everything is local

If a local build lets simulation directly modify canonical truth, it is not preserving the CrypSA model.

---

### 2. Keep candidate events explicit

Do not let local mode collapse into hidden direct state mutation.

The same candidate event structure should exist from the beginning.

---

### 3. Reconstruct from canonical event history even in local mode

Replay should be real, not simulated or faked.

This is how you verify that the architecture actually works.

---

### 4. Keep transport replaceable

Local mode may use function calls or in-process messaging.

Later modes may use network transport.

The event contract should survive both.

---

### 5. Treat local validator as a first-class deployment

Do not frame it as “temporary cheating” or “not real CrypSA.”

It is a valid deployment of the same architecture.

---

## Common Failure Modes

### Hidden Direct State Mutation

Problem:

* local prototype updates canonical state directly
* validator boundary becomes decorative

Result:

* later multiplayer migration becomes painful
* architecture is no longer truly CrypSA

---

### Local and Remote Modes Behave Differently

Problem:

* local mode accepts actions differently
* remote mode changes event semantics

Result:

* truth model forks
* bugs and conceptual drift appear

---

### Replay Is Skipped in Local Mode

Problem:

* local mode uses mutable state directly
* canonical replay is not actually exercised

Result:

* replay bugs only appear later
* architecture is not validated early

---

## Relationship to Validator Deployment Model

This design pattern is the practical application of:

* `architecture/CrypSA_Validator_Deployment_Model.md`

That document explains **what deployment models exist**.

This document explains:

> how to build in a way that can move between them cleanly

---

## Key Insight

> Local-first CrypSA is not about avoiding servers.
> It is about preserving the validator boundary from the start.

That is what makes later deployment changes architectural extensions instead of architectural rewrites.

---

## Summary

The local-first CrypSA design pattern means:

* start with a local validator
* preserve validation as the authority boundary
* keep canonical event history separate from local simulation
* scale outward without changing the truth model

This makes CrypSA easier to build, test, and evolve.

---

## One Sentence Summary

A local-first CrypSA system starts with a local validator while preserving the full validator boundary, allowing the architecture to scale from offline or single-observer use to host-based or remote deployment without changing how canonical truth is defined.
