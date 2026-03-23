# Runtime Schema

## Purpose

`crypsa_teaching_prototype_state.json` is the saved runtime state for the minimal CrypSA teaching prototype.

It stores observer state, accepted canonical history, current event-lineage selection, and UI logs. Canonical truth still comes from replaying accepted canonical history.

This schema belongs to a completed teaching artifact, so changes to it should be rare and justified by real maintenance pressure rather than cleanup for its own sake.

## Top-Level Structure

The state file has five top-level sections:

- `observer`
- `mint`
- `events`
- `selection`
- `logs`

When reading the runtime code, this file maps most directly to:

- `crypsa/crypsa_teaching_prototype.py` for the meaning of each section
- `crypsa/runtime_persistence.py` for the schema-aware store load/save boundary
- `crypsa/crypsa_state_io.py` for the low-level JSON file I/O

Useful reading pattern:

1. read this schema top-down
2. map each section back to the matching state group in `crypsa_teaching_prototype.py`
3. if the question is about load/save behavior, read `crypsa/runtime_persistence.py` next
4. only then drop into `crypsa_event_graph.py` for replay and branch-row meaning
5. if the question is about UI display, follow that state through `crypsa_lens_adapters.py` next

Fast truth rule:

- accepted canonical history lives in `events`
- replay-derived visible state comes from `crypsa_event_graph.py`
- the UI only presents translated views of that state

Typed-model shortcut:

- `observer.invariant_boundary_candidates` round-trips through `CandidateEvent` in `crypsa/runtime_models.py`
- `events.records` round-trip through `CanonicalEvent` in `crypsa/runtime_models.py`
- replay-derived visible canonical objects are not stored here; they are rebuilt later as `ReplayObjectRecord` and `ReplayBranchState`

## `observer`

This section stores observer-local state:

- `local_x`
- `local_y`
- `facing`
- `build_selection`
- `auto_reconcile`
- `observer_identity`
- `invariant_boundary_candidates`

`invariant_boundary_candidates` is the queue of observer-side candidate events waiting to cross the invariant boundary and be reconciled into canonical events.

In code, each saved queue item is hydrated into a typed `CandidateEvent` before runtime actions or reconciliation use it.

## `mint`

This section stores minimal Mint runtime data:

- `catalog_version`
- `next_object_id`

The actual Mint catalog lives in `mint_catalog.json`.

`catalog_version` matters for future accepted canonical events. Existing accepted objects keep the frozen Mint definition captured when they were accepted.

## `events`

This section stores accepted canonical event history:

- `next_sequence`
- `records`

Each record is one accepted canonical event and uses the current schema, including:

- `sequence`
- `event_id`
- `event_family`
- `event_type`
- `target_identity`
- `observer_identity`
- `timestamp`
- `lineage_parent`
- `causal_references`
- `branch_hint`
- `catalog_version`
- `payload`

In code, each saved record is hydrated into a typed `CanonicalEvent`, while `payload` remains the intentionally more dynamic part of the accepted record.

`lineage_parent` drives deterministic replay. `causal_references` keeps broader candidate-event context for canonical validation.

`branch_hint` is a UI aid for lineage visualization. It is not canonical truth by itself.

In this minimal prototype, non-lineage causal references do not drive replay, but they can be consulted by invariant validation rules that need contextual event families.

If you want to understand how this accepted canonical history becomes visible canonical state again, read `crypsa/crypsa_event_graph.py` next, especially the replay and branch-row helpers.

That replay path is easiest to follow in stages:

1. sort accepted events stably
2. walk `lineage_parent` backward from the selected head
3. replay those payloads forward into visible canonical state

If you want the accepted payload shapes themselves, read `PlacedObjectPayload` and `DestroyedObjectPayload` in `crypsa/runtime_models.py` before returning to replay code.

## `selection`

This section stores the currently viewed canonical position in the event graph:

- `branch`
- `event_id`
- `teaching_example_loaded`

`event_id` is the selected canonical event being viewed. If it is `null`, the prototype is viewing the root baseline.

`teaching_example_loaded` marks whether the current runtime state came from the built-in teaching example loader.

This section changes what history point replay starts from. It does not store a second canonical world state.

## `logs`

This section stores recent UI logs:

- `server`
- `observer`
- `server_serial`
- `observer_serial`

These logs are teaching and inspection aids. They are not canonical truth.

## Fresh Install Baseline

A fresh install baseline should look like this:

- no canonical events
- `next_sequence = 1`
- `next_object_id = 1`
- observer at `(4, 4)` facing `north`
- `branch = "main"`
- `event_id = null`
- no invariant-boundary candidates
- empty server and observer logs

This baseline corresponds to the runtime's empty replay state before any accepted canonical events exist.
