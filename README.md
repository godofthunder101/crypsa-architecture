## Specification
The CrypSA runtime behaviour is formally defined in '/spec/CrypSA_runtime_spec_v0.1.md'

New to CrypSA?

Start here:
- 📘 CRYPSA_IN_5_MINUTES.md
- 📖 TERMINOLOGY_PRIMER.md

# CrypSA - Cryptid Server Architecture

CrypSA is an architecture for building **persistent, event-driven multiplayer worlds**.

Instead of synchronizing full world state between clients and servers, CrypSA synchronizes **canonical events** and **invariant rules**.

Observers simulate the world locally, while the server validates actions and preserves shared truth.

---

## The Shift

Traditional multiplayer systems are typically:

- server-authoritative simulations  
- continuously synchronizing world state  
- tightly coupling simulation and authority  

CrypSA separates these concerns:

- **Observers (clients)** simulate locally  
- **The server** validates important actions  
- **Accepted events** define shared reality  
- **World state** is reconstructed from event history  

This shifts the server’s role from:
> simulation engine  
to  
> validator and guardian of canonical truth  

---

## What This Enables

CrypSA enables systems that are:

- **Persistent** — world state is derived from history, not tied to a running server  
- **Replayable** — events can reconstruct past states deterministically  
- **Inspectable** — history becomes a first-class debugging tool  
- **Flexible** — clients can simulate freely without constant synchronization  
- **Rule-driven** — invariants define what is allowed to become real  

These properties are especially useful for:
- sandbox worlds  
- building and crafting systems  
- economic simulations  
- persistent shared environments  

---

## Key Concepts

CrypSA introduces a small set of core concepts:

- **Canonical Events** — validated actions that define shared world history  
- **Observers** — clients that simulate and reconstruct the world locally  
- **Invariant Boundary** — where actions must be validated before becoming real  
- **Invariants** — rules that must always remain true  
- **Minted Identities** — unique objects with canonical identity  
- **Genomes** — deterministic definitions of object structure and behavior  
- **Lenses** — interpretation layers that define how the world is experienced  

For detailed definitions, see `TERMINOLOGY_PRIMER.md`.

---

## Repository Structure

### Foundation  
Conceptual framing and purpose  
`foundation/`

### Core Concepts  
Fundamental rules of CrypSA  
`core_concepts/`

### Architecture  
How the system operates  
`architecture/`

### Design  
Applications in games and systems  
`design/`

### Implementation  
Practical entry points and prototypes  
`implementation/`

### Diagrams  
Visual explanations  
`diagrams/`

### Atlas and Glossary  
Navigation and terminology  
`atlas/`

---

## Getting Started

If you want to go deeper:

1. `foundation/CrypSA_Traditional_vs_CrypSA.md`  
2. `foundation/CrypSA_Universe_Model.md`  
3. `core_concepts/CrypSA_Mental_Model_One_Page.md`  
4. `core_concepts/CrypSA_Object_Model.md`  
5. `core_concepts/CrypSA_Event_Model.md`  
6. `core_concepts/CrypSA_Invariant_Model.md`  
7. `architecture/CrypSA_Client_Observer_Model.md`  
8. `architecture/CrypSA_Server_Responsibility_Model.md`
9. `architecture/CrypSA_Client_Authority_and_Security.md`  

For a high-level overview, see `ARCHITECTURE_OVERVIEW.md`.

---

## Project Status

CrypSA is currently a **conceptual architecture and research model**.

- Documentation is actively evolving  
- Teaching prototypes are available  
- A networked reference implementation is planned  

---

## One Sentence Summary

CrypSA is an event-driven architecture where observers simulate the world locally while a server validates events and preserves the canonical history of a shared, persistent universe.

---

## Author

Beau Wells  
Creator of the CrypSA architecture

---

## License

Creative Commons Attribution 4.0 International

---

## Citation

If you reference or build upon this work, please use `CITATION.cff`.
