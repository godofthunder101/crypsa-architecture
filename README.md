New to CrypSA?

Start here:
- 📘 CRYPSA_IN_5_MINUTES.md
- 📖 TERMINOLOGY_PRIMER.md

# CrypSA - Cryptid Server Architecture

CrypSA is an architecture for building persistent digital universes.

Instead of synchronizing full world state between clients and servers, CrypSA synchronizes canonical events and invariant rules.

Observers reconstruct the universe locally, while the server validates and preserves shared truth.

## The Shift

Traditional multiplayer systems are usually based on clients, a server, and shared world state.

CrypSA is based on observers, events, validation, canonical history, and reconstruction.

This changes the role of the server from a simulation engine to a guardian of canonical truth.

## What This Enables

- Persistent worlds independent of specific servers
- Deterministic world reconstruction
- Built-in replay and time-travel debugging
- Flexible client-side simulation
- Strong invariant-based validation
- New gameplay possibilities such as branching timelines and observer-driven worlds

## Key Concepts

- Minted Identities - unique objects with canonical identity
- Genomes - deterministic definitions of object structure
- Canonical Events - the source of world evolution
- Invariants - rules that must always remain true
- Observers - clients that simulate and reconstruct reality
- Lenses - interpretation layers that define experiences

## Repository Structure

### Foundation

Conceptual framing and purpose.

Folder: `foundation/`

### Core Concepts

The fundamental rules of CrypSA.

Folder: `core_concepts/`

### Architecture

How the system operates.

Folder: `architecture/`

### Design

How CrypSA can be used in games and systems.

Folder: `design/`

### Implementation

Practical entry points for developers.

Folder: `implementation/`

### Diagrams

Visual explanations of the system.

Folder: `diagrams/`

### Atlas and Glossary

Navigation and terminology reference.

Folder: `atlas/`

## Getting Started

If you are new to CrypSA, start with these documents:

1. `foundation/CrypSA_Traditional_vs_CrypSA.md`
2. `foundation/CrypSA_Universe_Model.md`
3. `core_concepts/CrypSA_Mental_Model_One_Page.md`
4. `core_concepts/CrypSA_Object_Model.md`
5. `core_concepts/CrypSA_Event_Model.md`
6. `core_concepts/CrypSA_Invariant_Model.md`
7. `architecture/CrypSA_Client_Observer_Model.md`
8. `architecture/CrypSA_Server_Responsibility_Model.md`

For a high-level overview, see `ARCHITECTURE_OVERVIEW.md`.

## Project Status

CrypSA is currently a conceptual architecture and research model.

- Documentation is actively evolving
- Prototype systems are in development
- Future work may include engine integrations and reference implementations

## Author

Beau Wells

Creator of the CrypSA architecture.

## License

This project is licensed under Creative Commons Attribution 4.0 International.

## Citation

If you reference or build upon this work, please use `CITATION.cff`.

## One Sentence Summary

CrypSA is an event-driven architecture where observers simulate the world locally while a canonical server validates events and preserves the shared history of a persistent digital universe.

