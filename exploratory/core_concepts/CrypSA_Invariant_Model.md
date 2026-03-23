---

CrypSA Invariant Model

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to `../../CrypSA_In_5_Minutes.md`, `../../architecture/`, and `../../spec/`.

Purpose

This document describes the role of invariants in a CrypSA system.

Invariants define the rules that must always remain true within the canonical universe. The CrypSA server enforces these invariants when validating proposed events.

The invariant system ensures that the shared universe remains structurally consistent regardless of how many clients interact with it.


---

Core Principle

An invariant is a rule that must always remain true in canonical history.

Examples:

an object cannot exist in two locations simultaneously

an item cannot be owned by two players at the same time

a structure cannot occupy an invalid location

an upgrade cannot be applied to a non-existent item


If a proposed event would violate an invariant, the server rejects the event.

Invariants therefore form the foundation of canonical validation.


---

Why Invariants Exist

Invariants protect the structural integrity of the universe.

Without invariants, the system could produce contradictions such as:

duplicated unique items

impossible object states

invalid world geometry

inconsistent ownership chains


By enforcing invariants, CrypSA ensures that the canonical universe remains logically consistent.


---

Where Invariants Are Enforced

In CrypSA, invariants are enforced at the server validation stage.

This occurs during the event lifecycle:

Player Action
→ Client Simulation
→ Candidate Event Proposal
→ Server Validation (Invariant Enforcement)
→ Canonical Event Recording
→ Client Reconciliation

The invariant boundary separates local simulation freedom from canonical authority.


---

Categories of Invariants

Different types of invariants protect different aspects of the universe.

Identity Invariants

These ensure that objects maintain consistent identities.

Examples:

an object identity must be unique

objects cannot spontaneously duplicate

destroyed objects cannot reappear without a valid event



---

Ownership Invariants

These ensure that ownership transitions remain valid.

Examples:

an item must have exactly one owner

an actor cannot transfer an item they do not own

ownership transfers must follow valid transitions



---

Spatial Invariants

These protect the physical structure of the world.

Examples:

structures cannot overlap illegally

structures cannot be placed on restricted tiles

objects cannot exist in impossible coordinates



---

State Transition Invariants

These protect valid object evolution.

Examples:

an upgrade cannot occur before an item exists

a structure cannot be destroyed before it is built

a resource cannot be consumed before it is obtained



---

Resource Invariants

These ensure resource accounting remains valid.

Examples:

resources cannot be spent if they do not exist

crafting must consume the correct materials

resource balances cannot become negative



---

Relationship to the Mint

The mint defines the structural rules of objects.

Invariants enforce those rules during runtime.

For example:

The mint may define:

Sword
  → valid upgrades
  → durability range
  → ownership model

The invariant system ensures that events affecting swords follow those rules.


---

Client vs Server Responsibility

Clients may perform local checks for user experience purposes.

Examples:

preventing obviously invalid actions

showing placement restrictions

validating UI inputs


However, these checks are not authoritative.

Only the server performs canonical invariant enforcement.


---

Invariant Violations

When an invariant violation is detected:

1. the server rejects the event


2. canonical history remains unchanged


3. the client reconciles its local simulation



Example:

A client attempts to place a structure on a restricted tile.

Client Simulation → Structure appears locally
Server Validation → Invariant violated
Server Response → Event rejected
Client Reconciliation → Structure disappears

The canonical universe never enters an invalid state.


---

Deterministic Universe Evolution

Because all canonical events pass invariant validation, the universe evolves in a deterministic and consistent manner.

Observers can reconstruct the universe from canonical history with confidence that:

all events are valid

no structural contradictions exist

the universe remains logically consistent



---

Minimal Invariant System

At minimum, a CrypSA system must enforce invariants that protect:

identity uniqueness

object existence

valid state transitions

ownership consistency

spatial constraints


Additional invariants may be defined depending on the game.


---

Flexibility for Developers

CrypSA defines how invariants are enforced, but not which invariants must exist.

Game developers are free to define invariants appropriate to their universe.

For example:

A strategy game may emphasize spatial invariants.

An RPG may emphasize ownership and item evolution.

A sandbox game may emphasize construction constraints.


---

Summary

Invariants are the rules that must always remain true within the canonical universe.

The CrypSA server enforces these invariants during event validation to ensure that the shared universe remains logically consistent.

Clients may simulate freely, but canonical reality only changes when events pass invariant enforcement.


---

One Sentence Summary

CrypSA invariants define the structural rules of the universe and are enforced by the server to ensure that all canonical events preserve logical consistency.


---
