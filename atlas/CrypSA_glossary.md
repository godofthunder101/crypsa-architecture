---

CrypSA Glossary

Purpose

The CrypSA Glossary defines the core terminology used throughout the CrypSA architecture documentation.

Because CrypSA introduces several concepts that differ from traditional multiplayer architectures, consistent terminology is important for clear communication between developers, researchers, and implementers.

The terms defined here represent the canonical vocabulary of the CrypSA architecture.


---

Core Architectural Terms

CrypSA

CrypSA (Cryptid Server Architecture) is a distributed architecture for persistent digital universes.

Instead of synchronizing full world simulation state, CrypSA synchronizes canonical invariants and validated event history, allowing observers to reconstruct the universe locally.


---

Universe

A Universe is the persistent canonical structure governed by the CrypSA architecture.

It consists of:

minted identities

deterministic genomes

canonical invariant state

canonical event history


Observers experience the universe through local reconstruction.


---

Observer

An Observer is any system that reconstructs and experiences the universe.

Observers may include:

player clients

simulation nodes

analytics systems

automated agents


Observers simulate locally while respecting canonical invariants.


---

Observer Frame

An Observer Frame is the local context through which an observer experiences the universe.

It includes:

local simulation

lens interpretation

temporary phenomena

observer-relative state


Observer frames may differ between observers while still referencing the same canonical universe.


---

Structural Concepts

Canonical Object

A Canonical Object is a structural entity that exists within the universe.

Canonical objects are defined by:

identity

genome

invariant state

event history


These properties allow deterministic reconstruction.


---

Identity

An Identity is the immutable identifier assigned to a canonical object.

Identities ensure that observers refer to the same structural entity even when interpreted differently.


---

Genome

A Genome is the deterministic rule set that defines how a canonical object behaves and how its structure can be reconstructed.

Genomes may include:

generative parameters

behavioral rules

structural relationships



---

Mint

The Mint is the system responsible for issuing canonical identities and genomes.

It defines the structural existence of entities within the universe.

The Mint guarantees:

identity uniqueness

deterministic generation

structural reproducibility



---

Canonical Truth

Canonical Truth

Canonical Truth represents the shared structural reality of the universe.

It consists of:

canonical objects

invariant state

canonical event history


Observers reconstruct their experience using this information.


---

Invariant

An Invariant is a property of the universe that must remain globally consistent across observers.

Examples may include:

world structures

resource thresholds

discovery states

historical milestones


Actions that affect invariants must be validated.


---

Invariant Boundary

The Invariant Boundary separates observer-local simulation from canonical world changes.

Interactions that cross this boundary generate canonical events.


---

Event System

Canonical Event

A Canonical Event represents a validated change to shared world truth.

Canonical events are appended to the universe’s event history after validation.


---

Event History

The Event History is the chronological record of canonical events that have occurred in the universe.

Event history allows:

deterministic reconstruction

temporal replay

historical analysis



---

Event Reconciliation

Event Reconciliation is the process by which the server validates canonical events and updates invariant state.

The reconciliation system ensures that canonical truth remains consistent.


---

Interpretation System

Lens

A Lens is a modular interpretation layer that determines how canonical objects are perceived and interacted with by observers.

Lenses may modify:

visible properties

gameplay interactions

system behaviors

informational visibility



---

Lens Stack

A Lens Stack is a layered combination of lenses applied to an observer frame.

Example lens stack:

Observer Frame
   ↓
Gameplay Lens
   ↓
Economy Lens
   ↓
Discovery Lens
   ↓
Canonical Object


---

Simulation Concepts

Local Simulation

Local Simulation refers to simulation performed by observers within their own observer frame.

Examples include:

physics prediction

visual effects

temporary interactions

gameplay mechanics


Local simulation may vary between observers.


---

Observer Convergence

Observer Convergence refers to the process by which observers eventually align with canonical truth after receiving validated events.


---

Validation Concepts

Contextual Event Validation

Contextual Event Validation is a CrypSA validation approach where events are verified using surrounding context rather than immediate full-state verification.

This may include examining:

recent event trails

invariant changes

structural balance



---

Event Trail

An Event Trail is the contextual chain of related actions surrounding a canonical event.

Event trails may be used for anomaly detection or delayed validation.


---

Quarantine State

A Quarantine State is a provisional state applied to objects or events that require further validation.

During quarantine:

the object may appear usable

the system may perform background verification

anomalies may be investigated without disrupting observers



---

System Philosophy

Structural Reality

Structural Reality refers to the canonical universe defined by identities, genomes, invariants, and event history.


---

Experiential Reality

Experiential Reality refers to the observer’s interpreted experience of the universe through lenses and local simulation.


---

Summary

CrypSA separates the universe into two interacting layers:

Structural Reality

and

Observer Experience

The Mint defines what exists.
Canonical events define how the universe changes.
Lenses define how the universe is experienced.

Observers reconstruct reality locally while the system protects canonical truth.


---


