# CrypSA Local-First Development Approach

## Purpose

This document defines the recommended development approach for building CrypSA systems.

The core idea is:

> start with a local validator, prove the architecture, then move to a remote validator later

This approach reduces implementation complexity while preserving the full CrypSA model from the start.

It is an implementation strategy, not a runtime specification.

---

## Core Principle

CrypSA defines the validator as a **role**, not a location.

Because of this, a system can begin with:

* an observer
* a validator
* canonical event history (ordered via canonical_sequence)

all running locally, while still following the real architecture.

This means:

> local-first development is not a shortcut — it is a valid CrypSA deployment.

---

## Why Local-First Matters

Building a CrypSA system directly as a networked deployment introduces multiple layers of complexity simultaneously:

* validation logic
* event flow
* replay correctness
* reconciliation
* transport and networking
* reconnection and resynchronization

A local-first approach allows these concerns to be introduced in stages.

It lets builders first prove:

* candidate events are correctly formed
* validation behaves correctly
* canonical event history is correct, append-only, and ordered via canonical_sequence
* replay produces deterministic results based on canonical ordering
* observers reconcile properly

---

## The Recommended Sequence

### Step 1 — Start with a Local Validator

Begin with a minimal local deployment:

* observer and validator in the same process or machine
* canonical event history stored locally
* replay and derived state functioning normally
* validation fully active
* invariant boundary explicitly enforced

At this stage, the goal is to prove the **actual runtime loop**, not simulate one.

You should already have:

* explicit candidate events
* explicit validation
* append-only canonical event history ordered via canonical_sequence
* deterministic replay
* observer reconciliation

---

### Step 2 — Validate the Architecture

Before introducing networking, confirm that the CrypSA model works locally.

This means proving:

* local simulation does not define truth
* candidate events cross the invariant boundary
* the validator determines accept/reject
* accepted events become canonical and are assigned canonical_sequence
* replay produces consistent derived canonical state
* rejected events correctly roll back or adjust local state
* snapshot and reconnect logic can be reasoned about

---

### Step 3 — Introduce Remote Deployment

Once the validator model is working locally, introduce a transport boundary.

This may involve:

* host-based deployment
* or a dedicated remote validator

At this stage, the architecture must remain unchanged.

What changes:

* process separation
* transport mechanism
* observer ↔ validator communication

What must not change:

* event structure
* validation semantics
* canonical event history behavior
* canonical ordering via canonical_sequence
* replay behavior
* observer reconciliation model

---

## What Must Remain Stable

A correct CrypSA implementation preserves the following across deployment changes:

* observers submit candidate events
* validator determines truth
* canonical event history remains append-only
* canonical event history remains ordered via canonical_sequence
* replay remains deterministic and ordered via canonical_sequence
* derived canonical state remains reconstructable
* invariant boundary remains explicit

If these change when moving to a remote validator:

> the architecture is drifting

---

## What Can Be Added Later

After the core system works locally, additional concerns can be layered in:

* network transport (e.g. WebSocket)
* session management
* reconnect handling
* authentication
* persistence strategies
* snapshot distribution
* multi-observer synchronization

These are **deployment concerns**, not core architecture.

They should not be introduced before the runtime model is proven.

---

## Why This Helps Builders

Local-first development isolates complexity.

It allows builders to first solve:

* truth
* validation
* replay
* reconciliation

Then later solve:

* transport
* latency
* disconnection
* distributed synchronization

This prevents architectural confusion and reduces debugging complexity.

---

## Common Mistake to Avoid

Do not treat local mode as a “fake” or simplified mode.

Examples of incorrect approaches:

* bypassing validation because everything is local
* mutating canonical state directly
* skipping replay
* ignoring canonical_sequence or relying on local ordering
* letting observer/UI logic define truth

This is not CrypSA.

A local validator must behave exactly like a real validator, including:

* enforcing invariants
* assigning canonical_sequence
* maintaining canonical event history

---

## Relationship to Other Documents

This document complements:

* `architecture/CrypSA_Validator_Deployment_Model.md`
* `implementation/CrypSA_Minimal_Validator_v0.1.md`
* `implementation/CrypSA_Local_First_Design_Pattern.md`

This document defines the **recommended development path**.

---

## Key Insight

> First prove CrypSA locally. Then move the validator, not the architecture or canonical ordering model.

---

## Summary

The recommended CrypSA development approach is:

* start with a local validator
* validate the architecture locally
* introduce remote deployment later

This keeps the truth model stable while allowing complexity to be introduced in controlled stages.

---

## One Sentence Summary

CrypSA should be built local-first: start with a real local validator, prove validation and replay locally, then move to host-based or remote deployment without changing canonical truth or canonical ordering.
