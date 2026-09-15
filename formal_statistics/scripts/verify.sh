#!/usr/bin/env bash
# ==============================================================================
# Verify the Formal Statistics Lean 4 library (Kutner Ch. 1-2).
#
# Requires: elan/lake and network access on the first run (to fetch Mathlib).
# ==============================================================================
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v lake >/dev/null 2>&1; then
  echo "lake not found; install Lean 4 via elan (https://leanprover.github.io/lean4/doc/setup.html)" >&2
  exit 1
fi

echo "==> Fetching prebuilt Mathlib oleans (first run only)..."
if [ ! -d ".lake/packages/mathlib" ]; then
  lake exe cache get || echo "(cache fetch skipped; will compile from source)"
fi

echo "==> Building FormalStatistics..."
lake build

echo "==> Checking for unfinished proofs..."
if grep -rn --include='*.lean' -E '\b(sorry|admit)\b' FormalStatistics FormalStatistics.lean; then
  echo "ERROR: found sorry/admit" >&2
  exit 1
fi

echo "==> All formal statistics modules verified."
