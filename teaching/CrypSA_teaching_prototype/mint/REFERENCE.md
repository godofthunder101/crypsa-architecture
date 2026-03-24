# Mint Reference

## Purpose

This folder contains the Mint authoring side of the CrypSA Teaching Prototype.

Mint is the definition layer for future canonical objects. In this prototype, accepted objects freeze the Mint definition they were created from.

That is why the Mint side matters to the CrypSA model itself: it is not just editor content, it is structural input to future candidate-event validation and accepted canonical objects.

Use this document when you want to understand how Mint editing, validation, and saving are split across files.

If you want a guided tutorial for following the code across files, start with `Codebase_Walkthrough.md` in the project root first, then use this file for the Mint-specific reference view.

If you want the current artifact status and maintenance posture before reading Mint internals, read `../STATUS.md` in the project root.

If you want the quickest manual validation path after changing Mint or runtime/Mint integration behavior, use `Manual_Regression_Checklist.md` in the project root.

If you are lost on the Mint side, use this file to separate three concerns: editor orchestration, modal presentation, and schema truth.

If your question becomes "how does Mint fit into the broader CrypSA runtime beyond this teaching app?", read `../Prototype_vs_Current_CrypSA_Model.md` and then the newer `../architecture/` and `../spec/` documentation. This folder teaches the local authoring boundary, not the full architecture around it.

## Folder Role

The `mint` package owns:

- the standalone Mint editor window
- the Mint kind edit modal
- the Mint detail/modal translation layer
- tag-management UI
- catalog normalization and validation
- catalog file save/load logic

The runtime reads from Mint. The Mint editor writes to Mint.

The easiest Mint-side layer stack is:

1. editor orchestration
2. typed Mint models
3. adapters
4. modal UI
5. schema and persistence

If you are following a runtime behavior question back into Mint, the usual path is:

1. identify which Mint kind or genome rule matters
2. inspect the typed shared shape in `mint_models.py`
3. inspect the detail or modal lens in `mint_lens_adapters.py`
4. inspect the stored shape in `mint_catalog_store.py`

## What This Folder Is Not

This package is not:

- a casual no-code content editor
- the runtime replay engine
- the canonical event graph

It is a technical authoring and validation layer for future canonical object definitions.

Inside this repo, it should be read as part of a completed teaching artifact rather than an open-ended content system.

## Main Workflow

The Mint side follows this loop:

1. Load `mint_catalog.json`.
2. Show the list of Mint kinds.
3. Let the user create, edit, rename, remove, or retag kinds.
4. Normalize and validate the result.
5. Save the catalog back to disk with a bumped version.
6. Let the runtime reload the updated catalog when needed.

Teaching-prototype note:

- if a catalog reload removes a kind that is still referenced by queued candidates or accepted canonical objects, the runtime resets the local teaching world to baseline
- this is intentional teaching behavior, not a migration strategy for a full runtime

## Module Map

### `mint_catalog_editor.py`

This is the Mint editor orchestration layer.

It owns:

- the root editor window
- the left-side Mint kind list
- the right-side detail view
- create, edit, remove, reload, and tag actions
- save/reload status text

This file is the entrypoint for the standalone Mint editor.

If you want to know "what happens when I click Add, Edit, Remove, Tags, or Reload," start here.

Recent readability note:

- the editor file now stays closer to pure orchestration
- read-only detail shaping and modal starter values now live in `mint_lens_adapters.py`

Helper-stage map:

- `_refresh_list()`: restore selection and keep the list/detail view in sync after save or reload
- `_set_selected_kind()`: render the currently selected kind using a `MintDetailLens`
- `_submit_entity_modal()`: validate modal input, update the catalog, and save

### `mint_lens_adapters.py`

This is the Mint-side translation layer.

It owns:

- right-hand detail-pane lens data
- create/edit modal starter data
- summary/detail string shaping for the editor view

This file matters because it is the handoff boundary between raw catalog state and the narrower data shapes the editor UI renders.

This is deliberate architectural scaffolding, not just string-formatting convenience:

- adapters keep the editor UI from coupling too tightly to raw catalog structure
- adapters shape selected-kind and create-flow data into presentation-facing forms
- modal UI can stay focused on layout and input gathering instead of catalog traversal

Helper-stage map:

- `build_mint_detail_lens()`: translate selected Mint state into right-hand detail data
- `build_mint_entity_modal_lens()`: translate selected or default catalog state into create/edit modal starter values

Reading tip:

- if you are wondering "where did this modal field value come from?", check `build_mint_entity_modal_lens()` before reading widget code
- if you are wondering "why does the right-hand detail pane look like this?", check `build_mint_detail_lens()` before reading the editor renderer

### `mint_models.py`

This is the typed shared Mint-structure layer.

It owns:

- `Genome`
- `InvariantRule`
- `ActionTransition`
- `EntityMetadata`
- `MintedDefinition`
- `build_minted_definition()`

This file matters because it is the narrow shared vocabulary between:

