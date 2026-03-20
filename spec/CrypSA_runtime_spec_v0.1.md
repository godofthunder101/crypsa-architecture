---

CrypSA Runtime Spec v0.1

Purpose

This document defines the minimal runtime behavior of a CrypSA system.

It focuses on the path by which local observer actions become canonical events, how those events are validated, how canonical truth is updated, and how observers reconcile to that truth.

This is not a full production protocol. It is the minimum runtime contract needed to make CrypSA technically reviewable and implementable.


---

1. Scope

This v0.1 runtime spec covers:

observer action proposal

candidate event structure

server-side validation

event acceptance and rejection

canonical event recording

canonical update distribution

observer reconciliation

per-object ordering

snapshot-assisted reconstruction


This v0.1 spec does not fully define:

combat adjudication

anti-cheat systems beyond validation boundaries

distributed shard coordination

mergeable offline branches

advanced partitioning

cryptographic trust proofs



---

2. Runtime Roles

A CrypSA runtime contains the following logical roles.

2.1 Observer

A process that:

reconstructs canonical objects locally

simulates local experience

proposes candidate events

reconciles local state with canonical truth


In most games, this is the client.

2.2 Canonical Server

A process that:

receives candidate events

validates them

enforces invariants

records accepted canonical events

distributes canonical updates


2.3 Canonical Truth Store

The persistent runtime store containing:

canonical event log

object identity registry

genome references

derived canonical state

snapshots



---

3. Core Runtime Principle

A player action does not directly modify canonical truth.

Instead, the runtime flow is:

Local Action
→ Candidate Event
→ Server Validation
→ Accept or Reject
→ Canonical Log Update
→ Observer Reconciliation

Only accepted events become canonical.


---

4. Event Classes

CrypSA v0.1 divides events into two broad classes.

4.1 Local-Only Actions

Actions that do not affect canonical truth.

Examples:

camera movement

visual effects

local UI changes

cosmetic preview changes


These never enter canonical history.

4.2 Canonical Candidate Actions

Actions that may affect canonical truth.

Examples:

mint object

place structure

destroy structure

transfer ownership

upgrade item

consume resource


These must cross the invariant boundary and be validated.


---

5. Candidate Event Structure

Each candidate event must contain at minimum:

event_id
event_type
actor_id
target_ids
payload
client_time
branch_id
precondition_refs

5.1 Field Definitions

event_id

A client-generated unique identifier for this proposal.

Purpose:

deduplication

retry safety

rejection/acceptance tracking


event_type

The action being proposed.

Examples:

mint_object

place_structure

upgrade_item

transfer_object


actor_id

Canonical identity of the acting observer or entity.

target_ids

One or more canonical object identities affected by the event.

payload

Event-specific proposed state transition data.

Example:

structure type

target owner

upgrade type

quantity


client_time

Client-local timestamp for debugging and traceability only.

Not authoritative for ordering.

branch_id

The branch/timeline the observer believes it is operating on.

precondition_refs

References to canonical state or prior events that the client assumes are true.

Examples:

current owner expected to be player_A

target tile expected to be empty

item expected to exist and be upgradeable



---

6. Event Ordering Model

CrypSA v0.1 uses:

> server-defined canonical ordering with per-object conflict resolution



6.1 Canonical Order

Accepted events are assigned authoritative order by the canonical server.

Client submission order is not authoritative.

6.2 v0.1 Conflict Scope

v0.1 assumes conflicts are resolved primarily at the level of:

object

tile

inventory slot

ownership target


This means:

two events affecting the same mutually exclusive target are ordered by server acceptance

the first accepted valid event wins

later conflicting proposals are rejected


6.3 No Global Strong Ordering Guarantee

CrypSA v0.1 does not require a globally meaningful simulation order for all events everywhere.

It requires canonical order where invariants depend on it.


---

7. Validation Pipeline

Each candidate canonical event passes through the following validation stages.

7.1 Schema Validation

Check that required fields exist and are well-formed.

Reject if:

fields missing

invalid types

malformed payload


7.2 Identity Validation

Check that referenced canonical identities exist where required.

Reject if:

actor does not exist

target object does not exist

branch reference invalid


7.3 Precondition Validation

Check that the event’s expected world assumptions still hold.

Examples:

target tile still empty

actor still owns object

item still exists

structure still buildable


Reject if assumptions no longer hold.

7.4 Invariant Validation

Check that accepting the event would not violate canonical rules.

