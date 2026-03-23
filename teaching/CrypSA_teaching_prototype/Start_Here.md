# Start Here

This is the quickest guide for learning the project without getting lost.

This project should now be read as a completed teaching artifact. Start with `STATUS.md` if you want the current maintenance posture before reading code.

For the authoritative adapter and observer-model docs, see:

- `../../architecture/CrypSA_Adaptor_Model.md`
- `../../architecture/CrypSA_Client_Observer_Model.md`

Use this file when your question is:

- Where do I start?
- What should I open next?
- Which doc or file answers the kind of question I have?

## The Short Version

The project is easiest to understand in this order:

1. `README.md`
2. `STATUS.md`
3. `Codebase_Walkthrough.md`
4. `Prototype_vs_Current_CrypSA_Model.md`
5. `implementation/CrypSA_Teaching_Prototype_Layers.md`
6. `implementation/CrypSA_Refactor_Guardrails.md`
7. the package `REFERENCE.md` files
8. source files only after you know which layer you are trying to read

If you want the fastest mental model first:

- observer actions are local first
- build/destroy become candidate events
- canonical reconciliation accepts or rejects them
- accepted canonical history is the source of truth
- visible canonical state is replay-derived from that history

## The Main Layer Stack

Keep this architecture stack in mind:

1. runtime/controller
2. replay/event graph
3. adapters
4. lenses and typed requests
5. UI modules
6. Mint modules

If a file feels confusing, first ask which layer it belongs to.

## Best First Reading Path

If you are new to the repo, use this path:

1. Read `README.md`
2. Read `Codebase_Walkthrough.md`
3. Read `crypsa/REFERENCE.md`
4. Open `crypsa/crypsa_teaching_prototype.py`
5. Then read these runtime files in order:
   - `crypsa/runtime_store.py`
   - `crypsa/runtime_models.py`
   - `crypsa/runtime_actions.py`
   - `crypsa/validation.py`
   - `crypsa/reconciliation.py`
   - `crypsa/canonical_apply.py`
   - `crypsa/canonical_replay.py`
   - `crypsa/request_dispatch.py`
6. Then read:
   - `crypsa/crypsa_lens_adapters.py`
   - `crypsa/ui/REFERENCE.md`
   - the specific UI file you care about

That path gives you meaning first, then runtime mechanics, then UI handoff.

## If You Want To Run The App First

Use this order:

1. Run `.\start-crypsa-teaching-prototype.cmd`
2. Click `How To Read`
3. Click `Load Teaching Example`
4. Open `History`
5. Open `Timeline`
6. Queue a build candidate
7. Reconcile it
8. Compare the observer pane, canonical pane, and accepted history

That is the best end-to-end teaching loop in the project.

## If You Have One Specific Question

Use this shortcut map.

### "How does runtime meaning work?"

Go to:

1. `crypsa/crypsa_teaching_prototype.py`
2. `crypsa/runtime_store.py`
3. `crypsa/runtime_models.py`

### "Why was a candidate event accepted or rejected?"

Go to:

1. `crypsa/validation.py`
2. `crypsa/reconciliation.py`
3. `crypsa/canonical_apply.py`

### "How does accepted history become visible state?"

Go to:

1. `crypsa/canonical_replay.py`
2. `crypsa/crypsa_event_graph.py`

### "Why does this button or modal do this?"

Go to:

1. the matching UI file in `crypsa/ui/`
2. `crypsa/crypsa_lens_adapters.py`
3. `crypsa/crypsa_action_requests.py`
4. `crypsa/request_dispatch.py`
5. the targeted controller method in `crypsa/crypsa_teaching_prototype.py`

### "How does the UI stay separate from runtime meaning?"

Go to:

1. `README.md`
2. `crypsa/REFERENCE.md`
3. `crypsa/ui/REFERENCE.md`
4. `crypsa/crypsa_lens_adapters.py`
5. `crypsa/crypsa_action_requests.py`
6. `crypsa/request_dispatch.py`

### "How does Mint work?"

Go to:

1. `Mint_Editor_Usage.md`
2. `mint/REFERENCE.md`
3. `mint/mint_catalog_editor.py`
4. `mint/mint_models.py`
5. `mint/mint_lens_adapters.py`
6. `mint/mint_editor_ui.py`
7. `mint/mint_catalog_store.py`

### "How does this prototype relate to the broader CrypSA model?"

Go to:

1. `Prototype_vs_Current_CrypSA_Model.md`
2. then the newer `repo/` docs if needed

## If You Changed Code

For the fastest confidence check:

1. run `python -m unittest`
2. use `Manual_Regression_Checklist.md` for Tk/manual flows

## Final Advice

Do not read everything linearly.

Instead:

1. choose one flow
2. follow it across layers
3. return to the reference docs when you lose orientation

The best first flow is still:

1. load the teaching example
2. queue a build
3. reconcile it
4. inspect History and Timeline
5. trace that exact path in code
