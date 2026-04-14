# CrypSA Project Status

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This document provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details may vary based on product requirements.

This document illustrates one possible way to structure a system that conforms to CrypSA.

---

## Purpose

This document describes the current state of the CrypSA project.

It clarifies:

* what has been defined
* what has been prototyped
* what has not yet been built
* what the immediate next steps are

---

## Current State (v0.1 Phase)

CrypSA is currently:

* a defined architecture
* supported by structured documentation
* backed by a completed teaching prototype
* not yet a production runtime

CrypSA is:

* architecturally complete
* runtime incomplete

The project has moved beyond a conceptual idea and now includes:

* formal specifications
* a defined runtime model
* a clear implementation direction

---

## Core Model (Mental Frame)

CrypSA separates responsibilities into four layers:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining observer meaning
* **Experience** — UI and local simulation

The validator controls truth.

👉 The validator defines what becomes canonical and therefore controls canonical truth.

Observers simulate locally.

* canonical event history is ordered via canonical_sequence
* canonical event history is the source of truth

If accepted, an event becomes canonical and is appended to canonical event history.

---

## Documentation Authority

CrypSA uses a layered documentation model.

Current authority order is:

1. `../spec/` — authoritative for runtime behavior
2. `../architecture/` — authoritative for system structure
3. `../implementation/` — implementation direction and engineering guidance
4. `../teaching/` — teaching materials and prototype explanation
5. `../exploratory/`, `../design/`, `../diagrams/`, `../atlas/` — supporting or non-authoritative material

Important:

> `exploratory/` provides historical background and conceptual context.
> It is not the current source of truth for CrypSA runtime behavior.

---

## What Exists Today

### 1. Authoritative Architecture and Runtime Definition

The repository currently defines CrypSA through:

* `../architecture/` — system structure and architectural boundaries
* `../spec/` — runtime behavior and implementation-facing system contracts

Together, these describe:

* the observer model
* the validator role in validation and canonical event handling
* validated canonical event-driven world evolution
* invariant-based validation
* reconstruction via replay of canonical event history ordered via canonical_sequence

---

### 2. Supporting Historical and Exploratory Material

The repository also includes:

* `../exploratory/foundation/`
* `../exploratory/core_concepts/`

These documents provide background, earlier framing, and conceptual exploration.

They are useful for historical context and idea evolution, but they are not authoritative for the current CrypSA model.

---

### 3. Formal Specifications

The `../spec/` folder defines intended runtime behavior.

Current coverage includes:

* runtime behavior
* event structure
* validation pipeline
* consistency model
* replay model
* snapshot model
* identity model
* transport model
* canonical ordering model (`canonical_sequence`)

These documents define how CrypSA is expected to function as a system.

---

### 4. Teaching Prototype

A local teaching prototype exists in:

`../teaching/CrypSA_teaching_prototype/`

For authoritative prototype status, see:

`../teaching/CrypSA_teaching_prototype/STATUS.md`

It demonstrates:

* canonical event flow
* validation and invariant boundaries
* explicit invariant boundary enforcement
* canonical vs observer-local state
* replay-derived canonical state
* adapter and lens separation

Status:

* complete for its intended purpose
* stable and internally consistent
* frozen except for bug fixes and documentation updates

Important:

> This prototype demonstrates the CrypSA model locally.
> It is not a proof of networked runtime behavior.

---

### 5. Minimal Validator Design

A minimal validator design has been defined in:

* `CrypSA_Minimal_Server_v0.1.md`

This document describes:

* the smallest viable independent validator
* validation pipeline structure
* invariant boundary enforcement
* canonical event handling and ordering (`canonical_sequence`)
* observer interaction

---

## What Does NOT Exist Yet

The following are **not yet implemented**:

* a fully functional independent CrypSA validator runtime
* real networked multi-observer runtime
* production-grade persistence layer
* large-scale performance testing
* shard or partition coordination
* advanced anti-cheat systems
* cryptographic validation or trust systems
* branch merging or offline synchronization
* verified canonical ordering under distributed conditions

---

## Teaching Prototype Limitations

The teaching prototype:

* runs locally
* does not use real networking
* simplifies validation and conflict handling
* does not represent real latency or concurrency
* prioritizes clarity over production correctness

It exists to:

> demonstrate the model, not prove runtime behavior

---

## What the Project is Trying to Prove

CrypSA is currently focused on proving:

1. that canonical event-driven truth with deterministic ordering is viable
2. that invariant-based validation can replace full server simulation
3. that observers can reconstruct derived canonical state from canonical event history
4. that observer reconciliation is manageable
5. that deterministic reconstruction via replay of canonical event history ordered via canonical_sequence is reliable

---

## Determinism Guarantee

Given the same:

* canonical event history
* interpretation logic

reconstruction must produce equivalent derived canonical state

---

## Next Major Step

### CrypSA Minimal Validator v0.1

The teaching prototype demonstrates the model.

The minimal validator will test CrypSA as a runtime system.

This introduces:

* an independent validator process
* real event submission over a network
* validation pipeline execution
* canonical event history (ordered via canonical_sequence)
* derived canonical state reconstruction via replay
* multi-observer interaction

---

### Key Distinction

* The **teaching prototype** exists to make the model understandable
* The **minimal validator** exists to test the model under real runtime conditions

---

## Near-Term Development Focus

Immediate priorities:

1. build the minimal validator runtime
2. connect multiple observers
3. test validation and conflict resolution
4. validate replay and reconstruction
5. test reconnect and snapshot recovery
6. validate canonical ordering under network conditions

---

## Future Direction

Long-term evolution is described in:

👉 `CrypSA_Roadmap.md`

---

## How to Approach This Repository

### To understand the idea

* `../CrypSA_In_5_Minutes.md`
* `../CrypSA_Terminology_Primer.md`
* `../FAQ.md`

---

### To understand the current system definition

* `../architecture/`
* `../spec/`

Use `../spec/` for runtime behavior and `../architecture/` for system structure.

---

### To understand the model in practice

* `../teaching/CrypSA_teaching_prototype/`

Treat this as a completed teaching artifact, not as the runtime proof.

---

### To understand historical context

* `../exploratory/foundation/`
* `../exploratory/core_concepts/`

Use these for background only, not as the current source of truth.

---

### To understand how to build it

* `CrypSA_Minimal_Server_v0.1.md`

---

## One Sentence Summary

CrypSA is a defined architecture with formal specifications and a completed teaching prototype, now moving toward its first real runtime implementation through a minimal validator while preserving canonical event history as the source of truth, canonical ordering via canonical_sequence, and deterministic reconstruction via replay.
