# CrypSA Invariant Model

> Exploratory note: This document reflects conceptual exploration and early modeling.
>
> For the current CrypSA model, refer to:
>
> * `../../CrypSA_In_5_Minutes.md`
> * `../../architecture/`
> * `../../spec/`

---

## Purpose

This document describes the role of invariants in a CrypSA system.

Invariants define rules that must remain true within canonical reality as represented by canonical event history. The validator enforces these rules when validating candidate events.

This document provides a conceptual view of invariants, not a formal specification.

---

## Core Principle

An invariant is a rule that must always remain true in canonical reality.

Canonical reality is defined by canonical event history, and derived canonical state is a computed view of that history.

Examples:

* an object cannot exist in two locations simultaneously
* an item cannot be owned by multiple actors at the same time
* a structure cannot occupy an invalid location
* an upgrade cannot be applied to a non-existent item

If a proposed event would violate an invariant:

> the event is rejected

Invariants are a key part of canonical validation.

---

## Why Invariants Exist

Invariants protect the structural integrity of the universe.

Without invariants, systems could produce:

* duplicated unique objects
* impossible states
* invalid geometry
* inconsistent ownership

By enforcing invariants, CrypSA ensures canonical event history remains logically consistent.

---

## Where Invariants Are Enforced

Invariants are enforced during validator validation.

Conceptually:

```text id="m3g0f1"
Observer Action
→ Local Simulation
→ Invariant Boundary Check
→ Candidate Event
→ Validation (Invariant Enforcement)
→ Accepted Event (Canonical Event)
→ Assign canonical_sequence
→ Append to Canonical Event History
→ Observer Reconciliation
```

canonical_sequence defines the authoritative ordering of events for deterministic replay.

The invariant boundary defines the point where actions that affect canonical event history must be validated before becoming canonical.

---

## Categories of Invariants

### Identity Invariants

Ensure identity consistency.

Examples:

* identities are unique
* objects cannot duplicate
* destroyed objects cannot reappear without a canonical event

---

### Ownership Invariants

Ensure valid ownership transitions.

Examples:

* objects have a valid owner
* ownership cannot be transferred without authority
* transitions follow allowed rules

---

### Spatial Invariants

Protect world structure.

Examples:

* objects cannot overlap illegally
* placement rules are enforced
* coordinates must be valid

---

### State Transition Invariants

Ensure valid evolution of objects.

Examples:

* an object must exist before being modified
* invalid transitions are disallowed
* order of operations is preserved via canonical_sequence

---

### Resource Invariants

Ensure valid resource accounting.

Examples:

* resources cannot go negative
* costs must be paid
* balances must remain valid

---

## Relationship to the Mint

The Mint defines the structural possibilities of objects.

Invariants enforce which changes are allowed at runtime.

Example:

The Mint may define:

* valid upgrades
* durability range
* ownership model

Invariants ensure that candidate events affecting those objects follow valid rules before becoming canonical events.

---

## Observer vs Validator Responsibility

Observers may perform local checks for user experience.

Examples:

* preventing obvious invalid actions
* showing placement previews
* validating UI inputs

These checks are not authoritative.

Only the validator enforces invariants for canonical event history.

---

## Invariant Violations

When an invariant violation occurs:

1. the candidate event is rejected
2. canonical event history is unchanged
3. the observer corrects local simulation

Example:

* a structure is placed locally
* validation fails
* the structure is removed during reconciliation

---

## Deterministic Evolution

Because all accepted events satisfy invariants:

* canonical event history remains consistent
* reconstruction via replay in canonical_sequence order is reliable
* contradictions do not occur

---

## Minimal Invariant System

A minimal CrypSA system must enforce invariants for:

* identity
* existence
* state transitions
* ownership
* spatial rules

Additional invariants depend on the application.

---

## Flexibility for Developers

CrypSA defines how invariants are enforced, not which invariants must exist.

Different systems emphasize different invariant sets.

---

## Summary

Invariants define the rules that must remain true in canonical reality.

The validator enforces these rules during validation, ensuring that all accepted events preserve consistency before being recorded in canonical event history.

---

## One Sentence Summary

CrypSA invariants define the rules of canonical reality and are enforced during validation so that only events that preserve consistency are assigned canonical_sequence and become part of canonical event history.
