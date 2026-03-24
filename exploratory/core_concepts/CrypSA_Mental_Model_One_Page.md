# CrypSA Mental Model (One Page)

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document provides a concise mental model for understanding CrypSA.

It is intended as a **simplified conceptual overview**, not a full description of the architecture.

---

## The Core Idea

CrypSA separates:

* local observer experience
* canonical event history

Observers simulate the world locally, but only validated events can change the shared universe.

```text
Local Simulation
      ↓
Invariant Boundary Check
      ↓
Validation
      ↓
Canonical Event History Updated
      ↓
Observers Reconstruct
````

---

## A Simple Conceptual Model

CrypSA can be understood through a small set of key ideas.

This is a learning model, not the full architectural structure.

---

### 1. Observers

An observer is any system that reconstructs and experiences the universe.

Examples:

* players
* AI agents
* tools
* replay systems

Observers simulate locally.

---

### 2. Identity

Every canonical object has a unique identity.

Identity answers:

> What object is this?

Identity does not change.

---

### 3. Genome

A genome defines the structure and rules of an object.

It describes:

* valid states
* allowed interactions
* structural constraints

---

### 4. Invariants

Invariants are rules that must remain true in canonical event history.

Examples:

* objects cannot duplicate illegally
* ownership must remain consistent
* invalid states are not allowed

---

### 5. Events

Events represent proposed changes to canonical event history.

Examples:

* building
* transferring ownership
* crafting

Events must be validated before becoming canonical.

---

## The Invariant Boundary

The invariant boundary determines:

> Does this interaction affect canonical event history?

* No → remains local
* Yes → becomes a candidate event

---

## Validation

When an event crosses the boundary:

* the server validates it
* invariants are enforced

Result:

* accepted → canonical event history updated
* rejected → local simulation corrected

---

## Canonical Evolution

The universe evolves through validated events:

```text
Sₙ → Event → Sₙ₊₁
```

---

## Observer Reconstruction

Observers rebuild the world from canonical data:

```text
Identity + Genome + Canonical Event History → World State
```

This allows consistent shared reality.

---

## The CrypSA Loop

```text
Reconstruct
→ Simulate
→ Interact
→ Boundary Check
→ Validate
→ Update Canonical Event History
→ Reconstruct
```

---

## Relationship to Architecture

This simplified model maps to the full architecture:

* **Truth** → canonical events and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → local simulation and UI

This document focuses on conceptual understanding rather than full structure.

---

## Why CrypSA Works

CrypSA avoids centralized continuous simulation.

Instead:

* observers simulate locally
* only meaningful changes are validated
* canonical event history records evolution
* reconstruction ensures consistency

---

## Key Insight

> CrypSA allows local freedom while protecting shared reality through validation of canonical event history.

---

## One Sentence Summary

CrypSA is an architecture where observers simulate locally, but only validated events that respect invariant rules are allowed to become part of canonical event history and shape the shared universe.
and we start building the system.
```