- the Mint editor
- the Mint store
- runtime-side canonical validation
- the frozen Mint definitions attached to accepted canonical objects

Reading tip:

- start here if you need to know "what shape is this Mint data supposed to have?"
- then move outward to `mint_catalog_store.py` for normalization or `mint_lens_adapters.py` for presentation shaping

### `mint_editor_ui.py`

This is the Mint modal UI layer.

It contains:

- popup creation
- labeled field helpers
- the Mint-kind edit modal
- the tag-manager modal
- color-swatch grid helpers

This module is mostly presentation. It gathers user input and sends it back to the editor orchestration layer.

It now reads best as:

- lens-backed starter values from `mint_lens_adapters.py`
- widget/layout work in this module
- validation/save back in `mint_catalog_editor.py`

Recent readability note:

- the Mint kind modal now reads as named layout sections such as the scrollable body, tag selector, and genome editor
- that keeps the top-level modal function shorter without changing what the modal does

Helper-stage map:

- `_build_scrollable_modal_body()`: two-column scrollable shell for the edit modal
- `_build_tag_selector()`: editable tag rows for the current kind
- `_build_genome_editor()`: the advanced JSON editor plus preset controls

Reading tip:

- start with `open_entity_modal()` to see the overall edit flow, then drop into the three helpers above only if you need the specific layout details
- the preset controls in `_build_genome_editor()` are the quickest way to understand the intended starting shapes for new Mint kinds

### `mint_catalog_store.py`

This is the Mint schema and persistence boundary.

It owns:

- the catalog file path
- default Mint definitions
- default genome generation
- rule-tag normalization
- genome normalization
- invariant-rule normalization
- catalog load/save
- input sanitization

This is the safest file to treat as the "truth" for what a valid Mint catalog looks like.

Recent readability note:

- the normalization path now uses more small helper functions for JSON parsing, transition normalization, and catalog assembly
- the validation rules are the same, but the file is easier to scan in stages

Helper-stage map:

- `_json_object_or_value()`: accept Python objects or JSON text from the editor
- `_normalized_transition()`: validate one action-transition entry
- `_normalize_invariant_rule_entry()`: validate one invariant-rule entry
- `_load_entity_definitions()` / `_load_entity_metadata()`: staged catalog assembly during load

Reading tip:

- if you need the allowed catalog shape, read the default builders and load/save path first
- if you need one specific validation rule, then drop into the narrower normalization helpers

## Key Mint Concepts

### Entity definitions

`entity_definitions` stores the visible identity palette for each Mint kind.

In this prototype that means the color pair used to draw a kind.

### Entity metadata

`entity_metadata` stores everything else about a Mint kind, including:

- description
- rule tags
- default color
- genome

### Genome

The genome is the structured behavior definition for a Mint kind.

It contains:

- valid states
- allowed actions
- action transitions
- invariant rules
- initial invariant state

The editor keeps these fields visible as JSON because this prototype values clarity and directness over a heavily abstracted form builder.

### Rule tags

Rule tags are lightweight labels for grouping Mint kinds.

They help organize the catalog, but they do not replace genome rules.

### Catalog version

Each save bumps the catalog version. The runtime can then reload the latest catalog and use those definitions for future accepted objects.

Existing accepted canonical objects keep their frozen Mint definition.

## Validation Strategy

The Mint editor does not trust raw form input.

Instead:

- the modal gathers strings and JSON text
- the editor passes those values to sanitization helpers
- the store module normalizes and validates the result
- only valid data is written back to `mint_catalog.json`

This keeps schema rules in one place instead of scattering them across UI code.

## Defaults And Recovery

The store module also defines fallback behavior when the catalog file is missing or unusable.

That means this folder is responsible not only for editing Mint, but also for establishing what a safe baseline Mint catalog looks like.

## Recommended Reading Order

1. `mint_catalog_editor.py`
2. `mint_models.py`
3. `mint_lens_adapters.py`
4. `mint_editor_ui.py`
5. `mint_catalog_store.py`

That order starts with user actions, then the edit modal, then the schema rules underneath.

Shortcut:

- "what does this button do?" -> `mint_catalog_editor.py`
- "what shape is this Mint data supposed to have?" -> `mint_models.py`
- "where did this modal value come from?" -> `mint_lens_adapters.py`
- "what JSON shape is valid?" -> `mint_catalog_store.py`

## Beginner Notes

- The Mint editor is a technical authoring tool, not a no-code game editor.
- JSON errors during editing usually mean the genome structure does not match what the store module expects.
- If a new invariant rule type is added, the store module should usually be updated first, then the UI/help text second.
- If the runtime behavior changes, the Mint docs and the build modal explanations should stay in sync.
- If you are debugging a runtime behavior difference, remember the key split: Mint changes future accepted objects, not already accepted canonical history.
- The best reading path is still editor -> modal UI -> store, but the helper functions inside each file now carry more of the detailed formatting and normalization work than before.
- If you are adding comments in the Mint code, prefer comments that explain stage boundaries or validation intent, not comments that restate the JSON field names.
