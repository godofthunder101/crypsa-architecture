# CrypSA Refactor Guardrails

## Purpose

This document defines the architectural guardrails for future refactoring of the CrypSA teaching prototype.

The major structural refactors have already been implemented.

The goal now is not to reinvent the architecture.

The goal is to:

- protect clear boundaries
- prevent drift back into controller-heavy design
- keep future changes selective and justified

## Current Architectural Phase

The teaching prototype is no longer in a:

- "fix the obvious architecture problems"

phase.

It is now in a:

- "protect and refine the architecture"

phase.

That means future refactors should be:

- targeted
- boundary-aware
- driven by real pressure
- not cosmetic

## Core Principle

Refactors should make the architecture clearer, not merely more abstract.

Prefer:

- explicit boundaries
- boring modules
- direct data flow
- obvious ownership

Avoid:

- framework-ization
- premature abstraction
- splitting files just to make them smaller
- moving logic into the wrong layer for neatness

## The Current Layer Model

The teaching prototype is structured as:

1. Runtime / Controller
2. Replay / Event Graph
3. Adapter Layer
4. Lens + Request Layer
5. UI Layer
6. Mint Layer

Future refactors should reinforce this layering, not blur it.

## Global Rules

### Rule 1 - Only Extract When the Destination Is Obvious

Do not split code merely because a file feels large.

Only extract code when:

- the extracted piece has a clear identity
- the extracted piece maps to an existing layer
- the extracted piece has a stable reason to exist

Good extraction:

- replay logic -> replay module
- validation logic -> validation module
- request routing -> request dispatch

Bad extraction:

- splitting one controller method across three files without a real boundary
- creating vague helper modules with unstable responsibilities

### Rule 2 - Do Not Chase a Perfectly Thin Controller

The controller is allowed to orchestrate.

It should not own every concern inline, but it does not need to disappear.

Do not refactor just to make the controller look small.

Refactor only when:

- duplication appears
- a coordination pattern becomes reusable
- a clear boundary already exists elsewhere

### Rule 3 - Prefer Explicitness Over Cleverness

This is a teaching prototype.

That means:

- readable beats clever
- explicit beats magical
- stable beats elegant-looking abstraction

A small amount of repetition is acceptable if it keeps layer boundaries obvious.

## Runtime / Controller Guardrails

The runtime/controller layer owns:

- orchestration
- action coordination
- top-level meaning
- the bridge between user intent and canonical outcomes

It must not drift into:

- UI rendering logic
- adapter shaping
- replay implementation details
- Mint editor implementation
- file-format parsing details

Allowed:

- calling runtime actions
- triggering replay
- coordinating request handling
- scheduling UI refresh

Not allowed:

- manually reshaping UI view models inline
- embedding validation rules inline
- embedding replay algorithms inline

## Replay / Event Graph Guardrails

Replay and event-graph logic own:

- canonical derivation
- lineage
- event ordering
- branch-aware reconstruction

They must remain separate from:

- UI
- validation
- request dispatch
- controller-specific behavior

Allowed:

- derive state from accepted canonical history
- traverse event lineage
- reconstruct branch-selected state

Not allowed:

- mutate UI
- validate candidates
- dispatch actions
- perform persistence side effects

Specific rule:

Do not collapse:

- `canonical_replay.py`
- `crypsa_event_graph.py`

back into one vague replay blob unless there is a very strong reason.

## Adapter Guardrails

Adapters translate data.

They do not define truth.

Allowed:

- reshape runtime data
- aggregate canonical and observer state
- produce stable outputs for lenses or UI

Not allowed:

- mutate canonical state
- enforce invariants
- validate events
- decide system behavior
- trigger side effects

Specific rule:

If an adapter starts doing decision-making, it is no longer just an adapter.

Move that logic back into:

- runtime actions
- validation
- reconciliation
- controller coordination

## Lens Guardrails

Lenses interpret data.

They do not translate raw runtime state from scratch, and they do not own truth.

Allowed:

