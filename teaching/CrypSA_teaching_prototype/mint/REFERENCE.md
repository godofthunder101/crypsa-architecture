# Mint Reference

## Purpose

This folder contains the Mint authoring side of the CrypSA Teaching Prototype.

Mint is the definition layer for future canonical objects.

In this prototype, accepted canonical objects **freeze the Mint definition they were created from**.

This means:

> Mint defines structure for future canonical events and objects, not past ones.

Mint is therefore not just editor content. It is structural input to:

- candidate-event validation
- canonical event acceptance
- canonical object reconstruction

Use this document when you want to understand how Mint editing, validation, and saving are split across files.

---

## Architectural Position

Mint belongs to the **structural definition layer** of CrypSA.

It feeds into the **truth layer**, but does not belong to it.

```text
Mint → Validation → Canonical Event History → Replay → Derived Canonical State
````

Mint:

* defines what objects *can be*
* does not define what *has happened*

---

## Folder Role

The `mint` package owns:

* the standalone Mint editor window
* the Mint kind edit modal
* the Mint detail/modal translation layer
* tag-management UI
* catalog normalization and validation
* catalog file save/load logic

The runtime **reads from Mint**.
The Mint editor **writes to Mint**.

---

## Mint-Side Stack

1. editor orchestration
2. typed Mint models
3. adapters
4. modal UI
5. schema + persistence

---

## What This Folder Is Not

This package is not:

* the source of canonical event history
* the runtime replay system
* the validation authority

It does not:

* validate candidate events at runtime
* mutate canonical event history
* reconstruct canonical state

It defines **possible structure**, not **actual history**.

---

## Main Workflow

The Mint side follows this loop:

1. Load `mint_catalog.json`
2. Show available Mint kinds
3. Allow create/edit/remove/tag operations
4. Normalize and validate catalog structure
5. Save catalog with incremented version
6. Runtime reloads catalog when needed

---

## Teaching Prototype Behavior

If a catalog change invalidates existing runtime data:

* queued candidate events referencing removed kinds are discarded
* accepted canonical objects referencing removed kinds trigger a full runtime reset

This is:

> a teaching constraint, not a production migration strategy

---

## Module Map

### `mint_catalog_editor.py`

Editor orchestration layer.

Responsibilities:

* root editor window
* kind list and selection
* detail panel rendering
* create/edit/remove flows
* save/reload operations

This is the entrypoint for Mint editing.

---

### `mint_lens_adapters.py`

Translation layer for Mint.

Responsibilities:

* shaping catalog data into UI-ready structures
* building modal starter values
* building detail panel data

This preserves separation between:

* raw catalog structure
* UI presentation

---

### `mint_models.py`

Typed structural definition layer.

Defines:

* `Genome`
* `InvariantRule`
* `ActionTransition`
* `EntityMetadata`
* `MintedDefinition`

This is the **shared structural contract** between:

* Mint editor
* runtime validation
* canonical event processing

---

### `mint_editor_ui.py`

Modal UI layer.

Responsibilities:

* dialog layout
* input gathering
* modal interaction

Important:

> This layer gathers input but does not define schema validity.

---

### `mint_catalog_store.py`

Schema + persistence boundary.

Responsibilities:

* catalog load/save
* schema normalization
* validation of Mint definitions
* default catalog creation

This is the closest thing to **Mint schema truth**.

---

## Key Mint Concepts

### Entity Definitions

Defines identity and presentation (e.g. colors).

---

### Entity Metadata

Defines:

* description
* rule tags
* genome

---

### Genome

The genome defines object behavior structure.

It includes:

* valid states
* allowed actions
* action transitions
* invariant rules
* initial invariant state

---

### Rule Tags

Used for grouping and organization.

They do not replace genome rules.

---

### Frozen Definitions

When a canonical event creates an object:

* the Mint definition is frozen into that object's history

This ensures:

* deterministic replay
* stable reconstruction

---

### Catalog Version

Each save increments the version.

Runtime may reload updated definitions for **future events only**.

---

## Validation Strategy

Mint validation ensures:

* structural correctness of definitions
* schema validity
* rule completeness

It does NOT:

* validate runtime candidate events
* enforce canonical invariants at runtime

Runtime validation happens in:

```text
runtime → validation.py → reconciliation → canonical event history
```

---

## Defaults and Recovery

If the catalog is missing or invalid:

* a default catalog is generated

This ensures:

* runtime can always function
* baseline definitions always exist

---

## Relationship to Runtime

Mint affects:

* future candidate-event validation
* canonical event acceptance
* object creation rules

Mint does NOT affect:

* past canonical event history
* already accepted canonical objects

---

## Key Insight

> Mint defines what objects *can be*.
> Canonical event history defines what *has happened*.

---

## Recommended Reading Order

1. `mint_catalog_editor.py`
2. `mint_models.py`
3. `mint_lens_adapters.py`
4. `mint_editor_ui.py`
5. `mint_catalog_store.py`

---

## Debug Shortcut

* Button behavior → `mint_catalog_editor.py`
* Data structure → `mint_models.py`
* Modal values → `mint_lens_adapters.py`
* Schema validation → `mint_catalog_store.py`

---

## Beginner Notes

* This is a **technical authoring tool**, not a no-code system
* JSON errors usually indicate invalid genome structure
* Add new rule types in the store module first
* Keep Mint, runtime, and UI explanations aligned
* Mint affects **future events**, not past history

---

## One Sentence Summary

Mint defines the structural possibilities of canonical objects, providing the schemas and rules that validation uses to determine which candidate events can become part of canonical event history.
