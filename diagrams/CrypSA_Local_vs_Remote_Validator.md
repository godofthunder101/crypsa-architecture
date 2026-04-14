# CrypSA Local vs Remote Validator

## Purpose

This diagram shows two valid deployment models for the CrypSA validator role.

The key idea is:

> the validator is a role, not a location

CrypSA can operate with validation running:

* locally, within the observer environment
* remotely, as a separate system

This is a deployment distinction, not a change to the truth model.

For the authoritative conceptual flow of the system, see:

→ ../architecture/CrypSA_Runtime_Model.md

---

## Core Principle

In both models:

* candidate events are evaluated by a validator
* accepted events become canonical
* canonical event history defines truth

What changes is:

* where the validator runs
* how the observer communicates with it

What does **not** change is:

> how canonical truth is defined

---

## Diagram

> This diagram illustrates deployment configurations within the CrypSA runtime model.
> It does not define runtime behavior or event flow.
> For the authoritative conceptual flow, see:
> → ../architecture/CrypSA_Runtime_Model.md

```mermaid
flowchart TB

subgraph Case_A["Case A - Local Validator"]
    A1[Observer]
    A2[Validator]
    A3[Canonical Event History]
    A1 --> A2
    A2 --> A3
end

subgraph Case_B["Case B - Remote Validator"]
    B1[Observer]
    B2[Network]
    B3[Validator]
    B4[Canonical Event History]
    B1 --> B2
    B2 --> B3
    B3 --> B4
end
````

---

## How to Read This

### Case A — Local Validator

In this model:

* the observer and validator run in the same environment
* validation still occurs
* canonical event history is still protected

This is useful for:

* offline or single-observer operation
* development and testing
* local-first system design

Even here:

> the validator remains a separate logical role

The invariant boundary still exists.

---

### Case B — Remote Validator

In this model:

* the observer communicates over a network
* the validator runs as a separate system
* canonical event history is maintained remotely

This is useful for:

* shared worlds
* persistent multiplayer systems
* centralized canonical authority

A remote validator is what CrypSA refers to as a **server deployment**.

---

## What This Demonstrates

This diagram exists to clarify that CrypSA does **not** require a permanently remote validator in order to preserve its core model.

Both deployment forms support the same architecture:

* observers simulate locally
* candidate events cross the invariant boundary
* the validator determines what becomes canonical

---

## Relationship to the Rest of CrypSA

This diagram supports:

* `CrypSA_Terminology_Primer.md`
* `architecture/CrypSA_Validator_Deployment_Model.md`
* `spec/CrypSA_Runtime_Spec_v0.1.md`

It is illustrative, not authoritative.

---

## Key Insight

> Local validator and remote validator are different deployments of the same role.

CrypSA keeps the truth model stable across both.

---

## One Sentence Summary

CrypSA supports both local and remote validator deployments, but in both cases the validator remains the role that determines what becomes canonical truth.
