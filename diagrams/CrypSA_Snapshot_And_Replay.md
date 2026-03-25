# CrypSA Snapshot and Replay

## Purpose

This diagram shows how CrypSA reconstructs current derived canonical state using:

* a snapshot
* the canonical event tail after that snapshot

It illustrates how CrypSA avoids replaying from genesis while keeping canonical event history as the source of truth.

---

## Diagram

```mermaid
flowchart LR

A[Canonical Event History] --> B[Create Snapshot at Sequence N]

B --> C[Observer Connects or Reconnects]
C --> D[Load Snapshot at Sequence N]

A --> E[Fetch Events After Sequence N]

D --> F[Apply Snapshot State]
E --> G[Replay Event Tail]

F --> H[Reconstructed Derived Canonical State]
G --> H

H --> I[Observer Continues Simulation]
````

---

## How to Read This

### 1. Canonical Event History Is the Source of Truth

Canonical event history defines what is real.

Snapshots do not replace history.

They are:

> cached reconstruction points

---

### 2. Snapshot Captures a Known State

A snapshot:

* is created from canonical event history
* captures derived canonical state at a specific sequence
* is tied to a known position in history

This allows:

> Snapshot + event tail = current derived canonical state

---

### 3. Observer Loads Snapshot

When an observer connects or reconnects, it can:

* load a snapshot
* avoid replaying from genesis

---

### 4. Replay Applies the Event Tail

The observer fetches and applies events after the snapshot position.

This reconstructs current derived canonical state deterministically.

---

### 5. Simulation Continues

Once reconstructed:

* the observer has up-to-date derived canonical state
* local simulation resumes

---

## Key Insight

> Snapshots improve practicality.
> Canonical event history remains the source of truth.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → canonical event history
* **Reconstruction** → replay + snapshot
* **Experience** → observer simulation

Snapshots are an optimization, not a source of truth.

---

## Relationship to Specs

This diagram maps to:

* `spec/CrypSA_Replay_Model.md`
* `spec/CrypSA_Snapshot_Model.md`
* `spec/CrypSA_Runtime_Spec_v0.1.md`

---

## One Sentence Summary

CrypSA uses snapshots as cached reconstruction points, allowing observers to load a known state and replay only the remaining event tail while canonical event history remains the authoritative source of truth.
