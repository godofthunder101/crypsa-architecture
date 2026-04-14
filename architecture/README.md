# CrypSA Architecture

## Purpose

This section explains how CrypSA works as a system.

It focuses on **structure and relationships**, not step-by-step execution.

This folder is part of the **authoritative architecture layer**.

Other documents must not redefine the concepts described here.

For the authoritative conceptual flow of the system, see:

→ CrypSA_Runtime_Model.md

---

## 📜 Authority Level

The CrypSA documentation is structured as:

* `/spec` — authoritative definition of runtime behavior
* `/architecture` — system structure and conceptual models

The runtime model (`CrypSA_Runtime_Model.md`) defines the authoritative conceptual flow of the system.

If there is any conflict:

* spec takes precedence over architecture
* architecture takes precedence over all other documents in this repository

---

## Core Idea

CrypSA structures multiplayer systems around **validated events as truth**.

* actions become **candidate events**
* the **validator** defines what becomes canonical
* accepted events form **canonical event history**

> **The shared world is defined by canonical event history, not synchronized state.**
> Canonical event history is the source of truth.

---

## System Flow (High-Level)

At a system level, everything follows this flow:

1. Observer simulates locally
2. Observer proposes a **candidate event**
3. Validator evaluates the event
4. If accepted, an event becomes canonical and is appended to canonical event history
5. Observers reconcile to canonical truth

This defines the boundary between:

* local simulation
* canonical reality

---

## Four Responsibilities (Mental Model)

CrypSA is organized into four responsibilities:

* **Truth** → canonical event history and validation
* **Translation** → adapters shaping runtime data
* **Interpretation** → lenses determining meaning
* **Experience** → UI and local simulation

These responsibilities define the architecture.

For strict separation of these responsibilities, see:

→ CrypSA_Boundary_Definitions.md

---

## Key Architectural Ideas

---

### Event-Based Truth

CrypSA is event-driven:

* actions → candidate events
* validation → canonical events (assigned `canonical_sequence`)
* canonical events → canonical event history

Canonical event history defines **truth**.

---

### Validation as Authority

The **validator** operates in the **truth layer**.

It:

* validates candidate events
* enforces invariants
* determines what becomes canonical

> The validator defines what becomes canonical.

The validator enforces the invariant boundary — where candidate events become canonical or are rejected.

It is a **role**, not a location.

---

### Observer-Side Simulation

Observers:

* reconstruct derived canonical state
* simulate the world locally
* respond immediately to input
* reconcile when canonical updates arrive

This provides responsiveness without sacrificing consistency.

---

### Replay as State

State is not stored as truth.

* canonical event history is authoritative
* derived canonical state is reconstructed via replay

> Derived canonical state is a projection of canonical event history. It is not the source of truth.

Replay enables:

* deterministic reconstruction
* debugging
* verification

---

### Adapters (Translation Layer)

Adapters:

* reshape canonical and observer/runtime data
* prepare structured outputs
* isolate internal data from interpretation

They belong to the **translation layer**.

---

### Lenses (Interpretation Layer)

Lenses:

* interpret translated data
* determine meaning, relevance, and context
* produce observer-specific views

They belong to the **interpretation layer**.

---

### Experience Layer

The experience layer:

* renders the world
* handles input
* provides immediate feedback

It is:

* responsive
* local
* non-authoritative

---

## Layer Relationship (Simplified)

```mermaid
flowchart LR

A["Canonical Event History"] --> B["Derived Canonical State"]
B --> C["Adapters"]
C --> D["Lenses"]
D --> E["UI / Experience"]
````

---

## Why This Architecture Exists

Separating responsibilities enables:

* deterministic reconstruction
* responsive local simulation
* clear debugging via event history
* multiple observer perspectives
* independent evolution of layers

---

## Relationship to Other Documents

This document defines **structure and relationships**.

For other aspects:

* Runtime behavior → `/spec/`
* Conceptual flow → `CrypSA_Runtime_Model.md`
* Responsibility boundaries → `CrypSA_Boundary_Definitions.md`
* Concepts and definitions → Terminology Primer
* End-to-end flow → Worked Example

---

## Where to Go Next

* `CrypSA_Runtime_Model.md` — authoritative conceptual flow
* `CrypSA_Architecture_Overview.md` — system overview
* `CrypSA_Boundary_Definitions.md` — responsibility boundaries
* `../spec/CrypSA_Event_Model.md` — event structure
* `../spec/CrypSA_Validation_Model.md` — invariant enforcement
* `../spec/CrypSA_Replay_Model.md` — state reconstruction
