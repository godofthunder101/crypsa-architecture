# CrypSA — Object Lifecycle Walkthrough

## Purpose

This document provides a simple example of how an object evolves in CrypSA.

It demonstrates how:

* objects are defined by **minted structure + canonical event history**
* canonical events create and evolve objects
* observers reconstruct objects from canonical event history

This is an illustrative walkthrough, not a specification.

---

## Core Idea

In CrypSA, an object is defined by:

```text
Minted Structure + Canonical Event History
```

* The **Mint** defines what the object can validly be
* The **canonical event history** defines what has happened to it

Observers reconstruct the current object from both.

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

* a unique identity is created via a mint event
* the genome is associated
* initial state is established via canonical events
* canonical event history begins

---

## Observer

The observer:

* shows crafting UI
* optionally performs local checks
* prepares a candidate event

Example:

```text
create_sword
actor = Player A
recipe = basic_sword
```

The observer proposes the event.
It does not create canonical reality.

---

## Validator

The validator evaluates:

* actor validity
* rule permissions
* invariant constraints
* genome validity

If accepted:

* a mint event establishes identity (e.g. `sword_9AF3`)
* the validator assigns `server_sequence`
* the canonical event is appended to canonical event history
* derived canonical state is updated via replay

Example canonical event history (illustrative labels):

```text
minted
assigned_to_Player_A
```

> Note: "minted" represents identity creation.
> Additional events (like assignment) are separate canonical events.

---

## Observer Reconstruction

Observers reconstruct the object by:

* applying canonical events in order
* resolving identity and genome
* deriving current state

The sword now exists canonically.

---

# Step 2 — Upgrade

## Conceptual Outcome

The object remains the same.

* identity is unchanged
* canonical event history expands
* derived canonical state evolves

---

## Observer

The observer:

* shows upgrade UI
* previews results
* submits a candidate event

Example:

```text
upgrade_sword
actor = Player A
target = sword_9AF3
payload = { upgrade_type: sharpen_1 }
```

---

## Validator

The validator evaluates:

* ownership
* upgrade rules
* invariant constraints

If accepted:

* assigns `server_sequence`
* appends canonical event
* derived canonical state updates via replay

Example (illustrative):

```text
upgraded
```

---

## Observer Reconstruction

The same object is reconstructed by replaying canonical event history.

---

# Step 3 — Transfer

## Conceptual Outcome

The object persists.

* identity remains the same
* ownership changes
* canonical event history expands

---

## Observer

The observer submits:

```text
transfer_sword
actor = Player A
target = sword_9AF3
payload = { new_owner: Player B }
```

---

## Validator

The validator evaluates:

* object existence
* ownership
* transfer rules

If accepted:

* assigns `server_sequence`
* appends canonical event
* derived canonical state updates via replay

Example (illustrative):

```text
transferred_to_Player_B
```

---

## Observer Reconstruction

Observers reconstruct:

* same identity
* updated ownership
* full canonical event history

---

# Final Canonical Event History

```text
sword_9AF3

minted
assigned_to_Player_A
upgraded
transferred_to_Player_B
```

---

# Final Reconstructed Object

```text
identity = sword_9AF3
genome = sword
owner = Player B
upgrade_level = 1
history = canonical event history for this object
```

---

# What This Demonstrates

## 1. Mint Defines Structure

The Mint defines what the object can be.

---

## 2. Canonical Event History Defines Life

Canonical events define what has happened to the object.

---

## 3. Identity Persists

The object remains the same across all changes.

---

## 4. Observer Reconstruction

Observers rebuild the object by replaying canonical event history.

---

## 5. Validator Responsibility

The validator:

* validates candidate events
* enforces invariants
* maintains canonical event history

---

# Key Principle

> The Mint defines what an object can be.
> Canonical event history defines what it has become.
> Observers reconstruct the result.

---

## One Sentence Summary

A CrypSA object is a persistent identity defined by a valid minted structure and an evolving canonical event history, reconstructed locally by observers.
