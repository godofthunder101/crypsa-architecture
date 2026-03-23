# CrypSA Architecture Overview

This document provides a high-level map of how CrypSA is structured.

It is intentionally focused on system structure rather than step-by-step flow.

For a worked example, see:

- `CrypSA_WORKED_EXAMPLE.md`

---

## High-Level View

CrypSA is best understood as four core responsibilities:

- **Truth** — canonical events and validation  
- **Translation** — adapters shaping runtime data  
- **Interpretation** — lenses determining observer meaning  
- **Experience** — UI and local simulation  

These responsibilities are implemented across different parts of the system:

- observers (clients)
- canonical server
- adapter layer
- lens layer
- UI / observer experience

---

## Core Components

### Observers (Clients)

Observers:

- simulate the world locally  
- generate candidate events  
- render the world to the player  
- reconcile with canonical updates  

They are responsible for the **experience layer** and parts of interpretation.

---

### Canonical Server

The server:

- receives candidate events  
- validates them against invariants  
- accepts or rejects them  
- assigns canonical order  

The server defines **truth**.

---

### Adapter Layer

Adapters:

- reshape canonical and observer state  
- combine runtime data into structured forms  
- prepare data for interpretation and UI  

Adapters are the **translation layer**.

They do not define truth.

---

### Lens Layer

Lenses:

- interpret adapted data  
- determine what an observer sees  
- define interaction meaning  

Lenses are the **interpretation layer**.

They do not define truth or mutate runtime state.

---

### UI / Observer Experience

The UI layer:

- renders the world  
- handles input  
- provides immediate feedback  
- drives local simulation  

This is the **experience layer**.

---

## Architectural Separation

The key idea in CrypSA is that these responsibilities remain separate:

| Responsibility | Layer |
|------|--------|
| Truth | Canonical events + validation |
| Translation | Adapters |
| Interpretation | Lenses |
| Experience | UI / local simulation |

This separation prevents:

- UI logic leaking into runtime truth  
- validation becoming entangled with presentation  
- interpretation being confused with data shaping  

---

## Why This Structure Exists

Traditional architectures often combine:

- simulation
- validation
- rendering

into tightly coupled systems.

CrypSA separates them to:

- improve clarity  
- enable deterministic replay  
- support multiple observer views  
- allow independent evolution of layers  

---

## Data Flow (Simplified)

```mermaid
flowchart LR

A[Canonical Events] --> B[Derived State]
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
C -->|Accepted| D[Canonical Events]
C -->|Rejected| E[Rejection]
```

---

## Important Distinction

CrypSA separates:

* **what is true**
  from
* **how it is seen**

Truth lives in canonical history.

Everything else derives from it.

---

## Summary

CrypSA is structured around a clear separation of responsibilities:

* canonical events define truth
* adapters translate data
* lenses interpret meaning
* observers experience and simulate the world

This separation is what makes the system predictable, debuggable, and extensible.
👉 `CrypSA_Terminology_Primer.md` (very small but important alignment tweak)
```
