# CrypSA Terminology Primer

This document defines the core terms used throughout CrypSA.

If something feels unclear, check here first.

---

## Mental Model (Quick Anchor)

A useful way to understand CrypSA is to think in terms of four responsibilities:

- **Truth** — canonical events and validation  
- **Translation** — adapters shaping runtime data  
- **Interpretation** — lenses determining observer meaning  
- **Experience** — UI and local simulation  

The terms below map into these responsibilities.

---

## Core Terms

### Canonical Event

A canonical event is an event that has been:

- validated by the server  
- accepted into shared history  
- assigned an order  

Canonical events define **truth**.

---

### Candidate Event

A candidate event is:

- proposed by an observer  
- not yet validated  
- subject to rejection  

Candidate events are **attempts at truth**, not truth itself.

---

### Invariant

An invariant is a rule that must always hold.

Examples:

- a player cannot have negative resources  
- two objects cannot occupy the same exclusive space  

Invariants are enforced during validation and protect **truth**.

---

### Validation

Validation is the process of checking a candidate event against invariants.

If valid → it becomes canonical  
If invalid → it is rejected  

Validation determines whether something becomes **truth**.

---

### Canonical History

The canonical history is:

- the ordered sequence of accepted events  
- the authoritative record of what has happened  

Everything else derives from this.

---

### Replay

Replay is the process of:

- taking canonical history  
- rebuilding the current world state  

Replay is how **truth becomes state**.

---

### Derived State

Derived state is:

- the current world state  
- produced from replaying canonical events  

It is not directly synchronized — it is reconstructed.

---

### Observer

An observer is:

- a client  
- a local simulation of the world  

Observers:

- propose events  
- simulate locally  
- reconcile with canonical truth  

Observers own the **experience layer**.

---

### Reconciliation

Reconciliation is when:

- an observer updates its local simulation  
- to match canonical outcomes  

This happens after events are accepted or rejected.

---

### Adapter

An adapter reshapes data.

It:

- takes canonical and observer state  
- produces structured outputs for interpretation or UI  

Adapters belong to the **translation layer**.

They do not define truth.

---

### Lens

A lens interprets data.

It determines:

- what is visible  
- what is interactable  
- what matters to an observer  

Lenses belong to the **interpretation layer**.

They do not define truth or mutate state.

---

### UI / Experience

The experience layer includes:

- rendering  
- input  
- local feedback  
- local simulation  

This is what the player interacts with directly.

It is responsive, but not authoritative.

---

## Summary

CrypSA separates the system into four responsibilities:

- **truth** is defined by canonical events  
- **translation** shapes data via adapters  
- **interpretation** gives meaning via lenses  
- **experience** presents the world to the observer  

Understanding this separation makes the rest of CrypSA much easier to follow.
