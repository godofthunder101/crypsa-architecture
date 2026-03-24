# CrypSA State Transition Diagram

## Purpose

This diagram shows how canonical universe state evolves in CrypSA.

The universe does not evolve through continuous simulation, but through:

> validated canonical events that transition the universe between stable states

---

## Diagram

```mermaid
flowchart TD

S0[Canonical State S_n]
A[Observer Simulation]
B[Invariant Boundary Check]
C[Candidate Event]
D[Validation and Invariant Enforcement]
R[Event Rejected]
E[Event Accepted]
S1[Canonical State S_n+1]

S0 --> A
A --> B

B -->|No invariant change| A
B -->|Affects canonical truth| C

C --> D

D -->|Rejected| R
R --> A

D -->|Accepted| E
E --> S1

S1 --> A
```

---

## How to Read This

### Canonical State

* represents shared truth at a given point
* derived from canonical event history
* stable and reconstructable

---

### Observer Simulation

Observers:

* reconstruct canonical state
* simulate locally
* generate interactions

---

### Invariant Boundary

The key decision point:

> Does this interaction affect canonical truth?

---

### Local Result

If no:

* the result remains local
* no canonical state change occurs

---

### Candidate Event

If yes:

* a candidate event is created
* submitted for validation

---

### Validation

The server:

* checks invariants
* verifies rules
* accepts or rejects

---

### State Transition

If accepted:

* event is appended to canonical history
* the universe transitions from Sₙ → Sₙ₊₁

---

### Rejection

If rejected:

* canonical state does not change
* observer corrects local simulation

---

## Key Insight

> Only validated canonical events can transition the universe between states.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → canonical events and state transitions
* **Experience** → observer simulation
* **Invariant Boundary** → decision between local and canonical

---

## Properties of State Transitions

CrypSA state transitions are:

* deterministic
* validated
* ordered
* reconstructable

---

## Why This Matters

This model enables:

* replay and reconstruction
* debugging via event history
* persistent worlds
* consistent shared truth

---

## One Sentence Summary

CrypSA models the universe as a sequence of validated canonical state transitions, where each accepted event moves the system from one stable state to the next.
