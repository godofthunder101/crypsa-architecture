# CrypSA Event Model Spec v0.1

This document defines the structure, behavior, and lifecycle of events in CrypSA.

Events are the foundation of the system.

For a conceptual overview of how events flow through the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

> Canonical event history is the source of truth.  
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## Core Principle

CrypSA is event-driven.

* the world is not the source of truth  
* **canonical event history is the source of truth**  
* derived canonical state is a projection of canonical event history. It is not the source of truth  

Canonical state is not stored. Only canonical event history is authoritative.

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

* If accepted, an event becomes canonical and is appended to canonical event history  
* immutable  
* assigned validator-defined canonical metadata  

---

## Event State Model

An event may exist in one of the following states:

### Candidate

* proposed by an observer  
* not yet validated  
* not canonical  

---

### Rejected

* evaluated by the validator  
* does not become canonical  
* is not appended to canonical event history  

---

### Canonical

* If accepted, an event becomes canonical and is appended to canonical event history  

---

## Event Lifecycle

This lifecycle is part of the runtime model described in:

→ ../architecture/CrypSA_Runtime_Model.md

Every event follows this lifecycle:

1. **Creation**  
   An observer creates a candidate event  

2. **Submission**  
   The candidate event is submitted to the validator  

3. **Validation**  
   The validator evaluates the candidate event using **validation rules derived from applicable invariants**  

4. **Decision**

   * If accepted, an event becomes canonical and is appended to canonical event history  
   * If rejected, the event does not become canonical and is not appended to canonical event history  

5. **Propagation**  
   Observers receive the canonical event as part of the runtime model  

6. **Replay**  
   Observers reconstruct derived canonical state via canonical event replay in `canonical_sequence` order  

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
* must contain all data required to produce equivalent derived canonical state via replay  

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
* identifies the canonical event record after acceptance

---

#### `canonical_sequence`

* authoritative ordering index
* assigned by the validator
* defines replay order

> `canonical_sequence` defines a total canonical order across canonical events.

---

#### `accepted_at`

* timestamp of acceptance (validator-defined)

---

## Canonical Event Definition

A **canonical event** is an event that has become canonical through validation.

If accepted, an event becomes canonical and is appended to canonical event history.

---

## Canonical Event Guarantees

Canonical events must satisfy:

* **immutability**
  once accepted, events cannot change

* **append-only history**
  canonical event history is never rewritten

* **deterministic replay**
  given the same canonical event history and interpretation logic, replay produces equivalent derived canonical state

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

> If accepted, an event becomes canonical and is appended to canonical event history.

Validation ensures:

* validation rules derived from applicable invariants are satisfied
* preconditions are satisfied

Rejected events:

* are not appended to canonical event history
* must not affect canonical state

---

## Invariant Boundary Relationship

Candidate events originate from actions that cross the invariant boundary into validation.

The invariant boundary defines:

* the transition from local simulation
* to canonical validation

Only events that satisfy validation rules derived from applicable invariants become canonical.

Actions that do not cross this boundary:

* remain local
* do not produce candidate events

---

## Summary

CrypSA events:

* represent all canonical changes
* are validated before acceptance
* If accepted, an event becomes canonical and is appended to canonical event history
* canonical event history is the source of truth
* are replayed to reconstruct state

---

## One Sentence Summary

CrypSA uses validated, immutable canonical events as the source of truth, and all world state is derived by replaying those events in validator-defined canonical order.
