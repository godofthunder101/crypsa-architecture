# CrypSA Lens Model

## Purpose

This document defines the role of **lenses** in a CrypSA system.

Lenses are the mechanism by which observers interpret canonical reality into local experience.

They help explain how CrypSA separates:

- canonical truth  
from  
- observer-visible experience  

---

## Core Principle

In CrypSA:

> canonical history defines what is real  
> lenses define how that reality is interpreted locally

A lens does not create canonical truth.

A lens interprets canonical truth for a specific observer, system, or experience layer.

---

## Why Lenses Exist

CrypSA separates:

- **what happened**
- **how that is experienced**

This matters because the same canonical world may need to be interpreted differently depending on:

- the observing player
- local simulation needs
- presentation needs
- gameplay context
- partial information or visibility rules

Lenses allow this interpretation to happen without changing canonical truth.

---

## What a Lens Is

A lens is a local interpretation layer that transforms canonical state and canonical events into observer-usable state.

In practical terms, a lens may:

- filter canonical information
- derive local gameplay state
- shape what an observer can see
- transform canonical objects into presentation-ready structures
- support gameplay-specific interpretation

---

## What a Lens Is Not

A lens is **not**:

- a source of canonical truth
- a replacement for validation
- a way to bypass invariants
- a server-authoritative decision system
- a mutation of canonical history

Lenses interpret reality.

They do not define it.

---

## Inputs to a Lens

A lens may consume one or more of the following:

- canonical event history
- derived canonical state
- observer identity
- observer-local state
- gameplay context
- visibility or access rules

The exact inputs depend on the type of lens.

---

## Outputs of a Lens

A lens produces observer-usable interpretation.

Examples:

- filtered object state
- visible world state
- gameplay-specific derived information
- UI-ready structures
- simulation-ready local representations

---

## Where Lenses Run

In CrypSA v0.1, lenses are primarily an **observer-side concept**.

They usually run on the client or local observer process.

This means:

- canonical truth is produced by the server
- lenses interpret that truth locally

Future systems may use lens-like logic elsewhere, but that is not required for v0.1.

---

## Relationship to Observers

Observers are not passive receivers of state.

They:

- reconstruct canonical history
- simulate locally
- interpret the world through lenses

This means a CrypSA observer is effectively:

> canonical reconstruction + local simulation + lens-based interpretation

---

## Why Lenses Matter

Without lenses, CrypSA would still have:

- canonical events
- canonical state
- validation
- replay

But it would not clearly explain how observers turn canonical reality into:

- local gameplay
- visibility models
- presentation logic
- player-specific experience

Lenses make that step explicit.

---

## Example Lens Roles

Examples of lens behavior include:

### 1. Visibility Lens

Determines what an observer can currently perceive.

Examples:
- fog of war
- hidden objects
- line-of-sight filtering
- player-specific information access

---

### 2. Presentation Lens

Transforms canonical state into rendering-ready data.

Examples:
- animations
- UI markers
- visual highlighting
- audio cues

---

### 3. Gameplay Lens

Builds local gameplay interpretation from canonical truth.

Examples:
- interactable objects
- local control context
- tactical overlays
- simulation-specific derived state

---

### 4. Debug / Inspection Lens

Provides alternate representations for tools or debugging.

Examples:
- event lineage view
- canonical diff view
- validation failure overlays
- object provenance inspection

---

## Lens and Canonical Truth

A lens must never be mistaken for canonical truth.

For example:

- a visibility lens may hide an object locally
- but the object still exists canonically

Or:

- a gameplay lens may highlight an object as interactable
- but that does not make the interaction valid until validated

This is the key separation:

> lenses shape interpretation  
> validation shapes reality

---

## Lens and Reconciliation

When canonical truth changes, lens outputs may also need to change.

This means lenses participate indirectly in reconciliation.

Example:
- canonical event changes ownership
- observer reconstructs new state
- lens recalculates what is visible or interactable
- player experience updates

So while lenses do not reconcile canonical truth themselves, they must respond to reconciliation.

---

## Lens and Determinism

Lenses do not need to define canonical truth, but they should still be designed carefully.

For gameplay-critical observer behavior, lens behavior should be:

- consistent
- understandable
- reproducible where needed

Presentation-only lenses can be more flexible.

Canonical correctness, however, must never depend on lens output alone.

---

## Lens Categories

A useful way to think about lenses is by category.

### Canonical Interpretation Lens
Transforms canonical state into observer-usable structures.

### Visibility Lens
Determines what is exposed to an observer.

### Presentation Lens
Shapes the rendered/player-facing experience.

### Tooling Lens
Supports debugging, editing, inspection, or replay tools.

These categories may overlap in practice.

---

## Lens Boundaries

A good lens should:

- consume canonical or observer-local input
- produce interpreted output
- avoid mutating canonical truth directly

A lens should not:

- decide event validity
- enforce invariants on behalf of the server
- write to canonical history

Those responsibilities belong elsewhere.

---

## Minimal Lens Model (v0.1)

At minimum, a CrypSA lens can be understood as:

```text
Canonical State + Observer Context → Interpreted Local View
````

This is the simplest useful definition.

---

## Example

Canonical reality:

* tile_42 contains mining_station
* player_A owns it
* player_B does not

Lens outputs may differ:

### Observer A Lens

* shows mining_station as owned and interactable

### Observer B Lens

* shows mining_station as visible but not controllable

### Debug Lens

* shows mining_station with ownership metadata and event provenance

The canonical truth is the same in all cases.

The interpretation differs.

---

## Relationship to Other CrypSA Concepts

### Lenses vs Observers

Observers use lenses to interpret the world.

### Lenses vs Invariants

Invariants define what is allowed to become real.
Lenses do not override them.

### Lenses vs Canonical Events

Events define world change.
Lenses interpret the results of that change.

### Lenses vs Derived State

Derived state may be an input to lenses.
Lens output is not itself canonical derived state.

---

## Why This Concept Matters

Lenses are one of the mechanisms that make CrypSA more flexible than a simple event log plus replay model.

They allow:

* observer-specific world views
* richer local gameplay interpretation
* separation of truth from presentation
* tooling and debugging layers
* extensible client-side architecture

---

## Current Status

Lenses are part of the CrypSA architecture and are already reflected in the teaching prototype.

However, the exact taxonomy and implementation patterns for lenses may still evolve over time.

For v0.1, the key point is:

> Lenses are real architectural components, not just abstract language.

---

## Summary

In CrypSA, lenses are local interpretation layers that transform canonical reality into observer-specific experience.

They do not define truth.

They define how truth is seen, understood, and used locally.

---

## One Sentence Summary

A CrypSA lens is an observer-side interpretation layer that turns canonical state and history into local gameplay, visibility, presentation, or tooling views without changing canonical truth.
