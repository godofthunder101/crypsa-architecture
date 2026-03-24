# CrypSA Teaching Prototype - Data Flow Diagram

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

---

## Purpose

This document shows how data moves through the CrypSA teaching prototype.

It complements `CrypSA_Teaching_Prototype_Layers.md` by focusing on:

* truth flow
* replay flow
* presentation flow
* intent flow

The goal is to make the prototype's architecture understandable at a glance.

For artifact status and maintenance posture, pair this with `STATUS.md`.

---

## Core Principle

The teaching prototype is built around two opposite flows:

* downward: truth becomes experience
* upward: user intent becomes validated canonical change

This demonstrates the CrypSA model, not a distributed production implementation.

---

## Full System Data Flow

```text
Canonical Event History
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI / Player Experience

UI Interaction
-> Typed Request
-> Request Dispatch
-> Controller Action Handling
-> Validation
-> Canonical Event Application
-> Canonical Event History
-> Replay
-> Derived Canonical State
```

---

## Downward Flow — Truth To Experience

```text
Canonical Event History
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI
```

This is the path by which accepted canonical history, replayed truth, and observer-local context become visible state and interaction options.

---

## Upward Flow — Intent To Truth

```text
UI Action
-> Typed Request
-> Request Dispatch
-> Controller Action Handling
-> Validation
-> Canonical Event Application
-> Canonical Event History
-> Replay
-> Derived Canonical State
```

This is the path by which user intent becomes accepted canonical truth or is rejected during validation.

---

## Boundary Emphasis

### Runtime / Controller

Owns coordination and execution of actions.
Does not directly define canonical truth.

---

### Replay

Owns derivation of canonical state from canonical event history.

---

### Adapters

Own data shaping.

---

### Lenses + Requests

Own interpretation and intent handoff.

---

### UI

Owns presentation and input.

---

### Mint

Owns authored definition structure.

Referenced during:

* validation
* replay

Not part of runtime data flow.

---

## Why This Matters

This structure makes it easier to:

* teach CrypSA clearly
* inspect canonical event history
* debug local vs canonical divergence
* evolve layers independently
* avoid runtime/UI coupling

---

## One Sentence Summary

The CrypSA teaching prototype turns canonical event history into observer experience through replay, adapters, lenses, and UI, while user intent flows upward through typed requests, controller handling, validation, and canonical event application.
