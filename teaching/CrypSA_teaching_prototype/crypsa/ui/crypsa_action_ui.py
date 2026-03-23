from __future__ import annotations

import tkinter as tk
from typing import Any

from ..crypsa_teaching_theme import ACCENT, BG, MUTED, PANEL, TEXT


def open_mint_modal(app: Any) -> None:
    """Show direct server mint actions that create canonical events immediately."""

    modal = app._open_modal("Server Mint", "360x420")
    lens = app._mint_action_modal_lens()
    # The action UI now renders pre-shaped option/request data from the lens
    # adapter instead of discovering runtime/catalog details inline.
    # This is the shortest action modal on purpose. Its job is to contrast
    # immediate canonical creation with the longer observer-side build flow.
    tk.Label(modal, text="Server Mint", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(modal, text="Server minting accepts canonical mint events directly into the event graph.", bg=BG, fg=MUTED, justify="left", wraplength=310).pack(anchor="w", padx=18, pady=(0, 12))

    # Header actions stay separate from the kind list so the modal reads as:
    # refresh/open tooling first, then choose one immediate canonical action.
    header_actions = tk.Frame(modal, bg=BG)
    header_actions.pack(fill="x", padx=18, pady=(0, 10))
    tk.Button(header_actions, text="Reload Catalog", command=lambda req=lens.reload_request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="left")
    tk.Button(header_actions, text="Open Mint Editor", command=lambda req=lens.open_editor_request: app._execute_action_request(req), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="right")
    shell = tk.Frame(modal, bg=BG)
    shell.pack(fill="both", expand=True, padx=18, pady=(0, 18))
    for option in lens.options:
        row = tk.Frame(shell, bg=BG)
        row.pack(fill="x", pady=4)
        tk.Label(row, text=option.kind, bg=BG, fg=TEXT, anchor="w", font=("Consolas", 11)).pack(side="left")
        tk.Button(row, text="Mint", command=lambda req=option.request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 9), cursor="hand2").pack(side="right")
        if option.requires_causal_context:
            tk.Label(row, text="requires causal context", bg=BG, fg="#fde68a", anchor="e", font=("Segoe UI", 9)).pack(side="right", padx=(0, 10))


