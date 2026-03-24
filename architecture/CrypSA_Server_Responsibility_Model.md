# CrypSA Server Responsibility Model

## Purpose

This document defines the role of the server in a CrypSA system.

The server is responsible for protecting the integrity of **canonical event history** by validating events, enforcing invariants, and maintaining that history.

---

## Core Principle

In CrypSA:

> The server does not simulate the world.
> It controls what becomes real.

The server acts as:

* an event validator
* an invariant enforcer
* a canonical event recorder

Observers simulate the world locally.
The server ensures all accepted events are valid.

---

## Architectural Position

CrypSA separates responsibilities into:

* **Truth** → canonical events and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

The server operates strictly in the **truth layer**.

It does not:

* simulate gameplay
* interpret meaning
* manage presentation

---

## The Server Model

CrypSA replaces centralized simulation with **canonical event validation**.

Instead of computing the entire world, the server:

1. receives candidate events
2. validates them
3. accepts or rejects them
4. appends accepted events to canonical event history

This is the minimal loop.

---

## Core Responsibilities

### 1. Event Acceptance

The server receives **candidate events** from observers.

Examples:

* crafting
* upgrading
* transferring
* building

Each event represents **intent**, not truth.

---

### 2. Validation and Invariant Enforcement

The server validates events against:

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

The server’s persistent data consists of:

* object identities
* genome definitions (from the Mint)
* canonical event history
* invariant-relevant state
* optional snapshots

The system is **event-first**, not state-first.

---

## Minimal Runtime Flow (v0.1)

The minimal server loop is:

1. receive request
2. parse into typed intent
3. validate against canonical context
4. accept or reject
5. append event if accepted
6. return result

This is sufficient to maintain shared reality.

---

## What the Server Does NOT Do

The server does not need to:

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

At minimum, a CrypSA server must:

1. receive candidate events
2. validate them
3. enforce invariants
4. accept or reject
5. record canonical event history
6. expose canonical updates

---

## Server vs Client Responsibilities

| Responsibility           | Client | Server       |
| ------------------------ | ------ | ------------ |
| Canonical reconstruction | Yes    | Yes          |
| Local simulation         | Yes    | Not required |
| Translation (adapters)   | Yes    | Not required |
| Interpretation (lenses)  | Yes    | Not required |
| Event proposal           | Yes    | No           |
| Event validation         | No     | Yes          |
| Invariant enforcement    | No     | Yes          |
| Canonical recording      | No     | Yes          |
| Rendering                | Yes    | No           |
| Truth authority          | No     | Yes          |

---

## Summary

The CrypSA server is the **guardian of canonical event history**.

It:

* validates events
* enforces invariants
* records canonical events

Observers simulate and interpret the world locally.

---

## Key Idea

The CrypSA server is not a simulation engine.

It is a **canonical event acceptance system** that determines what is allowed to become real.
