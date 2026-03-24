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

---

## Version Authority

The specification version defines the expected system behavior.

Implementations must:

* align with the spec version they target
* clearly declare if they deviate

---

## Change Policy (v0.x)

During v0.x:

* breaking changes are allowed
* specifications may evolve rapidly
* documents must remain internally consistent
* cross-spec alignment must be maintained

---

## Implementation Alignment

Implementations should:

* track the spec version they implement
* update alongside spec changes
* avoid mixing behaviors from different spec versions

If a mismatch exists:

> the spec version must be treated as the source of truth

---

## Future Direction

Future versions are expected to include:

* formal compatibility guarantees
* migration paths between versions
* protocol-level version negotiation
* version-aware replay and validation

---

## One Sentence Summary

CrypSA v0.1 is an experimental specification set that defines the initial runtime model, with breaking changes expected before a stable v1.0.
