# CrypSA Architecture Overview

This document provides a high-level map of how CrypSA is structured.

It is intentionally focused on system structure rather than step-by-step flow.

For a worked example, see:

* `CrypSA_Worked_Example.md`

---

## High-Level View

CrypSA is best understood as four core responsibilities:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining observer meaning
* **Experience** — UI and local interaction

These responsibilities are implemented across different parts of the system:

* observers (clients)
* the server
* adapter layer
* lens layer
* UI / observer experience

---

## Core Components

### Observers (Clients)

Observers:

* simulate the world locally
* generate candidate events
* maintain local prediction
* reconcile with canonical updates

They are responsible for local simulation and parts of interpretation.

---

### Server

The server:

* receives candidate events
* validates them against invariants
* accepts or rejects them
* assigns canonical ordering (`server_sequence`)

The server enforces validation and ordering.

Canonical event history defines what is true.

---

### Adapter Layer

Adapters:

* reshape canonical and observer state
* combine canonical and observer data
* prepare structured outputs for interpretation and UI

Adapters are the **translation layer**.

They do not define truth.

---

### Lens Layer

Lenses:

* interpret adapted data
* determine what an observer sees
* define interaction meaning

Lenses are the **interpretation layer**.

They do not define truth or mutate runtime state.

---

### UI / Observer Experience

The UI layer:

* renders the world
* handles input
* provides immediate feedback

This is the **experience layer**.

---

## Architectural Separation

The key idea in CrypSA is that these responsibilities remain separate:

| Responsibility | Layer                                   |
| -------------- | --------------------------------------- |
| Truth          | Canonical event history + validation     |
| Translation    | Adapters                                |
| Interpretation | Lenses                                  |
| Experience     | UI / interaction                        |

This separation prevents:

* UI logic leaking into runtime truth
* validation becoming entangled with presentation
* interpretation being confused with data shaping

---

## Why This Structure Exists

Traditional architectures often combine:

* simulation
* validation
* rendering

into tightly coupled systems.

CrypSA separates them to:

* improve clarity
* enable deterministic replay
* support multiple observer perspectives
* allow independent evolution of layers

---

## Data Flow (Simplified)

```mermaid
flowchart LR

A[Canonical Event History] --> B[Derived Canonical State]
B --> C[Adapters]
C --> D[Lenses]
D --> E[UI / Experience]
````

---

## Intent Flow (Simplified)

```mermaid
flowchart LR

A[User Action] --> B[Candidate Event]
B --> C[Validation]
C -->|Accepted| D[Canonical Event History]
C -->|Rejected| E[Rejection]
```

---

## Important Distinction

CrypSA separates:

* **what is true**
  from
* **how it is seen**

Truth lives in canonical event history.

Derived canonical state is reconstructed via replay.

Everything else builds on that.

---

## Summary

CrypSA is structured around a clear separation of responsibilities:

* canonical event history defines truth
* adapters translate data
* lenses interpret meaning
* observers simulate and reconcile
* UI presents the experience

This separation is what makes the system predictable, debuggable, and extensible.
