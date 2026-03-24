# CrypSA Quick Start for Engineers

> Scope note: This document is an implementation-oriented starting point.
>
> For authoritative runtime behavior, refer to `../spec/`.
>
> Intended audience: engineers who understand the core CrypSA idea and want to build a minimal working system.

---

## Purpose

This document provides a concise guide for building a minimal CrypSA-based system.

It is not a full introduction to CrypSA.

It focuses on:

* the smallest viable runtime loop
* the minimum required components
* how to go from concept → working system

---

## Minimal CrypSA System

A minimal CrypSA implementation requires only:

* identity and object definitions
* canonical event history
* derived canonical state cache
* validation pipeline
* observer clients

Each part exists to protect canonical event history while allowing local simulation.

---

## Step 1 — Define Identity and Object Structure

Every canonical object must have:

* a unique identity
* a structural definition (genome)
* a valid event history

Example:

```text
Object Identity: sword_1001
Genome: sword_type_A
````

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
server_sequence
event_type
actor_id
target_ids
payload
accepted_at
```

The system should:

* append events in order
* avoid mutating history
* keep events inspectable

Avoid:

* treating world state as primary storage

---

## Step 4 — Maintain Derived Canonical State

The server maintains a derived canonical state cache for:

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

It is updated by applying accepted events.

---

## Step 5 — Build the Observer

Observers reconstruct the world locally using:

* identity
* genome
* canonical event history
* snapshot or derived state

Observers:

* simulate locally
* present the world
* gather user input
* track pending candidate events

---

## Step 6 — Implement the Invariant Boundary

Every interaction must answer:

> Does this affect canonical event history?

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
* `client_time` is informational only
* ordering is determined by the server

---

## Step 8 — Validate on the Server

The server evaluates candidate events through a validation pipeline.

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

* assign canonical metadata (including `server_sequence`)
* append to canonical event history
* update derived canonical state
* notify observers

Example:

```python
def accept_event(event):
    canonical_event = assign_canonical_metadata(event)  # assigns server_sequence
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

> all observers converge on the same shared state derived from canonical event history

---

## Minimal CrypSA Loop

```text
Reconstruct world
→ Simulate locally
→ Interaction occurs
→ Invariant boundary check
→ Candidate event submission
→ Server validation
→ Assign server_sequence
→ Canonical event history updated
→ Derived canonical state updated
→ Observer reconciliation
```

---

## Server Responsibility (Important)

The server:

* validates candidate events
* enforces invariants
* maintains canonical event history

The server does **not**:

* simulate the world
* predict outcomes
* control user experience

> The server controls truth, not simulation

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

A minimal CrypSA system requires:

* identity and structural definitions
* canonical event history
* derived canonical state
* observer reconstruction
* invariant boundary checks
* server-side validation

With these, a persistent event-driven universe can be built.

---

## One Sentence Summary

A minimal CrypSA system allows observers to simulate locally while a server validates candidate events, records accepted events as canonical event history, and distributes that shared history back to all observers.
