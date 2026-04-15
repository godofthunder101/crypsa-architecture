# CrypSA Event Flow Model

---

“Terminology in this document may not match current CrypSA definitions.
Refer to the Terminology Primer for authoritative meaning.”

---

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes how interactions propagate through a CrypSA system.

It presents a conceptual flow of how observer actions may become part of canonical event history.

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
→ Accepted / Rejected
→ Assign canonical_sequence (if accepted)
→ Append to Canonical Event History
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
       Submit Candidate Event to Validator
                     ↓
                 Validation
                     ↓
              Accepted / Rejected
                ├─ Rejected → Local Correction
                └─ Accepted
                        ↓
            Assign canonical_sequence
                        ↓
     Append to Canonical Event History
                        ↓
   Observer Reconstruction (Derived Canonical State)
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

> Does this interaction affect canonical event history?

* No → remains local
* Yes → becomes a candidate event

---

### 4. Candidate Event

If the interaction crosses the invariant boundary:

* a candidate event is created
* it represents a proposed change

A candidate event is **not yet canonical**.

---

### 5. Event Submission

The candidate event is submitted to the validator for validation.

---

### 6. Validation

The validator evaluates the event:

* schema validation
* identity validation
* precondition checks
* invariant enforcement
* rule validation

The event is:

* accepted
  or
* rejected

---

### 7. Canonical Event Acceptance

If accepted:

* the validator assigns `canonical_sequence` (authoritative ordering)
* canonical_sequence defines the authoritative ordering of events for replay
* the event becomes a **canonical event**
* it is appended to canonical event history

If rejected:

* no canonical change occurs
* the observer corrects local simulation

---

### 8. Observer Reconstruction

Observers receive canonical updates and:

* replay canonical event history in canonical_sequence order (or apply ordered updates)
* reconstruct affected objects
* align with canonical truth

---

## Observer Convergence

Observers may temporarily diverge due to local simulation.

After canonical updates:

* all observers reconstruct consistently
* shared reality converges

---

## Key Insight

> CrypSA systems evolve through validated canonical events ordered and recorded in canonical event history, not continuous synchronized simulation.

---

## Notes on Implementation

Some implementations may include additional metadata or validation context.

These are implementation choices and not required by the core model.

---

## Summary

CrypSA systems:

* simulate locally
* validate when crossing the invariant boundary
* accept or reject candidate events
* append accepted events to canonical event history
* reconstruct shared reality deterministically

---

## One Sentence Summary

CrypSA models interaction flow as a transition from local simulation to validated canonical events, where accepted events are assigned canonical_sequence, recorded in canonical event history, and used to deterministically reconstruct shared reality.
