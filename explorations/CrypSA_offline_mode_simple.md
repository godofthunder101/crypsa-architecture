---

CrypSA Offline Mode – Simple

Purpose

This document describes a simple offline mode model for CrypSA systems.

CrypSA allows clients to simulate the universe locally even when disconnected from the canonical server. This enables responsive gameplay and experimentation without requiring constant network connectivity.

In the Simple Offline Mode, offline activity occurs in a temporary local branch that exists only on the client and is not merged into canonical history.

When the client reconnects, it simply resumes interaction with the canonical universe maintained by the server.


---

Core Principle

CrypSA separates local simulation from canonical truth.

Clients are free to simulate the universe locally while offline, but:

Canonical truth only exists on the server.

Offline play therefore occurs in a local branch of the universe that is not merged into the shared canonical timeline.


---

Canonical Mint Authority

The canonical mint exists on the server.

It is responsible for:

issuing canonical object identities

defining valid object genomes

validating canonical object creation

enforcing uniqueness constraints

maintaining the official object registry


Only the server can admit objects into canonical reality.


---

Local Mint Mirror

Clients maintain a local mint mirror.

The mint mirror contains structural knowledge about the universe, allowing the client to:

reconstruct objects

understand genome definitions

simulate object creation

simulate upgrades or transformations

interpret canonical event history


The local mint mirror enables clients to simulate the universe consistently even when offline.

However, the local mint mirror does not have canonical authority.


---

Offline Simulation

When disconnected from the server, the client may simulate the universe locally.

Offline simulation may include:

movement

building structures

destroying structures

crafting objects

upgrading items

interacting with the environment


These events occur only within the local branch of the universe.

They are not considered canonical.


---

Local Branch Universes

Offline play creates a local branch of the universe.

This branch:

exists only on the client

uses the local mint mirror

simulates events normally

maintains its own local event history


However, this branch is not intended to merge into canonical history.

It is effectively a single-player universe derived from canonical state.


---

Reconnecting to the Server

When the client reconnects:

1. The client contacts the canonical server


2. The server provides the latest canonical history


3. The client reconstructs the canonical universe


4. The offline branch is discarded or archived



The player then resumes gameplay within the canonical universe.


---

Canonical Entry Points

A canonical entry point is the moment when a local action must cross the boundary from simulation into canonical validation.

Examples include:

minting an object

transferring ownership

placing a persistent structure

destroying a persistent structure

modifying canonical world state


Before the entry point, actions may exist only in local simulation.

After the entry point, the action must pass through:

server validation

invariant enforcement

canonical event recording


This boundary separates local simulation freedom from canonical authority.


---

Why Offline Branches Are Not Merged

Merging offline branches into canonical history introduces significant complexity.

Challenges include:

world state conflicts

structure placement conflicts

ownership conflicts

resource duplication

invariant violations


The simple offline model avoids these problems entirely by treating offline play as a separate local branch.


---

Benefits of the Simple Offline Model

This approach provides several advantages.

Simplicity

No complex merge logic is required.

Deterministic Canonical History

Canonical events always originate from validated server actions.

Reliable Offline Play

Players can continue exploring and experimenting without connection.

Clear Authority Model

The server remains the sole authority for canonical truth.


---

Optional Offline Features

Offline branches may optionally allow players to:

experiment with building systems

test strategies

explore environments

practice gameplay mechanics

prototype structures


Because these branches are not canonical, they can be freely simulated.


---

Optional Offline Archiving

Clients may optionally store offline branches locally.

This allows players to:

revisit offline experiments

maintain personal worlds

explore alternate timelines


These branches remain separate from the canonical universe.


---

Offline Mode Variations

The simple offline model described in this document is intentionally minimal.

CrypSA does not require a single offline strategy. Different games may choose different approaches depending on their design goals.

Possible alternatives include:

Mergeable Offline Branches

Offline activity may later merge into canonical history.

This requires additional systems such as:

branch reconciliation

conflict resolution

invariant conflict detection

duplication prevention


This approach is significantly more complex.


---

Local Worlds or Personal Universes

Offline play may occur in completely separate worlds.

Examples include:

personal sandbox worlds

creative mode environments

private server instances

modded environments


These worlds remain independent of the canonical universe.


---

Offline Event Buffers

Clients may store candidate events while offline and submit them when reconnecting.

The server then:

validates each event

accepts or rejects them

integrates valid events into canonical history


This approach requires careful validation logic.


---

Summary

CrypSA clients may simulate the universe offline using a local mint mirror.

In the Simple Offline Mode, offline activity occurs in a temporary local branch that exists only on the client and is not merged into canonical history.

When reconnecting, the client simply reconstructs the canonical universe and resumes interaction with the shared timeline.

This approach preserves simplicity while still enabling responsive offline gameplay.


---

One Sentence Summary

CrypSA Simple Offline Mode allows clients to simulate the universe locally using a mint mirror, while canonical truth remains exclusively controlled by the server and offline activity remains isolated from the shared canonical history.


---


