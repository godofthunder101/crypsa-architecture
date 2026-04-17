# CrypSA Validation Model v0.1

This document defines how CrypSA validates proposed actions before they become part of canonical event history.

Validation is the mechanism that:

* protects canonical event history
* enforces invariants through validation rules
* determines what becomes canonical

For a conceptual overview of how validation fits into the system runtime, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Core Principle

In CrypSA:

> Observers may simulate freely, but only accepted events become canonical and are appended to canonical event history.

Validation occurs at the **invariant boundary**, where proposed actions transition from local simulation to canonical event history.

---

> Canonical event history is the source of truth.  
> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## Validator Inputs

Validation operates on:

* the candidate event
* canonical event history (or context derived from it)
* validation rules derived from applicable invariants

Validation must not depend on:

* observer-local state
* non-canonical external state

---

## Validation Flow

This flow is part of the runtime model described in:

→ ../architecture/CrypSA_Runtime_Model.md

The validation pipeline follows this sequence:

1. **Observer Action**  
   Local simulation only  

2. **Candidate Creation**  
   Action becomes a candidate event  

3. **Submission**  
   Event is sent to the validator  

4. **Validation**  
   The validator evaluates the candidate event using **validation rules derived from applicable invariants**

5. **Decision**

   * If accepted, an event becomes canonical and is appended to canonical event history  
   * If rejected, the event does not become canonical and does not enter canonical event history  

6. **Observer Reconciliation**  
   Observers update local state based on canonical events as part of the runtime model  

---

## Validation Pipeline

Validation is a layered, ordered process.

---

### 1. Schema Validation

Ensures the event is well-formed.

Checks include:

* required fields present  
* valid structure  
* correct data types  

---

### 2. Identity Validation

Ensures referenced identities are valid.

Checks include:

* actor exists  
* target objects exist  
* identities are valid at event time  

---

### 3. Precondition Validation

Ensures observer assumptions are still valid.

Checks include:

* expected state matches derived canonical state  
* required resources exist  
* required conditions hold  

---

### 4. Validation Rules (Enforcement Layer)

Validation rules enforce applicable invariants.

These rules are derived from:

* architectural invariants  
* system invariants  

Examples:

* no duplicate ownership  
* valid placement  
* valid state transitions  
* upgrade paths  
* allowed interactions  
* resource costs  

---

### 5. Optional Validation Layers

These are not required for v0.1 runtime behavior.

---

#### Simulation Validation (Optional)

* verifies plausibility of proposed outcome  
* does not define canonical outcome  
* may re-simulate critical actions  

---

#### Pattern / Anomaly Validation (Optional)

* evaluates behavior over time  
* detects suspicious or invalid patterns  
* does not directly determine canonical acceptance  

---

## Acceptance Criteria

A candidate event is accepted only if:

* it passes all validation layers  
* all validation rules derived from applicable invariants are satisfied  
* all preconditions hold  

If any validation step fails:

* the event is rejected  
* the event does not become canonical  

---

## Validation Requirements

Validation must be:

* atomic within the relevant conflict scope  
* based on canonical event history and derived canonical state  

Validation must be deterministic.

Given the same:

* candidate event  
* canonical event history (or equivalent derived context)  
* validation rules  

the validator must produce the same result.

---

## Validation Outcomes

Each candidate results in:

---

### Accepted

If accepted, an event becomes canonical and is appended to canonical event history.

* assigned `canonical_sequence`  

---

### Rejected

* the event does not become canonical  
* the event does not enter canonical event history  

Optional:

* rejection reason returned  
* rejection logged  

---

## Rejection Codes (Recommended)

* `invalid_schema`  
* `invalid_identity`  
* `precondition_failed`  
* `invariant_violation`  
* `rule_violation`  
* `conflict_lost`  

---

## Invariant and Validation Rule Design

Invariants define:

* what must always be true  
* what cannot be violated  

Validation rules:

* enforce those invariants at runtime  

Examples:

* an object has one location  
* ownership is unique  
* transitions follow valid paths  

Strong design ensures:

* consistency  
* correctness  
* security  

---

## Validation Scope

Only actions that affect canonical event history are validated.

Examples:

| Action Type      | Validation      |
| ---------------- | --------------- |
| Local simulation | Not validated   |
| UI interaction   | Not validated   |
| Candidate events | Fully validated |

---

## Performance Considerations

CrypSA reduces validator load by:

* avoiding full simulation  
* validating only boundary-crossing actions  
* applying deeper validation selectively  

---

## Trust Model

CrypSA does not trust observer simulation.

It trusts:

> the validation process that determines what becomes canonical  

Observers may propose any action, but:

* invalid actions are rejected  
* only accepted events become canonical and are appended to canonical event history  

---

## Failure Modes

Validation must handle:

* duplicate submissions  
* delayed submissions  
* conflicting actions  
* incomplete context  

Validation outcomes must remain consistent regardless of:

* submission timing  
* message ordering  
* network conditions  

Strategies include:

* idempotency checks  
* conflict resolution  
* ordering rules based on `canonical_sequence`  

---

## Relationship to Canonical Event History

Validation determines what enters canonical event history.

Once accepted:

* events are immutable  
* history is append-only  
* state is derived via replay  

---

## Summary

CrypSA validation is:

* layered  
* deterministic  
* rule-driven  
* authoritative at the invariant boundary  

It ensures:

> observers may act freely,  
> only validated actions become canonical and are appended to canonical event history
