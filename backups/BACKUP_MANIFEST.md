# Backup Registry — WamaCare

| Backup | Date | Type | Status |
|--------|------|------|--------|
| `wamacare_20260529_0747/` | 2026-05-29 07:47 | Pre-setup source files | COMPLETE |
| `wamacare_20260529_0839/` | 2026-05-29 08:39 | Post Phase 7 — DB + filestore + config | COMPLETE |
| `wamacare_20260529_0948/` | 2026-05-29 09:48 | Post Phase 8 — NGN currency, COA, users, purchase approval, assets, LPO | COMPLETE |
| `wamacare_phase11_20260529_1441/` | 2026-05-29 14:41 | Phase 11 restore drill — 5MB dump, 423 files. Drill PASS, RTO 45s | COMPLETE |

---

**Note:** Binary dump files (`*.dump`, `*.zip`, `*.sql`) are NOT stored in Git.
Only this manifest and per-backup `BACKUP_MANIFEST.md` files are tracked.

The original database dump (`mamacare1.dump.zip`) is located at:
`/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/mamacare1.dump.zip`

Keep a copy outside the Git repository for disaster recovery.
