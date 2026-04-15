# CrypSA Terminology Primer

This document defines the core terms used throughout CrypSA.

If something feels unclear, check here first.

---

This document defines terms used in:

→ CrypSA_In_One_Diagram.md  
→ CrypSA_In_5_Minutes.md  

If something here feels abstract, refer back to those documents.

---

## 📜 Terminology Authority

This document defines the authoritative terminology used across CrypSA.  
It does not define runtime behavior.

CrypSA documentation is structured across layers:

* `/spec` — authoritative definition of runtime behavior  
* `/architecture` — system structure and conceptual models  
* `/architecture/CrypSA_Terminology_Primer.md` — authoritative terminology definitions  

If there is any conflict:

* spec takes precedence over terminology usage  

All other documents must:

* use these terms consistently  
* avoid redefining terms  
* reference this document when introducing terminology  

---

## ⚖️ Core Rule

If accepted, an event becomes canonical and is appended to canonical event history.

---

### Rule

Terms are defined once, and used everywhere else.

If a definition is needed outside this document, it must use:

→ See: Terminology Primer → [Term]

---

### Purpose

This ensures:

* consistency across the repository  
* no drift in meaning  
* a single source of truth for terminology  

---

## 🧠 Mental Model (Quick Anchor)

CrypSA can be understood as four responsibilities:

* **Truth** → canonical event history and validation  
* **Translation** → adapters shaping data  
* **Interpretation** → lenses defining meaning  
* **Experience** → UI and local interaction  

These responsibilities do not overlap.

> Canonical event history is the source of truth.

All terms below map into one of these responsibilities.

---

## 📌 Canonical Scope Rule

The term “canonical” applies only to:

* canonical events  
* canonical event history  

It does not apply to stored state.

Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## 🔁 Replay Terminology

Replay refers to reconstruction via canonical event replay.

It means applying canonical events from canonical event history in canonical_sequence order to reconstruct derived canonical state.

Replay is deterministic.

---

# 🔐 Validator vs Server (Critical Distinction)

The **validator** is the authority over canonical truth.

It:

* validates candidate events  
* enforces invariants  
* If accepted, an event becomes canonical and is appended to canonical event history  

A **server** is a deployment of a validator.

The validator:

* may run locally (same process as an observer)  
* may run remotely (shared system)  
* may run in a host-based configuration  

> The validator’s responsibilities do not change based on deployment.

---

## 🔒 Architectural Rule

Use **validator** when referring to:

* validation  
* canonical truth  
* event acceptance/rejection  
* canonical sequencing  

Use **server** only when referring to:

* network topology  
* deployment  
* infrastructure  

---

## ✅ Examples

| Incorrect                     | Correct                              |
| ----------------------------- | ------------------------------------ |
| server validates events       | validator validates events           |
| server accepts the event      | validator accepts the event          |
| server assigns sequence       | validator assigns canonical sequence |
| server is the source of truth | validator is the source of truth     |

---

## ⚠️ Important

If a sentence is still correct when the validator is running locally,  
then **“validator” is the correct term**, not “server”.

---

# Core Terms

---

## Validator

The **validator** determines what becomes canonical.

It:

* accepts or rejects candidate events  
* enforces invariants and rules  
* maintains canonical event history  

The validator is a **role**, not a machine.

It may run:

* locally (alongside an observer)  
* remotely (shared across observers)  

> The validator defines what becomes canonical.

---

## Invariant Boundary

The invariant boundary is where candidate events are evaluated by the validator.

It separates:

* observer-proposed events  
* canonical truth  

Only events that pass validation cross this boundary and become canonical.

---

## Local Validator

A **local validator** runs within the observer’s environment.

Examples:

* same process  
* same application  
* same device  

Use cases:

* single-player or offline operation  
* development and testing  
* local-first systems  
* resilience during network interruption  

Even when local, the validator remains a **separate logical role**.

The invariant boundary still exists:

* observer proposes candidate events  
* validator evaluates them  
* canonical event history is updated  

---

## Remote Validator

A **remote validator** runs on a separate system.

Observers communicate with it over a network.

Use cases:

* shared canonical truth  
* persistent multiplayer systems  
* distributed environments  

> Deployment changes location, not responsibility.

---

## Server (CrypSA Context)

A **server** is a remote deployment of a validator.

It is an infrastructure term, not an authority role.

Not all validators are servers.  
All servers host a validator.

---

## Canonical Event

A **canonical event** is an event that has become canonical through validation.

If accepted, an event becomes canonical and is appended to canonical event history.

Canonical events:

* are immutable  
* have a `canonical_sequence`  
* define truth  

---

## Candidate Event

A **candidate event** is:

* proposed by an observer  
* not yet validated  
* subject to rejection  

It represents **intent**, not truth, and does not affect canonical event history unless accepted.

---

## Invariant

An **invariant** is a rule that must always hold for canonical truth.

Examples:

* a player cannot have negative resources  
* two objects cannot occupy the same exclusive space  

Invariants protect canonical truth.

---

## Validation

**Validation** is the process performed by the validator to evaluate a candidate event.

It includes:

* schema validation  
* identity validation  
* precondition checks  
* invariant validation  
* rule validation  

Result:

* If accepted, an event becomes canonical and is appended to canonical event history  
* If rejected, the event does not become canonical  

---

## Canonical Event History

The **canonical event history** is:

* the ordered sequence of canonical events  
* the authoritative record of what has happened  

> Canonical event history is the source of truth.

Everything else is derived from this.

---

## Derived Canonical State

The **derived canonical state** is:

* the current world state  
* produced via replay  

It is:

* not authoritative  
* not stored as truth  
* always reconstructable  

> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

## Observer

An **observer**:

* simulates the world locally  
* proposes candidate events  
* reconciles with canonical truth  

Observers operate in the **experience layer**.

Observers do not define truth.

---

## Observer Reconciliation

**Observer reconciliation** is when:

* local simulation is updated  
* to match canonical outcomes  

This occurs via canonical event replay, aligning local derived state with canonical outcomes.

Observers do not modify canonical event history directly.

---

## Adapter

An **adapter** reshapes data.

It:

* transforms canonical and observer data  
* produces structured outputs  

Adapters belong to the **translation layer**.

Adapters reshape data without affecting truth or interpreting meaning.

---

## Lens

A **lens** interprets data.

It determines:

* meaning  
* relevance  
* context for an observer  

Lenses belong to the **interpretation layer**.

Lenses interpret data but do not modify canonical data or define truth.

---

## UI / Experience

The **experience layer** includes:

* rendering  
* input  
* local feedback  

It is:

* responsive  
* immediate  
* non-authoritative  

---

## Replay

**Replay** reconstructs derived canonical state via canonical event replay.

---

# Summary

CrypSA separates the system into four responsibilities:

* **truth** → canonical event history and validation  
* **translation** → adapters shape data  
* **interpretation** → lenses define meaning  
* **experience** → local interaction  

And critically:

> The validator defines what becomes canonical, regardless of deployment.
