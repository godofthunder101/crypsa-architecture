# CrypSA in 5 Minutes

This is a quick mental model for understanding CrypSA.

If you only read one document, read this.

---

Before reading this, you should have seen:
→ CrypSA_In_One_Diagram.md

This document explains the same system in words.

---

## The Core Idea

CrypSA is a system where:

* nothing is true until it is validated
* truth is stored as a sequence of events
* all state is derived from those events

In CrypSA:

* **observers** simulate locally
* actions are proposed as **candidate events**
* a **validator** evaluates those events
* If accepted, an event becomes canonical and is appended to canonical event history

> Canonical event history is the source of truth.

---

## The Event Flow

Everything in CrypSA follows this flow:

1. An observer simulates locally
2. The observer proposes a **candidate event**
3. The **validator** checks invariants
4. If accepted, an event becomes canonical and is appended to canonical event history
5. canonical events are replayed to reconstruct derived canonical state
6. observers reconcile to derived canonical state

This is the boundary between:

* local possibility
* canonical reality

---

## The Validator

The validator is responsible for:

* accepting or rejecting candidate events
* enforcing invariants
* determining whether an event becomes canonical
* maintaining canonical event history

> The validator defines what becomes canonical.

Importantly:

> the validator is a role, not a location

It may run:

* **locally**, alongside an observer
* **remotely**, as a shared system

This means the truth model remains stable even when deployment changes.

A system can begin with a **local validator** and later move to a **remote validator** without changing its architecture.

---

## 📊 Core Mental Model (Visual)

```mermaid
flowchart LR

subgraph Truth Layer
A[Canonical Event History]
B[Derived Canonical State]
end

subgraph Translation
C[Adapters]
end

subgraph Interpretation
D[Lenses]
end

subgraph Experience
E[UI and Observer Experience]
F[Local Simulation]
end

A --> B
B --> C
C --> D
D --> E
```

---

## The Mental Model

Think of CrypSA like this:

* the validator determines what becomes canonical
* observers simulate what they think is happening
* only validated events become part of canonical event history
* everything else is local prediction

The system is easiest to understand as **four separate responsibilities**.

---

## The Four Responsibilities

---

### 1. Truth

This is the canonical layer.

It includes:

* canonical event history
* validation
* canonical ordering (`canonical_sequence`)
* derived canonical state via replay

This layer defines what is real.

If something is not part of canonical event history:

> it did not happen

This is where the validator operates.

---

### 2. Translation

This is the adapter layer.

Adapters:

* reshape canonical and observer data
* prepare structured outputs

They do not define truth.

They answer:

> “How should this data be structured?”

---

### 3. Interpretation

This is the lens layer.

Lenses:

* interpret translated data
* define meaning for an observer
* determine relevance and context

They do not define truth.

They answer:

> “What does this mean for this observer?”

---

### 4. Experience

This is what the player directly interacts with.

It includes:

* UI
* rendering
* local feedback
* local simulation and prediction

This layer is:

* fast
* responsive
* immediate

But:

> nothing here becomes canonical automatically

---

## Derived State

> Derived canonical state is a projection of canonical event history. It is not the source of truth.
> Derived canonical state is reconstructed via replay.

---

## Determinism

Given the same:

* canonical event history
* interpretation logic

all observers derive equivalent derived canonical state via replay.

---

## Local and Remote Validation

CrypSA does not require validation to be remote.

A validator may run locally, remotely, or transition between them.

### Resilience

A local validator enables:

* offline operation
* degraded connectivity handling
* local-first development

### Portability

Designing around a validator boundary allows easy transition between:

* local validation
* host-based validation
* remote validation

> The truth model remains stable even as deployment changes.

---

## What This Changes

Traditional systems often combine:

* simulation
* validation
* rendering

CrypSA separates them:

* **truth is defined by canonical event history**
* **validation determines what becomes canonical**
* **translation structures data**
* **interpretation defines meaning**
* **experience remains local and responsive**

---

## Why This Matters

This separation makes systems easier to:

* reason about
* debug
* persist
* replay
* evolve without breaking boundaries

It also enables:

* offline-first development
* migration between deployment models
* resilience during connectivity issues

---

## What CrypSA Is Not

CrypSA is not:

* a replacement for all multiplayer systems
* a solution for every type of game
* a way to eliminate latency

It is a way of structuring:

* authority
* validation
* interpretation
* shared system behavior

---

## Where It Fits

CrypSA works best when:

* actions are discrete
* history matters
* persistence matters

Examples:

* building systems
* crafting systems
* economic systems
* sandbox worlds

---

## Where It Fits Less Well

CrypSA is not ideal for:

* twitch shooters
* high-frequency combat
* physics-heavy PvP

---

## If You Understand This, You Understand CrypSA

* events become canonical only after validation
* canonical event history is the source of truth
* derived canonical state is reconstructed via replay
* observers simulate locally and reconcile
* the validator defines what becomes canonical
