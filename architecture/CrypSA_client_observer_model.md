# CrypSA Client / Observer Responsibility Model

## Purpose

This document defines the role of the client (observer) in a CrypSA system.

In CrypSA architecture, observers are responsible for reconstructing canonical reality, simulating the world locally, shaping runtime data through adapters, interpreting that data through lenses, and presenting the result to the player.

The server protects canonical truth.

This separation allows the universe to exist as shared canonical history rather than as a centralized simulation.

---

## Core Principle

In CrypSA, the client is not merely a passive renderer.

Instead, the client acts as an observer-simulator of the universe.

Observers:

- reconstruct canonical state locally  
- simulate world behavior locally  
- shape runtime data through adapters  
- interpret canonical reality through lenses  
- propose candidate events to the server  
- reconcile their simulation with canonical truth  

---

## Observer-Side Flow

A CrypSA observer typically operates in this order:

1. reconstruct canonical state  
2. run local simulation  
3. use adapters to shape runtime data  
4. use lenses to interpret that data  
5. present the world to the player  

This is the observer-side counterpart to canonical validation on the server.

---

## Observer Responsibilities

The CrypSA client performs several key roles.

---

### 1. Canonical State Reconstruction

Observers reconstruct the world from canonical history.

Examples include reconstructing:

- object creation and existence  
- ownership  
- structure placement  
- inventory contents  
- upgrade levels  

This gives the observer a local view of canonical reality.

---

### 2. Local Simulation

Observers simulate the world locally using canonical state as a foundation.

Examples of simulation include:

- player movement  
- physics interactions  
- combat mechanics  
- resource harvesting  
- AI behavior  
- environmental interactions  

This allows gameplay to remain responsive without requiring constant server computation.

---

### 3. Adapter-Based Data Shaping

Observers use adapters to shape runtime and canonical data into forms that can be safely consumed by lenses, UI, and tools.

Examples include:

- building a world grid view from canonical occupancy  
- preparing timeline rows from canonical event history  
- combining observer context with canonical state into interaction-ready structures  
- shaping teaching/debug overlays  

Adapters help prevent:

- lenses from digging into raw runtime structures directly  
- UI modules from depending on internal runtime details  
- interpretation layers from becoming tightly coupled to each other  

Adapters do not define truth or interpretation.

They prepare data for use across boundaries.

---

### 4. Lens-Based Interpretation

Observers interpret canonical reality through lenses.

A lens transforms shaped runtime data into observer-specific meaning.

Examples include:

- visibility filtering  
- interactable object determination  
- player-specific overlays  
- presentation-oriented world interpretation  
- debug/inspection views  

Lenses allow different observers or tools to interpret the same canonical reality differently without changing canonical truth.

---

### 5. Event Proposal

When a player performs an action, the client generates a candidate event.

Examples:

- craft item  
- upgrade weapon  
- trade object  
- place structure  
- destroy structure  

The client proposes this event to the server for validation.

The event is not considered canonical until the server accepts it.

---

### 6. Reconciliation

The client must reconcile its local simulation with canonical truth.

Reconciliation occurs when:

- the server accepts an event  
- the server rejects an event  
- another player creates a canonical event  
- history branches or corrections occur  

The client updates its local simulation to remain consistent with canonical history.

Adapters and lenses may then re-run on the updated canonical state.

---

### 7. Prediction and Responsiveness

Clients may predict outcomes to keep gameplay responsive.

For example:

- predicting movement  
- predicting ability usage  
- predicting combat interactions  

If predictions differ from canonical results, reconciliation corrects the simulation.

---

## Client State vs Canonical Truth

The client maintains a local world interpretation, but this interpretation is not authoritative.

The authoritative state of the universe is determined by:

- canonical event history  
- invariant enforcement by the server  

Observers adjust their simulations whenever canonical truth changes.

---

## Client Data Layers

Observers may maintain several types of local data.

---

### 1. Canonical Object State

Derived from canonical history.

Examples:

- item ownership  
- item upgrade levels  
- structure states  
- inventory contents  

---

### 2. Local Simulation State

Examples:

- player positions  
- physics states  
- AI states  
- combat states  

---

### 3. Adapter-Shaped Data

Examples:

- world grid models  
- history/timeline rows  
- action-ready view models  
- teaching/debug summaries  

These are structured forms of runtime and canonical data prepared for other layers.

---

### 4. Lens-Interpreted State

Examples:

- visible objects  
- interactable objects  
- player-specific contextual data  
- presentation-oriented world views  

---

### 5. Presentation Data

Examples:

- animations  
- visual effects  
- UI overlays  
- audio cues  

---

## Client Autonomy

Observers can operate with significant autonomy.

Because observers simulate locally, they can:

- continue rendering the world during latency  
- predict outcomes  
- maintain fluid gameplay  

Canonical reconciliation ensures that all observers eventually converge on the same truth.

---

## Client Limitations

Despite their autonomy, observers cannot alter canonical truth directly.

The client cannot:

- create canonical objects without server validation  
- modify ownership arbitrarily  
- violate universe invariants  
- bypass canonical validation rules  

All canonical changes must pass through the server.

---

## Observer Synchronization

Observers maintain synchronization through canonical updates.

Synchronization mechanisms may include:

- event broadcast  
- event streams  
- periodic reconciliation  
- snapshot updates  

Observers update their local simulations whenever new canonical events appear.

After canonical updates arrive:

- canonical state may be rebuilt  
- adapters may reshape new data  
- lenses may reinterpret the result  
- presentation may update accordingly  

---

## Failure Scenarios

If a client disconnects:

- the canonical universe continues to exist  
- the observer simply stops simulating  

When the observer reconnects:

- canonical history can be replayed  
- local world state can be reconstructed  
- adapters and lenses can rebuild the observer’s view  

This allows the universe to remain persistent even if observers come and go.

---

## Minimal Client Responsibilities

At minimum, a CrypSA client must:

1. reconstruct canonical event history into local canonical state  
2. simulate the world locally  
3. shape runtime data through adapters  
4. interpret that data through lenses  
5. propose candidate events  
6. reconcile with canonical truth  
7. present the world to the player  

---

## Server vs Client Responsibilities

| Responsibility | Client | Server |
|---|---|---|
| Canonical state reconstruction | Yes | Yes |
| Local simulation | Yes | Not required |
| Adapter-based data shaping | Yes | Not required |
| Lens-based interpretation | Yes | Not required |
| Event proposal | Yes | No |
| Event validation | No | Yes |
| Invariant enforcement | No | Yes |
| Canonical event recording | No | Yes |
| Local rendering | Yes | No |
| Canonical truth authority | No | Yes |

---

## Summary

In CrypSA architecture, observers reconstruct canonical reality, simulate the universe locally, shape runtime data through adapters, interpret that data through lenses, and present the result to the player.

The server validates candidate events and records the canonical evolution of the universe.

Together, this separation allows the universe to exist as a shared event-driven history rather than a centralized simulation.

---

## Key Idea

A CrypSA client is not merely a game client.

It is an observer that reconstructs, simulates, shapes, interprets, and experiences a canonical universe.
