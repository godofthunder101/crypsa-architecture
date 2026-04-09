# CrypSA Minimal Validator Folder Structure

---

## ⚠️ Implementation Guidance (Non-Authoritative)

This document provides one possible file and module structure for a CrypSA minimal validator.

👉 This structure is not required, but is designed to maintain clear architectural boundaries.

👉 CrypSA defines invariants and behavior through the `/spec` directory.

👉 Alternative structures may be used, as long as CrypSA invariants are preserved.

---

## Purpose

This document provides a clean file and module structure for building **CrypSA Minimal Validator v0.1**.

Its goal is to make the minimal validator:

* easy to understand
* easy to implement incrementally
* aligned with the CrypSA runtime model
* easy to grow later without architectural drift

This is an implementation guide, not a specification.

---

## Core Principle

> Organize the validator around responsibilities, not convenience.

The minimal validator should reflect the same core runtime boundaries that exist in the architecture:

* event intake
* validation
* canonical event history
* derived canonical state
* transport
* observer/session coordination
* replay and snapshots

The file structure is intended to reinforce those boundaries.

---

## Recommended Top-Level Structure (Example)

```text
minimal-validator/
├── src/
│   ├── main.ts
│   ├── config/
│   │   └── validator-config.ts
│   ├── transport/
│   │   ├── websocket-server.ts
│   │   ├── message-types.ts
│   │   └── session-manager.ts
│   ├── events/
│   │   ├── candidate-event-types.ts
│   │   ├── canonical-event-types.ts
│   │   ├── event-intake.ts
│   │   └── event-idempotency.ts
│   ├── validation/
│   │   ├── validation-pipeline.ts
│   │   ├── schema-validation.ts
│   │   ├── identity-validation.ts
│   │   ├── precondition-validation.ts
│   │   ├── invariant-validation.ts
│   │   ├── rule-validation.ts
│   │   └── conflict-scope-resolver.ts
│   ├── history/
│   │   ├── canonical-event-history.ts
│   │   ├── sequence-generator.ts
│   │   └── event-store.ts
│   ├── state/
│   │   ├── derived-state.ts
│   │   ├── state-queries.ts
│   │   ├── state-apply-event.ts
│   │   └── identity-registry.ts
│   ├── replay/
│   │   ├── replay-engine.ts
│   │   └── replay-from-sequence.ts
│   ├── snapshots/
│   │   ├── snapshot-types.ts
│   │   ├── snapshot-store.ts
│   │   └── snapshot-generator.ts
│   ├── runtime/
│   │   ├── validator-runtime.ts
│   │   ├── submit-candidate-event.ts
│   │   ├── broadcast-canonical-event.ts
│   │   └── reconnect-flow.ts
│   └── utils/
│       ├── result.ts
│       ├── time.ts
│       └── logging.ts
├── data/
│   ├── events/
│   └── snapshots/
├── tests/
│   ├── validation/
│   ├── replay/
│   ├── conflicts/
│   └── reconnect/
├── package.json
├── tsconfig.json
└── README.md
```

---

## File Responsibilities

---

### `src/main.ts`

Entry point.

Responsible for:

* loading config
* starting the validator runtime
* starting transport
* wiring components together

This file should stay thin.

It should not contain business logic.

---

### `src/config/validator-config.ts`

Defines runtime configuration, such as:

* port
* snapshot frequency
* data paths
* logging behavior

Keep configuration separate from logic.

---

## Transport Layer

These files handle communication with observers.

---

### `src/transport/websocket-server.ts`

May handle:

* accepting observer connections
* receiving inbound messages
* sending outbound messages

This file should only deal with transport concerns, not validation logic.

---

### `src/transport/message-types.ts`

Defines transport message shapes, such as:

* candidate event submission
* event result
* canonical event broadcast
* reconnect request
* snapshot delivery

This keeps message contracts explicit.

---

### `src/transport/session-manager.ts`

Typically responsible for:

* tracking connected observers
* storing last known `server_sequence`
* identifying which observers need which updates

This is observer/session coordination, not truth logic.

---

## Event Layer

These files define event shapes and intake behavior.

---

### `src/events/candidate-event-types.ts`

Defines the structure of candidate events.

Examples:

* `event_id`
* `event_type`
* `actor_id`
* `target_ids`
* `payload`
* `precondition_refs`

---

### `src/events/canonical-event-types.ts`

Defines the structure of canonical events.

Examples:

* `canonical_event_id`
* `source_event_id`
* `server_sequence`
* `accepted_at`

---

### `src/events/event-intake.ts`

May Handle:

* parsing incoming event messages
* checking required fields exist
* normalizing shape before validation

This is intake preparation, not full validation.

---

### `src/events/event-idempotency.ts`

May Handle:

* tracking processed `event_id`s
* preventing duplicate canonicalization
* mapping duplicates to prior outcomes

This is critical to correctness.

---

## Validation Layer

These files implement the validator’s decision process.

---

### `src/validation/validation-pipeline.ts`

Main validation orchestrator.

Responsible for calling, in order:

* schema validation
* identity validation
* precondition validation
* invariant validation
* rule validation

This should return a clear accept/reject result.

---

### `src/validation/schema-validation.ts`

Checks structural correctness.

Examples:

* required fields present
* correct data types
* valid payload structure

---

### `src/validation/identity-validation.ts`

Checks identity correctness.

Examples:

* actor exists
* target exists
* identity references are valid

---

### `src/validation/precondition-validation.ts`

Checks whether assumptions still hold.

Examples:

* tile still empty
* ownership unchanged
* resource still available

---

### `src/validation/invariant-validation.ts`

Checks system-wide truth constraints.

Examples:

* no duplicate occupancy
* no invalid resource states
* no impossible canonical state transitions

---

### `src/validation/rule-validation.ts`

Checks event-specific rules.

Examples:

* placement allowed
* upgrade requirements met
* transfer valid

---

### `src/validation/conflict-scope-resolver.ts`

Typically responsible for:

* identifying affected conflict scope
* locking or isolating validation context
* ensuring atomicity within the scope

This is one of the most important files in the runtime.

---

## History Layer

These files maintain canonical truth.

---

### `src/history/canonical-event-history.ts`

May handle:

* appending canonical events
* reading ordered history
* exposing history queries

This represents the canonical log.

---

### `src/history/sequence-generator.ts`

Responsible for:

* assigning `server_sequence`
* ensuring strictly increasing canonical order

Keep sequence assignment explicit and isolated.

---

### `src/history/event-store.ts`

Typically responsible for:

* writing canonical events to storage
* reading persisted canonical events from disk

In v0.1, this can be a simple append-only file.

---

## State Layer

These files maintain derived canonical state.

---

### `src/state/derived-state.ts`

Represents in-memory derived canonical state.

This is:

* useful
* queryable
* non-authoritative

It must always remain reconstructable from canonical event history.

---

### `src/state/state-queries.ts`

Defines read helpers over derived state.

Examples:

* get tile occupancy
* get player resources
* get object status

Keep read logic separate from mutation logic.

---

### `src/state/state-apply-event.ts`

May handle:

* applying one canonical event to derived canonical state
* ensuring deterministic state transitions

This file is central to replay correctness.

---

### `src/state/identity-registry.ts`

Tracks identity-related derived information, such as:

* object existence
* lifecycle status
* genome references

Useful for validation and replay.

---

## Replay Layer

These files reconstruct derived state from canonical history.

---

### `src/replay/replay-engine.ts`

Typically responsible for:

* reconstructing derived state from history
* replaying events in `server_sequence` order
* producing deterministic results

---

### `src/replay/replay-from-sequence.ts`

Responsible for:

* replaying only an event tail
* supporting reconnect and snapshot usage

Useful for partial replay.

---

## Snapshot Layer

These files improve practicality.

---

