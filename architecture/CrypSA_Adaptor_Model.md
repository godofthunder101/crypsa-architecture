# CrypSA Adapter Model

## Purpose

This document defines the role of **adapters** in CrypSA.

Adapters are responsible for **translation**.

They convert runtime data into forms usable by other layers without altering meaning, truth, or intent.

---

## Core Principle

Adapters **translate data without changing its meaning**.

They do not:

* define truth
* interpret meaning
* execute logic
* mutate canonical state

They exist to ensure that:

* systems remain decoupled
* data remains consistent
* boundaries remain explicit

---

## Adapters in the CrypSA Architecture

CrypSA separates responsibilities into four layers:

* **Truth** → canonical event history and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

Adapters sit strictly in the **translation layer**.

They:

* consume canonical event history, derived canonical state, or observer/runtime data
* reshape it for other systems
* do not influence truth or interpretation

---

## What Adapters Do

Adapters perform **pure data transformation**.

Typical responsibilities include:

* reshaping canonical data into UI-friendly structures
* converting runtime data into lens-ready inputs
* formatting data for debugging or external tools
* mapping between internal representations and transport formats

Examples:

* converting derived canonical state into a UI view model
* transforming canonical event history into a structured feed
* exposing validation context in a readable format
* mapping network payloads into typed requests

Adapters are:

* deterministic
* stateless (or effectively stateless)
* side-effect free

---

## What Adapters Must Not Do

Adapters must never:

* define or alter truth
* perform validation or enforce rules
* execute gameplay or domain logic
* act as controllers or coordinators
* interpret meaning (this is the role of lenses)
* assign canonical ordering or authority (e.g. canonical sequence)

If an adapter begins making decisions about meaning or rules, it is no longer an adapter.

---

## 🔍 Adapters vs Lenses (Critical Boundary)

Adapters and lenses are distinct and must not overlap in responsibility.

| Layer   | Responsibility                                   |
| ------- | ------------------------------------------------ |
| Adapter | Shapes data structure for systems                |
| Lens    | Determines meaning or visibility for an observer |

---

### 🔒 Boundary Rules

Adapters:

* reshape data
* preserve meaning
* do not interpret

Lenses:

* interpret data
* determine meaning
* do not modify canonical data

---

### ⚠️ Hard Constraints

* Adapters do not decide meaning
* Lenses do not modify canonical data

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
  No conditionals that encode gameplay or meaning
  Structural transformation logic is allowed, but semantic or rule-based decisions are not

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

Prepare data for display layers.

---

### Lens Input Adapters

Shape data into forms expected by lenses.

---

### Transport Adapters

Convert between wire formats and internal structures.

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

Adapters operate on data around truth boundaries, but do not define or modify canonical truth.

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
* preserve meaning
* enforce separation between systems

They do not:

* define truth
* interpret meaning
* execute logic

---

## One Sentence Summary

Adapters convert data between systems without changing its meaning, ensuring that truth, interpretation, and experience remain cleanly separated.
