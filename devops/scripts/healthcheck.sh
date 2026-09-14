#!/usr/bin/env bash
# Poll a health endpoint until healthy or timeout.
set -euo pipefail

URL="${1:-http://localhost:8080/healthz}"
TIMEOUT="${2:-60}"
deadline=$((SECONDS + TIMEOUT))

until curl -fsS "${URL}" >/dev/null 2>&1; do
  if (( SECONDS >= deadline )); then
    echo "healthcheck timed out after ${TIMEOUT}s" >&2
    exit 1
  fi
  sleep 2
done
echo "healthy: ${URL}"
