# CrypSA Spec Status

This document describes the maturity of each specification in the `spec/` folder.

---

## Status Levels

### Draft

Conceptual and may change significantly.

* not fully aligned with the overall system
* terminology or behavior may still evolve
* not ready for reliable implementation

---

### Defined

Structurally complete and internally consistent.

* aligned with other spec documents
* terminology is stable
* behavior is clearly described
* minimal ambiguity

---

### Testable

Can be implemented and verified against expected runtime behavior.

* suitable for prototype implementation
* behavior can be validated in a running system
* used to guide real system development
* edge cases are reasonably defined

---

### Stable

Considered reliable for production use.

* unlikely to change significantly
* suitable as a long-term system contract
* validated through implementation and testing
* edge cases and failure modes are well understood

---

## Current Spec Status (v0.1)

| Spec              | Status   |
| ----------------- | -------- |
| Runtime Spec      | Testable |
| Event Model       | Defined  |
| Validation Model  | Defined  |
| Consistency Model | Defined  |
| Replay Model      | Defined  |
| Snapshot Model    | Defined  |
| Identity Model    | Defined  |
| Transport Model   | Draft    |

---

## Interpretation

* **Defined** → structurally complete and aligned
* **Testable** → ready to implement and validate
* **Draft** → still evolving and not yet implementation-ready

---

## Relationship to Authority

All documents in `spec/` are authoritative for runtime behavior.

Status reflects **maturity**, not authority.

> A Draft spec is still authoritative within its scope, but may change.

---

## Current Focus

CrypSA is currently transitioning from:

> Defined → Testable

This phase involves:

* building the Minimal Validator v0.1
* validating runtime behavior
* testing observer ↔ validator interaction
* confirming replay and consistency guarantees

---

## Progression Model

Specifications are expected to move through:

```text
Draft → Defined → Testable → Stable
```

Progression is achieved by:

* refining definitions
* removing ambiguity
* validating behavior through implementation
* testing under real runtime conditions

---

## Goal

Move all specs toward:

> Stable

by:

* validating behavior through implementation
* refining unclear areas
* eliminating ambiguity
* confirming correctness under real conditions

---

## One Sentence Summary

CrypSA v0.1 specifications are structurally complete and transitioning toward full runtime validation through implementation of a minimal validator system.
