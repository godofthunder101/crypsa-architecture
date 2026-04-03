# CrypSA Concept Map

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document presents CrypSA as a single conceptual chain.

It is intended as a **mental model**, not an authoritative description of the system.

It helps illustrate how core ideas connect, but does not define architecture or behavior.

---

## Conceptual Chain

```text
Mint
→ (Identity + Genome)
→ Canonical Object
→ Invariants
→ Observer Reconstruction
→ Adapters (Translation)
→ Lenses (Interpretation)
→ Experience (Simulation/UI)
→ Invariant Boundary
→ Candidate Event
→ Validation
→ Canonical Event History (ordered via canonical_sequence)
→ Derived Canonical State
```

---

## How to Read This

This chain describes a conceptual flow:

* objects are defined structurally
* observers reconstruct and interpret them
* simulation occurs locally
* some interactions cross the invariant boundary
* validated events update canonical history
* observers reconstruct updated state

---

## Important Clarification

This chain is a **conceptual simplification**.

The authoritative CrypSA architecture is defined as:

* **Truth** — canonical events and validation
* **Translation** — adapters
* **Interpretation** — lenses
* **Experience** — UI and local simulation

This document should not be used to redefine those layers.

---

## Notes on Concepts

### Mint, Identity, Genome

These define canonical structure within the truth model.

They are presented here in sequence for conceptual clarity.

---

### Observer Reconstruction

Observers rebuild canonical reality locally via replay from:

* identity
* genome
* canonical event history

---

### Adapters and Lenses

* adapters shape data (**translation**)
* lenses interpret meaning (**interpretation**)

---

### Experience

Local simulation and UI form the observer’s experience.

---

### Invariant Boundary

This determines whether an action affects canonical event history:

* remains local
* becomes a candidate event

---

### Validation and Canonical Events

The validator validates candidate events.

Accepted events:

* are appended to canonical event history
* define shared truth

---

### Reconstruction Loop

Observers reconstruct updated state from canonical event history in canonical_sequence order.

This forms a continuous loop between:

* simulation
* validation
* reconstruction

---

## Key Insight

> CrypSA can be understood as a cycle of reconstruction, local simulation, validation, and canonical event history updates.

---

## Why This Exists

This conceptual map helps:

* understand the system holistically
* connect otherwise separate components
* reason about flow without strict layering

---

## One Sentence Summary

CrypSA can be viewed as a cycle where deterministic object definitions and canonical event history, combined with local simulation and invariant-protected validation, work together to produce and maintain canonical shared reality.
