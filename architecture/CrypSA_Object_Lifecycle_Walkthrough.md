---

CRYPSA — OBJECT LIFECYCLE WALKTHROUGH

An abstract example showing what happens on the client and server


---

Purpose

This document provides a simple walkthrough of how a CrypSA object evolves over time.

The goal is to show, step by step, how an object begins as a valid canonical structure from the Mint, then gains history through canonical events, and is reconstructed on clients as that history changes.

This example uses a very simple object lifecycle:

1. A player creates a sword


2. The sword is upgraded


3. The sword is traded to another player



At each step, this document explains:

what is happening on the client

what is happening on the server


The example is intentionally abstract so the architecture remains easy to follow.


---

Core Idea

In CrypSA, an object is not defined only by its current state.

It is defined by:

Minted Structure
+ Canonical Event History

The Mint defines what the object can validly be.

Event history defines what has actually happened to that specific object.

Clients reconstruct the current object from both.


---

Initial Conditions

Before the example begins, assume the universe already contains:

a valid player identity for Player A

a valid player identity for Player B

a valid sword genome in the Mint

a valid crafting rule that allows swords to be created


The sword does not yet exist as a canonical object instance.


---

Step 1 — Player A Creates a Sword

Conceptual Outcome

A new canonical sword instance comes into existence.

The sword receives:

a unique identity

a sword genome

an initial canonical state

its first event history entries



---

What Happens on the Client

Player A performs a crafting action.

The client may do several local things first:

display the crafting interface

check whether the action appears possible

show immediate local feedback

prepare a proposed canonical event


The client does not decide that the sword canonically exists.

Instead, it creates a candidate event such as:

create_sword
actor = Player A
recipe = basic_sword

The client sends this event for reconciliation.


---

What Happens on the Server

The server receives the candidate creation event.

It validates:

that Player A exists

that the crafting action is allowed

that required invariants are satisfied

that the sword genome is valid

that the creation event is permitted by canonical rules


If valid, the server performs canonical creation.

This includes:

1. Minting the object

A new unique sword identity is created.

Example:

sword_9AF3

2. Associating the genome

The sword is linked to the correct sword genome.

3. Setting initial canonical state

For example:

owner = Player A
upgrade_level = 0
status = owned

4. Appending event history

The server records events such as:

E1: sword_9AF3 minted
E2: sword_9AF3 created by Player A
E3: sword_9AF3 assigned to Player A

The sword now canonically exists.


---

What Clients Reconstruct After Reconciliation

Observers reconstruct the sword using:

identity = sword_9AF3
genome = sword
canonical state = owned by Player A, upgrade level 0
event history = minted, created, assigned

Player A now sees the sword as a real canonical object.

Other observers may also reconstruct it if relevant.


---

Step 2 — Player A Upgrades the Sword

Conceptual Outcome

The sword remains the same object.

Its identity does not change.

Its history expands, and its canonical state changes.

This is important:

> The sword is still the same sword.
It is not replaced by a different object unless the system explicitly models it that way.




---

What Happens on the Client

Player A chooses to upgrade the sword.

The client may:

show upgrade UI

preview local stat changes

display animation or feedback

prepare a candidate canonical event


The client generates something like:

upgrade_sword
target = sword_9AF3
actor = Player A
upgrade_type = sharpen_1

This event is submitted for reconciliation.


---

What Happens on the Server

The server receives the upgrade event.

It validates:

that sword_9AF3 exists

that Player A is allowed to upgrade it

that the sword genome allows this upgrade path

that upgrade invariants are not violated

that resources or prerequisites are satisfied


If valid, the server updates canonical state.

For example:

upgrade_level = 1
damage_profile = sharpened

It then appends new event history:

E4: sword_9AF3 upgraded by Player A

The sword’s identity remains unchanged.

Its current canonical form has evolved through history.


---

What Clients Reconstruct After Reconciliation

Clients reconstruct the same object again:

identity = sword_9AF3
genome = sword
canonical state = owned by Player A, upgrade level 1
event history = minted, created, assigned, upgraded

The client now shows an upgraded sword.

The important CrypSA concept here is:

> The Mint still defines what the object is.
Event history now defines what has happened to this specific sword.




---

Step 3 — Player A Trades the Sword to Player B

Conceptual Outcome

The sword remains the same object again.

Its ownership changes.

Its history expands further.

This step shows that identity persists across ownership changes.


---

What Happens on the Client

Player A initiates a trade.

The client may:

open a trade interface

show the sword being offered

display a pending transfer state

create a candidate canonical event


The candidate event may look like:

transfer_sword
target = sword_9AF3
from = Player A
to = Player B

This event is submitted to the server.

Player B’s client may also locally show the pending trade.


---

What Happens on the Server

The server receives the transfer event.

It validates:

that sword_9AF3 exists

that Player A currently owns it

that the sword is transferable

that Player B is a valid recipient

that no ownership invariant is violated

that the item is not in a restricted state


If valid, the server updates canonical state:

owner = Player B
status = owned

It appends a new canonical event:

E5: sword_9AF3 transferred from Player A to Player B

The sword remains the same object with the same identity.

Its lineage now includes a transfer event.


---

What Clients Reconstruct After Reconciliation

Clients now reconstruct:

identity = sword_9AF3
genome = sword
canonical state = owned by Player B, upgrade level 1
event history = minted, created, assigned, upgraded, transferred

Player A no longer sees it as owned.

Player B now sees the same sword as their owned object.


---

What This Example Demonstrates

This walkthrough demonstrates several core CrypSA ideas.


---

1. The Mint Defines Valid Structure

The Mint ensures that the sword is a valid canonical object type.

It defines things such as:

sword identity rules

sword genome

allowed state transitions

invariant constraints


The Mint does not define the sword’s full lived history.


---

2. Event History Defines the Object’s Actual Life

The object’s history tells us:

who created it

whether it was upgraded

who currently owns it


Without event history, the system would know only what a sword could be, not what this sword has become.


---

3. The Client Reconstructs From Structure and History

The client reconstructs the sword using both:

Minted structure

Canonical history / canonical state


This is why the object can evolve over time without losing identity.


---

4. The Server Protects Canonical Truth

The server does not invent arbitrary object reality.

Its job is to:

validate events

enforce invariants

update canonical state

append event history


The server protects shared truth.


---

Simplified Event Lineage for the Example

The final sword history might look like this:

sword_9AF3

E1: minted
E2: created by Player A
E3: assigned to Player A
E4: upgraded by Player A
E5: transferred to Player B

This event lineage is enough to explain the object’s current reality.


---

Final Reconstructed Object

After all three steps, the reconstructed sword is:

identity = sword_9AF3
genome = sword
owner = Player B
upgrade_level = 1
history = minted, created, upgraded, transferred

This is the same object that began in Step 1.

It has simply evolved through canonical events.


---

Key Principle

The cleanest way to summarize this document is:

> The Mint defines what the object is allowed to be.
Canonical event history defines what has actually happened to it.
The client reconstructs the current object from both.




---

One Sentence Summary

In CrypSA, an object begins as a valid minted structure, then evolves through canonical event history, while clients reconstruct its current form from both its base genome and its accumulated canonical history.


---
