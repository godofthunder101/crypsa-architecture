# Diagrams

## Purpose

This folder contains visual representations of CrypSA concepts.

Diagrams are used to:

* illustrate architectural ideas
* clarify system relationships
* provide intuitive understanding of concepts

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

## Consistency Requirements

All diagrams must align with the core CrypSA architecture:

* **Truth** — canonical events and validation
* **Translation** — adapters
* **Interpretation** — lenses
* **Experience** — UI and local simulation

Diagrams must not introduce alternative models or terminology.

---

## Scope

Diagrams may:

* simplify concepts for clarity
* omit implementation details
* present high-level flows

Diagrams must not:

* redefine architecture
* introduce new system behavior
* specify implementation details that belong in `spec/` or `implementation/`

---

## Mermaid Guidelines

All diagrams should be compatible with GitHub’s Mermaid renderer.

Recommended practices:

* use quoted subgraph names
* avoid parentheses in node labels
* keep labels simple and readable
* avoid complex or ambiguous syntax

---

## Relationship to Other Docs

* **architecture/** → defines structure and responsibilities
* **spec/** → defines behavior and rules
* **diagrams/** → visualizes those concepts

---

## One Sentence Summary

Diagrams visualize CrypSA concepts to aid understanding, but authoritative definitions and behavior are defined only in the architecture and spec layers.
