# BACKUP_AND_RECOVERY.md — WamaCare Backup and Recovery

**Date:** 2026-05-29 | **Status:** DRAFT — Phase 11 will add restore drill results

---

## Backup Policy

| What | How | Where | Frequency |
|------|-----|-------|-----------|
| Database | `pg_dump -F c` (custom format) | `backups/wamacare_<date>/` | Before every phase; weekly in production |
| Filestore | `tar.gz` or `cp -r` | Same backup folder | With every DB backup |
| Config (sanitised) | `cp` with password stripped | Same backup folder | With every DB backup |
| Code / Docs | `git commit && git push` | GitHub | After every phase |
| CSV templates | Part of Git | GitHub | Automatic |

---

## Backup Script (to be created in Phase 11)

Location: `scripts/backup_wamacare.sh`

```bash
#!/bin/bash
# WamaCare Backup Script
TIMESTAMP=$(date +%Y%m%d_%H%M)
BACKUP_DIR="/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/backups/wamacare_${TIMESTAMP}"
DB_NAME="wamacare_local"
FILESTORE_SRC="$HOME/Library/Application Support/Odoo/filestore/${DB_NAME}"

mkdir -p "$BACKUP_DIR"

# Database dump
pg_dump -U odoo -F c "$DB_NAME" -f "${BACKUP_DIR}/${DB_NAME}.dump"

# Filestore
cp -r "$FILESTORE_SRC" "${BACKUP_DIR}/filestore/"

# Manifest (to be created separately)
echo "Backup complete: ${BACKUP_DIR}"
```

---

## Restore Procedure

```bash
BACKUP_DIR="/path/to/backup/wamacare_<timestamp>"
TARGET_DB="wamacare_local"

# 1. Create fresh database
createdb -U odoo "$TARGET_DB"

# 2. Restore database (custom format)
pg_restore -U odoo -d "$TARGET_DB" --disable-triggers "${BACKUP_DIR}/${TARGET_DB}.dump"

# 3. Restore filestore
FILESTORE_DST="$HOME/Library/Application Support/Odoo/filestore/${TARGET_DB}"
mkdir -p "$FILESTORE_DST"
cp -r "${BACKUP_DIR}/filestore/" "$FILESTORE_DST/"

# 4. Start Odoo and validate
```

---

## Original Dump (pre-setup)

| Item | Value |
|------|-------|
| File | `mamacare1.dump.zip` |
| Location | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/mamacare1.dump.zip` |
| Format | ZIP: `dump.sql` (plain SQL) + `filestore/` |
| Date | 2025-12-29 |
| Git status | Excluded (`.gitignore`) |
| Recovery note | Keep a copy outside the project folder for disaster recovery |

---

## Recovery Time Objective (RTO)

| Scenario | Estimated Time |
|---------|---------------|
| Restore from local dump | ~5-10 minutes |
| Restore from GitHub + manual dump import | ~20-30 minutes |
| Full rebuild from scratch + CSV import | ~2-4 hours |

---

## Backup Manifests

All backup manifests are committed to Git under `backups/`.
Binary dump files are NOT committed to Git.

---

*Phase 11 restore drill results will be added to this document.*
