# CrypSA Offline Mode — Simple

## Purpose

This document describes a simple offline mode model for CrypSA systems.

It explores how observers can simulate the universe locally while disconnected from the validator.

This is an **exploratory design**, not a required architectural component.

---

## Core Principle

CrypSA separates:

* local simulation
* canonical event history

Observers may simulate freely while offline, but:

> canonical event history exists only through the validator

---

## Offline Model Overview

In the simple offline model:

* offline activity occurs in **observer-local simulation state**
* this state exists only on the observer
* it is not merged into canonical event history

When reconnecting:

* the observer discards or archives its local state
* canonical event history is reloaded
* simulation resumes from canonical state

---

## Local Simulation While Offline

When disconnected, the observer may simulate:

* movement
* building
* crafting
* upgrades
* environment interaction

These actions:

* exist only in local simulation
* do not affect canonical event history

---

## Observer-Local Event History

Offline play may maintain an **observer-local event history**.

This history:

* is derived from canonical state at the time of disconnection
* records locally simulated actions
* is not shared with other observers
* does not become canonical

It behaves like a temporary single-observer simulation timeline.

---

## Reconstruction on Reconnect

When reconnecting:

1. the observer requests canonical updates
2. canonical event history is received
3. the observer reconstructs derived canonical state via replay
4. local simulation state is discarded or archived

The observer resumes from canonical event history.

---

## Invariant Boundary

The invariant boundary still applies.

When connected:

* actions that affect canonical event history must be validated

When offline:

* no actions cross the invariant boundary
* all activity remains local

---

## Why Offline State Is Not Merged

Merging offline activity into canonical event history introduces complexity:

* conflicting state changes
* ownership conflicts
* resource duplication
* invariant violations

The simple model avoids these issues by:

> not merging offline activity into canonical event history

---

## Optional Implementation Pattern: Mint Mirror

Some implementations may include a **local Mint mirror**.

This allows the observer to:

* understand object structure
* simulate object creation
* reconstruct canonical data

This is a practical approach, not a required architectural component.

---

## Optional Features

Offline simulation may support:

* experimentation
* strategy testing
* sandbox play
* personal progression

These remain separate from canonical event history.

---

## Alternative Offline Models

CrypSA does not require a single offline strategy.

Other approaches may include:

---

### Mergeable Offline State (Advanced)

Offline changes may later be submitted to the validator.

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

Observers store candidate events while offline and submit them later.

The validator:

* validates events
* accepts or rejects them

---

## Key Insight

> Offline simulation is possible because canonical event history is protected by validation.

---

## Summary

In the simple offline model:

* observers simulate locally while disconnected
* offline activity exists only in observer-local simulation
* canonical event history remains validator-controlled
* no merging occurs

This keeps the system simple while preserving CrypSA’s core guarantees.

---

## One Sentence Summary

CrypSA Simple Offline Mode allows observer-local simulation while canonical event history remains exclusively controlled by the validator, and offline activity is never merged into shared history.
