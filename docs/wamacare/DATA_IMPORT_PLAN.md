# DATA_IMPORT_PLAN.md — WamaCare Data Import Plan

**Date:** 2026-05-29 | **Status:** READY for Phase 7

---

## Overview

WamaCare has 14 CSV data files ready for import. If the database is restored from `mamacare1.dump.zip`, some or all of these may already be present. If a fresh database is created, they must be imported in the sequence below.

All CSV files are stored in: `csv_templates/wamacare/`

---

## Import Sequence

### Priority 1 — Foundation (must be first)

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 1 | `mamacare_analytic_accounts.csv` | `account.analytic.account` | Create programme accounts before projects |
| 2 | `hr_department.csv` | `hr.department` | Create departments before employees |
| 3 | `mamacare_projects.csv` | `project.project` | Requires analytic accounts to exist |
| 4 | `projects.csv` | `project.project` | Duplicate check needed — same model |

### Priority 2 — Partners (vendors and beneficiaries)

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 5 | `vendor.csv` | `res.partner` | Set type=supplier |
| 6 | `wamacare_vendors.csv` | `res.partner` | 15 specialist vendors |
| 7 | `beneficiaries.csv` | `res.partner` | Tag as Beneficiary |

### Priority 3 — Products and Services

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 8 | `mamacare_products.csv` | `product.template` | NGO programme services |
| 9 | `wamacare_products.csv` | `product.template` | Duplicate check with mamacare_products |

### Priority 4 — Staff

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 10 | `hr_employees.csv` | `hr.employee` | Requires departments to exist |

### Priority 5 — Assets

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 11 | `assets.csv` | `maintenance.equipment` or `account.asset` | Confirm model post-restore |

### Priority 6 — Operations

| Order | File | Target Model | Notes |
|-------|------|-------------|-------|
| 12 | `activities.csv` | `project.task` | Requires projects to exist |
| 13 | `lpo.csv` | `purchase.order` | Requires vendors and products to exist |
| 14 | `mamacare_expenses.csv` | `account.move` (Bill) | Requires vendors and analytic accounts |

---

## Pre-Import Checks

For each CSV before importing:

- [ ] File opens correctly in a text editor
- [ ] Header row matches Odoo field names
- [ ] No duplicate external IDs
- [ ] Required fields are not empty
- [ ] Foreign key references exist in the system
- [ ] Analytic account names match exactly

---

## Known Data Issues

| File | Issue | Action |
|------|-------|--------|
| `beneficiaries.csv` | Missing email addresses | OK for CBO — phone is primary |
| `hr_employees.csv` | External IDs (`emp_aliyu`, etc.) referenced in hr_department | Must import employees before referencing as managers |
| `mamacare_expenses.csv` | Only 1 row — likely demo data | Import as reference only |
| `activities.csv` | Only 1 row | Import as demo seed |
| `mamacare_projects.csv` + `projects.csv` | May overlap | De-duplicate before import |

---

## Cleaned CSV Location

If any file needs cleaning before import, the cleaned version goes to:
`csv_templates/wamacare/cleaned/`

The original is never modified.

---

*Detailed import sequence with field mappings: see [data_imports/IMPORT_SEQUENCE.md](./data_imports/IMPORT_SEQUENCE.md)*
