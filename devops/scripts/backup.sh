#!/usr/bin/env bash
# Postgres backup with retention.
set -euo pipefail

: "${DATABASE_URL:?DATABASE_URL is required}"
DEST="${BACKUP_DIR:-/var/backups}"
STAMP="$(date +%Y%m%dT%H%M%S)"
KEEP_DAYS="${KEEP_DAYS:-14}"

mkdir -p "${DEST}"
pg_dump "${DATABASE_URL}" | gzip > "${DEST}/db-${STAMP}.sql.gz"
find "${DEST}" -name 'db-*.sql.gz' -mtime "+${KEEP_DAYS}" -delete
echo "backup written to ${DEST}/db-${STAMP}.sql.gz"
