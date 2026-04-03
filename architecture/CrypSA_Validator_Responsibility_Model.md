# CrypSA Validator Responsibility Model

## Purpose

This document defines the role of the **validator** in a CrypSA system.

The validator is responsible for protecting the integrity of **canonical event history** by validating events, enforcing invariants, and maintaining that history.

---

## 📜 Specification Authority

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Core Principle

In CrypSA:

> The validator does not simulate the world.
> It controls what becomes real.

The validator acts as:

* an event validator
* an invariant enforcer
* a canonical event recorder

Observers simulate the world locally.
The validator ensures all accepted events are valid.

---

## Validator as a Role

In CrypSA, the validator is a **logical role**, not a specific machine.

It may run:

* **locally**, alongside an observer
* **remotely**, as a separate system

The responsibilities of the validator do not change based on where it runs.

> Validation defines canonical truth, regardless of deployment.

---

## Server (Deployment Term)

A **server** is a deployment of a validator that runs remotely.

Not all validators are servers, but all servers host a validator.

---

## Architectural Position

CrypSA separates responsibilities into:

* **Truth** → canonical events and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

The validator operates strictly in the **truth layer**.

It does not:

* simulate gameplay
* interpret meaning
* manage presentation

---

## The Validator Model

CrypSA replaces centralized simulation with **canonical event validation**.

Instead of computing the entire world, the validator:

1. receives candidate events
2. validates them
3. accepts or rejects them
4. appends accepted events to canonical event history

This is the minimal loop.

---

## Core Responsibilities

### 1. Event Acceptance

The validator receives **candidate events** from observers.

Examples:

* crafting
* upgrading
* transferring
* building

Each event represents **intent**, not truth.

---

### 2. Validation and Invariant Enforcement

The validator validates events against:

* object existence
* ownership rules
* invariant constraints
* rule compliance
* resource requirements

Invariants define what must always be true.

If an event violates invariants:

→ it is rejected
→ it never becomes canonical

---

### 3. Canonical Event Recording

Accepted events are appended to canonical event history.

This history defines:

* object creation
* state changes
* ownership changes
* world evolution

Canonical event history is the source of truth.

---

## Canonical Data Model

The validator’s persistent data consists of:

* object identities
* genome definitions (from the Mint)
* canonical event history
* invariant-relevant state
* optional snapshots

The system is **event-first**, not state-first.

---

## Minimal Runtime Flow (v0.1)

The minimal validator loop is:

1. receive request
2. parse into typed intent
3. validate against canonical context
4. accept or reject
5. append event if accepted
6. return result

This is sufficient to maintain shared reality.

---

## What the Validator Does NOT Do

The validator does not need to:

* simulate the full world
* run physics or AI continuously
* maintain large mutable world-state models
* render or predict gameplay

Observers handle simulation and experience.

---

## Optional Supporting Systems

Production systems may include:

### Auditing

* anomaly detection
* suspicious behavior tracking

### Security

* exploit detection
* rate limiting

### Performance

* snapshots
* caching
* indexing

### Analytics

* telemetry
* behavior analysis

These are optional and do not define the core model.

---

## Minimal Responsibilities

At minimum, a CrypSA validator must:

1. receive candidate events
2. validate them
3. enforce invariants
4. accept or reject
5. record canonical event history
6. expose canonical updates

---

## Validator vs Observer Responsibilities

| Responsibility           | Observer | Validator    |
| ------------------------ | -------- | ------------ |
| Canonical reconstruction | Yes      | Yes          |
| Local simulation         | Yes      | Not required |
| Translation (adapters)   | Yes      | Not required |
| Interpretation (lenses)  | Yes      | Not required |
| Event proposal           | Yes      | No           |
| Event validation         | No       | Yes          |
| Invariant enforcement    | No       | Yes          |
| Canonical recording      | No       | Yes          |
| Rendering                | Yes      | No           |
| Truth authority          | No       | Yes          |

---

## Deployment Independence

The validator’s behavior is independent of deployment.

Whether the validator runs:

* locally (within an observer environment)
* remotely (as a dedicated server)

The following remain unchanged:

* validation rules
* invariant enforcement
* canonical event semantics
* definition of truth

What changes is:

* where validation executes
* how observers communicate with the validator

---

## Summary

The CrypSA validator is the **guardian of canonical event history**.

It:

* validates events
* enforces invariants
* records canonical events

Observers simulate and interpret the world locally.

---

## Key Idea

The CrypSA validator is not a simulation engine.

It is a **canonical event acceptance system** that determines what is allowed to become real.
