# BACKUP_MANIFEST.md — Post Phase 8 Backup

**Date:** 2026-05-29 09:48 | **Type:** Post-Phase 8 functional configuration

| Item | Value |
|------|-------|
| DB dump | `wamacare_local.dump` (4 MB, custom format) |
| Filestore | ~404 files |
| Config | `wamacare.conf.sanitised` |

## Database State
- Modules: 65 (+ l10n_ng, base_vat)
- Currency: NGN (₦)
- Company: WamaCare (Tiko CBO), Abuja FCT
- COA: 68 accounts (21 NGO-specific)
- Projects: 5 (all linked to analytic accounts)
- Analytic accounts: 13
- Users: 5 (admin, aliyu.umaru, finance.officer, field.officer, hr.officer)
- Equipment: 3 (Ambulance, Ultrasound, Laptop)
- Purchase orders: 1 (LPO-001)
- Vendors: 17, Beneficiaries: 13, Employees: 4

## Restore
```bash
createdb -U odoo wamacare_local
pg_restore -U odoo -d wamacare_local --disable-triggers backups/wamacare_20260529_0948/wamacare_local.dump
cp -r backups/wamacare_20260529_0948/filestore/ "$HOME/Library/Application Support/Odoo/filestore/wamacare_local/"
```
