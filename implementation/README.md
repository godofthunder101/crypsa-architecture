# Implementation

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This folder provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details will vary based on product requirements.

Documents in this folder illustrate possible implementation approaches to structure systems that conform to CrypSA.

---

## Purpose

This folder contains implementation strategy, build direction, and practical engineering guidance for CrypSA.

These documents describe:

* how the system may be implemented in code
* how components may be organized in practice
* how architectural ideas are proven through implementation

👉 Implementation exists to **prove the CrypSA runtime model through executable systems**.

Implementation must treat the validator as the component that defines what becomes canonical.

---

## Where to Start

The recommended starting point is:

👉 `CrypSA_Minimal_Runtime_Walkthrough.md`

This document defines:

* the smallest possible working CrypSA system
* the minimal runtime loop
* the components required to prove the architecture

👉 Implementation should begin by proving this minimal runtime, not by building a full system.

---

## Implementation Approach

CrypSA development follows a **proof-first approach**:

1. implement the minimal runtime loop
2. verify canonical event flow
3. prove deterministic replay
4. validate reconciliation behavior
5. expand system scope incrementally

👉 A full system should only be built after the minimal runtime has been proven.

👉 The goal is to validate the architecture through working systems, not speculative design.

---

## Important

Documents in this folder are **not authoritative**.

They:

* do not define runtime behavior
* do not define validation rules
* do not define truth

They must not be treated as:

* specification documents
* architecture definitions

Implementation must not treat derived state or local simulation as authoritative.

Canonical event history remains the sole source of truth.

Examples and code patterns are illustrative and must not be treated as normative or complete implementations.

Implementation choices must not redefine or reinterpret CrypSA behavior.

---

## Source of Truth

For authoritative system behavior, refer to:

* `../spec/`

For conceptual system structure, refer to:

* `../architecture/`

---

## Relationship Between Layers

CrypSA separates documentation responsibilities across three layers:

* **Architecture** → what the system is
* **Spec** → how the system behaves
* **Implementation** → how the system is built and proven

This folder exists only in the **implementation layer**.

👉 Implementation must prove architecture and strictly conform to the spec.

Implementation must never override, reinterpret, or bypass behavior defined in the spec.

---

## Consistency Rules

Documents in this folder must not:

* redefine validation logic
* redefine event structure
* redefine invariants
* redefine invariant boundary behavior
* introduce conflicting terminology

If a conflict exists:

> the spec and architecture always take precedence

---

## Evolution

Implementation guidance may evolve as the system is built.

If implementation patterns become stable and necessary:

* behavioral rules must move to `spec/`
* structural definitions must move to `architecture/`
* this folder must remain non-authoritative

No behavioral rule should remain only in implementation documentation.

Implementation documents must not become authoritative definitions.

---

## One Sentence Summary

This folder provides practical guidance for proving and building CrypSA systems, while authoritative behavior and structure are defined in the specification and architecture layers.
