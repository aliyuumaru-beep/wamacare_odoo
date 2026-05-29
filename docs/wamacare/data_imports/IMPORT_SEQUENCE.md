# IMPORT_SEQUENCE.md — WamaCare Detailed Data Import Sequence

**Date:** 2026-05-29 | **Phase:** 7

---

## Pre-Import Checklist

Before any import:
- [ ] Odoo is running on `wamacare_local`
- [ ] Target module is installed (e.g., `project` before importing projects)
- [ ] File is in `csv_templates/wamacare/`
- [ ] File has been reviewed for blank required fields
- [ ] External IDs are consistent across dependent files

---

## Import 1 — Analytic Accounts

**File:** `mamacare_analytic_accounts.csv`  
**Target model:** `account.analytic.account`  
**Odoo path:** Accounting → Analytic → Analytic Accounts → Import

| Column | Odoo field | Notes |
|--------|-----------|-------|
| Name | `name` | Programme name |
| Plan | `plan_id/name` | Must be "Programs" — create plan first |

**Pre-requisites:** Analytic Plans enabled in Accounting settings  
**Risk:** LOW  
**Test first:** YES — import 1 row first

---

## Import 2 — HR Departments

**File:** `hr_department.csv`  
**Target model:** `hr.department`  
**Odoo path:** Employees → Configuration → Departments → Import

| Column | Odoo field | Notes |
|--------|-----------|-------|
| name | `name` | Department name |
| parent_id/id | `parent_id/id` | External ID of parent dept |
| manager_id/id | `manager_id/id` | Must reference employee external IDs |

**Pre-requisites:** HR module installed; manager employees must be imported BEFORE using external IDs as managers  
**Risk:** MEDIUM — manager external IDs will fail if employees not imported first  
**Workaround:** Import departments WITHOUT manager column first; add managers after employee import

---

## Import 3 — Projects / Programmes

**File:** `mamacare_projects.csv`  
**Target model:** `project.project`  
**Odoo path:** Project → Projects → Import

| Column | Odoo field | Notes |
|--------|-----------|-------|
| Name | `name` | Programme name |
| Active | `active` | True/False |

**Pre-requisites:** `project` module installed; analytic accounts created  
**Risk:** LOW  

---

## Import 3b — Additional Projects

**File:** `projects.csv`  
**Target model:** `project.project`  
**Action:** Check for duplicates against `mamacare_projects.csv` before importing

---

## Import 4 — Vendors (Basic)

**File:** `vendor.csv`  
**Target model:** `res.partner`  
**Odoo path:** Purchase → Vendors → Import

| Column | Odoo field | Notes |
|--------|-----------|-------|
| Name | `name` | |
| Company Type | `company_type` | "company" |
| Vendor Rank | `supplier_rank` | Set to 1 |
| Email | `email` | |
| Phone | `phone` | |

---

## Import 5 — WamaCare Vendors (Extended)

**File:** `wamacare_vendors.csv`  
**Target model:** `res.partner`  
**Action:** Check for duplicates with `vendor.csv` imports

---

## Import 6 — Beneficiaries

**File:** `beneficiaries.csv`  
**Target model:** `res.partner`  
**Odoo path:** Contacts → Import

| Column | Odoo field | Notes |
|--------|-----------|-------|
| Name | `name` | |
| Email | `email` | May be blank — OK |
| Phone | `phone` | |
| City | `city` | |
| Country | `country_id/name` | "Nigeria" |
| Latitude | `partner_latitude` | |
| Longitude | `partner_longitude` | |
| Category Tags | `category_id/name` | Comma-separated: create tags first |

**Pre-requisites:** Partner categories (Beneficiary, Maternal Health, Protection, etc.) must exist  
**Risk:** MEDIUM — tag creation required  
**Privacy note:** Restrict access after import

---

## Import 7 — Products/Services

**Files:** `mamacare_products.csv`, `wamacare_products.csv`  
**Target model:** `product.template`  
**Action:** De-duplicate between the two files before importing

---

## Import 8 — Employees

**File:** `hr_employees.csv`  
**Target model:** `hr.employee`  
**Action:** After import, go back and set department managers using employee IDs

---

## Import 9 — Assets

**File:** `assets.csv`  
**Target model:** `maintenance.equipment` or `account.asset` (confirm after Phase 5)  
**Risk:** MEDIUM — confirm correct model first

---

## Import 10 — Project Tasks/Activities

**File:** `activities.csv`  
**Target model:** `project.task`

---

## Import 11 — LPO (Purchase Order)

**File:** `lpo.csv`  
**Target model:** `purchase.order`  
**Risk:** HIGH — requires vendors, products, and projects to exist  
**Action:** Import as draft; do not confirm automatically

---

## Import 12 — Expenses / Vendor Bills

**File:** `mamacare_expenses.csv`  
**Target model:** `account.move` (Vendor Bill)  
**Risk:** HIGH — financial record; validate carefully before posting  
**Action:** Import as draft; finance officer to review before posting

---

## Post-Import Validation

For each import, run these checks:
```sql
-- Count records (run in psql)
SELECT COUNT(*) FROM res_partner WHERE supplier_rank > 0;  -- vendors
SELECT COUNT(*) FROM project_project;                      -- projects
SELECT COUNT(*) FROM hr_employee;                          -- employees
SELECT COUNT(*) FROM account_analytic_account;             -- analytic accounts
```
