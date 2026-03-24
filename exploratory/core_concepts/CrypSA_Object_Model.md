# CrypSA Object Model

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes a conceptual model for how objects are represented in a CrypSA system.

In CrypSA, objects are not defined by continuously updated mutable state.

Instead, objects are reconstructed deterministically from:

* identity
* genome
* canonical event history

Derived state is computed from this information.

---

## Core Principle

A CrypSA object is not defined by its current state alone.

Instead:

> A CrypSA object is a deterministic reconstruction of identity, genome, and validated event history.

Canonical event history is the source of truth.

Derived state is a computed result.

---

## Object Components

Every canonical object can be understood through four conceptual components.

---

### 1. Identity

The identity uniquely defines the object.

Examples:

* player_17
* sword_4821
* structure_slot_42

Properties:

* immutable
* globally unique within canonical scope
* issued or recognized by the mint

Identity ensures all observers refer to the same object.

---

### 2. Genome

The genome defines the structural rules of the object.

It describes:

* what the object is
* how it behaves
* how it can evolve
* what transitions are valid

Examples:

Sword genome:

* max durability
* allowed upgrades
* ownership rules

Structure slot genome:

* buildable or not
* allowed structure types
* spatial constraints

The genome is deterministic and shared across observers.

---

### 3. Canonical Event History

The event history defines how the object evolves over time.

Examples:

```text
mint → upgrade → transfer → upgrade → damage
```

This history is:

* canonical (server-validated)
* ordered
* append-only (conceptually)

This is the authoritative source of truth.

---

### 4. Derived Canonical State

Derived state represents the current observable state of the object.

Examples:

* current owner
* durability
* structure type
* upgrade level

This state:

* is derived from canonical event history
* is not independently authoritative

---

## Object Reconstruction

Observers reconstruct objects using:

```text
identity + genome + canonical event history → derived state
```

This enables:

* consistent object state across observers
* deterministic replay
* temporal inspection
* reduced need for full state synchronization

---

## Example: Sword Lifecycle

### Step 1 — Mint

identity: sword_1001
genome: sword_type_A

---

### Step 2 — Upgrade

Event:

```text
upgrade → +sharpness
```

---

### Step 3 — Ownership Transfer

Event:

```text
transfer → player_B
```

---

### Step 4 — Reconstruction

Any observer reconstructs:

* identity → sword_1001
* genome → sword_type_A
* history → [mint, upgrade, transfer]
* derived state → computed from history

All observers reach the same result.

---

## Relationship to the Mint

The mint defines:

* valid identities
* valid genomes

The object model uses those definitions to reconstruct objects.

The mint answers:

> What is allowed to exist?

The object model answers:

> What does this object represent over time?

---

## Relationship to Invariants

Invariants ensure that transitions remain valid.

Examples:

* cannot upgrade a non-existent object
* cannot transfer ownership without owning the object
* cannot place a structure in an invalid location

The object model relies on invariants to ensure event history remains valid.

---

## Relationship to Event Lifecycle

Objects evolve through events:

```text
Event → validated → appended → affects derived state
```

The object model is the result of this process.

---

## Client vs Server Perspective

**Client (Observer)**

* reconstructs objects
* simulates interactions
* predicts outcomes

**Server (Truth Layer)**

* validates events
* enforces invariants
* appends canonical event history

The object model is shared, but authority differs.

---

## Object Stability

Because identity and genome are stable:

* objects remain consistent across observers
* objects can be reconstructed at any time
* objects do not depend on continuous simulation

This supports long-term persistence.

---

## Temporal Reconstruction

Because objects are event-driven, they can be reconstructed at any point in time.

This enables:

* replay systems
* debugging
* historical analysis
* branching exploration

---

## Minimal Object Model

At minimum, a CrypSA object requires:

* identity
* genome
* canonical event history

Derived state can always be computed.

---

## Key Insight

> CrypSA objects are derived from validated history, not stored as mutable state.

---

## Summary

The CrypSA object model describes objects as deterministic reconstructions of identity, genome, and canonical event history.

This allows consistent shared worlds without requiring centralized simulation or constant state synchronization.

---

## One Sentence Summary

A CrypSA object is a deterministic reconstruction of identity, genome, and validated event history, with current state derived from that history.
