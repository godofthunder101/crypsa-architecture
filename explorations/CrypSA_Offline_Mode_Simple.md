# CrypSA Offline Mode — Simple

## Purpose

This document describes a simple offline mode model for CrypSA systems.

It explores how clients can simulate the universe locally while disconnected from the canonical server.

This is an **exploratory design**, not a required architectural component.

---

## Core Principle

CrypSA separates:

* local simulation
* canonical truth

Clients may simulate freely while offline, but:

> canonical truth exists only on the server

---

## Offline Model Overview

In the simple offline model:

* offline activity occurs in a **local branch**
* the branch exists only on the client
* it is not merged into canonical history

When reconnecting:

* the client discards or archives the branch
* canonical history is reloaded
* simulation resumes from canonical truth

---

## Local Simulation While Offline

When disconnected, the client may simulate:

* movement
* building
* crafting
* upgrades
* environment interaction

These actions:

* exist only in local simulation
* do not affect canonical truth

---

## Local Branch Concept

Offline play creates a **local branch of the universe**.

This branch:

* is derived from canonical state
* maintains its own local event history
* is not shared with other observers

It behaves like a temporary single-player universe.

---

## Reconstruction on Reconnect

When reconnecting:

1. the client requests canonical updates
2. canonical history is received
3. the client reconstructs canonical state
4. the local branch is discarded or archived

The observer resumes from canonical truth.

---

## Invariant Boundary

The invariant boundary still applies.

When connected:

* actions that affect canonical truth must be validated

When offline:

* no actions cross the invariant boundary
* all activity remains local

---

## Why Offline Branches Are Not Merged

Merging offline branches into canonical history introduces complexity:

* conflicting state changes
* ownership conflicts
* resource duplication
* invariant violations

The simple model avoids these issues by:

> not merging offline branches at all

---

## Optional Implementation Pattern: Mint Mirror

Some implementations may include a **local mint mirror**.

This allows the client to:

* understand object structure
* simulate object creation
* reconstruct canonical data

This is a practical approach, not a required architectural component.

---

## Optional Features

Offline branches may support:

* experimentation
* strategy testing
* sandbox play
* personal progression

These remain separate from canonical truth.

---

## Alternative Offline Models

CrypSA does not require a single offline strategy.

Other approaches may include:

### Mergeable Offline Branches

Offline changes may later merge into canonical history.

This requires:

* conflict resolution
* invariant conflict handling
* duplication prevention

---

### Separate Local Worlds

Offline play occurs in independent worlds:

* sandbox environments
* creative modes
* private instances

---

### Event Buffering

Clients store events while offline and submit them later.

The server:

* validates events
* accepts or rejects them

---

## Key Insight

> Offline simulation is allowed because canonical truth is protected by validation.

---

## Summary

In the simple offline model:

* clients simulate locally while disconnected
* offline activity exists in a local branch
* canonical truth remains server-controlled
* no merging occurs

This keeps the system simple while preserving CrypSA’s core guarantees.

---

## One Sentence Summary

CrypSA Simple Offline Mode allows local simulation in a temporary client-only branch while canonical truth remains exclusively controlled by the server and offline activity is never merged into shared history.
