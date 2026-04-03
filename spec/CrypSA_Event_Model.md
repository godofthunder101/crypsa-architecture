# CrypSA Event Model Spec v0.1

This document defines the structure, behavior, and lifecycle of events in CrypSA.

Events are the foundation of the system.

> Canonical events define shared reality.
> State is derived by replaying canonical event history.

---

## Core Principle

CrypSA is event-driven.

* the world is not the source of truth
* **canonical event history is the source of truth**
* world state is derived from that history

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

* accepted by the validator
* immutable
* part of canonical event history
* used for replay and reconstruction

---

## Event Lifecycle

Every event follows this lifecycle:

1. **Creation**
   Observer creates a candidate event

2. **Submission**
   Event is submitted to the validator

3. **Validation**
   Validator evaluates the event

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

Examples:

* `place_object`
* `destroy_object`
* `transfer_item`

---

#### `actor_id`

* the entity performing the action

---

#### `target_ids`

* objects affected by the event
* may be empty or contain multiple targets

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

#### `observer_time` (optional)

* timestamp from observer
* informational only
* must not be used for ordering

---

## Canonical Metadata (Validator-Assigned)

When an event is accepted, the validator assigns:

---

#### `canonical_event_id`

* unique identifier for the canonical event

---

#### `canonical_sequence`

* authoritative ordering index
* defines replay order

> `canonical_sequence` is assigned by the validator and defines canonical ordering.

---

#### `accepted_at`

* timestamp of acceptance (validator-defined)

---

## Canonical Event Definition

A canonical event is an accepted candidate event that:

* has passed validation
* has been assigned `canonical_sequence`
* has been appended to canonical event history
* is immutable

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

The system must ensure that duplicate `event_id` submissions do not create duplicate canonical events.

Each candidate event must be processed exactly once.

---

## Replay Requirement

State must be derived by:

* applying canonical events in `canonical_sequence` order

Replay must be:

* deterministic
* consistent across all observers
* equivalent to full reconstruction from canonical event history

---

## Payload Constraints

Event payloads must:

* be deterministic
* avoid hidden dependencies
* not rely on external mutable state

This ensures:

> replay produces identical results across observers

---

## Validation Relationship

Candidate events only become canonical through validation.

Validation ensures:

* invariants are preserved
* preconditions are satisfied
* rules are enforced

Rejected events:

* do not enter canonical event history
* must not affect canonical state

---

## Invariant Boundary Relationship

Candidate events originate from actions that cross the invariant boundary.

The invariant boundary defines:

* the transition from local simulation
* to canonical validation

Actions that do not cross this boundary:

* remain local
* do not produce candidate events

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

CrypSA uses validated, immutable canonical events as the source of truth, and all world state is derived by replaying those events in validator-defined canonical order.
