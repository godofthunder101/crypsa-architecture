# CrypSA Adapter Model

## Purpose

This document defines the role of **adapters** in CrypSA.

Adapters are responsible for **translation**.

They reshape data into forms usable by other layers without affecting truth, meaning, or intent.

---

## 📜 Authority Level

This document defines system structure and responsibilities.  
It does not define runtime behavior.

CrypSA documentation is structured across layers:

* `/spec` — authoritative definition of runtime behavior
* `/architecture` — system structure and conceptual models

If there is any conflict:

* spec takes precedence over architecture

---

## Core Principle

Adapters translate data without affecting meaning.

They do not:

* define truth
* interpret meaning
* execute logic
* mutate canonical state

They exist to ensure:

* systems remain decoupled
* data remains consistent
* boundaries remain explicit

For formal responsibility boundaries, see:

→ `CrypSA_Boundary_Definitions.md`

---

## Adapters in the CrypSA Architecture

CrypSA separates responsibilities into four layers:

* **Truth** → canonical event history and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

Adapters sit strictly in the **translation layer**.

They:

* consume derived canonical state or observer/runtime data
* reshape it for other systems
* do not influence truth or interpretation

For strict separation of these responsibilities, see:

→ `CrypSA_Boundary_Definitions.md`

---

## What Adapters Do

This is a conceptual model, not a strict execution definition.

Adapters perform **pure data transformation**.

Typical responsibilities include:

* reshaping canonical data into structures suitable for presentation layers
* converting runtime data into lens-ready inputs
* formatting data for debugging or external tools
* mapping between internal representations and transport formats

Examples:

* converting derived canonical state into a view model
* transforming canonical event history into a structured feed
* exposing validation context in a readable format
* mapping network payloads into structured request objects

Adapters are:

* deterministic
* stateless or dependent only on explicit inputs
* side-effect free

---

## What Adapters Must Not Do

Adapters must never:

* define or alter truth
* perform validation or enforce rules
* execute gameplay or domain logic
* act as controllers or coordinators
* interpret meaning (this is the role of lenses)
* assign canonical ordering or authority (e.g. `canonical_sequence`)

If an adapter begins making decisions about meaning or rules, it is no longer an adapter.

---

## 🔍 Adapters vs Lenses (Critical Boundary)

Adapters and lenses are distinct and must not overlap in responsibility.

| Layer   | Responsibility                                  |
| ------- | ----------------------------------------------- |
| Adapter | Shapes data structure for systems               |
| Lens    | Determines meaning or relevance for an observer |

---

### 🔒 Boundary Rules

Adapters:

* reshape data structure
* do not define or interpret meaning

Lenses:

* interpret data
* determine meaning
* do not modify canonical data

---

### ⚠️ Hard Constraints

* Adapters do not decide meaning
* Lenses do not modify canonical data

For formal boundary definitions between translation and interpretation, see:

→ `CrypSA_Boundary_Definitions.md`

---

### Example

Given canonical data:

```json
{ "health": 25 }
```

* Adapter → outputs `{ health: 25 }` (structured for use)
* Lens → interprets as `"critical condition"`

Adapters are neutral.
Lenses are interpretive.

---

## Design Rules

Adapters should follow these rules:

* **No logic creep**
  No conditionals that encode gameplay rules or meaning
  Structural transformation logic is allowed

* **No mutation of source data**
  They do not change canonical or runtime state

* **Single responsibility**
  Each adapter serves one transformation purpose

* **Explicit inputs and outputs**
  No hidden dependencies or implicit state

* **Replaceable**
  Adapters can be swapped without affecting truth or interpretation

---

## Adapter Categories

Adapters may exist in different contexts:

### UI Adapters

Prepare data for presentation layers.

---

### Lens Input Adapters

Shape data into forms expected by lenses.

---

### Transport Adapters

Transform data between transport formats and internal structures.

---

### Debug / Tooling Adapters

Expose runtime or canonical data for inspection.

---

## Relationship to Truth

Adapters may consume truth-derived data, but they do not define or modify it.

Truth is:

* created through validated events
* stored in canonical event history
* reconstructed into derived canonical state

Adapters operate on data around truth boundaries, without affecting canonical truth.

---

## What the Teaching Prototype Confirmed

The teaching prototype demonstrated that:

* removing adapters leads to tight coupling between runtime and UI
* lenses become overloaded without proper data shaping
* debugging becomes harder without structured translation layers
* systems become harder to reason about without explicit boundaries

Adapters are therefore a **required architectural boundary**, not an optional pattern.

---

## Summary

Adapters are the **translation layer** of CrypSA.

They:

* reshape data
* enforce separation between systems

They do not:

* define truth
* interpret meaning
* execute logic

---

## One Sentence Summary

Adapters reshape data between systems without affecting truth or meaning, ensuring that truth, interpretation, and experience remain cleanly separated.
