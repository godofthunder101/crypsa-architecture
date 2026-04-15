# CrypSA Validator Runtime Flow

## Purpose

This document describes the runtime execution flow.

It shows how a candidate event moves through the system:

> submission → validation → canonicalization → distribution

This is an implementation-oriented document that connects:

* event intake
* invariant boundary
* validation pipeline
* canonical event history
* derived canonical state
* observer updates

---

## Core Principle

> The validator is the only authority that may modify canonical event history.

In CrypSA, canonical changes follow this pattern:

* originate from a candidate event
* cross the invariant boundary
* pass validation
* be assigned canonical ordering
* be appended to canonical event history

---

## High-Level Flow

```text
Candidate Event Submitted
→ Event Intake
→ Idempotency Check
→ Invariant Boundary (enter validator)
→ Validation Pipeline
→ Accepted?
    ├── No → Rejection Result → Observer Correction
    └── Yes
         → Assign canonical_sequence
         → Append to canonical event history
         → Apply to Derived Canonical State
         → Broadcast Canonical Event
         → Observers Reconcile
```

---

## Step-by-Step Runtime Flow

---

### 1. Candidate Event Submission

An observer submits a candidate event.

Input includes:

* event_id
* event_type
* actor_id
* target_ids
* payload
* precondition_refs

At this point:

> the event is not canonical and does not affect shared reality

---

### 2. Event Intake

The validator receives the event.

Responsibilities:

* parse message
* validate basic structure (non-authoritative)
* normalize data

This stage prepares the event for validation.

It must not:

* enforce invariants
* modify canonical state

---

### 3. Idempotency Check

The validator checks:

> has this event_id already been processed?

---

#### If duplicate:

* return previous result
* do not reprocess
* do not create a new canonical event

---

#### If new:

* continue to validation

---

## 4. Invariant Boundary

At this point, the event crosses the invariant boundary.

From here onward:

> the validator determines whether the event becomes canonical truth

No component outside this boundary may:

* modify canonical event history
* assign canonical ordering

---

## 5. Validation Pipeline

The validator evaluates the event in ordered stages:

```text
Schema → Identity → Preconditions → Invariants → Rules
```

---

### Validation Requirements

Validation should be:

* deterministic
* based on canonical context
* free of side effects

---

### Outcome

---

#### ❌ Rejected

If any stage fails:

* produce rejection result
* do not modify canonical event history
* return reason

---

#### ✅ Accepted

If all stages pass:

* proceed to canonicalization

---

## 6. Assign Canonical Ordering

The validator assigns:

```text
canonical_sequence
```

This:

* defines authoritative ordering
* establishes global event sequence
* enables deterministic replay

---

## 7. Canonicalization

The accepted event becomes a canonical event.

Steps:

* attach canonical metadata
* assign canonical_event_id
* record accepted_at timestamp

---

## 8. Append to Canonical Event History

The canonical event is appended to the canonical event history.

Expected characteristics:

* append-only
* strictly ordered by canonical_sequence
* never mutated after insertion

---

## 9. Apply to Derived Canonical State

The validator applies the canonical event:

```text
derived_state = apply_event(derived_state, canonical_event)
```

Requirements:

* deterministic
* consistent with replay
* reconstructable from canonical history

---

## 10. Broadcast Canonical Event

The validator sends the canonical event to observers.

Responsibilities:

* notify all relevant observers
* include canonical_sequence
* ensure observers can reconcile

Transport concerns (ordering, retries) are separate from truth.

---

## 11. Observer Reconciliation

Observers receive the canonical event and:

* compare with local prediction
* confirm or correct local state
* update derived canonical state

Result:

> all observers converge toward the same canonical state

---

## Rejection Flow

If validation fails:

```text
Validation Failed
→ Rejection Result
→ Observer Correction
```

Observers must:

* discard invalid prediction
* restore canonical consistency

---

## Idempotency Guarantee

The validator is expected to ensure:

> the same event_id never produces multiple canonical events

This prevents:

* duplicate state changes
* replay inconsistencies
* divergence between observers

---

## Determinism Guarantee

The system is expected to ensure:

```text
same canonical event history → same derived canonical state
```

This applies to:

* validation decisions
* event application
* replay

---

## Atomicity Guarantee

Within a conflict scope:

* only one event may succeed
* validation must operate on a consistent canonical context

This ensures:

* no race conditions
* no conflicting canonical states

---

## Runtime Responsibilities Summary

The validator runtime is responsible for:

* enforcing the invariant boundary
* validating candidate events
* assigning canonical ordering
* maintaining canonical event history
* updating derived canonical state
* broadcasting canonical updates

It must not:

* simulate the world
* predict outcomes
* manage UI or experience

---

## Key Insight

> The validator does not simulate the world — it decides what becomes real.

Everything else:

* derives from canonical event history
* exists outside the truth boundary

---

## One Sentence Summary

A CrypSA validator processes candidate events by enforcing the invariant boundary, validating them deterministically, assigning canonical_sequence, recording accepted events in canonical event history, updating derived state, and broadcasting results so all observers converge on shared reality.
