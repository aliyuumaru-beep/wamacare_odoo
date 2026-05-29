#!/bin/bash
# WamaCare Backup Script
# Creates timestamped backup of database + filestore
# Run from any directory.

DB_NAME="wamacare_local"
TIMESTAMP=$(date +%Y%m%d_%H%M)
WROOT="/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare"
BACKUP_DIR="$WROOT/backups/wamacare_${TIMESTAMP}"
FILESTORE_SRC="$HOME/Library/Application Support/Odoo/filestore/${DB_NAME}"

mkdir -p "$BACKUP_DIR"

echo "[$(date)] Starting WamaCare backup..."

# Database dump (custom format — faster restore, handles FK constraints)
pg_dump -U odoo -F c "$DB_NAME" -f "${BACKUP_DIR}/${DB_NAME}.dump"
if [ $? -ne 0 ]; then
  echo "ERROR: Database dump failed"
  exit 1
fi

# Filestore
if [ -d "$FILESTORE_SRC" ]; then
  cp -r "$FILESTORE_SRC" "${BACKUP_DIR}/filestore/"
  echo "Filestore: $(find "${BACKUP_DIR}/filestore" -type f | wc -l) files"
else
  echo "WARNING: Filestore not found at $FILESTORE_SRC"
fi

# Sanitised config (no passwords)
grep -v "password\|passwd\|secret\|token" "$WROOT/wamacare.conf" > "${BACKUP_DIR}/wamacare.conf.sanitised" 2>/dev/null

DUMP_SIZE=$(du -sh "${BACKUP_DIR}/${DB_NAME}.dump" | cut -f1)
echo "[$(date)] Backup complete: $BACKUP_DIR"
echo "  DB dump size: $DUMP_SIZE"
echo ""
echo "Update backups/BACKUP_MANIFEST.md and commit to Git."
