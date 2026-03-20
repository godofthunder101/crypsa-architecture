# CrypSA Terminology Primer

CrypSA uses a small set of custom terms to describe its architecture.

These terms were created to better express the model, but many of them map closely to existing concepts in multiplayer systems, backend architecture, and event-sourced systems.

This document exists to:
- clarify what each term means
- map CrypSA terminology to familiar industry concepts
- reduce friction for experienced developers

---

## Core Mental Model (Quick Translation)

If you are familiar with existing systems, CrypSA can be roughly understood as:

- **Canonical Events** ≈ committed events in an event-sourced system  
- **Invariant Boundary** ≈ server-authoritative validation boundary  
- **Observer** ≈ client or simulation view  
- **Mint / Genome** ≈ schema + prefab/config system  
- **Event Lineage** ≈ event chain / causal history  

CrypSA’s main idea is:
> The shared world is defined by accepted events, not continuously synchronized state.

---

## Core Concepts

---

### Observer

**Definition:**
An Observer is any process that simulates or views the world locally.

**In practice:**
- usually a client
- may include tools, bots, or other systems

**Key idea:**
Observers can:
- simulate freely
- make local predictions
- propose actions

But they do **not define shared truth**.

**Closest industry concepts:**
- client
- local simulation
- prediction layer

---

### Canonical

**Definition:**
Canonical refers to the shared, authoritative state of the world.

This state is not directly stored as "live state", but is derived from accepted events.

**Key idea:**
Only server-accepted events become canonical.

**Closest industry concepts:**
- authoritative state
- committed state
- source of truth

---

### Canonical Event

**Definition:**
A Canonical Event is an action that has been validated and accepted into the shared world history.

**Key properties:**
- immutable once accepted
- part of the canonical event log
- used to reconstruct world state

**Closest industry concepts:**
- committed event (event sourcing)
- authoritative action
- validated server command

---

### Candidate (Event Candidate)

**Definition:**
A Candidate is a proposed action that has not yet become canonical.

**In practice:**
- created by an observer
- waits at the invariant boundary
- may be accepted or rejected

**Closest industry concepts:**
- client command
- pending action
- uncommitted event

---

### Invariant Boundary

**Definition:**
The Invariant Boundary is the point where actions must be validated before becoming part of shared truth.

**Key idea:**
Anything crossing this boundary must:
- obey rules
- be validated
- be accepted before affecting the canonical world

**Closest industry concepts:**
- server-authoritative validation layer
- rule enforcement boundary
- transaction validation point

---

### Event Lineage

**Definition:**
Event Lineage is the chain of events that defines how the current state was reached.

In CrypSA, lineage is explicitly tracked and can branch when history is revisited.

**Key idea:**
- state is derived from history
- different historical paths can exist
- lineage determines replay order

**Closest industry concepts:**
- event chain
- causal history
- commit history (like Git, but for world state)

---

### Replay

**Definition:**
Replay is the process of reconstructing canonical state by applying events in lineage order.

**Key idea:**
The world is not stored as a final state — it is rebuilt from events.

**Closest industry concepts:**
- event replay (event sourcing)
- state reconstruction
- deterministic rebuild

---

## Mint System

---

### Mint

**Definition:**
Mint is the system used to define what kinds of objects can exist in the world.

It acts as a registry of object definitions.

**Key idea:**
- defines object behavior and rules
- controls what can be created in the world
- evolves over time

**Closest industry concepts:**
- schema registry
- prefab system
- data-driven entity definitions

---

### Genome

**Definition:**
A Genome is the full definition/configuration of an object type.

This includes:
- rules
- allowed actions
- state transitions
- invariant constraints

**Key idea:**
A Genome describes what an object *is allowed to be and do*.

**Closest industry concepts:**
- prefab definition
- JSON config
- schema + ruleset

---

### Mint Catalog

**Definition:**
The Mint Catalog is the collection of all available object definitions.

**Key idea:**
- acts as a registry of available object types
- can be edited to affect future objects
- does not retroactively change existing canonical objects

**Closest industry concepts:**
- definition database
- asset registry
- schema store

---

## Important Notes

---

### CrypSA is Event-Driven, Not State-Driven

Traditional systems:
- synchronize state continuously

CrypSA:
- accepts events
- derives state from those events

---

### Canonical ≠ Local

Observers can:
- move freely
- simulate freely

But:
- only accepted events affect the shared world

---

### This Terminology is Intentional

CrypSA uses custom terms to:
- separate concepts cleanly
- avoid overloading existing terminology
- describe systems that don’t map perfectly to one existing pattern

However, these terms are always grounded in real system concepts, and can be translated as shown above.

---

## Final Summary

If you prefer familiar language:

CrypSA is essentially:

> An event-sourced, server-validated, client-simulated architecture  
> where accepted events define shared reality, and state is reconstructed from history.

The custom terminology exists to make that model easier to reason about — not to replace existing knowledge.

---
