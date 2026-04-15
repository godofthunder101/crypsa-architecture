# CrypSA — Overview

This document provides a **conceptual explanation** of CrypSA.

It is intended as the primary reference for understanding:

* what CrypSA is
* how it works at a high level
* the core ideas behind the architecture

---

## 📜 Authority Level

This document is **non-authoritative**.

It explains the system conceptually.

👉 For authoritative runtime behavior, see:

* `/spec`

---

## Purpose

This document exists to:

* explain CrypSA clearly without implementation detail  
* establish the mental model required to understand the system  
* provide a single, cohesive explanation of the architecture  

---

## What CrypSA Is

CrypSA is an **architecture model** for building systems where:

👉 **truth is established through validated events**

Instead of synchronizing state across systems:

👉 CrypSA synchronizes **validated canonical events**

---

## Core Idea

In traditional systems:

* state is updated directly  
* systems try to stay in sync  

In CrypSA:

* systems propose **candidate events**  
* a validator determines whether those events are accepted  
* accepted events become **canonical**  
* all systems derive state from those canonical events  

---

## Core Principles

### 1. The Validator Defines Canonical Truth

The validator is responsible for:

* accepting or rejecting events  
* enforcing invariants  
* determining what becomes canonical  

👉 Truth is not assumed—it is **validated**

---

### 2. Canonical Event History Is the Source of Truth

Truth is not stored as state.

It exists only as:

👉 **an ordered sequence of canonical events**

This sequence is:

* append-only  
* immutable  
* authoritative  

---

### 3. State Is Derived, Not Stored as Truth

All state in CrypSA is:

* derived from canonical event history  
* reconstructable through replay  
* non-authoritative  

👉 State is a **projection of truth**, not truth itself

---

### 4. Replay Is Fundamental

Systems reconstruct state by:

👉 replaying canonical event history

This enables:

* deterministic reconstruction  
* debugging and inspection  
* consistency across observers  

---

### 5. Observers Simulate Locally

Observers:

* simulate the system locally  
* perform prediction  
* provide responsiveness  

But:

👉 Observers do not define truth  

---

### 6. The Invariant Boundary Protects Truth

All events must pass through:

👉 the **invariant boundary**

Where:

* rules are enforced  
* invalid events are rejected  
* canonical history is protected  

---

## High-Level Flow

At a high level, CrypSA operates like this:

1. An observer performs a local action  
2. The observer creates a candidate event  
3. The event is submitted to the validator  
4. The validator checks invariants  
5. If accepted:
   * the event becomes canonical  
   * it is appended to canonical event history  
6. Observers:
   * replay the updated history  
   * reconcile their local state  

---

## Key Concepts

### Validator
Defines canonical truth by validating events.

---

### Observer
Simulates locally and proposes candidate events.

---

### Canonical Event History
The append-only log that defines truth.

---

### Derived Canonical State
The reconstructed system state produced by replay.

---

### Invariants
Rules that determine whether events are valid.

---

### Replay
The process of reconstructing state from canonical history.

---

## What CrypSA Does NOT Define

CrypSA intentionally does not define:

* networking model  
* client/server structure  
* storage strategy  
* prediction systems  
* reconciliation strategy  
* UI or rendering  

👉 These are **implementation decisions**

---

## What CrypSA Defines

CrypSA defines:

* how events become canonical  
* how truth is established  
* how state is derived  
* how systems remain consistent  

---

## Why CrypSA Exists

CrypSA is designed to solve problems related to:

* consistency across distributed systems  
* replayability and debugging  
* authority and validation  
* synchronization complexity  

By shifting from:

👉 state synchronization  
to  
👉 **event validation + replay**

---

## Summary

CrypSA is an architecture where:

* truth is defined by validated events  
* canonical event history is the source of truth  
* state is derived through replay  
* observers simulate locally  
* invariants protect canonical truth  

And most importantly:

> Reality is not synchronized — it is agreed upon through validated events.
