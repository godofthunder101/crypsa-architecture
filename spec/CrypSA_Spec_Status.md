# CrypSA Spec Status

This document describes the maturity of each specification in the `spec/` folder.

---

## Status Levels

### Draft

Conceptual and may change significantly.

Not yet aligned with the full system.

---

### Defined

Structurally complete and internally consistent.

* aligned with other spec documents
* terminology is stable
* behavior is clearly described

---

### Testable

Can be implemented and verified against expected runtime behavior.

* suitable for prototype implementation
* behavior can be validated in a running system
* used to guide real system development

---

### Stable

Considered reliable for production use.

* unlikely to change significantly
* suitable as a long-term system contract

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
* **Draft** → still evolving

---

## Relationship to Authority

All documents in `spec/` are authoritative for runtime behavior.

Status reflects maturity, not authority.

---

## Current Focus

CrypSA is currently in the transition from:

> Defined → Testable

This phase involves:

* building the Minimal Server v0.1
* validating runtime behavior
* testing observer/server interaction
* confirming replay and consistency guarantees

---

## Goal

Move all specs through:

> Defined → Testable → Stable

by:

* validating behavior through implementation
* refining unclear areas
* eliminating ambiguity

---

## One Sentence Summary

CrypSA v0.1 specifications are structurally complete and moving toward full runtime validation through implementation.