Examples:

unique object duplication

invalid placement

impossible ownership state

illegal transition sequence


Reject if any invariant would be broken.

7.5 Rule Validation

Check event-type-specific rules.

Examples:

correct resources available

valid upgrade path

transfer allowed

target state transition permitted by genome


7.6 Acceptance

If all prior stages pass:

event is accepted

event enters canonical history

derived state updates

observers are notified



---

8. Validation Outcomes

Each proposed event results in one of two outcomes.

8.1 Accepted

The server:

assigns canonical sequence metadata

appends event to canonical log

updates derived canonical state

schedules/broadcasts observer updates


8.2 Rejected

The server:

records rejection result for the proposal

does not update canonical truth

returns a rejection reason

expects the observer to reconcile


8.3 Rejection Codes

v0.1 should support at least these rejection classes:

invalid_schema

invalid_identity

invalid_branch

precondition_failed

invariant_violation

rule_violation

conflict_lost



---

9. Canonical Event Recording

Accepted events are recorded in the canonical event log.

Each accepted event should include server-side metadata:

canonical_event_id
source_event_id
server_sequence
accepted_at
branch_id
validation_result = accepted

The canonical event log is append-only in concept.

Historical correction, if needed, occurs through new canonical events or branch changes, not silent mutation of old events.


---

10. Derived Canonical State

CrypSA does not require replay from genesis for every query.

The runtime maintains derived canonical state for efficiency.

Examples:

current owner of object

current upgrade level

current tile occupancy

current structure state

current resource quantity


This derived state must be:

fully derivable from accepted canonical history

treated as a materialized canonical view, not independent truth



---

11. Snapshots

Snapshots are first-class runtime features in v0.1.

11.1 Purpose

Snapshots exist to:

reduce replay cost

support late join

support debugging

support branch restoration


11.2 Snapshot Contents

A snapshot should contain:

branch identifier

canonical sequence position

derived canonical state for relevant scope

object registry state for relevant scope


11.3 Reconstruction Rule

Observers reconstruct from:

Latest Relevant Snapshot
+ Canonical Log Tail

not necessarily from genesis.


---

12. Observer Reconciliation

When canonical updates arrive, the observer must reconcile local simulation.

12.1 If Local Prediction Matches

confirm local state

clear pending proposal markers


12.2 If Local Prediction Differs

correct local representation

remove invalid local objects/states

rebuild affected objects from canonical truth


12.3 Reconciliation Minimum

Observers must be able to:

identify which local proposal was accepted/rejected

rebuild affected canonical objects

update local UI/logs/state accordingly



---

13. Worked Runtime Example: Structure Placement

13.1 Local Action

Observer attempts to place mining_station on tile_42.

13.2 Candidate Proposal

Client sends:

event_type = place_structure
actor_id = player_A
target_ids = [tile_42]
payload = { structure_type: mining_station }
precondition_refs = { tile_42_empty: true }
branch_id = main

13.3 Server Validation

Server checks:

player_A exists

tile_42 exists

tile_42 is still empty

tile_42 is buildable

placement does not violate spatial invariants

actor has required resources


13.4 Accepted Path

If valid:

append canonical event

update tile occupancy

consume resources

notify observers


13.5 Rejected Path

If invalid:

reject proposal with code

canonical truth unchanged

client removes local pending structure during reconciliation



---

14. Applicability of v0.1 Runtime Spec

This runtime model is best suited to systems where:

canonical state transitions matter more than twitch-frame simulation

object history and provenance are important

world mutation is persistent

replay and auditability are valuable


It is not yet a complete fit for:

high-frequency twitch combat

strict real-time PvP adjudication

heavy physics-authoritative action games



---

15. v0.1 Non-Goals

This document does not yet define:

full anti-cheat protocol

multi-region consistency

cryptographic event signing

branch merge semantics

large-scale shard federation

deterministic combat simulation spec


Those belong to later versions.


---

16. Summary

CrypSA v0.1 defines a runtime in which:

observers simulate locally

canonical-affecting actions become candidate events

the server validates those events against schema, identity, preconditions, rules, and invariants

accepted events enter canonical history

derived state and snapshots support efficient reconstruction

observers reconcile to canonical truth



---

One Sentence Summary

CrypSA Runtime Spec v0.1 defines how local observer actions become candidate events, how the canonical server validates and records those events, and how observers reconstruct and reconcile to shared event-driven truth.


---
