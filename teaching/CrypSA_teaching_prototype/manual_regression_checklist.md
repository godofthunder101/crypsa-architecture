# Manual Regression Checklist

## Purpose

This repo now has a small non-UI automated test layer, but the Tk-heavy paths
still need manual verification.

Use this checklist after changing runtime/UI/Mint behavior, especially around:

- adapter/request handoff code
- Tk modal interactions
- history/timeline selection
- Mint modal parsing and save behavior

The goal is not exhaustive QA. The goal is to catch the high-value interactive regressions quickly.

This checklist exists for a completed teaching artifact, so use it to protect stable behavior after bug fixes or small doc/packaging updates rather than as a reason to keep expanding the prototype indefinitely.

Reading note:

- if a checklist item fails, trace the matching path in `codebase_walkthrough.md` first
- then use the package `REFERENCE.md` file for the subsystem you changed
- for interactive bugs, the usual debug order is runtime/controller -> lens adapter -> UI module -> request type -> request dispatch
- for non-UI behavior, run the automated tests first and then use this checklist for Tk/manual confirmation

Fast automated check:

```powershell
python -m unittest
```

## Runtime Launch

1. Run:

```powershell
.\start-crypsa-teaching-prototype.cmd
```

2. Confirm the main window opens without traceback.
3. Confirm both panes render and the bottom buttons appear.

## Build Modal

1. Click `Build`.
2. Confirm the modal opens without traceback.
3. Confirm the card list renders kinds from the current catalog.
4. Click `Submit Build Candidate` on any non-context-sensitive kind.
5. Confirm:
   - the modal closes
   - `Pending Submissions` increments
   - the observer log records the queued candidate

## Beacon Teaching Path

1. If the teaching example is not loaded, click `Try Beacon`.
2. Confirm:
   - the teaching example loads
   - the build chooser reopens
   - `Beacon` is selected or clearly emphasized
3. Submit the Beacon build candidate.
4. Reconcile.
5. Confirm:
   - no traceback occurs
   - Beacon is either accepted or rejected with an explicit reason
   - on success, the observer log points the user toward `History` or `Timeline`

## Candidate Queue

1. Queue at least one build candidate.
2. Open `Candidates`.
3. Confirm queued lines render in order.
4. Click `Clear Candidates`.
5. Confirm:
   - the modal closes
   - the queue clears
   - `Pending Submissions` returns to `0`

## History Modal

1. Open `History`.
2. Confirm the modal renders accepted events without traceback.
3. Click `Select` on a non-head event if available.
4. Confirm:
   - the modal closes
   - the main window redraws
   - the canonical pane now reflects the selected historical event
   - branch selection remains sensible for shared-ancestor events

## Timeline Modal

1. Open `Timeline`.
2. Confirm rows, node colors, connectors, and inspector render.
3. Click an event node.
4. Confirm:
   - no traceback occurs
   - the inspector updates
   - the selected-node outline updates in the still-open modal
   - the active-lineage label updates in the still-open modal
   - the main window redraws to the selected history point
5. Click `Center Observer View Near Canonical State`.
6. Confirm:
   - the Timeline modal stays open
   - the observer position changes
   - the observer log records the recenter action

## Server Mint Modal

1. Open `Mint` from the canonical pane.
2. Confirm the modal opens and lists mintable kinds.
3. Click `Mint` on a normal kind.
4. Confirm:
   - the modal closes
   - a new canonical event is accepted
   - the canonical pane updates

## Mint Editor Launch

1. From the server Mint modal, click `Open Mint Editor`.
2. Confirm the standalone editor opens without traceback.

## Mint Create Modal

1. In the Mint editor, click `Add`.
2. Confirm the create modal opens fully on screen.
3. Confirm the quick-start text and preset buttons are visible.
4. Leave the default genome JSON in place.
5. Enter:
   - a unique kind name
   - optional description
6. Click `Save`.
7. Confirm:
   - no traceback occurs
   - the modal closes
   - the new kind appears in the left list
   - the right detail pane updates

## Mint Parser Edge Cases

These are high-value because `_normalize_text_list()` has changed.

1. Create or edit a Mint kind using default JSON arrays.
2. Confirm save succeeds.
3. Edit one field into plain comma text, for example:
   - `build, mint`
4. Confirm save succeeds.
5. Edit one list field into a single JSON string, for example:

```json
"build"
```

6. Confirm the editor shows a validation error or accepts it consistently with the intended schema behavior, and does not crash.

## Catalog Reload

1. After saving a Mint kind, return to the prototype.
2. Open `Build` or `Mint`.
3. Click `Reload Catalog`.
4. Confirm the modal closes and the main UI keeps a valid selection.
5. Reopen the modal and confirm the new kind appears.

## State Persistence

1. Close the prototype normally.
2. Relaunch it.
3. Confirm:
   - the app starts without traceback
   - saved observer/canonical state loads coherently
   - the selected build kind is still valid

## Close-Out

If a change touched:

- `crypsa_lens_adapters.py`
- `crypsa_action_requests.py`
- `crypsa/ui/crypsa_history_ui.py`
- `crypsa/ui/crypsa_action_ui.py`
- `mint/mint_lens_adapters.py`
- `mint/mint_catalog_store.py`

then this checklist should be treated as the minimum manual validation pass.
