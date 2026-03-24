# CrypSA Event Flow Model

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_MinUTES.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes how interactions propagate through a CrypSA system.

It presents a conceptual flow of how observer actions may become part of canonical truth.

This is a **conceptual model**, not an authoritative runtime definition.

---

## High-Level Flow

```text
Observer Action
→ Local Simulation
→ Invariant Boundary Check
→ Candidate Event
→ Submission
→ Validation
→ Canonical Event History Update
→ Observer Reconstruction
```

---

## Conceptual Flow

```text
Observer Action
      ↓
Local Simulation
      ↓
Invariant Boundary Check
      ├─ No  → Remain Local
      └─ Yes → Candidate Event
                     ↓
               Event Submission
                     ↓
                 Validation
                     ↓
              Accepted / Rejected
                     ↓
     Canonical Event History Updated
                     ↓
         Observer Reconstruction
```

---

## Step-by-Step Explanation

### 1. Observer Action

An observer initiates an interaction.

Examples:

* picking up an item
* placing a structure
* triggering a system event

At this stage, the interaction exists only locally.

---

### 2. Local Simulation

The observer simulates the interaction.

Examples:

* movement
* physics
* prediction
* temporary effects

This provides immediate feedback.

---

### 3. Invariant Boundary Check

The system determines:

> Does this interaction affect canonical truth?

* No → remains local
* Yes → becomes a candidate event

---

### 4. Candidate Event

If the interaction affects canonical truth:

* a candidate event is created
* it represents a proposed change

---

### 5. Event Submission

The candidate event is sent to the server.

---

### 6. Validation

The server evaluates the event:

* invariant enforcement
* rule validation
* identity and reference checks

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

### 8. Observer Reconstruction

Observers receive updates and:

* reconstruct affected objects
* align with canonical truth

---

## Observer Convergence

Observers may temporarily diverge in local simulation.

After canonical updates:

* all observers reconstruct consistently
* shared reality converges

---

## Key Insight

> CrypSA systems evolve through validated canonical events, not continuous synchronized simulation.

---

## Notes on Implementation

Some implementations may include additional context or metadata to support validation.

These are implementation choices and not required by the core model.

---

## Summary

CrypSA systems:

* simulate locally
* validate only when necessary
* update canonical history through accepted events
* reconstruct shared reality deterministically

---

## One Sentence Summary

CrypSA models interaction flow as a transition from local simulation to validated canonical events, followed by deterministic reconstruction of shared reality.
