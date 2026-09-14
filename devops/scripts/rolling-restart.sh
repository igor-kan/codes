#!/usr/bin/env bash
# Zero-downtime restart of all deployments in a namespace.
set -euo pipefail

NAMESPACE="${1:-default}"
for deploy in $(kubectl -n "${NAMESPACE}" get deploy -o name); do
  echo "restarting ${deploy}"
  kubectl -n "${NAMESPACE}" rollout restart "${deploy}"
  kubectl -n "${NAMESPACE}" rollout status "${deploy}" --timeout=180s
done
