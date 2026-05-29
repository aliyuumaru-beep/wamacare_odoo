# RESTORE_DRILL.md — WamaCare Backup and Restore Drill

**Phase:** 11 | **Date:** 2026-05-29 | **Status:** COMPLETE — PASS

---

## Summary

| Item | Value |
|------|-------|
| Source database | `wamacare_local` |
| Restore target | `wamacare_restore_test` |
| Backup format | `pg_dump -F c` (PostgreSQL custom format) |
| Backup size | 5.0 MB (dump) + 423 filestore files |
| Restore time | **45 seconds** |
| Modules on restore | 78 (0 errors, 0 pending) |
| Record parity | **PASS — all counts match source** |
| FamOil isolation on restore | **PASS — no FamOil references** |
| Odoo startup on restore | **PASS — 78 modules loaded cleanly** |
| Overall result | **PASS** |

---

## Drill Procedure

### Step 1 — Create Backup

```bash
TIMESTAMP=$(date +%Y%m%d_%H%M)
BACKUP_DIR="backups/wamacare_phase11_${TIMESTAMP}"
mkdir -p "$BACKUP_DIR"

# Database
pg_dump -U odoo -F c wamacare_local -f "${BACKUP_DIR}/wamacare_local.dump"

# Filestore
cp -r "$HOME/Library/Application Support/Odoo/filestore/wamacare_local/." \
  "${BACKUP_DIR}/filestore/"

# Config (sanitised)
grep -v "password\|passwd" wamacare.conf > "${BACKUP_DIR}/wamacare.conf.sanitised"
```

### Step 2 — Restore to Test Database

```bash
BACKUP_DIR="backups/wamacare_phase11_20260529_1441"
RESTORE_DB="wamacare_restore_test"

# Create target
createdb -U odoo "$RESTORE_DB"

# Restore database
pg_restore -U odoo -d "$RESTORE_DB" --disable-triggers \
  "${BACKUP_DIR}/wamacare_local.dump"

# Restore filestore
mkdir -p "$HOME/Library/Application Support/Odoo/filestore/${RESTORE_DB}"
cp -r "${BACKUP_DIR}/filestore/." \
  "$HOME/Library/Application Support/Odoo/filestore/${RESTORE_DB}/"
```

### Step 3 — Start Odoo Against Restored DB

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate && \
python /Users/mac/odoo17/odoo/odoo-bin \
  -d wamacare_restore_test -r odoo \
  --addons-path="/Users/mac/odoo17/odoo/odoo/addons,/path/to/WamaCare/custom_addons" \
  --http-port=8071 \
  --stop-after-init
```

### Step 4 — Clean Up

```bash
dropdb -U odoo wamacare_restore_test
rm -rf "$HOME/Library/Application Support/Odoo/filestore/wamacare_restore_test"
```

---

## Validation Results

### Record Parity (source vs restore)

| Entity | Source | Restored | Match |
|--------|--------|----------|-------|
| Modules installed | 78 | 78 | ✓ |
| Partners (total) | 49 | 49 | ✓ |
| Projects | 5 | 5 | ✓ |
| Employees (active) | 10 | 10 | ✓ |
| Departments | 6 | 6 | ✓ |
| Analytic accounts | 13 | 13 | ✓ |
| COA accounts | 70 | 70 | ✓ |
| Equipment | 3 | 3 | ✓ |
| Purchase orders | 1 | 1 | ✓ |
| Products | 21 | 21 | ✓ |

### Configuration Checks

| Check | Result |
|-------|--------|
| Company name: WamaCare (Tiko CBO) | PASS |
| Currency: NGN | PASS |
| 5 departments with managers | PASS |
| 4 NGO accounts (4000, 5000, 2100, 3000) present | PASS |
| No FamOil references in company records | PASS |

### Module Load

| Check | Result |
|-------|--------|
| Odoo starts against restored DB | PASS |
| 78 modules loaded | PASS |
| 0 modules pending/errored | PASS |
| Registry loaded in 5 seconds | PASS |

---

## Recovery Time Objective (RTO)

| Scenario | Time |
|---------|------|
| `pg_restore` (45 seconds) + filestore copy | **~1 minute** |
| Full restart of Odoo service | + ~15 seconds |
| **Total estimated RTO** | **< 2 minutes** |

---

## Backup Location

| Backup | Path | Size |
|--------|------|------|
| Phase 11 drill backup | `backups/wamacare_phase11_20260529_1441/` | 5 MB + 423 files |

> Binary dump files are excluded from Git. Keep a copy of `backups/wamacare_phase11_20260529_1441/` outside the repository for disaster recovery.

---

## How to Run a Future Restore Drill

1. Run `scripts/backup_wamacare.sh` to create a fresh backup
2. Follow Step 2–4 above using the new backup folder
3. Update this document with results and date
4. Drop the test database when done

---

*Phase 11 restore drill completed 2026-05-29. wamacare_restore_test dropped after validation.*
