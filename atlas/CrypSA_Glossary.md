# CrypSA Glossary

## Purpose

This glossary defines the core terminology used throughout the CrypSA architecture.

These terms represent the **canonical vocabulary** of the system.

Definitions here should align with the architecture, spec, and implementation layers.

---

## Core Terms

### CrypSA

CrypSA (Cryptid Server Architecture) is a distributed architecture for persistent digital universes.

It synchronizes **validated canonical events** rather than full world state, allowing observers to reconstruct the universe locally.

---

### Universe

A Universe is the persistent system governed by CrypSA.

It consists of:

* canonical identities
* deterministic genomes
* invariant constraints
* canonical event history

---

### Observer

An Observer is any system that reconstructs and experiences the universe.

Examples include:

* player clients
* simulation nodes
* tools or analytics systems

Observers simulate locally while reconciling with canonical event history.

---

## Structural Concepts

### Canonical Object

A Canonical Object is an entity defined by:

* identity
* genome
* invariant-relevant state
* canonical event history

It can be reconstructed deterministically from canonical data.

---

### Identity

An Identity is a unique, immutable identifier for a canonical object.

---

### Genome

A Genome defines the deterministic structure and rules for a canonical object.

---

### Mint

The Mint is responsible for issuing identities and genomes.

It ensures:

* identity uniqueness
* deterministic structure
* reproducibility

---

## Truth Layer

### Canonical Event

A Canonical Event is a validated event that has been accepted into canonical event history.

---

### Canonical Event History

Canonical Event History is the ordered, append-only record of canonical events.

It defines how the universe evolves over time and is the source of truth.

---

### Invariant

An Invariant is a rule that must always remain valid within canonical event history.

---

### Invariant Boundary

The Invariant Boundary is where proposed actions are validated before becoming canonical events.

---

## Observer Concepts

### Local Simulation

Local Simulation is simulation performed by observers.

Examples:

* movement
* physics
* gameplay mechanics

It is not authoritative.

---

### Observer Convergence

Observer Convergence is the process by which observers align with canonical event history after updates.

---

## Translation Layer

### Adapter

An Adapter reshapes data between system layers without changing meaning.

---

## Interpretation Layer

### Lens

A Lens interprets canonical or translated data into observer-specific meaning.

---

### Lens Stack

A Lens Stack is a composition of lenses applied to produce interpretation.

---

## Experience Layer

### Experience

The Experience layer includes:

* UI
* input handling
* feedback systems

It represents how the observer interacts with the universe.

---

## Summary

CrypSA separates responsibilities into:

* **Truth** — canonical events and validation
* **Translation** — adapters
* **Interpretation** — lenses
* **Experience** — UI and simulation

This separation allows:

* deterministic reconstruction
* flexible observer behavior
* consistent shared reality derived from canonical event history
