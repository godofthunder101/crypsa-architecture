# CrypSA Worked Example

This document walks through a complete end-to-end example of how CrypSA operates at runtime.

It demonstrates how:

- a local action becomes a candidate event  
- the server validates that event  
- canonical history is updated  
- observers reconcile their local state  

This example is intentionally simple and focuses on clarity over complexity.

---

## Scenario: Placing a Structure

A player places a mining station on an empty tile.

---

## Initial State

Canonical world state (derived):

- tile_42 → empty  
- player_A → owns 100 resources  

Observers have reconstructed this state locally.

---

## Step 1 — Local Action (Observer)

The player performs an action:

> “Place mining station on tile_42”

The observer:

- updates local predicted state  
- shows the structure immediately (optimistic simulation)  

---

## Step 2 — Candidate Event Creation

The observer creates a candidate event:

event_type = place_structure
actor_id = player_A
target_ids = [tile_42]

payload = {
structure_type: mining_station,
cost: 50
}

precondition_refs = {
tile_42_empty: true,
player_resources >= 50
}

branch_id = main

This event represents an **intent**, not a confirmed state change.

---

## Step 3 — Event Sent to Server

The observer sends the candidate event to the canonical server.

At this point:

- the local client assumes success  
- the server has not yet accepted the event  

---

## Step 4 — Server Validation

The server processes the event through the validation pipeline.

### 4.1 Schema Validation

- fields exist  
- payload is valid  

✅ passes

---

### 4.2 Identity Validation

- player_A exists  
- tile_42 exists  

✅ passes

---

### 4.3 Precondition Validation

- tile_42 is still empty  
- player_A still has ≥ 50 resources  

✅ passes

---

### 4.4 Invariant Validation

- placing a structure does not violate spatial rules  
- no duplicate or conflicting structure  

✅ passes

---

### 4.5 Rule Validation

- mining_station is valid for this tile  
- resource cost is correct  

✅ passes

---

## Step 5 — Event Accepted

The server accepts the event.

It assigns canonical metadata:

canonical_event_id = 9001
server_sequence = 1203
accepted_at = timestamp

The event is appended to the canonical event log.

---

## Step 6 — Canonical State Update

Derived state updates:

- tile_42 → now contains mining_station  
- player_A resources → reduced to 50  

---

## Step 7 — Broadcast to Observers

The server broadcasts the accepted canonical event to all observers.

---

## Step 8 — Observer Reconciliation

Each observer compares:

- local predicted state  
vs  
- canonical update  

### Case A — Prediction Matches

If the local observer predicted correctly:

- no visible change  
- pending marker cleared  

---

### Case B — Prediction Differs

If something changed (e.g. conflict or rejection):

- local state is corrected  
- incorrect objects are removed  
- canonical state is applied  

---

## Alternative Scenario — Conflict

Two players attempt to build on tile_42 at the same time.

### What Happens:

- both send candidate events  
- server validates both  
- first valid event is accepted  
- second fails precondition (tile no longer empty)  

### Result:

Second player receives:

rejection_code = precondition_failed

Their observer:

- removes predicted structure  
- updates to canonical state  

---

## What This Example Shows

This flow demonstrates:

- actions do not directly change canonical truth  
- events are proposals, not guarantees  
- the server validates instead of simulating everything  
- canonical history is the source of truth  
- observers reconstruct and reconcile  

---

## Why This Matters

Traditional systems:

> server simulates → clients receive state  

CrypSA:

> clients simulate → server validates → history defines truth  

---

## One Sentence Summary

A player action becomes a candidate event, the server validates it, accepted events enter canonical history, and all observers reconcile their local simulation to that shared truth.
