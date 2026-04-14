# CrypSA Validator Deployment Model

## Purpose

This document defines how the **validator role** in CrypSA can be deployed.

Validator behavior within the system is defined in the runtime model:

→ CrypSA_Runtime_Model.md

CrypSA treats validation as an **architectural responsibility**, not a fixed machine location.

This allows the same system model to operate across different deployment styles without changing how canonical truth is defined.

---

## 📜 Authority Level

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Core Principle

> The validator defines canonical truth, regardless of where it runs.

Validation determines:

* whether candidate events are accepted or rejected
* what becomes part of canonical event history
* the canonical ordering (`canonical_sequence`)
* what is considered real within the universe

This responsibility does not change based on deployment.

---

## Validator as a Role

In CrypSA, the validator is a **logical role**, not a specific system.

It is responsible for:

* validation
* invariant enforcement
* canonical event recording
* making canonical events available to observers

The validator is **not defined by being a server**.

A server is a deployment of a validator, not the source of authority itself.

---

## Deployment Models

CrypSA supports multiple validator deployment models.

These models differ in **where the validator runs**, not in **how validation behaves**.

---

### 1. Local-Only Validation

In this model:

* the validator runs alongside the observer
* no external system is required
* the system can operate fully offline

#### Characteristics

* single observer (or isolated environment)
* no shared canonical event history across multiple observers
* validation and simulation occur within the same environment, but remain logically separate

#### Benefits

* simple architecture
* ideal for development and testing
* supports offline-first systems
* resilient to network interruption

#### Important Note

Even in this model:

> the validator remains a separate logical role

The invariant boundary still applies.

---

### 2. Host-Based Validation

In this model:

* one observer (the host) runs the validator
* other observers connect to it
* the host acts as the canonical authority

#### Characteristics

* shared canonical event history
* no dedicated external system required
* connected observers rely on host validation

#### Benefits

* lower infrastructure requirements
* suitable for small-scale multiplayer
* easier to set up than dedicated deployments

#### Tradeoffs

* host becomes a single point of failure
* authority is tied to a player-controlled system
* potential trust and fairness concerns

---

### 3. Dedicated Remote Validator

In this model:

* the validator runs as a separate system
* observers connect over a network
* canonical truth is maintained independently of any single observer

#### Characteristics

* shared canonical event history across observers
* supports persistent universes
* independent of any single observer

#### Benefits

* stable canonical authority
* suitable for large-scale or persistent systems
* clearer separation between observer and truth

#### Tradeoffs

* requires infrastructure
* network dependency
* increased system complexity

---

## Relationship Between Models

These deployment models are not separate architectures.

They are different **configurations of the same architecture**.

A system may transition between them:

```text id="7m2d1k"
Local → Host-Based → Dedicated Remote
```

This progression allows:

* development to begin locally
* multiplayer to be introduced incrementally
* infrastructure to scale over time

---

## Invariant Boundary Consistency

Across all deployment models:

* the invariant boundary remains intact
* validation rules remain unchanged
* canonical event history remains the source of truth

What changes is:

* where validation executes
* how observers receive canonical events from the validator

What does not change is:

> how truth is defined

---

## Observer Relationship

Observers always:

* simulate locally
* propose candidate events
* reconcile with canonical outcomes

Regardless of deployment:

* observers do not define truth
* validation defines truth

---

## Local-First Design Insight

CrypSA naturally supports a **local-first development model**.

Because the validator is a role (not a location):

* systems can begin with a local validator
* offline operation works from the start
* transitioning to multiplayer does not require architectural changes

This enables a powerful development flow:

```text id="n2qk9z"
Local Development → Host-Based Multiplayer → Dedicated Deployment
```

Where each step:

* preserves the same validation model
* preserves canonical event history behavior
* requires only deployment changes, not system redesign

See:

```
implementation/CrypSA_Local_First_Development_Approach.md
```

---

## Key Insight

> Deployment changes where validation runs, not what validation means.

---

## Summary

CrypSA supports multiple validator deployment models:

* local-only validation
* host-based validation
* dedicated remote validation

These models differ in deployment, not in behavior.

> Validation defines canonical truth.
> Deployment defines where validation runs.
