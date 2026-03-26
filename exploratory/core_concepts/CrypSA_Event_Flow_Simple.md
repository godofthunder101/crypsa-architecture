# CrypSA Event Flow (Simplified)

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document presents a simplified conceptual view of how events flow through a CrypSA system.

It is intended as a high-level mental model, not a formal specification.

---

## Conceptual Flow

```text
Observer Action
→ Local Simulation
→ Candidate Event
→ Validation
→ Accepted Event (Canonical Event)
→ Canonical Event History Updated
→ Observer Reconstruction
````

---

## Simplified Diagram

```text
Observer Action
      ↓
Local Simulation
      ↓
Candidate Event
      ↓
Validation
   ├── Reject → Local Correction
   └── Accept → Assign server_sequence → Canonical Event → Canonical Event History Updated
                         ↓
               Observer Reconstruction
```

---

## How to Read This

### Observer Action

An observer initiates an interaction.

---

### Local Simulation

The action is simulated locally:

* immediate feedback
* prediction
* temporary effects

---

### Candidate Event

If the action affects canonical event history:

* a candidate event is created
* it represents a proposed change
* it is **not yet canonical**

---

### Validation

The server evaluates the event:

* invariants
* rules
* references

Result:

* accepted
  or
* rejected

---

### Canonical Event History

If accepted:

* the server assigns `server_sequence` (authoritative ordering)
* the event becomes a **canonical event**
* the event is appended to canonical event history

If rejected:

* no canonical change occurs
* the observer corrects local simulation

---

### Observer Reconstruction

Observers:

* receive canonical updates
* rebuild affected state
* align with canonical event history

---

## Key Insight

> CrypSA systems evolve through validated canonical events recorded in canonical event history, not continuous synchronized simulation.

---

## Relationship to Other Docs

This document overlaps with:

* Event Lifecycle
* Event Flow Model

It provides a simplified view of the same concepts.

---

## One Sentence Summary

CrypSA models interaction flow as a progression from local simulation to validated canonical events, where accepted events are ordered, recorded in canonical event history, and used to reconstruct shared reality.
