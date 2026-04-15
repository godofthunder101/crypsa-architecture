# 🧠 CrypSA Reviewer Guide

This document provides important context for reviewing the CrypSA repository.

Reading this ensures the project is evaluated using the correct expectations.

---

## What CrypSA Is

CrypSA is an **architecture model**, not a framework, library, or complete product.

It defines:

* how truth is established
* how events become canonical through validation
* how state is derived
* how systems remain replayable and consistent

It does **not** provide:

* a full implementation
* a fixed runtime design
* a required networking model

---

## What to Evaluate

This repository should be evaluated on:

* clarity of the architecture
* internal consistency of terminology
* correctness of the runtime model
* alignment between spec, architecture, and implementation guidance
* ability to support real system implementation

---

## What Not to Evaluate

This repository is **not intended to be judged** on:

* amount of production code
* completeness of a runnable system
* presence of a full framework or SDK
* performance optimizations

The goal of this repo is **architectural correctness**, not implementation completeness.

---

## Source of Truth

👉 The `/spec` directory defines authoritative runtime behavior.

* If any document appears inconsistent:
  → the spec is correct
* Architecture documents define structure
* Implementation documents provide guidance

---

## How to Read the Repository

CrypSA is **layered**, not linear.

Recommended entry path:

1. `CrypSA_In_One_Diagram.md`
2. `CrypSA_In_5_Minutes.md`
3. `CrypSA_Terminology_Primer.md`
4. `CrypSA_Worked_Example.md`

Then:

* `architecture/` → system structure
* `spec/` → authoritative behavior
* `implementation/` → how to build

---

## Core Concepts to Understand

### Validator

The validator is a **role**, not a location.

* it may run locally or remotely
* it defines what becomes canonical

👉 The validator defines what becomes canonical and therefore controls canonical truth.

---

### Canonical Event History

> Canonical event history is the source of truth

* it is append-only
* all state is derived from it

---

### Canonical Lifecycle

> If accepted, an event becomes canonical and is appended to canonical event history

This is the core rule of the system.

---

### Replay

Replay is a required mechanism.

* derived canonical state is reconstructed via replay
* replay must be deterministic

---

### Observers

Observers:

* perform local prediction
* propose candidate events
* reconcile to canonical state

They do **not define truth**.

---

## Design Philosophy

CrypSA separates:

* **what must be true** (invariants)
* **how systems are built** (design space)

This means:

* invariants are strict
* implementation choices are flexible

Flexibility is **intentional**, not a lack of definition.

---

## Current Project State

This repository is:

* **architecturally complete**
* **spec-complete**
* **implementation-ready (with minimal validator as the first execution step)**

The next step is:

👉 building the minimal validator

---

## Key Insight

CrypSA does not synchronize state.

> It synchronizes validated events.

---

## One Sentence Summary

CrypSA is an architecture model where a validator determines what becomes canonical, canonical event history is the source of truth, and derived canonical state is reconstructed via deterministic replay.
