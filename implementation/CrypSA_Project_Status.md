# CrypSA Project Status

> Scope note: This document describes project status and implementation direction.
>
> For authoritative runtime behavior, refer to `../spec/`.

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

The server controls truth.

Observers simulate locally.

---

## What Exists Today

### 1. Conceptual Architecture

The repository defines:

* observer model
* canonical server model
* event-driven world evolution
* invariant-based validation
* reconstruction from canonical event history

These are described in:

* `exploratory/foundation/`
* `exploratory/core_concepts/`
* `architecture/`

---

### 2. Formal Specifications

The `spec/` folder defines intended runtime behavior.

Current coverage includes:

* runtime behavior
* event structure
* validation pipeline
* consistency model
* replay model
* snapshot model
* identity model
* transport model

These documents describe how CrypSA is expected to function as a system.

---

### 3. Teaching Prototype

A local teaching prototype exists in:

`teaching/crypsa_teaching_prototype/`

For authoritative prototype status, see:

`../teaching/CrypSA_teaching_prototype/STATUS.md`

It demonstrates:

* canonical event flow
* validation and invariant boundaries
* canonical vs observer-local state
* replay-derived state
* adapter and lens separation

Status:

* complete for its intended purpose
* stable and internally consistent
* frozen except for bug fixes and documentation updates

Important:

> This prototype demonstrates the CrypSA model locally.
> It is not a proof of networked runtime behavior.

---

### 4. Minimal Server Design

A minimal server design has been defined in:

* `implementation/CrypSA_Minimal_Server_v0.1.md`

This document describes:

* the smallest viable independent server
* validation pipeline structure
* canonical event handling
* observer interaction

---

## What Does NOT Exist Yet

The following are **not yet implemented**:

* a fully functional independent CrypSA server
* real networked multi-client runtime
* production-grade persistence layer
* large-scale performance testing
* shard or partition coordination
* advanced anti-cheat systems
* cryptographic validation or trust systems
* branch merging or offline synchronization

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

1. that canonical event-driven truth is viable
2. that invariant-based validation can replace full server simulation
3. that observers can reconstruct shared state from canonical event history
4. that observer reconciliation (alignment of local prediction with canonical truth) is manageable

The goal is to validate the architecture, not optimize it.

---

## Next Major Step

## CrypSA Minimal Server v0.1

The teaching prototype demonstrates the model.

The minimal server will test CrypSA as a runtime system.

This introduces:

* an independent server process
* real event submission over a network
* validation pipeline execution
* canonical event history
* derived state updates
* multi-observer interaction

---

### Key Distinction

* The **teaching prototype** exists to make the model understandable
* The **minimal server** exists to test the model under real runtime conditions

---

## Near-Term Development Focus

Immediate priorities:

1. build the minimal server runtime
2. connect multiple observers
3. test validation and conflict resolution
4. validate replay and reconstruction
5. test reconnect and snapshot recovery

---

## Future Direction

Long-term evolution is described in:

👉 `CrypSA_Roadmap.md`

---

## How to Approach This Repository

### To understand the idea

* `CrypSA_In_5_Minutes.md`
* `CrypSA_Terminology_Primer.md`
* `FAQ.md`

---

### To understand the system

* `architecture/`
* `spec/`

---

### To understand the model in practice

* `teaching/crypsa_teaching_prototype/`

---

### To understand how to build it

* `implementation/CrypSA_Minimal_Server_v0.1.md`

---

## One Sentence Summary

CrypSA is a defined architecture with formal specifications and a completed teaching prototype, now moving toward its first real runtime implementation through a minimal independent server.
