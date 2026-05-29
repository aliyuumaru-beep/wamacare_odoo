# BACKUP_MANIFEST.md — WamaCare Post-Setup Backup

**Backup date:** 2026-05-29 08:39  
**Phase:** Post Phase 7 — first backup with real data  
**Type:** Full database + filestore

---

## What Was Backed Up

| Item | Details |
|------|---------|
| Database dump | `wamacare_local.dump` (4 MB, custom format) |
| Filestore | `filestore/` (~400 files) |
| Config (sanitised) | `wamacare.conf.sanitised` |

---

## Database State at Backup

| Entity | Count |
|--------|-------|
| Modules installed | 63 (Community) |
| Analytic accounts | 13 |
| HR departments | 5 |
| Projects/programmes | 5 |
| Beneficiaries | 13 |
| Vendors | 17 |
| Employees | 4 |
| Products/services | 15 |
| Company | WamaCare (Tiko CBO) — Nigeria |

---

## Restore Instructions

```bash
createdb -U odoo wamacare_local
pg_restore -U odoo -d wamacare_local --disable-triggers backups/wamacare_20260529_0839/wamacare_local.dump
cp -r backups/wamacare_20260529_0839/filestore/ \
  "$HOME/Library/Application Support/Odoo/filestore/wamacare_local/"
```

---

## Binary Files NOT in Git

- `wamacare_local.dump` — excluded by .gitignore
- `filestore/` — excluded by .gitignore

*Store this backup folder in a secure location outside the Git repository.*
