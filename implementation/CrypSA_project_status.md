# CrypSA Project Status

This document describes the current state of the CrypSA project.

It clarifies:

- what has been defined  
- what has been prototyped  
- what has not yet been built  
- what the immediate next steps are  

---

## Current State (v0.1 Phase)

CrypSA is currently:

- a defined architecture  
- supported by structured documentation  
- backed by a completed teaching prototype  
- not yet a production runtime  

The project has moved beyond a conceptual idea and now includes:

- formal specifications  
- a defined runtime model  
- a clear implementation direction  

---

## Core Model (Mental Frame)

CrypSA separates responsibilities into four layers:

- **Truth** — canonical events and validation  
- **Translation** — adapters shaping runtime data  
- **Interpretation** — lenses determining observer meaning  
- **Experience** — UI and local simulation  

The current repository demonstrates this model conceptually and through the teaching prototype.

---

## What Exists Today

### 1. Conceptual Architecture

The repository defines:

- observer model  
- canonical server model  
- event-driven world evolution  
- invariant-based validation  
- reconstruction from canonical history  

These are described in:

- `foundation/`  
- `core-concepts/`  
- `architecture/`  

---

### 2. Formal Specifications

The `spec/` folder defines the system at a runtime level.

Current spec coverage includes:

- runtime behavior  
- event structure  
- validation pipeline  
- consistency model  
- replay model  
- snapshot model  
- identity model  
- transport model  

These documents define how CrypSA is expected to function as a system.

---

### 3. Teaching Prototype

A local teaching prototype exists in:

`teaching/crypsa_teaching_prototype/`

It demonstrates:

- canonical event flow  
- validation and invariant boundaries  
- canonical vs observer-local state  
- replay-derived state  
- event lineage and branching  
- adapter and lens separation in practice  

Status:

- complete for its intended purpose  
- stable and internally consistent  
- frozen except for bug fixes and documentation updates  

Important:

> This prototype demonstrates the CrypSA model locally.  
> It is not a runtime or network proof.

---

### 4. Minimal Server Design

A minimal server design has been defined in:

- `implementation/CrypSA_Minimal_Server_v0.1.md`

This document describes:

- the smallest viable independent server  
- validation pipeline structure  
- canonical event handling  
- observer interaction  

---

## What Does NOT Exist Yet

The following are **not yet implemented**:

- a fully functional independent CrypSA server  
- real networked multi-client runtime  
- production-grade persistence layer  
- large-scale performance testing  
- shard or partition coordination  
- advanced anti-cheat systems  
- cryptographic validation or trust systems  
- branch merging or offline synchronization  

---

## Teaching Prototype Limitations

The teaching prototype:

- runs locally  
- does not use real networking  
- simplifies validation and conflict handling  
- does not represent real latency or concurrency  
- focuses on clarity over production correctness  

It is intended to:

> demonstrate the model, not prove runtime behavior  

---

## What the Project is Trying to Prove

CrypSA is currently focused on proving:

1. that canonical event-driven truth is viable  
2. that invariant-based validation can replace full server simulation  
3. that observers can reconstruct shared state from event history  
4. that reconciliation between local prediction and canonical truth is manageable  

The goal is to validate the architecture, not optimize it.

---

## Next Major Step

The next major milestone is:

## CrypSA Minimal Server v0.1

The teaching prototype demonstrates the CrypSA model.

The minimal server will test CrypSA as a runtime system.

This will introduce:

- an independent server process  
- real event submission over a network  
- validation pipeline execution  
- canonical event log  
- derived state updates  
- multi-observer interaction  

This step moves CrypSA from:

> defined architecture → working runtime system  

---

### Key Distinction

- The **teaching prototype** exists to make the model understandable  
- The **minimal server** exists to test whether the model holds under real runtime conditions  

This separation is intentional:

- the prototype prioritizes clarity  
- the server will prioritize correctness under real constraints  

---

## Near-Term Development Focus

The immediate priorities are:

1. build the minimal server runtime  
2. connect multiple observers to the server  
3. test event validation and conflict resolution  
4. validate replay and reconstruction behavior  
5. test reconnection and snapshot-based recovery  

---

## Future Direction

Longer-term evolution of CrypSA (scalability, security, advanced features) is described in:

👉 `ROADMAP.md`

---

## How to Approach This Repository

### To understand the idea
- `CRYPSA_IN_5_MINUTES.md`  
- `TERMINOLOGY_PRIMER.md`  
- `FAQ.md`  

---

### To understand the system
- `architecture/`  
- `spec/`  

---

### To understand the model in practice
- `teaching/crypsa_teaching_prototype/`  

---

### To understand how to build it
- `implementation/CrypSA_Minimal_Server_v0.1.md`  

---

## One Sentence Summary

CrypSA is a defined architecture with formal specifications and a completed teaching prototype, now moving toward its first real runtime implementation via a minimal independent server.
