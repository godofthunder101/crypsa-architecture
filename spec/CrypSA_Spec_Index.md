# CrypSA Specification

This folder contains the implementation-facing specifications for CrypSA.

These documents define how the system is expected to behave at runtime.

If the `architecture/` folder explains:

> what CrypSA is and why it exists

the `spec/` folder explains:

> how CrypSA is expected to function as a real system

---

## Purpose of This Folder

The documents in this folder define the core runtime behavior of CrypSA, including:

- how events are structured
- how validation works
- how consistency is maintained
- how replay reconstructs state
- how snapshots improve performance
- how identities remain stable over time
- how transport moves events between observers and the server

These are not full production guarantees.

They are the minimum system definitions needed to make CrypSA technically reviewable and implementable.

---

## Recommended Reading Order

If you are reading the specs for the first time, use this order:

1. `CrypSA_Runtime_Spec_v0.1.md`  
   The top-level runtime contract.  
   Defines the overall flow from local action to canonical truth.

2. `CrypSA_Event_Model_Spec.md`  
   Defines what events are, how they are structured, and how they move through the system.

3. `CrypSA_Validation_Model.md`  
   Defines how candidate events are checked before becoming canonical.

4. `CrypSA_Consistency_Model.md`  
   Defines how observers and the server converge on shared reality.

5. `CrypSA_Replay_Model.md`  
   Defines how world state is reconstructed from canonical history.

6. `CrypSA_Snapshot_Model.md`  
   Defines how snapshots support replay, loading, and recovery.

7. `CrypSA_Identity_Model.md`  
   Defines how objects are identified, created, and versioned over time.

8. `CrypSA_Transport_Model.md`  
   Defines how candidate events and canonical updates move between observers and the server.

---

## How to Read These Specs

The specs are meant to be read as a connected system.

A useful mental model is:

- **Runtime Spec** = overall loop  
- **Event + Validation** = what enters canonical history  
- **Consistency + Replay** = how shared reality stays coherent  
- **Snapshot + Identity + Transport** = how the runtime remains practical and stable  

---

## Scope of the Current Specs

The current spec set is focused on CrypSA v0.1.

It is intended to define:

- a minimal canonical event-driven runtime
- observer/server interaction
- deterministic reconstruction
- practical implementation direction

It does **not yet fully define**:

- combat adjudication
- advanced anti-cheat
- shard federation
- offline branch merging
- full production networking guarantees
- cryptographic trust systems

These belong to later iterations.

---

## Relationship to the Rest of the Repo

Suggested reading flow:

### New to CrypSA
- `../CrypSA_In_5_Minutes.md`
- `../CrypSA_Terminology_Primer.md`
- `../FAQ.md`

### Want the conceptual model
- `../exploratory/foundation/`
- `../exploratory/core_concepts/`
- `../architecture/`

### Want the formal system definition
- start here in `spec/`

### Want implementation direction
- `../implementation/CrypSA_Minimal_Server_v0.1.md`

---

## Current Status

These specs define the architecture at a system level.

They are intended to guide:

- prototype implementation
- technical review
- future runtime experiments

They should be treated as evolving documents rather than final standards.

---

## One Sentence Summary

The `spec/` folder defines the implementation-facing behavior of CrypSA: how events, validation, consistency, replay, identity, snapshots, and transport work together to produce shared canonical reality.
