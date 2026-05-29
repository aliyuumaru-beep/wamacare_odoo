# KNOWN_ISSUES.md — WamaCare Open Issues

**Project:** WamaCare | **Updated:** 2026-05-29 (Compliance Review)

---

## Open Issues

| # | Issue | Phase | Priority | Status |
|---|-------|-------|---------|--------|
| 6 | `Untitled.rtf` junk file in root — kept pending operator decision | — | LOW | OPEN |
| 9 | No GitHub CI/CD configured yet | Phase 12 | LOW | OPEN |
| 10 | No offsite backup configured (cloud sync) | Phase 11 | LOW | OPEN |
| 11 | Beneficiary data privacy — role-based access not yet configured in Odoo UI | Phase 8 | HIGH | OPEN |
| 13 | CLAUDE.md active phase description was stale (Phase 5 shown, Phase 7 complete) | — | LOW | FIXED 2026-05-29 |
| 14 | `PASSWORD = "admin"` hardcoded in `import_wamacare_data.py` | — | LOW | OPEN |
| 15 | `addons_path` in scripts and conf references absolute paths (`/Users/mac/...`) — not portable | Phase 12 | MEDIUM | OPEN |
| 16 | `FUNCTIONAL_CONFIGURATION.md` referenced in README but not yet created | Phase 8 | MEDIUM | OPEN |
| 17 | `testing/PHASE_10_VALIDATION_REPORT.md` not yet created | Phase 10 | MEDIUM | OPEN |
| 18 | `RESTORE_DRILL.md` not yet created | Phase 11 | MEDIUM | OPEN |
| 19 | `wamacare.conf.sanitised` in backups folder not yet committed | — | LOW | OPEN |
| 20 | Company name "My Company" used in OdooBot/portal references — needs full config | Phase 8 | MEDIUM | OPEN |
| 21 | No chart of accounts configured for Nigeria (NGN, FIRS structure) | Phase 8 | HIGH | OPEN |
| 22 | No purchase approval workflow threshold configured | Phase 8 | MEDIUM | OPEN |
| 23 | Analytic accounting not enabled in Odoo Accounting settings (required for analytic tags on bills) | Phase 8 | HIGH | OPEN |
| 24 | Assets (Ambulance, Ultrasound) not yet imported to `maintenance.equipment` | Phase 7 | MEDIUM | OPEN |
| 25 | LPO demo data and expense demo records not yet imported | Phase 7 | LOW | OPEN |

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
| 8 | `hr_employees.csv` manager external ID dependencies | Phase 7 — 2026-05-29 | Import script imported employees without manager refs; managers to be set in Phase 8 |
| 12 | No backup script created | Phase 4 — 2026-05-29 | `scripts/backup_wamacare.sh` created |

---

## Issue Template

When adding a new issue:
```
| N | Short description | Phase expected | Priority (HIGH/MEDIUM/LOW) | OPEN/RESOLVED |
```
