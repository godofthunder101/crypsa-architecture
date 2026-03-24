# CrypSA Universe Model

> Exploratory note: This document represents early conceptual framing.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_Why_It_Exists.md`
> * `../../CrypSA_Where_It_Fits.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document presents a conceptual model of how a CrypSA universe is structured.

Rather than representing a universe as continuously simulated state, CrypSA represents a universe as:

> canonical event history from which observers reconstruct the world

This is a conceptual model, not an authoritative system definition.

---

## Diagram

```mermaid
flowchart TD

A[Observers] --> B[Local Simulation]
B --> C[Invariant Boundary]
C -->|Candidate Event| D[Validation]
D -->|Accepted| E[Canonical Event History]
E --> F[Object Reconstruction]
F --> G[Observer Experience]
G --> B
````

---

## How to Read This

### Observers

Observers (players, systems, tools):

* reconstruct the universe
* simulate locally
* interact with the world

---

### Local Simulation (Experience)

Observers simulate:

* movement
* rendering
* prediction
* temporary effects

This provides responsiveness without requiring centralized simulation.

---

### Invariant Boundary

The invariant boundary determines:

> Does this interaction affect canonical event history?

* No → remains local
* Yes → becomes a candidate event

---

### Validation (Truth Layer)

The server validates candidate events:

* enforces invariants
* checks rules
* determines acceptance

Accepted events are appended to canonical event history.

---

### Canonical Event History

Canonical event history defines shared reality.

Examples:

* object minting
* structure placement
* resource collection
* ownership transfer

This history is:

* ordered
* append-only
* authoritative

---

### Object Reconstruction

Observers reconstruct objects using:

```text
identity + genome + canonical event history → derived canonical state
```

Objects are defined by their history, not stored mutable state.

---

### Observer Experience Loop

Observers continuously:

* reconstruct
* simulate
* interact
* submit candidate events for validation when crossing the invariant boundary

This creates a loop between local simulation and canonical event history.

---

## Timeline Structure (Exploratory)

A CrypSA universe can be viewed as a timeline of events.

In exploratory or advanced scenarios, alternate branches may exist for:

* debugging
* experimentation
* simulation forks

This is not part of the minimal v0.1 runtime model.

---

## Key Idea

> A CrypSA universe is defined by canonical event history, not by a single stored world state.

Observers reconstruct the universe by interpreting that history.

---

## Relationship to Architecture

This conceptual model maps to:

* **Experience** → local simulation and UI
* **Interpretation** → lenses (not shown in diagram)
* **Translation** → adapters (not shown in diagram)
* **Truth** → validation and canonical event history

---

## Summary

CrypSA transforms how persistent worlds are represented.

Instead of:

```text
Server → World State
```

CrypSA uses:

```text
Canonical Event History → Reconstructed Universe
```

This enables:

* distributed simulation
* deterministic reconstruction
* persistent world history
* scalable system design

---

## One Sentence Summary

A CrypSA universe is defined by canonical event history, and observers reconstruct and experience that universe through local simulation and interpretation.
