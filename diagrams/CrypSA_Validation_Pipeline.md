# CrypSA Validation Pipeline

This diagram shows how the canonical server evaluates a candidate event before it can become part of canonical history.

It represents the layered validation model used to decide whether an event is:

- accepted
- rejected

---

```mermaid
flowchart TD

A[Candidate Event] --> B[Schema Validation]

B -->|Fail| R1[Reject: invalid_schema]
B -->|Pass| C[Identity Validation]

C -->|Fail| R2[Reject: invalid_identity]
C -->|Pass| D[Precondition Validation]

D -->|Fail| R3[Reject: precondition_failed]
D -->|Pass| E[Invariant Validation]

E -->|Fail| R4[Reject: invariant_violation]
E -->|Pass| F[Rule Validation]

F -->|Fail| R5[Reject: rule_violation]
F -->|Pass| G[Accept Event]

G --> H[Append to Canonical Log]
H --> I[Update Derived State]
I --> J[Broadcast Canonical Update]

````

---

## How to Read This

### 1. Schema Validation

The server checks that the candidate event is well-formed.

Examples:

* required fields exist
* payload shape is valid
* field types are correct

---

### 2. Identity Validation

The server checks that referenced identities are valid.

Examples:

* actor exists
* target object exists
* branch reference is valid

---

### 3. Precondition Validation

The server checks that the client’s assumptions are still true.

Examples:

* tile is still empty
* actor still owns the object
* required resources still exist

---

### 4. Invariant Validation

The server checks that canonical rules would remain true if the event were accepted.

Examples:

* no duplicate ownership
* no impossible placement
* no invalid state transition

---

### 5. Rule Validation

The server checks event-specific rules.

Examples:

* structure type is allowed here
* upgrade path is valid
* resource cost is correct

---

## Key Insight

> Validation is layered.
> Failure at any stage prevents canonicalization.

---

## Relationship to Specs

This diagram maps directly to:

* `spec/CrypSA_Validation_Model.md`
* `spec/CrypSA_Runtime_Spec_v0.1.md`

---

## One Sentence Summary

A candidate event must pass schema, identity, precondition, invariant, and rule validation before it can become part of canonical history.
