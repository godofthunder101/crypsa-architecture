# CrypSA Adapter, Lens, and Runtime Relationship

## Purpose

This diagram shows how CrypSA separates:

* **truth**
* **translation**
* **interpretation**
* **experience**

---

## 📊 System Relationship Diagram

```mermaid
flowchart LR

subgraph Truth Layer
A[Canonical Event History]
B[Derived Canonical State]
end

subgraph Observer (Local State)
C[Observer State]
end

subgraph Translation Layer
D[Adapters]
end

subgraph Interpretation Layer
E[Lenses]
end

subgraph Experience Layer
F[UI / Observer Experience]
end

A --> B
B --> D
C --> D

D --> E
E --> F
```

---

## How to Read This

### Truth Layer

The truth layer defines what is real.

* canonical event history is the source of truth
* derived state is a convenience for access and computation

---

### Observer State

Observers maintain local state such as:

* simulation
* prediction
* context

This state is not authoritative.

---

### Translation Layer (Adapters)

Adapters:

* reshape canonical and observer data
* prepare structured inputs
* isolate internal state

Adapters answer:

> “How should this data be structured?”

---

### Interpretation Layer (Lenses)

Lenses:

* interpret translated data
* determine visibility and interaction
* produce observer-specific meaning

Lenses answer:

> “What does this mean for this observer?”

---

### Experience Layer

The experience layer:

* renders the world
* handles interaction
* provides feedback

This is what the player experiences.

---

## Key Insight

> Truth, translation, interpretation, and experience are separate responsibilities.

---

## Simplified Flow

```text
Canonical Events → Derived State → Adapter → Lens → Experience
```

---

## Why This Matters

This separation enables:

* modular systems
* flexible client behavior
* clear debugging
* replayability
* independent evolution of layers

---

## One Sentence Summary

CrypSA separates canonical truth, data translation, interpretation, and experience into distinct layers so the system remains clear, modular, and extensible.

You’ve now eliminated almost all structural risk 👍
