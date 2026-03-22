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
- how adapters shape data across boundaries  
- how lenses interpret canonical reality into experience  

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
- how adapters protect boundaries between systems  
- how lenses interpret canonical reality into observer experience  
- how CrypSA differs from traditional multiplayer systems  

---

## Recommended Reading Order

If you are new to the architecture layer, start with:

1. `CrypSA_Client_Observer_Model.md`  
   Explains the role of observers, local simulation, and reconciliation.

2. `CrypSA_Server_Responsibility_Model.md`  
   Explains what the server does and does not do.

3. `CrypSA_Adapter_Model.md`  
   Explains how data is translated between runtime, lenses, and UI.

4. `CrypSA_Lens_Model.md`  
   Explains how observers interpret canonical reality.

5. `CrypSA_Observer_Server_Contract.md` *(if present)*  
   Describes how observers and the server interact.

6. `CrypSA_Event_Flow.md` *(if present)*  
   Walks through how actions become canonical events.

---

## Key Architectural Ideas

The architecture layer is built around a few core ideas:

- **Observers simulate locally**
- **The server validates instead of simulating everything**
- **Canonical history defines shared reality**
- **Reconstruction replaces state synchronization**
- **Adapters translate data across system boundaries**
- **Lenses interpret canonical reality into player experience**

These ideas form the conceptual backbone of CrypSA.

---

## System Layering (Conceptual)

CrypSA can be understood as layered responsibilities:

```text
Canonical History / Derived State (Truth)
        ↓
Adapter Layer (Translation)
        ↓
Lens Layer (Interpretation)
        ↓
Observer Experience / UI (Presentation)
````

This separation ensures that:

* truth remains consistent
* interpretation remains flexible
* presentation remains decoupled

---

## How This Relates to the Specs

The architecture documents are **conceptual**.

They describe:

* intent
* structure
* mental models

The `spec/` folder describes:

* exact behavior
* validation rules
* ordering and consistency
* runtime requirements

A good way to read CrypSA is:

```text
Architecture → Spec → Implementation
```

---

## Relationship to Other Folders

### Foundation

High-level philosophy and motivation.

```text
../foundation/
```

---

### Core Concepts

Definitions of key ideas such as:

* events
* invariants
* observers
* identities

```text
../core-concepts/
```

---

### Specifications

Formal runtime behavior.

```text
../spec/
```

---

### Implementation

How CrypSA can be built and tested.

```text
../implementation/
```

---

## What This Folder Is Not

This folder does **not** define:

* exact event schemas
* validation pipelines
* network behavior
* replay guarantees

Those are defined in the `spec/` folder.

---

## Current Scope

The architecture documents describe CrypSA at a high level.

They are:

* intentionally simplified
* focused on understanding
* not complete system definitions

They should be read as a bridge between:

* conceptual framing
* formal system specification

---

## One Sentence Summary

The `architecture/` folder explains how CrypSA works conceptually—how observers, adapters, lenses, events, and the canonical server interact to define shared reality—without diving into full implementation details.
