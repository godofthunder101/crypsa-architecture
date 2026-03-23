---

CrypSA Universe Model

> Exploratory note: This document represents early conceptual framing.
>
> For the current CrypSA model, refer to `../../CrypSA_Why_It_Exists.md`, `../../CrypSA_Where_It_Fits.md`, `../../architecture/`, and `../../spec/`.

Purpose

The CrypSA Universe Model illustrates how a CrypSA world is structured.

Instead of representing a universe as a continuously simulated state, CrypSA represents a universe as a history of canonical events that observers use to reconstruct the world.

Objects, player actions, and world changes all emerge from this shared event history.


---

CrypSA Universe Model Diagram

CRYPSA UNIVERSE MODEL


                ┌───────────────────────┐
                │        Observers       │
                │                       │
                │  Player A             │
                │  Player B             │
                │  Player C             │
                └───────────┬───────────┘
                            │
                            │ Local Simulation
                            ▼

           ┌─────────────────────────────────┐
           │     Observer Simulation Layer    │
           │                                  │
           │  • movement                      │
           │  • rendering                     │
           │  • interaction                   │
           │  • prediction                    │
           │                                  │
           └───────────────┬──────────────────┘
                           │
                           │ Proposed Events
                           ▼

              ┌────────────────────────────┐
              │       Invariant Boundary    │
              │           (Server)          │
              │                              │
              │  • validate rules            │
              │  • enforce invariants        │
              │  • maintain canonical log    │
              └───────────────┬─────────────┘
                              │
                              │ Canonical Events
                              ▼

              ┌────────────────────────────┐
              │     Canonical Event Log     │
              │                              │
              │  E1: Object Minted           │
              │  E2: Object Placed           │
              │  E3: Resource Mined          │
              │  E4: Structure Built         │
              │  E5: Object Transferred      │
              │                              │
              └───────────────┬─────────────┘
                              │
                              │ Timeline History
                              ▼

             ┌────────────────────────────────┐
             │        Timeline Structure       │
             │                                 │
             │ Genesis                         │
             │   │                             │
             │   ├─ Event A                    │
             │   │    │                        │
             │   │    └─ Event B               │
             │   │         │                   │
             │   │         └─ Event C          │
             │   │                             │
             │   └─ Alternate Branch           │
             │        │                        │
             │        └─ Event B'              │
             │              │                  │
             │              └─ Event C'        │
             └───────────────┬────────────────┘
                             │
                             ▼

                ┌────────────────────────┐
                │   Object Reconstruction │
                │                        │
                │ Objects defined by    │
                │ their event history   │
                │                        │
                │ Example:              │
                │ Sword #9AF3           │
                │  Minted → Modified    │
                │  Transferred → Used   │
                └────────────────────────┘


---

What This Diagram Shows

This model highlights several core CrypSA ideas.

Observers

Players or clients act as observers of the universe.

They simulate the world locally and interact with it.


---

Observer Simulation

Observers run their own simulation:

movement

rendering

prediction

local interactions


This allows responsive gameplay without requiring the server to simulate everything.


---

Invariant Boundary

The server acts as the invariant boundary.

Its job is to:

validate events

enforce world rules

record canonical history


The server protects the integrity of the universe.


---

Canonical Event Log

All accepted events are recorded in a canonical event log.

This log defines the shared history of the universe.

Examples include:

object minting

structure construction

resource gathering

ownership transfer



---

Timeline Structure

The universe is represented as a timeline of events.

In some cases, alternate branches may exist for:

debugging

experimentation

simulation forks


This makes CrypSA worlds conceptually similar to versioned histories.


---

Object Reconstruction

Objects in CrypSA are defined by their event lineage rather than just their current state.

This allows:

historical tracking

provenance

reconstructable objects



---

Key Idea

A CrypSA universe is not defined by a single world state.

It is defined by:

the canonical history of events that created the world.

Observers reconstruct the universe by interpreting that history.


---

Summary

CrypSA transforms how persistent worlds are represented.

Instead of:

Server → World State

CrypSA uses:

Canonical Event History → Reconstructed Universe

This enables:

distributed simulation

historical world reconstruction

event-driven persistence

preservation-friendly world design



---
