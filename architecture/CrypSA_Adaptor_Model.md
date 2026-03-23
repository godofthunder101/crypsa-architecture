# CrypSA Adapter Model

## Purpose

This document defines the role of **adapters** in a CrypSA system.

Adapters are responsible for shaping runtime data into forms that can be safely consumed by:

- lenses  
- UI modules  
- tooling layers  

They exist to preserve separation between:

- runtime meaning  
- interpretation  
- presentation  

---

## Core Principle

In CrypSA:

> adapters translate data  
> lenses interpret data  
> the runtime defines truth  

Adapters do not define behavior or truth.

They make data usable across boundaries.

---

## Why Adapters Exist

CrypSA introduces multiple layers:

- canonical event history  
- derived canonical state  
- observer-local state  
- lenses (interpretation layers)  
- UI and tooling  

Without adapters:

- lenses would access raw runtime state directly  
- lenses would depend on each other’s internal structure  
- UI modules would become tightly coupled to runtime data  
- interpretation logic would spread across the system  

Adapters prevent this by acting as **controlled translation boundaries**.

---

## What the Teaching Prototype Confirmed

The teaching prototype demonstrated that adapters are not optional structure.

They are necessary to prevent:

- lens-to-lens coupling  
- UI/runtime entanglement  
- controller sprawl  
- interpretation logic leaking into data access  

In practice:

- adapters allowed multiple UI panels to coexist without shared assumptions  
- adapters prevented lenses from depending on raw runtime internals  
- adapters made it possible to refactor runtime structures without breaking UI or interpretation  

This confirmed that adapters are a **practical architectural boundary**, not just a conceptual one.

---

## What an Adapter Is

An adapter is a **pure or near-pure translation layer** that:

- takes structured runtime or canonical data  
- reshapes or aggregates it  
- outputs data tailored for a specific consumer  

An adapter does not decide what is true.

It prepares data so that other layers can operate cleanly.

---

## What an Adapter Does

Adapters typically:

- transform canonical state into view-ready structures  
- aggregate multiple runtime sources into a single model  
- normalize data shapes  
- prepare inputs for lenses  
- prepare outputs for UI modules  
- isolate consumers from internal runtime structure  

Example responsibilities:

- building a timeline view from canonical event history  
- shaping grid/occupancy data for rendering  
- combining observer selection + canonical state into interaction options  
- preparing teaching/debug overlays  

---

## What an Adapter Is Not

An adapter is **not**:

- a source of canonical truth  
- a validation layer  
- a mutation layer  
- a controller  
- a lens  

Adapters must not:

- mutate canonical state  
- enforce invariants  
- decide whether events are valid  
- append to canonical history  
- coordinate unrelated system behavior  

---

## Adapters vs Lenses

Adapters and lenses are closely related but serve different roles.

### Adapter

- prepares data  
- translates structure  
- aggregates inputs  
- outputs clean, consumable models  

### Lens

- interprets meaning  
- applies visibility rules  
- determines player-facing experience  
- transforms data into gameplay or presentation semantics  

---

### Relationship

A typical flow is:

```text
Canonical State / Observer State
        ↓
     Adapter
        ↓
       Lens
        ↓
        UI
````

Adapters provide structured input.

Lenses decide what that input means for the observer.

---

## Where Adapters Sit in the Architecture

Adapters sit between:

* runtime systems (canonical + observer state)
* interpretation and presentation layers

They form a **boundary layer** that protects both sides.

---

### Full Flow

```text
Runtime (Truth + State)
        ↓
Adapter Layer (Translation)
        ↓
Lens Layer (Interpretation)
        ↓
UI / Tooling (Presentation)
```

---

## Adapter Inputs

Adapters may consume:

* canonical event history
* derived canonical state
* observer-local state
* selection/context state
* branch/history position

Adapters should not depend on:

* internal UI state
* unrelated lens outputs
* hidden global state

---

## Adapter Outputs

Adapters produce:

* view models
* structured datasets
* normalized representations
* lens-ready input
* UI-ready data

Outputs should be:

* stable
* predictable
* well-scoped to their purpose

---

## Adapter Design Rules

Good adapters follow these rules:

### 1. Narrow Scope

Each adapter should do one job.

Bad:

* “world + history + UI + debug adapter”

Good:

* “timeline adapter”
* “world grid adapter”
* “interaction adapter”

---

### 2. No Mutation

Adapters do not change:

* canonical history
* derived state
* observer state

They are read-only transformations.

---

### 3. No Validation Logic

Adapters must not:

* enforce invariants
* accept or reject events
* apply canonical rules

That belongs to the validation layer.

---

### 4. No Hidden Control Flow

Adapters should not:

* trigger actions
* coordinate UI behavior
* act as controllers

They prepare data only.

---

### 5. Stable Contracts

Adapters should expose consistent output shapes.

This allows:

* UI modules to remain simple
* lenses to remain isolated
* future refactoring without cascading breakage

---

## Adapter Types

Adapters can be grouped by purpose.

---

### 1. View Adapters

Prepare canonical and observer data for display.

Examples:

* world grid view
* event timeline view
* branch/history view

---

### 2. Interaction Adapters

Prepare data for user interaction.

Examples:

* selectable targets
* valid actions for a selected object
* contextual action lists

---

### 3. Teaching Adapters

Prepare data for teaching/debugging.

Examples:

* pending vs canonical comparison
* validation result overlays
* event lineage visualization

---

### 4. Debug / Inspection Adapters

Prepare data for developer tools.

Examples:

* canonical diff views
* replay inspection data
* invariant violation traces

---

## Adapters in the Teaching Prototype

In the teaching prototype, adapters are used to:

* prevent lenses from directly accessing runtime internals
* isolate UI modules from raw data structures
* shape canonical and observer state into view-ready forms
* support multiple UI panels without cross-coupling

They are a key mechanism for keeping the prototype understandable and maintainable.

---

## Why This Matters

Adapters are critical because they:

* prevent lens-to-lens coupling
* prevent UI from depending on runtime internals
* prevent controller sprawl
* preserve architectural boundaries
* make the system easier to reason about
* allow independent evolution of runtime, lenses, and UI

Without adapters, the system would gradually collapse into tightly coupled modules.

---

## Current Status

Adapters are part of the CrypSA architecture and are actively used in the teaching prototype.

Their exact structure and patterns may evolve, but their role as a **translation boundary layer** is fundamental.

---

## Summary

In CrypSA, adapters are translation layers that reshape runtime and canonical data into structured forms for lenses and UI, preserving separation between truth, interpretation, and presentation.

---

## One Sentence Summary

A CrypSA adapter is a read-only translation layer that prepares canonical and observer state for lenses and UI, without modifying truth or enforcing system rules.
