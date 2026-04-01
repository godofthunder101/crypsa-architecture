# Foundation

## Purpose

This folder contains the early conceptual framing, motivation, and philosophical background of CrypSA.

These documents explain:

* why CrypSA exists
* the problems it was designed to address
* how the architecture evolved over time

They provide context for the system, not its current definition.

---

## Important

Documents in this folder are **non-authoritative**.

They:

* do not define the current architecture
* do not define runtime behavior
* may contain outdated terminology, models, or assumptions

They must not be treated as:

* architecture definitions
* specification rules
* implementation guidance

---

## Source of Truth

For the current CrypSA model, refer to:

* `../../CrypSA_In_One_Diagram.md`
* `../../CrypSA_In_5_Minutes.md`
* `../../CrypSA_Terminology_Primer.md`
* `../../architecture/`
* `../../spec/`

These define the authoritative structure, terminology, and behavior of the system.

---

## Relationship to Explorations

The `foundation/` folder captures **where CrypSA came from**.

The `explorations/` folder captures **where CrypSA might go**.

* Foundation → historical context and origin
* Explorations → forward-looking ideas and experiments

Both are non-authoritative, but serve different roles.

---

## Consistency Rules

Documents in this folder must not:

* redefine core architectural concepts
* introduce conflicting terminology
* override definitions in `architecture/` or `spec/`

If a conflict exists:

> the authoritative sources always take precedence

---

## Evolution

This folder preserves the conceptual development of CrypSA.

If ideas from these documents become stable, they must be:

1. refined
2. aligned with current terminology
3. integrated into the correct layer:

   * `architecture/` (structure)
   * `spec/` (behavior)
   * `implementation/` (practical guidance)

They must not become authoritative while remaining in this folder.

---

## Design Role

This folder acts as a:

* historical record of the architecture’s origin
* explanation of underlying motivations
* reference for how ideas evolved into the current model

It helps readers understand not just **what CrypSA is**, but **why it became that way**.

---

## One Sentence Summary

This folder captures the origin, motivation, and early conceptual framing of CrypSA, while the authoritative system definition lives in the architecture and specification layers.
