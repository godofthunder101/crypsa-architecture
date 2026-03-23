# CrypSA Snapshot Model Spec v0.1

This document defines how CrypSA captures and uses snapshots of derived world state.

Snapshots are used to:
- improve replay performance
- enable fast recovery
- support scalable persistence

---

## Core Principle

In CrypSA:

> Canonical history is the source of truth,  
> snapshots are derived performance artifacts.

Snapshots do not replace event history.

They are a cached representation of state at a specific point in that history.

---

## Snapshot Overview

A snapshot is:

- a derived state of the world
- tied to a specific canonical event position
- used as a starting point for replay

---

## Snapshot Position

Every snapshot must reference:

- a canonical event position  
  (e.g., `canonical_sequence`, event_id, or lineage point)

This ensures:

> Replay from snapshot + subsequent events produces the same result as full replay.

---

## Snapshot Contents

A snapshot contains:

- derived world state (objects, positions, properties)
- relevant system state (inventories, relationships, etc.)
- reference to event position
- version metadata

Snapshots should NOT contain:

- unvalidated or observer-local data
- transient client state
- candidate (non-canonical) events

---

## Snapshot Types

CrypSA supports multiple snapshot strategies:

---

### Full Snapshot

- captures entire world state
- used for full recovery or new observers

---

### Partial Snapshot

- captures a subset of the world
- examples:
  - region snapshot
  - object group snapshot

---

### Incremental Snapshot

- stores only changes since last snapshot
- reduces storage cost
- increases reconstruction complexity

---

## Snapshot Creation

Snapshots may be created:

- periodically (time-based)
- after a number of events
- during low-load periods
- on-demand (manual or system-triggered)

---

## Snapshot Frequency

Choosing frequency is a tradeoff:

| High Frequency | Low Frequency |
|----------------|----------------|
| Faster replay   | Lower storage cost |
| More storage    | Longer replay time |

---

## Snapshot Usage

Snapshots are used for:

---

### 1. Fast Startup

- new observers load snapshot
- replay only recent events

---

### 2. Recovery

- system restarts from snapshot
- avoids full replay

---

### 3. Partition Loading

- load only relevant world sections
- supports scalable systems

---

## Replay with Snapshots

Replay process with snapshots:

1. Load snapshot state
2. Identify snapshot event position
3. Fetch events after snapshot
4. Apply events in order
5. Produce current state

---

## Snapshot Consistency

Snapshots must satisfy:

- derived from valid canonical history
- correspond to a specific event position
- reproducible via replay

---

## Snapshot Validation

Snapshots should be verified by:

- comparing replay results against snapshot
- periodic consistency checks
- optional checksum or hash validation

---

## Snapshot Immutability

Snapshots are typically immutable once created.

If updated:
- a new snapshot is created
- old snapshots may be archived or deleted

---

## Snapshot Storage

Snapshots may be stored:

- locally (for single-node systems)
- in distributed storage systems
- in partitioned storage (per region/object)

---

## Snapshot Versioning

Snapshots must include:

- schema version
- compatible event version range
- definition (Genome/Mint) version references

This ensures:

> replay remains correct across system evolution

---

## Failure Modes

Snapshot systems must handle:

- corrupted snapshot data
- mismatch between snapshot and event history
- missing events after snapshot
- incompatible schema versions

---

## Performance Considerations

Snapshot performance depends on:

- snapshot size
- frequency
- serialization format
- partitioning strategy

Optimization strategies include:

- compression
- partial snapshots
- incremental updates
- caching hot regions

---

## Security Considerations

Snapshots must:

- only include canonical data
- be protected from tampering
- be verifiable against event history

---

## Tradeoffs

Snapshots introduce tradeoffs:

### Advantages

- faster replay  
- improved scalability  
- quicker recovery  
- reduced startup cost  

---

### Costs

- storage overhead  
- snapshot management complexity  
- consistency verification requirements  

---

## Relationship to Canonical History

Snapshots do not replace canonical history.

They are:

> a cached projection of that history at a point in time.

Canonical history remains:

- authoritative  
- complete  
- required for full reconstruction  

---

## Summary

CrypSA snapshots are:

- derived  
- versioned  
- position-aware  
- replay-compatible  

They ensure that:

> Event-driven worlds remain practical to operate at scale.

---
