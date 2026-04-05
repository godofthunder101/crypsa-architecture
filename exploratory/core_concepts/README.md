# Core Concepts

## Purpose

This folder contains exploratory concept documents and early explanatory models of CrypSA.

These documents are intended to:

* provide intuition and mental models
* explore early or alternative ideas
* capture conceptual thinking

This folder is part of the broader `exploratory/` layer and follows the same non-authoritative rules.

---

## Important

Documents in this folder are **non-authoritative**.

They:

* do not define the current architecture
* do not define system behavior
* may be incomplete, evolving, or simplified

They must not be treated as:

* architecture definitions
* specification rules
* implementation requirements

---

## Source of Truth

For the current CrypSA model, refer to:

* `../../CrypSA_In_5_Minutes.md`
* `../../architecture/`
* `../../spec/`

These define the authoritative structure and runtime behavior of the system.

If there is any conflict between documents:

> the `/spec` layer takes precedence

---

## Consistency Rules

Documents in this folder must not:

* redefine core architectural concepts
* introduce conflicting terminology
* override definitions in `architecture/` or `spec/`

Documents in this folder must also:

* use **validator**, not “server” (unless referring to deployment)
* use canonical terminology (e.g. canonical event history, candidate event, invariant boundary)

If a conflict exists:

> the authoritative sources always take precedence

---

## Promotion Path

If a concept from this folder becomes stable:

1. it is formalized
2. terminology is aligned
3. it is moved into:

   * `architecture/` (structure)
   * `spec/` (behavior)
   * `implementation/` (practical guidance)

Concepts must not become authoritative while remaining in this folder.

---

## One Sentence Summary

This folder captures conceptual models and early ideas for CrypSA, while the authoritative system definition lives in the architecture and spec layers.
