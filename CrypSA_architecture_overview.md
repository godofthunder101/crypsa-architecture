# CrypSA Architecture Overview

This document provides a high-level map of the CrypSA system.

It shows how the major components relate to each other without going into full detail.

For detailed explanations, see the architecture and spec documents.

---

## Purpose

This document answers:

> What are the main parts of CrypSA, and how do they fit together?

It is not intended to teach the full system.

It is intended to:

- orient readers  
- provide a system map  
- show relationships between components  

---

## High-Level View

CrypSA is built around four core layers:

1. Observers (clients)  
2. Canonical server  
3. Adapter layer (translation)  
4. Lens layer (interpretation)  

---

## System Overview Diagram

```mermaid
flowchart LR

subgraph Observer
A[Local Simulation]
B[Predicted Actions]
C[Observer State]
end

subgraph Server
D[Validation Pipeline]
E[Canonical Event Log]
F[Derived State]
end

subgraph Adapter Layer
G[Adapters]
end

subgraph Lens Layer
H[Lenses]
end

subgraph Presentation
I[UI / Player Experience]
end

A --> B
B --> D

D -->|Accepted| E
D -->|Rejected| C

E --> F
F --> G
C --> G

G --> H
H --> I
````

---

## Core Components

---

### Observer (Client)

Observers are responsible for:

* reconstructing canonical state
* simulating the world locally
* proposing candidate events
* shaping data through adapters
* interpreting data through lenses
* presenting the world

Observers provide responsiveness and local experience.

---

### Canonical Server

The canonical server is responsible for:

* validating candidate events
* enforcing invariants
* recording canonical events
* defining shared truth

The server does not need to simulate the full world.

---

### Canonical Event Log

The canonical event log is the source of truth.

* all accepted events are recorded
* history defines reality
* state is derived from events

---

### Derived Canonical State

Derived state is a materialized view of canonical history.

It exists to:

* improve performance
* simplify queries

It must always be:

> reproducible from canonical events

---

### Adapter Layer

Adapters are responsible for:

* translating runtime and canonical data
* shaping data for consumption
* isolating system boundaries

They sit between:

* runtime state
* lenses and UI

Adapters do not define truth or interpretation.

---

### Lens Layer

Lenses are responsible for:

* interpreting canonical reality
* applying visibility and gameplay meaning
* producing observer-specific views

Lenses transform structured data into player-facing experience.

---

### Presentation Layer

The presentation layer includes:

* UI
* visuals
* interaction

It consumes lens outputs and presents them to the player.

---

## Key Flow

At a high level:

1. observers simulate locally
2. actions become candidate events
3. the server validates events
4. accepted events enter canonical history
5. canonical state is derived
6. adapters shape data
7. lenses interpret that data
8. the UI presents the result
9. observers reconcile with canonical truth

---

## Key Idea

CrypSA separates:

* truth (canonical events)
* structure (adapters)
* interpretation (lenses)
* experience (UI and simulation)

This separation allows the system to be:

* flexible
* debuggable
* persistent
* replayable

---

## Relationship to Other Documents

* `architecture/` → explains each component
* `spec/` → defines runtime behavior
* `CrypSA_WORKED_EXAMPLE.md` → shows a full flow
* `diagrams/` → visual explanations

---

## One Sentence Summary

CrypSA is structured as observers and a canonical server, with adapters shaping data and lenses interpreting it, allowing shared reality to emerge from validated event history.
