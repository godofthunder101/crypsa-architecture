from __future__ import annotations

from dataclasses import dataclass

from mint.mint_models import (
    InvariantState,
    MintedDefinition,
    copy_invariant_state,
    copy_minted_definition,
    is_invariant_state,
    is_minted_definition,
)

# This module is the typed runtime vocabulary for the teaching prototype.
# The goal is not to eliminate every dict at once. The goal is to give names to
# the highest-value runtime records first, then let the remaining dynamic data
# stay intentionally flexible unless a real shared seam proves it needs more
# structure.
#
# Reading tip:
# 1. start with CandidateEvent and CanonicalEvent to understand queued intent
#    versus accepted canonical history
# 2. then read ReplayObjectRecord and ReplayBranchState for replay-derived state
# 3. then read the payload classes to see what accepted structural events carry
# 4. read this as a completed teaching artifact: type the critical seams, not
#    every last inner map just because it is possible


@dataclass(frozen=True)
class CandidateEvent:
    """Typed observer-side candidate waiting for canonical validation."""

    action: str
    x: int
    y: int
    kind: str | None = None

    def to_dict(self) -> dict[str, object]:
        data: dict[str, object] = {"action": self.action, "x": self.x, "y": self.y}
        if self.kind is not None:
            data["kind"] = self.kind
        return data

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "CandidateEvent | None":
        action = data.get("action")
        x = data.get("x")
        y = data.get("y")
        if not isinstance(action, str) or not isinstance(x, int) or not isinstance(y, int):
            return None
        kind = data.get("kind")
        kind_value = str(kind) if isinstance(kind, str) else None
        return cls(action=action, x=x, y=y, kind=kind_value)


@dataclass(frozen=True)
class CanonicalEvent:
    """Typed accepted canonical event record."""

    # The top-level accepted event envelope is typed here, but payload remains a
    # dict so the prototype can migrate accepted payload shapes gradually.

    sequence: int
    event_id: str
    event_family: str
    event_type: str
    target_identity: str
    observer_identity: str
    timestamp: str
    lineage_parent: str | None
    causal_references: list[str]
    branch_hint: str
    catalog_version: int
    payload: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return {
            "sequence": self.sequence,
            "event_id": self.event_id,
            "event_family": self.event_family,
            "event_type": self.event_type,
            "target_identity": self.target_identity,
            "observer_identity": self.observer_identity,
            "timestamp": self.timestamp,
            "lineage_parent": self.lineage_parent,
            "causal_references": list(self.causal_references),
            "branch_hint": self.branch_hint,
            "catalog_version": self.catalog_version,
            "payload": dict(self.payload),
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "CanonicalEvent | None":
        sequence = data.get("sequence")
        event_id = data.get("event_id")
        event_family = data.get("event_family")
        event_type = data.get("event_type")
        target_identity = data.get("target_identity")
        observer_identity = data.get("observer_identity")
        timestamp = data.get("timestamp")
        branch_hint = data.get("branch_hint")
        catalog_version = data.get("catalog_version")
        payload = data.get("payload")
        if not all(
            [
                isinstance(sequence, int),
                isinstance(event_id, str),
                isinstance(event_family, str),
                isinstance(event_type, str),
                isinstance(target_identity, str),
                isinstance(observer_identity, str),
                isinstance(timestamp, str),
                isinstance(branch_hint, str),
                isinstance(catalog_version, int),
                isinstance(payload, dict),
            ]
        ):
            return None
        if not _valid_canonical_payload(event_type, payload):
            return None
        raw_parent = data.get("lineage_parent")
        lineage_parent = str(raw_parent) if isinstance(raw_parent, str) else None
        causal_references = [str(ref) for ref in data.get("causal_references", []) if isinstance(ref, str)]
        return cls(
            sequence=sequence,
            event_id=event_id,
            event_family=event_family,
            event_type=event_type,
            target_identity=target_identity,
            observer_identity=observer_identity,
            timestamp=timestamp,
            lineage_parent=lineage_parent,
            causal_references=causal_references,
            branch_hint=branch_hint,
            catalog_version=catalog_version,
            payload=dict(payload),
        )


@dataclass(frozen=True)
class ReplayObjectRecord:
    """Typed replay-derived canonical object visible at one history point."""

    # Replay objects now type both shared inner seams they carry repeatedly:
    # invariant state and frozen Mint definition.

    object_id: str
    kind: str
    x: int
    y: int
    invariant_state: InvariantState
    minted_definition: MintedDefinition

    def to_dict(self) -> dict[str, object]:
        return {
            "object_id": self.object_id,
            "kind": self.kind,
            "x": self.x,
            "y": self.y,
            "invariant_state": copy_invariant_state(self.invariant_state),
            "minted_definition": copy_minted_definition(self.minted_definition),
        }


@dataclass(frozen=True)
class ReplayBranchState:
    """Typed replay-derived canonical state for one selected branch head."""

    objects: dict[str, ReplayObjectRecord]
    event_count: int
    head_event_id: str | None


@dataclass(frozen=True)
class PlacedObjectPayload:
    """Typed canonical payload for build_object and mint_object events."""

    # This payload shape is shared by both observer-side build acceptance and
    # server-side direct minting because both actions place one object into the
    # replay-derived canonical world.

    object_id: str
    kind: str
    x: int
    y: int
    invariant_state: InvariantState
    minted_definition: MintedDefinition

    def to_dict(self) -> dict[str, object]:
        return {
            "object_id": self.object_id,
            "kind": self.kind,
            "x": self.x,
            "y": self.y,
            "invariant_state": copy_invariant_state(self.invariant_state),
            "minted_definition": copy_minted_definition(self.minted_definition),
        }


@dataclass(frozen=True)
class DestroyedObjectPayload:
    """Typed canonical payload for destroy_object events."""

    # Destroy keeps both prior and next invariant state so accepted canonical
    # history records what object was removed and what state transition justified
    # that removal.

    object_id: str
    kind: str
    x: int
    y: int
    prior_invariant_state: InvariantState
    next_invariant_state: InvariantState

    def to_dict(self) -> dict[str, object]:
        return {
            "object_id": self.object_id,
            "kind": self.kind,
            "x": self.x,
            "y": self.y,
            "prior_invariant_state": copy_invariant_state(self.prior_invariant_state),
            "next_invariant_state": copy_invariant_state(self.next_invariant_state),
        }


def _valid_canonical_payload(event_type: str, payload: dict[str, object]) -> bool:
    """Validate the accepted payload shape for the known structural event types."""

    if event_type in {"build_object", "mint_object"}:
        return all(
            [
                isinstance(payload.get("object_id"), str),
                isinstance(payload.get("kind"), str),
                isinstance(payload.get("x"), int),
                isinstance(payload.get("y"), int),
                is_invariant_state(payload.get("invariant_state")),
                is_minted_definition(payload.get("minted_definition")),
            ]
        )
    if event_type == "destroy_object":
        return all(
            [
                isinstance(payload.get("object_id"), str),
                isinstance(payload.get("kind"), str),
                isinstance(payload.get("x"), int),
                isinstance(payload.get("y"), int),
                is_invariant_state(payload.get("prior_invariant_state")),
                is_invariant_state(payload.get("next_invariant_state")),
            ]
        )
    return True
