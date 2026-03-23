# CrypSA Architecture Atlas

## Purpose

The CrypSA Architecture Atlas provides a structured overview of the CrypSA conceptual model and documentation corpus.

It acts as a **navigation layer**, helping readers understand:

* how the system is structured
* how components relate
* where to find authoritative definitions

This document does not redefine concepts.
It organizes them.

---

## Core Idea

CrypSA describes how persistent digital universes can be built using:

* canonical events
* invariant validation
* observer-side simulation

Rather than synchronizing world state, CrypSA synchronizes:

> validated canonical events

---

## Architectural Model

CrypSA separates responsibilities into four layers:

* **Truth** — canonical events and validation
* **Translation** — adapters shaping data
* **Interpretation** — lenses defining meaning
* **Experience** — UI and local simulation

These layers describe how the system is structured.

---

## System Overview

At a high level:

* the **server** operates in the truth layer
* the **observer** operates across translation, interpretation, and experience
* canonical events define shared reality
* observers reconstruct and simulate locally

---

## Core Concepts

The following concepts are defined in dedicated documents:

### Mint

Defines valid object structure and identity.

### Canonical Events

Define how the universe changes.

### Invariants

Define what must always remain true.

### Canonical Objects

Defined by identity, genome, and event history.

### Observers

Reconstruct and simulate the world locally.

### Adapters

Translate data between layers.

### Lenses

Interpret canonical reality into observer experience.

---

## System Behavior

The system operates as:

* observers propose candidate events
* the server validates them
* accepted events become canonical
* observers reconstruct updated reality

For detailed behavior, see `../spec/`.

---

## Documentation Structure

CrypSA documentation is organized into:

### Architecture (`architecture/`)

Defines system structure and responsibilities.

### Specification (`spec/`)

Defines runtime behavior and rules.

### Implementation (`implementation/`)

Describes how to build CrypSA systems.

### Teaching (`teaching/`)

Demonstrates concepts through examples and prototypes.

### Exploratory (`exploratory/`)

Contains non-authoritative or experimental ideas.

---

## Relationship Between Documents

* Architecture defines structure
* Spec defines behavior
* Implementation defines how to build
* Teaching demonstrates the system
* Exploratory extends ideas

Each concept should be defined authoritatively in only one place.

---

## Evolution

CrypSA is an evolving architecture.

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

The server protects truth.
Observers simulate and interpret locally.
Canonical events define the shared universe.
