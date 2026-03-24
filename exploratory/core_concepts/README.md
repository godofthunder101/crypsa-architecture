# Core Concepts

## Purpose

This folder contains exploratory concept documents and early explanatory models of CrypSA.

These documents are intended to:

* provide intuition and mental models
* explore early or alternative ideas
* capture conceptual thinking

---

## Important

Documents in this folder are **not authoritative**.

They:

* do not define the current architecture
* do not define system behavior
* may be incomplete, outdated, or simplified

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

These define the authoritative structure and behavior of the system.

---

## Consistency Rules

Documents in this folder must not:

* redefine core architectural concepts
* introduce conflicting terminology
* override definitions in `architecture/` or `spec/`

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

Concepts should not become authoritative while remaining in this folder.

---

## One Sentence Summary

This folder captures conceptual models and early ideas for CrypSA, but the authoritative system definition lives in the architecture and spec layers.
