# Client Authority and Security in CrypSA

CrypSA gives more simulation freedom to clients (Observers) than traditional multiplayer architectures.

This is intentional.

This document explains:
- why CrypSA allows this
- what risks it introduces
- how those risks are managed
- how this differs from traditional server-authoritative models

---

## The Core Tradeoff

Traditional multiplayer systems assume:

> Clients are untrusted → server must simulate everything

CrypSA assumes:

> Clients can simulate freely → but only validated events become shared truth

This shifts the problem from:
- preventing all invalid behavior

to:
- controlling what becomes canonical

---

## What Clients Can Do

In CrypSA, clients (Observers) can:

- simulate movement locally
- explore hypothetical actions
- queue potential changes
- operate without immediate server confirmation

This improves:
- responsiveness
- flexibility
- user experience
- offline or delayed interaction models

However:

> None of this becomes real until it is validated.

---

## The Invariant Boundary

The key control point in CrypSA is the **Invariant Boundary**.

Any action that affects the shared world must:

1. be proposed as a candidate
2. be validated by the server
3. be accepted before becoming canonical

If validation fails:
→ the action is rejected  
→ it never becomes part of shared reality  

---

## What the Server Controls

The server does **not** need to simulate everything.

But it **must**:

- validate invariant rules
- enforce world constraints
- decide which events become canonical
- maintain the canonical event history

This means:

> The server controls truth, not simulation.

---

## Security Model

CrypSA’s security model is based on:

### 1. Validation

Before an event is accepted:
- rules are checked
- invariants are enforced
- invalid actions are rejected

---

### 2. Canonical Gatekeeping

Only accepted events:
- affect the shared world
- are visible to other observers
- become part of history

Everything else is discarded.

---

### 3. Auditability

Because CrypSA is event-driven:

- all accepted actions are recorded
- history is inspectable
- past states can be reconstructed

This enables:
- debugging
- moderation
- anomaly detection

---

### 4. Post-Validation Analysis

CrypSA allows for additional layers such as:

- anomaly detection
- behavioral analysis
- statistical validation
- rule-based moderation systems

These can operate on:
- event history
- patterns over time
- cross-observer comparisons

---

## Alternative Security Strategies

CrypSA does not enforce a single security approach.

Instead, it allows multiple strategies depending on the application:

### Strict Validation
- server checks every invariant in detail
- closer to traditional authoritative systems

---

### Lightweight Validation + Monitoring
- server validates basic rules
- deeper issues are caught through analysis

---

### Trust-Weighted Systems
- different observers may have different trust levels
- validation rules can vary accordingly

---

### Hybrid Simulation Validation
- server re-simulates critical actions only
- not the entire world

---

## Important Clarification

CrypSA does **not** assume clients are trustworthy.

It assumes:

> Trust is not required at the simulation level — only at the validation boundary.

---

## Tradeoffs

CrypSA introduces tradeoffs:

### Advantages

- more responsive client experience  
- reduced server simulation load  
- strong audit and replay capabilities  
- flexible system design  
- support for persistent worlds  

---

### Challenges

- requires careful validation design  
- introduces new attack surfaces  
- depends on strong invariant definitions  
- may not suit highly competitive real-time games  

---

## Where This Model Works Best

CrypSA’s approach is strongest in systems where:

- actions are discrete and meaningful  
- history matters  
- persistence is important  
- auditability is valuable  

Examples:
- sandbox worlds  
- building systems  
- crafting/economy systems  
- shared simulation environments  

---

## Where It Is Less Suitable

CrypSA is less suited for:

- twitch shooters  
- high-frequency combat  
- physics-heavy PvP  
- strict real-time competitive environments  

---

## Final Summary

CrypSA does not remove server authority.

It redefines it.

> The server does not control everything that happens.  
> It controls what is allowed to become real.

Security in CrypSA comes from:
- validation  
- controlled canonicalization  
- and inspectable history  

—not from preventing all client-side behavior.

---
