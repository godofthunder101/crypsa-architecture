# CrypSA Event Lifecycle

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes a conceptual lifecycle of how candidate events may become canonical in a CrypSA system.

It illustrates how observer actions propagate through validation and update shared reality defined by canonical event history.

This is a **conceptual model**, not an authoritative runtime specification.

---

## Core Principle

In CrypSA, actions do not directly change canonical event history.

Instead:

```text
Observer Action
→ Local Simulation
→ Candidate Event
→ Validation
→ Accepted Event (Canonical Event)
→ Assign server_sequence
→ Canonical Event History Update
→ Observer Reconciliation
````

Only accepted events affect shared reality.

---

## Conceptual Lifecycle

```text id="lifecycle_flow_fixed"
Observer Action
      ↓
Local Simulation
      ↓
Invariant Boundary Check
      ├── Remain Local
      └── Candidate Event
                ↓
         Event Submission
                ↓
             Validation
         ├── Reject → Local Correction
         └── Accept
                ↓
        Canonical Event Created
                ↓
        Assign server_sequence
                ↓
  Append to Canonical Event History
                ↓
     Observer Reconciliation
                ↓
    Continued Local Simulation
```

---

## Lifecycle Stages

### 1. Observer Action

An observer initiates an interaction.

Examples:

* placing a structure
* transferring ownership
* triggering a system event

This begins as local intent.

---

### 2. Local Simulation

The observer simulates the action locally:

* visual feedback
* prediction
* temporary effects

This keeps the experience responsive.

---

### 3. Invariant Boundary Check

The system determines:

> Does this affect canonical event history?

* No → remains local
* Yes → becomes a candidate event

---

### 4. Candidate Event

If canonical event history is affected:

* a candidate event is created
* it represents a proposed change
* it is **not yet canonical**

A minimal event may include:

* event type
* actor identity
* target identity
* payload

Additional metadata may exist depending on implementation.

---

### 5. Event Submission

The candidate event is sent to the server.

---

### 6. Validation

The server evaluates the event:

* schema validation
* identity validation
* precondition checks
* invariant enforcement
* rule validation

The event is:

* accepted
  or
* rejected

---

### 7. Canonical Event Acceptance

If accepted:

* the event becomes a **canonical event**
* the server assigns `server_sequence` (authoritative ordering)
* the event is appended to canonical event history

If rejected:

* no canonical change occurs
* the observer corrects local simulation

---

### 8. Observer Reconciliation

Observers receive updates and:

* confirm or correct local simulation
* rebuild affected objects via replay
* align with canonical event history

---

### 9. Continued Simulation

After reconciliation:

* observers continue simulation
* the lifecycle repeats

---

## Example: Build Attempt

### Local Step

A player places a structure locally.

---

### Candidate Event

The client submits:

```text
build_structure
actor = Player A
target = tile_42
payload = mining_station
```

---

### Validation

The server checks:

* tile exists
* tile is valid
* invariants are preserved

---

### Outcomes

**Accepted**

* event becomes a canonical event
* appended to canonical event history
* derived state updates via replay
* observers confirm

**Rejected**

* no canonical change
* local simulation corrected

---

## Observer Convergence

Observers may temporarily diverge locally.

After canonical updates:

* all observers reconstruct deterministically via replay
* shared reality (derived from canonical event history) converges

---

## Key Insight

> CrypSA systems evolve through validated canonical events recorded in canonical event history rather than continuous synchronized simulation.

---

## Notes on Implementation

Some implementations may include additional metadata or validation context.

These are optional and not required by the core model.

---

## Minimal Components

A minimal lifecycle requires:

* local simulation
* invariant boundary
* validation
* canonical event history
* observer reconciliation

---

## Summary

CrypSA systems:

* simulate locally
* validate when crossing the invariant boundary
* accept or reject candidate events
* append accepted events to canonical event history
* reconstruct shared reality deterministically

---

## One Sentence Summary

CrypSA models world evolution as a lifecycle where local actions become candidate events, validated events become canonical events, and accepted events are recorded in canonical event history for deterministic reconstruction by observers.
