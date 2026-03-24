# CrypSA System Stack Diagram

## Purpose

This diagram illustrates the layered structure of a CrypSA system.

It shows how CrypSA separates:

* observer experience
* interpretation
* data translation
* canonical event history

This separation allows observers to simulate locally while canonical event history remains consistent.

---

## Diagram

```mermaid
flowchart TB

subgraph "Experience Layer"
    A[UI and Observer Experience]
    B[Local Simulation and Feedback]
end

subgraph "Interpretation Layer"
    C[Lenses]
end

subgraph "Translation Layer"
    D[Adapters]
end

subgraph "Invariant Boundary"
    E[Candidate Events (Invariant Boundary)]
end

subgraph "Truth Layer"
    F[Validation and Invariant Enforcement]
    G[Canonical Event History]
end

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> A
````

---

## How to Read This

### Experience Layer

This layer includes:

* UI
* rendering
* input handling
* local simulation

It defines what the observer experiences.

---

### Interpretation Layer

Lenses:

* interpret data
* determine meaning
* define interaction

They shape how the observer understands the world.

---

### Translation Layer

Adapters:

* reshape data
* combine canonical and observer inputs
* prepare structured outputs

They isolate systems from raw runtime data.

---

### Invariant Boundary

The invariant boundary separates:

* local observer behavior
* canonical event history

When an interaction crosses this boundary:

* it becomes a candidate event
* it must be validated

---

### Truth Layer

The truth layer:

* validates events
* enforces invariants
* records canonical event history

Canonical event history defines shared reality.

---

## Key Insight

> CrypSA separates experience, interpretation, translation, and truth into distinct layers, with the invariant boundary controlling what becomes part of canonical event history.

---

## Relationship to Architecture

This diagram directly reflects:

* **Truth** → canonical events and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and simulation

---

## Why This Matters

This layered separation enables:

* responsive local simulation
* consistent shared reality
* modular system design
* scalable architecture

---

## One Sentence Summary

CrypSA structures systems into experience, interpretation, translation, and truth layers, with the invariant boundary ensuring only validated events become part of canonical event history.
