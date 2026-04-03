# CrypSA — 10 Diagrams

## Purpose

This document explains the CrypSA architecture through ten simple conceptual diagrams.

Each diagram highlights a key idea.

Together, they provide a high-level understanding of how CrypSA works as a system for persistent digital universes.

This document is **illustrative**, not authoritative.

---

## Diagram 1 — Traditional Multiplayer

Most online games use a server-authoritative model:

```text
Clients → Server → Database
```

The server:

* simulates the world
* manages mutable state
* resolves interactions
* synchronizes updates

This becomes expensive and difficult to scale.

---

## Diagram 2 — The CrypSA Shift

CrypSA changes what is synchronized:

```text
Observer → Local Simulation → Invariant Boundary → Validator → Canonical Event History
```

Instead of synchronizing full state, CrypSA synchronizes:

> validated events appended to canonical event history

---

## Diagram 3 — The Mint Model

Every canonical object begins with the Mint:

```text
Mint → Identity + Genome → Canonical Object
```

The Mint defines:

* identity
* structure
* allowed forms

---

## Diagram 4 — Deterministic Reconstruction

Observers reconstruct objects from canonical inputs:

```text
Identity + Genome + Canonical Event History → Object
```

This removes the need for full server-side simulation.

---

## Diagram 5 — The Observer Frame

Each observer operates locally:

```text
Observer → Simulation → Local Prediction → Local Effects
```

Observers may temporarily diverge in local simulation.

This is acceptable as long as canonical event history is preserved.

---

## Diagram 6 — The Invariant Boundary

The key decision:

```text
Does this affect canonical event history?
```

* No → remain local
* Yes → create candidate event

This boundary separates simulation from canonical event history.

---

## Diagram 7 — Validation and Canonical Acceptance

When an action affects canonical event history:

```text
Candidate Event → Validation → Accept / Reject
```

If accepted:

```text
→ assigned canonical_sequence and appended to canonical event history
```

The validator evaluates candidate events against invariants.
It does not simulate the world.

---

## Diagram 8 — Lens Interpretation

Canonical structure is not the same as experience:

```text
Canonical Data → Lenses → Observer Experience
```

Lenses define:

* visibility
* interaction
* meaning

---

## Diagram 9 — Derived Canonical State Transitions

The universe evolves through validated events:

```text
S_n → Event → S_n+1
```

Each accepted event produces a deterministic transition.

---

## Diagram 10 — CrypSA as a System

Conceptual layering (top to bottom):

```text
Experience → Interpretation → Translation → Truth
```

* observers simulate locally
* lenses interpret
* adapters translate
* the validator protects canonical event history

---

## The Big Picture

The full flow:

```text
Mint
→ Canonical Objects
→ Observer Reconstruction
→ Adapters (Translation)
→ Lenses (Interpretation)
→ Experience (Simulation/UI)
→ Invariant Boundary
→ Validation
→ Canonical Event History (ordered via canonical_sequence)
```

---

## Key Insight

> CrypSA separates truth, translation, interpretation, and experience into distinct responsibilities.

And:

> validation determines what becomes canonical truth, and ordering defines how it is applied

---

## One Sentence Summary

CrypSA replaces centralized simulation with validated events, local observer simulation, and layered interpretation of derived canonical state defined by canonical event history.
