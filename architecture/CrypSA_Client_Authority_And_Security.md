# Client Authority and Security in CrypSA

## Purpose

CrypSA allows clients (Observers) significantly more simulation freedom than traditional multiplayer architectures.

This is intentional.

This document explains:

* why CrypSA allows this
* what risks it introduces
* how those risks are controlled
* how this differs from traditional server-authoritative models

---

## The Core Tradeoff

Traditional multiplayer systems assume:

> Clients are untrusted → the server must simulate everything

CrypSA assumes:

> Clients may simulate freely → but only validated events become shared truth

This shifts the problem from:

* preventing all invalid behavior

to:

* controlling what becomes canonical

---

## Clients and Simulation

In CrypSA, clients (Observers) may:

* simulate actions locally
* explore hypothetical outcomes
* queue potential changes
* operate without immediate server confirmation

This improves:

* responsiveness
* flexibility
* offline and delayed interaction models

However:

> Local simulation has no authority over shared reality.

Only validated events affect the shared world.

---

## The Invariant Boundary

The control point in CrypSA is the **invariant boundary**.

Any action that affects shared reality must:

1. be proposed as a candidate
2. be validated against invariant rules
3. be accepted before becoming canonical

If validation fails:

* the action is rejected
* it never becomes part of shared reality

---

## Server Responsibility

CrypSA separates responsibilities into:

* **Truth** → canonical events and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

The server operates strictly in the **truth layer**.

It must:

* validate invariant rules
* enforce world constraints
* decide which events become canonical
* maintain canonical event history

It does not:

* simulate the entire world
* interpret meaning
* manage client experience

> The server controls truth, not simulation.

---

## Security Model

CrypSA’s security model is based on controlling canonicalization rather than restricting simulation.

### 1. Validation

Before an event is accepted:

* invariant rules are checked
* domain constraints are enforced
* invalid actions are rejected

---

### 2. Canonical Gatekeeping

Only accepted events:

* affect the shared world
* are visible to other observers
* become part of canonical history

All other actions are discarded.

---

### 3. Auditability

Because CrypSA is event-driven:

* all accepted actions are recorded
* history is inspectable
* past states can be reconstructed

This enables:

* debugging
* moderation
* anomaly detection

---

### 4. Post-Validation Analysis

Additional security layers may operate on canonical history:

* anomaly detection
* behavioral analysis
* statistical validation
* rule-based moderation

These systems analyze:

* event patterns over time
* cross-observer behavior
* deviations from expected norms

---

## Security Strategies

CrypSA supports multiple validation strategies depending on system needs:

### Strict Validation

* detailed invariant enforcement
* closer to traditional authoritative systems

---

### Lightweight Validation + Monitoring

* minimal validation at acceptance
* deeper issues detected post hoc

---

### Trust-Weighted Systems

* different observers have different trust levels
* validation strictness may vary

---

### Hybrid Simulation Validation

* server re-simulates critical actions only
* avoids full world simulation

---

## Important Clarification

CrypSA does not assume clients are trustworthy.

It assumes:

> Trust is not required at the simulation level — only at the validation boundary.

---

## Tradeoffs

### Advantages

* responsive client experience
* reduced server simulation load
* strong audit and replay capabilities
* flexible architecture
* support for persistent worlds

---

### Challenges

* requires careful invariant design
* introduces new attack surfaces
* depends on strong validation rules
* not ideal for high-frequency competitive systems

---

## Suitable Use Cases

CrypSA works best where:

* actions are discrete and meaningful
* history matters
* persistence is important
* auditability is valuable

Examples:

* sandbox worlds
* building systems
* crafting and economies
* shared simulation environments

---

## Less Suitable Use Cases

CrypSA is less suited for:

* twitch shooters
* high-frequency combat systems
* physics-heavy PvP
* strict real-time competitive environments

---

## Summary

CrypSA does not remove server authority.  
It redefines it.

> The server does not control everything that happens.  
> It controls what is allowed to become real.

Security in CrypSA comes from:

* validation
* controlled canonicalization
* and inspectable history

—not from restricting client-side behavior.
