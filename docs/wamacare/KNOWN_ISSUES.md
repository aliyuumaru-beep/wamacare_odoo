# KNOWN_ISSUES.md — WamaCare Open Issues

**Project:** WamaCare | **Updated:** 2026-05-29 (Phase 8 complete)

---

## Open Issues

| # | Issue | Phase | Priority | Status |
|---|-------|-------|---------|--------|
| 6 | `Untitled.rtf` junk file in root — kept pending operator decision | — | LOW | OPEN |
| 9 | No GitHub CI/CD configured yet | Phase 12 | LOW | OPEN |
| 10 | No offsite backup configured (cloud sync) | Phase 11 | LOW | OPEN |
| 11 | Admin password still `admin/admin` — must be changed before non-local use | Manual | HIGH | OPEN |
| 15 | Absolute paths in scripts/conf (`/Users/mac/...`) — not portable to other machines | Phase 12 | MEDIUM | OPEN |
| 17 | `testing/PHASE_10_VALIDATION_REPORT.md` not yet created | Phase 10 | MEDIUM | OPEN |
| 18 | `RESTORE_DRILL.md` not yet created | Phase 11 | MEDIUM | OPEN |
| 26 | Nigeria chart template not applied via UI — taxes available but fiscal COA links pending | Manual | MEDIUM | OPEN |
| 27 | Department managers not yet assigned in Odoo UI | Manual | LOW | OPEN |
| 28 | Bank account not configured for WamaCare | Manual | LOW | OPEN |
| 29 | Expense demo records (mamacare_expenses.csv) not yet imported | Phase 7 | LOW | OPEN |
| 30 | wamacare_products.csv not imported (deferred — overlaps mamacare_products.csv) | Phase 7 | LOW | OPEN |

---

## Resolved Issues

| # | Issue | Resolved | Notes |
|---|-------|---------|-------|
| 1 | Database not yet restored/created | Phase 5 — 2026-05-29 | Fresh Community DB created (`wamacare_local`) |
| 2 | Odoo version in dump not confirmed | Phase 5 — 2026-05-29 | Dump was Odoo Enterprise (Ubuntu); new DB is 17.0 Community |
| 3 | `wamacare.conf` not created | Phase 4 — 2026-05-29 | Created at project root, port 8070, excluded from Git |
| 4 | No custom addons detected | Phase 6 — 2026-05-29 | Confirmed not needed at this stage |
| 5 | `mamacare1.dump.zip` Enterprise compatibility | Phase 5 — 2026-05-29 | Documented in DEC-007; fresh Community DB used instead |
| 7 | `projects.csv` / `mamacare_projects.csv` overlap risk | Phase 7 — 2026-05-29 | Import script used only `mamacare_projects.csv`; deduplication built in |
| 8 | `hr_employees.csv` manager external ID dependencies | Phase 7 — 2026-05-29 | Imported without manager refs; managers to be set in UI |
| 12 | No backup script created | Phase 4 — 2026-05-29 | `scripts/backup_wamacare.sh` created |
| 13 | CLAUDE.md active phase stale | Compliance review 2026-05-29 | Corrected to Phase 7, then Phase 8 |
| 14 | `PASSWORD = "admin"` hardcoded in import script | Phase 8 — 2026-05-29 | Changed to env var `WAMACARE_ADMIN_PASS` with default |
| 16 | `FUNCTIONAL_CONFIGURATION.md` missing | Phase 8 — 2026-05-29 | Created with full Phase 8 config details |
| 19 | `wamacare.conf.sanitised` not committed | Compliance 2026-05-29 | Committed to backup folder |
| 20 | Company name "My Company" | Phase 8 — 2026-05-29 | Renamed to "WamaCare (Tiko CBO)", Abuja FCT |
| 21 | No Nigeria chart of accounts | Phase 8 — 2026-05-29 | l10n_ng installed; 21 NGO accounts created (4xxx income, 5xxx expense, 2xxx liabilities) |
| 22 | No purchase approval threshold | Phase 8 — 2026-05-29 | Two-step approval at ₦200,000 threshold |
| 23 | Analytic accounting not enabled | Phase 8 — 2026-05-29 | Enabled via res.config.settings; all 13 accounts linked to projects |
| 24 | Assets not imported | Phase 8 — 2026-05-29 | Ambulance ₦35M, Ultrasound ₦12M, Laptop ₦850K in maintenance.equipment |
| 25 | LPO not imported | Phase 8 — 2026-05-29 | LPO-001 Health Supplies ₦2.5M imported |

---

## Issue Template

When adding a new issue:
```
| N | Short description | Phase expected | Priority (HIGH/MEDIUM/LOW) | OPEN/RESOLVED |
```
