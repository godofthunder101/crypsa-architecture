# CrypSA Terminology Primer

This document defines the key terms used in CrypSA.

It is intended to:

- reduce ambiguity  
- align understanding  
- help experienced developers map CrypSA concepts to familiar patterns  

---

## Core Concepts

---

### Observer

An **observer** is a process (usually a client) that:

- reconstructs canonical state  
- simulates the world locally  
- proposes candidate events  
- reconciles with canonical truth  

An observer is not just a renderer.

> It is a simulator and interpreter of the universe.

---

### Canonical Server

The **canonical server** is responsible for:

- validating candidate events  
- enforcing invariants  
- recording accepted events  
- defining shared reality  

It does **not need to simulate the entire world**.

> It protects truth, not experience.

---

### Canonical Truth

**Canonical truth** is the authoritative definition of the world.

It is derived from:

- accepted canonical events  
- canonical ordering  

If something is not part of canonical history:

> it did not happen

---

### Canonical Event

A **canonical event** is a validated action that has been accepted by the server.

It:

- changes the canonical state  
- becomes part of the permanent event log  
- is used to reconstruct the world  

---

### Candidate Event

A **candidate event** is a proposed action created by an observer.

It represents:

> intent, not reality  

It must pass validation before becoming canonical.

---

### Invariants

**Invariants** are rules that must always remain true in canonical state.

Examples:

- a tile cannot contain two structures  
- ownership must be consistent  
- invalid transitions are not allowed  

If an event violates an invariant:

> it is rejected

---

### Derived State

**Derived state** is a materialized view of canonical history.

It exists to:

- improve performance  
- simplify queries  

It must always be:

> reproducible from canonical events

---

### Replay

**Replay** is the process of reconstructing state from canonical history.

CrypSA systems rely on:

- replay  
- snapshots  

to rebuild the world.

---

## Interpretation and Presentation

---

### Lens

A **lens** is an interpretation layer.

It transforms canonical state into observer-specific experience.

A lens may:

- filter information (e.g. fog of war)  
- determine what is visible  
- shape gameplay context  
- produce presentation-ready data  

A lens:

- does **not** define truth  
- does **not** validate events  
- does **not** mutate canonical state  

> A lens answers: “What does this mean to this observer?”

---

### Adapter

An **adapter** is a translation layer.

It prepares runtime and canonical data so that lenses and UI can consume it safely.

An adapter may:

- reshape data structures  
- aggregate multiple sources  
- normalize output formats  
- build view models  

An adapter:

- does **not** interpret meaning  
- does **not** validate events  
- does **not** mutate canonical state  

> An adapter answers: “How do we structure this data so it can be used?”

---

### Adapter vs Lens (Key Distinction)

| Concept  | Role |
|----------|------|
| Adapter  | Translates and shapes data |
| Lens     | Interprets and gives meaning |

---

Flow:

```text
Canonical State → Adapter → Lens → UI
````

---

## Runtime Concepts

---

### Validation

**Validation** is the process by which the server decides whether a candidate event is allowed.

It includes:

* schema checks
* identity checks
* precondition checks
* invariant checks
* rule checks

Only valid events become canonical.

---

### Reconciliation

**Reconciliation** is the process by which observers update local state to match canonical truth.

This occurs when:

* events are accepted
* events are rejected
* canonical state changes

---

### Branch

A **branch** represents a timeline or sequence of canonical events.

Branches allow:

* exploration of alternate histories
* replay from different points

---

### Snapshot

A **snapshot** is a stored canonical state at a specific point in history.

It allows:

* faster reconstruction
* late joining
* debugging

---

## Summary

CrypSA separates:

* **truth** (canonical events and validation)
* **structure** (adapters)
* **interpretation** (lenses)
* **experience** (UI and simulation)

---

## One Sentence Summary

CrypSA defines a system where canonical events determine truth, adapters shape data, lenses interpret it, and observers experience and simulate the resulting world.
