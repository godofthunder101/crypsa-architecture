# CrypSA Snapshot Model Spec v0.1

This document defines how CrypSA captures and uses snapshots of derived canonical state.

Snapshots are used to:

* improve replay performance
* enable fast recovery
* support practical reconstruction for reconnect and late join

---

## Core Principle

In CrypSA:

> Canonical event history is the source of truth.
> Snapshots are derived performance artifacts.

Snapshots do not replace canonical event history.

They are cached representations of derived canonical state at a specific point in canonical history.

---

## Snapshot Overview

A snapshot is:

* derived canonical state
* tied to a specific canonical sequence position
* used as a starting point for replay

---

## Snapshot Position

Every snapshot must reference:

* `server_sequence`

It may also include:

* the last canonical event ID included in the snapshot

This ensures:

> replay from snapshot + subsequent canonical events produces the same result as full replay

> `server_sequence` is assigned by the validator and defines canonical ordering.

---

## Snapshot Contents

A snapshot contains:

* derived canonical state
* relevant system state required for reconstruction
* snapshot position (`server_sequence`)
* version metadata

Snapshots must not contain:

* unvalidated or observer-local data
* transient client state
* candidate events
* data that cannot be reproduced from canonical event history

---

## Snapshot Types

CrypSA may support multiple snapshot strategies.

### 1. Full Snapshot

* captures the full derived canonical state
* used for full recovery or new observers

---

### 2. Partial Snapshot

* captures a subset of derived canonical state

Examples:

* region snapshot
* object-group snapshot

---

### 3. Incremental Snapshot

* stores only changes since the previous snapshot
* reduces storage cost
* increases reconstruction complexity

---

### v0.1 Requirement

Version 0.1 only requires support for a basic full snapshot model.

---

## Snapshot Creation

Snapshots may be created:

* periodically
* after a number of accepted canonical events
* during low-load periods
* on demand

---

## Snapshot Frequency

Choosing snapshot frequency is a tradeoff:

| High Frequency | Low Frequency      |
| -------------- | ------------------ |
| Faster replay  | Lower storage cost |
| More storage   | Longer replay time |

---

## Snapshot Usage

Snapshots are used for:

### 1. Fast Startup

* observers load a snapshot
* replay only recent canonical events

---

### 2. Recovery

* system restarts from a snapshot
* avoids full replay from genesis

---

### 3. Partial Loading

* load only relevant world sections (if supported)
* useful for larger systems beyond the minimal model

---

## Replay with Snapshots

Replay using snapshots follows this process:

1. load snapshot state
2. read snapshot `server_sequence`
3. fetch canonical events after that sequence
4. apply events in `server_sequence` order
5. produce current derived canonical state

---

## Snapshot Consistency

Snapshots must satisfy all of the following:

* derived from valid canonical event history
* tied to a specific `server_sequence`
* reproducible via replay
* equivalent to replaying history up to that sequence

---

## Snapshot Validation

Snapshots should be verified by:

* comparing replay results against snapshot contents
* periodic consistency checks
* optional checksum or hash validation

If a mismatch exists:

> canonical event history is authoritative, and the snapshot must be treated as invalid

---

## Snapshot Immutability

Snapshots are typically immutable once created.

If state changes:

* a new snapshot is created
* old snapshots may be archived or deleted

---

## Snapshot Storage

Snapshots may be stored:

* locally for single-node systems
* in distributed storage systems
* in partitioned storage for larger deployments

Version 0.1 only requires a simple local or file-backed approach.

---

## Snapshot Versioning

Snapshots must include:

* snapshot schema version
* compatible event model version
* relevant genome / definition version references

This ensures replay remains correct across system evolution.

---

## Failure Modes

Snapshot systems must handle:

* corrupted snapshot data
* mismatch between snapshot and canonical event history
* missing canonical events after the snapshot
* incompatible schema versions

---

## Performance Considerations

Snapshot performance depends on:

* snapshot size
* snapshot frequency
* serialization format
* replay tail length

---

### Optimization Strategies

* compression
* partial snapshots
* incremental snapshots
* caching frequently used regions

---

## Security Considerations

Snapshots must:

* contain only canonical-derived data
* be verifiable against canonical event history
* never override canonical event history in the event of mismatch

---

## Tradeoffs

### Advantages

* faster replay
* quicker recovery
* reduced startup cost
* more practical reconnect behavior

---

### Costs

* storage overhead
* snapshot management complexity
* consistency verification requirements

---

## Relationship to Canonical Event History

Snapshots do not replace canonical event history.

They are:

> cached projections of canonical event history at a specific canonical sequence

Canonical event history remains:

* authoritative
* complete
* required for full reconstruction

---

## Summary

CrypSA snapshots are:

* derived
* versioned
* sequence-aware
* replay-compatible

They make event-driven worlds practical to operate without changing the source of truth.

---

## One Sentence Summary

CrypSA snapshots are derived, sequence-bound representations of canonical state that accelerate replay while preserving canonical event history as the sole source of truth.
