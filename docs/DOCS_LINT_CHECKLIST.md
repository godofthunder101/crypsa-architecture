# CrypSA Docs Lint Checklist

Use this checklist before committing or submitting a PR.

This is a **self-review tool** to ensure documentation remains consistent, precise, and aligned with CrypSA architecture.

---

## 🧠 Core Model Alignment

* [ ] Does this change align with the CrypSA mental model?
* [ ] Does it reinforce (not weaken) the separation of:

  * Truth
  * Translation
  * Interpretation
  * Experience

---

## 🔒 Authority Rules

* [ ] Am I defining runtime behavior outside `spec/`? (If yes → ❌ fix)
* [ ] Does this contradict anything in `spec/`? (If yes → ❌ fix)
* [ ] Am I explaining vs redefining behavior correctly?

---

## 🧠 Terminology

* [ ] Are all terms used exactly as defined in `CrypSA_Terminology_Primer.md`?
* [ ] Did I accidentally introduce a synonym for a core concept?
* [ ] Did I redefine a term instead of referencing it?

---

## 🔐 Canonical Phrasing (Strict)

If applicable, confirm exact usage:

* [ ] "The validator defines what becomes canonical."

* [ ] "If accepted, an event becomes canonical and is appended to canonical event history."

* [ ] "Canonical event history is the source of truth."

* [ ] "Derived canonical state is a projection of canonical event history. It is not the source of truth."

* [ ] I did not rephrase or approximate these statements

---

## 🔁 Event Lifecycle Consistency

* [ ] Candidate → validation → canonical flow is described correctly
* [ ] I did not skip or compress important steps incorrectly
* [ ] Event transitions match the standard phrasing

---

## 🧱 Architectural Boundaries

* [ ] No mixing of responsibilities between layers
* [ ] Adapters do not define meaning
* [ ] Lenses do not define truth
* [ ] UI does not define canonical state
* [ ] Observers do not define canonical truth

---

## 📚 Definition Discipline

* [ ] Did I define a concept more than once?

* [ ] If yes → should it instead reference the Terminology Primer?

* [ ] Did I introduce a new concept?

  * [ ] If yes → did I add it to the Terminology Primer?

---

## ✍️ Writing Quality

* [ ] Is the language direct and precise?
* [ ] Did I remove unnecessary words or fluff?
* [ ] Would a new reader understand this without guessing?

---

## 🔍 Consistency Check

* [ ] Does this wording match how the concept is described elsewhere?
* [ ] Would this sentence feel out of place in another CrypSA doc?
* [ ] Does this feel like the same “voice” as the rest of the repo?

---

## 🚫 Anti-Patterns

* [ ] I did NOT:

  * redefine concepts
  * introduce vague language
  * mix layers
  * add speculative behavior into authoritative docs
  * describe implementation inside spec

---

## 🧪 Final Sanity Check

* [ ] This change improves clarity
* [ ] This change strengthens consistency
* [ ] This change reinforces the architecture

---

## 🏁 Final Question

> If someone copied my wording into another doc, would it still be correct?

* [ ] Yes → good
* [ ] No → revise

---
