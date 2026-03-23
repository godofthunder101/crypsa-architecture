# CrypSA — Object Lifecycle Walkthrough

## Purpose

This document provides a simple example of how an object evolves in CrypSA.

It demonstrates how:

* objects are defined by **minted structure + event history**
* canonical events create and evolve objects
* clients reconstruct objects from canonical truth

This is an illustrative walkthrough, not a specification.

---

## Core Idea

In CrypSA, an object is defined by:

```
Minted Structure + Canonical Event History
```

* The **Mint** defines what the object can validly be
* The **event history** defines what has happened to it

Clients reconstruct the current object from both.

---

## Initial Conditions

Assume:

* Player A and Player B exist
* a valid sword genome exists in the Mint
* a valid crafting rule allows swords to be created

No sword instance exists yet.

---

# Step 1 — Creation

## Conceptual Outcome

A new canonical object is created.

* a unique identity is assigned
* the genome is associated
* initial canonical state is set
* initial event history is recorded

---

## Client

The client:

* shows crafting UI
* optionally performs local checks
* prepares a candidate event

Example:

```
create_sword
actor = Player A
recipe = basic_sword
```

The client proposes the event.
It does not create canonical reality.

---

## Server

The server validates:

* actor validity
* rule permissions
* invariant constraints
* genome validity

If accepted:

* assigns identity (e.g. sword_9AF3)
* associates genome
* sets initial state
* appends canonical events

Example lineage:

* minted
* created
* assigned

---

## Client Reconstruction

Observers reconstruct:

* identity
* genome
* canonical state
* event history

The sword now exists canonically.

---

# Step 2 — Upgrade

## Conceptual Outcome

The object remains the same.

* identity is unchanged
* history expands
* canonical state evolves

---

## Client

The client:

* shows upgrade UI
* previews results
* submits a candidate event

Example:

```
upgrade_sword
target = sword_9AF3
actor = Player A
upgrade_type = sharpen_1
```

---

## Server

The server validates:

* ownership
* upgrade rules
* invariant constraints

If accepted:

* updates canonical state
* appends event

Example:

* upgraded

---

## Client Reconstruction

The same object is reconstructed with updated state.

---

# Step 3 — Transfer

## Conceptual Outcome

The object persists.

* identity remains the same
* ownership changes
* history expands

---

## Client

The client submits:

```
transfer_sword
target = sword_9AF3
from = Player A
to = Player B
```

---

## Server

The server validates:

* existence
* ownership
* transfer rules

If accepted:

* updates owner
* appends event

Example:

* transferred

---

## Client Reconstruction

Observers now reconstruct:

* same identity
* updated ownership
* full event history

---

# Final Event Lineage

```
sword_9AF3

minted
created
assigned to Player A
upgraded
transferred to Player B
```

---

# Final Reconstructed Object

```
identity = sword_9AF3
genome = sword
owner = Player B
upgrade_level = 1
history = full event lineage
```

---

# What This Demonstrates

## 1. Mint Defines Structure

The Mint defines what the object can be.

---

## 2. Event History Defines Life

Events define what has happened to this object.

---

## 3. Identity Persists

The object remains the same across all changes.

---

## 4. Client Reconstruction

Clients rebuild the object from structure + history.

---

## 5. Server Protects Truth

The server:

* validates events
* enforces invariants
* records canonical history

---

# Key Principle

> The Mint defines what an object can be.
> Event history defines what it has become.
> Clients reconstruct the result.

---

## One Sentence Summary

A CrypSA object is a persistent identity defined by a valid minted structure and an evolving canonical event history, reconstructed locally by observers.
