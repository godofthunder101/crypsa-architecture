# CrypSA Specification (v0.1)

This folder contains the **authoritative runtime specifications** for CrypSA.

These documents define how the system behaves at runtime.

If the `architecture/` folder explains:

> what CrypSA is and why it exists

the `spec/` folder defines:

> how CrypSA behaves as a real system

---

## 🧭 Purpose of This Folder

The documents in this folder define the **minimum required runtime behavior** of CrypSA, including:

* event structure and lifecycle
* validation and invariant enforcement
* canonical event history rules
* ordering (`canonical_sequence`)
* consistency and reconciliation
* deterministic replay
* snapshot behavior
* identity and object lifecycle
* observer ↔ validator communication

These specifications make CrypSA:

* implementable
* testable
* technically reviewable

They do **not** define full production systems.

---

## ⚙️ Core Runtime Principle

> Canonical truth is defined by validated canonical events — not by synchronized state.

At runtime:

* observers propose candidate events
* the validator evaluates them
* accepted events are appended to canonical event history
* derived canonical state is reconstructed via deterministic replay

This model applies regardless of validator deployment:

* local
* host-based
* remote

---

## 🔒 Authority

Documents in this folder are **authoritative for runtime behavior**.

If a conflict exists between:

* `spec/`
* `architecture/`
* `implementation/`
* `exploratory/`

then:

> the `spec/` definitions take precedence

---

## 🧠 Ownership of Runtime Concepts

The `spec/` folder is the **single source of truth for runtime definitions**.

This includes:

* event structure
* validation behavior
* canonical event handling
* ordering (`canonical_sequence`)
* consistency and reconciliation rules
* replay and derived state behavior
* snapshot behavior
* identity and minting
* transport expectations

Other folders must:

* reference these definitions
* explain or illustrate them

They must **not redefine or override them**.

---

## 📚 Recommended Reading Order

If you are reading the specs for the first time:

1. `CrypSA_Runtime_Model.md`
   → Defines the overall runtime loop and system contract

2. `CrypSA_Event_Model.md`
   → Defines event structure and lifecycle

3. `CrypSA_Validation_Model.md`
   → Defines how candidate events are validated

4. `CrypSA_Consistency_Model.md`
   → Defines how shared reality converges

5. `CrypSA_Replay_Model.md`
   → Defines deterministic reconstruction

6. `CrypSA_Snapshot_Model.md`
   → Defines snapshot usage and performance

7. `CrypSA_Identity_Model.md`
   → Defines identity, minting, and lifecycle

8. `CrypSA_Transport_Model.md`
   → Defines observer ↔ validator communication

---

## 🧩 How to Read These Specs

These documents form a connected system:

* **Runtime Model** → defines the system loop
* **Event + Validation** → defines how truth is created
* **Consistency + Replay** → defines how truth is maintained
* **Snapshot + Identity + Transport** → defines how the system remains practical

---

## 🔁 Consistency Rules

All documents in this folder must:

* use consistent terminology
* not redefine shared concepts differently
* not contradict other spec documents

If ambiguity exists:

> the Runtime Model defines final behavior

---

## 🧠 Validator Model (Important)

The runtime model assumes:

> the validator is a role, not a location

Therefore:

* validation behavior must remain identical whether the validator runs:

  * locally
  * on a host
  * on a remote system

* deployment must not change:

  * event semantics
  * validation rules
  * canonical event history behavior

---

## 📦 Scope of v0.1

These specifications define CrypSA v0.1 as:

* a minimal canonical event-driven runtime
* observer ↔ validator interaction
* deterministic reconstruction
* a clear implementation baseline

Not yet included:

* combat adjudication
* advanced anti-cheat
* shard federation
* offline branch merging
* full networking guarantees
* cryptographic trust systems

These are future extensions.

---

## 🔗 Relationship to the Repo

Suggested reading flow:

### New to CrypSA

* `../CrypSA_In_One_Diagram.md`
* `../CrypSA_In_5_Minutes.md`
* `../CrypSA_Terminology_Primer.md`
* `../FAQ.md`

---

### Conceptual Understanding

* `../exploratory/`
* `../architecture/`

---

### Runtime Definition

* this `spec/` folder

---

### Implementation

* `../implementation/minimal_validator/CrypSA_Minimal_Validator_v0.1.md`
* `../implementation/CrypSA_Local_First_Development_Approach.md`

---

## 🚧 Current Status

These specifications are:

* stable for v0.1
* sufficient for implementation
* expected to evolve in future versions

---

## One Sentence Summary

The `spec/` folder defines the authoritative runtime behavior of CrypSA—how events, validation, consistency, replay, identity, snapshots, and transport work together to produce shared canonical reality through validator-controlled canonical event history.
