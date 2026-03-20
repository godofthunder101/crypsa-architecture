# CrypSA Architecture

This folder explains how CrypSA works at a conceptual level.

If the `spec/` folder defines:

> how CrypSA behaves as a system

the `architecture/` folder explains:

> how to think about CrypSA and how its parts fit together

---

## Purpose of This Folder

These documents describe:

- the observer model  
- the role of the canonical server  
- how canonical truth is defined  
- how events shape the world  
- how reconstruction replaces state synchronization  

They are intended to:

- build intuition  
- explain system structure  
- prepare readers for the formal specs  

---

## What You Will Learn Here

By reading the architecture docs, you should understand:

- why CrypSA separates simulation from truth  
- why the server validates instead of simulating everything  
- how canonical history defines shared reality  
- how observers reconstruct the world  
- how CrypSA differs from traditional multiplayer systems  

---

## Recommended Reading Order

If you are new to the architecture layer, start with:

1. `CrypSA_Client_Observer_Model.md`  
   Explains the role of observers and local simulation.

2. `CrypSA_Server_Responsibility_Model.md`  
   Explains what the server does and does not do.

3. `CrypSA_Observer_Server_Contract.md` (if present)  
   Describes how observers and the server interact.

4. `CrypSA_Event_Flow.md` (if present)  
   Walks through how actions become canonical events.

---

## How This Relates to the Specs

The architecture documents are **conceptual**.

They describe:

- intent  
- structure  
- mental models  

The `spec/` folder describes:

- exact behavior  
- validation rules  
- ordering and consistency  
- runtime requirements  

A good way to read CrypSA is:

Architecture → Spec → Implementation

---

## Relationship to Other Folders

### Foundation

High-level philosophy and motivation.

../foundation/

---

### Core Concepts

Definitions of key ideas like:

- events  
- invariants  
- observers  
- identities  

../core-concepts/

---

### Specifications

Formal runtime behavior.

../spec/

---

### Implementation

How CrypSA can be built and tested.

../implementation/

---

---

## What This Folder Is Not

This folder does **not** define:

- exact event schemas  
- validation pipelines  
- network behavior  
- replay guarantees  

Those are defined in the `spec/` folder.

---

## Current Scope

The architecture documents describe CrypSA at a high level.

They are:

- intentionally simplified  
- focused on understanding  
- not complete system definitions  

They should be read as a bridge between:

- conceptual framing  
- formal system specification  

---

## One Sentence Summary

The `architecture/` folder explains how CrypSA works conceptually—how observers, events, and the canonical server interact to define shared reality—without diving into full implementation details.
