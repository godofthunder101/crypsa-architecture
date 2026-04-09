# CrypSA: A Distributed Architecture for Persistent Digital Universes

---

“Terminology in this document may not match current CrypSA definitions.
Refer to the Terminology Primer for authoritative meaning.”

---


> Exploratory note: This document represents early conceptual framing.
>
> It reflects the evolution of CrypSA and may contain terminology or structure that differs from the current model.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_Why_It_Exists.md`
> * `../../CrypSA_Where_It_Fits.md`
> * `../../architecture/`
> * `../../spec/`

Author: Beau Wells
Year: 2026

---

## Abstract

CrypSA (Cryptid Server Architecture) is a distributed simulation architecture designed to support persistent digital universes while minimizing centralized world simulation.

Traditional multiplayer systems rely on server-authoritative models that continuously synchronize mutable world state between clients and servers. As the scale and complexity of shared worlds increase, this model introduces significant challenges related to synchronization overhead, scalability, and infrastructure cost.

CrypSA proposes an alternative approach in which the system synchronizes **validated canonical events** rather than full simulation state. Structural identities and deterministic object genomes allow observers to reconstruct canonical objects locally. **Canonical event history evolves through validated canonical events**, rather than continuous centralized simulation.

This architecture separates structural reality from experiential interpretation. The Mint defines immutable identities and deterministic object definitions, while Lenses provide modular interpretation layers that determine how observers experience the universe.

By shifting responsibility for simulation toward observers while preserving canonical event history through validation, CrypSA enables scalable persistent universes with reduced reliance on centralized simulation infrastructure.

---

## 1. Introduction

Large-scale multiplayer environments present significant architectural challenges.

Traditional models maintain global consistency by continuously synchronizing mutable world state across connected clients. While effective for small environments, this model becomes increasingly complex and resource-intensive as worlds grow larger and interactions become more numerous.

Server-authoritative architectures must track:

* world object state
* simulation ticks
* player interactions
* conflict resolution
* synchronization across observers

As world size increases, the system becomes responsible for maintaining and distributing an ever-growing volume of mutable state.

CrypSA introduces a different model.

Instead of synchronizing mutable world state, CrypSA synchronizes **validated canonical event history** and enforces invariants at the boundary of shared reality.

Observers reconstruct their experience of the universe locally, while a **validator** acts as the authority over canonical changes rather than a simulator of the world.

---

## 2. The CrypSA Model

CrypSA separates structural reality from observer experience.

The system can be understood through four responsibilities:

```text
Experience (Simulation + UI)
↓
Interpretation (Lenses)
↓
Translation (Adapters)
↓
Invariant Boundary
↓
Truth (Validation + Canonical Event History)
```

* observers simulate and experience the world locally
* lenses interpret canonical data into meaning
* adapters shape data for interpretation
* the invariant boundary determines what affects canonical event history
* the validator evaluates and records canonical events

The validator does not simulate the world.
It enforces correctness of canonical event history.

---

## 3. Core Concepts

### Invariants

Invariants define rules that must always remain true in canonical reality.

They are enforced during validation to ensure that accepted events do not produce invalid or contradictory states.

---

### Candidate Events

Candidate events represent proposed changes to canonical reality.

They originate from observer actions and are subject to validation.

---

### Canonical Events

Canonical events are candidate events that have:

* passed validation
* been assigned canonical ordering (`server_sequence`)
* been appended to canonical event history

Canonical events define shared truth.

---

## 4. Validation and Canonical Event Acceptance

When an observer performs an action affecting canonical event history:

1. the action is simulated locally

2. the invariant boundary determines if it affects canonical event history

3. a candidate event is created

4. the event is submitted to the validator

5. the validator evaluates the event against invariants and rules

6. if accepted:

   * the event becomes a canonical event
   * the validator assigns `server_sequence`
   * the event is appended to canonical event history

7. if rejected:

   * no canonical change occurs
   * the observer corrects local simulation

8. observers reconstruct the updated world via replay of canonical event history

This ensures that all observers eventually converge on the same derived canonical state.

---

## 5. Design Guarantees

### Invariant Consistency

Canonical event history remains consistent because:

* all candidate events are validated
* invariants are enforced before acceptance
* only valid events become canonical

---

## 6. Conclusion

CrypSA proposes a distributed architecture in which shared reality is maintained through identities, deterministic object definitions, and validated canonical event history.

Observers reconstruct the universe locally while the validator ensures that invariant rules remain intact through validation.

By separating structural reality from interpretation and experience, CrypSA enables scalable persistent digital universes that evolve through validated canonical events rather than centralized simulation.

---

## One Sentence Summary

CrypSA is a distributed architecture in which observers reconstruct persistent digital universes locally while a validator evaluates candidate events, accepts canonical events, and preserves canonical event history.
