# Backup Registry — WamaCare

| Backup | Date | Type | Status |
|--------|------|------|--------|
| `wamacare_20260529_0747/` | 2026-05-29 07:47 | Pre-setup source files | COMPLETE |
| `wamacare_20260529_0839/` | 2026-05-29 08:39 | Post Phase 7 — DB + filestore + config | COMPLETE |
| `wamacare_20260529_0948/` | 2026-05-29 09:48 | Post Phase 8 — NGN currency, COA, users, purchase approval, assets, LPO | COMPLETE |
| `wamacare_phase11_20260529_1441/` | 2026-05-29 14:41 | Phase 11 restore drill — 5MB dump, 423 files. Drill PASS, RTO 45s | COMPLETE |
| `wamacare_tier1_20260529_2020/` | 2026-05-29 20:20 | After Tier 1 — bank, fiscal year, budgets (₦33M), equipment categories | COMPLETE |
| `wamacare_tier0_20260530_1116/` | 2026-05-30 11:16 | After Tier 0 — BEN-006 active, user roles fixed, beneficiary data protected | COMPLETE |
| `wamacare_proctest_20260530_1204/` | 2026-05-30 12:04 | After procurement lifecycle test — P00002, BILL, PWBNK created | COMPLETE |

---

**Note:** Binary dump files (`*.dump`, `*.zip`, `*.sql`) are NOT stored in Git.
Only this manifest and per-backup `BACKUP_MANIFEST.md` files are tracked.

The original database dump (`mamacare1.dump.zip`) is located at:
`/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/mamacare1.dump.zip`

Keep a copy outside the Git repository for disaster recovery.
