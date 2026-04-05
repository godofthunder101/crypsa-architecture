# CrypSA Architecture

## Purpose

This section explains how CrypSA works as a system.

It focuses on **structure and relationships**, not step-by-step execution.

This folder is part of the **authoritative architecture layer**.

Other documents must not redefine the concepts described here.

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Core Idea

CrypSA structures multiplayer systems around **validated events as truth**.

* actions become **candidate events**
* the **validator** determines what becomes canonical
* accepted events form **canonical event history**

> **The shared world is defined by canonical event history, not synchronized state.**

---

## System Flow (High-Level)

At a system level, everything follows this flow:

1. Observer simulates locally
2. Observer proposes a **candidate event**
3. Validator evaluates the event
4. Accepted events become **canonical**
5. Canonical events are appended to **canonical event history**
6. Observers reconcile to canonical truth

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

> The validator defines truth.

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
* state is reconstructed via replay

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

```mermaid id="f1y8qk"
flowchart LR

A[Canonical Event History] --> B[Derived Canonical State]
B --> C[Adapters]
C --> D[Lenses]
D --> E[UI / Experience]
```

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
* Concepts and definitions → Terminology Primer
* End-to-end flow → Worked Example

---

## Where to Go Next

* `CrypSA_Architecture_Overview.md` — system overview
* `../spec/CrypSA_Event_Model.md` — event structure
* `../spec/CrypSA_Validation_Model.md` — invariant enforcement
* `../spec/CrypSA_Replay_Model.md` — state reconstruction
