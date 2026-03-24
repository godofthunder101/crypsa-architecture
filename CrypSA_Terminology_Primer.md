# CrypSA Terminology Primer

This document defines the core terms used throughout CrypSA.

If something feels unclear, check here first.

---

## Mental Model (Quick Anchor)

A useful way to understand CrypSA is to think in terms of four responsibilities:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining observer meaning
* **Experience** — UI and local interaction

The terms below map into these responsibilities.

---

## Core Terms

### Canonical Event

A canonical event is an event that has been:

* validated by the server
* accepted into canonical event history
* assigned canonical order (`server_sequence`)
* made immutable

Canonical events define **truth**.

---

### Candidate Event

A candidate event is:

* proposed by an observer
* not yet validated
* subject to rejection

Candidate events are **attempts at truth**, not truth itself.

---

### Invariant

An invariant is a rule that must always hold.

Examples:

* a player cannot have negative resources
* two objects cannot occupy the same exclusive space

Invariants are enforced during validation and protect **truth**.

---

### Validation

Validation is the process of evaluating a candidate event before it becomes canonical.

It includes:

* schema validation
* identity validation
* precondition checks
* invariant validation
* rule validation

If valid → it becomes canonical
If invalid → it is rejected

Validation determines whether something becomes **truth**.

---

### Canonical Event History

The canonical event history is:

* the ordered sequence of accepted canonical events
* the authoritative record of what has happened

Everything else derives from this.

---

### Replay

Replay is the process of:

* taking canonical event history
* applying events in canonical order
* rebuilding derived state deterministically

Replay is how **truth becomes state**.

---

### Derived State

Derived state is:

* the current world state
* produced from replaying canonical event history

It is:

* not authoritative
* not stored as truth
* always reconstructable

---

### Observer

An observer is:

* a client
* a local simulation of the world

Observers:

* simulate locally
* propose candidate events
* reconcile with canonical truth

Observers contribute to the **experience layer**.

---

### Observer Reconciliation

Observer reconciliation is when:

* an observer updates its local simulation
* to match canonical outcomes

This occurs after events are accepted or rejected.

---

### Adapter

An adapter reshapes data.

It:

* takes canonical and observer-derived state
* produces structured outputs for interpretation or UI

Adapters belong to the **translation layer**.

They do not define truth.

---

### Lens

A lens interprets data.

It determines:

* what is visible
* what is interactable
* what matters to an observer

Lenses belong to the **interpretation layer**.

They do not define truth or mutate state.

---

### UI / Experience

The experience layer includes:

* rendering
* input
* local feedback

This is what the player interacts with directly.

It is responsive, but not authoritative.

---

## Summary

CrypSA separates the system into four responsibilities:

* **truth** is defined by canonical event history
* **translation** shapes data via adapters
* **interpretation** gives meaning via lenses
* **experience** presents the world to the observer

Understanding this separation makes the rest of CrypSA much easier to follow.
