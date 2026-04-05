#!/usr/bin/env bash
set -euo pipefail

BASE_REF="${1:-origin/main}"

echo "🧠 CrypSA Docs Gate (v3)"
echo

# Get diff with file names and line numbers
diff_output="$(git diff --unified=0 "$BASE_REF"...HEAD -- '*.md' '*.MD' || true)"

if [[ -z "$diff_output" ]]; then
  echo "No markdown changes detected."
  exit 0
fi

failed=0

current_file=""

print_error() {
  local file="$1"
  local line="$2"
  local content="$3"
  local message="$4"

  echo "❌ $file:$line"
  echo "   $content"
  echo
  echo "   → $message"
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
      'Use "validator validates events", not "server validates events".'
    failed=1
  fi

  if [[ "$content" =~ \bserver\ accepts ]]; then
    print_error "$file" "$line" "$content" \
      'Use "validator accepts the event", not "server accepts the event".'
    failed=1
  fi

  if [[ "$content" =~ \bserver\ assigns ]]; then
    print_error "$file" "$line" "$content" \
      'Use "validator assigns canonical sequence", not "server assigns sequence".'
    failed=1
  fi

  # ------------------------------
  # Canonical authority drift
  # ------------------------------
  if [[ "$content" =~ validator\ defines\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use: "The validator defines what becomes canonical."'
    failed=1
  fi

  if [[ "$content" =~ validation\ defines ]]; then
    print_error "$file" "$line" "$content" \
      'Use: "The validator defines what becomes canonical."'
    failed=1
  fi

  if [[ "$content" =~ becomes\ real ]]; then
    print_error "$file" "$line" "$content" \
      'Use: "The validator defines what becomes canonical."'
    failed=1
  fi

  # ------------------------------
  # Event lifecycle drift
  # ------------------------------
  if [[ "$content" =~ appended\ to\ canonical\ event\ history ]]; then
    if [[ ! "$content" =~ becomes\ canonical ]]; then
      print_error "$file" "$line" "$content" \
        'Use: "If accepted, an event becomes canonical and is appended to canonical event history."'
      failed=1
    fi
  fi

  # ------------------------------
  # Source of truth drift
  # ------------------------------
  if [[ "$content" =~ canonical\ event\ history\ is\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use: "Canonical event history is the source of truth."'
    failed=1
  fi

  # ------------------------------
  # Derived state drift
  # ------------------------------
  if [[ "$content" =~ projection\ of\ truth ]]; then
    print_error "$file" "$line" "$content" \
      'Use the canonical derived state phrase.'
    failed=1
  fi
}

line_number=0

while IFS= read -r line; do
  # Track file names
  if [[ "$line" =~ ^diff\ --git ]]; then
    current_file="$(echo "$line" | awk '{print $4}' | sed 's|b/||')"
    continue
  fi

  # Track line numbers
  if [[ "$line" =~ ^@@ ]]; then
    line_number="$(echo "$line" | sed -E 's/^@@ .* \+([0-9]+).*/\1/')"
    continue
  fi

  # Only check added lines
  if [[ "$line" =~ ^\+ && ! "$line" =~ ^\+\+\+ ]]; then
    content="${line:1}"

    check_line "$current_file" "$line_number" "$content"

    ((line_number++))
  fi

done <<< "$diff_output"

if [[ "$failed" -ne 0 ]]; then
  echo "❌ CrypSA docs gate failed."
  exit 1
fi

echo "✅ CrypSA docs gate passed."
