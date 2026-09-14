#!/usr/bin/env bash
# Rolling deploy of an image tag to Kubernetes.
set -euo pipefail

IMAGE_TAG="${1:?usage: deploy.sh <image-tag>}"
NAMESPACE="${NAMESPACE:-default}"
DEPLOYMENT="${DEPLOYMENT:-api}"

echo "==> Deploying ${IMAGE_TAG} to ${NAMESPACE}/${DEPLOYMENT}"
kubectl -n "${NAMESPACE}" set image \
  "deployment/${DEPLOYMENT}" "api=ghcr.io/example/api:${IMAGE_TAG}"
kubectl -n "${NAMESPACE}" rollout status \
  "deployment/${DEPLOYMENT}" --timeout=180s
echo "==> Deploy complete"
