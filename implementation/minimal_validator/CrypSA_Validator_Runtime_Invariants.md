# Validator Runtime Invariants

## Purpose

This document defines the runtime invariants that must always hold inside **CrypSA Minimal Validator v0.1**.

These are not gameplay invariants.

They are **validator runtime correctness invariants**.

They exist to protect:

* canonical event history
* canonical ordering
* deterministic replay
* derived canonical state
* observer consistency

This is an implementation guidance document for the minimal validator.

For authoritative system behavior, refer to:

* `../../spec/`
* `../../architecture/`

---

## Core Principle

> If validator runtime invariants are broken, the CrypSA model is broken in implementation.

A validator may be small, local, or incomplete in features.

It may **not** violate the runtime invariants that protect canonical truth.

---

## Invariant 1 — Canonical Event History Is Append-Only

Accepted canonical events must only ever be:

* appended
* read
* replayed

They must never be:

* edited in place
* reordered after acceptance
* deleted during normal runtime flow

### Why This Matters

Canonical event history is the source of truth.

If accepted history can be rewritten, replay and reconstruction can no longer be trusted.

---

## Invariant 2 — Canonical Ordering Is Defined Only by `canonical_sequence`

Canonical ordering must be defined exclusively by:

* `canonical_sequence`

It must never be defined by:

* transport delivery order
* wall-clock arrival time
* observer send order
* UI timing
* local queue order alone

### Why This Matters

Transport is not truth.

Only the validator may define canonical ordering.

---

## Invariant 3 — Every Accepted Canonical Event Has Exactly One `canonical_sequence`

If an event is accepted:

* it must receive exactly one `canonical_sequence`
* that sequence must be unique
* that sequence must never later change

### Why This Matters

Canonical ordering must remain stable across:

* replay
* snapshot recovery
* reconnect flow
* observer reconciliation

---

## Invariant 4 — `canonical_sequence` Must Be Strictly Increasing

For accepted events:

```text id="strict_order"
event_n.canonical_sequence < event_n+1.canonical_sequence
```

No duplicates.
No reuse.
No backward movement.

### Why This Matters

Deterministic replay depends on a single monotonic canonical order.

---

## Invariant 5 — Candidate Events Must Never Directly Mutate Canonical Truth

Candidate events may be:

* parsed
* normalized
* validated
* accepted or rejected

They must never directly:

* modify canonical event history
* modify canonical ordering
* define truth before acceptance

### Why This Matters

Truth begins only after validation succeeds.

Before that, an event is only a proposal.

---

## Invariant 6 — All Canonical Changes Must Cross the Invariant Boundary

Every canonical change must originate from:

* a candidate event
* crossing the invariant boundary
* validator-side validation

There must be no hidden path that allows:

* direct canonical mutation
* bypassed validation
* internal shortcuts that alter truth

### Why This Matters

If canonical changes can happen outside the invariant boundary, CrypSA is no longer being implemented correctly.

---

## Invariant 7 — Validation Must Be Deterministic for the Same Input and Canonical Context

Given:

* the same candidate event
* the same canonical context

Validation must produce:

* the same accept/reject result
* the same rejection reason category
* the same canonicalization outcome if accepted

### Why This Matters

Non-deterministic validation destroys trust in replay, debugging, and correctness.

---

## Invariant 8 — Rejected Events Must Not Affect Canonical Event History

If validation rejects an event:

* no canonical event is created
* no canonical_sequence is assigned
* canonical event history remains unchanged

### Why This Matters

Rejection must be a true non-canonical outcome.

---

## Invariant 9 — Duplicate `event_id` Must Not Produce Multiple Canonical Events

If the validator receives the same candidate `event_id` more than once:

* it must not canonicalize it multiple times
* it must not assign multiple canonical_sequence values
* it must return or map to the original outcome

### Why This Matters

Idempotency is required for correctness under retries, reconnects, and duplicate delivery.

---

## Invariant 10 — Derived Canonical State Must Be Reconstructable from Canonical Event History

Derived canonical state must always be:

* producible from canonical event history
* consistent with replay
* non-authoritative

It must never become:

* an independent source of truth
* dependent on hidden mutations
* reliant on missing canonical events

### Why This Matters

