# CrypSA Adapter Rules

## Purpose

This document defines practical engineering rules for adapters in CrypSA.

Adapters are an important boundary layer in the teaching prototype and future implementations.

These rules exist to prevent adapters from becoming:

- hidden controllers  
- validation layers  
- mutation layers  
- tightly coupled runtime dependencies  

The goal is to keep adapters:

> narrow, boring, predictable, and safe

---

## Core Principle

In CrypSA:

> adapters translate data  
> they do not define truth

Adapters prepare runtime and canonical data for:

- lenses  
- UI modules  
- tooling  
- debugging views  

They are not part of canonical authority.

---

## Rule 1 — Adapters Translate, They Do Not Decide Truth

Adapters may:

- reshape data  
- aggregate inputs  
- normalize structures  
- build view-ready models  

Adapters must not:

- decide whether something is valid  
- decide whether an event should be accepted  
- decide what canonical truth is  

Truth belongs to:

- canonical history  
- validation  
- invariant enforcement  
- server-side runtime logic  

---

## Rule 2 — Adapters Do Not Mutate Canonical State

Adapters are read-only.

Adapters must not:

- append canonical events  
- modify derived canonical state  
- alter object ownership  
- change branch history  
- write directly to persistent runtime state  

If canonical state must change, that belongs to:

- runtime actions  
- validation/apply logic  
- replay/reconstruction systems  

---

## Rule 3 — Adapters Do Not Enforce Invariants

Adapters must never enforce canonical rules.

They must not decide:

- whether placement is legal  
- whether ownership is allowed  
- whether resources are sufficient  
- whether a state transition is valid  

Those belong to:

- validation logic  
- canonical runtime rules  
- invariant checks  

Adapters may display rule-related information, but they do not enforce it.

---

## Rule 4 — Adapters Should Be Narrow and Boring

A good adapter should do one job only.

Good examples:

- build timeline rows from canonical events  
- build render grid data from occupancy + observer selection  
- build teaching overlay data from pending/canonical comparison  

Bad examples:

- world + history + teaching + validation + UI adapter  
- one adapter that knows everything about the prototype  

If an adapter is hard to explain in one sentence, it is probably too broad.

---

## Rule 5 — Adapters Should Not Depend on Unrelated Lens Internals

Adapters should prepare data for lenses.

They should not:

- depend on the private output shape of unrelated lenses  
- reach into other lens modules directly  
- chain lens-specific assumptions across the system  

This keeps lenses independent and prevents lens-to-lens coupling.

Preferred pattern:

```text
Runtime State → Adapter → Lens
````

Not:

```text
Runtime State → Adapter A → Lens A → Adapter B → Lens B
```

Adapters should depend on runtime inputs, not on the internal behavior of other interpretation layers.

---

## Rule 6 — Adapters Output Lens-Ready or UI-Ready Data Only

Adapters should produce outputs that are clearly intended for a consumer.

Examples:

* lens-ready world view data
* UI-ready timeline rows
* debug-ready inspection models

Adapters should not output:

* half-runtime / half-UI mixed blobs
* ambiguous anonymous structures with unclear ownership
* data that still requires unrelated modules to dig through internal state

A good adapter output should answer:

> who is this data for?

---

## Rule 7 — Adapters Should Prefer Stable Output Shapes

Adapters should aim to produce consistent, predictable structures.

This reduces:

* UI breakage
* lens coupling
* fragile refactors

Good adapter outputs are:

* named clearly
* scoped clearly
* structurally stable

Where useful, adapters should produce:

* dataclasses
* typed dictionaries
* explicit view models

rather than loosely shaped anonymous dicts.

---

## Rule 8 — Adapters Should Not Trigger Side Effects

Adapters should not:

* save files
* fire UI actions
* dispatch events
* mutate selection
* open modals
* perform retries

They are translation layers, not workflow managers.

If an adapter causes side effects, it is probably not just an adapter anymore.

---

## Rule 9 — Adapters Should Be Easy to Test

A good adapter should be simple to test with:

* input state
* output model

Preferred form:

```text
input data → deterministic transformed output
```

This makes adapters:

* easier to trust
* easier to refactor
* easier to keep clean over time

---

## Rule 10 — Adapters May Aggregate, But Should Not Become Controllers

Adapters are allowed to combine multiple sources.

For example:

* canonical state + observer state
* branch selection + event history
* occupancy + pending prediction state

But aggregation is not the same as control.

An adapter becomes dangerous when it starts to:

* choose system behavior
* coordinate unrelated subsystems
* own application flow

If that happens, logic should move back into runtime actions or controllers.

---

## Rule 11 — Adapters Should Make Boundaries Clearer, Not Blurrier

The purpose of an adapter is to reduce coupling.

If an adapter makes the system harder to understand, it is failing its job.

A good adapter should make it easier to answer:

* where truth lives
* where interpretation lives
* where presentation lives

Adapters should sharpen boundaries, not absorb them.

---

## Adapter Checklist

Before creating or modifying an adapter, ask:

* Does this adapter only translate or shape data?
* Does it avoid mutating runtime or canonical state?
* Does it avoid validation or invariant logic?
* Is its scope narrow and explainable?
* Is its output clearly meant for a lens, UI, or tool?
* Does it avoid depending on unrelated lens internals?
* Can it be tested with simple input/output checks?

If any answer is “no”, the adapter probably needs to be redesigned.

---

## Examples

### Good Adapter

**Timeline Adapter**

* input: canonical event history
* output: timeline row models for UI

This is good because it:

* shapes data
* does not mutate state
* does not validate events
* has one clear purpose

---

### Bad Adapter

**World Interaction Adapter**

* reads all runtime state
* decides what interactions are allowed
* modifies pending actions
* updates UI state
* builds render models

This is bad because it mixes:

* translation
* rule logic
* control flow
* presentation behavior

---

## Relationship to Other CrypSA Concepts

### Adapters vs Runtime

Runtime owns truth and behavior.

### Adapters vs Validation

Validation decides what is allowed.

### Adapters vs Lenses

Lenses interpret meaning from adapted data.

### Adapters vs UI

UI displays and gathers intent using adapted outputs.

---

## Summary

CrypSA adapters are translation layers.

They should:

* be narrow
* be read-only
* avoid validation logic
* avoid side effects
* prepare clean outputs for lenses and UI

If adapters stay boring, the architecture stays healthy.

---

## One Sentence Summary

A good CrypSA adapter is a narrow, read-only translation layer that prepares runtime and canonical data for lenses or UI without mutating truth, enforcing rules, or becoming a hidden controller.
