# CrypSA Validation Model v0.1

This document defines how CrypSA validates proposed actions before they become part of canonical event history.

Validation is the mechanism that:

* protects canonical event history
* enforces invariants
* determines what becomes canonical

---

## Core Principle

In CrypSA:

> Clients may simulate freely, but only validated events become part of canonical event history.

Validation occurs at the **Invariant Boundary**, where proposed actions transition from local simulation to canonical event history.

---

## Validation Flow

The validation pipeline follows this sequence:

1. **Observer Action**  
   Local simulation only  

2. **Candidate Creation**  
   Action becomes a candidate event  

3. **Submission**  
   Event is sent to the server  

4. **Validation**  
   Server evaluates the event  

5. **Decision**

   * accepted → becomes a canonical event  
   * rejected → discarded  

6. **Canonical Update**  
   Accepted events are assigned `server_sequence` and appended to canonical event history  

7. **Observer Reconciliation**  
   Observers update local state based on canonical events  

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

Ensures client assumptions are still true.

Checks include:

* expected state matches canonical state  
* required resources exist  
* required conditions hold  

---

### 4. Invariant Validation

Ensures canonical rules are not violated.

Examples:

* no duplicate ownership  
* valid placement  
* valid state transitions  

---

### 5. Rule Validation

Ensures event-specific rules are satisfied.

Examples:

* upgrade paths  
* allowed interactions  
* resource costs  

---

### 6. Optional Validation Layers

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

## Validation Requirements

Validation must be:

* deterministic  
* atomic within conflict scope  
* based on canonical event history and derived canonical state  

---

## Validation Outcomes

Each candidate results in:

---

### Accepted

* event is valid  
* assigned `server_sequence`  
* appended to canonical event history  
* becomes part of canonical event history  

---

### Rejected

* event violates rules  
* no canonical change  

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

## Invariant Design

Invariants define:

* what must always be true  
* what cannot be violated  

Examples:

* an object has one location  
* ownership is unique  
* transitions follow valid paths  

Strong invariant design ensures:

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
| Canonical events | Fully validated |

---

## Performance Considerations

CrypSA reduces server load by:

* avoiding full simulation  
* validating only boundary-crossing actions  
* applying deeper validation selectively  

---

## Trust Model

CrypSA does not trust client simulation.

It trusts:

> the validation process that determines canonical event history  

Clients may propose any action, but:

* invalid actions are rejected  
* only accepted events affect canonical event history  

---

## Failure Modes

Validation must handle:

* duplicate submissions  
* delayed submissions  
* conflicting actions  
* incomplete context  

Strategies include:

* idempotency checks  
* conflict resolution  
* ordering rules  

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

> clients may act freely,  
> but only valid actions become part of canonical event history