def open_build_modal(app: Any) -> None:
    """Show observer-side build candidates before they cross the invariant boundary."""

    modal = app._open_modal("Build", "420x560")
    lens = app._build_action_modal_lens()
    # This is the teaching-heavy action modal, so it spends more space on
    # context hints, Beacon guidance, and per-kind summaries than the server
    # mint modal does.
    tk.Label(modal, text="Build", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    actions = tk.Frame(modal, bg=BG)
    actions.pack(fill="x", padx=18, pady=(0, 8))
    tk.Button(actions, text="Reload Catalog", command=lambda req=lens.reload_request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(side="right")
    tx, ty = lens.target_tile
    tk.Label(modal, text=f"Choose a Mint kind to submit as an invariant-boundary build candidate at ({tx}, {ty}).", bg=BG, fg=MUTED, justify="left", wraplength=360).pack(anchor="w", padx=18, pady=(0, 12))
    tk.Label(
        modal,
        text=(
            "Kinds with context rules need matching canonical history on the currently viewed lineage. "
            "Beacon is the teaching example and is easiest to understand after loading the teaching example."
        ),
        bg=BG,
        fg="#fde68a",
        justify="left",
        wraplength=360,
        font=("Segoe UI", 9),
    ).pack(anchor="w", padx=18, pady=(0, 10))
    if not lens.teaching_example_loaded:
        prompt_row = tk.Frame(modal, bg=BG)
        prompt_row.pack(fill="x", padx=18, pady=(0, 10))
        tk.Label(prompt_row, text="Want the clearest example first?", bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(side="left")
        tk.Button(prompt_row, text="Load Example + Focus Beacon", command=lambda req=lens.try_beacon_request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 9), cursor="hand2").pack(side="right")

    # The scrollable card list is the real body of this modal. Each card
    # summarizes one Mint kind before the user submits it as a local candidate.
    canvas = tk.Canvas(modal, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(modal, orient="vertical", command=canvas.yview)
    content = tk.Frame(canvas, bg=BG)
    content.bind("<Configure>", lambda _event, c=canvas: c.configure(scrollregion=c.bbox("all")))
    canvas.create_window((0, 0), window=content, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=(18, 0), pady=(0, 18))
    scrollbar.pack(side="right", fill="y", padx=(0, 18), pady=(0, 18))
    for card_lens in lens.cards:
        card = tk.Frame(content, bg=PANEL, highlightbackground="#243d6b", highlightthickness=1)
        card.pack(fill="x", pady=6)
        top = tk.Frame(card, bg=PANEL)
        top.pack(fill="x", padx=12, pady=(10, 4))
        tk.Label(top, text=card_lens.kind, bg=PANEL, fg=ACCENT, anchor="w", font=("Consolas", 12, "bold")).pack(side="left")
        if card_lens.is_selected:
            tk.Label(top, text="Selected", bg=PANEL, fg=TEXT, anchor="e", font=("Segoe UI", 9)).pack(side="right")
        tk.Label(card, text=card_lens.rule_tags_text, bg=PANEL, fg=TEXT, anchor="w", justify="left", wraplength=300).pack(fill="x", padx=12)
        tk.Label(card, text=card_lens.actions_summary_text, bg=PANEL, fg=MUTED, anchor="w", justify="left", wraplength=300).pack(fill="x", padx=12, pady=(2, 8))
        if card_lens.context_hint is not None:
            tk.Label(card, text=card_lens.context_hint, bg=PANEL, fg="#fde68a", anchor="w", justify="left", wraplength=300, font=("Segoe UI", 9)).pack(fill="x", padx=12, pady=(0, 8))
        if card_lens.beacon_hint is not None:
            tk.Label(card, text=card_lens.beacon_hint, bg=PANEL, fg=MUTED, anchor="w", justify="left", wraplength=300, font=("Segoe UI", 9)).pack(fill="x", padx=12, pady=(0, 8))
        tk.Button(card, text="Submit Build Candidate", command=lambda req=card_lens.request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 9), cursor="hand2").pack(anchor="e", padx=12, pady=(0, 10))


def open_candidate_modal(app: Any) -> None:
    """Show queued observer-side candidates awaiting canonical reconciliation."""

    modal = app._open_modal("Invariant-Boundary Candidates", "460x420")
    lens = app._candidate_queue_lens()
    # This modal is a queue inspector, not a second action-creation surface.
    # It lists the pending submissions in order and gives one escape hatch:
    # clearing the queue.
    tk.Label(modal, text="Invariant-Boundary Candidates", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(anchor="w", padx=18, pady=(16, 8))
    tk.Label(modal, text="These observer-side candidates are waiting to cross the invariant boundary and become canonical events.", bg=BG, fg=MUTED, justify="left", wraplength=390).pack(anchor="w", padx=18, pady=(0, 10))

    # Keep the body intentionally plain: order and queue contents matter more
    # here than rich card presentation.
    listbox = tk.Listbox(modal, bg="#0b1326", fg=TEXT, font=("Consolas", 10), relief="flat")
    listbox.pack(fill="both", expand=True, padx=18, pady=(0, 12))
    for line in lens.lines:
        listbox.insert("end", line)
    tk.Button(modal, text="Clear Candidates", command=lambda req=lens.clear_request, m=modal: app._execute_action_request(req, m), bg="#1f3357", fg=TEXT, activebackground="#29467a", activeforeground=TEXT, relief="solid", bd=1, font=("Segoe UI", 10), cursor="hand2").pack(anchor="e", padx=18, pady=(0, 18))
