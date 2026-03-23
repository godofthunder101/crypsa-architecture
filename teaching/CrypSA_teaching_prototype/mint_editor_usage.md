# Mint Editor Usage

## Purpose

The Mint Editor manages the shared `mint_catalog.json` used by the CrypSA prototypes.

In the current teaching prototype, the editor lets you edit both Mint identity metadata and the deterministic genome used for future accepted canonical events.

This keeps Mint authoring visible and concrete while still preserving a CrypSA-shaped catalog.

This editor now belongs to a completed teaching artifact, so the goal is stable authoring clarity rather than ongoing feature expansion for its own sake.

## What You Can Edit

For each Mint kind, the editor currently lets you change:

- `Kind Name`
- `Description`
- `Rule Tags`
- `Default Color`
- `Valid States`
- `Allowed Actions`
- `Action Transitions`
- `Invariant Rules`
- `Initial Invariant State`

The editor also shows the full genome definition for the selected Mint kind.

## Genome Editing

Genome fields are edited as JSON in the current version of the editor. That means the editor is flexible, but you should keep the schema valid for the prototype runtime.

This is intentional for the teaching prototype. The editor is closer to a technical authoring tool than a casual sandbox, so it keeps the Mint genome visible instead of hiding it behind heavier form abstractions.

The editor now includes two preset starting points inside the genome section:

- `Default Structure`: a normal buildable kind with the standard baseline genome
- `Beacon Example`: the built-in context-sensitive teaching pattern

If you are reading the code behind this editor, treat the modal in stages:

1. `mint_lens_adapters.py` prepares the starter values for the selected kind or the default create flow.
2. `open_entity_modal()` shows the overall edit flow.
3. `_build_scrollable_modal_body()` defines the two-column shell.
4. `_build_tag_selector()` and `_build_genome_editor()` hold most of the detailed form behavior.

On the Mint side, the easiest layer stack is:

1. editor orchestration
2. typed Mint models
3. adapters
4. modal UI
5. schema and persistence

## Basic Workflow

1. Launch the editor with:

```powershell
.\start-mint-editor.cmd
```

2. Select an existing Mint kind from the left list, or click `Add`.

3. In the edit popup:
   - set the kind name
   - write or update the description
   - choose one or more rule tags
   - choose a default color
   - choose a preset if you want a faster starting point
   - edit the genome JSON fields as needed

4. Click `Save`.

5. Back in the prototype, reload or reopen the Mint or candidate-event build UI if needed.

Context-sensitive invariant rules can also reference causal event context, not just the replay parent. In this prototype that means a Mint genome can require a contextual event family to appear in `causal_references` during canonical validation.

## Tags

Use the `Tags` button from the main editor window to manage the shared tag list.

You can:

- add a new tag
- rename an existing tag

Renaming a tag updates any Mint kinds that already use it.

## Files Involved

- `mint/mint_catalog_editor.py`: the editor UI
- `mint/mint_models.py`: typed shared Mint structures used by the editor, store, and frozen-definition handoff
- `mint/mint_lens_adapters.py`: detail-pane and modal starter-data translation
- `mint/mint_editor_ui.py`: the edit modal layout, field helpers, and presets
- `mint/mint_catalog_store.py`: validation and save/load logic
- `mint_catalog.json`: the shared Mint catalog file

## Notes

- The editor changes future mintable kinds only.
- Existing canonical objects already accepted into a universe keep their own frozen Mint definition.
- If another prototype window is already open, you may need to reload its catalog after changing the Mint catalog.
- In the teaching prototype, if a reload removes a Mint kind that is still referenced by queued candidates or accepted canonical objects, the local teaching world resets to baseline instead of trying to migrate that history.
- The current editor is optimized for clarity and directness, not for shielding users from raw JSON structure.
- If you are reading the code, start with `mint/mint_catalog_editor.py`, then `mint/mint_models.py`, then `mint/mint_lens_adapters.py`, then `mint/mint_editor_ui.py`, then `mint/mint_catalog_store.py`.
- If you are reading the store code, read the top-level load/save and default-catalog path first, then the narrower normalization helpers second.
- If you changed Mint save behavior or runtime/Mint integration behavior, use `manual_regression_checklist.md` as the minimum smoke test.
