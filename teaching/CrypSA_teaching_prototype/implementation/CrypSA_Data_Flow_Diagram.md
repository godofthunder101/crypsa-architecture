# CrypSA Teaching Prototype - Data Flow Diagram

## Purpose

This document shows how data moves through the CrypSA teaching prototype.

It complements `CrypSA_Teaching_Prototype_Layers.md` by focusing on:

- truth flow
- replay flow
- presentation flow
- intent flow

The goal is to make the prototype's architecture understandable at a glance.

For artifact status and maintenance posture, pair this with `STATUS.md`.

## Core Principle

The teaching prototype is built around two opposite flows:

- downward: truth becomes experience
- upward: user intent becomes validated canonical change

This demonstrates the CrypSA model, not a distributed production implementation.

## Full System Data Flow

```text
Canonical Event Log
-> Canonical Replay
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
-> Canonical Event Log
-> Canonical Replay
```

## Downward Flow - Truth To Experience

```text
Accepted Canonical History
-> Replay
-> Derived Canonical State
-> Adapters
-> Lenses
-> UI
```

This is the path by which accepted history, replayed truth, and observer-local context become visible state and interaction options.

## Upward Flow - Intent To Truth

```text
UI Action
-> Typed Request
-> Request Dispatch
-> Controller Mutation Path
-> Validation
-> Canonical Apply
-> Accepted Canonical Event
-> Replay
```

This is the path by which user intent becomes accepted canonical truth or is rejected during canonical validation.

## Boundary Emphasis

### Runtime / Controller

Owns meaning and coordination.

### Replay

Owns derivation of canonical state.

### Adapters

Own data shaping.

### Lenses + Requests

Own interpretation and intent handoff.

### UI

Owns presentation and input.

### Mint

Owns authored definition structure.

## Why This Matters

This structure makes it easier to:

- teach CrypSA clearly
- inspect canonical history
- debug local vs canonical divergence
- evolve layers independently
- avoid runtime/UI coupling

## One Sentence Summary

The CrypSA teaching prototype turns accepted canonical events into observer experience through replay, adapters, lenses, and UI, while all user intent flows back upward through typed requests, controller actions, validation, and canonical application.
