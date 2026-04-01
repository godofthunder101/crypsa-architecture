# CrypSA Design Principles

## Purpose

This document outlines the design principles that guide CrypSA.

CrypSA is not just a networking pattern. It is an architectural approach for building persistent digital universes around canonical event history, local observer simulation, and explicit reconstruction.

These principles describe how systems built on CrypSA should be designed.

---

## Foundational Principles

### 1. Canonical Event History Is Authoritative

Canonical event history must remain internally consistent.

No component, including observers, tools, or supporting systems, may bypass validation or violate invariants.

CrypSA assumes:

* canonical event history is authoritative
* invariants define what must remain valid
* validation protects the shared universe

This principle is the foundation of the architecture.

---

### 2. The Validator Protects Event History, Not Experience

CrypSA separates responsibilities into:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local simulation

The validator operates in the truth layer.

It determines what becomes canonical. It does not own:

* local feel
* presentation
* observer simulation

---

### 3. Simulate Locally Whenever Event History Is Not at Stake

Observers should simulate locally whenever doing so does not directly change canonical event history.

This includes:

* prediction
* temporary local effects
* presentation-driven behavior
* observer-relative simulation

Validation is required only when canonical event history may change.

This preserves responsiveness without weakening shared consistency.

---

### 4. Protect the Invariant Boundary

The invariant boundary separates observer-local behavior from canonical world change.

Every meaningful interaction should answer:

> Does this action affect canonical event history?

If yes:

* it must cross the invariant boundary
* it must be validated before becoming canonical

A clear invariant boundary is essential for:

* consistency
* security
* reconciliation
* architectural clarity

---

### 5. Favor Canonical Events Over Mutable State Synchronization

CrypSA systems should prefer validated canonical events as the basis of shared reality.

Rather than synchronizing mutable world state:

* observers reconstruct from canonical event history
* canonical events define all shared change

This keeps reality:

* explicit
* inspectable
* durable

---

### 6. Favor Reconstruction Over Hidden Authority

Observers should be able to reconstruct relevant canonical reality from:

* identity
* genome or structural definition
* canonical event history
* derived canonical state

This makes world evolution:

* understandable
* debuggable
* independent of opaque systems

---

### 7. Keep the Canonical Layer Minimal

Canonical event history should contain only what must remain globally consistent.

It should avoid storing:

* temporary simulation state
* observer-specific interpretation
* presentation details
* transient local effects

The canonical layer should remain:

* compact
* durable
* focused on event history

---

### 8. Separate Truth, Translation, Interpretation, and Experience

CrypSA depends on explicit architectural boundaries.

Systems must not collapse these layers together.

In particular:

* adapters must not become validators
* lenses must not become truth sources
* UI must not become runtime authority
* observer experience must not redefine canonical event history

This separation preserves clarity and prevents system coupling.

---

### 9. Preserve Object Identity and Provenance

Canonical objects must retain stable identity across their lifecycle.

Canonical event history records how they evolve over time.

This enables systems to reason about:

* ownership
* transitions
* lineage
* anomaly investigation
* persistence

CrypSA systems should preserve enough provenance to explain how canonical reality came to be.

---

### 10. Support Multiple Interpretations of the Same Event History

A single canonical universe may support multiple observer experiences.

Different systems may apply different lenses and experience layers to the same canonical event history.

This enables:

* different gameplay views
* different tooling views
* different visibility rules
* different observer contexts

Interpretation may vary.
Canonical event history must not.

---

### 11. Design Universes, Not Just Validators

CrypSA should be designed as infrastructure for persistent universes, not merely as a conventional multiplayer backend.

This means thinking in terms of:

* canonical event history
* invariants
* object lifecycle
* event evolution
* observer reconstruction

rather than only request/response flows or centralized simulation loops.

---

## Optional Design Strategies

The following are useful strategies in some CrypSA systems, but they are not universal requirements.

---

### Context-Aware Validation

Some systems may validate events using surrounding canonical context, provenance, or recent event history rather than only isolated checks.

This can support:

* stronger anomaly detection
* richer rule enforcement

---

### Deferred Investigation

Some systems may defer expensive investigation when immediate rejection is not required, provided canonical event history remains protected.

This can balance:

* responsiveness
* operational cost

---

### Gameplay-Integrated Infrastructure

Some applications may hide infrastructure delays or validation pacing behind diegetic gameplay concepts, such as:

* attunement
* stabilization
* synchronization periods

This is an application design strategy, not a core requirement.

---

### Risk-Based Validation Depth

Some systems may validate high-impact actions more deeply than low-impact actions, as long as canonical event history remains properly protected.

This is a scaling strategy, not permission to weaken invariants.

---

## Summary

CrypSA design is guided by a small set of core ideas:

* protect canonical event history
* simulate locally where possible
* keep the invariant boundary explicit
* reconstruct from canonical event history
* keep the canonical layer minimal
* preserve separation between truth, translation, interpretation, and experience

These principles allow CrypSA to support persistent universes that remain:

* consistent
* flexible
* understandable

---

## One Sentence Summary

CrypSA is designed around protecting canonical event history while allowing observers to simulate, interpret, and experience the universe locally through explicit architectural boundaries.
