# CrypSA — Cryptid Server Architecture

CrypSA is an event-driven architecture for building persistent digital worlds.

Instead of synchronizing full world state, CrypSA synchronizes **validated canonical events under invariant rules**.

Observers simulate the world locally, while a **validator** determines what becomes canonical truth.

> Reality is not synchronized — it is agreed upon through validated events.

> The validator defines canonical truth.
> It may run locally or remotely, but its role does not change.

For documentation precedence and folder roles, see `DOCS_STRUCTURE.md`. 

---

## 🧭 Start Here

If you're new to CrypSA:

1. 🧭 `CrypSA_In_One_Diagram.md` — the entire system in one view
2. 📘 `CrypSA_In_5_Minutes.md` — quick overview
3. 📖 `CrypSA_Terminology_Primer.md` — understand the vocabulary
4. ❓ `FAQ.md` — common questions and concerns

---

## 🧠 Why CrypSA Exists

Traditional multiplayer systems synchronize state:

```text
Client → Server → State Sync
```

This leads to:

* complex server-side simulation
* difficult scaling
* tightly coupled systems
* limited flexibility

CrypSA takes a different approach:

```text
Observer → Validation → Canonical Event History → Reconstruction
```

Instead of synchronizing state, it:

* validates events
* records canonical history
* reconstructs reality deterministically

This creates a system that is:

* easier to reason about
* replayable by design
* flexible in deployment (local or remote validator)
* naturally aligned with persistent worlds

---

## 🧠 For Technical Readers

If you want to understand how CrypSA actually works:

1. `spec/CrypSA_Runtime_Spec_v0.1.md`
2. `spec/CrypSA_Spec_Index.md` (spec reading order)
3. `implementation/CrypSA_Minimal_Server_v0.1.md`

These define runtime behavior (spec) and how the system can be implemented (implementation).

---

## 🔄 The Core Idea

Traditional multiplayer systems:

* server simulates the world
* clients receive state updates

CrypSA:

* observers simulate locally
* actions become candidate events
* a validator evaluates events
* accepted events are appended to canonical event history
* derived canonical state is reconstructed via replay

> The system moves from synchronizing state → to agreeing on events

In CrypSA:

> state is not stored as truth — it is derived from canonical event history via replay

> canonical event history is append-only

---

## 🧠 Mental Model

CrypSA is easiest to understand as four responsibilities:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping runtime data
* **Interpretation** — lenses determining observer meaning
* **Experience** — UI and local interaction

See:

* `CrypSA_In_5_Minutes.md`
* `architecture/`

---

## 📊 How CrypSA Works (Visual Overview)

```mermaid
flowchart LR

A[Player Action] --> B[Local Simulation]
B --> C[Create Candidate Event]
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

For more diagrams:

👉 `diagrams/`

---

## ⚙️ What CrypSA Enables

* Persistent worlds independent of specific deployments
* Deterministic world reconstruction
* Built-in replay and debugging via event history
* Flexible client-side simulation
* Strong invariant-based validation
* Flexible deployment (local, host-based, or remote validator)
* Local-first and offline-capable development
* New gameplay models (observer-driven views, replay-based systems)

---

## 🧩 Key Concepts

* **Validator** — determines what becomes canonical truth
* **Minted Identities** — persistent object identities
* **Genomes** — deterministic object definitions
* **Canonical Events** — immutable events forming canonical event history
* **Invariants** — rules that must always hold
* **Observers** — systems that reconstruct and simulate
* **Lenses** — interpretation layers

See:

`CrypSA_Terminology_Primer.md`

---

## 🛠 Implementation Guidance

CrypSA is designed to be built **local-first**.

This means:

* start with a local validator
* validate the architecture locally
* move to multiplayer as a deployment change, not a rewrite

👉 See:

```
implementation/CrypSA_Local_First_Development_Approach.md
```

This explains:

* why local validators are the correct starting point
* how to structure systems for offline-first development
* how to scale from local → host → dedicated validator

---

## 📁 Repository Structure

### Exploratory Foundation

Conceptual framing and motivation

```
exploratory/foundation/
```

---

### Core Concepts

High-level system models (non-authoritative)

```
exploratory/core_concepts/
```

---

### Architecture

How CrypSA is structured

```
architecture/
```

---

### Specifications (Core Runtime Behavior)

Authoritative system behavior

```
spec/
```

Includes:

* runtime model
* event model
* validation model
* consistency model
* replay model
* snapshot model
* identity model
* transport model

---

### Design

Use cases and applicability

```
design/
```

---

### Implementation

How to build CrypSA systems

```
implementation/
```

---

### Teaching

Learning materials and prototype

```
teaching/
```

---

### Diagrams

Visual explanations (non-authoritative)

```
diagrams/
```

---

### Atlas

Glossary and navigation

```
atlas/
```

---

## 🛠 Current Project Status

CrypSA is currently:

* a defined architecture with formal specifications
* supported by documentation and a teaching prototype
* not yet a production-ready system

Next major step:

→ build a minimal validator (local-first, then extendable to remote)

See:

```
implementation/CrypSA_Project_Status.md
```

---

## 🧪 Teaching Prototype

Located in:

```
teaching/CrypSA_teaching_prototype/
```

This prototype:

* demonstrates validation, replay, and observers
* is a learning tool
* is **not a production runtime**

---

## 🧭 Recommended Reading Path

### 1. Understand the Idea

1. `CrypSA_In_One_Diagram.md`
2. `CrypSA_In_5_Minutes.md`
3. `CrypSA_Terminology_Primer.md`
4. `FAQ.md`

---

### 2. See a Concrete Example

5. `CrypSA_Worked_Example.md`

---

### 3. Understand the Architecture

6. `architecture/`
7. `spec/`

---

### 4. See the Model in Practice

8. `teaching/CrypSA_teaching_prototype/`

---

### 5. Move Toward Implementation

9. `implementation/CrypSA_Minimal_Server_v0.1.md`
10. `implementation/CrypSA_Local_First_Development_Approach.md`

---

## ⚠️ Scope and Limitations

CrypSA v0.1 is best suited for:

* persistent worlds
* simulation-heavy systems
* object-driven interactions

It is not yet optimized for:

* twitch shooters
* frame-perfect PvP
* heavy physics-based simulation

---

## 👤 Author

Beau Wells

---

## 📄 License

Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 📌 Citation

See `CITATION.cff`.

---

## One Sentence Summary

CrypSA is an event-driven architecture where observers simulate locally, a validator evaluates events, and shared reality is defined by canonical event history.
