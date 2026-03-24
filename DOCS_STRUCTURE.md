# CrypSA Documentation Structure

CrypSA uses a layered documentation system so that each concept has a clear source of truth.

---

## Core Learning Path

* `CrypSA_In_5_Minutes.md`
* `CrypSA_Terminology_Primer.md`
* `FAQ.md`
* `CrypSA_Worked_Example.md`

---

## System Definition (Authoritative)

* `architecture/`
* `spec/`

---

## Implementation Direction

* `implementation/`

---

## Teaching System

* `teaching/`

---

## Supporting and Reference Content

* `diagrams/`
* `atlas/`
* `design/`

---

## Exploratory Content

* `exploratory/`

---

## Authority Rule

If multiple documents appear to describe the same concept, the following precedence applies:

1. `spec/` (runtime behavior — highest authority)
2. `architecture/` (system structure)
3. `implementation/` (build direction)
4. `teaching/` (examples and explanations)
5. supporting and exploratory content

Supporting and exploratory documents must not be treated as authoritative definitions of current CrypSA behavior.

---

## Consistency Rule

If two documents describe the same concept at the same level:

> one must be demoted or removed

No duplicate authoritative explanations are allowed.
