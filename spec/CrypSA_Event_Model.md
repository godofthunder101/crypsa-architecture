# CrypSA Event Model Spec v0.1

This document defines the structure, behavior, and lifecycle of events in CrypSA.

Events are the foundation of the system.

> Canonical event history is the source of truth.  
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## Core Principle

CrypSA is event-driven.

* the world is not the source of truth
* **canonical event history is the source of truth**
* derived canonical state is a projection of canonical event history. It is not the source of truth.

---

> Canonical event history is the source of truth.  
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

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
   The validator evaluates the event

4. **Decision**

   * accepted → proceeds to canonicalization
   * rejected → does not become canonical and does not enter canonical event history

5. **Canonicalization**

   * canonical metadata assigned
   * If accepted, an event becomes canonical and is appended to canonical event history

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
* must uniquely identify the candidate event

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
* must contain all data required for deterministic replay

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
* has been appended to canonical event history by the validator
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

Repeated submission of the same `event_id` must not result in more than one canonical event.

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

Candidate events originate from actions that cross the invariant boundary into validation.

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
* are appended to canonical event history
* canonical event history is the source of truth
* are replayed to reconstruct state

---

## One Sentence Summary

CrypSA uses validated, immutable canonical events as the source of truth, and all world state is derived by replaying those events in validator-defined canonical order.
