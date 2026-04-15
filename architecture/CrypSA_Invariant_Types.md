# CrypSA — Invariant Types

This document defines the categories of **invariants** in CrypSA.

It clarifies:

* what invariants are  
* how they are used  
* how different types of invariants relate to each other  
* where invariants apply within CrypSA

---

## 📜 Authority Level

This document is part of `/architecture`.

It defines the **structure and categorization** of invariants.

👉 It does not define specific validation rules.

For authoritative runtime behavior, see:

* `/spec`

---

## Purpose

This document exists to:

* prevent ambiguity around the term “invariant”  
* distinguish different types of invariants  
* clarify validator responsibility  
* support consistent system design  

---

## What Is an Invariant

An invariant is a rule that must hold for an event to become canonical.

In CrypSA:

👉 invariants define what is **allowed to become truth**

They are enforced at the **invariant boundary** during validation.

---

## Core Principle

> Invariants do not describe the system — they constrain what can become canonical.

Invariants operate exclusively at the invariant boundary.

---

## Invariant Categories

CrypSA defines two primary categories of invariants:

1. Architectural Invariants  
2. System Invariants  

These invariants are enforced through validation rules.

---

## 1. Architectural Invariants

Architectural invariants are required for CrypSA to function.

They define the fundamental structure of the system.

---

### Examples

* canonical event history is append-only  
* the validator defines what becomes canonical  
* state is derived from canonical event history  
* replay must produce consistent results  

---

### Properties

* required across all CrypSA systems  
* non-negotiable  
* define the architecture itself  

---

### Role

Architectural invariants ensure:

* consistency of the model  
* correctness of truth definition  
* integrity of replay and validation  

---

## 2. System Invariants

System invariants define rules specific to a particular system or product.

They describe what is valid within that system.

---

### Examples

* a player cannot move through walls  
* inventory cannot exceed capacity  
* an entity must exist before it can be modified  

---

### Properties

* defined by the system designer  
* vary between implementations  
* enforced during validation  

---

### Role

System invariants ensure:

* correctness of system behavior  
* consistency of domain rules  
* validity of state transitions  

---

## 3. Validation Rules (Enforcement Layer)

Validation rules are the concrete checks applied to candidate events.

They are the operational enforcement of invariants.

---

### Examples

* type validation  
* range checks  
* existence checks  
* rule enforcement based on system invariants  

---

### Properties

* executable  
* applied during validation  
* derived from architectural and system invariants  

---

### Role

Validation rules:

* determine whether a candidate event is accepted or rejected  
* enforce invariants at runtime  

---

## Relationship Between Categories

The invariant system forms a layered structure:

```text
Architectural Invariants
        ↓
System Invariants
        ↓
Validation Rules (Enforcement)
````

---

### Explanation

* Architectural invariants define the structure of the system
* System invariants define the rules of a specific system
* Validation rules enforce those rules in practice

---

## The Invariant Boundary

All invariants are enforced at:

👉 the **invariant boundary**

This is where:

* candidate events are evaluated
* validation rules are applied
* events are accepted or rejected

---

### Important

> Only events that satisfy all applicable invariants may become canonical.

---

## Validator Responsibility

The validator is responsible for:

* enforcing validation rules
* ensuring invariants are upheld
* determining whether events become canonical

The validator does not:

* define architectural invariants
* define system invariants

👉 It **enforces**, it does not **design**

---

## What Invariants Do NOT Do

Invariants do not:

* define how systems are implemented
* define how state is stored
* define networking behavior
* define user experience

👉 They constrain truth, not implementation

---

## Common Misinterpretations

---

### ❌ “Everything is an invariant”

Incorrect.

Not all rules belong at the invariant boundary.

Only rules that affect whether an event can become canonical are invariants.

---

### ❌ “Invariants define system behavior”

Incorrect.

Invariants constrain valid events.

They do not define how systems behave outside validation.

---

### ❌ “Validation rules are the same as invariants”

Incorrect.

Validation rules are:

👉 the enforcement of invariants

---

## Summary

CrypSA defines invariants as constraints on canonical truth:

* architectural invariants define the system structure
* system invariants define domain rules
* validation rules enforce those constraints

Together, they ensure that:

* only valid events become canonical
* canonical event history remains consistent
* systems maintain correctness through validation

And critically:

> Invariants do not define the system — they define what the system will accept as truth.
