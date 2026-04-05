# Pull Request Checklist

Please confirm the following before submitting your PR.

---

## 🧠 Understanding

* [ ] I understand that CrypSA is an **architecture-first repository**
* [ ] I have read `CONTRIBUTING.md`

---

## 🔒 Authority Rules

* [ ] I did not define runtime behavior outside `spec/`
* [ ] I did not contradict the spec in any document
* [ ] I placed changes in the correct documentation layer

---

## 🧠 Terminology

* [ ] I used terminology exactly as defined in `CrypSA_Terminology_Primer.md`
* [ ] I did not introduce new synonyms for existing concepts
* [ ] I did not redefine any existing terms

---

## 🔐 Canonical Phrasing (Required)

* [ ] I used the exact canonical phrases where applicable:

  * "The validator defines what becomes canonical."
  * "If accepted, an event becomes canonical and is appended to canonical event history."
  * "Canonical event history is the source of truth."
  * "Derived canonical state is a projection of canonical event history. It is not the source of truth."

---

## 🧱 Architectural Boundaries

* [ ] I did not blur boundaries between:

  * Truth (validation + canonical event history)
  * Translation (adapters)
  * Interpretation (lenses)
  * Experience (UI / simulation)

* [ ] I did not introduce logic into the wrong layer

---

## 📚 Documentation Discipline

* [ ] I did not duplicate definitions across documents
* [ ] I referenced existing concepts instead of redefining them
* [ ] My changes improve clarity without adding unnecessary complexity

---

## 🧪 Scope of Change

* [ ] This change is small and self-contained
  OR
* [ ] I opened an issue and discussed larger changes before implementing

---

## 🚫 Final Check

* [ ] This change does not introduce ambiguity
* [ ] This change strengthens consistency
* [ ] This change aligns with CrypSA’s architecture

---

## Summary

Briefly describe your change:

(Write here)
