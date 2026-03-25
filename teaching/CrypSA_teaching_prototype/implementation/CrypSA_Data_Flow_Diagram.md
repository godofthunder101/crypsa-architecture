> Scope note: This document reflects the teaching prototype implementation at the time it was completed.
>
> It may not match the current CrypSA specification.
>
> The prototype is preserved as a teaching artifact and is not updated to reflect ongoing architectural changes.
>
> For current system behavior, refer to `../../../spec/`.

# CrypSA Teaching Prototype — Data Flow Diagram

> Scope note: This document describes the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

---

## Purpose

This document shows how data moves through the CrypSA teaching prototype.

It complements `CrypSA_Teaching_Prototype_Layers.md` by focusing on:

- truth flow
- replay flow
- presentation flow
- intent flow

The goal is to make the prototype's architecture understandable at a glance.

For artifact status and maintenance posture, pair this with `STATUS.md`.

---

## Core Principle

The teaching prototype is built around two opposing flows:

- downward: canonical event history becomes experience  
- upward: user intent becomes validated canonical events  

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
-> Controller / Runtime Action
-> Validation
-> Canonical Apply
-> Canonical Event History
-> Replay
````

---

## Downward Flow — Canonical Event History to Experience

```text
Canonical Event History
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI
```

This is the path by which accepted canonical event history becomes:

* reconstructed state
* interpreted meaning
* visible experience

---

## Upward Flow — Intent to Canonical Event History

```text
UI Action
-> Typed Request
-> Request Dispatch
-> Controller Mutation Path
-> Validation
-> Canonical Apply
-> Accepted Canonical Event
-> Canonical Event History
-> Replay
```

This is the path by which user intent becomes:

* a candidate event
* validated against invariants and rules
* accepted (or rejected)
* appended to canonical event history

---

## Boundary Emphasis

### Runtime / Controller

Owns:

* coordination
* mutation pathways
* candidate event creation

---

### Replay

Owns:

* reconstruction of derived canonical state
* deterministic application of canonical event history

---

### Adapters

Own:

* shaping canonical and observer data
* preparing lens-ready structures

---

### Lenses + Requests

Own:

* interpretation of meaning
* intent handoff back into the runtime

---

### UI

Owns:

* presentation
* input
* local feedback

---

### Mint

Owns:

* structural definitions
* genome and invariant schema inputs

---

## Why This Matters

This structure makes it easier to:

* teach CrypSA clearly
* inspect canonical event history
* debug local vs canonical divergence
* evolve layers independently
* avoid runtime/UI coupling

---

## Key Insight

> Canonical event history defines what has happened.
> Replay derives what currently exists.
> Everything else builds on top of that.

---

## One Sentence Summary

The CrypSA teaching prototype transforms canonical event history into observer experience through replay, adapters, lenses, and UI, while all user intent flows upward through typed requests, controller actions, validation, and canonical application into canonical event history.
