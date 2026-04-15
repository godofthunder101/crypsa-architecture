# CrypSA — State Model

This document defines the different forms of **state** in CrypSA.

It clarifies:

* what is **truth**
* what is **derived**
* what is **local to observers**
* what is **interpretation or experience**

Understanding these distinctions is critical to implementing CrypSA correctly.

---

## 📜 Authority Level

This document is part of `/spec` and defines **state structure and behavior**.

👉 For the authoritative definition of truth vs state, see:
`CrypSA_Truth_vs_State.md`

If there is any conflict, **`CrypSA_Truth_vs_State.md` takes precedence**.

---

## Purpose

CrypSA separates **canonical truth** from all other forms of state.

This document exists to:

* define categories of state
* prevent confusion between state types
* protect the integrity of canonical truth
* guide implementation decisions
* ensure consistent mental models across contributors

---

## Defines

* categories of state
* authority of each state type
* relationship between truth and state

---

## Does Not Define

* validation rules
* invariant definitions
* replay implementation details
* observer implementation strategies

---

## Core Principle

> Canonical event history is the source of truth.  
> All state, including derived canonical state, is a product of replay and is not itself authoritative.

---

## Non-Negotiable Rule

State is never truth.

No form of state in CrypSA is authoritative.

Only canonical event history defines truth.

---

## State Categories

CrypSA defines five primary categories of state:

1. Canonical Event History (Truth)
2. Derived Canonical State
3. Observer Local State
4. Predicted (Speculative) State
5. Interpreted / Experience State

Each category has different responsibilities and authority.

---

## 1. Canonical Event History (Truth)

The **canonical event history** is:

* the ordered sequence of accepted canonical events
* the **only authoritative source of truth**

It is:

* append-only
* immutable
* authoritative within the system context

It is controlled exclusively by:

* the **validator**
* through the **invariant boundary**

---

### Role

Canonical event history defines:

* what has happened
* the authoritative timeline
* the basis for all reconstruction

---

## 2. Derived Canonical State

Derived canonical state is:

* a reconstructed representation of the system
* produced by replaying canonical event history

It is:

* deterministic when replayed against canonical event history under the same validation context
* reconstructable
* discardable
* not authoritative

---

### Properties

* fully derived from canonical events
* can be rebuilt at any time
* may be cached for performance

---

### Role

Derived canonical state is used as:

* validation context
* simulation reference
* synchronization
* debugging and replay

---

### Important

> Derived canonical state is **not truth** — it is a projection of truth.

---

## 3. Observer Local State

Observer local state exists within an observer.

It includes:

* local simulation state
* temporary runtime data

---

### Properties

* not authoritative
* may temporarily diverge from derived canonical state during reconciliation
* may be incomplete or approximate representations

---

### Role

Observer local state enables:

* responsiveness
* local interaction
* partial simulation

---

### Important

Observers may simulate freely, but:

> Local state does not define truth.

---

## 4. Predicted (Speculative) State

Predicted state is a form of observer local state.

It represents:

* expected outcomes of candidate events
* local prediction before validation

---

### Properties

* speculative
* may be incorrect
* must be reconciled

---

### Role

Predicted state enables:

* immediate feedback
* smooth interaction
* latency hiding

---

### Important

After validation:

* accepted predictions are confirmed
* rejected predictions must be corrected

---

## 5. Interpreted / Experience State

Interpreted state is what the observer **perceives**.

It is produced by:

* lenses (interpretation)
* UI systems (experience)

---

### Properties

* observer-specific
* context-dependent
* non-authoritative

---

### Role

This state determines:

* visibility
* interaction options
* presentation
* meaning

---

### Important

> Interpretation does not change truth — it changes perception.

Lenses do not influence validation or canonical outcomes.

---

## State Flow

The relationship between state types:

```text
Canonical Event History (Truth)
        ↓ (Replay)
Derived Canonical State
        ↓ (Used by validation and observers)
Observer Local State (includes predicted state)
        ↓ (Adapters + Lenses)
Interpreted / Experience State
````

---

## Authority Boundaries

| State Type              | Authority      | Can Modify Truth? |
| ----------------------- | -------------- | ----------------- |
| Canonical Event History | Validator      | Yes               |
| Derived Canonical State | Replay Process | No                |
| Observer Local State    | Observer       | No                |
| Predicted State         | Observer       | No                |
| Interpreted State       | Observer       | No                |

---

## Key Rules

1. **Only canonical event history is truth**
2. **All state must be derivable from canonical event history**
3. **State is always non-authoritative**
4. **Observers may simulate, but not define truth**
5. **Predicted state must reconcile with canonical outcomes**
6. **Interpretation must not mutate canonical data**

---

## Relationship to the Invariant Boundary

The invariant boundary:

* accepts candidate events
* validates them
* produces canonical events

It is the only mechanism by which:

* canonical event history may change

All state:

* depends on this process
* does not influence truth directly

---

## Relationship to Replay

Replay:

* consumes canonical event history
* produces derived canonical state

Replay is:

* deterministic when applied to canonical event history under the same validation context
* the foundation of reconstruction

---

## Relationship to Adapters and Lenses

Adapters:

* transform derived or local state into structured data

Lenses:

* interpret canonical and local data into meaning and experience

Neither:

* define truth
* modify canonical event history

---

## Implementation Notes (Non-Authoritative)

Implementations may:

* cache derived canonical state
* maintain local state for performance
* apply prediction systems

However:

* canonical event history remains the source of truth
* all state must remain consistent with replay

---

## Summary

CrypSA defines multiple forms of state, but only one form of truth:

* **canonical event history is authoritative**
* all state is derived, local, or interpretive

This separation ensures:

* deterministic reconstruction
* clear authority boundaries
* flexible observer behavior
* consistent system design

And critically:

> Truth is not stored as state — it is recorded as events.