If derived state cannot be rebuilt from history, then truth has leaked into mutable runtime structures.

---

## Invariant 11 — Applying Canonical Events Must Be Deterministic

Given:

* the same starting derived canonical state
* the same canonical event

`apply_event` must always produce:

* the same resulting derived canonical state

### Why This Matters

Replay correctness depends on deterministic event application.

---

## Invariant 12 — Full Replay and Incremental Application Must Agree

These two paths must agree:

1. full replay from canonical event history
2. incremental state updates during normal runtime

They must converge to the same derived canonical state.

### Why This Matters

If runtime application and replay differ, reconnect, snapshot restore, and debugging will drift.

---

## Invariant 13 — Snapshots Must Never Become a Source of Truth

Snapshots may be used to:

* speed up reconstruction
* support reconnect
* reduce replay cost

Snapshots must not:

* override canonical event history
* replace canonical truth
* justify skipping missing canonical events

### Why This Matters

Snapshots are optimization artifacts, not truth artifacts.

---

## Invariant 14 — Snapshot + Tail Replay Must Equal Full Replay

If a snapshot exists at canonical sequence `N`, then:

```text id="snapshot_tail"
snapshot_at_N + replay(events_after_N) == full_replay(all_events)
```

### Why This Matters

This is the core correctness guarantee for reconnect and practical runtime recovery.

---

## Invariant 15 — Conflict Resolution Must Operate on a Consistent Canonical Context

For any conflict scope:

* validation must evaluate against a consistent canonical context
* conflicting events must not both succeed if they cannot both be true
* acceptance must remain atomic within the scope

### Why This Matters

Without this, concurrent submissions can produce contradictory canonical outcomes.

---

## Invariant 16 — Transport Must Not Define Truth

Transport may:

* deliver messages
* duplicate messages
* delay messages
* reorder messages

Transport must never:

* define canonical ordering
* decide truth
* validate events
* mutate canonical event history

### Why This Matters

Truth belongs to the validator, not to delivery mechanics.

---

## Invariant 17 — Observer Sessions Must Not Influence Canonical Truth

Observer-specific runtime state may track:

* connection status
* last acknowledged canonical_sequence
* reconnect needs
* subscription or delivery state

These must never affect:

* event validity
* canonical ordering
* canonical history contents

### Why This Matters

Session coordination is delivery logic, not truth logic.

---

## Invariant 18 — Reconnect Must Restore Canonical Consistency

After reconnect:

* observer state may be stale
* canonical truth must not be stale

Reconnect flow must restore the observer to a state consistent with:

* canonical event history
* canonical ordering
* replay or snapshot + tail replay

### Why This Matters

Reconnect is not successful unless observer consistency is restored.

---

## Invariant 19 — Local and Remote Validator Modes Must Preserve the Same Truth Model

If the validator runs:

* locally
* in separate local process
* remotely over network

The following must remain unchanged:

* invariant boundary behavior
* validation behavior
* canonical ordering model
* canonical event history semantics
* replay semantics

### Why This Matters

Deployment may change.
Truth model may not.

---

## Invariant 20 — The Validator Must Not Simulate the Observer Experience

The validator may:

* validate candidate events
* append canonical events
* update derived canonical state
* coordinate canonical updates

The validator must not:

* run UI logic
* predict for the observer
* own presentation behavior
* define player experience

### Why This Matters

The validator protects truth, not experience.

---

## Runtime Invariant Checklist

At minimum, the validator runtime must always preserve:

* append-only canonical history
* exclusive canonical ordering via `canonical_sequence`
* explicit invariant boundary
* deterministic validation
* deterministic replay
* deterministic event application
* idempotent event handling
* replay-reconstructable derived state
* snapshot correctness
* conflict-scope atomicity
* transport separation from truth

If any of these fail, the implementation is drifting from CrypSA.

---

## How to Use This Document

Use this document when:

* designing validator modules
* reviewing implementation changes
* writing tests
* debugging replay mismatches
* evaluating whether a shortcut violates architecture

This is a runtime correctness guardrail.

---

## One Sentence Summary

A CrypSA validator runtime must preserve append-only canonical history, exclusive canonical ordering, deterministic validation and replay, idempotent event handling, and strict separation between truth, transport, and observer experience.
