# CrypSA in 5 Minutes

This is a quick mental model for understanding CrypSA.

If you only read one document, read this.

---

## The Core Idea

CrypSA is a multiplayer architecture where:

> The shared world is defined by accepted events, not continuously synchronized state.

Instead of synchronizing everything all the time:

* clients simulate locally
* actions are proposed as events
* the server validates those events
* accepted events define shared reality

---

## 📊 Core Mental Model (Visual)

```mermaid
flowchart LR

subgraph Truth
A[Canonical Event History]
B[Derived Canonical State (via Replay)]
end

subgraph Translation
C[Adapters]
end

subgraph Interpretation
D[Lenses]
end

subgraph Experience
E[UI / Observer Experience]
F[Local Simulation]
end

A --> B
B --> C
C --> D
D --> E
```

---

## The Mental Model

Think of CrypSA like this:

* The **server** decides what becomes canonical truth
* Observers simulate what they think is happening
* Only validated actions become part of shared reality
* Everything else is local prediction

But the system becomes much clearer if you think of it as **four separate responsibilities**.

---

## The Four Responsibilities

CrypSA is easiest to understand as four layers:

---

### 1. Truth

This is the canonical layer.

It includes:

* canonical event history
* validation
* canonical ordering (`server_sequence`)
* derived canonical state (via replay)

This is the part of the system that defines what is real.

If something is not part of canonical event history:

> it did not happen

---

### 2. Translation

This is the adapter layer.

Adapters take canonical and observer-side data and reshape it into forms that other layers can consume safely.

They do things like:

* combine canonical and observer state
* normalize structures
* build view-ready or lens-ready data

Adapters do **not** define truth.

They answer:

> “How should this data be structured so it can be used?”

---

### 3. Interpretation

This is the lens layer.

Lenses interpret translated data into observer-specific meaning.

They may determine:

* what is visible
* what is interactable
* what matters to this observer
* what should appear in a teaching/debug view

Lenses do **not** define truth either.

They answer:

> “What does this mean for this observer?”

---

### 4. Experience

This is what the player directly interacts with.

It includes:

* UI
* rendering
* local feedback
* local simulation and prediction

This layer is:

* fast
* responsive
* immediate

But:

> nothing here is automatically shared truth

---

## What This Changes

Traditional multiplayer systems often combine too many responsibilities together:

* server simulates
* client displays
* state is synchronized constantly

CrypSA separates them more clearly:

* **truth** is canonical
* **translation** is adapter-driven
* **interpretation** is lens-driven
* **experience** is local and responsive

---

## Why This Matters

This separation makes the system easier to:

* reason about
* debug
* persist
* replay
* evolve without collapsing boundaries

The teaching prototype made this especially clear:

> truth, translation, interpretation, and experience work better when kept separate

---

## What CrypSA Is Not

CrypSA is not:

* a replacement for all multiplayer systems
* a solution for every type of game
* a way to eliminate latency

It is a different way of structuring:

* authority
* validation
* interpretation
* and shared truth

---

## Where It Fits

CrypSA works best when:

* actions are discrete
* history matters
* persistence matters

Examples:

* building systems
* crafting systems
* economic systems
* sandbox worlds

---

## Where It Fits Less Well

CrypSA is not ideal for:

* twitch shooters
* high-frequency combat
* physics-heavy PvP

---

## One Missing Truth (Now Added)

In CrypSA:

> state is not stored as truth — it is derived from canonical event history via replay

---

## If You Want More

* Read `CrypSA_Terminology_Primer.md`
* Read `FAQ.md`
* See `CrypSA_WORKED_EXAMPLE.md` for a full step-by-step flow
* See `CrypSA_Architecture_Overview.md` for the system map

---

## Final Summary

CrypSA can be summarized as:

> canonical event history defines truth,
> adapters shape data,
> lenses interpret meaning,
> and observers simulate and experience the resulting world
