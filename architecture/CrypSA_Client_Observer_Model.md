# CrypSA Client / Observer Responsibility Model

## Purpose

This document defines the role of the client (observer) in a CrypSA system.

Observers are responsible for reconstructing canonical reality, simulating the world locally, translating runtime data through adapters, interpreting that data through lenses, and presenting the result to the player.

The server validates events and maintains canonical event history.

---

## Core Principle

In CrypSA, the client is not a passive renderer.

It is an **observer-simulator** of the universe.

Observers:

* reconstruct derived canonical state locally from canonical event history
* simulate world behavior locally
* translate data through adapters
* interpret data through lenses
* propose candidate events
* reconcile with canonical event history

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

They do not control truth.

---

## Observer-Side Flow

A CrypSA observer operates in the following sequence:

1. reconstruct derived canonical state from canonical event history  
2. simulate the world locally  
3. translate data through adapters  
4. interpret data through lenses  
5. present the world to the player  
6. emit typed requests based on intent  
7. execute requests locally (prediction)  
8. reconcile with canonical event history  

This mirrors server-side validation on the truth layer.

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

This produces derived canonical state for local use.

---

### 2. Local Simulation

Observers simulate the world locally using derived canonical state as a foundation.

Examples:

* movement  
* physics  
* combat  
* AI behavior  
* environmental interaction  

This enables responsiveness without server-side simulation.

---

### 3. Translation (Adapters)

Observers use adapters to shape runtime and canonical data into stable, consumable forms.

Adapters:

* reshape data  
* preserve meaning  
* isolate internal structures  

Examples:

* world grid models  
* timeline/event views  
* interaction-ready structures  
* debug/inspection outputs  

Adapters do not define truth or interpretation.

---

### 4. Interpretation (Lenses)

Observers interpret data through lenses.

Lenses assign meaning to translated data.

Examples:

* visibility filtering  
* interactable objects  
* player-specific context  
* presentation-layer meaning  

Different observers may apply different lenses to the same canonical event history.

---

### 5. Event Proposal

Observers generate candidate events from player intent.

Examples:

* crafting  
* trading  
* placement  
* destruction  
* upgrades  

These are sent to the server for validation.

They are not canonical until accepted.

---

### 6. Reconciliation

Observers reconcile local simulation with canonical event history.

Reconciliation occurs when:

* events are accepted  
* events are rejected  
* new canonical events arrive  
* corrections occur  

The client adjusts its simulation to remain consistent.

---

### 7. Prediction and Responsiveness

Observers may predict outcomes to maintain responsiveness.

Examples:

* movement prediction  
* ability usage  
* interaction timing  

Prediction is always secondary to canonical event history.

---

## Client State vs Canonical Event History

The client maintains a local interpretation of the world.

This is not authoritative.

Canonical event history is defined by:

* validated events  
* server-enforced invariants  

Observers must adjust whenever canonical event history changes.

---

## Client Data Layers

Observers may maintain multiple layers of data:

### Derived Canonical State

Derived from canonical event history.

### Local Simulation State

Runtime-only simulation data.

### Adapter-Shaped Data

Structured, translation-layer outputs.

### Lens-Interpreted Data

Meaningful, observer-specific views.

### Presentation Data

UI, visuals, audio, and effects.

---

## Client Autonomy

Observers operate with high autonomy:

* continue during latency  
* simulate independently  
* predict outcomes  

Observer reconciliation ensures eventual consistency.

---

## Client Limitations

Observers cannot:

* create canonical event history directly  
* bypass invariant validation  
* alter shared state without server approval  

All canonical changes pass through validation.

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

If a client disconnects:

* canonical event history continues  

On reconnect:

* history is replayed  
* derived canonical state is reconstructed  
* adapters and lenses rebuild the view  

---

## Minimal Responsibilities

A CrypSA client must:

1. reconstruct derived canonical state from canonical event history  
2. simulate locally  
3. translate data (adapters)  
4. interpret data (lenses)  
5. present the world  
6. emit typed requests  
7. reconcile with canonical event history  

---

## Server vs Client Responsibilities

| Responsibility           | Client | Server       |
| ------------------------ | ------ | ------------ |
| Canonical reconstruction | Yes    | Yes          |
| Local simulation         | Yes    | Not required |
| Translation (adapters)   | Yes    | Not required |
| Interpretation (lenses)  | Yes    | Not required |
| Event proposal           | Yes    | No           |
| Event validation         | No     | Yes          |
| Invariant enforcement    | No     | Yes          |
| Canonical recording      | No     | Yes          |
| Rendering                | Yes    | No           |
| Truth authority          | No     | Yes          |

---

## Summary

Observers reconstruct canonical reality from canonical event history, simulate the world locally, translate and interpret data, and present the experience to the player.

The server validates events and maintains canonical event history.

Together, this enables a shared universe defined by event history rather than centralized simulation.

---

## Key Idea

A CrypSA client is not a renderer.

It is an observer that reconstructs, simulates, translates, interprets, and experiences a universe defined by canonical event history.
