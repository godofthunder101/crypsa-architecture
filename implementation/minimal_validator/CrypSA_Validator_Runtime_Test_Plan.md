# Validator Runtime Test Plan

## Purpose

This document defines the test strategy for **CrypSA Minimal Validator v0.1**.

It ensures the validator implementation:

* preserves canonical truth
* enforces runtime invariants
* remains deterministic
* behaves correctly under real runtime conditions

This is not a generic test plan.

It is a **runtime correctness test plan**, directly derived from:

* Validator_Runtime_Invariants.md
* CrypSA runtime model

---

## Core Principle

> Tests must protect the architecture, not just the behavior.

A validator that "works" but violates invariants is incorrect.

---

## Test Categories

The validator must be tested across the following categories:

1. Validation correctness
2. Canonical event history correctness
3. Canonical ordering correctness
4. Idempotency
5. Derived state correctness
6. Replay correctness
7. Snapshot correctness
8. Conflict resolution
9. Transport independence
10. Reconnect behavior

---

## 1. Validation Tests

### Goal

Ensure only valid events become canonical.

---

### Test: Valid Event Is Accepted

```text
Given valid candidate event
When submitted
Then result = accepted
And canonical event is created
```

---

### Test: Invalid Event Is Rejected

```text
Given invalid candidate event
When submitted
Then result = rejected
And no canonical event is created
```

---

### Test: Rejection Does Not Change History

```text
Given canonical history length = N
When invalid event is submitted
Then canonical history length remains N
```

---

## 2. Canonical Event History Tests

### Goal

Ensure canonical history is append-only and stable.

---

### Test: Append-Only Behavior

```text
Submit event A → accepted
Submit event B → accepted

Expect:
history = [A, B]
```

---

### Test: No Mutation of Past Events

```text
Submit event A
Capture event A

Submit event B

Assert event A remains unchanged
```

---

## 3. Canonical Ordering Tests

### Goal

Ensure canonical_sequence defines ordering.

---

### Test: Sequential Ordering

```text
Submit event A
Submit event B

Expect:
A.sequence < B.sequence
```

---

### Test: No Duplicate Sequences

```text
Submit multiple events

Ensure:
all canonical_sequence values are unique
```

---

### Test: Strict Monotonic Increase

```text
Submit N events

Ensure:
sequence[i] < sequence[i+1] for all i
```

---

## 4. Idempotency Tests

### Goal

Ensure duplicate event_ids do not create duplicate canonical events.

---

### Test: Duplicate Event Submission

```text
Submit event X
Submit event X again

Expect:
only one canonical event exists
result is identical both times
```

---

### Test: Duplicate Does Not Advance Sequence

```text
Submit event X → accepted (sequence 1)
Submit event X again

Expect:
no new sequence assigned
```

---

## 5. Derived State Tests

### Goal

Ensure derived state is correct and non-authoritative.

---

### Test: Event Updates Derived State

```text
Submit event create_object(id=A)

Expect:
derivedState.objects[A] exists
```

---

### Test: Derived State Matches History

```text
Apply events A, B, C

Rebuild state from history

Expect:
rebuilt state == runtime state
```

---

## 6. Replay Tests

### Goal

Ensure deterministic reconstruction.

---

### Test: Full Replay Matches Runtime

```text
Run events A, B, C

Capture runtime state

Replay from empty history

Expect:
replay state == runtime state
```

---

### Test: Replay Determinism

```text
Replay same history twice

Expect:
identical state outputs
```

---

## 7. Snapshot Tests

### Goal

Ensure snapshot correctness.

---

### Test: Snapshot + Tail Equals Full Replay

```text
Create snapshot at sequence N

Apply events N+1, N+2

Reconstruct:
snapshot + tail

Expect:
equals full replay
```

---

### Test: Snapshot Does Not Replace History

```text
Create snapshot

Ensure:
canonical history still exists and is used
```

---

## 8. Conflict Resolution Tests

### Goal

Ensure only one event wins within a conflict scope.

---

### Test: Competing Events

```text
Event A targets tile_1
Event B targets tile_1

Submit both

Expect:
one accepted
one rejected
```

---

### Test: Conflict Does Not Produce Duplicate State

```text
Submit conflicting events

Ensure:
only one canonical state change occurs
```

---

## 9. Transport Independence Tests

### Goal

Ensure ordering is not dependent on delivery.

---

### Test: Out-of-Order Submission

```text
Submit events in reverse order

Expect:
canonical_sequence still defines correct order
```

---

### Test: Duplicate Delivery

```text
Deliver same event multiple times

Expect:
idempotent behavior
```

---

## 10. Reconnect Tests

### Goal

Ensure observer can recover canonical state.

---

### Test: Reconnect With Full Replay

```text
Disconnect observer

Reconnect

Replay history

Expect:
correct state
```

---

### Test: Reconnect With Snapshot

```text
Load snapshot
Apply tail events

Expect:
correct state
```

---

## Failure Injection Tests (Important)

These simulate real-world conditions.

---

### Test: Duplicate Messages

* send same event multiple times
* expect idempotency

---

### Test: Delayed Events

* simulate late arrival
* ensure ordering still correct

---

### Test: Partial Delivery

* drop some messages
* reconnect and recover

---

## Minimal Test Suite Order

Implement tests in this order:

```text
1. validation tests
2. canonical history tests
3. ordering tests
4. idempotency tests
5. derived state tests
6. replay tests
7. conflict tests
8. snapshot tests
9. reconnect tests
```

---

## Testing Strategy

Start with:

* in-process tests
* no network
* deterministic inputs

Then expand to:

* simulated transport
* delayed events
* reconnect scenarios

---

## What This Protects

This test plan ensures:

* canonical truth is preserved
* replay is correct
* ordering is stable
* duplicates are safe
* conflicts are resolved
* reconnect works

---

## Key Insight

> A CrypSA validator is correct only if replay, ordering, and validation remain stable under all conditions.

---

## Summary

This test plan translates CrypSA runtime invariants into concrete test cases that ensure correctness of validation, canonical history, ordering, replay, snapshots, and observer recovery.

---

## One Sentence Summary

The Validator Runtime Test Plan ensures that canonical event history, validation, ordering, replay, and reconciliation all behave deterministically and correctly under real runtime conditions.
