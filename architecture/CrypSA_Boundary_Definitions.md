# CrypSA Boundary Definitions

## Purpose

This document defines the critical conceptual boundaries in CrypSA.

These boundaries prevent:

* responsibility overlap
* architectural drift
* ambiguity in system design

They reinforce how different parts of the system relate to each other.

For the authoritative conceptual flow of the system, see:

→ CrypSA_Runtime_Model.md

---

## 📜 Authority Level

This document defines conceptual boundaries between system responsibilities.

It does not define runtime behavior or validation rules.

The CrypSA documentation is structured as:

* `/spec` — authoritative definition of runtime behavior
* `/architecture` — system structure and conceptual models

If there is any conflict:

* spec takes precedence over architecture
* architecture takes precedence over this document

---

# Core Boundaries

---

## Adapter vs Lens

### Adapter

An **adapter**:

* reshapes data
* bridges systems
* combines canonical and observer data
* prepares structured outputs

An adapter does:

* transform structure
* organize data for consumption

An adapter does not:

* define meaning
* interpret data
* modify canonical truth

---

### Lens

A **lens**:

* interprets data
* defines meaning
* determines visibility and interaction relevance
* produces observer-specific views

A lens does:

* assign meaning to structured data
* shape observer experience

A lens does not:

* alter canonical structure
* define canonical truth
* perform validation

---

### Boundary Summary

> Adapters shape data.  
> Lenses define meaning.

---

## Observer vs Validator

### Observer

An **observer**:

* performs local simulation
* produces prediction
* handles UI and experience
* proposes candidate events

An observer:

* is responsive and immediate
* may diverge temporarily from canonical truth

An observer does not:

* define truth
* modify canonical event history directly

---

### Validator

The **validator**:

* evaluates candidate events
* enforces invariants
* determines acceptance or rejection
* appends accepted events to canonical event history
* assigns `canonical_sequence`

The validator:

* defines what becomes canonical
* operates as the authority of truth

The validator does not:

* simulate the world
* provide observer experience

---

### Boundary Summary

> Observers simulate.  
> The validator defines what becomes canonical.

---

## Canonical vs Local State

### Canonical

Canonical state is:

* derived from canonical event history
* authoritative
* consistent across observers
* reconstructable via replay

Canonical state:

* is derived from canonical event history
* is not a source of truth
* exists as a computed result of canonical events

---

### Local

Local state is:

* observer-specific
* predicted
* responsive
* potentially divergent

Local state:

* may temporarily differ from canonical outcomes
* must reconcile when canonical events are received

---

### Boundary Summary

> Canonical state is authoritative.  
> Local state is predictive.

---

## Invariant Boundary

The **invariant boundary** separates:

* local simulation
* canonical truth

At this boundary:

* candidate events are evaluated
* invariants are enforced
* acceptance determines canonical impact

---

### Boundary Summary

> The invariant boundary determines whether an action remains local or must be validated.

---

## Validation vs Simulation

### Simulation

Simulation:

* occurs locally in observers
* produces immediate results
* is not authoritative

---

### Validation

Validation:

* occurs in the validator
* determines canonical truth
* enforces invariants and rules

---

### Boundary Summary

> Simulation proposes.  
> Validation decides.

---

# Why These Boundaries Matter

These boundaries ensure:

* clear separation of responsibilities
* predictable system behavior
* easier debugging and reasoning
* prevention of architectural drift

They allow CrypSA to maintain:

* local responsiveness
* shared canonical truth
* deterministic reconstruction

---

# One Sentence Summary

CrypSA enforces strict boundaries between data shaping, interpretation, simulation, and validation so that only validated events become canonical, while observers remain responsive and locally predictive.
