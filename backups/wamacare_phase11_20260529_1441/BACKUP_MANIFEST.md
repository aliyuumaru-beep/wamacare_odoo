# BACKUP_MANIFEST.md — Phase 11 Drill Backup

**Date:** 2026-05-29 14:41 | **Type:** Phase 11 restore drill source backup

| Item | Value |
|------|-------|
| DB dump | `wamacare_local.dump` (5 MB, custom format) |
| Filestore | 423 files |
| Config | `wamacare.conf.sanitised` |

## Database State at Backup
- 78 modules installed
- Currency: NGN, Company: WamaCare (Tiko CBO), Abuja FCT
- 70 COA accounts, 13 analytic accounts
- 5 projects, 13 beneficiaries, 17 vendors
- 10 employees, 6 departments, 3 assets
- 1 LPO (₦2,500,000), 21 products, 5 users

## Restore Drill Result
- Restored to `wamacare_restore_test` — **PASS**
- 78 modules loaded, 0 errors
- All record counts matched
- RTO: ~45 seconds
- Test DB dropped after validation

## Restore Command
```bash
createdb -U odoo wamacare_restore_test
pg_restore -U odoo -d wamacare_restore_test --disable-triggers \
  backups/wamacare_phase11_20260529_1441/wamacare_local.dump
mkdir -p "$HOME/Library/Application Support/Odoo/filestore/wamacare_restore_test"
cp -r backups/wamacare_phase11_20260529_1441/filestore/. \
  "$HOME/Library/Application Support/Odoo/filestore/wamacare_restore_test/"
```
