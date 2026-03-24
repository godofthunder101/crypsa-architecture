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
→ Canonical Event History
→ Observer Reconstruction
```

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
   └── Accept → Canonical Event History Updated
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

If the action affects canonical truth:

* a candidate event is created
* it represents a proposed change

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

* the event is appended to canonical event history
* shared truth is updated

---

### Observer Reconstruction

Observers:

* receive canonical updates
* rebuild affected state
* align with shared truth

---

## Key Insight

> CrypSA systems evolve through validated canonical events, not continuous synchronized simulation.

---

## Relationship to Other Docs

This document overlaps with:

* Event Lifecycle
* Event Flow Model

It provides a simplified view of the same concepts.

---

## One Sentence Summary

CrypSA models interaction flow as a progression from local simulation to validated canonical events, followed by deterministic reconstruction of shared reality.
