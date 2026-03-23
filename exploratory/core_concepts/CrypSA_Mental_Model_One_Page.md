---

CrypSA Mental Model (One Page)

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to `../../CrypSA_In_5_Minutes.md`, `../../architecture/`, and `../../spec/`.

Purpose

This document provides a concise mental model for understanding CrypSA architecture.

CrypSA is a system for building persistent shared digital worlds that remain consistent, verifiable, and scalable without requiring the server to simulate everything.

Instead of continuously simulating the entire universe, CrypSA defines a shared canonical truth and allows observers to reconstruct and simulate the world locally.


---

The Core Idea

CrypSA separates local experience from canonical truth.

Observers simulate and experience the world locally, but only validated events can change the shared universe.

Local Simulation
      ↓
Invariant Boundary Check
      ↓
Server Validation
      ↓
Canonical Truth Updated
      ↓
Observers Reconstruct World

This architecture allows large worlds to exist without forcing the server to simulate every detail.


---

The Five Core Concepts

Understanding CrypSA requires only five key ideas.


---

1. Observers

An observer is any system that reconstructs and experiences the universe.

Examples include:

players

AI agents

servers

simulation tools

replay systems


Observers build their own local view of the world from canonical data.


---

2. Identity

Every canonical object has a unique identity.

Identity answers the question:

What object is this?

Identity never changes.

Example identities might represent:

a sword

a building

a creature

a resource node


Identity anchors an object in canonical reality.


---

3. Genome

A genome defines the structural rules for an object.

It describes what the object is capable of and how it behaves.

Examples of genome rules:

what states the object can have

what actions it can perform

how it interacts with other objects

what invariants must never be violated


Genomes act like structural blueprints.


---

4. Invariants

An invariant is a rule that must always remain true in the canonical universe.

Examples:

an item cannot exist in two inventories at once

an object cannot occupy two exclusive states simultaneously

ownership relationships must remain consistent


The invariant system protects the structural integrity of the universe.


---

5. Events

An event represents a proposed change to canonical reality.

Examples include:

picking up an item

transferring ownership

building a structure

discovering a location


Events do not automatically become truth.

They must be validated before they are accepted.


---

The Invariant Boundary

The most important concept in CrypSA is the invariant boundary.

Every interaction must answer one question:

Does this interaction affect canonical truth?

If the answer is no, the result remains local.

If the answer is yes, the interaction becomes a candidate canonical event.


---

Canonical Validation

When an event crosses the invariant boundary, the server performs validation.

Typical validation checks include:

identity exists

genome rules permit the action

invariants are not violated

contextual conditions are satisfied


If validation fails, the event is rejected.

If validation succeeds, the event becomes canonical truth.


---

Canonical State Evolution

The universe evolves through validated events.

State S0
  ↓
Validated Event
  ↓
State S1
  ↓
Validated Event
  ↓
State S2

Each accepted event moves the universe to the next canonical state.


---

Observer Reconstruction

Observers rebuild their world view from canonical data.

This typically includes:

Identity
+ Genome
+ Invariant State
+ Event History

Because reconstruction is deterministic, observers converge on a consistent structural reality.


---

Why CrypSA Works

CrypSA works because it avoids the most expensive part of traditional multiplayer architecture: centralized continuous simulation.

Instead, it ensures:

canonical truth is protected

observers can simulate locally

validation occurs only when necessary

the universe evolves through verified transitions


This allows persistent worlds to scale while remaining structurally consistent.


---

The CrypSA Loop

The runtime loop of a CrypSA universe looks like this:

Observer reconstructs world
        ↓
Observer simulates locally
        ↓
Interaction occurs
        ↓
Invariant boundary check
        ↓
If canonical → validate event
        ↓
Canonical truth updated
        ↓
Observers reconstruct

This loop repeats continuously.


---

One Sentence Summary

CrypSA is an architecture where observers simulate the world locally, but only validated events that respect invariant rules are allowed to change the shared canonical universe.


---
