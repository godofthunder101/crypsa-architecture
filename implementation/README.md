# Implementation

## Purpose

This folder contains implementation strategy, build direction, project status, and practical engineering guidance for CrypSA.

These documents describe:

* how the system may be built
* how components may be structured in code
* how architectural ideas translate into implementation

---

## Important

Documents in this folder are **not authoritative**.

They:

* do not define runtime behavior
* do not define validation rules
* do not define canonical truth

They must not be treated as:

* specification documents
* architecture definitions

---

## Source of Truth

For authoritative system behavior, refer to:

* `../spec/`

For conceptual system structure, refer to:

* `../architecture/`

---

## Relationship Between Layers

CrypSA separates responsibilities across three layers:

* **Architecture** → what the system is
* **Spec** → how the system behaves
* **Implementation** → how the system is built

This folder exists only in the **implementation layer**.

---

## Consistency Rules

Documents in this folder must not:

* redefine validation logic
* redefine event structure
* redefine invariants
* introduce conflicting terminology

If a conflict exists:

> the spec and architecture always take precedence

---

## Evolution

Implementation guidance may evolve as the system is built.

If implementation patterns become stable and necessary:

* behavior belongs in `spec/`
* structure belongs in `architecture/`

Implementation documents should not become authoritative definitions.

---

## One Sentence Summary

This folder explains how CrypSA can be built in practice, but the authoritative system definition lives in the specification and architecture layers.
