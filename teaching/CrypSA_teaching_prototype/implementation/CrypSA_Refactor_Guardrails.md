> Scope note: This document reflects the teaching prototype implementation at the time it was completed.
>
> It may not match the current CrypSA specification.
>
> The prototype is preserved as a teaching artifact and is not updated to reflect ongoing architectural changes.
>
> For current system behavior, refer to `../../../spec/`.

# CrypSA Refactor Guardrails

> Scope note: This document describes guardrails for the teaching prototype implementation.
>
> It does not define the full CrypSA architecture. For prototype status, refer to `../STATUS.md`.

---

## Purpose

This document defines the architectural guardrails for future refactoring of the CrypSA teaching prototype.

The major structural refactors have already been implemented.

The goal now is not to reinvent the architecture.

The goal is to:

- protect clear boundaries  
- prevent drift back into controller-heavy design  
- keep future changes selective and justified  

---

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

---

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

---

## The Current Layer Model

The teaching prototype is structured as:

1. Runtime / Controller  
2. Validation / Apply / Reconciliation  
3. Replay / Event Graph  
4. Adapter Layer (Translation)  
5. Lens + Request Layer (Interpretation + Intent)  
6. UI Layer (Experience)  
7. Mint Layer (Structure)  

Future refactors should reinforce this layering, not blur it.

---

## Global Rules

### Rule 1 — Only Extract When the Destination Is Obvious

Do not split code merely because a file feels large.

Only extract code when:

- the extracted piece has a clear identity  
- the extracted piece maps to an existing layer  
- the extracted piece has a stable reason to exist  

Good extraction:

- replay logic → replay module  
- validation logic → validation module  
- request routing → request dispatch  

Bad extraction:

- splitting one controller method across multiple files without a real boundary  
- creating vague helper modules with unstable responsibilities  

---

### Rule 2 — Do Not Chase a Perfectly Thin Controller

The controller is allowed to orchestrate.

It should not own every concern inline, but it does not need to disappear.

Do not refactor just to make the controller look small.

Refactor only when:

- duplication appears  
- a coordination pattern becomes reusable  
- a clear boundary already exists elsewhere  

---

### Rule 3 — Prefer Explicitness Over Cleverness

This is a teaching prototype.

That means:

- readable beats clever  
- explicit beats magical  
- stable beats elegant abstraction  

A small amount of repetition is acceptable if it keeps layer boundaries obvious.

---

## Runtime / Controller Guardrails

The runtime/controller layer owns:

- orchestration  
- action coordination  
- candidate event creation  
- the bridge between user intent and canonical event history  

It must not drift into:

- UI rendering logic  
- adapter shaping  
- replay implementation details  
- Mint editor implementation  
- persistence or file-format parsing  

Allowed:

- calling runtime actions  
- triggering replay  
- coordinating request handling  
- scheduling UI updates  

Not allowed:

- reshaping UI view models inline  
- embedding validation rules inline  
- embedding replay algorithms inline  

---

## Validation / Apply / Reconciliation Guardrails

This layer defines how candidate events become canonical events.

It owns:

- validation (schema → identity → preconditions → invariants → rules)  
- canonical event acceptance  
- assignment of `server_sequence`  
- canonical event creation and append  

It must not:

- perform UI work  
- perform replay  
- shape adapter outputs  
- contain presentation logic  

---

## Replay / Event Graph Guardrails

Replay and event-graph logic own:

- canonical event history traversal  
- event ordering  
- deterministic reconstruction of derived canonical state  

They must remain separate from:

- UI  
- validation  
- request dispatch  
- controller-specific orchestration  

Allowed:

- derive state from canonical event history  
- traverse event lineage  
- reconstruct state deterministically  

Not allowed:

- mutate UI  
- validate candidate events  
- dispatch actions  
- perform persistence side effects  

Specific rule:

Do not collapse:

- `canonical_replay.py`  
- `crypsa_event_graph.py`  

back into a single ambiguous module without strong justification.

---

## Adapter Guardrails (Translation Layer)

Adapters translate data.

They do not define truth.

Allowed:

- reshape canonical and observer data  
- aggregate inputs  
- produce structured outputs for lenses or UI  

Not allowed:

- mutate canonical event history  
- enforce invariants  
- validate events  
- decide system behavior  
- trigger side effects  

