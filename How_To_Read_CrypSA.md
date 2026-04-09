# How to Read CrypSA

## Purpose

This document helps readers navigate the CrypSA repository effectively.

CrypSA is structured as a layered architecture with:

- conceptual explanations  
- architectural models  
- authoritative specifications  
- implementation guidance  

Different readers should approach the repo differently.

---

## Authority Level

This document provides guidance for navigating the repository.  
It does not define system behavior or architecture.

---

## Related Documents

- `README.md` — project overview
- `architecture/` — system structure and responsibilities
- `spec/` — authoritative runtime behavior
- `CrypSA_Terminology_Primer.md` — CrypSA language and terms

---

## Core Principle

👉 CrypSA is not meant to be read linearly.

👉 It is meant to be read based on your goal.

---

# Quick Start Paths

## 🧠 Fastest Understanding (5–10 minutes)

If you want to understand what CrypSA is:

1. CrypSA_In_One_Diagram.md  
2. CrypSA_In_5_Minutes.md  
3. CrypSA_Terminology_Primer.md  

This gives you:

- the core idea  
- the key concepts  
- the language of the system  

---

## 🧭 Conceptual Understanding

If you want to understand how CrypSA works:

1. CrypSA_In_5_Minutes.md  
2. CrypSA_Worked_Example.md  
3. architecture/  

This gives you:

- the mental model  
- the system structure  
- how concepts connect  

---

## ⚙️ Implementation Path

If you want to build a system using CrypSA:

1. spec/  
2. implementation/minimal_validator/  
3. implementation/CrypSA_Local_First_Development_Approach.md  

This gives you:

- authoritative behavior  
- a starting implementation  
- a practical build path  

> The spec defines runtime behavior.  
> Your implementation must follow it.

👉 Start with the minimal validator, then expand outward.

---

## 🧱 Architecture Deep Dive

If you want full architectural clarity:

1. architecture/  
2. spec/  
3. diagrams/  

This gives you:

- system boundaries  
- validation model  
- event model  
- consistency model  

---

## 🧪 Design Space and Flexibility

If you want to understand what CrypSA leaves open:

👉 architecture/CrypSA_Invariants_and_Design_Space.md  

This explains:

- what is fixed  
- what is product-dependent  
- how to make design decisions  

---

# Repository Structure (How to Think About It)

CrypSA is divided into layers:

---

## Core Model (Foundation)

Defines:

- canonical event history  
- validator authority  
- invariant boundary  

Important:

👉 This is the foundation of all CrypSA systems and defines canonical truth.

👉 All other layers depend on this model  

---

## Conceptual Documents

Explain:

- what CrypSA is  
- why it exists  
- how to think about it  

Examples:

- CrypSA_In_5_Minutes.md  
- CrypSA_Worked_Example.md  

---

## Architecture

Defines:

- system structure  
- responsibilities  
- boundaries between components  

Important:

👉 Architecture explains how the system is organized.

👉 It defines structure, not runtime behavior.

👉 The spec defines behavior within that structure.

---

## Spec (Authoritative)

Defines:

- runtime behavior  
- validation rules  
- event lifecycle  
- consistency guarantees  

Important:

👉 The spec is the source of truth for system behavior  

---

## Implementation

Provides:

- build strategies  
- reference implementations  
- practical guidance  

Important:

👉 Implementation docs are not authoritative

👉 They must not redefine system behavior  

---

## Diagrams

Provide:

- visual explanations  
- conceptual overviews  

Important:

👉 Diagrams are illustrative

👉 They must align with architecture and spec  

---

# How to Use This Repo Correctly

## 1. Do not treat architecture docs as spec

Architecture explains structure.

Spec defines behavior.

---

## 2. Do not treat implementation docs as rules

Implementation docs show possible approaches.

They are not required patterns.

---

## 3. Always defer to the spec for behavior

If there is any ambiguity:

👉 The spec is correct.

---

## 4. Use the design space intentionally

CrypSA is not all-or-nothing.

You are expected to:

- choose reconciliation strategies  
- choose prediction models  
- choose deployment models  

👉 within the constraints of CrypSA invariants  

👉 CrypSA provides structure for these decisions, not answers for all of them.

---

# Suggested Reading Order (Complete Path)

For a full understanding:

1. CrypSA_In_One_Diagram.md  
2. CrypSA_In_5_Minutes.md  
3. CrypSA_Terminology_Primer.md  
4. CrypSA_Worked_Example.md  
5. architecture/  
6. spec/  
7. implementation/  

---

# Summary

CrypSA is a structured architecture model with:

- strict invariants  
- flexible implementation space  
- layered documentation  

👉 Read based on your goal, not in strict sequence.

👉 Always distinguish between:

- concept (what it means)  
- architecture (how it is structured)  
- specification (how it behaves)  
- implementation (how it is built)
