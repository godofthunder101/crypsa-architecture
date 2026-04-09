# CrypSA Quick Start for Engineers

> Intended audience: engineers who understand the core CrypSA idea and want to build a minimal working system.

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This document provides example implementation approaches for CrypSA.

👉 These patterns are not required, but are recommended to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Implementation details may vary based on product requirements.

This document illustrates one possible way to structure a system that conforms to CrypSA.

---

## Purpose

This document provides a concise guide for building a minimal CrypSA-based system.

It is not a full introduction to CrypSA.

It focuses on:

* the smallest viable runtime loop
* the core components of a minimal CrypSA system
* how to go from concept → working system

---

## Minimal CrypSA System

A minimal CrypSA implementation can be built with:

* identity and object definitions
* canonical event history
* derived canonical state
* validation pipeline
* observer clients

Each part exists to protect canonical event history while allowing local simulation.

---

## Step 1 — Define Identity and Object Structure (Example Approach)

Every canonical object must have:

* a unique identity
* a structural definition (genome)
* a canonical event history (which may initially be empty)

Example:

```text
Object Identity: sword_1001
Genome: sword_type_A
```

The Mint (or equivalent system) defines:

* valid identities
* valid structural definitions

The key requirement:

> objects must be reconstructable from canonical inputs

---

## Step 2 — Define Minimal Event Types

Start with a very small set of events.

Recommended initial set:

* `mint_object`
* `place_structure`
* `destroy_structure`

Optional next step:

* `transfer_object`

These are enough to prove:

* validation
* conflict handling
* reconstruction

---

## Step 3 — Store Canonical Event History

Canonical event history is the source of truth.

Example structure:

```text
CanonicalEvent
--------------
canonical_event_id
canonical_sequence
event_type
actor_id
target_ids
payload
accepted_at
```

The system should:

* append events in order
* maintain strict ordering via canonical_sequence
* avoid mutating history
* keep events inspectable

Avoid:

* treating world state as primary storage

---

## Step 4 — Maintain Derived Canonical State

The validator maintains a derived canonical state (typically cached) for:

* validation
* querying
* efficient lookup

Examples:

* tile occupancy
* ownership
* object lifecycle state
* resource counts

Important:

> derived canonical state is a computed view, not the source of truth

It is updated by applying accepted events in canonical_sequence order.

---

## Step 5 — Build the Observer

Observers reconstruct the world locally using:

* identity
* genome
* canonical event history
* snapshot + canonical event history replay (ordered via canonical_sequence)

Observers:

* simulate locally
* present the world
* gather user input
* track pending candidate events

---

## Step 6 — Implement the Invariant Boundary

Every interaction must answer:

> Does this affect canonical event history?

All canonical changes must pass through the invariant boundary.

Example:

```python
if affects_canonical_event_history(interaction):
    create_candidate_event(interaction)
else:
    process_locally(interaction)
```

Most interactions remain local.

Only meaningful changes become candidate events.

---

## Step 7 — Submit Candidate Events

When canonical event history is affected, the observer submits a candidate event.

Example structure:

```text
CandidateEvent
--------------
event_id
event_type
actor_id
target_ids
payload
precondition_refs
client_time
```

Notes:

* `event_id` must be unique (used for idempotency)
* duplicate event_ids must not produce multiple canonical events
* `client_time` is informational only
* ordering is determined by canonical_sequence assigned by the validator

---

## Step 8 — Validate on the Server

The validator evaluates candidate events through a validation pipeline.

Validation must be deterministic for the same input and canonical context.

Typical stages:

* schema validation
* identity validation
* precondition validation
* invariant validation
* event-specific rule validation

Example:

```python
def validate_event(event):
    if not schema_valid(event):
        return reject("invalid_schema")

    if not identities_valid(event):
        return reject("invalid_identity")

    if not preconditions_hold(event):
        return reject("precondition_failed")

    if violates_invariants(event):
        return reject("invariant_violation")

    if not event_rules_valid(event):
        return reject("rule_violation")

    return accept()
```

---

## Step 9 — Append Accepted Events

If validation succeeds:

* assign canonical metadata (including `canonical_sequence`)
* append to canonical event history
* update derived canonical state
* notify observers

Example:

```python
def accept_event(event):
    canonical_event = assign_canonical_metadata(event)  # assigns canonical_sequence
    append_to_event_history(canonical_event)
    apply_to_derived_state(canonical_event)
    notify_observers(canonical_event)
```

---

## Step 10 — Reconcile Observers

Observers receive canonical updates and reconcile their local simulation.

This may involve:

* confirming predictions
* correcting divergence
* rebuilding objects
* updating UI

Because reconstruction is deterministic:

> all observers converge on the same derived canonical state reconstructed from canonical event history

---

## Minimal CrypSA Loop

```text
Reconstruct world
→ Simulate locally
→ Interaction occurs
→ Invariant boundary check
→ Candidate event submission
→ Validator validation
→ Assign canonical_sequence
→ Canonical event history updated
→ Derived canonical state updated
→ Observer reconciliation
```

---

## Validator Responsibility (Important)

The validator:

* validates candidate events
* enforces invariants
* maintains canonical event history

The validator does **not**:

* simulate the world
* predict outcomes
* control user experience

> The validator controls truth, not simulation

---

## What This Minimal System Omits

This quick start intentionally excludes:

* large-scale performance concerns
* anti-cheat systems
* distributed shards
* branch merging
* advanced validation strategies
* complex lens systems
* full persistence strategies

These are added later.

---

## Recommended First Demo

### Structure Placement

Why:

* simple
* visible
* conflict-prone
* easy to validate

---

### Object Transfer (Optional Next Step)

Why:

* demonstrates ownership rules
* demonstrates rejection cases
* tests invariant enforcement

---

## Summary

A minimal CrypSA system typically includes:

* identity and structural definitions
* canonical event history
* derived canonical state
* observer reconstruction
* invariant boundary checks
* validator-side validation

With these, a persistent event-driven universe can be built.

---

## One Sentence Summary

A minimal CrypSA system allows observers to simulate locally while a validator validates candidate events, records accepted events as canonical event history ordered via canonical_sequence, and distributes that shared history back to all observers.
