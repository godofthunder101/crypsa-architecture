# CrypSA Architecture Overview

This document provides a high-level map of how CrypSA is structured.

It focuses on system structure rather than step-by-step flow.

For a worked example, see:

* `CrypSA_Worked_Example.md`

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## High-Level View

CrypSA is structured around four core responsibilities:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local interaction

These responsibilities are implemented across:

* observers
* the validator
* adapter layer
* lens layer
* UI / experience layer

---

## Core Components

### Observers

Observers:

* simulate the world locally
* generate candidate events
* maintain local prediction
* reconcile with canonical updates

They are responsible for local simulation and experience.

Observers do **not define truth**.

---

### Validator

The validator:

* receives candidate events
* validates them against invariants
* accepts or rejects them
* assigns canonical ordering (`canonical_sequence`)

Accepted events are appended to canonical event history, which defines what is true.

The validator is a **logical role**, not a specific machine.

It may run:

* locally (within an observer environment)
* remotely (as a dedicated server)

Its responsibilities do not change based on deployment.

---

### Server (Deployment Term)

A server is a deployment of a validator that runs remotely.

It is an infrastructure term, not an authority role.

Not all validators are servers, but all servers host a validator.

---

### Adapter Layer

Adapters:

* reshape canonical and observer data
* prepare structured outputs for interpretation and UI

Adapters are the **translation layer**.

They change structure, not meaning.
They do not define truth.

---

### Lens Layer

Lenses:

* interpret adapted data
* define meaning for an observer
* determine how data is understood in context

Lenses are the **interpretation layer**.

They do not define truth or mutate canonical data.

---

### UI / Observer Experience

The UI layer:

* renders the world
* handles input
* provides immediate feedback

This is the **experience layer**.

---

## Architectural Separation

CrypSA enforces strict separation of responsibilities:

| Responsibility | Layer                                |
| -------------- | ------------------------------------ |
| Truth          | Validation + canonical event history |
| Translation    | Adapters                             |
| Interpretation | Lenses                               |
| Experience     | UI / interaction                     |

This separation prevents:

* UI logic leaking into canonical truth
* validation becoming entangled with presentation
* interpretation being confused with data transformation

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
```

---

## Intent Flow (Simplified)

```mermaid
flowchart LR

A[User Action] --> B[Candidate Event]
B --> C[Validator]
C -->|Accepted| D[Canonical Event History]
C -->|Rejected| E[Rejection]
```

---

## Important Distinction

CrypSA separates:

* **what is true**
  from
* **how it is interpreted and experienced**

Truth is established through validation and recorded in canonical event history.

Derived canonical state is reconstructed via replay.

Everything else builds on that.

---

## Summary

CrypSA is structured around a clear separation of responsibilities:

* validation determines what becomes canonical truth
* canonical event history defines that truth
* adapters transform data
* lenses interpret meaning
* observers simulate and reconcile
* UI presents the experience

This separation makes the system predictable, debuggable, and extensible.
