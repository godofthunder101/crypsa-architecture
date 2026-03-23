---

CrypSA Event Lifecycle

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to `../../CrypSA_In_5_Minutes.md`, `../../architecture/`, and `../../spec/`.

Purpose

This document describes the lifecycle of a canonical event in a CrypSA system.

CrypSA universes evolve through validated events rather than continuous centralized simulation.
Clients propose candidate events, servers validate them against invariants, and accepted events become part of canonical history.

This lifecycle is the core runtime loop of the architecture.


---

Core Principle

In CrypSA, player actions do not directly change canonical truth.

Instead, actions follow this path:

Player Action
→ Client Simulation
→ Candidate Event Proposal
→ Server Validation
→ Canonical Event Recording
→ Canonical Update Broadcast
→ Client Reconciliation

Only accepted events become part of shared reality.


---

Event Lifecycle Stages

1. Player Action

A player performs an action inside the client.

Examples:

move a pawn

build a structure

destroy a structure

craft an item

upgrade an item

transfer ownership


At this point, the action exists only as local intent.


---

2. Client Simulation

The client simulates the action locally.

This may include:

visual feedback

local movement

temporary placement preview

speculative state changes

pending inventory updates


This local simulation keeps the experience responsive.

The action is not yet canonical.


---

3. Invariant Boundary Check

The client or local simulation layer determines whether the action affects canonical truth.

Examples:

Local-only actions

camera movement

temporary effects

avatar color changes

UI interactions


These do not need canonical validation.

Canonical candidate actions

placing a structure

destroying a structure

creating an item

upgrading an item

transferring an object


These must be proposed to the server.


---

4. Candidate Event Proposal

If the action affects canonical truth, the client creates a candidate event.

A minimal event may include:

event_type
actor_identity
target_identity
payload
timestamp

Depending on the system, it may also include:

context trail reference

branch reference

local snapshot reference

provisional state marker


The candidate event is then sent to the server.


---

5. Server Validation

The server receives the candidate event and validates it.

Validation may include:

identity existence

genome rule compliance

ownership verification

invariant preservation

contextual validity

branch consistency

timing/order constraints


At this stage, the event is still only a proposal.


---

6. Validation Outcome

The server reaches one of two outcomes.

Event Accepted

The event is valid and may become canonical.

Event Rejected

The event violates a rule, invariant, or validation condition.

The server does not allow it to alter canonical truth.


---

7A. Accepted Event → Canonical Recording

If accepted, the server records the event in the canonical event history.

This may include:

appending to the event log

updating canonical state

updating lineage/provenance

advancing the active timeline branch


The universe has now changed.


---

7B. Rejected Event → No Canonical Change

If rejected, the server does not update canonical truth.

The client must eventually reconcile its local simulation back to the accepted shared reality.

Examples:

remove invalid placed structure

revert invalid ownership transfer

cancel invalid upgrade

restore previous local state



---

8. Canonical Update Broadcast

Once a canonical event is recorded, the server distributes the update to relevant observers.

This may happen through:

event stream updates

reconciliation messages

branch timeline updates

snapshot notifications


Observers are informed that shared truth has advanced.


---

9. Client Reconciliation

Clients receive the canonical update and reconcile their local simulations.

This may involve:

confirming the local prediction

correcting local divergence

rebuilding affected objects

updating UI/logs

creating a new local snapshot


The client returns to alignment with canonical truth.


---

10. Ongoing World Reconstruction

After reconciliation, the client continues simulating the world using updated canonical history.

The lifecycle then repeats for the next action.


---

Event Lifecycle Diagram

Player Action
      ↓
Client Simulation
      ↓
Invariant Boundary Check
      ├── Local Only → remain local
      └── Canonical Candidate
                ↓
        Candidate Event Proposal
                ↓
          Server Validation
           ├── Reject
           │     ↓
           │ Client Reconciliation
           │
           └── Accept
                 ↓
        Canonical Event Recording
                 ↓
       Canonical Update Broadcast
                 ↓
         Client Reconciliation
                 ↓
        Updated World Simulation


---

Example: Build Attempt

A simple example helps illustrate the lifecycle.

Local Step

A player places a structure on a tile.

The client shows the structure locally.

Candidate Event

The client sends:

build_structure
actor = Player A
target = tile_42
payload = mining_station

Server Validation

The server checks:

tile_42 exists

tile_42 is buildable

no invariant is violated


Accepted Case

If valid:

event recorded

tile ownership/state updated

clients confirm the structure


Rejected Case

If invalid:

no canonical change

local structure disappears during reconciliation



---

Why This Lifecycle Matters

This model is important because it explains how CrypSA can provide:

responsive local interaction

invariant-protected canonical truth

deterministic event history

branchable timelines

reconstructable universes


It is the operational core of the architecture.


---

Minimal Required Components

A minimal CrypSA event lifecycle needs:

a client that can simulate locally

an invariant boundary

a server that validates candidate events

a canonical event history

a reconciliation mechanism


That is enough to create a functioning event-driven universe.


---

Key Distinction

Traditional multiplayer often works like this:

Player Action
→ Server Simulation
→ State Update
→ Client Receives State

CrypSA works like this:

Player Action
→ Local Simulation
→ Event Proposal
→ Validation
→ Canonical History Update
→ Reconciliation

This is a fundamental architectural shift.


---

Summary

The CrypSA event lifecycle turns player actions into candidate events, validates them against canonical rules, records accepted changes in shared history, and reconciles local simulations with canonical truth.

This cycle is how CrypSA universes evolve.


---

One Sentence Summary

In CrypSA, shared reality evolves through a lifecycle in which local player actions become candidate events, servers validate them against invariants, and accepted events are recorded into canonical history before clients reconcile to the updated universe.


---
