# CrypSA Identity Model Spec v0.1

This document defines how objects are identified, created, and evolve within a CrypSA system.

The identity model ensures that:

* objects can be referenced consistently over time
* events can safely modify objects
* replay produces stable and correct results
* object definitions remain compatible with history

---

## Core Principle

In CrypSA:

> Identity is permanent.
> Definition may evolve.
> History must remain valid.

---

## Identity vs Definition

CrypSA separates:

* **Identity** → "what this object is"
* **Definition (Genome)** → "how this object behaves"

---

### Identity

* unique and persistent
* referenced in all events
* immutable
* does not change over time

---

### Definition (Genome)

* describes structure and rules
* may evolve over time
* must be version-aware

---

## Minted Identities

Objects are created through **mint events**.

---

### Mint Event

A mint event creates:

* a new unique identity (`object_id`)
* an initial genome reference (`genome_id`)
* initial state

---

### Example

```text
event_type = mint_object
payload = {
  object_id: obj_123,
  genome_id: mining_station_v1,
  initial_state: { ... }
}
```

---

### Requirements

* `object_id` must be globally unique within the canonical domain
* mint events must be accepted as canonical before the object exists
* no object exists without a canonical mint event

---

## Object Lifecycle

Objects follow this lifecycle:

```text
non-existent
→ minted
→ active
→ modified (via events)
→ possibly destroyed or archived
```

---

### Destruction

Destruction is represented by a canonical event.

* identity remains valid for historical reference
* destroyed objects cannot be modified

---

## Identity Stability

Once created:

* `object_id` never changes
* events always refer to the same identity
* identity remains valid even if the object is destroyed

---

## Genome (Definition Model)

Each object references a **genome**.

---

### Genome Purpose

Defines:

* structure
* allowed state transitions
* validation rules
* event compatibility

---

### Genome Versioning

Genomes must be versioned.

Example:

```text
mining_station_v1
mining_station_v2
```

---

### Historical Consistency

Replay must remain deterministic.

Objects must remain compatible with their genome definition.

---

### Strategy 1: Version Freeze (Required for v0.1)

* object remains tied to original genome version
* ensures deterministic replay
* avoids migration complexity

---

### Strategy 2: Explicit Migration (Future)

* new event updates object to a new genome version
* migration must be deterministic
* migration must be replay-safe

---

## Identity Referencing in Events

All canonical events must reference identities explicitly.

---

### Requirements

* all target objects must exist
* identity must be valid at event time
* destroyed objects cannot be modified

---

## Identity Registry

The system maintains an identity registry as part of derived state.

This registry contains:

* object_id
* genome reference
* lifecycle status
* derived state (materialized from canonical event history)

This registry is:

> a computed view, not the source of truth

---

## Identity and Replay

Replay relies on identity stability.

---

### Requirements

* identity must resolve consistently across replay
* genome references must be resolvable
* state transitions must be deterministic

---

## Identity Scope

Identity must be unique within the canonical system.

---

### v0.1 Assumption

* global uniqueness within a single canonical domain

---

### Future Extensions

* partitioned identity spaces
* shard-aware identity prefixes
* globally coordinated identity generation

---

## Identity Generation

In v0.1:

* clients may propose `object_id`
* server must validate uniqueness

---

### Requirements

* collision detection is required
* duplicate mint attempts must be rejected

---

### Alternative (Future)

* server-assigned identities
* deterministic ID generation
* namespace-based IDs

---

## Failure Modes

Identity systems must handle:

* duplicate object IDs
* missing identity references
* invalid genome references
* attempts to modify destroyed objects

---

## Security Considerations

Identity validation must ensure:

* no spoofed object IDs
* no unauthorized modification
* no duplication of unique objects

---

## Tradeoffs

### Advantages

* stable referencing
* replay safety
* clear object lifecycle
* flexible definition evolution

---

### Costs

* need for version management
* migration complexity
* identity registry overhead

---

## Summary

CrypSA identity model ensures:

* objects have permanent identities
* definitions are versioned and controlled
* events safely reference objects
* replay remains deterministic

---

## One Sentence Summary

CrypSA identity separates permanent object identity from evolving definitions, ensuring stable references, deterministic replay, and safe object lifecycle management.