### `src/snapshots/snapshot-types.ts`

Defines snapshot structure.

Examples:

* derived state
* snapshot sequence
* schema version

---

### `src/snapshots/snapshot-store.ts`

Typically responsible for:

* reading and writing snapshots
* managing snapshot file storage

---

### `src/snapshots/snapshot-generator.ts`

May handle:

* creating snapshots from current derived canonical state
* tagging them with `server_sequence`

---

## Runtime Layer

These files coordinate the overall validator flow.

---

### `src/runtime/validator-runtime.ts`

Main runtime coordinator.

Responsible for:

* initializing components
* accepting candidate events
* running validation
* canonicalizing accepted events
* triggering updates and broadcasts

This is the heart of the implementation.

---

### `src/runtime/submit-candidate-event.ts`

Handles one candidate event submission flow.

Suggested responsibilities:

* event intake
* idempotency check
* validation pipeline
* acceptance/rejection result

This is a good file to unit test heavily.

---

### `src/runtime/broadcast-canonical-event.ts`

Responsible for:

* sending canonical updates to observers
* formatting transport messages
* coordinating with session manager

---

### `src/runtime/reconnect-flow.ts`

Responsible for reconnect support.

Examples:

* find last known `server_sequence`
* load snapshot
* send event tail
* restore observer consistency

---

## Utilities

---

### `src/utils/result.ts`

Defines shared result types.

Examples:

* `ok / error`
* validation result
* rejection result

This improves consistency across modules.

---

### `src/utils/time.ts`

Centralized timestamp helpers.

Useful for:

* `accepted_at`
* logging
* consistent formatting

---

### `src/utils/logging.ts`

Defines logging helpers.

Keep logging consistent and centralized.

---

## Data Directory

```text
data/
├── events/
└── snapshots/
```

Use this for local persistence in v0.1.

Examples:

* append-only canonical event file
* latest snapshot file

Keep it simple.

---

## Test Structure

```text
tests/
├── validation/
├── replay/
├── conflicts/
└── reconnect/
```

Recommended focus:

### `tests/validation/`

Prove:

* valid events are accepted
* invalid events are rejected

### `tests/replay/`

Prove:

* same history → same state
* snapshot + tail = full replay

### `tests/conflicts/`

Prove:

* one event wins
* losing conflicts are rejected
* validation is atomic within scope

### `tests/reconnect/`

Prove:

* late join works
* reconnect restores consistency

---

## Example Build Order

If you want to implement this incrementally, one possible sequence is:

1. `candidate-event-types.ts`
2. `canonical-event-types.ts`
3. `event-intake.ts`
4. `canonical-event-history.ts`
5. `sequence-generator.ts`
6. `derived-state.ts`
7. `state-apply-event.ts`
8. `validation-pipeline.ts`
9. validation submodules
10. `validator-runtime.ts`
11. `websocket-server.ts`
12. snapshots
13. reconnect flow

---

## Design Rules

### 1. Keep truth separate from transport

Transport should move data.

It should not decide truth.

---

### 2. Keep replay real

Do not “fake” replay with direct mutable state shortcuts.

Derived state must remain reconstructable.

---

### 3. Keep validation explicit

Do not hide validation inside UI or observer code.

Validation belongs to the validator.

---

### 4. Keep canonical event history append-only

Never rewrite accepted canonical history.

---

## Key Insight

> A clean validator structure makes CrypSA easier to build without collapsing its architecture.

If your files mix:

* validation
* state mutation
* transport
* observer logic

then the implementation will drift away from CrypSA.

---

## Summary

This folder structure organizes the minimal validator around:

* candidate event intake
* validation
* canonical history
* derived state
* replay
* transport
* snapshots
* reconnect support

That structure mirrors the architecture and makes the minimal validator easier to implement correctly.

---

## One Sentence Summary

A good minimal CrypSA validator structure keeps validation, canonical history, derived state, replay, transport, and observer coordination clearly separated so the architecture remains correct as the system grows.
