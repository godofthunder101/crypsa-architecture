# CrypSA Adapter, Lens, and Runtime Relationship

This diagram shows how CrypSA separates:

- canonical truth  
- data shaping  
- interpretation  
- presentation  

---

## 📊 System Relationship Diagram

```mermaid
flowchart LR

subgraph Runtime
A[Canonical Event Log]
B[Derived Canonical State]
end

subgraph Observer
C[Observer State]
end

subgraph Adapter Layer
D[Adapters]
end

subgraph Lens Layer
E[Lenses]
end

subgraph Presentation
F[UI / Observer Experience]
end

A --> B
B --> D
C --> D

D --> E
E --> F
````

---

## How to Read This

### Runtime (Truth Layer)

The runtime defines what is real:

* canonical event log is the source of truth
* derived canonical state is a materialized view

---

### Observer State

The observer maintains local state such as:

* simulation state
* prediction state
* selection/context

This state is combined with canonical state for interpretation.

---

### Adapter Layer (Translation)

Adapters prepare data for use:

* reshape canonical state
* combine observer and canonical data
* produce structured outputs

Adapters answer:

> “How should this data be structured for use?”

---

### Lens Layer (Interpretation)

Lenses interpret adapted data:

* determine visibility
* define gameplay meaning
* produce observer-specific views

Lenses answer:

> “What does this data mean for this observer?”

---

### Presentation (Experience Layer)

The UI renders the result:

* visuals
* interaction
* feedback

This is what the player experiences.

---

## Key Insight

> Truth, structure, interpretation, and presentation are separate responsibilities.

---

## Simplified Flow

```text
Canonical Events → Derived State → Adapter → Lens → UI
```

---

## Why This Matters

This separation allows CrypSA systems to be:

* flexible
* debuggable
* replayable
* modular

Each layer can evolve independently without breaking the others.

---

## One Sentence Summary

CrypSA separates canonical truth, data translation, interpretation, and presentation into distinct layers so that the system remains clear, modular, and extensible.
