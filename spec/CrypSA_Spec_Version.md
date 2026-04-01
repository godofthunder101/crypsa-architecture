# CrypSA Specification Versioning (v0.x Policy)

This document defines how CrypSA specifications are versioned.

---

## Current Version

CrypSA Specification Set:

> v0.1

All documents in the `spec/` folder are part of this version unless explicitly stated otherwise.

---

## Version Meaning

### v0.x — Experimental

* concepts are stabilizing
* breaking changes are expected
* specifications may evolve rapidly
* not production-ready

Behavior defined in v0.x:

* is authoritative within the version
* is not guaranteed to remain compatible across minor revisions

---

### v1.0 — Stable Runtime

* core runtime model finalized
* backward compatibility becomes a requirement
* suitable for production use
* changes must preserve existing behavior

---

## Version Scope

Versioning applies to the entire specification set, including:

* runtime behavior
* event structure
* validation rules
* consistency guarantees
* identity model
* replay and snapshot behavior
* transport expectations

> A version represents a **coherent system definition**, not independent documents.

---

## Version Authority

The specification version defines the expected system behavior.

Implementations must:

* align with the spec version they target
* clearly declare the version they implement
* not mix behaviors from different spec versions

If a mismatch exists:

> the declared spec version is the source of truth

---

## Document Versioning

Individual documents inherit the version of the specification set.

They should:

* include the version in the title (e.g. `Spec v0.1`)
* remain consistent with the rest of the spec set

If a document diverges:

* it must explicitly declare a different version
* or be updated to match the current version

---

## Change Policy (v0.x)

During v0.x:

* breaking changes are allowed
* specifications may evolve rapidly
* documents must remain internally consistent
* cross-spec alignment must be maintained

When changes occur:

* all affected documents must be updated
* inconsistencies must not be introduced

---

## Implementation Alignment

Implementations should:

* track the spec version they implement
* update alongside spec changes
* validate behavior against the spec

Implementations must not:

* partially implement multiple versions
* assume compatibility across spec revisions

---

## Version Progression

Specifications are expected to evolve as follows:

```text id="version-flow"
v0.x → v1.0 → v1.x
```

---

### v0.x → v1.0

* core runtime behavior is finalized
* breaking changes are minimized or removed
* system is validated through implementation

---

### v1.x (Post-Stable)

* backward compatibility is maintained
* changes are additive or non-breaking
* versioning becomes stricter

---

## Future Direction

Future versions are expected to include:

* formal compatibility guarantees
* migration paths between versions
* protocol-level version negotiation
* version-aware replay and validation

---

## Design Principle

Versioning in CrypSA is:

> system-level, not document-level

A version defines:

* a complete, consistent runtime model
* a shared understanding between implementations

---

## One Sentence Summary

CrypSA v0.1 is an experimental, system-level specification defining the initial runtime model, with breaking changes expected before a stable and backward-compatible v1.0.
