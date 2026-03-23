# CrypSA Design Principles

## Purpose

This document outlines the design principles that guide CrypSA.

CrypSA is not just a networking pattern. It is an architectural approach for building persistent digital universes around canonical truth, local observer simulation, and explicit reconstruction.

These principles describe how systems built on CrypSA should be designed.

---

## Foundational Principles

### 1. Canonical Truth Is Authoritative

Canonical truth must remain internally consistent.

No component, including clients, tools, or supporting systems, may bypass canonical validation or violate invariants.

CrypSA assumes:

* canonical truth is authoritative
* invariants define what must remain true
* validation protects the shared universe

This principle is the foundation of the architecture.

---

### 2. The Server Protects Truth, Not Experience

CrypSA separates responsibilities into:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local simulation

The server operates in the truth layer.

It determines what becomes canonical. It does not need to own local feel, presentation, or full observer simulation.

---

### 3. Simulate Locally Whenever Canonical Truth Is Not at Stake

Observers should simulate locally whenever doing so does not directly change shared truth.

This includes:

* prediction
* temporary local effects
* presentation-driven behavior
* observer-relative simulation

Server validation is required when canonical truth may change.

This preserves responsiveness without weakening shared consistency.

---

### 4. Protect the Invariant Boundary

The invariant boundary separates observer-local behavior from canonical world change.

Every meaningful interaction should answer a simple question:

> Does this action affect canonical truth?

If yes, it must cross the invariant boundary and be validated before becoming canonical.

A clear invariant boundary is essential for:

* consistency
* security
* reconciliation
* architectural clarity

---

### 5. Favor Canonical Events Over Mutable State Synchronization

CrypSA systems should prefer validated canonical events as the basis of shared truth.

Rather than constantly synchronizing mutable world state, observers should reconstruct from canonical history and related canonical definitions.

This keeps truth explicit, inspectable, and durable.

---

### 6. Favor Reconstruction Over Hidden Authority

Observers should be able to reconstruct relevant canonical reality from:

* identity
* genome or structural definition
* canonical event history
* invariant-relevant state

This makes world evolution understandable and debuggable, and reduces dependence on opaque centralized simulation.

---

### 7. Keep the Canonical Layer Minimal

Canonical truth should contain only what must remain globally consistent.

It should avoid storing:

* temporary simulation state
* observer-specific interpretation
* presentation details
* transient local effects

The canonical layer should remain compact, durable, and focused on truth.

---

### 8. Separate Truth, Translation, Interpretation, and Experience

CrypSA depends on explicit architectural boundaries.

Systems should not collapse these layers together.

In particular:

* adapters must not become validators
* lenses must not become truth sources
* UI must not become runtime authority
* observer experience must not redefine canonical reality

This separation keeps the architecture understandable and prevents controller sprawl.

---

### 9. Preserve Object Identity and Provenance

Canonical objects should retain stable identity across their lifecycle, while canonical history records how they changed over time.

This allows systems to reason about:

* ownership
* transitions
* lineage
* anomaly investigation
* object persistence

CrypSA systems should preserve enough provenance to explain how canonical reality came to be.

---

### 10. Support Multiple Interpretations of the Same Truth

A single canonical universe may support multiple observer experiences.

Different systems may apply different lenses and experience layers to the same underlying truth.

This allows:

* different gameplay views
* different tooling views
* different visibility rules
* different observer contexts

Interpretation may vary. Canonical truth must not.

---

### 11. Design Universes, Not Just Servers

CrypSA should be designed as infrastructure for persistent universes, not merely as a conventional multiplayer backend.

This means thinking in terms of:

* canonical truth
* invariants
* object lifecycle
* event history
* observer reconstruction

rather than only request/response flows or centralized simulation loops.

---

## Optional Design Strategies

The following are useful strategies in some CrypSA systems, but they are not universal requirements.

### Context-Aware Validation

Some systems may validate events using surrounding canonical context, provenance, or recent event history rather than only isolated checks.

This can support stronger anomaly detection and richer rule enforcement.

---

### Deferred Investigation

Some systems may defer expensive investigation when immediate rejection is not required, provided canonical truth remains protected.

This can help balance responsiveness and operational cost.

---

### Gameplay-Integrated Infrastructure

Some applications may hide infrastructure delays or validation pacing behind diegetic gameplay concepts, such as attunement, stabilization, or synchronization periods.

This is an application design strategy, not a core architectural requirement.

---

### Risk-Based Validation Depth

Some systems may validate high-impact actions more deeply than low-impact actions, as long as canonical truth remains properly protected.

This is a scaling strategy, not permission to weaken invariants.

---

## Summary

CrypSA design is guided by a small set of core ideas:

* protect canonical truth
* simulate locally where possible
* keep the invariant boundary explicit
* reconstruct from canonical history
* keep the canonical layer minimal
* preserve separation between truth, translation, interpretation, and experience

These principles allow CrypSA to support persistent universes that remain consistent, flexible, and understandable.

---

## One Sentence Summary

CrypSA is designed around protecting canonical truth while allowing observers to simulate, interpret, and experience the universe locally through explicit architectural boundaries.
