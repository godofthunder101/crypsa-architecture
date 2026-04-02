# CrypSA Specification (v0.1)

This folder contains the implementation-facing specifications for CrypSA.

These documents define how the system behaves at runtime.

If the `architecture/` folder explains:

> what CrypSA is and why it exists

the `spec/` folder defines:

> how CrypSA functions as a real system

---

## Purpose of This Folder

The documents in this folder define the core runtime behavior of CrypSA, including:

* how events are structured
* how validation works
* how consistency is maintained
* how replay reconstructs state
* how snapshots improve performance
* how identities remain stable over time
* how events are transported between observers and the validator

These documents define the **minimum required system behavior** needed to make CrypSA:

* technically reviewable
* implementable
* testable

They do not define full production systems.

---

## Core Runtime Principle

> Canonical truth is defined by validated canonical events, not by synchronized state.

At runtime:

* observers propose candidate events
* the validator evaluates them
* accepted events are appended to canonical event history
* derived canonical state is reconstructed via replay

This model applies regardless of validator deployment:

* local
* host-based
* or remote

---

## Authority

Documents in this folder are **authoritative for runtime behavior**.

If a conflict exists between:

* `spec/`
* `architecture/`
* `implementation/`
* `exploratory/`

then:

> the `spec/` definitions take precedence

---

## Ownership of Runtime Concepts

The `spec/` folder is the **single source of truth for runtime definitions**.

This includes:

* event structure
* validation behavior
* canonical event handling
* ordering (`server_sequence`)
* consistency and reconciliation rules
* replay and derived state behavior
* snapshot and identity behavior
* transport expectations

Other folders must:

* reference these definitions
* explain or illustrate them

They must **not redefine or override them**.

If a runtime concept appears in multiple places:

> the definition in `spec/` is authoritative

---

## Recommended Reading Order

If you are reading the specs for the first time, use this order:

1. `CrypSA_Runtime_Spec_v0.1.md`
   Defines the overall runtime loop and system contract

2. `CrypSA_Event_Model_Spec_v0.1.md`
   Defines event structure and lifecycle

3. `CrypSA_Validation_Model_Spec_v0.1.md`
   Defines how candidate events are validated

4. `CrypSA_Consistency_Model_v0.1.md`
   Defines how shared reality converges

5. `CrypSA_Replay_Model_Spec_v0.1.md`
   Defines deterministic reconstruction

6. `CrypSA_Snapshot_Model_Spec_v0.1.md`
   Defines snapshot usage and performance

7. `CrypSA_Identity_Model_Spec_v0.1.md`
   Defines identity, minting, and object lifecycle

8. `CrypSA_Transport_Model_Spec_v0.1.md`
   Defines communication between observers and the validator

---

## How to Read These Specs

The specs are designed to be read as a connected system.

A useful mental model:

* **Runtime Spec** → defines the overall system loop
* **Event + Validation** → defines how truth is created
* **Consistency + Replay** → defines how truth is maintained
* **Snapshot + Identity + Transport** → defines how the system remains practical

---

## Consistency Rules

All documents in this folder must:

* use consistent terminology
* not redefine shared concepts differently
* not contradict other spec documents

If ambiguity exists:

> the Runtime Spec defines the final behavior

---

## Validator Consistency (Important)

The runtime model defined here assumes:

> the validator is a role, not a location

Therefore:

* validation behavior must remain identical whether the validator runs:

  * locally
  * on a host
  * or on a remote system

* deployment must not change:

  * event semantics
  * validation rules
  * canonical event history behavior

---

## Scope of the Current Specs

These specifications define CrypSA v0.1.

They are intended to define:

* a minimal canonical event-driven runtime
* observer ↔ validator interaction
* deterministic reconstruction
* practical implementation direction

They do **not yet fully define**:

* combat adjudication
* advanced anti-cheat
* shard federation
* offline branch merging
* full production networking guarantees
* cryptographic trust systems

These belong to future versions.

---

## Relationship to the Rest of the Repo

Suggested reading flow:

---

### New to CrypSA

* `../CrypSA_In_One_Diagram.md`
* `../CrypSA_In_5_Minutes.md`
* `../CrypSA_Terminology_Primer.md`
* `../FAQ.md`

---

### Conceptual / exploratory understanding

* `../exploratory/foundation/`
* `../exploratory/core_concepts/`
* `../architecture/`

---

### Formal system definition

* this `spec/` folder

---

### Implementation direction

* `../implementation/CrypSA_Minimal_Server_v0.1.md`
* `../implementation/CrypSA_Local_First_Design_Pattern.md`

---

## Current Status

These specifications define the CrypSA system at a runtime level.

They are:

* stable for v0.1
* sufficient for implementation
* expected to evolve in future versions

---

## One Sentence Summary

The `spec/` folder defines the authoritative runtime behavior of CrypSA—how events, validation, consistency, replay, identity, snapshots, and transport work together to produce shared canonical reality through validator-controlled canonical event history.
