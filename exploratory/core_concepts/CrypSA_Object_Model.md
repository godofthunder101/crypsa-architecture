CrypSA Object Model

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to `../../CrypSA_In_5_Minutes.md`, `../../architecture/`, and `../../spec/`.

Purpose

This document defines the structure of objects within a CrypSA system.

In CrypSA, objects are not stored as continuously updated mutable state.
Instead, objects are reconstructed deterministically from:

identity

genome

canonical invariant state

event history


This model allows objects to remain consistent across all observers while minimizing the need for centralized simulation.


---

Core Principle

A CrypSA object is not defined by its current state alone.

Instead:

> A CrypSA object is a deterministic reconstruction of identity + genome + validated history.




---

Object Components

Every canonical object in CrypSA is defined by four core components.


---

1. Identity

The identity uniquely defines the object.

Examples:

player_17

sword_4821

structure_slot_42


Properties:

immutable

globally unique (within canonical scope)

issued or recognized by the canonical mint


The identity ensures that all observers refer to the same object.


---

2. Genome

The genome defines the structural rules of the object.

It describes:

what the object is

how it behaves

how it can evolve

what transitions are valid


Examples:

Sword Genome:
- max durability
- allowed upgrades
- ownership rules

Structure Slot Genome:
- buildable or not
- allowed structure types
- spatial constraints

The genome is deterministic and shared across observers.


---

3. Canonical Invariant State

This represents the current accepted canonical state of the object.

Examples:

current owner

current durability

structure type placed

upgrade level


This state is not arbitrary — it is always the result of validated events.


---

4. Event History

The event history defines how the object has evolved over time.

Examples:

mint → upgrade → transfer → upgrade → damage

This history is:

canonical (server-validated)

ordered

append-only (conceptually)


The history allows reconstruction of the object at any point in time.


---

Object Reconstruction

Observers reconstruct objects using:

identity
+ genome
+ canonical invariant state
+ event history

This allows:

consistent object state across clients

deterministic replay

temporal inspection

reduced need for full state synchronization



---

Example: Sword Lifecycle

Step 1 — Mint

identity: sword_1001
genome: sword_type_A
state: base sword


---

Step 2 — Upgrade

Event:

upgrade → +sharpness

State becomes:

sharpness_level = 1


---

Step 3 — Ownership Transfer

Event:

transfer → player_B

State becomes:

owner = player_B


---

Step 4 — Reconstruction

Any observer can reconstruct the sword:

identity → sword_1001
genome → sword_type_A
history → [mint, upgrade, transfer]
state → derived from validated events

All observers arrive at the same result.


---

Relationship to the Mint

The mint defines:

valid identities

valid genomes


The object model uses those definitions to reconstruct objects.

The mint answers:

"What is allowed to exist?"

The object model answers:

"What does this object currently represent?"


---

Relationship to Invariants

Invariants ensure that object transitions remain valid.

Examples:

cannot upgrade a non-existent object

cannot transfer ownership without owning the object

cannot place a structure in an invalid location


The object model relies on invariants to ensure that its history remains valid.


---

Relationship to Event Lifecycle

Objects evolve through events.

Event → validated → recorded → affects object state

The object model is the result of this process.


---

Client vs Server Perspective

Client

reconstructs objects

simulates interactions

predicts outcomes


Server

validates events affecting objects

enforces invariants

records canonical history


The object model is shared, but authority differs.


---

Object Stability

Because identity and genome are stable:

objects remain consistent across observers

objects can be reconstructed at any time

objects do not depend on continuous simulation


This provides long-term persistence.


---

Temporal Reconstruction

Because objects are event-driven, they can be reconstructed at any point in time.

This enables:

replay systems

debugging

historical analysis

branching timelines



---

Minimal Object Definition

At minimum, a CrypSA object requires:

identity

genome

canonical event history


Canonical state can always be derived from these.


---

Key Insight

CrypSA objects are not stored as “current state.”

They are derived from validated history.


---

Summary

The CrypSA object model defines objects as deterministic reconstructions of identity, genome, and canonical event history.

This allows consistent shared worlds without requiring centralized simulation or constant state synchronization.


---

One Sentence Summary

A CrypSA object is a deterministic reconstruction of identity, genome, and validated event history, rather than a continuously stored mutable state.


---
