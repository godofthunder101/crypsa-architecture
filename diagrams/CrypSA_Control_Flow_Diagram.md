# CrypSA Control Flow Diagram

## Purpose

This diagram shows how runtime decisions are made in a CrypSA system.

The system continuously decides:

* does this remain local?
* does this affect canonical event history?
* should the validator evaluate it?
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
              Validator Evaluates
                  ↓
           Accepted?
            ├── No → Reject / Correct
            └── Yes → Assign server_sequence
                          ↓
                   Append to Canonical Event History
                          ↓
                   Observers Reconstruct
```

---

## Full Control Flow Diagram

```text
1. OBSERVER RECONSTRUCTS WORLD
   - from canonical event history
   - identity + genome + invariant-relevant state

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
                7. SUBMIT TO VALIDATOR
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

This reconstruction is based on canonical truth, not local prediction.

---

### Translation

Adapters prepare data for interpretation.

They reshape canonical and observer-side data into usable structures.

---

### Interpretation

Lenses assign meaning to the world.

They determine how the world is understood from a specific observer perspective.

---

### Simulation

Local systems produce immediate results.

This includes prediction, movement, effects, and other responsive observer-side behavior.

---

### Invariant Boundary

The key decision is:

> Does this affect canonical event history?

If not, the result remains local.

If yes, the action must cross the invariant boundary as a candidate event and be evaluated before it can become canonical.

---

### Validation

If the action affects canonical truth:

* a candidate event is submitted
* the validator evaluates it
* it is accepted or rejected

The validator may run locally or remotely, but its role does not change.

Validation determines whether the action becomes part of canonical truth.

---

### Canonical Update

Accepted events:

* are assigned `server_sequence`
* are appended to canonical event history
* extend the shared canonical history of the universe

---

### Reconciliation

Observers:

* receive accepted or rejected outcomes
* rebuild affected derived canonical state
* converge toward canonical truth

---

## Key Insight

> The invariant boundary determines whether an action remains local or becomes part of canonical event history.

And:

> validation determines whether a candidate event is allowed to cross that boundary into canonical truth.

---

## Comparison to Traditional Multiplayer

Traditional:

```text
Player → Server Simulation → Client Update
```

CrypSA:

```text
Observer → Invariant Boundary → Validator → Canonical Event History → Reconstruction
```

---

## Summary

CrypSA runtime flow is:

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

CrypSA control flow is driven by the invariant boundary, which determines whether actions remain local or become candidate events that are evaluated by the validator before updating canonical event history and triggering observer reconstruction.
