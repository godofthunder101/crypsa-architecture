---

Traditional Multiplayer vs CrypSA Architecture

> Exploratory note: This document represents early conceptual framing.
>
> For the current CrypSA model, refer to `../../CrypSA_Why_It_Exists.md`, `../../CrypSA_Where_It_Fits.md`, `../../architecture/`, and `../../spec/`.

Purpose

This diagram compares the traditional multiplayer architecture model with the CrypSA architecture model.

The goal is to illustrate the key difference:

Traditional systems synchronize world state.
CrypSA synchronizes canonical events.

This shift changes how simulation, networking, and persistence are handled in multiplayer worlds.


---

Traditional Multiplayer Architecture

TRADITIONAL MULTIPLAYER MODEL


        ┌───────────────┐      ┌───────────────┐
        │   Client A    │      │   Client B    │
        │               │      │               │
        └───────┬───────┘      └───────┬───────┘
                │                      │
                │ Input Commands      │
                ▼                      ▼

              ┌──────────────────────────┐
              │        Game Server        │
              │                           │
              │ • runs full simulation    │
              │ • calculates physics      │
              │ • tracks world state      │
              │ • resolves combat         │
              │ • manages AI              │
              └─────────────┬────────────┘
                            │
                            │ World State Updates
                            ▼

        ┌───────────────┐      ┌───────────────┐
        │   Client A    │      │   Client B    │
        │ receives      │      │ receives      │
        │ server state  │      │ server state  │
        └───────────────┘      └───────────────┘

Key Characteristics

Traditional multiplayer systems typically:

• centralize simulation on the server
• synchronize full world state to clients
• require powerful servers for large worlds
• depend on continuous server operation

If the server disappears, the world usually disappears with it.


---

CrypSA Architecture Model

CRYPSA ARCHITECTURE MODEL


        ┌───────────────┐      ┌───────────────┐
        │   Observer A  │      │   Observer B  │
        │               │      │               │
        └───────┬───────┘      └───────┬───────┘
                │                      │
                │ Local Simulation    │
                ▼                      ▼

      ┌─────────────────────────────────────────┐
      │         Observer Simulation Layer        │
      │                                          │
      │ • movement                               │
      │ • rendering                              │
      │ • prediction                             │
      │ • temporary local state                  │
      └───────────────┬──────────────────────────┘
                      │
                      │ Proposed Events
                      ▼

            ┌──────────────────────────┐
            │     Invariant Boundary    │
            │         (Server)          │
            │                           │
            │ • validates events        │
            │ • enforces invariants     │
            │ • records canonical log   │
            └─────────────┬────────────┘
                          │
                          │ Canonical Events
                          ▼

            ┌──────────────────────────┐
            │    Canonical Event Log    │
            │                           │
            │ • mint events             │
            │ • object lineage          │
            │ • world state evolution   │
            └─────────────┬────────────┘
                          │
                          │ Event Updates
                          ▼

      ┌─────────────────────────────────────────┐
      │        Observer Reconstruction Layer     │
      │                                          │
      │ Observers reconstruct shared world state │
      │ from canonical event history.            │
      └─────────────────────────────────────────┘


---

Core Difference

Traditional Model

Server Simulates the World

Clients receive updates from the server.

The server is responsible for:

world simulation

physics

combat

AI

game logic


This places heavy load on the server and tightly couples the world to server infrastructure.


---

CrypSA Model

Observers Simulate Locally

The server protects the canonical truth of the universe.

The server's responsibilities are limited to:

validating events

enforcing invariants

recording canonical history


Observers reconstruct the world locally from canonical events.


---

Key Architectural Differences

Traditional Multiplayer	CrypSA

Server runs simulation	Observers simulate locally
State synchronization	Event synchronization
Server computes world	Server protects invariants
World tied to server uptime	World defined by event history
Limited replayability	Full historical reconstruction possible



---

Implications

This architectural shift enables several possibilities:

• distributed simulation
• reconstructable worlds
• event-driven world history
• lower server simulation burden
• preservation-friendly universe design

CrypSA allows persistent universes to evolve through canonical event history, rather than continuous centralized simulation.


---