- visibility filtering
- observer-specific meaning
- interaction interpretation
- presentation-oriented interpretation

Not allowed:

- mutating runtime state
- validating actions
- depending directly on unrelated lens internals
- digging through raw runtime structures when adapted inputs exist

Specific rule:

Lenses should consume adapted data whenever practical.

## Request Guardrails

Requests carry intent.

They do not contain business logic.

Allowed:

- identify user intent
- carry small structured payloads
- provide stable dispatch input

Not allowed:

- validate themselves
- mutate runtime state
- contain branching behavior
- perform interpretation logic

Specific rule:

If a request object starts acquiring methods that decide behavior, it is drifting out of role.

## Request Dispatch Guardrails

Request dispatch routes intent.

It must not become the new hidden controller.

Allowed:

- map request type to runtime action
- perform straightforward routing

Not allowed:

- embed validation rules
- perform replay
- shape UI data
- coordinate unrelated workflows inline

Specific rule:

If dispatch starts growing condition-heavy behavior, that logic probably belongs in:

- runtime actions
- controller coordination
- reconciliation

## UI Guardrails

The UI layer presents and collects input.

It should remain read-only with respect to canonical truth.

Allowed:

- render adapted and lens-shaped data
- emit typed requests
- show status and feedback

Not allowed:

- mutate canonical state directly
- call validation directly
- build replay state
- bypass request dispatch for meaningful behavior

Specific rule:

If a UI module starts knowing too much about runtime internals, move that knowledge behind:

- adapters
- requests
- controller coordination

## Mint Guardrails

Mint is a definition system, not runtime authority.

Allowed:

- define object schemas
- define transitions and rules
- author reusable definitions
- normalize catalog structures

Not allowed:

- bypass runtime validation
- mutate canonical truth directly
- become a hidden runtime execution layer

Specific rule:

Mint defines what is possible.

Runtime decides what actually becomes canonical.

## Test Guardrails

The test suite should remain focused on architectural boundaries.

Prefer tests that protect:

- validation outcomes
- canonical apply behavior
- replay derivation
- request routing
- adapter output contracts
- fixture loading
- shared typed seams

Do not bloat the suite with large amounts of low-value UI automation unless a real risk justifies it.

## Typing Guardrails

Do not treat "more types everywhere" as the goal.

Add typing when:

- a shape crosses module boundaries often
- a shared seam becomes hard to maintain
- bugs or drift come from ambiguous structure

Keep some inner maps dynamic if that genuinely helps the teaching prototype stay flexible.

## Documentation Guardrails

As code changes, keep these aligned:

- README and start-here docs
- codebase walkthrough
- reference docs
- implementation-layer docs
- summary and handoff docs

Do not let docs fall far enough behind the code that reviewers get an outdated picture of the architecture.

## What We Are Not Trying To Do

We are not trying to:

- framework-ize the prototype
- pretend the teaching prototype is a production runtime
- split every large file into tiny files
- type every dynamic structure
- replace selective refinement with another broad architecture campaign

## Good Refactor Triggers

A refactor is likely justified when:

- a module boundary is already clear
- duplication is appearing
- a shared seam is causing real maintenance pain
- tests are getting harder because responsibilities are blurred
- a layer is starting to absorb behavior that belongs elsewhere

## Bad Refactor Triggers

A refactor is probably not justified when:

- a file just feels big
- a module could be split purely for aesthetic reasons
- abstraction is added before repeated need appears
- complexity is moved instead of reduced
- the result makes the teaching model harder to explain

## Quick Safety Checklist

Before making a refactor, ask:

1. What layer does this belong to?
2. Does the destination already have a clear identity?
3. Will this make the architecture easier to explain?
4. Am I reducing coupling, or just moving it?
5. Am I protecting the teaching model, or obscuring it?

If the answers are unclear, do not refactor yet.

## One Sentence Summary

Future CrypSA teaching prototype refactors should be selective, boundary-aware, and architecture-protective, reinforcing the existing layered design instead of reopening broad structural invention.
