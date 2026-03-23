# Prototype vs Current CrypSA Model

## Purpose

This document explains how the minimal teaching prototype relates to the newer CrypSA material in `repo/`.

Use it when you want to answer:

- what this prototype teaches directly
- what it simplifies on purpose
- what belongs in the broader CrypSA architecture and spec docs instead

This is a teaching crosswalk, not a replacement for `repo/`.

## Short Version

The prototype is meant to match the current CrypSA model at the concept level while staying much smaller at the implementation level.

It should stay faithful about:

- observer-local simulation
- candidate events waiting at the invariant boundary
- canonical validation before acceptance
- accepted canonical events as shared truth
- replay-derived canonical state
- Mint-authored definitions and invariant rules as structural inputs

It is allowed to stay simplified about:

- transport and networking
- snapshot systems
- distributed deployment concerns
- richer identity/versioning layers
- production reliability and anti-cheat concerns

The rule is:

- align the model
- simplify the runtime shape
- make the simplifications explicit

Another useful rule:

- if the prototype teaches a core CrypSA idea, keep it accurate
- if the broader `repo/` adds deployment or architecture depth, do not force all of that depth into this app

## What This Prototype Teaches Directly

The teaching prototype is already aligned with the current CrypSA model on these points:

1. Observers can act locally before anything becomes canonical.
2. Canonical-affecting actions become candidate events at the invariant boundary.
3. The canonical side validates those candidate events instead of treating local simulation as truth.
4. Accepted canonical events become the authoritative history.
5. Visible canonical state is derived by replaying accepted canonical history.
6. Selecting older accepted history changes the replay-derived view.
7. Reconciling from older accepted history can fork visible event lineage.
8. Mint definitions and invariant rules matter structurally, not cosmetically.

## Teaching Simplifications

These simplifications are intentional and should stay visible in the docs:

### Single-process teaching app

The prototype is one local Tk application.

It does not model:

- network transport
- separate deployed observer and canonical processes
- out-of-order delivery
- retries or distributed fault handling

### Direct replay without snapshot machinery

The current CrypSA material includes a broader replay/snapshot story.

The prototype keeps the simpler teaching version:

- accepted canonical history is stored
- visible canonical state is replay-derived directly from that history

That is a good simplification for teaching.

### Compressed runtime structure

The broader CrypSA material separates more concerns around:

- canonical history
- identity and definition references
- derived state materialization
- snapshots
- transport and consistency behavior

The prototype compresses those into a smaller in-memory runtime so the teaching loop is easier to follow.

### Narrower validation model

The broader CrypSA material has room for richer preconditions and validation structures.

The prototype teaches the narrower version through:

- invariant rules
- candidate events
- `lineage_parent`
- `causal_references`

That is still faithful to the model, just smaller.

## Intentionally Out Of Scope

The following topics belong primarily to `repo/`, not this teaching app:

- full transport architecture
- snapshot recovery and late join behavior
- distributed consistency details
- richer identity/versioning machinery
- production anti-cheat and anomaly handling
- storage/partitioning/deployment architecture

If a question starts moving in that direction, the prototype should point outward instead of pretending to model those concerns fully.

## Terminology Alignment

The newer CrypSA material is more consistent about a few phrases. This prototype should prefer the same wording:

- `candidate event` over vague `queued action` wording when the action is waiting for canonical validation
- `canonical validation` or `canonical validator` over wording that implies the server is the primary simulator
- `accepted canonical history` for the authoritative event log
- `replay-derived canonical state` for the left-pane world view
- `reconcile to canonical truth` for the observer-side catch-up story

The prototype can still use shorter UI wording where needed, but the docs should stay precise.

## How To Read Both Repos Together

Use this order if you want the teaching view first and the broader CrypSA model second:

1. `README.md`
2. `codebase_walkthrough.md`
3. this document
4. `repo/CrypSA_in_5_minutes.md`
5. `repo/CrypSA_architecture_overview.md`
6. `repo/core_concepts/` and `repo/architecture/`
7. `repo/spec/`

That order gives you:

1. the small teaching loop
2. the local code path
3. the scope boundary
4. the broader architecture and spec framing

## Practical Rule For Future Changes

When updating the prototype, ask:

1. Is this part of the core CrypSA model?
2. If yes, is the prototype still teaching it accurately?
3. If not, is this just a safe teaching simplification?
4. If it is a simplification, is that simplification stated clearly somewhere?

If the answer to the last question is no, the docs should usually be updated alongside the code.
