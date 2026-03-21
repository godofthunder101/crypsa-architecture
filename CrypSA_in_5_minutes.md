# CrypSA in 5 Minutes

This is a quick mental model for understanding CrypSA.

If you only read one document, read this.

---

## The Core Idea

CrypSA is a multiplayer architecture where:

> The shared world is defined by accepted events, not continuously synchronized state.

Instead of synchronizing everything all the time:

- clients simulate locally  
- actions are proposed as events  
- the server validates those events  
- accepted events define shared reality  

---

## The Mental Model

Think of CrypSA like this:

- The **server** decides what *actually happened*  
- The **clients** simulate what *they think is happening*  
- Only validated actions become part of shared reality  
- Everything else is local prediction  

---

## The Three Layers

CrypSA is easiest to understand as three layers:

---

### 1. Observer (Client / Local Simulation)

This is what the player directly interacts with.

- fast  
- responsive  
- immediate  

The player can act freely.

But:

> nothing here is automatically shared truth

---

### 2. Invariant Boundary (Validation Layer)

This is the checkpoint between local simulation and shared reality.

When an action affects the shared world:

- it must cross this boundary  
- it must be validated  

If it fails:

> it never becomes real

---

### 3. Canonical World (Shared Reality)

This is the true world.

- defined by accepted events  
- consistent for all observers  
- reconstructed from history  

If something is not part of canonical history:

> it did not happen

---

## What This Changes

Traditional systems:

> the server simulates everything

CrypSA:

> the server validates what matters

---

## Why This Matters

CrypSA separates:

### Local Simulation
- fast  
- flexible  
- not authoritative  

### Shared Reality
- validated  
- consistent  
- authoritative  

This separation makes systems easier to:

- reason about  
- debug  
- persist  
- replay  

---

## What CrypSA Is Not

CrypSA is not:

- a replacement for all multiplayer systems  
- a solution for every type of game  
- a way to eliminate latency  

It is a different way of structuring:

- authority  
- validation  
- and shared truth  

---

## Where It Fits

CrypSA works best when:

- actions are discrete  
- history matters  
- persistence matters  

Examples:

- building systems  
- crafting systems  
- economic systems  
- sandbox worlds  

---

## Where It Fits Less Well

CrypSA is not ideal for:

- twitch shooters  
- high-frequency combat  
- physics-heavy PvP  

---

## If You Want More

- Read `TERMINOLOGY_PRIMER.md`  
- Read `FAQ.md`  
- See `CrypSA_WORKED_EXAMPLE.md` for a full step-by-step flow  

---

## Final Summary

CrypSA can be summarized as:

> Clients simulate freely,  
> servers validate important actions,  
> and accepted events define shared reality.
