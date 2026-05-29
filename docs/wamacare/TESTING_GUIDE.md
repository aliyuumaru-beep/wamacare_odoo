# TESTING_GUIDE.md — WamaCare Testing Guide

**Date:** 2026-05-29 | **Status:** DRAFT

---

## Testing Phases

| Phase | Test Type | When |
|-------|----------|------|
| Phase 5 | Database restore validation | After restore |
| Phase 6 | Module load validation | After module install |
| Phase 7 | Import validation | After data import |
| Phase 8 | Functional workflow smoke tests | After configuration |
| Phase 10 | Full validation report | Before go-live |
| Phase 11 | Restore drill | Before handover |

---

## Phase 5 — Database Restore Validation Checklist

- [ ] PostgreSQL confirms `wamacare_local` exists
- [ ] `psql -U odoo -d wamacare_local -c "\dt" | wc -l` returns > 50 tables
- [ ] Odoo starts without error on `wamacare_local`
- [ ] Login page appears at http://localhost:8070
- [ ] No missing module errors in Odoo logs

---

## Phase 6 — Module Load Checklist

- [ ] All expected modules show as "Installed" in Apps menu
- [ ] No modules in "Upgrade needed" state
- [ ] No modules showing error state
- [ ] Settings menu opens without error
- [ ] Contacts menu opens
- [ ] Project menu opens
- [ ] Purchase menu opens
- [ ] Accounting menu opens

---

## Phase 7 — Import Validation Checklist

For each CSV import:
- [ ] Record count matches expected rows
- [ ] No duplicate external IDs
- [ ] No broken foreign key references
- [ ] Required fields populated
- [ ] Analytic accounts linked correctly

---

## Phase 8 — Smoke Tests

| Workflow | Test Steps | Expected Result |
|---------|-----------|----------------|
| Create beneficiary | New contact → tag as Beneficiary → assign programme | Record saved, searchable |
| Create LPO | Purchase → New RFQ → vendor → product → confirm | LPO confirmed, vendor bill can be created |
| Record expense | Expense → new → employee → programme analytic | Expense linked to analytic account |
| View programme report | Accounting → Analytic → Analytic Accounts → programme | Budget vs actual shown |
| Create project task | Project → programme → new task → assign | Task visible in programme |

---

## Log Inspection

Check Odoo logs for errors:
```bash
# Start Odoo and watch logs
python /Users/mac/odoo17/odoo/odoo-bin -d wamacare_local --log-level=debug 2>&1 | grep -i "error\|warning\|critical"
```

---

*Validation report template: `testing/PHASE_10_VALIDATION_REPORT.md`*
