# CrypSA — State Model

This document defines the different forms of **state** in CrypSA.

It clarifies:

* what counts as **truth**
* what is **derived**
* what is **local to observers**
* what is **interpretation or experience**

Understanding these distinctions is critical to implementing CrypSA correctly.

---

## Purpose

CrypSA separates **canonical truth** from all other forms of state.

This document exists to:

* prevent confusion between state types
* protect the integrity of canonical truth
* guide implementation decisions
* ensure consistent mental models across contributors

---

## Core Principle

> In CrypSA, **canonical event history is the only source of truth**.
> All other state is derived, local, or interpretive.

---

## State Categories

CrypSA defines five primary categories of state:

1. Canonical Event History
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
* globally authoritative

It is controlled exclusively by:

* the **validator**
* through the **invariant boundary**

---

### Properties

* cannot be modified directly
* cannot be reordered
* cannot be partially rewritten
* must be deterministic

---

### Role

Canonical event history defines:

* what has happened
* the authoritative timeline
* the basis for all reconstruction

---

## 2. Derived Canonical State

Derived canonical state is:

* the current world state
* produced by replaying canonical event history

It is:

* deterministic
* reconstructable
* not authoritative

---

### Properties

* fully derived from canonical events
* can be rebuilt at any time
* may be cached for performance

---

### Role

Derived canonical state is used for:

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

* local simulation data
* UI state
* temporary computation results

---

### Properties

* not authoritative
* may diverge from canonical truth
* may be incomplete or approximate

---

### Role

Observer local state enables:

* responsiveness
* local interaction
* partial simulation

---

### Important

Observers may simulate freely, but:

> local state does not define truth.

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

* adapters (translation)
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

---

## State Flow

The relationship between state types can be visualized as:

```text
Canonical Event History (Truth)
        ↓ (Replay)
Derived Canonical State
        ↓ (Used by Validator & Observers)
Observer Local State
        ↓ (Prediction / Interaction)
Predicted State
        ↓ (Adapters + Lenses)
Interpreted / Experience State
```

---

## Authority Boundaries

| State Type              | Authority       | Can Modify Truth? |
| ----------------------- | --------------- | ----------------- |
| Canonical Event History | Validator       | Yes               |
| Derived Canonical State | System (Replay) | No                |
| Observer Local State    | Observer        | No                |
| Predicted State         | Observer        | No                |
| Interpreted State       | Observer        | No                |

---

## Key Rules

1. **Only canonical event history is truth**
2. **All state must be derivable from canonical events**
3. **Observers may simulate, but not define truth**
4. **Predicted state must reconcile with canonical outcomes**
5. **Interpretation must not mutate canonical data**

---

## Relationship to the Invariant Boundary

The invariant boundary:

* accepts candidate events
* validates them
* produces canonical events

It is the only mechanism by which:

* canonical event history may change

All other state types:

* depend on this process
* do not influence truth directly

---

## Relationship to Replay

Replay:

* consumes canonical event history
* produces derived canonical state

Replay is:

* deterministic
* foundational to reconstruction

---

## Relationship to Adapters and Lenses

Adapters:

* transform derived or local state into structured data

Lenses:

* determine meaning and visibility

Neither:

* define truth
* modify canonical state

---

## Implementation Notes (Non-Authoritative)

Implementations may:

* cache derived canonical state
* maintain local state for performance
* apply prediction systems

However:

* canonical event history must remain the source of truth
* all derived state must remain consistent with replay

---

## Summary

CrypSA defines multiple forms of state, but only one form of truth:

* **canonical event history** is authoritative
* all other state is derived, local, or interpretive

This separation ensures:

* deterministic reconstruction
* clear authority boundaries
* flexible observer behavior
* consistent system design

And critically:

> Truth is not stored as state — it is recorded as events.
