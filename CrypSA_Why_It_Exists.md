# CrypSA — Why It Exists

This document explains why CrypSA was created, not where it should be used.

---

## Purpose

CrypSA was designed to address structural limitations in traditional multiplayer and distributed simulation architectures, particularly when building large persistent digital worlds.

The goal of CrypSA is to provide a model where digital universes remain:

* structurally consistent
* scalable
* persistent
* reconstructable

without requiring centralized continuous simulation.

---

## The Traditional Multiplayer Model

Most multiplayer systems rely on centralized authority and continuous simulation.

```text id="7j5g0p"
Players
↓
Clients
↓
Central Authority (Server)
↓
Game Database
```

In this model:

* a central system simulates the world
* clients send inputs
* interactions are resolved centrally
* state is continuously synchronized

This model works well for many games, but it has structural limitations as worlds become large, persistent, and complex.

---

## The Scaling Problem

Centralized simulation introduces several problems as worlds grow.

---

### Continuous Simulation Load

A centralized system must continuously simulate:

* physics
* AI
* world interactions
* object state

As the number of players and objects increases, workload grows dramatically.

---

### Synchronization Complexity

Large worlds require constant synchronization of mutable state across many clients.

This leads to:

* network congestion
* synchronization errors
* complex reconciliation logic

---

### Infrastructure Coupling

When the system responsible for maintaining canonical truth is removed, the world disappears.

More precisely:

> the canonical event history of the world is lost

Persistent worlds are therefore tied to:

* specific deployments
* specific implementations
* specific engine architectures

This limits long-term persistence.

---

## The Persistence Problem

Many online worlds are effectively temporary systems.

If the infrastructure maintaining them disappears, the universe itself is lost.

This raises an important question:

> Can a digital universe exist independently of the system that enforces it?

CrypSA attempts to answer yes.

---

## The CrypSA Approach

CrypSA introduces a different architectural model.

Instead of synchronizing full world simulation, CrypSA synchronizes:

* canonical event history

And enforces:

* canonical identities
* canonical invariants

Observers reconstruct the world locally via replay.

A **validator** focuses on:

* validating candidate events
* enforcing invariants
* maintaining canonical event history

---

## Separating Experience From Truth

CrypSA separates two concerns:

**Observer Experience**
vs
**Canonical Reality (defined by canonical event history)**

Observers simulate locally.

Canonical event history evolves only through validated events.

This removes the need for continuous centralized simulation of the entire world.

---

## The Invariant Boundary

The central concept of CrypSA is the invariant boundary.

Every interaction asks:

> Does this interaction affect canonical event history?

If no:

* it remains local

If yes:

* it becomes a candidate event
* it must be validated before becoming canonical

---

## Event-Driven Universe Evolution

CrypSA evolves the universe through validated events.

```text id="z0f9vr"
Candidate Event
↓
Validation
↓
Canonical Event
↓
Canonical Event History (extended)
```

Derived canonical state evolves through replay.

---

## A More Durable World Model

Because CrypSA records canonical structure rather than full simulation state, a universe can persist independently of any specific deployment.

The world is defined by:

* identities
* invariants
* canonical event history

These components allow the universe to be reconstructed through replay, even if the underlying infrastructure changes.

---

## Toward Persistent Digital Universes

CrypSA is motivated by the idea that digital worlds should not be tied to a single system or deployment.

Instead, they should be defined by a structural model of reality that can be reconstructed and preserved over time.

CrypSA proposes an architecture that makes this possible.

---

## Summary

CrypSA exists because traditional architectures struggle to support large persistent digital universes.

By separating local simulation from canonical event history and evolving the universe through validated events, CrypSA provides a scalable and durable model for shared digital worlds.

---

## One Sentence Summary

CrypSA exists to enable persistent digital universes that remain structurally consistent and reconstructable through canonical event history and replay, without relying on centralized continuous simulation.
