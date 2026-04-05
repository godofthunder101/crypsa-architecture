# CrypSA Terminology Primer

This document defines the core terms used throughout CrypSA.

If something feels unclear, check here first.

---

This document defines terms used in:

→ CrypSA_In_One_Diagram.md
→ CrypSA_In_5_Minutes.md

If something here feels abstract, refer back to those docs.

---

## 🔒 Terminology Authority

This document is the **authoritative source of all core term definitions in CrypSA**.

All other documents must:

* use these terms consistently
* avoid redefining terms independently
* reference this document when introducing terminology

---

### Rule

Terms are defined once, and used everywhere else.

If a definition is needed outside this document, it must use the form:

→ See: Terminology Primer → [Term]

---

### Purpose

This ensures:

* consistency across the repository
* no drift in meaning
* a single source of truth for terminology

---

## Mental Model (Quick Anchor)

A useful way to understand CrypSA is to think in terms of four responsibilities:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local interaction

The terms below map into these responsibilities.

---

## 🔐 Validator vs Server (Critical Distinction)

The **validator** is the authority over canonical truth.

It is responsible for:

* validating candidate events
* enforcing invariants
* appending accepted events to canonical event history

A **server** is one possible deployment of a validator.

The validator:

* may run locally (same process as an observer)
* may run remotely (as a dedicated server)
* may run in a host-based configuration

Its responsibilities do **not change** based on deployment.

---

### 🔒 Architectural Rule

All architectural descriptions must use **validator** when referring to:

* validation
* canonical truth
* event acceptance/rejection
* canonical sequencing

Use **server** only when referring to:

* network topology
* deployment model
* infrastructure

---

### ✅ Examples

| Incorrect                     | Correct                              |
| ----------------------------- | ------------------------------------ |
| server validates events       | validator validates events           |
| server accepts the event      | validator accepts the event          |
| server assigns sequence       | validator assigns canonical sequence |
| server is the source of truth | validator is the source of truth     |

---

### ⚠️ Important

If a sentence is still correct when the validator is running locally,
then **“validator” is the correct term**, not “server”.

---

## Core Terms

### Validator

A **validator** is responsible for:

* accepting or rejecting candidate events
* enforcing invariants and rules
* maintaining canonical event history

The validator determines what becomes part of canonical truth.

The validator is a **role**, not a specific machine.

It may run:

* **locally**, alongside an observer
* **remotely**, as a shared system for multiple observers

> In CrypSA, truth is defined by validation — not by where the validator runs.

---

### Local Validator

A **local validator** runs within the same environment as the observer.

This may mean:

* the same process
* the same application
* the same device

Common use cases:

* single-player or offline operation
* development and testing
* local-first system design
* resilience during network interruption

Even when local, the validator remains a **separate logical role**.

The invariant boundary still exists:

* observer proposes candidate events
* validator accepts or rejects them
* canonical event history is updated

> Local validation changes location, not responsibility.

---

### Remote Validator

A **remote validator** runs on a separate system from the observer.

Observers communicate with it over a network.

Common use cases:

* shared canonical truth across observers
* persistent multiplayer environments
* distributed systems

The responsibilities remain unchanged.

> Deployment does not redefine truth.

---

### Server (CrypSA Context)

A **server** is a deployment of a validator that runs remotely.

It is an infrastructure term, not an authority role.

Not all validators are servers, but all servers host a validator.

---

### Canonical Event

A canonical event is an event that has been:

* validated by the validator
* accepted into canonical event history
* assigned a `canonical_sequence`
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

If valid → appended to canonical event history
If invalid → rejected

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

An observer is a system that:

* simulates the world locally
* proposes candidate events
* reconciles with canonical event history

Observers contribute to the **experience layer**.

---

### Observer Reconciliation

Observer reconciliation is when:

* an observer updates its local simulation
* to match canonical outcomes

---

### Adapter

An adapter reshapes data.

It:

* transforms canonical and observer data
* produces structured outputs for other layers

Adapters belong to the **translation layer**.

They change structure, not meaning.

---

### Lens

A lens interprets data.

It determines:

* meaning
* relevance
* context for an observer

Lenses belong to the **interpretation layer**.

They do not define truth or mutate canonical data.

---

### UI / Experience

The experience layer includes:

* rendering
* input
* local feedback

This is what the observer interacts with directly.

It is responsive, but not authoritative.

---

## Summary

CrypSA separates the system into four responsibilities:

* **truth** is defined by canonical event history and validation
* **translation** shapes data via adapters
* **interpretation** gives meaning via lenses
* **experience** presents the world to the observer

And critically:

> validation defines canonical truth, regardless of deployment

Understanding this separation makes the rest of CrypSA much easier to follow.

---

## Next Step

Continue to:

👉 `CrypSA_Worked_Example.md`
