# Diagrams

## Purpose

This folder contains visual representations of CrypSA concepts.

Diagrams are used to:

* illustrate architectural ideas
* clarify system relationships
* provide intuitive understanding of concepts

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Important

Diagrams in this folder are **illustrative only**.

They:

* do not define authoritative behavior
* do not introduce new rules
* do not override architecture or specification

For authoritative definitions, refer to:

* `../architecture/`
* `../spec/`

---

## 📍 Diagram Context

Diagrams are visual aids and must support specific documents.

---

### Primary References

Most diagrams support:

* `../CrypSA_Worked_Example.md` — step-by-step system flow
* `../CrypSA_Architecture_Overview.md` — system structure

---

### Authority Reminder

If a diagram conflicts with:

* architecture → follow architecture
* spec → follow spec

Diagrams must always align with the core documentation.

---

## Consistency Requirements

All diagrams must align with the core CrypSA architecture:

* **Truth** — validation and canonical event history
* **Translation** — adapters
* **Interpretation** — lenses
* **Experience** — UI and local simulation

And must reflect these core principles:

* **validation determines canonical truth**
* **canonical event history is the source of truth**
* **the validator is the authority over canonical events**
* **the invariant boundary defines where candidate events are evaluated before becoming canonical**
* **derived canonical state is not a source of truth and must be shown as reconstructed from canonical event history**

Diagrams must not introduce alternative models or terminology.

---

## Terminology Requirements

Diagrams must use consistent CrypSA terminology:

* use **validator**, not “server”, unless explicitly describing deployment
* “server” must never be used as a synonym for authority
* use **candidate event**, not generic “action” when crossing the invariant boundary
* use **canonical event history**, not “state” as a source of truth
* use **canonical_sequence** for ordering, not server_sequence or other alternatives

If “server” is used, it must be clear that:

> a server is a deployment of a validator, not the definition of the role

---

## Scope

Diagrams may:

* simplify concepts for clarity
* omit implementation details
* present high-level flows

Diagrams may represent either:

* flow (event flow, control flow)
* structure (layer relationships, system stack)

Diagrams must not:

* redefine architecture
* introduce new system behavior
* introduce new concepts not defined in architecture or spec
* specify implementation details that belong in `spec/` or `implementation/`

---

## Mermaid Guidelines

All diagrams should be compatible with GitHub’s Mermaid renderer.

Recommended practices:

* always wrap node labels in quotes
* use quoted subgraph names
* avoid parentheses in node labels
* keep labels simple and readable
* avoid complex or ambiguous syntax

---

## Relationship to Other Docs

* **architecture/** → defines structure and responsibilities
* **spec/** → defines behavior and rules
* **diagrams/** → visualizes those concepts

Diagrams should reflect the architecture and spec, not reinterpret them.

---

## One Sentence Summary

Diagrams visualize CrypSA concepts to aid understanding, but authoritative definitions and behavior are defined only in the architecture and spec layers, where validation defines what becomes canonical truth and canonical event history is the sole source of that truth.
