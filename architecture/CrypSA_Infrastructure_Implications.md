# CrypSA Infrastructure Implications

## Purpose

This document describes how the CrypSA architecture changes the distribution of computation, state, and synchronization in a system.

It focuses on **what changes compared to traditional architectures**, not on measured performance or cost outcomes.

The goal is to provide a clear, neutral understanding of:

* how responsibilities shift within the system
* what infrastructure patterns are no longer required
* what new considerations are introduced

This document does not claim performance improvements.

It outlines implications that may affect scalability, complexity, and infrastructure design.

For the underlying runtime model, see:

→ ../architecture/CrypSA_Runtime_Model.md

For terminology definitions, see:

→ ../architecture/CrypSA_Terminology_Primer.md

---

## 📜 Authority Level

This document describes architectural implications.

It does not define runtime behavior.

It does not define implementation details.

If there is any conflict:

* `/spec` defines behavior
* `/architecture` defines system structure
* this document describes consequences of that structure

---

## Traditional System Model

In a typical server-authoritative system:

> In this document, “server” refers to a traditional authoritative runtime, not the CrypSA validator role.

* the server runs a continuous authoritative simulation loop
* the server maintains mutable state
* clients send actions to the server
* the server resolves interactions
* the server synchronizes state to clients

This requires:

* continuous server-side computation
* state storage and mutation on the server
* frequent state synchronization across the network
* reconciliation logic on clients

---

## CrypSA System Model

In CrypSA:

* observers perform local prediction
* actions become candidate events when crossing the invariant boundary
* the validator determines what becomes canonical
* accepted events are appended to canonical event history
* observers reconstruct state via replay

This removes the requirement for:

* continuous authoritative simulation loop
* server-owned mutable world state
* direct state synchronization between clients

---

## Responsibility Shift

CrypSA changes where key responsibilities live.

### Simulation

* Traditional → server (authoritative runtime)
* CrypSA → observer

Observers perform local prediction for responsiveness.

---

### State Representation

* Traditional → server-managed mutable state
* CrypSA → derived from canonical event history

State is reconstructed through deterministic replay.

---

### Authority

* Traditional → server runtime
* CrypSA → validator role

The validator defines what becomes canonical.

---

### Synchronization

* Traditional → state replication
* CrypSA → canonical event distribution

Observers receive events and derive state independently.

---

## Infrastructure Implications

These architectural changes lead to different infrastructure characteristics.

### Reduced Continuous Server Computation

Because local prediction occurs on observers:

* the system does not require a continuously running authoritative simulation loop

---

### Reduced State Synchronization Requirements

Because state is derived from events:

* large state payloads do not need to be transmitted
* synchronization is based on events rather than full state updates

---

### Event-Based Network Traffic

Network communication shifts from:

* state updates → event distribution

This may result in:

* smaller payload sizes
* different bandwidth patterns
* reliance on ordered event delivery (`canonical_sequence`)

---

### Simplified Backend State Model

Because canonical truth is stored as event history:

* backend systems can use append-only storage
* mutation-heavy state management is reduced

---

### Replay-Dependent State

Because state is derived:

* replay becomes a core system requirement
* performance depends on replay efficiency and optimization strategies

---

## New Considerations

CrypSA introduces new areas that must be handled carefully.

### Validator Scalability

The validator must:

* process candidate events
* enforce invariants
* maintain ordering

Its performance characteristics become critical.

---

### Event Throughput

The system must handle:

* event ingestion
* event ordering
* event distribution

Throughput requirements depend on application design.

---

### Replay Performance

Replay must remain:

* deterministic
* efficient
* scalable with event history size

Optimization strategies may be required.

---

### Event Storage and Persistence

Canonical event history must be:

* durable
* ordered
* queryable for replay

Storage design becomes an important consideration.

---

## What Must Be Proven

The following areas require practical validation:

* validator performance under load
* replay performance at scale
* event throughput limits
* comparison of event-based vs state-based bandwidth usage

These are implementation concerns that determine real-world outcomes.

---

## Summary

CrypSA does not eliminate infrastructure requirements.

It changes:

* where computation occurs
* how state is represented
* how systems synchronize

These changes may lead to different scaling characteristics and system designs.

---

## One Sentence Summary

CrypSA shifts local prediction to observers, replaces synchronized state with canonical event history, and uses validation to define truth, resulting in a fundamentally different distribution of infrastructure responsibilities.
