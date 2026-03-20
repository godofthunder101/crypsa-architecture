# CrypSA FAQ

This document answers common questions about CrypSA (Cryptid Server Architecture).

---

## What is CrypSA in simple terms?

CrypSA is an event-driven architecture where:

- players (observers) simulate the world locally  
- actions become candidate events  
- the server validates those events  
- accepted events form canonical history  
- the world is reconstructed from that history  

---

## Is CrypSA server authoritative?

Yes — but in a different way than traditional systems.

Traditional servers:
- simulate the world directly

CrypSA servers:
- validate events
- enforce invariants
- define canonical truth

The server is authoritative over:
- what events are accepted
- what becomes part of history

---

## Does CrypSA trust the client?

No.

Clients can propose events, but:

- all canonical changes must be validated  
- invalid or conflicting events are rejected  
- invariants enforce correctness  

The client has **freedom to simulate**, not authority to define truth.

---

## Then why give so much power to the client?

Because CrypSA separates:

- **simulation (client-side)**  
from  
- **truth (server-side)**  

This allows:

- smoother local responsiveness  
- flexible rendering and interpretation  
- reduced need for full state synchronization  

The server still controls what is real.

---

## Is this just event sourcing?

CrypSA is similar to event sourcing, but not identical.

Similarities:
- event log as source of truth  
- state derived from events  
- replayable history  

Differences:
- built specifically for interactive simulations and games  
- includes invariant validation as a core system  
- explicitly models observers and reconstruction  
- allows client-side simulation before validation  

---

## Is CrypSA peer-to-peer?

No.

CrypSA still relies on a **canonical server** that:

- validates events  
- enforces invariants  
- maintains canonical history  

It is not a fully decentralized system.

---

## What does the server actually do?

The server:

- receives candidate events  
- validates them (schema, identity, preconditions, invariants, rules)  
- resolves conflicts  
- records accepted events  
- updates derived canonical state  
- distributes canonical updates  

It does **not** need to simulate the full world continuously.

---

## How is this different from traditional multiplayer?

Traditional model:
- server simulates the world
- clients receive state updates

CrypSA model:
- clients simulate locally
- server validates events
- world is reconstructed from event history

The key shift is:

> from synchronizing state → to agreeing on events

---

## What are “invariants”?

Invariants are rules that must always be true in canonical reality.

Examples:
- an object cannot exist in two places at once  
- ownership must be consistent  
- resources cannot go negative  
- placement rules must be respected  

If an event would break an invariant, it is rejected.

---

## What are “preconditions”?

Preconditions are the assumptions a client makes when proposing an action.

Examples:
- “this tile is empty”  
- “I own this object”  
- “this item still exists”  

If those assumptions are no longer true, the event is rejected.

---

## What happens if two players act at the same time?

Both players can submit events.

The server:

- validates both  
- accepts one (first valid within conflict scope)  
- rejects the other with a conflict result  

Observers then reconcile.

---

## What happens when the client is wrong?

The client may:

- predict an action locally  
- be rejected by the server  

When this happens:

- the local prediction is corrected  
- the observer rebuilds from canonical truth  

This is expected behavior.

---

## Does CrypSA support real-time gameplay?

Yes, but with tradeoffs.

CrypSA works best for:

- persistent worlds  
- strategy systems  
- simulation-heavy games  
- object-driven interactions  

It is less suited (v0.1) for:

- twitch shooters  
- frame-perfect combat  
- heavy physics-based systems  

---

## Is CrypSA deterministic?

Yes — at the canonical level.

Given the same:

- event history  
- rules  
- definitions  

All observers must derive the same state.

---

## Is canonical state stored or reconstructed?

Both.

- canonical truth = event history  
- derived state = materialized view for performance  
- snapshots = cached reconstruction points  

The system **can always rebuild from events**.

---

## What are snapshots?

Snapshots are stored derived state at a specific point in history.

They are used to:

- speed up loading  
- avoid full replay  
- support recovery  

They do not replace event history.

---

## What is the current state of the project?

CrypSA is currently:

- a conceptual architecture  
- supported by documentation and specifications  
- backed by a teaching prototype  

It is **not yet a production-ready system**.

---

## Is the current prototype networked?

No.

The current prototype is a **teaching playground** designed to:

- demonstrate event flow  
- show validation concepts  
- visualize canonical vs local state  

A real networked prototype is planned.

---

## Why does CrypSA use custom terminology?

Some terms (Mint, Genome, Observer, etc.) are custom.

This is because:

- existing terms did not cleanly describe the model  
- the architecture combines multiple paradigms  

A terminology primer is provided to map these to familiar concepts.

---

## Can CrypSA scale?

Potentially, but this is not yet proven.

Scaling depends on:

- partitioning strategies  
- validation performance  
- snapshot systems  
- event distribution  

This is an area for future development and testing.

---

## What are the biggest risks of CrypSA?

- complexity of validation logic  
- handling divergence and reconciliation  
- performance under high event load  
- networking and latency challenges  
- lack of production testing (current state)  

---

## Why build CrypSA?

CrypSA explores a different approach to multiplayer systems:

- persistent, replayable worlds  
- strong rule enforcement via invariants  
- flexible client-side simulation  
- event-driven canonical truth  

It is an attempt to rethink how shared digital worlds are constructed.

---

## Where should I start?

If you're new:

1. `CRYPSA_IN_5_MINUTES.md`  
2. `TERMINOLOGY_PRIMER.md`  
3. `CrypSA_Runtime_Spec.md`  

---

## One Sentence Summary

CrypSA is a system where clients simulate locally, servers validate events, and shared reality is defined by an agreed-upon history of those events.

---
