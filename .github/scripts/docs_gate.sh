#!/usr/bin/env bash
set -euo pipefail

BASE_REF="${1:-origin/main}"

# Get unified=0 diff so only changed lines are shown with minimal context.
diff_output="$(git diff --unified=0 "$BASE_REF"...HEAD -- '*.md' '*.MD' || true)"

if [[ -z "$diff_output" ]]; then
  echo "No markdown changes detected."
  exit 0
fi

# Collect only added lines from markdown diffs.
# Ignore file headers (+++) and diff hunk markers.
added_lines="$(printf '%s\n' "$diff_output" | grep -E '^\+' | grep -vE '^\+\+\+' || true)"

if [[ -z "$added_lines" ]]; then
  echo "No added markdown lines to check."
  exit 0
fi

echo "Checking added markdown lines only..."
echo

failed=0

check_pattern() {
  local pattern="$1"
  local message="$2"

  local matches
  matches="$(printf '%s\n' "$added_lines" | grep -nEi "$pattern" || true)"

  if [[ -n "$matches" ]]; then
    echo "$matches"
    echo
    echo "ERROR: $message"
    echo
    failed=1
  fi
}

# ------------------------------
# Validator vs server drift
# ------------------------------
check_pattern '\bserver validates events\b' \
  'Use "validator validates events", not "server validates events".'

check_pattern '\bserver accepts( the)? event\b' \
  'Use "validator accepts the event", not "server accepts the event".'

check_pattern '\bserver assigns( canonical)? sequence\b' \
  'Use "validator assigns canonical sequence", not "server assigns sequence".'

check_pattern '\bserver is the source of truth\b' \
  'Use "Canonical event history is the source of truth" and "The validator defines what becomes canonical."'

# ------------------------------
# Canonical authority drift
# ------------------------------
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

check_pattern '\bdefines what becomes real\b' \
  'Use the canonical phrase: "The validator defines what becomes canonical."'

# ------------------------------
# Event lifecycle drift
# ------------------------------
check_pattern '\bevent is appended to canonical event history\b' \
  'Use the canonical phrase: "If accepted, an event becomes canonical and is appended to canonical event history."'

check_pattern '\baccepted events are appended to canonical event history\b' \
  'Use the canonical phrase: "If accepted, an event becomes canonical and is appended to canonical event history."'

check_pattern '\baccepted events form canonical event history\b' \
  'Prefer the canonical lifecycle phrasing when describing acceptance.'

# ------------------------------
# Source of truth drift
# ------------------------------
check_pattern '\bcanonical event history is truth\b' \
  'Use the canonical phrase: "Canonical event history is the source of truth."'

check_pattern '\bdefines what is true\b' \
  'Prefer the canonical phrase: "Canonical event history is the source of truth."'

# ------------------------------
# Derived state drift
# ------------------------------
check_pattern '\bprojection of truth\b' \
  'Use the canonical phrase: "Derived canonical state is a projection of canonical event history. It is not the source of truth."'

check_pattern '\bstate is not stored as truth — it is derived from events\b' \
  'Use the canonical derived-state phrase instead.'

check_pattern '\bstate is not stored as truth\b' \
  'When defining derived state, use: "Derived canonical state is a projection of canonical event history. It is not the source of truth."'

# ------------------------------
# Optional soft bans for likely drift
# ------------------------------
check_pattern '\bclient\b' \
  'Use "observer" unless this is specifically a networking discussion.'

if [[ "$failed" -ne 0 ]]; then
  echo "CrypSA docs gate failed."
  exit 1
fi

echo "CrypSA docs gate passed."
