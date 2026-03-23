# CrypSA Snapshot and Replay

This diagram shows how CrypSA reconstructs current canonical state using:

- a snapshot
- the canonical event tail after that snapshot

It illustrates how CrypSA avoids replaying from genesis every time while keeping canonical history as the source of truth.

---

```mermaid
flowchart LR

A[Canonical Event Log] --> B[Snapshot Created at Sequence N]

B --> C[Observer Connects or Reconnects]
C --> D[Load Snapshot at Sequence N]

A --> E[Fetch Events After Sequence N]
D --> F[Apply Snapshot State]
E --> G[Replay Event Tail]

F --> H[Reconstructed Current State]
G --> H

H --> I[Observer Continues from Canonical Truth]

````

---

## How to Read This

### 1. Canonical History Remains the Source of Truth

CrypSA stores canonical events as the authoritative history.

Snapshots do not replace this history.

They are:

> cached reconstruction points

---

### 2. A Snapshot Is Created at a Known Position

At some canonical position:

* a snapshot is generated
* it captures derived state
* it is tied to a specific sequence or event position

This means:

> Snapshot + later events = current state

---

### 3. An Observer Joins or Reconnects

When an observer needs to reconstruct the world, it does not always need full replay from genesis.

Instead it can:

* load the latest relevant snapshot
* fetch events after that snapshot
* replay only the missing tail

---

### 4. Replay Applies the Event Tail

The observer applies canonical events after the snapshot position in canonical order.

This rebuilds the current state consistently.

---

### 5. The Observer Continues from Canonical Truth

After reconstruction:

* the observer has current canonical state
* local simulation can continue from there

---

## Key Insight

> Snapshots improve practicality.
> Canonical history remains the real source of truth.

---

## Relationship to Specs

This diagram maps directly to:

* `spec/CrypSA_Replay_Model.md`
* `spec/CrypSA_Snapshot_Model.md`
* `spec/CrypSA_Runtime_Spec_v0.1.md`

---

## One Sentence Summary

CrypSA uses snapshots as cached reconstruction points, allowing observers to load a known canonical state and replay only the remaining event tail to reach the current world state.
