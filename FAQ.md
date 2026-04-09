# CrypSA FAQ

This document answers common questions about CrypSA.

It focuses on clarifying behavior, tradeoffs, and concerns — not teaching the system.

For a quick explanation, see:

* `CrypSA_In_5_Minutes.md`

For the authoritative adapter and observer-model docs, see:

* `architecture/CrypSA_Adapter_Model.md`
* `architecture/CrypSA_Observer_Model.md`

---

## What is CrypSA in simple terms?

CrypSA is an event-driven architecture where:

* observers simulate locally
* actions are proposed as candidate events
* a validator evaluates those events
* if accepted, an event becomes canonical and is appended to canonical event history

👉 Canonical event history is the source of truth.

---

## Does CrypSA require a server?

No.

CrypSA requires a **validator**, not a server.

> A validator is a role, not a location.

The validator may run:

* locally
* on a host (one observer acts as validator)
* on a dedicated remote system (server deployment)

A server is simply one way to deploy a validator.

---

## Can CrypSA work offline?

Yes.

CrypSA fully supports offline operation using a **local validator**.

In this mode:

* the observer and validator run together
* canonical event history is maintained locally
* validation still occurs
* the full runtime model remains intact

This is not a simplified mode — it is a valid CrypSA deployment.

---

## What happens if the connection drops?

It depends on how the system is deployed.

### If using a remote validator

* the observer continues local simulation
* no new canonical events can be accepted
* canonical updates stop arriving
* local derived state may temporarily diverge

When the connection is restored:

* canonical updates are fetched
* canonical event history is synchronized
* reconstruction via canonical event replay occurs
* the observer converges to derived canonical state

---

### If using a local validator

* the system continues operating normally
* validation still occurs locally
* canonical event history continues uninterrupted

---

## Is CrypSA validator authoritative?

Yes — but differently than traditional systems.

The validator does not simulate everything.

Instead:

> The validator defines what becomes canonical.

It is authoritative over:

* which events are accepted
* what becomes canonical event history

---

## Does CrypSA trust the observer?

No.

Observers can propose events, but:

* all canonical changes must be validated
* invalid or conflicting events are rejected

Observers simulate freely, but:

> Only accepted events become canonical and are appended to canonical event history.

Observers do not define truth.

---

## Then why allow observer-side simulation?

CrypSA separates:

* simulation (observer-side)
* truth (validator-controlled)

This allows:

* responsiveness
* flexibility
* reduced synchronization overhead

The validator still defines what becomes canonical.

---

## Is this just event sourcing?

It is similar, but not identical.

Event sourcing:

* stores a history of events

CrypSA:

* uses validated events to define shared reality
* includes invariant enforcement as a core responsibility
* explicitly models observers and reconstruction via canonical event replay

---

## Is CrypSA peer-to-peer?

Not exactly.

CrypSA is **validator-based**, not strictly peer-to-peer or server-based.

It can be deployed as:

* local-only
* host-based
* dedicated validator

The architecture defines how truth is determined, not how networking must be structured.

---

## What does the validator actually do?

The validator:

* receives candidate events
* validates them
* enforces invariants
* assigns canonical ordering (`canonical_sequence`)
* if accepted, an event becomes canonical and is appended to canonical event history

It does not need to simulate the entire world continuously.

---

## What happens if two observers act at the same time?

Both actions may be submitted.

The validator:

* evaluates both
* accepts one valid event
* rejects the other

Only the accepted event becomes canonical.

The rejected observer reconciles via canonical event replay.

---

## What happens when the observer is wrong?

If an observer predicts incorrectly:

* the validator rejects the event
* the observer corrects its local state via canonical event replay

This is expected and correct behavior.

---

## How does CrypSA prevent observer-side logic from breaking the system?

CrypSA enforces strict separation of responsibilities:

* the validator defines what becomes canonical
* canonical event history is the source of truth
* derived state is reconstructed via replay

In addition:

* observers emit candidate events representing intent
* canonical changes occur only through validation
* adapters and lenses prevent direct access to runtime internals

---

## Is CrypSA deterministic?

Yes — at the canonical level.

Given the same:

* canonical event history
* validation rules
* interpretation logic

All observers must derive equivalent state via canonical event replay.

---

## Does CrypSA store world state?

Not as truth.

* canonical truth = canonical event history
* derived state = reconstructed via replay
* snapshots = reconstruction checkpoints

---

## What are snapshots?

Snapshots are stored derived state used to:

* speed up loading
* reduce replay cost
* support recovery

They do not replace canonical event history.

---

## Can I start building CrypSA locally and scale later?

Yes — this is a core design goal.

CrypSA supports a **local-first development model**:

```text
Local Validator → Host-Based → Dedicated Validator
```

You can:

* start with a local validator
* build and test the full system offline
* later move validation to a remote system

Without changing:

* event structure
* validation logic
* replay model
* truth definition

👉 For how to actually build CrypSA step-by-step, see:

`implementation/CrypSA_Local_First_Development_Approach.md`

---

## Does CrypSA support real-time gameplay?

Yes, with tradeoffs.

Works best for:

* persistent worlds
* simulation systems
* object-driven interactions

Less suited for:

* twitch combat
* frame-perfect PvP
* heavy physics systems

---

## What is the current state of the project?

CrypSA is:

* a defined architecture
* supported by specifications
* backed by a teaching prototype

It does not yet include a full reference implementation or minimal validator.

---

## Where should I start?

1. `CrypSA_In_One_Diagram.md`
2. `CrypSA_In_5_Minutes.md`
3. `CrypSA_Terminology_Primer.md`
4. `CrypSA_Worked_Example.md`

---

## One Sentence Summary

CrypSA is a system where observers simulate locally, a validator evaluates candidate events, and canonical event history defines shared reality.
