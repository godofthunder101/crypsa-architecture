# CrypSA Event Model Spec v0.1

This document defines the structure, behavior, and lifecycle of events in CrypSA.

Events are the foundation of the system.

> Canonical events define shared reality.  
> State is derived by replaying those events.

---

## Core Principle

CrypSA is event-driven.

- The world is not the source of truth  
- The **event history is the source of truth**  
- World state is a projection of that history  

---

## Event Types

CrypSA distinguishes between two primary event types:

### 1. Candidate Events

- Created by observers (clients)
- Represent proposed actions
- Not yet part of shared reality
- Subject to validation

---

### 2. Canonical Events

- Accepted by the server
- Immutable
- Part of canonical history
- Used for replay and reconstruction

---

## Event Lifecycle

Every event follows this lifecycle:

1. **Creation**
   - Observer creates a candidate event

2. **Submission**
   - Event is sent to the server

3. **Validation**
   - Server evaluates the event

4. **Decision**
   - Accepted → becomes canonical  
   - Rejected → discarded  

5. **Canonicalization**
   - Event is assigned canonical metadata
   - Added to canonical history

6. **Propagation**
   - Observers receive the canonical event

7. **Replay**
   - Observers update state via replay

---

## Event Structure

A CrypSA event contains the following fields:

### Required Fields

#### `event_id`
- Unique identifier
- Must be globally unique (e.g., UUID)

---

#### `event_type`
- Defines the action type
- Examples:
  - `place_object`
  - `destroy_object`
  - `transfer_item`

---

#### `issuer_id`
- The observer or system that created the event

---

#### `target_ids`
- Objects affected by the event
- May be empty or multiple

---

#### `payload`
- Event-specific data
- Example:
  ```json
  {
    "position": [10, 5],
    "object_kind": "house"
  }
