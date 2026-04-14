# CrypSA Runtime Model

## Purpose

This document defines the end-to-end runtime behavior of CrypSA at a conceptual level.

It explains how events move through the system and how canonical truth is established and observed.

For authoritative behavior, refer to the `/spec` directory.

---

## Authority Level

This document describes system structure and runtime flow.

It does not define validation rules or exact behavior.

If there is any conflict, the `/spec` takes precedence.

---

## Core Principle

👉 The validator defines what becomes canonical.  
👉 Canonical event history is the source of truth.

---

## Core Runtime Loop

CrypSA operates through a continuous event-driven loop:

1. An observer creates a candidate event  
2. The candidate event is submitted to the validator  
3. The validator evaluates the event against invariants  
4. If accepted, the event becomes canonical and is appended to canonical event history  
5. The canonical event is distributed  
6. Observers receive the canonical event  
7. Observers reconcile their local state with canonical event history, yielding to canonical outcomes where differences exist  

This loop repeats continuously.

---

## Key Properties

### Observers Do Not Define Truth

Observers may simulate and predict, but they do not determine canonical outcomes.

---

### Canonical Event History Is the Source of Truth

All authoritative state is derived from canonical event history.

There is no separate source of truth.

---

### No Direct State Authority

No system component maintains authoritative state outside of canonical event history.

---

### State Is Derived, Not Stored as Truth

System state is reconstructed from canonical event history through replay.

Any stored state is a derived representation.

---

### Replay Is Fundamental

Replay is not a recovery feature.

Replay is the mechanism by which canonical event history becomes observable system state.

---

### Local Prediction May Diverge

Observers may temporarily diverge from canonical truth due to local prediction, but must reconcile upon receiving canonical events.

---

### Convergence Occurs Through Canonical Events

Observers converge toward canonical truth as canonical events are received and applied.

---

## Event Lifecycle (Conceptual)

An event moves through the following stages:

- Created as a candidate by an observer  
- Submitted to the validator  
- Evaluated against invariants  
- If accepted, becomes canonical  
- Appended to canonical event history  
- Distributed to observers  
- Applied by observers to reconcile local state with canonical event history  

---

## Validator Role in the Runtime

The validator is responsible for:

1. Receiving candidate events  
2. Evaluating events against invariants  
3. Determining acceptance or rejection  
4. Assigning canonical sequence (establishing order within canonical event history)  
5. Appending accepted events to canonical event history  
6. Distributing canonical events to observers  

The validator defines what becomes canonical.

---

## Observer Role in the Runtime

Observers are responsible for:

- Local simulation and experience  
- Generating candidate events  
- Maintaining predicted state  
- Receiving canonical events  
- Reconciling local state with canonical event history  

Observers do not define truth.

---

## Relationship to Replay

Replay is the process of applying canonical event history to derive state.

This means:

- state is not authoritative  
- canonical history is authoritative  
- replay ensures deterministic reconstruction of state  

Snapshots and optimizations may be used, but they do not replace canonical history.

---

## Relationship to Consistency

CrypSA does not rely on direct state synchronization.

Consistency emerges through:

- shared canonical event history  
- deterministic replay  
- observer reconciliation  

---

## Relationship to Deployment

The runtime model is independent of deployment.

The validator may run:

- locally  
- remotely  
- in a hybrid configuration  

This does not change the runtime model.

---

## Summary

CrypSA is a system where:

- events are proposed by observers  
- validated by a validator  
- recorded as canonical history  
- replayed to deterministically produce state  

👉 Truth is not synchronized.  
👉 Truth is established through validated events and observed through deterministic replay.

---

## Additional Clarification

Canonical events define the only authoritative sequence of system changes.
