# CrypSA in 5 Minutes

This is a quick, practical explanation of what CrypSA is and how it works.

If you only read one document, read this.

---

## The Core Idea

CrypSA is a multiplayer architecture where:

> The shared world is defined by accepted events, not continuously synchronized state.

Instead of syncing everything all the time, CrypSA does this:

1. Clients (Observers) simulate locally
2. They propose actions
3. The server validates those actions
4. Accepted actions become **canonical events**
5. The world is reconstructed from those events

---

## The Mental Model

Think of CrypSA like this:

- The **server** decides what *actually happened*
- The **clients** simulate what *they think is happening*
- Only validated actions become part of shared reality
- Everything else is just local prediction

---

## The Three Layers

CrypSA is easiest to understand as three layers:

### 1. Observer (Client / Local Simulation)

This is what the player controls.

- Movement is local
- Simulation is fast and responsive
- The player can do things immediately

But:
- Nothing here is automatically shared truth

---

### 2. Invariant Boundary (Validation Layer)

This is the checkpoint.

When something matters to the shared world:
- it must cross this boundary
- it must be validated

Examples:
- placing an object
- destroying something
- transferring items

If it fails validation → it never becomes real

---

### 3. Canonical World (Shared Reality)

This is the real world.

- Defined by accepted events
- Stored as a history of events
- Reconstructed through replay

If it’s not here:
→ it didn’t happen

---

## A Simple Example

### Step 1 — Local Action

A player moves around.

- This is **Observer-only**
- It is not canonical
- No server validation required

---

### Step 2 — Propose an Action

The player places a structure.

- This becomes a **Candidate**
- It reaches the **Invariant Boundary**

---

### Step 3 — Server Validation

The server checks:
- is the location valid?
- does the player have resources?
- does it obey the rules?

If yes:
→ it becomes a **Canonical Event**

If no:
→ it is rejected

---

### Step 4 — Canonical Update

The accepted event is added to history.

All observers:
- update their world
- reconcile if needed

---

### Step 5 — Replay

The world state is derived by replaying events.

There is no “final stored state” as the source of truth.

The source of truth is:
→ **the event history**

---

## Why This Matters

CrypSA separates two things that are usually tangled together:

### Local Simulation
- fast
- responsive
- not authoritative

### Shared Reality
- validated
- consistent
- authoritative

This separation makes it easier to:
- reason about multiplayer behavior
- track history
- debug systems
- build persistent worlds

---

## What CrypSA Is NOT

CrypSA is not:

- a traditional “sync everything” multiplayer model
- a full replacement for all multiplayer architectures
- a magic solution to latency or cheating

It is a different way of structuring:
- validation
- authority
- and shared truth

---

## Where CrypSA Fits Best

CrypSA works best in systems where:

- history matters
- persistence matters
- actions are discrete and meaningful

Examples:
- building systems
- crafting systems
- economic systems
- shared sandbox worlds

---

## Where It Fits Less Well

CrypSA is not ideal for:

- twitch shooters
- high-frequency combat systems
- physics-heavy PvP
- strict real-time competitive games

---

## How This Repo Helps

This repository includes:

- a **teaching prototype**
- tools to explore:
  - observer vs canonical state
  - event submission
  - validation and rejection
  - event lineage and replay
  - Mint (object definition system)

The goal is not to be production-ready.

The goal is to make the model:
→ understandable

---

## If You Want More

- Read `TERMINOLOGY_PRIMER.md` for definitions
- Explore the teaching prototype
- Then move on to the architecture docs

---

## Final Summary

CrypSA can be summarized as:

> A system where clients simulate freely,  
> servers validate important actions,  
> and accepted events define shared reality.

Everything else builds on that.
