# CrypSA State Transition Diagram

## Purpose

This diagram shows how canonical universe state evolves in CrypSA.

The universe does not evolve through continuous simulation, but through:

> validated canonical events that transition the universe between stable states

For the authoritative conceptual flow of the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Diagram

> This diagram illustrates state transitions within the CrypSA runtime model.
> It does not define runtime behavior or event flow.
> For the authoritative conceptual flow, see:
> → ../architecture/CrypSA_Runtime_Model.md

```mermaid
flowchart TD

S0["Derived Canonical State S_n"]
A["Local Simulation"]
B["Invariant Boundary Check"]
C["Create Candidate Event"]
D["Validation and Invariant Enforcement"]
R["Event Rejected"]
E["Event Accepted"]
O["Assign canonical_sequence"]
S1["Derived Canonical State S_n+1"]

S0 --> A
A --> B

B -->|Does not affect canonical event history| A
B -->|Affects canonical event history| C

C --> D

D -->|Rejected| R
R --> A

D -->|Accepted| E
E --> O
O --> S1

S1 --> A
````

---

## How to Read This

### Canonical State

* represents state derived from canonical event history
* stable and reconstructable

Derived canonical state is not the source of truth.

It is produced from canonical event history and reflects the current validated state of the universe.

---

### Observer Simulation

Observers:

* reconstruct derived canonical state
* simulate locally
* generate interactions

This simulation is responsive and immediate, but not authoritative.

---

### Invariant Boundary

The key decision point is:

> Does this interaction affect canonical event history?

If not, the result remains local.

If yes, the interaction must cross the invariant boundary as a candidate event.

---

### Local Result

If no:

* the result remains local
* no canonical event history change occurs

---

### Candidate Event

If yes:

* a candidate event is created
* submitted to the validator for evaluation

---

### Validation

The validator:

* checks invariants
* verifies rules
* accepts or rejects

The validator may run locally or remotely, but its role does not change.

Validation determines whether the proposed interaction becomes canonical.

---

### State Transition

If accepted:

* the validator assigns `canonical_sequence`
* canonical_sequence defines the authoritative ordering of events for replay
* the event is appended to canonical event history
* the universe transitions from Sₙ → Sₙ₊₁ via deterministic replay

This is how canonical state changes in CrypSA.

---

### Rejection

If rejected:

* canonical event history does not change
* observer corrects local simulation

---

## Key Insight

> Only validated canonical events can transition the universe between states.

And:

> local simulation may propose changes, but only validation can make them real.

---

## Relationship to Architecture

This diagram reflects:

* **Truth** → canonical event history and validation
* **Experience** → observer simulation
* **Invariant Boundary** → decision between local and canonical

---

## Properties of State Transitions

CrypSA state transitions are:

* deterministic
* validated
* ordered (via `canonical_sequence`)
* reconstructable

---

## Why This Matters

This model enables:

* replay and reconstruction
* debugging via event history
* persistent worlds
* consistent shared reality

Because the universe evolves through validated canonical events rather than uncontrolled simulation, every canonical transition can be understood, replayed, and verified.

---

## One Sentence Summary

CrypSA models the universe as a sequence of validated canonical state transitions ordered via `canonical_sequence`, where each accepted event moves the system from one stable state to the next through canonical event history.
