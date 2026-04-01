# CrypSA Terminology Primer

This document defines the core terms used throughout CrypSA.

If something feels unclear, check here first.

---

## Mental Model (Quick Anchor)

A useful way to understand CrypSA is to think in terms of four responsibilities:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining observer meaning
* **Experience** — UI and local interaction

The terms below map into these responsibilities.

---

## Core Terms

### Validator

A **validator** is the system responsible for:

* accepting or rejecting candidate events
* enforcing invariants and rules
* maintaining canonical event history

The validator determines what becomes part of canonical truth.

The validator is a **role**, not a specific machine.

It may run:

* **locally**, alongside an observer
* **remotely**, as a shared system for multiple observers

The responsibilities of the validator do not change based on where it runs.

> In CrypSA, truth is defined by validation — not by where the validator is located.

---

### Local Validator

A **local validator** is a validator that runs within the same environment as the observer.

This may mean:

* the same process
* the same application
* the same device

A local validator is commonly used for:

* single-player or offline operation
* development and testing
* local-first system design
* resilience during network interruption

Even when local, the validator remains a **separate logical role**.

The invariant boundary still exists:

* observer proposes candidate events
* validator accepts or rejects them
* canonical event history is updated

> Local validation does not remove the boundary between observer and truth — it changes where that boundary runs.

---

### Remote Validator

A **remote validator** is a validator that runs on a separate system from the observer.

Observers communicate with it over a network.

A remote validator is commonly used for:

* shared canonical truth across multiple observers
* persistent multiplayer environments
* authoritative validation in distributed systems

The responsibilities of the validator remain the same:

* validate candidate events
* enforce invariants
* maintain canonical event history

> Moving the validator to a remote system changes deployment, not the definition of truth.

---

### Server (CrypSA Context)

In CrypSA, a **server** is a deployment of a validator that runs remotely.

Not all validators are servers, but all servers act as validators.

---

### Canonical Event

A canonical event is an event that has been:

* validated by the validator
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

If valid → it is appended to canonical event history
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
* rebuilding derived canonical state deterministically

Replay is how canonical event history is transformed into derived canonical state.

---

### Derived Canonical State

Derived canonical state is:

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
* reconcile with canonical event history

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

* **truth** is defined by canonical event history and validation
* **translation** shapes data via adapters
* **interpretation** gives meaning via lenses
* **experience** presents the world to the observer

And critically:

> validation defines canonical truth, regardless of whether the validator runs locally or remotely

Understanding this separation makes the rest of CrypSA much easier to follow.
