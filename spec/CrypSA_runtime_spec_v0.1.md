# CrypSA Runtime Spec v0.1

## Purpose

This document defines the minimal runtime behavior of a CrypSA system.

It specifies how:

- local observer actions become candidate events  
- candidate events are validated  
- canonical truth is updated  
- observers reconcile to canonical state  

This is the minimum runtime contract required for CrypSA to be:

> technically reviewable and implementable

This is not a full production protocol.

---

## 1. Scope

This v0.1 runtime spec covers:

- observer action proposal  
- candidate event structure  
- server-side validation  
- event acceptance and rejection  
- canonical event recording  
- canonical update distribution  
- observer reconciliation  
- per-object ordering  
- snapshot-assisted reconstruction  

This v0.1 spec does **not fully define**:

- combat adjudication  
- advanced anti-cheat systems  
- distributed shard coordination  
- mergeable offline branches  
- advanced partitioning strategies  
- cryptographic trust proofs  

---

## 2. Runtime Roles

### 2.1 Observer

A process that:

- reconstructs canonical objects locally  
- simulates local experience  
- proposes candidate events  
- reconciles local state with canonical truth  

In most games, this is the client.

---

### 2.2 Canonical Server

A process that:

- receives candidate events  
- validates them  
- enforces invariants  
- records accepted canonical events  
- distributes canonical updates  

---

### 2.3 Canonical Truth Store

The persistent runtime store containing:

- canonical event log  
- object identity registry  
- genome references  
- derived canonical state  
- snapshots  

---

## 3. Core Runtime Principle

A player action does **not directly modify canonical truth**.

Instead:
