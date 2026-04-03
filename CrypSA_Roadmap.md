# CrypSA Roadmap

This document outlines the planned evolution of the CrypSA architecture.

It describes how the system progresses from a defined model to a practical runtime.

---

## Guiding Principle

CrypSA is developed iteratively.

Each phase is designed to:

* prove a specific part of the system
* expose limitations
* guide the next stage of development

---

## Phase 1 — Runtime Definition

**Goal:** Define a complete and reviewable system model.

Focus:

* runtime specification
* event model
* validation model
* consistency model
* replay and snapshot systems
* identity and transport definitions

Success Criteria:

* system is internally consistent
* behavior is clearly defined
* implementation is possible from specs

---

## Phase 2 — Minimal Runtime Implementation

(**CrypSA Minimal Validator v0.1**)

**Goal:** Prove that the architecture works in practice.

Focus:

* build minimal validator implementation
* implement validation pipeline
* implement canonical event history
* implement replay system
* implement derived canonical state (via replay)
* support multiple observers
* basic networking

Success Criteria:

* multiple observers can connect
* events are validated and recorded
* canonical event history drives all state
* observers converge on shared canonical state
* replay produces consistent results

---

## Phase 3 — Robustness and Edge Cases

**Goal:** Understand real-world behavior.

Focus:

* latency and ordering issues
* reconciliation edge cases
* reconnect and recovery
* snapshot behavior under change
* failure scenarios

Success Criteria:

* system remains stable under imperfect conditions
* edge cases are understood and documented

---

## Phase 4 — Expanded Capabilities

**Goal:** Extend the system beyond the minimal runtime.

Focus:

* branching timelines (experimental, non-core capability)
* offline progression and later reconciliation
* richer invariant systems
* partial world reconstruction
* event compression and optimization

Success Criteria:

* system supports more complex use cases
* extended features remain consistent with the core model

---

## Phase 5 — Security and Trust

**Goal:** Make CrypSA viable in adversarial environments.

Focus:

* validation boundaries
* moderation and auditing tools
* anti-cheat strategies
* optional cryptographic verification

Success Criteria:

* system can operate in untrusted environments
* trust model is clearly defined

---

## Phase 6 — Scalability and Distribution

**Goal:** Support large persistent systems.

Focus:

* partitioning and sharding
* distributed canonical event history
* cross-region canonical consistency
* scalable snapshot distribution

Success Criteria:

* system can scale across multiple validator instances
* performance characteristics are understood

---

## Phase 7 — Engine Integration and Tooling

**Goal:** Make CrypSA usable in real projects.

Focus:

* engine integrations (e.g. Godot, Unity)
* developer tooling
* debugging and replay tools
* visualization and inspection systems

Success Criteria:

* developers can practically use CrypSA
* tooling reduces complexity of adoption

---

## Open Questions

CrypSA still needs to explore:

* limits of observer-side simulation
* tradeoffs between responsiveness and validation
* handling of high-frequency interactions
* integration with existing engine architectures

These questions will be addressed across multiple phases.

---

## How to Read This Roadmap

This roadmap is directional, not fixed.

The goal is to:

* validate early
* adapt based on findings
* avoid premature optimization

---

## One Sentence Summary

CrypSA evolves from a defined system into a working runtime through staged validation, expanding toward robustness, security, scalability, and real-world usability.
