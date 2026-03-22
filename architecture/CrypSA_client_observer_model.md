# CrypSA Client / Observer Responsibility Model

## Purpose

This document defines the role of the client (observer) in a CrypSA system.

In CrypSA, observers simulate and interpret the world locally, while the server protects canonical truth.

This separation allows the universe to exist as shared canonical history rather than a centralized simulation.

---

## 📊 Observer vs Canonical Model

```mermaid
flowchart LR

subgraph Observer
A[Local Simulation]
B[Predicted Actions]
C[Local State]
D[Lens Interpretation]
end

subgraph Server
E[Validation Pipeline]
F[Canonical Event Log]
G[Derived Canonical State]
end

A --> B
B --> E

E -->|Accepted| F
E -->|Rejected| C

F --> G
G --> D
D --> C

````

---

## Core Principle

In CrypSA, the client is not a passive renderer.

It is an **observer-simulator** of the universe.

Observers:

* simulate world behavior locally
* interpret canonical history
* propose candidate events
* reconcile with canonical truth

---

## Observer Responsibilities

The CrypSA client performs several key roles.

---

### 1. Local Simulation

Observers simulate the world locally using canonical history.

Examples include:

* player movement
* physics interactions
* combat mechanics
* AI behavior
* environmental interactions

This allows gameplay to remain responsive without requiring constant server computation.

---

### 2. Canonical History Interpretation

Observers reconstruct the world state by interpreting canonical events.

Examples include:

* object creation (minting)
* item upgrades
* ownership transfers
* structure placement
* resource changes

Each observer builds a local representation of the universe from this history.

---

### 3. Lens-Based Interpretation

Observers interpret canonical reality through **lenses**.

A lens transforms canonical state into observer-specific experience.

Examples:

* visibility filtering (fog of war)
* interactable objects
* UI and presentation layers
* gameplay-specific interpretation

This allows different observers to experience the same canonical world differently without changing canonical truth.

---

### 4. Event Proposal

When a player performs an action, the observer generates a candidate event.

Examples:

* craft item
* upgrade object
* trade resources
* place structure
* destroy structure

These events are sent to the server for validation.

They are not canonical until accepted.

---

### 5. Reconciliation

Observers must reconcile their local simulation with canonical truth.

Reconciliation occurs when:

* an event is accepted
* an event is rejected
* another observer creates a canonical event

The observer updates its local state to match canonical history.

---

### 6. Prediction and Responsiveness

Observers may predict outcomes to keep gameplay responsive.

Examples:

* movement prediction
* action prediction
* interaction prediction

If predictions differ from canonical results, reconciliation corrects the simulation.

---

## Client State vs Canonical Truth

The client maintains a local interpretation of the world.

However:

> canonical truth is defined only by validated event history

Observers adjust their simulation whenever canonical truth changes.

---

## Client Data Types

Observers may maintain multiple layers of local data.

---

### Local Simulation State

* positions
* physics
* AI state
* combat state

---

### Canonical Object State

Derived from canonical history:

* ownership
* upgrade levels
* structures
* inventory

---

### Lens-Interpreted State

Produced by lenses:

* visible objects
* interactable elements
* UI-ready data
* player-specific views

---

### Presentation Data

* animations
* visual effects
* audio cues
* UI overlays

---

## Client Autonomy

Observers can operate with significant autonomy.

They can:

* simulate during latency
* predict outcomes
* maintain fluid gameplay

Canonical reconciliation ensures convergence across observers.

---

## Client Limitations

Observers cannot:

* create canonical truth directly
* bypass validation
* violate invariants
* modify canonical history

All canonical changes must be validated by the server.

---

## Observer Synchronization

Observers maintain synchronization through canonical updates.

Mechanisms may include:

* event broadcast
* event streams
* snapshot updates
* replay

Observers update their local simulation when canonical events change.

---

## Failure Scenarios

If a client disconnects:

* the canonical universe continues

When reconnecting:

* canonical history is replayed
* state is reconstructed

---

## Minimal Client Responsibilities

At minimum, a CrypSA observer must:

1. interpret canonical event history
2. simulate the world locally
3. apply lenses for interpretation
4. propose candidate events
5. reconcile with canonical truth
6. present the world to the player

---

## Server vs Client Responsibilities

| Responsibility            | Client | Server       |
| ------------------------- | ------ | ------------ |
| World simulation          | Yes    | Not required |
| Event proposal            | Yes    | No           |
| Event validation          | No     | Yes          |
| Invariant enforcement     | No     | Yes          |
| Canonical event recording | No     | Yes          |
| Local rendering           | Yes    | No           |
| Canonical authority       | No     | Yes          |

---

## Summary

In CrypSA, observers simulate and interpret the universe locally while the server protects canonical truth.

Observers reconstruct canonical history, apply lenses to interpret it, and maintain responsive local simulation.

The server validates events and defines what becomes real.

---

## Key Idea

A CrypSA client is not just a game client.

> It is an observer that simulates, interprets, and experiences a canonical universe.
