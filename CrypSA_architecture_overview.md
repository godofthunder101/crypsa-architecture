# CrypSA — Architecture Overview

## Purpose

This document provides a high-level map of the CrypSA architecture.

It is intended to help readers understand:

- how the repository is structured  
- how CrypSA is organized into layers  
- how the major components relate to each other  

> This document maps the system.  
> It does not fully explain how CrypSA works.

For conceptual understanding, see:
- `CRYPSA_IN_5_MINUTES.md`
- `TERMINOLOGY_PRIMER.md`

For formal behavior, see:
- `spec/`

---

## The CrypSA Stack

CrypSA is organized into layered responsibilities.

Each layer builds on the one below it.

---

### 🌌 1. Foundation Layer

Defines the **why** behind CrypSA.

- motivation  
- problem space  
- comparison to traditional systems  

📁 See:

- `foundation/CrypSA_Origin_Statement.md`
- `foundation/CrypSA_Universe_Model.md`
- `foundation/CrypSA_Traditional_vs_CrypSA.md`

---

### 🧠 2. Core Concepts Layer

Defines the **building blocks** of the system.

- what objects are  
- how events work  
- what invariants are  
- how state evolves  

📁 See:

- `core-concepts/CrypSA_Object_Model.md`
- `core-concepts/CrypSA_Invariant_Model.md`
- `core-concepts/CrypSA_Event_Model.md`
- `core-concepts/CrypSA_Event_Lifecycle.md`
- `core-concepts/CrypSA_Mental_Model_One_Page.md`

---

### 🏗 3. Architecture Layer

Defines how the system operates conceptually.

- observer (client) responsibilities  
- server responsibilities  
- interaction between components  

📁 See:

- `architecture/CrypSA_Client_Observer_Model.md`
- `architecture/CrypSA_Server_Responsibility_Model.md`
- `architecture/CrypSA_Object_Lifecycle_Walkthrough.md`

---

### 📐 4. Specification Layer

Defines the **formal runtime behavior** of CrypSA.

This is where the system becomes technically implementable.

📁 See:

- `spec/`

Includes:

- runtime model  
- event model  
- validation model  
- consistency model  
- replay model  
- snapshot model  
- identity model  
- transport model  

---

### 🎮 5. Design Layer

Explores how CrypSA can be used in real systems.

- design principles  
- gameplay considerations  
- optional patterns  

📁 See:

- `design/CrypSA_Design_Principles.md`
- `design/CrypSA_Offline_Mode_Simple.md`

---

### 🧪 6. Implementation Layer

Provides guidance for building CrypSA systems.

- minimal server design  
- prototype direction  
- engineering entry points  

📁 See:

- `implementation/CrypSA_Minimal_Server_v0.1.md`
- `implementation/CrypSA_Quick_Start_For_Engineers.md`

---

### 📊 Supporting Layers

#### Diagrams

Visual representations of system behavior.

📁 `diagrams/`

---

#### Atlas & Glossary

Terminology and navigation support.

📁 `atlas/`

---

## How to Navigate the Repository

Different readers should approach the repo differently.

---

### New to CrypSA

1. `CRYPSA_IN_5_MINUTES.md`  
2. `TERMINOLOGY_PRIMER.md`  
3. `FAQ.md`  

---

### Understanding the Architecture

1. `foundation/`  
2. `core-concepts/`  
3. `architecture/`  

---

### Understanding the System Behavior

1. `spec/CrypSA_Runtime_Spec_v0.1.md`  
2. `spec/README.md`  

---

### Building with CrypSA

1. `implementation/CrypSA_Minimal_Server_v0.1.md`  

---

## Relationship Between Layers

CrypSA is best understood as a progression:

Foundation → Concepts → Architecture → Spec → Implementation

- Foundation explains **why**
- Concepts define **what exists**
- Architecture explains **how it fits together**
- Spec defines **how it behaves**
- Implementation shows **how to build it**

---

## Summary

This document provides a structural overview of CrypSA.

To understand the system in depth:

- use conceptual docs for intuition  
- use specs for exact behavior  
- use implementation docs to build  

---

## One Sentence Summary

The CrypSA architecture is organized into layered documentation that moves from conceptual foundations to formal specifications and implementation guidance.
