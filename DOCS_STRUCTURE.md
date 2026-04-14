# CrypSA Documentation Structure

CrypSA uses a layered documentation system so that each concept has a clear source of truth.

This structure ensures:

* clarity of responsibility
* consistency across documents
* a predictable learning path

---

## Core Learning Path

Start here to understand CrypSA:

* `CrypSA_In_One_Diagram.md`
* `CrypSA_In_5_Minutes.md`
* `CrypSA_Terminology_Primer.md`
* `CrypSA_Worked_Example.md`
* `FAQ.md`

These documents provide:

* high-level understanding
* core terminology
* conceptual grounding
* concrete examples

---

## System Definition (Authoritative)

These define the system’s behavior and structure:

* `spec/` — runtime behavior and validation rules (**highest authority for behavior**)
* `architecture/` — system structure and responsibilities

These documents define:

* validation behavior
* canonical event model
* system responsibilities
* invariant enforcement

Core truths:

* canonical event history is the source of truth
* the validator defines what becomes canonical
* derived canonical state is reconstructed via replay of canonical event history

---

## Implementation Direction

These describe how CrypSA can be built:

* `implementation/`

These documents:

* guide system construction
* describe practical approaches
* must not redefine system behavior defined in the spec

---

## Teaching System

These demonstrate and explain the system:

* `teaching/`

Includes:

* teaching prototype
* learning-oriented materials

These documents are:

* illustrative
* non-authoritative

---

## Supporting and Reference Content

These help explain and navigate the system:

* `diagrams/` — visual representations (non-authoritative)
* `atlas/` — navigation and supporting reference material

These documents:

* support understanding
* must align with authoritative sources
* must not introduce or reinterpret system behavior

---

## Exploratory Content

Forward-looking or non-final ideas:

* `exploratory/`

These documents:

* explore possibilities
* test concepts
* are explicitly non-authoritative

---

## Authority Rule

If multiple documents appear to describe the same concept, the following precedence applies:

1. `spec/` — runtime behavior
2. `architecture/` — system structure
3. `implementation/` — build direction
4. `teaching/` — examples and explanation
5. supporting and exploratory content

> In case of conflict, higher-authority documents override lower-authority ones and define the correct interpretation.

Supporting and exploratory documents must not be treated as authoritative definitions of CrypSA behavior.

---

## Consistency Rule

If two documents describe the same concept at the same authority level:

> one must be merged, clarified, or removed

No duplicate authoritative definitions are allowed.

---

## Design Principle

Each concept in CrypSA should have:

* one authoritative definition
* any number of supporting explanations

This prevents:

* conflicting interpretations
* duplicated logic
* architectural drift

---

## One Sentence Summary

CrypSA documentation is structured so that authoritative definitions live in `spec/` and `architecture/`, canonical event history is the source of truth, and all other documents support understanding without redefining behavior.
