# REUSE_GUIDE.md — How to Fork WamaCare for Another NGO/CBO

**Date:** 2026-05-29 | **Status:** DRAFT (Phase 9 will complete)

---

## When to Use This Guide

Use this guide when deploying WamaCare as a template for a **second or subsequent NGO/CBO** organisation.

Estimated adaptation time: **1-3 days** for a similar Nigerian NGO/CBO.

---

## Step 1 — Fork or Clone the Repository

```bash
# Option A: Fork on GitHub (for independent deployment)
# Go to https://github.com/aliyuumaru-beep/wamacare_odoo → Fork

# Option B: Clone for local adaptation
git clone https://github.com/aliyuumaru-beep/wamacare_odoo.git new_org_name
cd new_org_name
git remote set-url origin https://github.com/your-account/new_org_odoo.git
```

---

## Step 2 — Create a New Database

```bash
createdb -U odoo new_org_local
python /Users/mac/odoo17/odoo/odoo-bin -d new_org_local -r odoo \
  --addons-path=... \
  -i base,contacts,project,purchase,account,analytic,hr,hr_expense,maintenance
```

---

## Step 3 — Update Organisation Profile in Odoo

In Odoo Settings → Companies:
- Company name → new organisation name
- Logo → upload new logo
- Address, phone, email → update
- Currency → NGN (or local currency)
- Country → Nigeria (or new country)

---

## Step 4 — Adapt the CSV Templates

In `csv_templates/wamacare/`:

| File | What to Change |
|------|---------------|
| `mamacare_projects.csv` | Rename programmes to match new org |
| `mamacare_analytic_accounts.csv` | Rename analytic accounts per programme |
| `beneficiaries.csv` | Replace with new org's beneficiary data |
| `hr_department.csv` | Update departments if different |
| `hr_employees.csv` | Replace with new org's staff |
| `vendor.csv` / `wamacare_vendors.csv` | Replace with new org's vendors |

---

## Step 5 — Import Data

Follow: [DATA_IMPORT_PLAN.md](./DATA_IMPORT_PLAN.md)  
Use sequence: analytic accounts → departments → projects → partners → products → employees → assets → transactions

---

## Step 6 — Update Documentation

- `CLAUDE.md` — update project name, database name, organisation name
- `README.md` — update project title and overview
- `docs/wamacare/PROJECT_IDENTITY.md` — update org profile
- `CHANGELOG.md` — add fork entry

---

## Customisation Levels

| Level | Effort | When needed |
|-------|--------|------------|
| 0 — Data swap only | 0.5-1 day | Same sector (health CBO), different org |
| 1 — Programme rename | 1-2 days | Same sector, different programme names |
| 2 — Module add/remove | 2-3 days | Different sector (education, WASH, livelihoods) |
| 3 — Custom addons | 1-2 weeks | Sector-specific workflows not in native Odoo |

---

*Full reuse guide to be completed after WamaCare MVP is validated.*
