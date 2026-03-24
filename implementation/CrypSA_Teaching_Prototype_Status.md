# CrypSA Teaching Prototype — Status

> Scope note: This document summarizes the teaching prototype from the implementation-direction layer.
>
> For authoritative prototype status, refer to `../teaching/CrypSA_teaching_prototype/STATUS.md`.

---

## Purpose

This document clarifies the role and status of the CrypSA teaching prototype within the repository.

It exists to ensure the prototype is understood correctly and not misinterpreted as a production runtime.

---

## What This Prototype Is

The CrypSA teaching prototype is:

* a completed teaching artifact
* a structured, inspectable implementation of the CrypSA model
* designed to demonstrate how core concepts interact in a live system

It demonstrates:

* canonical event history as the source of truth
* validation against invariants
* state derived from canonical event history (via replay)
* observer-side simulation and observer reconciliation
* separation of truth, translation, interpretation, and experience
* adapter and request boundaries in practice

Its goal is to make the architecture understandable and tangible.

---

## What This Prototype Is Not

This prototype is not:

* a production runtime
* a distributed or networked system
* a scalability or performance proof
* a final reference implementation of CrypSA

It simplifies or omits:

* networking and transport layers
* concurrency and multi-client synchronization
* large-scale performance concerns
* security and adversarial validation

Important:

> This prototype does not include an independent server or real networked authority.

---

## Current Status

Status: **Complete for its intended purpose**

The prototype:

* fulfills its teaching goals
* reflects the CrypSA model in a local teaching context
* has been refined to a stable and consistent state

It is now:

> frozen except for bug fixes and documentation updates

---

## Why It Is Not Being Extended Further

Continuing to evolve this prototype would:

* blur its role as a teaching artifact
* introduce complexity unrelated to its purpose
* risk collapsing clear architectural boundaries

Instead:

> new ideas and experiments should be explored in separate programs or prototypes

---

## Relationship to the CrypSA Architecture

This prototype demonstrates the architecture locally.

It maps to the core model:

| Responsibility | Demonstrated In                                                 |
| -------------- | --------------------------------------------------------------- |
| Truth          | canonical event history, validation, derived state (via replay) |
| Translation    | adapters                                                        |
| Interpretation | lenses                                                          |
| Experience     | UI and local simulation                                         |

This makes it a useful reference for understanding how the system is structured.

---

## Relationship to Future Work

The next phase of CrypSA is not to extend this prototype.

Instead, future work should focus on:

* building a minimal server/runtime
* testing distributed behavior
* validating synchronization and transport models
* exploring multi-observer and network scenarios

These should be implemented as **separate programs**, not as extensions of this teaching prototype.

---

## How to Use This Prototype

Use this prototype to:

* understand the CrypSA model
* explore canonical event flow
* inspect replay and derived state
* experiment with local simulation and observer reconciliation
* study adapter and lens boundaries

Do not use it as:

* a production base
* a performance benchmark
* a complete runtime reference

---

## Summary

The CrypSA teaching prototype is a completed, stable teaching artifact that demonstrates the architecture in a local, inspectable system.

It is not a production runtime and will not be extended further; future CrypSA development will occur in separate programs.
