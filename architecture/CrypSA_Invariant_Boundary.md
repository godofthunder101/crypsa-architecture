# CrypSA — Invariant Boundary

This document defines the **invariant boundary** in CrypSA.

It formalizes the point at which:

* observer-proposed events
* are evaluated against canonical truth
* and either accepted or rejected

This is the **only place where canonical truth may change**.

---

## Authority Level

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Purpose

The invariant boundary exists to:

* protect canonical truth
* enforce system correctness
* separate observer simulation from authoritative validation

All changes to canonical event history must pass through this boundary.

---

## Defines

- The **invariant boundary** as the structural interface between observer-proposed events and validator authority
- The rules, inputs, outputs, and guarantees of boundary validation
- The authority constraint that only the validator may change canonical event history

---

## Does Not Define

- Authoritative runtime behavior (defined in `/spec`)
- Implementation strategies for the validator or boundary
- Observer-side simulation behavior beyond event proposal

---

## Related Documents

- `spec/CrypSA_Validation_Model.md` — authoritative runtime validation behavior
- `architecture/CrypSA_Observer_Model.md` — observer responsibilities and state model
- `architecture/CrypSA_Invariants_and_Design_Space.md` — CrypSA invariants and design space

---

## Core Definition

The **invariant boundary** is the control and validation interface between:

* **observers** (which propose candidate events)
  and
* the **validator** (which determines canonical truth)

> The invariant boundary is the only entry point through which canonical event history may change.

It defines:

* how inputs are evaluated  
* how validation is performed  
* what outputs are produced  
* how canonical events are created or rejected  

---

## Boundary Rules

1. Observers may **propose**, but never define truth
2. The validator is the **only authority** over canonical event history
3. No system component may bypass the invariant boundary
4. All canonical events must originate from successful validation

---

## Guarantees

The invariant boundary guarantees:

* **No observer authority leakage**  
  Observers cannot directly affect canonical event history.

* **Deterministic canonicalization**  
  Given the same candidate event and canonical context, the validator produces the same result.

* **Atomic validation within conflict scope**  
  Each candidate event is evaluated as a single unit of validation and either fully accepted or rejected.

---

## Input

The invariant boundary receives:

### Candidate Event

A candidate event represents an attempted change to the system.

It must include:

* event type
* required data payload
* referenced identities (if applicable)
* any required metadata

The exact structure is defined in:

→ `spec/`

---

### Canonical Context

Validation requires access to canonical truth.

This may include:

* current derived canonical state
* canonical event history (directly or via derived canonical state)
* identity and ownership information

This context is used to evaluate invariants and rules.

---

## Validation Process

At the invariant boundary, the validator performs:

* schema validation
* identity validation
* precondition checks
* invariant enforcement
* rule evaluation

These stages may be structured differently depending on the implementation,
but must produce consistent results for the same input and context.

The validator must produce the same outcome given the same input and canonical context.

---

## Output

The invariant boundary produces exactly one of the following outcomes:

---

### Accepted Event

If validation succeeds:

* the event becomes **canonical**
* it is appended to canonical event history
* it is assigned a **`canonical_sequence`**
* it becomes immutable

#### Result

```text
Accepted(candidate_event) → canonical_event
```

---

### Rejected Event

If validation fails:

* the event is **not** added to canonical history
* a rejection result is produced

#### Result

```text
Rejected(candidate_event) → rejection_result
```

The rejection result should include:

* reason for rejection
* any relevant validation details

---

## Canonical Sequence

Accepted events are assigned a **`canonical_sequence`**.

This sequence:

* defines ordering
* enables deterministic replay
* establishes a single authoritative timeline

`canonical_sequence` is assigned **only by the validator**.

---

## Authority Constraint

The invariant boundary enforces a strict rule:

> Canonical event history may only be modified by the validator through successful validation.

No observer, adapter, lens, or UI component may:

* insert canonical events
* modify canonical events
* reorder canonical events

---

## Relationship to Observers

Observers:

* simulate locally
* generate candidate events
* submit events across the invariant boundary

Observers may:

* temporarily diverge from canonical truth
* predict outcomes locally

However:

* canonical truth is defined only after validation

---

## Relationship to Replay

Replay operates **after** the invariant boundary.

It:

* consumes canonical event history
* produces derived canonical state

Replay does not:

* validate events
* modify canonical history

---

## Relationship to Deployment

The invariant boundary exists regardless of deployment.

Whether the validator runs:

* locally
* on a host
* as a dedicated remote system

The boundary:

* still exists
* still enforces the same rules

> Deployment changes location, not authority.

---

## Implementation Notes (Non-Authoritative)

The invariant boundary may be implemented in various ways, including:

* a function call (local validator)
* a message interface (remote validator)
* a service endpoint

However:

* implementation details do not change its role
* behavior must remain consistent with the spec

---

## Summary

The invariant boundary is the point where:

* candidate events are evaluated
* invariants are enforced
* canonical truth is determined

It ensures that:

* all truth is validated
* all state is derived from canonical events
* observer simulation never bypasses authority

And critically:

> The invariant boundary is the gatekeeper of truth in CrypSA.
