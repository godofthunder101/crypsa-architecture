---

CrypSA Event Model

Purpose

The CrypSA Event Lifecycle describes how actions performed by observers become part of the canonical universe.

Instead of continuously synchronizing world state, CrypSA synchronizes validated events. Observers propose events, which pass through an invariant boundary before becoming part of the canonical event history.

This lifecycle ensures that the universe evolves through verifiable events rather than centralized simulation.


---

CrypSA Event Lifecycle Diagram

CRYPSA EVENT LIFECYCLE


        ┌─────────────────────────────┐
        │        Player Action         │
        │                              │
        │  move / build / interact     │
        └──────────────┬──────────────┘
                       │
                       │
                       ▼

        ┌─────────────────────────────┐
        │     Local Simulation         │
        │                              │
        │ Observer updates local state │
        │ immediately for responsiveness│
        └──────────────┬──────────────┘
                       │
                       │ Proposed Event
                       ▼

        ┌─────────────────────────────┐
        │        Event Proposal        │
        │                              │
        │ event sent to invariant      │
        │ boundary for validation      │
        └──────────────┬──────────────┘
                       │
                       │
                       ▼

        ┌─────────────────────────────┐
        │      Invariant Boundary      │
        │          (Server)            │
        │                              │
        │ validate rules               │
        │ enforce invariants           │
        │ detect conflicts             │
        └──────────────┬──────────────┘
                       │
              ┌────────┴─────────┐
              │                  │
              ▼                  ▼

     ┌─────────────────┐   ┌──────────────────┐
     │ Event Accepted  │   │ Event Rejected    │
     │                 │   │                   │
     │ canonical event │   │ client must       │
     │ recorded        │   │ reconcile state   │
     └───────┬─────────┘   └────────┬──────────┘
             │                      │
             │                      │
             ▼                      ▼

   ┌──────────────────────┐   ┌──────────────────────┐
   │ Canonical Event Log  │   │ Reconciliation       │
   │                      │   │                      │
   │ event becomes part   │   │ local simulation     │
   │ of universe history  │   │ corrected if needed  │
   └──────────┬───────────┘   └──────────┬───────────┘
              │                          │
              └──────────────┬───────────┘
                             │
                             ▼

           ┌─────────────────────────────┐
           │ Observer Reconstruction      │
           │                              │
           │ observers update world       │
           │ from canonical event history │
           └─────────────────────────────┘


---

Event Lifecycle Explained

1. Player Action

A player performs an action in the world.

Examples:

moving a pawn

building a structure

mining a resource

interacting with an object



---

2. Local Simulation

The observer immediately updates its local simulation.

This provides responsiveness and smooth gameplay.

The action is temporarily assumed to be valid.


---

3. Event Proposal

The action is converted into an event proposal.

This event is sent to the invariant boundary for validation.


---

4. Invariant Boundary

The server checks whether the proposed event violates any canonical rules.

Examples of invariants:

building on restricted terrain

exceeding resource limits

conflicting object ownership

duplicate unique items



---

5. Event Outcome

Accepted Event

The event becomes part of the canonical event history.

All observers will eventually reconcile to this event.


---

Rejected Event

The observer must reconcile its local simulation with canonical reality.

This may result in:

removing a locally placed structure

reverting an invalid action

adjusting local world state



---

6. Canonical Event Log

Accepted events are recorded in the canonical event log.

This log defines the shared history of the universe.


---

7. Observer Reconstruction

Observers update their simulation using the canonical event history.

The shared universe emerges through reconstruction of the event log.


---

Why This Model Matters

The CrypSA event lifecycle enables:

• distributed simulation
• canonical history tracking
• deterministic world reconstruction
• flexible conflict resolution
• preservation of world evolution

Instead of synchronizing full world states, CrypSA synchronizes the events that define the universe.


---


