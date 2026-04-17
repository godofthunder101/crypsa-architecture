# CrypSA Runtime Model

## Purpose

This document defines the end-to-end runtime behavior of CrypSA at a conceptual level.

It explains how events move through the system and how canonical truth is established and observed.

For authoritative behavior, refer to the `/spec` directory.

For implications of this runtime model on infrastructure design, see:

→ `CrypSA_Infrastructure_Implications.md`

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

1. An observer performs an action  
2. The invariant boundary determines whether the action must be represented as a candidate event
   - If no, the result remains local  
   - If yes, a candidate event is created  
3. The candidate event is submitted to the validator  
4. The validator evaluates the candidate event using **validation rules derived from applicable invariants** to determine whether it becomes canonical  
   - If rejected, canonical event history does not change. Observers reconcile their local state with canonical event history  
5. If accepted, an event becomes canonical and is appended to canonical event history  
6. The canonical event is made available to observers
   - events may be delayed or arrive out of order  
   - ordering is resolved using `canonical_sequence`, which defines authoritative event order  
7. Observers apply canonical events via deterministic replay  
8. Observers reconcile their local state with canonical event history, yielding to canonical outcomes where differences exist  

This loop repeats continuously as observers interact with the system.

---

## Visual Representation

```mermaid
flowchart LR

A["Observer Action"] --> B["Invariant Boundary Check"]

B -->|Remains Local| L["Local Result (No Canonical Change)"]

B -->|Creates Candidate Event| C["Candidate Event"]

C --> D["Submit to Validator"]

D --> E["Validation (Enforcement of Invariants)"]

E -->|Rejected| R["Reject → Observers Reconcile Local State with Canonical Event History"]

E -->|Accepted| F["If accepted, an event becomes canonical and is appended to canonical event history"]

F --> G["Make Canonical Event Available to Observers"]

G --> H["Apply Canonical Events via Deterministic Replay"]

H --> I["Observer Reconciliation"]

I --> A
````

---

## Key Properties

### Observers Do Not Define Truth

Observers may perform local prediction, but they do not determine canonical outcomes.

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

## Canonical Authority Constraint

Canonical event history can only be extended through events accepted by the validator.

No other mechanism can modify canonical truth.

---

## Validator Role in the Runtime

The validator is responsible for:

1. Receiving candidate events
2. Evaluating events using **validation rules derived from applicable invariants**
3. Determining acceptance or rejection
4. Assigning `canonical_sequence` (establishing authoritative ordering)
5. Appending accepted events to canonical event history
6. Making canonical events available to observers

The validator defines what becomes canonical.

---

## Observer Role in the Runtime

Observers are responsible for:

* Local prediction and experience
* Generating candidate events (when crossing the invariant boundary)
* Maintaining predicted state
* Receiving canonical events
* Reconciling local state with canonical event history

Observers do not define truth.

---

## Relationship to Replay

Replay is the process of applying canonical event history to derive state.

This means:

* state is not authoritative
* canonical event history is authoritative
* replay ensures deterministic reconstruction of state

Snapshots and optimizations may be used, but they do not replace canonical history.

---

## Relationship to Consistency

CrypSA does not rely on direct state synchronization.

Consistency emerges through:

* shared canonical event history
* deterministic replay
* observer reconciliation

---

## Relationship to Deployment

The runtime model is independent of deployment.

The validator may run:

* locally
* remotely
* in a hybrid configuration

This does not change the runtime model.

---

## Summary

CrypSA is a system where:

* observers perform local prediction
* the invariant boundary determines what becomes a candidate event
* candidate events are validated using **validation rules derived from invariants**
* accepted events are appended to canonical event history
* canonical event history is replayed to deterministically produce state

👉 Truth is not synchronized.
👉 Truth is established through validated events and observed through deterministic replay.

---

## Additional Clarification

Canonical events define the only authoritative sequence of system changes.
