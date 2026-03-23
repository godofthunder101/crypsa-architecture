# CrypSA Conflict Resolution

This diagram shows how CrypSA resolves conflicting candidate events that target the same canonical conflict scope.

Examples of conflict scope include:

- the same tile
- the same object
- the same inventory slot
- the same ownership target

In CrypSA v0.1:

> the first valid accepted event wins within the conflict scope

---

```mermaid
flowchart TD

A[Observer A submits candidate event] --> C[Server identifies conflict scope]
B[Observer B submits candidate event] --> C

C --> D[Lock or atomically evaluate conflict scope]

D --> E[Validate Event A]
D --> F[Validate Event B]

E -->|Passes first| G[Accept Event A]
E -->|Fails| R1[Reject Event A]

F -->|Scope already changed| R2[Reject Event B: conflict_lost or precondition_failed]
F -->|Passes first| H[Accept Event B]
F -->|Fails| R3[Reject Event B]

G --> I[Append canonical event]
H --> I

I --> J[Update derived state]
J --> K[Broadcast canonical update]

R1 --> L[Return rejection result]
R2 --> L
R3 --> L

K --> M[Observers reconcile]
L --> M

````

---

## How to Read This

### 1. Two Conflicting Actions Arrive

Two observers submit actions that affect the same conflict scope.

Examples:

* both place on the same tile
* both claim the same object
* both consume the same unique resource

---

### 2. The Server Evaluates the Scope Atomically

The server must ensure that:

* conflicting events are not accepted simultaneously
* validation happens against a consistent canonical view

This may be implemented with:

* locking
* atomic transactions
* scope-based serialization

---

### 3. One Event Wins

In v0.1:

* the first valid accepted event wins
* later conflicting events are rejected

---

### 4. Rejection Happens for a Reason

The losing event may be rejected because:

* the conflict was already resolved
* its preconditions are no longer true
* the canonical state changed before it could be accepted

Typical rejection results:

* `conflict_lost`
* `precondition_failed`

---

### 5. Observers Reconcile

Once the accepted canonical event is broadcast:

* the winning observer confirms its prediction
* the losing observer removes or corrects its local prediction

---

## Key Insight

> Conflict resolution is not decided by local simulation.
> It is decided by atomic validation against canonical truth.

---

## Relationship to Specs

This diagram maps directly to:

* `spec/CrypSA_Runtime_Spec_v0.1.md`
* `spec/CrypSA_Validation_Model.md`
* `spec/CrypSA_Consistency_Model.md`

---

## One Sentence Summary

When multiple observers submit conflicting actions, the server resolves them atomically within the conflict scope, accepts one valid event, rejects the others, and all observers reconcile to the resulting canonical truth.
Say “next” and I’ll do the **Snapshot + Replay** diagram.
```
