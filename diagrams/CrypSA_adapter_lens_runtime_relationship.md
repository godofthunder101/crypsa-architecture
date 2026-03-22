# CrypSA Adapter, Lens, and Runtime Relationship

This diagram shows how CrypSA separates:

- canonical truth  
- data shaping  
- interpretation  
- presentation  

---

```mermaid
flowchart LR

subgraph Runtime
A[Canonical Event Log]
B[Derived Canonical State]
C[Observer State]
end

subgraph Adapter Layer
D[Adapters]
end

subgraph Lens Layer
E[Lenses]
end

subgraph Presentation
F[UI / Player Experience]
end

A --> B
B --> D
C --> D

D --> E
E --> F

````

---

## How to Read This

### Runtime Layer

Defines truth and state:

* canonical events
* derived state
* observer-local state

---

### Adapter Layer

Prepares data for use:

* reshapes structures
* aggregates inputs
* normalizes outputs

---

### Lens Layer

Interprets data:

* determines visibility
* applies gameplay meaning
* produces observer-specific views

---

### Presentation Layer

Displays the world:

* UI
* visuals
* interaction

---

## Key Insight

> Truth, structure, and interpretation are separate responsibilities.

---

## One Sentence Summary

CrypSA separates canonical truth, data translation, interpretation, and presentation into distinct layers to preserve clarity and flexibility.
