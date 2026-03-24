# CrypSA FAQ

This document answers common questions about CrypSA.

It focuses on clarifying behavior, tradeoffs, and concerns — not teaching the system.

For a quick explanation, see:

* `CrypSA_In_5_Minutes.md`

For the authoritative adapter and observer-model docs, see:

* `architecture/CrypSA_Adaptor_Model.md`
* `architecture/CrypSA_Client_Observer_Model.md`

---

## What is CrypSA in simple terms?

CrypSA is an event-driven architecture where:

* clients simulate locally
* actions are proposed as events
* the server validates those events
* accepted events define shared reality

---

## Is CrypSA server authoritative?

Yes — but differently than traditional systems.

The server does not simulate everything.

Instead, it is authoritative over:

* which events are accepted
* what becomes canonical event history

---

## Does CrypSA trust the client?

No.

Clients can propose events, but:

* all canonical changes must be validated
* invalid or conflicting events are rejected

Clients have freedom to simulate, not authority to define truth.

---

## Then why give power to the client?

CrypSA separates:

* simulation (client-side)
* truth (server-side)

This allows:

* responsiveness
* flexibility
* reduced synchronization overhead

The server still controls what is real.

---

## Is this just event sourcing?

It is similar, but not identical.

CrypSA:

* is designed for interactive simulations
* includes invariant validation as a core system
* explicitly models observers and reconstruction

---

## Is CrypSA peer-to-peer?

No.

CrypSA requires a server to:

* validate events
* enforce invariants
* maintain canonical event history

---

## What does the server actually do?

The server:

* receives candidate events
* validates them
* enforces invariants
* records accepted events
* distributes canonical updates

It does not need to simulate the entire world continuously.

---

## What happens if two players act at the same time?

Both actions may be submitted.

The server:

* validates both
* accepts one
* rejects the other

The rejected observer reconciles to canonical state.

---

## What happens when the client is wrong?

If a client predicts incorrectly:

* the server rejects the event
* the observer corrects its local state

This is expected behavior.

---

## How does CrypSA prevent client-side logic from breaking the system?

CrypSA relies on strict separation of responsibilities:

* the server defines truth
* adapters shape data
* lenses interpret meaning
* UI presents the result

In addition:

* clients emit **typed requests** representing intent
* canonical changes occur only through validated events
* adapters prevent UI and lenses from accessing raw runtime structures

---

## Is CrypSA deterministic?

Yes, at the canonical level.

Given the same:

* canonical event history
* rules
* definitions

All observers must derive the same state via replay.

---

## Does CrypSA store world state?

Not as truth.

* canonical truth = canonical event history
* derived state = reconstructed via replay
* snapshots = reconstruction checkpoints

---

## What are snapshots?

Snapshots are stored derived state used to:

* speed up loading
* reduce replay cost
* support recovery

They do not replace canonical event history.

---

## Does CrypSA support real-time gameplay?

Yes, with tradeoffs.

Works best for:

* persistent worlds
* simulation systems
* object-driven interactions

Less suited for:

* twitch combat
* frame-perfect PvP
* heavy physics systems

---

## What is the current state of the project?

CrypSA is:

* a defined architecture
* supported by specifications
* backed by a teaching prototype

It is not yet a production system.

---

## Is the current prototype networked?

No.

It is a teaching tool designed to demonstrate:

* event flow
* validation
* canonical vs local state

It demonstrates the model, not runtime behavior.

---

## What is the difference between the prototype and the real system?

The teaching prototype:

* demonstrates the CrypSA model locally
* focuses on clarity and inspectability
* simplifies runtime constraints

The minimal server:

* will test CrypSA as a runtime system
* introduces networking and multi-observer interaction
* validates behavior under real constraints

---

## Can CrypSA scale?

Potentially, but not yet proven.

Scaling depends on:

* validation performance
* event distribution
* snapshot systems

---

## What are the biggest risks?

* validation complexity
* reconciliation challenges
* performance under load
* networking edge cases
* lack of production testing

---

## Why build CrypSA?

CrypSA explores a different approach:

> shared reality defined by history, not synchronized state

It aims to:

* enable persistent systems
* improve auditability
* simplify some multiplayer problems

---

## Where should I start?

1. `CrypSA_In_5_Minutes.md`
2. `CrypSA_Terminology_Primer.md`
3. `CrypSA_WORKED_EXAMPLE.md`

---

## One Sentence Summary

CrypSA is a system where clients simulate locally, servers validate events, and shared reality is defined by canonical event history.
