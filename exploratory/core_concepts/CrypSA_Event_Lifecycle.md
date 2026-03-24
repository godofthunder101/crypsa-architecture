# CrypSA Event Lifecycle

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_MinUTES.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes a conceptual lifecycle of how candidate events may become canonical in a CrypSA system.

It illustrates how observer actions can propagate through validation and update shared reality.

This is a **conceptual model**, not an authoritative runtime specification.

---

## Core Principle

In CrypSA, actions do not directly change canonical truth.

Instead:

```text
Observer Action
→ Local Simulation
→ Candidate Event
→ Validation
→ Canonical Event History Update
→ Observer Reconciliation
```

Only accepted events affect shared reality.

---

## Conceptual Lifecycle

```text
Observer Action
      ↓
Local Simulation
      ↓
Invariant Boundary Check
      ├── Remain Local
      └── Candidate Event
                ↓
         Event Submission
                ↓
             Validation
         ├── Reject
         └── Accept
                ↓
  Canonical Event History Update
                ↓
     Observer Reconciliation
                ↓
    Continued Local Simulation
```

---

## Lifecycle Stages

### 1. Observer Action

An observer initiates an interaction.

Examples:

* placing a structure
* transferring ownership
* triggering a system event

This begins as local intent.

---

### 2. Local Simulation

The observer simulates the action locally:

* visual feedback
* prediction
* temporary effects

This keeps the experience responsive.

---

### 3. Invariant Boundary Check

The system determines:

> Does this affect canonical truth?

* No → remains local
* Yes → becomes a candidate event

---

### 4. Candidate Event

If canonical truth is affected:

* a candidate event is created
* it represents a proposed change

A minimal event may include:

* event type
* actor identity
* target identity
* payload

Additional metadata may exist depending on implementation.

---

### 5. Event Submission

The candidate event is sent to the server.

---

### 6. Validation

The server evaluates the event:

* invariant enforcement
* rule validation
* identity checks

The event is:

* accepted
  or
* rejected

---

### 7. Canonical Event History Update

If accepted:

* the event is appended to canonical event history
* canonical truth is updated

---

### 8. Observer Reconciliation

Observers receive updates and:

* confirm or correct local simulation
* rebuild affected objects
* align with canonical truth

---

### 9. Continued Simulation

After reconciliation:

* observers continue simulation
* the lifecycle repeats

---

## Example: Build Attempt

### Local Step

A player places a structure locally.

---

### Candidate Event

The client submits:

```text
build_structure
actor = Player A
target = tile_42
payload = mining_station
```

---

### Validation

The server checks:

* tile exists
* tile is valid
* invariants are preserved

---

### Outcomes

**Accepted**

* event recorded
* canonical state updated
* observers confirm

**Rejected**

* no canonical change
* local simulation corrected

---

## Observer Convergence

Observers may temporarily diverge locally.

After canonical updates:

* all observers reconstruct deterministically
* shared reality converges

---

## Key Insight

> CrypSA systems evolve through validated canonical events rather than continuous synchronized simulation.

---

## Notes on Implementation

Some implementations may include additional metadata or validation context.

These are optional and not required by the core model.

---

## Minimal Components

A minimal lifecycle requires:

* local simulation
* invariant boundary
* validation
* canonical event history
* observer reconciliation

---

## Summary

CrypSA systems:

* simulate locally
* validate only when needed
* update canonical history through accepted events
* reconstruct shared reality deterministically

---

## One Sentence Summary

CrypSA models world evolution as a lifecycle where local actions become candidate events, validated events update canonical history, and observers reconcile to shared truth.
