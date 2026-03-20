# Where CrypSA Fits (and Where It Doesn't)

CrypSA is not a universal replacement for all multiplayer architectures.

It is designed for specific types of systems, and it introduces tradeoffs that make it better suited for some domains than others.

This document outlines where CrypSA is a strong fit, where it is weaker, and how it compares to traditional approaches.

---

## Core Strength of CrypSA

CrypSA is strongest in systems where:

> the history of events matters more than frame-by-frame simulation

It prioritizes:

- canonical event history  
- deterministic reconstruction  
- invariant-based validation  
- persistent world evolution  

---

## Where CrypSA Fits Well

### 1. Persistent World Games

Examples:

- sandbox building games  
- survival worlds  
- MMO-style environments  
- simulation-driven worlds  

Why it fits:

- world state evolves through discrete events  
- history and provenance matter  
- replay and reconstruction are valuable  

---

### 2. Strategy and Simulation Games

Examples:

- RTS (non twitch-heavy)  
- turn-based or hybrid strategy  
- colony simulations  

Why it fits:

- actions are discrete and verifiable  
- outcomes can be validated against rules  
- deterministic reconstruction is achievable  

---

### 3. Economy-Driven Systems

Examples:

- trading systems  
- resource networks  
- logistics simulations  

Why it fits:

- transactions are event-based  
- auditability is valuable  
- invariant validation maps well to economic rules  

---

### 4. Asynchronous / Long-Lived Worlds

Examples:

- idle or incremental games  
- persistent online worlds  
- offline progression systems  

Why it fits:

- events can be validated independently  
- snapshots + replay support long timelines  
- clients do not need constant synchronization  

---

### 5. Systems Requiring Replay and Auditability

Examples:

- competitive logs  
- debugging-heavy simulations  
- content playback systems  

Why it fits:

- canonical history is first-class  
- replay is built into the architecture  
- state can be reconstructed at any point  

---

## Where CrypSA Is a Poor Fit (v0.1)

### 1. High-Frequency Twitch Gameplay

Examples:

- FPS games  
- fighting games  
- real-time action combat  

Why it struggles:

- requires frame-level authority  
- latency sensitivity is extreme  
- event validation is too slow for per-frame decisions  

---

### 2. Physics-Heavy Simulations

Examples:

- vehicle physics  
- destructible environments  
- continuous collision systems  

Why it struggles:

- continuous simulation is hard to represent as discrete events  
- deterministic reconstruction is difficult  
- invariant validation becomes complex and expensive  

---

### 3. Strict Server-Authoritative Competitive Systems

Examples:

- anti-cheat critical PvP  
- esports-grade environments  

Why it struggles:

- CrypSA gives more responsibility to observers  
- validation replaces full server simulation  
- requires additional trust and security layers  

---

## Hybrid Possibilities

CrypSA does not need to replace all systems.

It can coexist with traditional approaches.

Examples:

- CrypSA for world state + traditional server authority for combat  
- CrypSA for economy + traditional sync for physics  
- CrypSA for persistence + snapshot injection into real-time systems  

This hybrid approach may be the most practical path for many projects.

---

## Key Tradeoffs

CrypSA introduces important tradeoffs:

### Gains

- replayability  
- auditability  
- persistence  
- flexible client simulation  
- reduced server simulation load  

---

### Costs

- more complex validation logic  
- reconciliation complexity  
- harder mental model  
- potential security challenges  
- not suited for all gameplay types  

---

## Why CrypSA Exists

CrypSA is an exploration of a different question:

> What if multiplayer systems agreed on history instead of synchronizing state?

It is not intended to replace all architectures.

It is intended to:

- expand the design space  
- enable new types of systems  
- simplify some problems while shifting complexity elsewhere  

---

## When to Consider CrypSA

You should consider CrypSA if your system:

- is event-driven at its core  
- benefits from persistent history  
- needs replay or auditability  
- can tolerate validation-based authority  
- is not dependent on frame-perfect simulation  

---

## When NOT to Use CrypSA

You should avoid CrypSA if your system:

- depends on frame-level precision  
- requires strict server-side control of every interaction  
- relies heavily on continuous physics  
- cannot tolerate reconciliation corrections  

---

## One Sentence Summary

CrypSA is best suited for event-driven, persistent, and simulation-oriented systems, and is not currently a good fit for high-frequency, physics-heavy, or strictly server-authoritative real-time games.
