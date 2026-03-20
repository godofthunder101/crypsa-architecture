---
# CrypSA - Cryptid Server Architecture

CrypSA is an event-driven architecture for building persistent digital worlds.

Instead of synchronizing full world state, CrypSA synchronizes **canonical events and invariant rules**.

Observers simulate the world locally, while a server validates events and preserves shared truth.

---

## 🚀 Start Here

If you're new to CrypSA:

1. 📘 `CRYPSA_IN_5_MINUTES.md` — quick overview  
2. 📖 `TERMINOLOGY_PRIMER.md` — understand the vocabulary  
3. ❓ `FAQ.md` — common questions and concerns  

---

## 🧠 For Technical Readers

If you want to understand how CrypSA actually works:

1. `spec/CrypSA_Runtime_Spec_v0.1.md`  
2. `spec/README.md` (spec reading order)  
3. `implementation/CrypSA_Minimal_Server_v0.1.md`  

These define the runtime behavior and how the system can be implemented.

---

## 🔄 The Core Idea

Traditional multiplayer systems:

- server simulates the world  
- clients receive state updates  

CrypSA:

- clients (observers) simulate locally  
- actions become candidate events  
- server validates events  
- accepted events form canonical history  
- world state is reconstructed from that history  

> The system moves from synchronizing state → to agreeing on events.

---

## ⚙️ What CrypSA Enables

- Persistent worlds independent of specific servers  
- Deterministic world reconstruction  
- Built-in replay and debugging via event history  
- Flexible client-side simulation  
- Strong invariant-based validation  
- Potential for new gameplay models (branching timelines, observer-driven views)  

---

## 🧩 Key Concepts

- **Minted Identities** — persistent object identities  
- **Genomes** — versioned object definitions  
- **Canonical Events** — source of world change  
- **Invariants** — rules that must always hold  
- **Observers** — clients that reconstruct and simulate  
- **Lenses** — interpretation layers (view-dependent logic)  

See `TERMINOLOGY_PRIMER.md` for detailed explanations.

---

## 📁 Repository Structure

### Foundation

Conceptual framing and motivation.

---

foundation/

---

---

### Core Concepts

High-level system models.

---

core-concepts/

---

---

### Architecture

How CrypSA operates conceptually.

---

architecture/

---

---

### Specifications (Core Runtime Behavior)

Formal system definitions.

---

spec/

---

Includes:
- runtime model  
- event model  
- validation model  
- consistency model  
- replay model  
- snapshot model  
- identity model  
- transport model  

---

### Design

Use cases, patterns, and applicability.

---

design/

---

---

### Implementation

Practical guides and prototype direction.

---

implementation/

---

---

### Diagrams

Visual explanations of system behavior.

---

diagrams/

---

---

### Atlas

Glossary and navigation support.

---

atlas/

---

---

## 🛠 Current Project Status

CrypSA is currently:

- a defined architecture with formal specifications  
- supported by documentation and a teaching prototype  
- not yet a production-ready system  

Next major step:

→ building a minimal independent server to validate the runtime model  

See:
`implementation/CrypSA_Project_Status.md` (if present)

---

## 🧭 Recommended Reading Path

### New to CrypSA
1. 5-minute overview  
2. terminology primer  
3. FAQ  

---

### Architecture understanding
1. foundation docs  
2. core concepts  
3. architecture docs  

---

### Implementation understanding
1. runtime spec  
2. event + validation models  
3. minimal server doc  

---

## ⚠️ Scope and Limitations

CrypSA v0.1 is best suited for:

- persistent worlds  
- simulation-heavy systems  
- object-driven interactions  

It is not yet optimized for:

- twitch shooters  
- frame-perfect PvP  
- heavy physics-based simulation  

---

## 👤 Author

Beau Wells

---

## 📄 License

Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 📌 Citation

If referencing this work, see `CITATION.cff`.

---

## One Sentence Summary

CrypSA is an event-driven architecture where clients simulate locally, servers validate events, and shared reality is defined by a canonical history of those events.
---
---
t’s the next thing that will make your repo feel like a real engineering artifact instead of just documentation.
