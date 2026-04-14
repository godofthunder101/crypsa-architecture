# CrypSA Conflict Resolution

## Purpose

This diagram shows how CrypSA resolves conflicting candidate events that target the same **conflict scope**.

Examples of conflict scope include:

* the same tile
* the same object
* the same inventory slot
* the same ownership target

In CrypSA v0.1:

> the first valid event within the conflict scope is accepted

For the authoritative conceptual flow of the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Diagram

> This diagram illustrates conflict resolution within the CrypSA runtime model.
> It does not define runtime behavior or event flow.
> For the authoritative conceptual flow, see:
> → ../architecture/CrypSA_Runtime_Model.md

```mermaid
flowchart TD

A[Observer A submits candidate event] --> C[Validator evaluates conflict scope]
B[Observer B submits candidate event] --> C

C --> D[Evaluate against canonical event history]

D --> E[Validate candidate event]

E -->|Valid and first| G[Accept event]
E -->|Invalid| R1[Reject event]

G --> H[Assign canonical_sequence]
H --> I[Append to canonical event history]
I --> J[Observers receive canonical update]

J --> K[Observers reconcile]

R1 --> L[Return rejection result]
L --> K
````

---

## How to Read This

### 1. Conflicting Actions Arrive

Multiple observers submit actions affecting the same conflict scope.

Examples:

* placing on the same tile
* claiming the same object
* consuming a unique resource

---

### 2. Evaluation Uses Canonical Event History

The validator evaluates events against canonical event history at the moment of validation.

This ensures:

* no two conflicting events are accepted for the same scope
* validation is based on a stable and ordered history defined by `canonical_sequence`

---

### 3. One Event Is Accepted

In v0.1:

* the first valid event within the scope is accepted
* acceptance is determined by validation order recorded via `canonical_sequence`
* later conflicting events are rejected

---

### 4. Rejection Has a Defined Cause

Rejected events may fail because:

* the conflict was already resolved
* preconditions are no longer valid
* canonical event history changed before validation

Typical results include:

* `conflict_lost` (another event already resolved the conflict scope)
* `precondition_failed`

---

### 5. Observers Reconcile

After the canonical event is accepted:

* observers receive the update
* local predictions are confirmed or corrected
* all observers converge to derived canonical state

---

## Key Insight

> Conflict resolution is determined by validation against canonical event history, not by local simulation.

And:

> the validator defines which event becomes canonical within a conflict scope

---

## Relationship to Specs

This diagram maps to:

* `spec/CrypSA_Runtime_Spec_v0.1.md`
* `spec/CrypSA_Validation_Model.md`
* `spec/CrypSA_Consistency_Model.md`

---

## One Sentence Summary

When multiple observers submit conflicting actions, the validator evaluates them against canonical event history, assigns ordering via `canonical_sequence`, accepts one valid event within the conflict scope, rejects the others, and observers reconcile to the resulting derived canonical state.