Specific rule:

If an adapter starts making decisions, it is no longer an adapter.

Move that logic into:

- runtime actions  
- validation  
- reconciliation  
- controller coordination  

---

## Lens Guardrails (Interpretation Layer)

Lenses interpret data.

They do not define truth.

Allowed:

- visibility filtering  
- observer-specific meaning  
- interaction interpretation  
- presentation-oriented derivation  

Not allowed:

- mutating runtime state  
- validating actions  
- depending on unrelated lens internals  
- bypassing adapters to access raw runtime structures unnecessarily  

Specific rule:

Lenses should consume adapter-shaped data whenever practical.

---

## Request Guardrails

Requests carry intent.

They do not contain logic.

Allowed:

- represent user intent  
- carry structured payloads  
- provide stable dispatch inputs  

Not allowed:

- validate themselves  
- mutate runtime state  
- contain branching logic  
- interpret meaning  

Specific rule:

If a request object starts deciding behavior, it is no longer just a request.

---

## Request Dispatch Guardrails

Request dispatch routes intent.

It must not become a hidden controller.

Allowed:

- map request type to runtime actions  
- perform straightforward routing  

Not allowed:

- embed validation rules  
- perform replay  
- shape UI data  
- coordinate unrelated workflows  

Specific rule:

If dispatch becomes condition-heavy, logic likely belongs in:

- runtime actions  
- controller coordination  
- reconciliation  

---

## UI Guardrails (Experience Layer)

The UI layer presents and collects input.

It must remain non-authoritative.

Allowed:

- render adapter + lens outputs  
- emit typed requests  
- display feedback  

Not allowed:

- mutate canonical event history  
- call validation directly  
- perform replay  
- bypass request dispatch  

Specific rule:

If UI modules gain knowledge of runtime internals, move that behind:

- adapters  
- requests  
- controller coordination  

---

## Mint Guardrails (Structure Layer)

Mint is a definition system, not runtime authority.

Allowed:

- define genomes and schemas  
- define invariant inputs and allowed transitions  
- normalize catalog structures  

Not allowed:

- mutate canonical event history  
- bypass validation  
- act as a runtime execution layer  

Specific rule:

Mint defines what is possible.  
Runtime determines what becomes canonical.

---

## Test Guardrails

Tests should protect architectural boundaries.

Prefer tests that verify:

- validation outcomes  
- canonical event application  
- replay correctness  
- request routing  
- adapter outputs  
- fixture loading  

Avoid excessive UI-heavy testing unless justified by real risk.

---

## Typing Guardrails

Do not treat “more types everywhere” as the goal.

Add typing when:

- structures cross module boundaries frequently  
- shared seams become unstable  
- bugs arise from ambiguous data  

Allow some dynamic structures where they improve clarity in a teaching context.

---

## Documentation Guardrails

Keep documentation aligned with code:

- README and entry points  
- walkthrough docs  
- architecture and implementation docs  
- summary and handoff documents  

Do not allow documentation drift that misrepresents the system.

---

## What We Are Not Trying To Do

We are not trying to:

- turn the prototype into a framework  
- treat it as production runtime  
- split every large file  
- type every structure  
- restart architectural redesign  

---

## Good Refactor Triggers

A refactor is justified when:

- a boundary is already clear  
- duplication appears  
- shared seams create maintenance pain  
- tests become harder due to blurred responsibilities  
- a layer begins absorbing incorrect responsibilities  

---

## Bad Refactor Triggers

A refactor is not justified when:

- a file simply feels large  
- changes are aesthetic only  
- abstraction is added prematurely  
- complexity is moved rather than reduced  
- the teaching model becomes harder to explain  

---

## Quick Safety Checklist

Before refactoring, ask:

1. What layer does this belong to?  
2. Does the destination already have a clear identity?  
3. Will this make the architecture easier to explain?  
4. Am I reducing coupling, or just moving it?  
5. Am I protecting the teaching model, or obscuring it?  

If the answers are unclear, do not refactor yet.

---

## Key Insight

> The goal is not to improve the code endlessly.
> The goal is to preserve a clear, teachable architecture.

---

## One Sentence Summary

Future CrypSA teaching prototype refactors should be selective, boundary-aware, and architecture-protective, reinforcing the existing layered design while preserving clarity of canonical event history, validation, replay, and observer experience.
