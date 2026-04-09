# Implementation

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This folder provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details may vary based on product requirements.

Documents in this folder illustrate possible ways to structure systems that conform to CrypSA.

---

## Purpose

This folder contains implementation strategy, build direction, project status, and practical engineering guidance for CrypSA.

These documents describe:

* how the system may be implemented in code
* how components may be organized in practice
* how architectural ideas translate into implementation

Implementation must treat the validator as the authority over canonical event history.

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
* **Implementation** → how the system is built

This folder exists only in the **implementation layer**.

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

Implementation documents should not become authoritative definitions.

---

## One Sentence Summary

This folder provides practical guidance for building CrypSA systems, while authoritative behavior and structure are defined in the specification and architecture layers.
