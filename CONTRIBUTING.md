# Contributing to CrypSA

Thank you for your interest in contributing to CrypSA.

This repository defines a **software architecture**, not just a codebase.  
Clarity, consistency, and correctness are critical.

Before contributing, please read this document carefully.

---

## 🧭 Core Principle

CrypSA is **architecture-first**.

This means:

* the **spec defines runtime behavior**
* the **architecture defines structure and boundaries**
* implementation follows these definitions

> Contributions must preserve clarity and consistency of the model.

---

## 🔒 Authority Rules (Critical)

The repository is structured by document authority:

| Layer             | Purpose                        | Authority         |
| ----------------- | ------------------------------ | ----------------- |
| `spec/`           | Runtime behavior               | **Highest**       |
| `architecture/`   | Structure and responsibilities | High              |
| `implementation/` | How to build                   | Support           |
| `diagrams/`       | Visualization                  | Non-authoritative |
| `exploratory/`    | Ideas                          | Non-authoritative |

### Rules

* **Do not redefine runtime behavior outside `spec/`**
* **Do not contradict spec from any other document**
* Architecture documents must **explain**, not redefine behavior
* Diagrams must **align with spec and architecture**

If there is any conflict:

> The `spec/` directory is the source of truth.

---

## 🧠 Terminology Rules (Strict)

CrypSA depends on precise language.

All contributors must follow the terminology defined in:

👉 `CrypSA_Terminology_Primer.md`

---

### Key requirements

* Do not redefine existing terms
* Do not introduce synonyms for core concepts
* Use terms exactly as defined

---

### Critical distinctions

#### Validator vs Server

* **Validator** → authority role (used in architecture and spec)
* **Server** → deployment term only

✔ Correct:

``` id="tr8wq5"
validator validates events
````

❌ Incorrect:

```id="83nmq2"
server validates events
```

---

#### Observer vs Client

* **Observer** → correct architectural term
* **Client** → only for networking discussions

---

#### Canonical Terms

Always use:

* canonical event history
* canonical event
* canonical_sequence
* derived canonical state

Avoid vague terms like:

* “state”
* “events”
* “history”

unless clearly scoped

---

### Core Authority Concept

> The validator defines what becomes canonical.

---

## 🔐 Canonical Phrasing Rules

The following phrases are **canonical** and must be used exactly as written.

Do not rephrase, simplify, substitute, or partially restate these phrases.

If a sentence expresses one of these concepts, it must use the canonical phrasing exactly.
Near matches are not acceptable.

---

### Validator Authority

> The validator defines what becomes canonical.

---

### Event Lifecycle

> If accepted, an event becomes canonical and is appended to canonical event history.

---

### Source of Truth

> Canonical event history is the source of truth.

---

### Derived State

> Derived canonical state is a projection of canonical event history. It is not the source of truth.

---

These phrases define the core model.

They must remain identical across all documentation.

---

## 🧱 Architectural Boundaries

CrypSA enforces strict separation:

| Responsibility | Layer                                |
| -------------- | ------------------------------------ |
| Truth          | Validation + canonical event history |
| Translation    | Adapters                             |
| Interpretation | Lenses                               |
| Experience     | UI / simulation                      |

### Rules

* Adapters **change structure, not meaning**
* Lenses **define meaning, not structure**
* UI **does not define truth**
* Observers **never define canonical truth**

Do not blur these boundaries in contributions.

---

## 📝 Writing Guidelines

### General

* Be clear and precise
* Prefer simple, direct language
* Avoid unnecessary abstraction
* Do not add “fluff” explanations

---

### When adding new concepts

1. Add the definition to:
   → `CrypSA_Terminology_Primer.md`

2. Reference it elsewhere:

```id="f6o525"
See: Terminology Primer → [Term]
```

---

### Avoid duplication

* Define concepts once
* Reference instead of repeating
* Do not restate definitions differently in multiple places

---

## 📚 Documentation Structure

When contributing documentation:

### Use the correct location

| Type of content         | Location          |
| ----------------------- | ----------------- |
| Runtime rules           | `spec/`           |
| System structure        | `architecture/`   |
| Implementation guidance | `implementation/` |
| Visual explanation      | `diagrams/`       |
| Experimental ideas      | `exploratory/`    |

---

### Do not mix responsibilities

Examples:

❌ Spec logic inside architecture docs
❌ Implementation details inside spec
❌ New concepts defined inside diagrams

---

## 🔄 Making Changes

### Small changes

* typo fixes
* wording clarity
* link fixes

→ can be submitted directly

---

### Larger changes

If your change affects:

* architecture structure
* terminology
* runtime behavior
* spec definitions

You should:

1. Open an issue first
2. Explain:

   * what is changing
   * why it is needed
   * how it affects the model

---

## 🔍 Documentation Linting

Before submitting any change, contributors should run:

→ `docs/DOCS_LINT_CHECKLIST.md`

This ensures:

* terminology consistency
* canonical phrasing correctness
* architectural boundary integrity

The repository also enforces a strict docs gate in CI.

Pull requests that introduce banned terminology drift or non-canonical phrasing in changed documentation may fail automatically.

---

## 🧪 Adding Examples or Diagrams

When adding diagrams:

* mark them as **non-authoritative**
* ensure they match current terminology
* ensure they align with spec behavior

---

## 🚫 What Not to Do

Do not:

* introduce conflicting terminology
* redefine core concepts
* blur architecture boundaries
* treat CrypSA as a game engine or networking library
* add behavior that is not defined in the spec

---

## 🧭 Contribution Mindset

Good contributions:

* improve clarity
* reinforce consistency
* strengthen boundaries
* make the system easier to understand

Bad contributions:

* add complexity without clarity
* introduce ambiguity
* weaken terminology discipline
* mix responsibilities across layers

---

## 🙌 Final Note

CrypSA is designed to be:

* deterministic
* understandable
* structurally clean

Every contribution should move the project further in that direction.

---

## One Sentence Summary

Contribute by improving clarity and consistency while respecting CrypSA’s strict terminology, architectural boundaries, and spec authority.
