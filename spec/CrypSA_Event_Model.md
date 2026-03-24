# CrypSA Event Model Spec v0.1

This document defines the structure, behavior, and lifecycle of events in CrypSA.

Events are the foundation of the system.

> Canonical events define shared reality.
> State is derived by replaying canonical event history.

---

## Core Principle

CrypSA is event-driven.

* The world is not the source of truth
* **Canonical event history is the source of truth**
* World state is derived from that history

---

## Event Types

CrypSA defines two primary event types:

### 1. Candidate Events

* created by observers
* represent proposed actions
* not part of shared reality
* subject to validation

---

### 2. Canonical Events

* accepted by the server
* immutable
* part of canonical event history
* used for replay and reconstruction

---

## Event Lifecycle

Every event follows this lifecycle:

1. **Creation**
   Observer creates a candidate event

2. **Submission**
   Event is sent to the server

3. **Validation**
   Server evaluates the event

4. **Decision**

   * accepted → becomes canonical
   * rejected → discarded

5. **Canonicalization**

   * canonical metadata assigned
   * appended to canonical event history

6. **Propagation**
   Observers receive the canonical event

7. **Replay**
   Observers update state via replay

---

## Event Structure

CrypSA events consist of two layers:

* candidate event fields
* canonical metadata (added on acceptance)

---

### Candidate Event Fields

#### `event_id`

* unique identifier for the candidate event
* used for idempotency
* must be unique per submission

---

#### `event_type`

* defines the action type
* examples:

  * `place_object`
  * `destroy_object`
  * `transfer_item`

---

#### `actor_id`

* the entity performing the action

---

#### `target_ids`

* objects affected by the event
* may be empty or multiple

---

#### `payload`

* event-specific data
* must be deterministic
* must contain all data required for replay

Example:

```json
{
  "position": [10, 5],
  "object_kind": "house"
}
```

---

#### `precondition_refs`

* expected state conditions at time of submission
* used for validation

Example:

```json
{
  "tile_42_empty": true
}
```

---

#### `client_time` (optional)

* timestamp from observer
* informational only
* must not be used for ordering

---

## Canonical Metadata (Server-Assigned)

When an event is accepted, the server assigns:

---

#### `canonical_event_id`

* unique identifier for the canonical event

---

#### `server_sequence`

* authoritative ordering index
* defines replay order

---

#### `accepted_at`

* server timestamp of acceptance

---

## Canonical Event Guarantees

Canonical events must satisfy:

* **immutability**
  once accepted, events cannot change

* **append-only history**
  canonical event history is never rewritten

* **deterministic replay**
  same history → same state

---

## Idempotency Requirement

The system must ensure:

* duplicate `event_id` submissions
* do not create duplicate canonical events

Each candidate event must be processed exactly once.

---

## Replay Requirement

State must be derived by:

* applying canonical events in `server_sequence` order

Replay must be:

* deterministic
* consistent across all observers

---

## Payload Constraints

Event payloads must:

* be deterministic
* avoid hidden dependencies
* not rely on external mutable state

This ensures:

> replay produces identical results across observers

---

## Summary

CrypSA events:

* represent all canonical changes
* are validated before acceptance
* are stored in canonical event history
* define shared reality
* are replayed to reconstruct state

---

## One Sentence Summary

CrypSA uses validated, immutable canonical events as the source of truth, and all world state is derived by replaying those events in server-defined order.
