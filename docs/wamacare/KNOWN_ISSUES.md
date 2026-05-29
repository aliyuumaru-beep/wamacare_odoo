# KNOWN_ISSUES.md — WamaCare Open Issues

**Project:** WamaCare | **Updated:** 2026-05-29

---

## Open Issues

| # | Issue | Phase | Priority | Status |
|---|-------|-------|---------|--------|
| 1 | Database not yet restored — `wamacare_local` does not exist | Phase 5 | HIGH | OPEN |
| 2 | Odoo version of dump not confirmed (expected 17.0) | Phase 5 | HIGH | OPEN |
| 3 | `wamacare.conf` config file not yet created | Phase 4 | MEDIUM | OPEN |
| 4 | No custom addons detected — post-restore check needed | Phase 6 | MEDIUM | OPEN |
| 5 | Module checklist XLSX (`Odoo_module_checklist.xlsx`) not parsed | Phase 6 | LOW | OPEN |
| 6 | `Untitled.rtf` junk file in root — kept pending operator decision | — | LOW | OPEN |
| 7 | `projects.csv` and `mamacare_projects.csv` may have overlapping data | Phase 7 | MEDIUM | OPEN |
| 8 | `hr_employees.csv` references manager external IDs that must pre-exist | Phase 7 | MEDIUM | OPEN |
| 9 | No GitHub CI/CD configured yet | Phase 12 | LOW | OPEN |
| 10 | No offsite backup configured | Phase 11 | LOW | OPEN |
| 11 | Beneficiary data in dump may be sensitive — access control needed | Phase 8 | HIGH | OPEN |
| 12 | No backup script created yet | Phase 11 | MEDIUM | OPEN |

---

## Resolved Issues

*(None yet — project started 2026-05-29)*

---

## Issue Template

When adding a new issue:
```
| N | Short description | Phase expected | Priority (HIGH/MEDIUM/LOW) | OPEN/RESOLVED |
```

When resolving an issue, move it to the Resolved table and add resolution date and notes.
