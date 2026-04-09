#!/usr/bin/env bash
set -euo pipefail

BASE_REF="${1:-origin/main}"

echo "🧠 CrypSA Docs Gate (v3.2)"
echo

diff_output="$(git diff --unified=0 "$BASE_REF"...HEAD -- '*.md' '*.MD' || true)"

if [[ -z "$diff_output" ]]; then
  echo "No markdown changes detected."
  exit 0
fi

failed=0
current_file=""
line_number=0
in_code_block=0

print_error() {
  local file="$1"
  local line="$2"
  local content="$3"
  local message="$4"
  local suggestion="$5"

  echo "❌ $file:$line"
  echo "   Offending line:"
  echo "   $content"
  echo
  echo "   Reason:"
  echo "   $message"
  echo
  echo "   Suggested fix:"
  echo "   $suggestion"
  echo
}

check_line() {
  local file="$1"
  local line="$2"
  local content="$3"

  # ------------------------------
  # Validator vs server drift
  # ------------------------------
  if [[ "$content" =~ \bserver\ validates\ events\b ]]; then
    print_error "$file" "$line" "$content" \
      'Use "validator" for authority role, not "server".' \
      'validator validates events'
    failed=1
  fi

  if [[ "$content" =~ \bserver\ accepts(\ the)?\ event\b ]]; then
    print_error "$file" "$line" "$content" \
      'Use "validator" for event acceptance, not "server".' \
      'validator accepts the event'
    failed=1
  fi

  if [[ "$content" =~ \bserver\ assigns(\ canonical)?\ sequence\b ]]; then
    print_error "$file" "$line" "$content" \
      'Use "validator" for canonical sequencing, not "server".' \
      'validator assigns canonical sequence'
    failed=1
  fi

  if [[ "$content" =~ \bserver\ is\ the\ source\ of\ truth\b ]]; then
    print_error "$file" "$line" "$content" \
      'Canonical truth is defined by validator authority and canonical event history, not "server".' \
      'Canonical event history is the source of truth.'
    failed=1
  fi

  # ------------------------------
  # Canonical authority drift
  # ------------------------------
  if [[ "$content" =~ validator\ defines\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical authority phrase exactly.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  if [[ "$content" =~ validation\ defines\ canonical\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the validator as the actor, not validation as the process.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  if [[ "$content" =~ validation\ defines\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the validator as the actor, not validation as the process.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  if [[ "$content" =~ validation\ defines\ reality ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical authority phrase exactly.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  if [[ "$content" =~ controls\ what\ becomes\ real ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical authority phrase exactly.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  if [[ "$content" =~ defines\ what\ becomes\ real ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical authority phrase exactly.' \
      'The validator defines what becomes canonical.'
    failed=1
  fi

  # ------------------------------
  # Event lifecycle drift
  # ------------------------------
  if [[ "$content" =~ accepted\ \-\>\ becomes\ canonical$ ]]; then
    print_error "$file" "$line" "$content" \
      'Use the full canonical lifecycle phrase when stating the acceptance rule.' \
      'If accepted, an event becomes canonical and is appended to canonical event history.'
    failed=1
  fi

  if [[ "$content" =~ event\ becomes\ canonical$ ]]; then
    print_error "$file" "$line" "$content" \
      'Use the full canonical lifecycle phrase when stating the acceptance rule.' \
      'If accepted, an event becomes canonical and is appended to canonical event history.'
    failed=1
  fi

  # ------------------------------
  # Source of truth drift
  # ------------------------------
  if [[ "$content" =~ canonical\ event\ history\ is\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical source-of-truth phrase exactly.' \
      'Canonical event history is the source of truth.'
    failed=1
  fi

  if [[ "$content" =~ defines\ what\ is\ true ]]; then
    print_error "$file" "$line" "$content" \
      'Prefer the canonical source-of-truth phrase.' \
      'Canonical event history is the source of truth.'
    failed=1
  fi

  # ------------------------------
  # Derived state drift
  # ------------------------------
  if [[ "$content" =~ projection\ of\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical derived-state phrase exactly.' \
      'Derived canonical state is a projection of canonical event history. It is not the source of truth.'
    failed=1
  fi

  if [[ "$content" =~ state\ is\ not\ stored\ as\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical derived-state phrase instead of a partial restatement.' \
      'Derived canonical state is a projection of canonical event history. It is not the source of truth.'
    failed=1
  fi
}

while IFS= read -r line; do
  if [[ "$line" =~ ^diff\ --git ]]; then
    current_file="$(echo "$line" | awk '{print $4}' | sed 's|b/||')"
    continue
  fi

  if [[ "$line" =~ ^@@ ]]; then
    line_number="$(echo "$line" | sed -E 's/^@@ .* \+([0-9]+).*/\1/')"
    continue
  fi

  if [[ "$line" =~ ^\+ && ! "$line" =~ ^\+\+\+ ]]; then
    content="${line:1}"

    if [[ "$content" =~ ^\`\`\` ]]; then
      if [[ "$in_code_block" -eq 0 ]]; then
        in_code_block=1
      else
        in_code_block=0
      fi
      ((line_number++))
      continue
    fi

    if [[ "$in_code_block" -eq 0 ]]; then
      check_line "$current_file" "$line_number" "$content"
    fi

    ((line_number++))
  fi
done <<< "$diff_output"

if [[ "$failed" -ne 0 ]]; then
  echo "❌ CrypSA docs gate failed."
  echo
  echo "Review the suggested fixes above and update the changed documentation."
  exit 1
fi

echo "✅ CrypSA docs gate passed."
