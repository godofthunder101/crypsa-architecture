CrypSA — Cryptid Server Architecture

CrypSA is an event-driven architecture for building persistent digital worlds.

Instead of synchronizing full world state, CrypSA synchronizes validated canonical events under invariant rules.

Observers simulate locally, while a validator evaluates events.

> The validator defines what becomes canonical.



Canonical events form canonical event history, which is the source of truth.

Reality is not synchronized — it is agreed upon through validated events.

The validator may run locally or remotely, but its role does not change.


---

🚀 Start Here

If you're new to CrypSA, follow this path:

🧭 CrypSA_In_One_Diagram.md — see the system at a glance

📘 CrypSA_In_5_Minutes.md — understand the core idea

📖 CrypSA_Terminology_Primer.md — learn the language

📖 CrypSA_Worked_Example.md — see it in action



---

🛠 Build CrypSA

Start implementing with the minimal validator:

👉 implementation/minimal_validator/CrypSA_Minimal_Validator_v0.1.md

Then follow:

👉 implementation/CrypSA_Local_First_Development_Approach.md


---

🧠 What CrypSA Is

CrypSA defines how systems agree on truth.

It provides a model where:

truth is validated, not assumed

state is derived from canonical event history, not synchronized

simulation is local, but authority is centralized


This enables systems that are:

deterministic

replayable

resistant to desynchronization



---

❌ What CrypSA Is Not

CrypSA does not replace engines or networking stacks.

It is not:

a game engine

a networking library

a state replication system

an ECS framework


CrypSA defines truth agreement, not rendering, transport, or simulation.


---

🔒 Core Rules

The following must always hold:

Only the validator may modify canonical event history

All canonical changes must pass validation

All changes must cross the invariant boundary

Observers may simulate freely, but never define truth



---

⚙️ How CrypSA Works

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


---

📚 Documentation Guide

CrypSA documentation is structured by role:

Type	Purpose

Conceptual	Mental models and explanations
Architecture	System structure and boundaries
Spec	Authoritative runtime behavior
Example	Concrete walkthroughs
Diagram	Visual explanations (non-authoritative)
Exploratory	Non-final ideas


👉 Full structure: DOCS_STRUCTURE.md


---

🧭 Full Reading Path

If you want deeper understanding:

Foundation

CrypSA_In_One_Diagram.md

CrypSA_In_5_Minutes.md

CrypSA_Terminology_Primer.md


Motivation

CrypSA_Why_It_Exists.md


Example

CrypSA_Worked_Example.md


Architecture

architecture/


Runtime (Required for Implementation)

spec/


Implementation

implementation/



---

👥 Who This Is For

🧠 Learners

Start with:

CrypSA_In_5_Minutes.md

CrypSA_Worked_Example.md



---

⚙️ Implementers

Focus on:

spec/

minimal validator docs


The spec defines behavior — your implementation must follow it.


---

🧱 Contributors

Read:

terminology primer

architecture

spec


Follow:

do not redefine terminology

do not duplicate definitions

do not introduce behavior outside the spec



---

🚧 Project Status — v1.0

CrypSA v1.0 defines the core architecture and runtime model.

It is:

stable in its core concepts

consistent in terminology and structure

ready for implementation


Ongoing work includes:

reference implementations

documentation refinement


v1.0 is a stable architectural baseline, not a finished product.


---

🔢 Versioning Philosophy

v1.x → stable architecture, evolving implementations

v2.0 → breaking architectural changes



---

🧠 Why CrypSA Exists

Traditional systems:

Client → Server → State Sync

CrypSA:

Observer → Validation → Canonical Event History → Reconstruction

Instead of synchronizing state, it:

validates events

records canonical event history

reconstructs reality deterministically



---

🧩 Key Concepts

Validator

Canonical Events

Invariants

Observers

Lenses


See:

👉 CrypSA_Terminology_Primer.md


---

📁 Repository Structure

architecture/

spec/

implementation/

diagrams/

exploratory/

teaching/

atlas/



---

👤 Author

Beau Wells


---

One Sentence Summary

CrypSA defines how systems agree on truth through validated canonical events.