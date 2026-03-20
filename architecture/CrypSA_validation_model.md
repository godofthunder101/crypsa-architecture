# CrypSA Validation Model v0.1

This document defines how CrypSA validates proposed actions before they become part of canonical world history.

Validation is the mechanism that:
- protects shared truth
- enforces rules (invariants)
- determines what becomes canonical

---

## Core Principle

In CrypSA:

> Clients may simulate freely, but only validated events become real.

Validation is applied at the **Invariant Boundary**, where proposed actions transition from local simulation to shared reality.

---

## Validation Flow

The validation pipeline follows this sequence:

1. **Observer Action**
   - A client performs a local action (simulation only)

2. **Candidate Creation**
   - The action is packaged as an event candidate

3. **Submission**
   - The candidate is sent to the server

4. **Validation**
   - The server evaluates the candidate against rules and context

5. **Decision**
   - Accepted → becomes a canonical event  
   - Rejected → discarded (or optionally logged)

6. **Canonical Update**
   - Accepted events are appended to canonical history

7. **Reconciliation**
   - Observers update their local state based on canonical changes

---

## Validation Layers

Validation is not a single check. It is a layered process.

---

### Layer 1 — Structural Validation

Ensures the event is well-formed.

Checks may include:
- valid schema
- required fields present
- valid object references
- valid event type

**Purpose:**
Reject malformed or invalid data early.

---

### Layer 2 — Invariant Validation

Ensures the event does not violate core rules.

Examples:
- object cannot exist in two places at once
- required resources must be available
- placement must be valid
- state transitions must be allowed

**Purpose:**
Protect logical consistency of the world.

---

### Layer 3 — Contextual Validation

Evaluates the event against its surrounding context.

Examples:
- proximity requirements (e.g., must be near a beacon)
- environmental constraints
- relationships between objects
- dependencies on other events

**Purpose:**
Ensure the event makes sense within the world context.

---

### Layer 4 — Simulation Validation (Optional)

Re-simulates or verifies the action outcome.

Examples:
- movement plausibility
- interaction results
- physics constraints (if required)

**Purpose:**
Catch cases where a client submits an outcome without valid cause.

**Note:**
This layer is optional and can be applied selectively.

---

### Layer 5 — Anomaly / Pattern Validation (Optional)

Analyzes patterns over time rather than single events.

Examples:
- impossible frequency of actions
- statistical anomalies
- suspicious behavior patterns

**Purpose:**
Detect cheating or exploitation that is not visible in single events.

---

## Validation Outcomes

Each candidate results in one of the following:

### Accepted
- Event is valid
- Added to canonical history
- Becomes part of shared reality

---

### Rejected
- Event violates rules or constraints
- Does not affect canonical state

Optional:
- rejection reason may be returned
- rejection may be logged for analysis

---

### Flagged (Optional)

- Event is accepted but marked for review
- May trigger monitoring or moderation systems

---

## Invariant Design

Invariants are the foundation of validation.

They define:
- what is allowed
- what must always be true

Strong invariant design is critical for:
- security
- consistency
- correctness

Examples:
- "An object must have exactly one location"
- "An item cannot be duplicated without a defined rule"
- "State transitions must follow defined paths"

---

## Validation Scope

Not all actions require the same level of validation.

CrypSA allows selective validation:

| Action Type            | Validation Level            |
|-----------------------|-----------------------------|
| Local movement        | None (observer-only)        |
| UI interaction        | Minimal                    |
| Object placement      | Invariant + contextual     |
| Item transfer         | Invariant + contextual     |
| Critical interactions | Full validation stack      |

---

## Performance Considerations

CrypSA reduces server load by:

- avoiding full world simulation
- validating only boundary-crossing actions
- applying deeper validation selectively

However:

- validation cost depends on invariant complexity
- contextual checks may require data access
- simulation validation can be expensive

Design should balance:
- correctness
- performance
- risk tolerance

---

## Trust Model

CrypSA does not trust client simulation.

It trusts:

> the validation process that decides what becomes canonical.

Clients may propose any action, but:

- invalid actions are rejected
- only accepted events affect the world

---

## Failure Modes

Validation systems must handle:

- duplicate submissions
- delayed submissions
- conflicting actions
- partial context availability
- inconsistent client state

Handling strategies may include:
- idempotency checks
- ordering rules
- conflict resolution policies

---

## Relationship to Canonical History

Validation determines what enters canonical history.

Once accepted:

- events are immutable
- history becomes the source of truth
- world state is derived through replay

Validation therefore directly defines:
> the integrity of the universe

---

## Summary

CrypSA validation is:

- layered
- rule-driven
- selective
- authoritative at the boundary

It ensures that:

> Clients can act freely,  
> but only valid actions become part of reality.

---
