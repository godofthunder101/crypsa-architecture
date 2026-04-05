#!/usr/bin/env bash
set -euo pipefail

BASE_REF="${1:-origin/main}"

changed_files="$(git diff --name-only "$BASE_REF"...HEAD -- '*.md' '*.MD' || true)"

if [[ -z "$changed_files" ]]; then
  echo "No markdown files changed."
  exit 0
fi

echo "Checking changed markdown files:"
echo "$changed_files"
echo

failed=0

check_pattern() {
  local pattern="$1"
  local message="$2"

  if grep -nE "$pattern" $changed_files; then
    echo
    echo "ERROR: $message"
    echo
    failed=1
  fi
}

# Validator vs server drift
check_pattern '\bserver validates events\b' \
  'Use "validator validates events", not "server validates events".'

check_pattern '\bserver accepts( the)? event\b' \
  'Use "validator accepts the event", not "server accepts the event".'

check_pattern '\bserver assigns( canonical)? sequence\b' \
  'Use "validator assigns canonical sequence", not "server assigns sequence".'

check_pattern '\bserver is the source of truth\b' \
  'Use "Canonical event history is the source of truth" and "The validator defines what becomes canonical."'

# Canonical authority drift
check_pattern '\bvalidator defines truth\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

check_pattern '\bvalidation defines canonical truth\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

check_pattern '\bvalidation defines truth\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

check_pattern '\bvalidation defines reality\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

check_pattern '\bcontrols what becomes real\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

# Event lifecycle drift
check_pattern '\bevent is appended to canonical event history\b' \
  'Use the canonical phrase: "If accepted, an event becomes canonical and is appended to canonical event history."'

check_pattern '\baccepted events are appended to canonical event history\b' \
  'Use the canonical phrase: "If accepted, an event becomes canonical and is appended to canonical event history."'

# Source of truth drift
check_pattern '\bcanonical event history is truth\b' \
  'Use the canonical phrase: "Canonical event history is the source of truth."'

check_pattern '\bdefines what is true\b' \
  'Prefer the canonical phrase: "Canonical event history is the source of truth."'

# Derived state drift
check_pattern '\bprojection of truth\b' \
  'Use the canonical phrase: "Derived canonical state is a projection of canonical event history. It is not the source of truth."'

check_pattern '\bstate is not stored as truth — it is derived from events\b' \
  'Use the canonical phrase for derived canonical state.'

check_pattern '\bstate is not stored as truth\b' \
  'Use the canonical phrase: "Derived canonical state is a projection of canonical event history. It is not the source of truth." when defining derived state.'

if [[ "$failed" -ne 0 ]]; then
  echo "CrypSA docs gate failed."
  exit 1
fi

echo "CrypSA docs gate passed."
