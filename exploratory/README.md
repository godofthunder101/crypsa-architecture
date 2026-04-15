# CrypSA Exploratory

---

“Terminology in this document may not match current CrypSA definitions.
Refer to the Terminology Primer for authoritative meaning.”

---

## Purpose

This section contains experimental and forward-looking ideas related to CrypSA.

These documents explore possible extensions, alternative designs, and future directions.

They exist to:

* expand the design space
* test ideas before formalization
* capture thinking that is not yet part of the core system

They are intentionally separated from the authoritative system definition.

---

## Important

Documents in this section are **non-authoritative**.

They:

* are not part of the v0.1 runtime specification
* are not required to understand CrypSA
* may be incorrect, incomplete, or superseded by future work
* may change, be rewritten, or be removed at any time

They must not be treated as:

* architecture definitions
* specification rules
* implementation requirements

Exploration documents must not define or modify canonical truth.

---

## Scope

Exploration documents may:

* propose new ideas
* test alternative models
* describe potential features
* explore future system directions

They may be:

* incomplete
* speculative
* intentionally unrefined

---

## Constraints

Exploration documents must not:

* redefine existing architecture concepts
* introduce conflicting terminology
* introduce new terminology unless clearly marked as exploratory
* override definitions in `architecture/` or `spec/`
* redefine canonical ordering or introduce alternatives to `canonical_sequence`
* blur the boundary between truth, translation, interpretation, and experience

If a concept conflicts with the core system:

> the definitions in `architecture/` and `spec/` take precedence

---

## Relationship to Core System

For authoritative understanding, start with:

* `../CrypSA_In_One_Diagram.md`
* `../CrypSA_In_5_Minutes.md`
* `../architecture/`
* `../spec/`

After understanding the core system, return to this section to explore:

* alternative approaches
* future ideas
* experimental directions

---

## Promotion Path

Ideas in this section may evolve into core concepts.

When that happens:

1. the concept is formalized
2. terminology is aligned with the architecture
3. behavior is defined clearly (if applicable)
4. it is moved into:

   * `architecture/` (structure)
   * `spec/` (behavior)
   * `implementation/` (practical use)

Exploratory documents must never become authoritative without being moved and formalized in `architecture/` or `spec/`.

---

## Design Role

This section acts as a:

* sandbox for architectural thinking
* staging area for future features
* space for testing ideas without affecting core clarity

It allows CrypSA to evolve without destabilizing the current model.

---

## Diagram Rule Alignment

Any diagrams in this section must follow the rules defined in:

* `../diagrams/README.md`

---

## One Sentence Summary

This section explores where CrypSA could go, without defining or altering the current authoritative system.
