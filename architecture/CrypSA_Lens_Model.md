# CrypSA Lens Model

## Purpose

This document defines the role of **lenses** in CrypSA.

Lenses are responsible for **interpretation**.

They transform data derived from canonical event history into observer-specific experience without altering truth.

---

## 📜 Authority Level

The `/spec` directory is the **authoritative definition of runtime behavior**.

Architecture documents explain the system.
The spec defines how it must behave.

If there is any conflict, **the spec takes precedence**.

---

## Core Principle

In CrypSA:

> Canonical event history defines what is real
> Lenses define how that reality is interpreted

Lenses do not create or modify canonical event history.
They interpret it.

---

## Lenses in the CrypSA Architecture

CrypSA separates responsibilities into:

* **Truth** → canonical event history and validation
* **Translation** → adapters
* **Interpretation** → lenses
* **Experience** → UI and local simulation

Lenses sit strictly in the **interpretation layer**.

They:

* consume adapter-shaped data or derived canonical state
* produce observer-specific meaning and context
* do not influence truth or validation

---

## Why Lenses Exist

CrypSA separates:

* **what happened**
* **how it is experienced**

This allows:

* different observers to see different views
* gameplay context to shape interpretation
* visibility and access rules to apply locally
* presentation to vary without affecting truth

Lenses make this separation explicit.

---

## What a Lens Is

A lens is an interpretation layer that transforms input data into observer-usable meaning.

It may:

* filter information
* derive gameplay-relevant state
* determine visibility and interaction relevance
* define presentation context

---

## What a Lens Is Not

A lens is not:

* a source of canonical event history
* a validation system
* a way to bypass invariants
* a controller or execution system
* a mutation of canonical event history

> Lenses interpret reality. They do not define it.

---

## 🔍 Lenses vs Adapters (Critical Boundary)

Lenses and adapters are distinct and must not overlap in responsibility.

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

Given canonical-derived data:

```json id="0n7b31"
{ "health": 25 }
```

* Adapter → outputs `{ health: 25 }` (structured for use)
* Lens → interprets as `"critical condition"`

Adapters are neutral.
Lenses are interpretive.

---

## Inputs to a Lens

A lens may consume:

* derived canonical state (from canonical event history)
* adapter-shaped data
* observer identity
* local simulation context
* gameplay or visibility rules

---

## Outputs of a Lens

A lens produces interpreted, observer-specific data.

Examples:

* visible world state
* interactable objects
* gameplay overlays
* UI-ready outputs
* debugging views

---

## Where Lenses Run

In v0.1, lenses run on the observer side by design.

* the validator produces canonical event history
* observers interpret that history locally

---

## Relationship to Observers

Observers:

* reconstruct canonical event history
* simulate locally
* interpret through lenses

A CrypSA observer is:

> canonical reconstruction + local simulation + lens-based interpretation

---

## Lens and Canonical Event History

Lenses must never be mistaken for truth.

Examples:

* a hidden object still exists canonically
* an interactable object is not necessarily valid to interact with
* a highlighted action may still fail validation

> Lenses shape interpretation
> Validation defines reality

---

## Lens and Reconciliation

When canonical event history changes:

* observers reconstruct state
* lenses re-run interpretation
* the local experience updates

Lenses do not perform reconciliation, but they respond to it.

---

## Lens Design Considerations

Lenses should be:

* consistent
* understandable
* reproducible where needed

Gameplay-critical lenses should behave predictably.

Presentation-focused lenses may be more flexible.

Canonical correctness must never depend on lens output.

---

## Lens Categories

Lenses can be grouped by purpose:

### Visibility Lens

Controls what an observer can perceive.

### Gameplay Lens

Determines interactable or relevant objects.

### Presentation Lens

Shapes interpretation for rendering and UI.

### Tooling Lens

Supports debugging, inspection, and replay.

These categories may overlap.

---

## Minimal Lens Model (v0.1)

```text id="9m17ls"
Derived State + Observer Context → Interpreted View
```

---

## Example

Canonical data:

* tile_42 contains mining_station
* player_A owns it

Different lenses:

### Observer A

* sees station as owned and interactable

### Observer B

* sees station as visible but not controllable

### Debug Tool

* sees ownership and event provenance

Canonical event history remains unchanged.

---

## Boundaries

A lens should:

* consume canonical or translated data
* produce interpreted output

A lens must not:

* validate events
* enforce invariants
* write to canonical event history

---

## Summary

Lenses are the **interpretation layer** of CrypSA.

They:

* transform canonical data into observer-specific meaning
* enable flexible, contextual experiences
* preserve separation between truth and experience

They do not:

* define truth
* validate actions
* alter canonical event history

---

## One Sentence Summary

A CrypSA lens interprets canonical data into observer-specific meaning without changing what is defined by canonical event history.
