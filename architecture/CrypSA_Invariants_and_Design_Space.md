# CrypSA — Invariants and Design Space

## Purpose

This document defines:

* the **non-negotiable architectural invariants** of CrypSA
* the **product-dependent design space** intentionally left open to implementers

Its goal is to clarify that CrypSA is:

👉 a structured architecture model with fixed core truths  
👉 not a single rigid system design  

---

## Defines

* CrypSA's non-negotiable architectural invariants and the product-dependent design space  
* Structured design axes for reasoning about implementation choices  

---

## Does Not Define

* A single required implementation strategy  
* Authoritative runtime behavior (defined in `/spec`)  
* Observer-side or validator-side implementation details  

---

## 📜 Authority Level

This document defines system structure and responsibilities.  
It does not define runtime behavior.  

👉 The `/spec` directory is the authoritative source of behavior.  

---

## Related Documents

* `architecture/CrypSA_Invariant_Types.md` — invariant categorization and enforcement model  
* `spec/CrypSA_Validation_Model.md` — authoritative runtime validation behavior  
* `architecture/CrypSA_Invariant_Boundary.md` — the invariant boundary  
* `architecture/CrypSA_Observer_Model.md` — observer responsibilities  
* `architecture/CrypSA_Validator_Responsibility_Model.md` — validator responsibilities  

---

## Core Principle

👉 CrypSA defines **what must be true**  
👉 but does not prescribe **how every system must be built**  

---

## What CrypSA Is

CrypSA is an architecture model that defines:

* how truth is established  
* how events become canonical  
* how state is derived  
* how systems remain replayable and consistent  

---

## What CrypSA Is Not

CrypSA is **not**:

* a fixed client-server architecture  
* a required networking topology  
* a single implementation pattern  
* a one-size-fits-all runtime design  

---

# Architectural Invariants (Non-Negotiable)

The following are **fundamental to CrypSA**.

If these are not preserved, the system is no longer a CrypSA system.

---

## 1. The Validator Defines What Becomes Canonical

* All candidate events must be evaluated by a validator  
* The validator defines what becomes canonical and enforces validation rules derived from applicable invariants  
* If accepted, an event becomes canonical and is appended to canonical event history  

👉 Observers do not define truth  

---

## 2. Canonical Event History Is the Source of Truth

* Canonical event history is the authoritative record of the system  
* It is append-only  
* Canonical event history is the source of truth  

---

## 3. Derived State Is Not Truth

* All state is derived from canonical event history  
* Derived canonical state is a projection  
* Derived canonical state may be reconstructed at any time via replay of canonical event history  

👉 Derived canonical state is not authoritative  

---

## 4. All Changes That Affect Canonical Event History Cross the Invariant Boundary

* Any change that affects canonical event history must:

  * be represented as a candidate event  
  * pass through the invariant boundary  
  * be evaluated against validation rules derived from applicable invariants  

* If accepted, an event becomes canonical and is appended to canonical event history  

---

## 5. Observers Are Non-Authoritative

Observers:

* may simulate locally  
* may predict outcomes  
* may propose candidate events  

But:

👉 observers do not define canonical truth  

---

## 6. Replay Is a Required Capability

* Systems must be able to reconstruct derived canonical state from canonical event history via replay  
* Replay is a required capability  
* Snapshots are optimizations, not truth  

---

## 7. Replay Must Be Deterministic

Given the same:

* canonical event history  
* interpretation logic  

replay must produce equivalent derived canonical state  

---

# Design Space (Product-Dependent)

CrypSA intentionally leaves several areas **open to implementation choice**.

These are not undefined — they are **design axes** that must be decided based on product goals.

---

## Key Principle

👉 CrypSA defines that these concerns exist  
👉 but does not define a single correct solution  

👉 These are not optional concerns — they must be addressed, but the solutions are product-dependent  

---

## 1. Validator Deployment

Options include:

* local validator (single-player / offline / fallback)  
* remote validator (shared systems)  
* hybrid models  

CrypSA defines the role of the validator, not its location  

---

## 2. Reconciliation Strategy

Systems may choose:

* full replay-based reconciliation  
* partial rollback  
* state patching  
* hybrid approaches  

CrypSA requires consistency with canonical event history,  
but does not enforce how reconciliation is implemented  

---

## 3. Prediction Model

Observers may:

* aggressively predict outcomes  
* minimally predict  
* avoid prediction entirely  

Tradeoff:

* responsiveness vs correction frequency  

---

## 4. Observer Simulation Depth

Observer-side systems may include:

* full local simulation  
* partial simulation  
* presentation-only layers  

CrypSA defines that observer simulation is non-authoritative,  
but does not define its depth  

---

## 5. Snapshot Strategy

Snapshots may vary in:

* frequency  
* granularity  
* storage model  

Snapshots are:

* derived artifacts  
* performance optimizations  
* never authoritative  

---

## 6. Partitioning Strategy

Systems may choose:

* no partitioning  
* spatial partitioning  
* logical/domain partitioning  
* hybrid models  

CrypSA defines conflict scope,  
but not how partitions are implemented  

---

## 7. Transport Layer

CrypSA is transport-agnostic, but requires:

* reliable delivery of canonical events  
* correct ordering of canonical events  
* replay-safe communication  

👉 ordering must be enforced via `canonical_sequence`  

The transport implementation is product-dependent  

---

## 8. Security Model

Systems may choose:

* strict validation  
* lightweight validation with monitoring  
* trust-weighted systems  
* hybrid approaches  

CrypSA enforces that:

👉 If accepted, an event becomes canonical and is appended to canonical event history  

but does not enforce a single validation strictness model  

---

# Design Axes (Structured Tradeoffs)

These axes help implementers reason about choices.

---

## Validation Strictness

* strict validation ↔ permissive validation  

---

## Reconciliation

* heavy replay ↔ lightweight correction  

---

## Prediction

* aggressive prediction ↔ minimal prediction  

---

## State Reconstruction

* replay-heavy ↔ snapshot-heavy  

---

## Deployment

* local-first ↔ remote-authority systems  

---

## Partitioning

* fine-grained ↔ coarse-grained  

---

## Security

* high-trust ↔ zero-trust systems  

---

# Implementation Responsibility

Implementers are responsible for:

* selecting appropriate strategies within this design space  
* ensuring chosen strategies do not violate CrypSA architectural invariants  
* balancing performance, responsiveness, and correctness  

---

# Summary

CrypSA provides:

* a **fixed model of truth**  
* a **structured event-driven architecture**  
* a **clear authority boundary**  

CrypSA does not provide:

* a single runtime design  
* a fixed deployment model  
* a universal implementation strategy  

---

## Final Statement

👉 CrypSA is a framework for structuring systems around canonical validation and replayable truth  

👉 It defines invariants and their enforcement model, not implementations  

👉 Systems built with CrypSA are expected to make product-driven decisions within this structure  
