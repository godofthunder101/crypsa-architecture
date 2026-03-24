# CrypSA Control Flow Diagram

## Purpose

This diagram shows how runtime decisions are made in a CrypSA system.

The system continuously decides:

* does this remain local?
* does this affect canonical event history?
* should the server validate it?
* should observers reconstruct?

---

## High-Level Control Flow

```text
Reconstruct
   ↓
Translate (Adapters)
   ↓
Interpret (Lenses)
   ↓
Simulate
   ↓
Invariant Boundary Check
   ├── No → Remain Local
   └── Yes → Submit Candidate Event
                  ↓
              Validate
                  ↓
           Accepted?
            ├── No → Reject / Correct
            └── Yes → Assign server_sequence
                          ↓
                   Append to Canonical Event History
                          ↓
                   Observers Reconstruct
````

---

## Full Control Flow Diagram

```text
1. OBSERVER RECONSTRUCTS WORLD
   - from canonical event history
   - identity + genome + invariant state

        ↓

2. TRANSLATION (ADAPTERS)
   - shape canonical + observer data
   - prepare structured inputs

        ↓

3. INTERPRETATION (LENSES)
   - determine meaning, visibility, interaction

        ↓

4. LOCAL SIMULATION
   - movement, physics, prediction, effects

        ↓

5. ACTION PRODUCES RESULT

        ↓

6. INVARIANT BOUNDARY CHECK
   Does this affect canonical event history?

        ├── NO → REMAIN LOCAL
        │       - UI updates
        │       - prediction
        │       - temporary effects
        │
        └── YES → GENERATE CANDIDATE EVENT
                        ↓
                7. SUBMIT TO SERVER
                        ↓
                8. VALIDATION
                        ↓
                ACCEPTED?
                  ├── NO → REJECT / CORRECT
                  └── YES → ASSIGN server_sequence
                                      ↓
                          9. APPEND TO CANONICAL EVENT HISTORY
                                      ↓
                          10. OBSERVERS RECONSTRUCT
```

---

## How to Read This

### Reconstruction

Observers rebuild the world from canonical event history.

---

### Translation

Adapters prepare data for interpretation.

---

### Interpretation

Lenses assign meaning to the world.

---

### Simulation

Local systems produce immediate results.

---

### Invariant Boundary

The key decision:

> Does this affect canonical event history?

---

### Validation

If yes:

* a candidate event is submitted
* the server validates it
* it is accepted or rejected

---

### Canonical Update

Accepted events:

* are appended to canonical event history
* define new shared state

---

### Reconciliation

Observers:

* receive updates
* rebuild affected state
* converge to canonical event history

---

## Key Insight

> The invariant boundary determines whether an action remains local or becomes part of canonical event history.

---

## Comparison to Traditional Multiplayer

Traditional:

```text
Player → Server Simulation → Client Update
```

CrypSA:

```text
Observer → Invariant Boundary → Validation → Canonical Event History → Reconstruction
```

---

## Summary

CrypSA runtime flow:

* reconstruct
* translate
* interpret
* simulate
* check invariant boundary
* validate if needed
* update canonical event history
* reconstruct again

---

## One Sentence Summary

CrypSA control flow is driven by the invariant boundary, which determines whether actions remain local or become validated canonical events that update canonical event history and trigger observer reconstruction.
