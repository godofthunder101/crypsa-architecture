# CrypSA Truth vs State

This document defines the distinction between **truth** and **state** in CrypSA.

This is a **core architectural concept** and must not be reinterpreted or weakened.

---

## 📜 Authority Level

This document is part of `/spec` and is **authoritative**.

If any other document implies that state is authoritative, this document takes precedence.

---

## Purpose

This document defines:

* what constitutes **truth** in CrypSA
* what constitutes **state**
* how state is derived
* why state is not authoritative

---

## Defines

* truth
* canonical event history
* state
* derived canonical state
* authority boundaries between truth and state

---

## Does Not Define

* how state is stored
* how state is optimized (snapshots, caching, etc.)
* how state is presented
* implementation strategies for replay

---

## Core Principle

> Canonical event history is the source of truth.  
> All state, including derived canonical state, is a product of replay and is not itself authoritative.

---

## Truth

In CrypSA, **truth is defined exclusively as canonical event history**.

Truth has the following properties:

* append-only
* validator-defined
* globally consistent (within the system context)
* replayable
* authoritative

Truth is **not**:

* a snapshot
* a materialized state
* a database row set
* a cached structure

Truth exists only as:

👉 **the ordered sequence of canonical events**

---

## State

**State is a derived construct.**

State is produced by:

👉 replaying canonical event history

State has the following properties:

* derived
* reconstructable
* discardable
* environment-dependent (e.g. observer context, lenses)
* non-authoritative

State may exist in many forms:

* in-memory structures
* cached results
* database materializations
* UI representations

None of these forms are truth.

---

## Derived Canonical State

Derived canonical state refers to:

👉 the state produced by replaying canonical event history under canonical conditions

This form of state is:

* consistent with canonical history
* useful for system operation
* often treated as the “current state” of the system

However:

> Derived canonical state is still not truth.

It is:

* a **projection of truth**
* not the source of truth itself

---

## Why State Is Not Truth

State is not authoritative because:

1. **It is derived**
   * It depends on replay of canonical history

2. **It can be reconstructed**
   * Given canonical event history, state can be rebuilt

3. **It can diverge**
   * Different observers may hold different local state during reconciliation

4. **It is replaceable**
   * State can be discarded and recomputed without loss of truth

---

## Authority Boundary

The authority boundary in CrypSA is:

* **Before validation → not truth**
* **After validation → canonical event history (truth)**
* **After replay → state (derived, non-authoritative)**

---

## Common Misinterpretations

### ❌ “Canonical state is truth”

Incorrect.

There is no state representation that is inherently authoritative.

Only canonical event history is authoritative.

---

### ❌ “The database state is truth”

Incorrect.

A database is a storage mechanism for:

* derived state
* cached projections
* or canonical history

Only canonical history stored within it represents truth.

---

### ❌ “The latest state is truth”

Incorrect.

The latest state is:

* a **current projection**
* not a **source of authority**

---

## Implications

This distinction ensures that:

* systems remain replayable
* recovery is always possible
* observers can reconcile safely
* architecture does not depend on fragile state synchronization

---

## Related Documents

* `CrypSA_Event_Model.md`
* `CrypSA_Validation_Model.md`
* `CrypSA_Replay_Model.md`
* `CrypSA_State_Model.md`
