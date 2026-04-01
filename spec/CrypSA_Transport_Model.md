# CrypSA Transport Model Spec v0.1

This document defines how events and canonical updates are transmitted between observers and the validator.

It specifies:

* how candidate events are submitted
* how canonical updates are delivered
* delivery guarantees
* ordering expectations
* retry and idempotency behavior

This is a minimal transport model for CrypSA v0.1.

---

## Core Principle

CrypSA transport is designed around:

> reliable agreement on canonical events, not perfect real-time synchronization

The system prioritizes:

* correctness
* eventual consistency
* idempotent communication

over strict real-time guarantees.

---

## Transport Roles

### Observer → Validator

* submits candidate events
* may retry submissions
* does not control ordering

---

### Validator → Observer

* delivers canonical events
* delivers validation outcomes
* informs observers of accepted/rejected proposals

---

## Communication Model

CrypSA v0.1 assumes:

* asynchronous communication
* unreliable networks
* variable latency
* possible message duplication
* possible message reordering

The system must remain correct under these conditions.

---

## Candidate Event Submission

Observers submit candidate events to the validator.

---

### Requirements

* each event must include a unique `event_id`
* submissions must be retry-safe
* duplicate submissions must not create duplicate canonical events

---

### Idempotency

The validator must treat `event_id` as idempotent.

If the same event is submitted multiple times:

* it must be processed once
* duplicates must be ignored or mapped to the same result

---

### Submission Outcomes

Each submission results in:

* **accepted** → becomes part of canonical event history
* **rejected** → no canonical change

The observer must be informed of the outcome.

---

## Acknowledgment Model

The validator should provide:

* acknowledgment of receipt (optional in v0.1)
* final validation outcome (required)

Observers must track:

* pending submissions
* accepted events
* rejected events

---

## Canonical Event Distribution

The validator distributes accepted canonical events to observers.

---

### Delivery Model

Canonical events must be:

* eventually delivered to all relevant observers
* complete and consistent with canonical event history ordering (`server_sequence`)

---

### Ordering Guarantee

Transport does **not** guarantee ordering.

Canonical ordering is defined by:

* `server_sequence` assigned by the validator

Observers must:

* reorder events as needed
* apply events strictly in `server_sequence` order

---

## Event Stream Model

Observers receive a stream of canonical events.

This stream may:

* arrive delayed
* arrive out of order
* contain duplicates

Observers must:

* reorder events using `server_sequence`
* discard duplicates
* apply events deterministically

---

## Replay Alignment

Observers must align received events with their local replay state.

If gaps are detected:

* request missing events
* ensure replay does not proceed with incomplete canonical event history

---

## Retry Behavior

Observers may retry event submission when:

* no response received
* timeout occurs
* connection interrupted

---

### Requirements

* retries must reuse the same `event_id`
* the validator must handle duplicates safely

---

## Disconnection Handling

When an observer disconnects:

* local simulation may continue
* no canonical updates are received

Upon reconnection:

* observer must fetch canonical updates
* reconcile local state with canonical event history

---

## Resynchronization

Observers must support resynchronization.

---

### Minimum Mechanism

* request canonical events since last known `server_sequence`
* optionally load snapshot
* replay event tail

---

## Snapshot Integration

Transport may provide:

* snapshot delivery
* event tail delivery

Reconstruction:

> Snapshot + Event Stream → Current Derived Canonical State

---

## Flow Control (v0.1 Simplified)

CrypSA v0.1 does not define:

* backpressure mechanisms
* rate limiting
* prioritization strategies

These are implementation-defined.

---

## Failure Modes

Transport must tolerate:

* packet loss
* duplicated messages
* delayed delivery
* out-of-order delivery
* temporary disconnections

---

## Security Considerations

Transport layer must ensure:

* events cannot be spoofed or altered in transit
* observer identity is authenticated
* validator authority is trusted

v0.1 does not mandate specific cryptographic protocols.

---

## Performance Considerations

Transport performance depends on:

* event frequency
* payload size
* snapshot size
* network conditions

---

### Optimization Strategies

* batching events
* compressing payloads
* prioritizing critical updates

---

## Tradeoffs

### Advantages

* resilient to unreliable networks
* simple retry model
* supports eventual consistency
* decouples simulation from transport

---

### Costs

* increased reconciliation complexity
* delayed consistency under latency
* need for idempotent handling
* possible temporary divergence

---

## Relationship to Runtime

Transport is responsible for:

* moving candidate events to validation
* delivering canonical events to observers

It does not:

* validate events
* define canonical event history
* simulate world state

---

## Summary

CrypSA transport is:

* asynchronous
* idempotent
* eventually consistent
* resilient to network imperfections

It ensures:

> candidate events reach the validator,
> canonical events reach observers,
> and all participants converge on shared history

---

## One Sentence Summary

CrypSA Transport defines how candidate events and canonical updates move between observers and the validator using an asynchronous, idempotent, and eventually consistent communication model.
