# CrypSA Architecture Atlas

## Purpose

The CrypSA Architecture Atlas provides a structured overview of the CrypSA conceptual model and documentation corpus.

It acts as a **navigation layer**, helping readers understand:

* how the system is structured
* how components relate
* where to find authoritative definitions

This document does not redefine concepts.
It organizes them.

This document is non-authoritative and should not be used to define system behavior.

---

## Core Idea

CrypSA describes how persistent digital universes can be built using:

* canonical events
* invariant validation
* observer-side simulation

Rather than synchronizing world state, CrypSA synchronizes:

> validated canonical events forming canonical event history (ordered via `canonical_sequence`)

---

## Architectural Model

CrypSA separates responsibilities into four layers:

* **Truth** — canonical event history and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local simulation

These layers describe how the system is structured.

---

## System Overview

At a high level:

* the **validator** operates in the truth layer
* the **observer** operates across translation, interpretation, and experience
* canonical event history defines shared reality
* observers reconstruct and simulate locally

The validator determines what becomes canonical truth.

This role is **deployment-independent**:

* it may run locally alongside an observer
* or remotely as a shared system

Its responsibilities do not change based on where it runs.

---

## Core Concepts

The following concepts are defined in dedicated documents:

### Mint

Defines valid object structure and identity (see Terminology Primer).

---

### Canonical Events

Define how the universe changes.

---

### Invariants

Define what must always remain true.

---

### Canonical Objects

Defined by identity, genome, and event history.

---

### Observers

Reconstruct and simulate the world locally.

---

### Validator

Determines whether candidate events become canonical.

Responsible for:

* validation
* invariant enforcement
* canonical event recording

See: Terminology Primer and Runtime Spec.

---

### Adapters

Translate data between layers.

---

### Lenses

Interpret canonical reality into observer experience.

---

## System Behavior

The system operates as:

* observers propose candidate events
* the validator evaluates them
* accepted events become canonical (assigned `canonical_sequence`)
* observers reconstruct updated reality

For detailed behavior, see `../spec/`.

---

## Documentation Structure

CrypSA documentation is organized into:

### Architecture (`architecture/`)

Defines system structure and responsibilities.

---

### Specification (`spec/`)

Defines runtime behavior and rules.

---

### Implementation (`implementation/`)

Describes how to build CrypSA systems.

---

### Teaching (`teaching/`)

Demonstrates concepts through examples and prototypes.

---

### Exploratory (`exploratory/`)

Contains non-authoritative or experimental ideas.

---

## Relationship Between Documents

* Architecture defines structure
* Spec defines behavior
* Implementation defines how to build
* Teaching demonstrates the system
* Exploratory extends ideas

Each concept must be defined authoritatively in only one place.

---

## Evolution

CrypSA is a stable architecture that will continue to evolve.

Future work may expand:

* validation strategies
* simulation models
* persistence techniques
* tooling and debugging systems

The Atlas will evolve to reflect these changes.

---

## Summary

CrypSA enables persistent digital universes by separating:

* canonical truth
* observer simulation
* interpretation
* experience

The validator protects truth.
Observers simulate and interpret locally.
Canonical event history defines the shared universe.
