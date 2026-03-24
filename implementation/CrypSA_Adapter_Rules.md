# CrypSA Adapter Rules

> Scope note: This document provides implementation guidance for adapters.
>
> For authoritative system behavior, refer to `../spec/` and `../architecture/`.

---

## Purpose

This document defines practical engineering rules for adapters in CrypSA.

Adapters are part of the **translation layer** and exist to shape runtime and canonical data for consumption by:

* lenses
* UI modules
* tools
* debugging systems

These rules exist to prevent adapters from becoming:

* hidden controllers
* validation layers
* mutation layers
* tightly coupled runtime dependencies

The goal is to keep adapters:

> narrow, boring, predictable, and safe

---

## Architectural Context

CrypSA separates responsibilities into:

* **Truth** — validation and canonical event history
* **Translation** — adapters
* **Interpretation** — lenses
* **Experience** — UI and local simulation

Adapters belong strictly to the **translation layer**.

They must not cross into:

* truth (validation or canonical mutation)
* interpretation (lens logic)
* experience (UI control or simulation behavior)

---

## Core Principle

In CrypSA:

> adapters translate data
> they do not define truth

Adapters prepare runtime and canonical data for:

* lenses
* UI modules
* tooling
* debugging views

They are not part of canonical authority or server decision-making.

---

## Rule 1 — Adapters Translate, They Do Not Decide Truth

Adapters may:

* reshape data
* aggregate inputs
* normalize structures
* build view-ready models

Adapters must not:

* decide whether something is valid
* decide whether an event should be accepted
* decide what canonical truth is

Truth belongs to:

* canonical event history
* validation
* invariant enforcement
* server-side logic

---

## Rule 2 — Adapters Do Not Mutate Canonical or Runtime State

Adapters are read-only.

Adapters must not:

* append canonical events
* modify derived state
* alter identity or ownership
* write to runtime state

Derived state is:

> a read-only result of canonical event history reconstruction

Any change to canonical truth belongs to:

* validation logic
* event application
* reconstruction systems

---

## Rule 3 — Adapters Do Not Enforce Invariants

Adapters must never enforce canonical rules.

They must not decide:

* whether placement is legal
* whether ownership is allowed
* whether resources are sufficient
* whether a state transition is valid

Those belong to:

* validation logic
* invariant checks

Adapters may display rule-related information, but they do not enforce it.

---

## Rule 4 — Adapters Should Be Narrow and Boring

A good adapter should do one job only.

Good examples:

* build timeline rows from canonical event history
* build render grid data from occupancy + observer selection
* build teaching overlay data from pending vs canonical comparison

Bad examples:

* one adapter handling world logic, validation, UI, and control flow

If an adapter is hard to explain in one sentence, it is too broad.

---

## Rule 5 — Adapters Depend on Data, Not Interpretation

Adapters prepare data for lenses.

They must not:

* depend on lens outputs
* rely on interpretation-specific structures
* chain interpretation logic across modules

Preferred pattern:

```text
Runtime Data → Adapter → Lens
```

Not:

```text
Runtime Data → Adapter → Lens → Adapter → Lens
```

Adapters depend on **data**, not **interpretation outputs**.

---

## Rule 6 — Adapters Output Consumer-Ready Data

Adapters should produce outputs clearly intended for a consumer.

Examples:

* lens-ready world data
* UI-ready timeline rows
* debug-ready inspection models

Adapters should not output:

* ambiguous mixed structures
* data that requires deep inspection by other systems

A good adapter answers:

> who is this data for?

---

## Rule 7 — Adapters Prefer Stable Output Shapes

Adapters should produce:

* consistent structures
* clearly named fields
* predictable formats

Prefer:

* dataclasses
* typed dictionaries
* explicit view models

Over:

* loosely structured anonymous data

---

## Rule 8 — Adapters Must Not Trigger Side Effects

Adapters must not:

* dispatch events
* mutate UI state
* save data
* perform retries
* control workflows

They are translation layers, not behavior layers.

---

## Rule 9 — Adapters Must Be Pure and Testable

Adapters should follow:

```text
input → deterministic output
```

They should be easy to test with:

* known input
* expected output

This makes them:

* reliable
* easy to refactor
* easy to reason about

---

## Rule 10 — Adapters May Aggregate, But Must Not Control

Adapters may combine inputs such as:

* canonical state + observer state
* event history + selection
* prediction + canonical data

But must not:

* coordinate system behavior
* manage application flow
* act as controllers

Aggregation is allowed. Control is not.

---

## Rule 11 — Adapters Must Not Depend on Transport or Async Behavior

Adapters must not:

* depend on networking logic
* handle retries or timeouts
* depend on async sequencing
* assume ordering guarantees

Transport and timing belong to:

* networking systems
* runtime coordination
* server/client communication layers

---

## Rule 12 — Adapters Must Clarify Boundaries

A good adapter makes it easier to understand the system.

It should clarify:

* where truth lives
* where interpretation happens
* where presentation happens

If an adapter makes the system harder to reason about, it is incorrectly designed.

---

## Adapter Checklist

Before creating or modifying an adapter, ask:

* Does this adapter only translate or shape data?
* Does it avoid mutating runtime or canonical state?
* Does it avoid validation logic?
* Is its scope narrow and explainable?
* Is its output clearly meant for a lens or UI?
* Does it avoid depending on interpretation internals?
* Is it deterministic and easy to test?

If any answer is “no”, redesign the adapter.

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

---

### Adapters vs Validation

Validation decides what is allowed.

---

### Adapters vs Lenses

Lenses interpret meaning from adapted data.

---

### Adapters vs UI

UI displays and gathers intent using adapted outputs.

---

## Summary

CrypSA adapters are translation layers.

They should:

* be narrow
* be read-only
* avoid validation
* avoid side effects
* produce clean outputs

If adapters stay boring, the architecture stays healthy.

---

## One Sentence Summary

A CrypSA adapter is a narrow, read-only translation layer that prepares data for lenses or UI without mutating truth, enforcing rules, or becoming a hidden controller.
