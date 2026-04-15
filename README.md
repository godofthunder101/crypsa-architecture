> ⚠️ This repository defines an architecture model.
> If you are reviewing it, please read REVIEWER_GUIDE.md first.

# CrypSA — Cryptid Server Architecture

CrypSA defines how systems establish canonical truth through validated canonical events and deterministic replay.

In CrypSA:

* the validator defines what becomes canonical
* canonical event history is the source of truth
* derived canonical state is reconstructed via replay

It is an event-driven architecture for building persistent digital worlds.

Rather than synchronizing world state, CrypSA synchronizes validated canonical events governed by invariants.

All canonical changes must cross the invariant boundary, where invariants are enforced before events can become canonical. Observers perform local simulation and predictive behavior.

> Reality is not synchronized — it is agreed upon through validated events.  
> Canonical event history is the source of truth.

The validator may run locally or remotely, but its role as the authority of canonical truth does not change.

---

## 🚀 Start Here (Required Path)

If this is your first time reading CrypSA, follow this path:

1. 🧭 `CrypSA_In_One_Diagram.md` — see the system at a glance  
2. 📘 `CrypSA_In_5_Minutes.md` — understand the core idea  
3. 📖 `CrypSA_Terminology_Primer.md` — learn the language  
4. 📖 `CrypSA_Worked_Example.md` — see it in action  

---

👉 **Only after completing the above:**

**These documents assume familiarity with the core model.**

5. 🏗 `architecture/` — understand system structure  
6. 📜 `/spec` — understand authoritative runtime behavior  

---

⚠️ **Do not start with `/spec` on your first pass.**  
CrypSA is concept-driven and requires the mental model first.

---

## 📘 Additional Navigation

For a deeper walkthrough of how to read CrypSA:

👉 `How_To_Read_CrypSA.md`

For core terminology:

👉 `CrypSA_Terminology_Primer.md`

---

## 🧭 Reading Modes

Choose your path based on your goal:

---

### First-time reader  
Follow the **Start Here (Required Path)** above.

---

### Architecture deep dive  
Go to:

👉 `architecture/`

---

### Formal behavior (authoritative)  
Go to:

👉 `/spec`

---

### Implementation / building  
Go to:

👉 `implementation/`

---

## 🏗 Infrastructure Implications

CrypSA changes how systems distribute:

* computation
* state
* synchronization

Instead of relying on continuous server-side simulation and state synchronization:

* observers perform local prediction  
* canonical truth is defined by validated events  
* state is reconstructed via replay  

This results in a different distribution of infrastructure responsibilities.

For a neutral breakdown of these changes, see:

👉 `architecture/CrypSA_Infrastructure_Implications.md`

---

## ⚙️ Canonical Event Lifecycle (At a Glance)

The canonical event lifecycle is defined by the CrypSA runtime model:

👉 `architecture/CrypSA_Runtime_Model.md`

At a high level:

1. Observers create candidate events  
2. Events are validated by the validator  
3. If accepted, an event becomes canonical and is appended to canonical event history  
4. Observers derive state through replay and reconciliation  

This defines the boundary between:

* local simulation (non-authoritative)  
* canonical reality (validator-defined)  

Canonical event history is an append-only log.  
It is never mutated, only extended through accepted events.

All derived state must be consistent with this history.

Canonical event history is the source of truth.

---

## 🛠 Build CrypSA

Start with the smallest working system:

👉 `implementation/CrypSA_Minimal_Runtime_Walkthrough.md`

Then explore:

👉 `implementation/minimal_validator/CrypSA_Minimal_Validator_v0.1.md`  
👉 `implementation/CrypSA_Local_First_Development_Approach.md`

---

## 🧠 What CrypSA Is (and Is Not)

CrypSA defines how systems establish and maintain canonical truth through validated canonical events.

It provides a model where:

* truth is validated, not assumed  
* the validator defines what becomes canonical  
* state is derived, not synchronized  
* simulation is local, but canonical authority is enforced by the validator  

> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

### ✅ CrypSA Is

CrypSA is:

* a structured architecture model  
* a set of invariants around truth, validation, and canonical event history  
* a framework for building replayable and consistent systems  

It defines:

👉 what must be true for a system to maintain canonical agreement  

CrypSA is typically integrated alongside existing systems such as game engines, simulation layers, and networking stacks.

Systems built with CrypSA are inherently replayable from canonical event history.

---

### ❌ CrypSA Is NOT

CrypSA is not:

* a fixed networking architecture  
* a required client-server topology  
* a one-size-fits-all implementation  
* a game engine  
* a networking library  
* a state replication system  
* an ECS framework  
* a state synchronization model  

> CrypSA defines truth agreement, not rendering, transport, or simulation.

---

### 🧭 What CrypSA Defines vs Leaves Open

CrypSA defines:

* how events become canonical  
* how truth is established  
* how state is derived from canonical event history  

CrypSA intentionally leaves open:

* how systems are structured at runtime  
* how networking is implemented  
* how reconciliation and prediction are handled  
* how systems are shaped to meet product goals  

👉 CrypSA defines invariants and structure, not a single implementation.  

👉 CrypSA provides a structured design space for making these decisions.  

👉 Implementers are expected to choose these based on product requirements.  

This flexibility is intentional.

CrypSA is designed to support multiple valid implementations that all preserve canonical truth through validation and canonical event history.

---

## 📘 Learn More

For a full breakdown of invariants and product-dependent design:

👉 `architecture/CrypSA_Invariants_and_Design_Space.md`

For strict separation of responsibilities:

👉 `architecture/CrypSA_Boundary_Definitions.md`

---

## ⚙️ How CrypSA Works

```mermaid
flowchart LR  

A[Player Action] --> B[Local Prediction]
B --> C[Observer Creates Candidate Event]
C --> D[Submit to Validator]

D --> E[Validation Pipeline]

E -->|Accepted| F[Canonical Event History]
E -->|Rejected| G[Rejection Result]

F --> H[Replay]
H --> I[Derived Canonical State]
I --> J[Broadcast]

J --> K[Observer Reconciliation]
G --> K
```

> If accepted, an event becomes canonical and is appended to canonical event history.

For the full runtime flow, see:

👉 `architecture/CrypSA_Runtime_Model.md`
