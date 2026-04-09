# Local-First CrypSA Design Pattern

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This document provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details may vary based on product requirements.

This document illustrates one possible way to structure a system that conforms to CrypSA.

---

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

Canonical event history must remain ordered via `canonical_sequence`, even in local deployments.

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

---

### 3. Practical Development

A local validator allows developers to:

* test the real event flow early
* validate replay and canonical event history locally
* debug the invariant boundary without networking complexity
* evolve toward multiplayer incrementally

---

## The Pattern

### Step 1 — Define the Validator Boundary

Design the system so that:

* observers propose candidate events
* a validator evaluates them
* canonical event history is updated only through validation

The invariant boundary must remain explicit, even in local execution.

---

### Step 2 — Run the Validator Locally

In the first implementation:

* the observer and validator may run in one application, but remain separate logical roles
* candidate events still flow through validation
* canonical event history is still distinct from local simulation

This is not a shortcut or reduced mode.

It is a valid CrypSA deployment.

---

### Step 3 — Keep Canonical Truth Separate from Experience

Even in a local-only implementation:

* local simulation must not directly define truth
* canonical event history must remain the source of truth
* canonical event history must never be directly mutated by local simulation
* derived canonical state must remain deterministically reconstructable by replay

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
* canonical event history remains ordered via canonical_sequence
* observers always reconcile to canonical outcomes
* replay remains deterministic
* the invariant boundary remains explicit

---

## What May Change

These things may change as the system grows:

* process boundaries
* networking transport
* event distribution mechanisms
* snapshot delivery
* authentication and security layers
* infrastructure scaling strategy

These are deployment concerns, not architectural changes.

---

## Example Progression

### Stage 1 — Local-Only Prototype

* observer and validator in one app
* local canonical event history
* replay and snapshots tested locally

---

### Stage 2 — Host-Based Multiplayer

* one observer runs the validator
* other observers connect to it
* shared canonical event history introduced

---

### Stage 3 — Dedicated Remote Validator

* validator runs independently
* observers connect over a network
* canonical truth is maintained remotely

---

## Design Rules for Local-First CrypSA

### 1. Never bypass validation just because everything is local

Even in local mode, all candidate events must pass through the invariant boundary.

---

### 2. Keep candidate events explicit

All changes to shared or canonical state must be represented as candidate events, not implicit mutations.

---

### 3. Reconstruct from canonical event history even in local mode

Replay must be deterministic and based on canonical event history ordered by canonical_sequence.

---

### 4. Keep transport replaceable

The candidate event contract and validation behavior must remain identical across transport layers.

---

### 5. Treat local validator as a first-class deployment

Local validation is not a temporary shortcut. It is a valid CrypSA deployment that should follow the same architectural rules as remote systems.

---

## Common Failure Modes

### Hidden Direct State Mutation

Problem:

* local systems mutate runtime or canonical state directly
* changes bypass candidate events and validation

Result:

* breaks invariant boundary
* introduces hidden state changes
* prevents reliable replay

---

### Local and Remote Modes Behave Differently

Problem:

* local mode bypasses validation or uses different logic
* remote mode enforces full validation

Result:

* inconsistent behavior between environments
* bugs that only appear after deployment
* loss of architectural continuity

---

### Replay Is Skipped in Local Mode

Problem:

* local systems rely on live state instead of reconstructing from canonical event history

Result:

* replay becomes unreliable or impossible
* derived canonical state diverges
* debugging becomes difficult

---

### Canonical Ordering Drift

Problem:

* local mode does not enforce canonical_sequence
* ordering differs between environments

Result:

* replay divergence
* inconsistent derived canonical state
* non-deterministic behavior

---

## Relationship to Validator Deployment Model

The local-first design pattern aligns directly with the CrypSA validator deployment model.

The validator is a role, not a location.

In a local-first system:

* the validator may run in the same process as the observer
* the invariant boundary remains explicit
* canonical event history is still produced through validation

As the system evolves:

* the validator may move to a host process
* or to a dedicated remote system

This transition does not change:

* the validation model
* the event lifecycle
* the role of the invariant boundary

Only the deployment changes. The architecture remains the same.

---

## Key Insight

> Local-first CrypSA is not about avoiding servers.
> It is about preserving the validator boundary and canonical event ordering from the start.

---

## Summary

The local-first CrypSA pattern allows systems to be built and tested without introducing architectural shortcuts.

By preserving:

* the invariant boundary
* canonical event history
* deterministic replay
* validator authority

from the beginning, the system can scale from local execution to distributed deployment without requiring structural changes.

---

## One Sentence Summary

A local-first CrypSA system starts with a local validator while preserving the full validator boundary, allowing the architecture to scale from offline or single-observer use to host-based or remote deployment without changing how canonical truth and canonical ordering are defined.
