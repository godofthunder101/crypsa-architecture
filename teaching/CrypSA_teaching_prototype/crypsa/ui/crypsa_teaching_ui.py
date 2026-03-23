from __future__ import annotations

import tkinter as tk
from typing import Any

from ..crypsa_teaching_theme import BG, MUTED, TEXT


def open_teaching_modal(app: Any) -> None:
    """Explain the core CrypSA teaching model used by this prototype."""

    modal = app._open_modal("How To Read CrypSA", "620x560")
    tk.Label(modal, text="How To Read CrypSA", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text=(
            "This prototype teaches the core CrypSA split between observer-local state, "
            "candidate events at the invariant boundary, and accepted canonical history."
        ),
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=560,
    ).pack(anchor="w", padx=18, pady=(0, 12))

    # This modal is the high-level mental-model entrypoint. Keep it focused on
    # the teaching loop before dropping into narrower pane or timeline details.
    info = tk.Text(
        modal,
        bg="#0b1326",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        wrap="word",
        font=("Consolas", 10),
        height=18,
    )
    info.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    info.insert(
        "1.0",
        "\n".join(
            [
                "1. Observer Representation",
                "   The observer moves locally. This is not automatically canonical truth.",
                "   In plain English: the right pane shows local player intent, not official world state.",
                "",
                "2. Candidate Events At The Invariant Boundary",
                "   Build and destroy actions wait here as candidate events until canonical reconciliation.",
                "   In plain English: these are pending local actions that have not been accepted into canonical history yet.",
                "",
                "3. Canonical Representation",
                "   The server pane shows replay-derived canonical state built from accepted canonical events.",
                "   In plain English: the left pane shows what the world officially knows.",
                "",
                "4. Accepted Canonical History",
                "   Accepted canonical history is the substrate of truth in this prototype. State is reconstructed from event replay.",
                "",
                "5. Event Lineage",
                "   Reconciling from an older canonical event forks a new event lineage.",
                "   In plain English: choosing older history and acting from there creates an alternate branch.",
                "   Timeline rows help humans inspect those forks, but the rows themselves are not canonical truth.",
                "",
                "6. Best First Path",
                "   Load Teaching Example.",
                "   Open History.",
                "   Open Timeline.",
                "   Queue a build candidate event.",
                "   Reconcile to canonical truth.",
                "   Return to History and compare observer-local state against accepted canonical history.",
                "",
                "7. Lineage Parent vs Causal References",
                "   lineage_parent drives deterministic replay.",
                "   causal_references are shown for causal context and can also affect validation rules.",
                "   Try the Beacon Mint kind after loading the teaching example.",
                "   Because canonical history already exists there, Beacon has the structural causal context it requires.",
                "",
                "8. Mint",
                "   Mint definitions supply immutable canonical object definitions and genomes for future accepted canonical events.",
                "",
                "9. Scope Of This Prototype",
                "   This is a teaching model, not a networking benchmark or production server architecture.",
                "   It is meant to show the CrypSA split clearly before real runtime constraints are added.",
                "   It deliberately avoids sockets, distributed processes, deployment concerns, and production anti-cheat machinery.",
                "",
                "Use 'Load Teaching Example' below if you want a small prebuilt event history with a fork.",
            ]
        ),
    )
    info.configure(state="disabled")

    # Keep the teaching actions adjacent to the explanation so the user can
    # move directly from reading the model to loading or testing it.
    actions = tk.Frame(modal, bg=BG)
    actions.pack(fill="x", padx=18, pady=(0, 18))
    tk.Button(actions, text="Load Teaching Example", command=lambda m=modal: app._load_teaching_example(m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left")
    tk.Button(actions, text="Try Beacon", command=lambda m=modal: app._try_beacon_path(m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left", padx=(8, 0))
    tk.Button(actions, text="Reset To Fresh Install", command=lambda m=modal: _reset_from_teaching_modal(app, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left", padx=(8, 0))
    tk.Button(actions, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="right")


def _reset_from_teaching_modal(app: Any, modal: tk.Toplevel | None = None) -> None:
    """Reset the runtime to the fresh-install baseline from teaching UI."""

    app._wipe_to_fresh_start()
    if isinstance(modal, tk.Toplevel) and modal.winfo_exists():
        modal.destroy()


def open_walkthrough_modal(app: Any) -> None:
    """Give a concrete reading order for exploring the prototype."""

    modal = app._open_modal("CrypSA Walkthrough", "680x560")
    tk.Label(modal, text="CrypSA Walkthrough", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text=(
            "This walkthrough gives one concrete way to read the prototype. "
            "It works best after loading the teaching example, but it is still useful on an empty baseline."
        ),
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=620,
    ).pack(anchor="w", padx=18, pady=(0, 12))

    # This is the "do these steps in order" companion to How To Read. It
    # should stay procedural so first-time users can follow it linearly.
    walkthrough = tk.Text(
        modal,
        bg="#0b1326",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        wrap="word",
        font=("Consolas", 10),
        height=22,
    )
    walkthrough.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    walkthrough.insert(
        "1.0",
        "\n".join(
            [
                "1. Load a world to inspect",
                "   Use 'How To Read' -> 'Load Teaching Example' if the universe is empty.",
                "",
                "2. Compare the two panes",
                "   Observer Representation shows observer-local state.",
                "   Canonical Representation shows replay-derived canonical state.",
                "",
                "3. Open History",
                "   Canonical events are the substrate of truth in this prototype.",
                "   Selecting an older event changes the canonical state being viewed.",
                "",
                "4. Open Timeline",
                "   Timeline rows visualize event lineage forks.",
                "   The active lineage is the fork target if you reconcile from a shared ancestor.",
                "",
                "5. Queue a build or destroy candidate event",
                "   These actions wait at the invariant boundary until canonical reconciliation.",
                "",
                "6. Reconcile",
                "   Accepted candidate events become canonical events in accepted canonical history.",
                "   If you reconcile from historical selection, the canonical side forks a new event lineage.",
                "",
                "7. Try Beacon",
                "   Load Teaching Example if you have not already.",
                "   Open Build and select Beacon.",
                "   Submit Beacon as a candidate event, then reconcile it.",
                "   Reopen History or Timeline and compare the accepted result against the viewed lineage.",
                "   Beacon demonstrates a Mint genome that checks causal context through causal_references.",
                "",
                "8. Read replay vs context",
                "   lineage_parent drives deterministic replay.",
                "   causal_references do not drive replay, but they can drive contextual validation rules.",
                "   Beacon is the concrete example of a context-sensitive Mint kind.",
                "",
                "9. Read Mint",
                "   Mint definitions provide immutable canonical object definitions and genomes for future accepted events.",
                "",
                "10. Keep the scope in mind",
                "   This prototype is the conceptual front door for CrypSA.",
                "   It is intentionally simpler than a real independent server runtime.",
            ]
        ),
    )
    walkthrough.configure(state="disabled")

    actions = tk.Frame(modal, bg=BG)
    actions.pack(fill="x", padx=18, pady=(0, 18))
    if not app.teaching_example_loaded:
        tk.Button(actions, text="Load Teaching Example", command=lambda m=modal: app._load_teaching_example(m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left")
    tk.Button(actions, text="Try Beacon", command=lambda m=modal: app._try_beacon_path(m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left", padx=(8 if not app.teaching_example_loaded else 0, 0))
    tk.Button(actions, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="right")


def open_model_notes_modal(app: Any) -> None:
    """Summarize the core behavior this prototype is teaching."""

    modal = app._open_modal("Model Notes", "640x460")
    tk.Label(modal, text="Model Notes", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text="These notes summarize the core behavior this prototype is teaching.",
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=580,
    ).pack(anchor="w", padx=18, pady=(0, 12))

    # Model Notes is the compact conceptual summary after the user already has
    # the larger teaching copy from How To Read and Walkthrough.
    notes = tk.Text(
        modal,
        bg="#0b1326",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        wrap="word",
        font=("Consolas", 10),
        height=14,
    )
    notes.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    notes.insert(
        "1.0",
        "\n".join(
            [
                "Observer movement is local only.",
                "",
                "Build and destroy first become candidate events at the invariant boundary.",
                "",
                "In plain English: local actions become official only after canonical validation accepts them.",
                "",
                "Enter submits invariant-boundary candidate events for canonical reconciliation.",
                "",
                "Reconciling from a historical event selection forks a new event lineage.",
                "",
                "In plain English: acting from older accepted history creates a new branch of accepted events.",
                "",
                "Timeline rows are a lineage view, not canonical truth.",
                "",
                "lineage_parent drives replay; causal_references can affect contextual validation.",
                "",
                "This prototype teaches the model shape, not a full independent server runtime.",
                "",
                "It is the conceptual front door for CrypSA, not the final runtime shape under real deployment constraints.",
            ]
        ),
    )
    notes.configure(state="disabled")
    tk.Button(modal, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(anchor="e", padx=18, pady=(0, 18))


def open_hotkeys_modal(app: Any) -> None:
    """List the keyboard shortcuts available in the teaching prototype."""

    modal = app._open_modal("Hotkeys", "520x420")
    tk.Label(modal, text="Hotkeys", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(
        modal,
        text="These keyboard shortcuts are available in the main prototype window.",
        bg=BG,
        fg=MUTED,
        justify="left",
        wraplength=460,
    ).pack(anchor="w", padx=18, pady=(0, 12))

    shortcuts = tk.Text(
        modal,
        bg="#0b1326",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        wrap="word",
        font=("Consolas", 10),
        height=14,
    )
    shortcuts.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    shortcuts.insert(
        "1.0",
        "\n".join(
            [
                "W  -> move observer north",
                "A  -> move observer west",
                "S  -> move observer south",
                "D  -> move observer east",
                "",
                "B      -> open Build",
                "F      -> queue Destroy candidate",
                "Enter  -> reconcile invariant-boundary candidates",
                "",
                "Escape -> close the current modal, or close the app from the main window",
                "F12    -> reset to fresh install baseline",
            ]
        ),
    )
    shortcuts.configure(state="disabled")
    tk.Button(modal, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(anchor="e", padx=18, pady=(0, 18))


def open_pane_help_modal(app: Any, pane_name: str) -> None:
    """Explain one main pane without keeping the text inline in the layout."""

    pane_key = pane_name.lower().strip()
    if pane_key == "canonical":
        title = "Canonical Pane Help"
        lines = [
            "Selected Event: the canonical event currently being viewed and replayed.",
            "",
            "Branch: the currently viewed event lineage.",
            "",
            "Lineage: the branch of accepted history you are currently looking through.",
            "",
            "Branch Head: the latest accepted event on the active event lineage.",
            "",
            "Canonical Events: the accepted events that define canonical history.",
            "",
            "Canonical: official or accepted by the model shown in this prototype.",
            "",
            "Catalog: the active Mint definition set used for future accepted objects.",
            "",
            "Lineage Event Families: the event-family types visible on the currently viewed lineage.",
            "",
            "Teaching scope: this pane explains the model, not a full independent server runtime.",
            "",
            "It shows the conceptual shape of CrypSA, not the deployment shape of a real authority.",
        ]
    else:
        title = "Observer Pane Help"
        lines = [
            "Target Tile: build and destroy submit against the tile in front of the observer.",
            "",
            "Build Kind: the Mint kind that will be used for the next build candidate.",
            "",
            "Mint kind: the authored object definition that future accepted objects freeze from.",
            "",
            "Pending Canonical Events: observer-side candidate events waiting at the invariant boundary.",
            "",
            "Pending submissions: local candidate events that have not been accepted into canonical history yet.",
            "",
            "Invariant-Boundary Candidates: candidate events that are not canonical yet.",
            "",
            "Context-rule hints: some kinds, such as Beacon, require matching canonical context on the viewed lineage.",
            "",
            "Teaching scope: this pane shows the local-vs-canonical split clearly, not every runtime concern a deployed system would carry.",
        ]

    modal = app._open_modal(title, "520x420")
    tk.Label(modal, text=title, bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))

    # Pane help stays narrower than How To Read. It is meant for quick label
    # clarification while the user is already looking at the main window.
    body = tk.Text(
        modal,
        bg="#0b1326",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        wrap="word",
        font=("Consolas", 10),
        height=14,
    )
    body.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    body.insert("1.0", "\n".join(lines))
    body.configure(state="disabled")
    tk.Button(modal, text="Close", command=modal.destroy, bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(anchor="e", padx=18, pady=(0, 18))
