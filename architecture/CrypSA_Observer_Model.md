# CrypSA Observer Model

## Purpose

This document defines the role of the **observer** in a CrypSA system.

Observer behavior within the system is defined in the runtime model:

→ CrypSA_Runtime_Model.md

Observers are responsible for reconstructing canonical reality from canonical event history, simulating the world locally, translating runtime data through adapters, interpreting that data through lenses, and presenting the result to the player.

The validator validates events and maintains canonical event history.

---

## Defines

- The observer's architectural role within a CrypSA system
- Observer responsibilities and capabilities
- The observer-side state model and its relationship to canonical truth

---

## Does Not Define

- Canonical truth or validation authority (owned by the validator)
- Authoritative runtime behavior (defined in `/spec`)
- A single required implementation pattern for observers

---

## 📜 Authority Level

This document defines system structure and responsibilities.  
It does not define runtime behavior.  
The `/spec` directory is the **authoritative definition of runtime behavior**.

If there is any conflict, **the spec takes precedence**.

---

## Related Documents

- `spec/CrypSA_Validation_Model.md` — authoritative runtime validation behavior
- `architecture/CrypSA_Invariant_Boundary.md` — the invariant boundary the observer interacts with
- `architecture/CrypSA_Invariants_and_Design_Space.md` — CrypSA invariants and design space
- `architecture/CrypSA_Adapter_Model.md` — adapter responsibilities
- `architecture/CrypSA_Lens_Model.md` — lens responsibilities

---

## Core Principle

In CrypSA, the observer is not a passive renderer.

It is a system that **reconstructs and simulates a view of the universe** defined by canonical event history.

Observers:

* reconstruct derived canonical state locally from canonical event history  
* simulate world behavior locally (to a degree appropriate for the product)  
* translate data through adapters  
* interpret data through lenses  
* propose candidate events  
* reconcile with canonical event history  

Observers do not define truth.

---

## Architectural Position

CrypSA separates responsibilities into:

* **Truth** → canonical events and validation  
* **Translation** → adapters  
* **Interpretation** → lenses  
* **Experience** → UI and local simulation  

Observers operate across:

* translation  
* interpretation  
* experience  

They do not operate in the truth layer.

---

## Observer-Side Flow

This flow operates within the runtime model described in:

→ CrypSA_Runtime_Model.md

A CrypSA observer operates in the following sequence:

1. reconstruct derived canonical state from canonical event history  
2. simulate the world locally  
3. translate data through adapters  
4. interpret data through lenses  
5. present the world to the player  
6. emit candidate events representing intent  
7. apply local prediction based on those events  
8. reconcile with canonical event history  

This complements validator-side validation on the truth layer.

---

## Observer Responsibilities

### 1. Canonical State Reconstruction

Observers reconstruct the world from canonical event history.

Examples:

* object existence  
* ownership  
* structure placement  
* inventory contents  
* progression state  

This produces **derived canonical state** for local use.

---

### 2. Local Simulation

Observers simulate the world locally using derived canonical state as a foundation.

Examples:

* movement  
* physics  
* combat  
* AI behavior  
* environmental interaction  

This enables responsiveness without requiring validator-side simulation.

---

### 3. Translation (Adapters)

Observers use adapters to shape runtime and canonical data into stable, consumable forms.

Adapters:

* reshape data  
* preserve meaning  
* isolate internal structures  

Adapters do not define truth or interpretation.

---

### 4. Interpretation (Lenses)

Observers interpret data through lenses.

Lenses assign meaning to translated data.

Different observers may apply different lenses to the same canonical event history.

---

### 5. Event Proposal

Observers generate candidate events from player intent.

These are sent to the validator for validation.

They are not canonical until accepted.

---

### 6. Prediction and Responsiveness

Observers may predict outcomes to maintain responsiveness.

Prediction:

* occurs locally  
* is provisional  
* may be corrected  

Prediction never defines canonical truth and must be reconciled against it.

---

### 7. Reconciliation

Observers reconcile local state with canonical event history.

Reconciliation occurs when:

* events are accepted  
* events are rejected  
* new canonical events arrive  
* corrections occur  

The observer must adjust its state to remain consistent with canonical truth.

---

## Observer State Model

Observers may maintain multiple categories of state.

These categories define how observer-side data relates to canonical truth.

---

### Derived Canonical State

State reconstructed from canonical event history.

* must remain consistent with canonical history  
* forms the authoritative local baseline  

---

### Predicted State

Provisional state based on local prediction.

* improves responsiveness  
* may be corrected during reconciliation  
* never authoritative  

---

### Local-Only Runtime State

Runtime state used for simulation support or control.

Examples:

* input buffers  
* temporary physics values  
* AI working state  

* never canonical  
* never shared directly  

---

### Presentation State

Experience-layer state.

Examples:

* UI  
* animations  
* visual effects  
* audio  

* not authoritative  
* not part of canonical state  

---

### Important

👉 These categories may exist in different forms depending on the product.

👉 CrypSA defines their relationship to canonical truth, not a single implementation pattern.

---

## Observer and Canonical Truth

Observers maintain a local view of the world.

This view is not authoritative and must always yield to canonical event history.

Canonical event history is defined by:

* validated events  
* validator-enforced invariants  

---

## Observer Autonomy

Observers operate with high autonomy:

* continue during latency  
* simulate independently  
* predict outcomes  

However:

👉 autonomy exists only outside canonical authority  

Reconciliation ensures alignment with canonical truth.

---

## Observer Limitations

Observers cannot:

* create canonical event history directly  
* bypass invariant validation  
* alter shared state without validator approval  

👉 All canonical changes pass through the invariant boundary, where system invariants are enforced.

---

## Synchronization

Observers synchronize through canonical updates:

* event streams  
* polling or broadcast  
* reconciliation cycles  
* snapshot updates  

On update:

* canonical event history is extended  
* derived canonical state is updated  
* adapters reshape data  
* lenses reinterpret  
* presentation updates  

---

## Failure and Recovery

If an observer disconnects:

* canonical event history continues  

On reconnect:

* history is replayed  
* derived canonical state is reconstructed  
* adapters and lenses rebuild the view  

---

## Required Capabilities

A CrypSA observer must:

1. reconstruct derived canonical state from canonical event history  
2. simulate locally  
3. translate data (adapters)  
4. interpret data (lenses)  
5. present the world  
6. emit candidate events  
7. reconcile with canonical event history  

---

## Validator vs Observer Responsibilities

| Responsibility           | Observer | Validator    |
| ------------------------ | -------- | ------------ |
| Canonical reconstruction | Yes      | Not required |
| Local simulation         | Yes      | Not required |
| Translation (adapters)   | Yes      | Not required |
| Interpretation (lenses)  | Yes      | Not required |
| Event proposal           | Yes      | No           |
| Event validation         | No       | Yes          |
| Invariant enforcement    | No       | Yes          |
| Canonical recording      | No       | Yes          |
| Rendering                | Yes      | No           |
| Truth authority          | No       | Yes          |

---

## Summary

Observers reconstruct canonical reality from canonical event history, simulate the world locally, translate and interpret data, and present the experience.

The validator validates events and maintains canonical event history.

Together, this enables a shared universe defined by event history rather than centralized simulation.

---

## Key Idea

A CrypSA observer is not a renderer.

It is a system that reconstructs, simulates, translates, interprets, and experiences a universe defined by canonical event history.
