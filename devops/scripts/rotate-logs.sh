#!/usr/bin/env bash
# Compress and prune application logs.
set -euo pipefail

LOG_DIR="${LOG_DIR:-/var/log/app}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"

find "${LOG_DIR}" -type f -name '*.log' -size +10M -exec gzip -f {} \;
find "${LOG_DIR}" -type f -mtime "+${RETENTION_DAYS}" -delete
echo "log rotation complete in ${LOG_DIR}"
