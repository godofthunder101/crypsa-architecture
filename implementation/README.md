# Implementation

## Purpose

This folder contains implementation strategy, build direction, project status, and practical engineering guidance for CrypSA.

These documents describe:

* how the system may be structured and built in code  
* how components may be organized in practice  
* how architectural ideas translate into implementation  

---

## Important

Documents in this folder are **not authoritative**.

They:

* do not define runtime behavior  
* do not define validation rules  
* do not define truth  

They must not be treated as:

* specification documents  
* architecture definitions  

Examples and code patterns in this folder are illustrative and must not be treated as authoritative behavior.

---

## Source of Truth

For authoritative system behavior, refer to:

* `../spec/`

For conceptual system structure, refer to:

* `../architecture/`

---

## Relationship Between Layers

CrypSA separates documentation responsibilities across three layers:

* **Architecture** → what the system is  
* **Spec** → how the system behaves  
* **Implementation** → how the system is built  

This folder exists only in the **implementation layer**.

Implementation must never override or reinterpret behavior defined in the spec.

---

## Consistency Rules

Documents in this folder must not:

* redefine validation logic  
* redefine event structure  
* redefine invariants  
* introduce conflicting terminology  

If a conflict exists:

> the spec and architecture always take precedence  

---

## Evolution

Implementation guidance may evolve as the system is built.

If implementation patterns become stable and necessary:

* behavioral rules must move to `spec/`  
* structural definitions must move to `architecture/`  
* this folder must remain non-authoritative  

Implementation documents should not become authoritative definitions.

---

## One Sentence Summary

This folder explains how CrypSA can be built in practice, but the authoritative system definition lives in the specification and architecture layers.
