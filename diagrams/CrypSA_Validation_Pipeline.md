# CrypSA Validation Pipeline

## Purpose

This diagram shows how the **validator** evaluates a candidate event before it becomes part of canonical event history.

It represents the layered validation model used to determine whether an event is:

* accepted
* rejected

---

## Diagram

```mermaid id="t1o4rv"
flowchart TD

A[Candidate Event] --> B[Schema Validation]

B -->|Fail| R1[Reject invalid_schema]
B -->|Pass| C[Identity Validation]

C -->|Fail| R2[Reject invalid_identity]
C -->|Pass| D[Precondition Validation]

D -->|Fail| R3[Reject precondition_failed]
D -->|Pass| E[Invariant Validation]

E -->|Fail| R4[Reject invariant_violation]
E -->|Pass| F[Rule Validation]

F -->|Fail| R5[Reject rule_violation]
F -->|Pass| G[Accept and Assign server_sequence]

G --> H[Append to Canonical Event History]
H --> I[Observers Receive Canonical Update]
```

---

## How to Read This

### 1. Schema Validation

The validator checks that the event is well-formed.

Examples:

* required fields exist
* payload structure is valid
* data types are correct

---

### 2. Identity Validation

The validator verifies referenced identities.

Examples:

* actor exists
* target exists
* references are valid

---

### 3. Precondition Validation

The validator checks that assumptions still hold.

Examples:

* tile is still empty
* ownership is unchanged
* required resources still exist

---

### 4. Invariant Validation

The validator ensures canonical event history does not violate invariants.

Examples:

* no invariant violations
* no invalid transitions
* no impossible states

---

### 5. Rule Validation

The validator applies event-specific rules.

Examples:

* placement rules
* upgrade constraints
* cost validation

---

## Key Insight

> Validation is layered.
> Failure at any stage prevents the event from being appended to canonical event history.

And:

> validation is the mechanism that determines whether a candidate event becomes canonical truth

---

## Relationship to Architecture

This diagram reflects the **truth layer**:

* validation
* invariant enforcement
* canonical event recording

The validator operates entirely within this layer.

---

## Relationship to Specs

This diagram maps to:

* `spec/CrypSA_Validation_Model.md`
* `spec/CrypSA_Runtime_Spec_v0.1.md`

---

## One Sentence Summary

A candidate event must pass schema, identity, precondition, invariant, and rule validation before it is assigned `server_sequence`, accepted, and recorded in canonical event history.
