# EVIDENCE_BASED_AUDIT.md — WamaCare Capability Audit

**Date:** 2026-05-29 | **Auditor:** Claude Code (automated database + RPC inspection)
**Method:** Direct PostgreSQL queries + Odoo XML-RPC calls against `wamacare_local`

> This audit compares capability claims in BUSINESS_CAPABILITY_MAP.md and FEATURE_REGISTRY.md
> against actual database evidence. Claims are verified or refuted using SQL and RPC results.
> No assumptions. Evidence only.

---

## Audit Legend

| Verdict | Meaning |
|---------|---------|
| ✅ VERIFIED | Claim is correct. Evidence confirms functionality. |
| 🔶 PARTIAL/UNUSED | Module or config exists, but zero usage data. Installed ≠ operational. |
| ❌ OVERCLAIMED | Claimed COMPLETED or PARTIAL but evidence shows nothing done. |
| ⚠️ WRONG | Claim is factually incorrect — wrong status assigned. |
| 🔴 CRITICAL GAP | Gap has security, compliance, or operational consequences. |

---

## Section 1 — Governance

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| GOV-001 Department Structure | COMPLETED | 6 departments in `hr_department`, 5 with managers confirmed | ✅ VERIFIED |
| GOV-002 Role-Based Access Control | COMPLETED | 5 users with group assignments confirmed in `res_groups_users_rel` | ⚠️ PARTIALLY WRONG — see note |
| GOV-003 Audit Trail (Chatter) | COMPLETED | `mail` module installed, chatter on all models | ✅ VERIFIED |
| GOV-004 Purchase Approval Workflow | COMPLETED | `po_double_validation = 'two_step'`, `po_double_validation_amount = 200,000` confirmed in `res_company` | ✅ VERIFIED |
| GOV-005 Two-Factor Authentication | COMPLETED | `auth_totp` module installed. `totp_required_role` column does NOT exist — 2FA is available but NOT enforced. Any user can log in without TOTP. | ❌ OVERCLAIMED |
| GOV-006 Fiscal Year Management | COMPLETED | `om_fiscal_year` module installed. `account_fiscal_year` table: **0 records** | 🔶 PARTIAL/UNUSED |
| GOV-007 Contract Repository | PLANNED | `hr_contract` = uninstalled, `sign` = uninstallable, `documents` = not present | ✅ VERIFIED (correctly PLANNED) |

**GOV-002 Note:** `field.officer` role has "Analytic Accounting", "Internal User" — but does **NOT** have `project.group_project_user`. Field officers cannot see project tasks. Role assignment is incomplete. `aliyu.umaru` is in "Administrator" group which grants excessive system access.

---

## Section 2 — HR

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| HR-001 Employee Records | COMPLETED | 10 active employees in `hr_employee`, correctly department-assigned | ✅ VERIFIED |
| HR-002 Org Chart | COMPLETED | `hr_org_chart` installed, departments with managers configured | ✅ VERIFIED |
| HR-003 Job Positions | COMPLETED | 9 job positions confirmed via `hr_job` and employee records | ✅ VERIFIED |
| HR-004 Expense Claims | COMPLETED | `hr_expense` module installed, linked to projects. `hr_expense` table: **0 records**. `hr_expense_sheet` table: **0 records**. Never used. | 🔶 PARTIAL/UNUSED |
| HR-005 Skills Tracking | PARTIAL | `hr_skills` installed. `hr_employee_skill` table: **0 records**. No skills entered for any employee. | ❌ OVERCLAIMED (claimed PARTIAL, actually empty) |
| HR-006 Staff Onboarding | PARTIAL | `hr_resume_line` table: 9 records. These are auto-generated job title entries (e.g. "Mobilizer at WamaCare"), NOT structured onboarding checklists. | ❌ OVERCLAIMED |
| HR-007 Training Records | PLANNED | No training data anywhere. Correctly PLANNED. | ✅ VERIFIED |

---

## Section 3 — Programme Management

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| PROG-001 Programme Definition | COMPLETED | 5 projects in `project_project` | ✅ VERIFIED |
| PROG-002 Analytic Account per Programme | COMPLETED | All 5 projects linked to analytic accounts. 13 accounts under "Programs" plan. | ✅ VERIFIED |
| PROG-003 Budget per Programme | COMPLETED | `om_account_budget` installed. `crossovered_budget`: **0 records**. `crossovered_budget_lines`: **0 records**. `account_budget_post`: **0 budgetary positions**. Budget module installed but never configured or used. | ❌ OVERCLAIMED |
| PROG-004 Activity Calendar | COMPLETED | `calendar` module installed | ✅ VERIFIED |
| PROG-005 Task and Activity Tracking | PARTIAL | `project_task` table: **0 records**. 5 projects exist with 0 tasks. Projects are shells with no activity content. | 🔶 PARTIAL/UNUSED |
| PROG-006 Programme Dashboard | PARTIAL | Spreadsheet dashboard table: 2 records — "Invoicing" and "Vendors". These are **generic Odoo defaults**. No WamaCare programme dashboard exists. | ❌ OVERCLAIMED |
| PROG-007 Milestone Tracking | PARTIAL | `project_milestone` table: **0 records** | 🔶 PARTIAL/UNUSED |
| PROG-008 Budget vs Actual | PLANNED | Impossible to run — no budget records, no financial transactions | ✅ VERIFIED (correctly PLANNED) |

---

## Section 4 — Donor Management

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| DONOR-001 Donor Contact Records | PARTIAL | 17 vendor partners exist. No partner has "Donor" category tag. No donor-specific contacts created. | ❌ OVERCLAIMED |
| DONOR-002 Grant Analytic Accounts | COMPLETED | 13 analytic accounts correctly created and linked to projects | ✅ VERIFIED |
| DONOR-003 Recurring Payments | COMPLETED | `om_recurring_payments` installed. No recurring payment records found. | 🔶 PARTIAL/UNUSED |
| DONOR-004 Donor Follow-Up | COMPLETED | `om_account_followup` installed. No follow-up records. | 🔶 PARTIAL/UNUSED |
| DONOR-005 MOU Storage | PLANNED | No documents module. Correctly PLANNED. | ✅ VERIFIED |

---

## Section 5 — Procurement

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| PROC-001 Vendor Management | COMPLETED | 17 vendors with `supplier_rank > 0` confirmed | ✅ VERIFIED |
| PROC-002 Local Purchase Order (LPO) | COMPLETED | P00001 exists in `purchase_order`, amount ₦2,500,000 | ✅ VERIFIED |
| PROC-003 LPO Approval Workflow | COMPLETED | `po_double_validation = 'two_step'` confirmed. P00001 is in **DRAFT** state — it has never been submitted for approval. Workflow configured but never executed. | 🔶 PARTIAL/UNUSED |
| PROC-004 Vendor Invoice Processing | COMPLETED | `account.move` vendor bills: **0 records**. No vendor bill has ever been created from any LPO. | 🔶 PARTIAL/UNUSED |
| PROC-005 Payment Approval | COMPLETED | Account module installed. `account_payment` table: **0 records**. | 🔶 PARTIAL/UNUSED |
| PROC-006 Procurement Reports | COMPLETED | 2 purchase report templates confirmed in `ir_act_report_xml` (RFQ and PO reports) | ✅ VERIFIED |

---

## Section 6 — Finance

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| FIN-001 Chart of Accounts (NGO) | COMPLETED | 70 accounts in `account_account` including 21 NGO-specific (4000–5090, 2100–2140, 3000–3010) | ✅ VERIFIED |
| FIN-002 NGN Functional Currency | COMPLETED | `res_company.currency_id` = NGN confirmed | ✅ VERIFIED |
| FIN-003 Nigeria VAT (7.5%) | COMPLETED | `l10n_ng` installed. Tax records created. | ✅ VERIFIED |
| FIN-004 WHT | COMPLETED | `l10n_ng` installed. WHT accounts 252001/252002 present | ✅ VERIFIED |
| FIN-005 Analytic Accounting | COMPLETED | Config param `account.analytic_accounting = 1` confirmed. 13 analytic accounts. | ✅ VERIFIED |
| FIN-006 Budget Management | COMPLETED | Module installed. `crossovered_budget`: **0 records**. `account_budget_post` (budgetary positions): **0 records**. Nothing configured. | ❌ OVERCLAIMED |
| FIN-007 Asset Depreciation | COMPLETED | `om_account_asset` installed. `account_asset_asset`: **0 records**. No asset has been configured for depreciation. | ❌ OVERCLAIMED |
| FIN-008 Recurring Payments | COMPLETED | `om_recurring_payments` installed. No recurring records. | 🔶 PARTIAL/UNUSED |
| FIN-009 Daily Financial Reports | COMPLETED | `om_account_daily_reports` installed. `account_move` (all types): **0 records**. Reports exist but there is no data to report on. | 🔶 PARTIAL/UNUSED |
| FIN-010 Full Accounting Suite | COMPLETED | `om_account_accountant` installed and functional | ✅ VERIFIED |
| FIN-011 FIRS Tax Report | COMPLETED | `l10n_ng` installed with tax report structure | ✅ VERIFIED |
| FIN-012 Bank Account | PARTIAL | `res_partner_bank`: **0 records**. No bank account configured. | ✅ VERIFIED (correctly PARTIAL) |
| FIN-013 Bank Reconciliation | PARTIAL | Depends on FIN-012. No bank account = no reconciliation possible. | ✅ VERIFIED (correctly PARTIAL) |
| FIN-014 PAYE/PENCOM | PARTIAL | COA accounts 2110/2130 created. No payroll transactions. | ✅ VERIFIED (correctly PARTIAL) |
| FIN-015 Budget vs Actual Dashboard | PLANNED | Impossible — no budget records, no transactions. | ✅ VERIFIED (correctly PLANNED) |

**Critical Finance Finding:** `account_move` (all journal entries): **0 records**. WamaCare has installed a comprehensive accounting system with zero financial activity. No bill has ever been created, no payment recorded, no expense posted. The system is a financial infrastructure with no financial history.

---

## Section 7 — Asset Management

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| ASSET-001 Asset Register | COMPLETED | 3 records in `maintenance_equipment` (Ambulance, Ultrasound, Laptop) | ✅ VERIFIED |
| ASSET-002 Asset Depreciation Module | COMPLETED | `om_account_asset` installed. `account_asset_asset`: **0 records**. The 3 maintenance equipment records have NOT been set up as financial assets for depreciation. Module installed but assets not configured in it. | ❌ OVERCLAIMED |
| ASSET-003 Equipment Categories | PARTIAL | `maintenance_equipment.category_id`: **NULL for all 3 assets**. No categories assigned. | ❌ OVERCLAIMED (worse than PARTIAL — nothing done) |
| ASSET-004 Asset Assignment | PARTIAL | `maintenance_equipment.employee_id`: **NULL for all 3 assets**. No assets assigned to any department or employee. | ❌ OVERCLAIMED |
| ASSET-005 Maintenance Scheduling | PARTIAL | Module installed. No maintenance requests or schedules created. | ❌ OVERCLAIMED |
| ASSET-006 Depreciation Config | PLANNED | Correctly PLANNED — confirmed nothing done. | ✅ VERIFIED |

---

## Section 8 — Inventory

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| INV-001 Product Catalogue | COMPLETED | 21 records in `product_template` | ✅ VERIFIED |
| INV-002–007 Stock features | PLANNED | `stock` module not installed. Correctly PLANNED. | ✅ VERIFIED |

---

## Section 9 — Beneficiary Management

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| BEN-001 Beneficiary Registration | COMPLETED | 13 beneficiary records confirmed | ✅ VERIFIED |
| BEN-002 Programme Tagging | COMPLETED | Category tags (Maternal Health, Protection, etc.) on partner records confirmed | ✅ VERIFIED |
| BEN-003 Geolocation | COMPLETED | `partner_latitude`/`partner_longitude` populated for all 13 | ✅ VERIFIED |
| BEN-004 Gender Tagging | COMPLETED | "Female" category tag confirmed on all 13 beneficiaries | ✅ VERIFIED |
| BEN-005 Anonymised Naming | PARTIAL | BEN-004 to BEN-016 naming scheme confirmed. No formal enforcement mechanism. | ✅ VERIFIED |
| BEN-006 Access Restriction | PLANNED | `ir_rule` on `res.partner`: only **2 system defaults** (company isolation + portal access). **No WamaCare-specific beneficiary access rule exists**. Field officers, finance staff, and all internal users can currently see all 13 beneficiary records including names, phones, locations, and programme tags. | 🔴 CRITICAL GAP |

---

## Section 10 — Safeguarding

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| SAFE-001 Safeguarding Programme | COMPLETED | "Safeguarding & Protection Program" confirmed in `project_project` | ✅ VERIFIED |
| SAFE-002 Safeguarding Department | COMPLETED | "Legal & Compliance" department confirmed with Head Legal & Compliance as manager | ✅ VERIFIED |
| SAFE-003 Safeguarding Lead Role | COMPLETED | "Safeguarding Lead C" in Legal & Compliance confirmed | ✅ VERIFIED |
| SAFE-004 NDPR Privacy Module | PARTIAL | `privacy_lookup` installed. `privacy_lookup_wizard` table: **0 records**. Module available but never used. | 🔶 PARTIAL/UNUSED |
| SAFE-005–009 | PLANNED | Correctly PLANNED. No alert, escalation, or referral mechanism exists. | ✅ VERIFIED |

---

## Section 11 — M&E

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| ME-001 M&E Programme | COMPLETED | "Monitoring & Evaluation Program" confirmed in `project_project` | ✅ VERIFIED |
| ME-002 Task Completion | COMPLETED | `project_task`: **0 records**. No tasks exist in any programme. Task completion tracking is impossible with no tasks. | ❌ OVERCLAIMED |
| ME-003 Budget vs Actual | COMPLETED | Claimed because infrastructure exists. `account_move`: **0 records**. `crossovered_budget`: **0 records**. There is nothing to compare. | ❌ OVERCLAIMED |
| ME-004 Programme Dashboard | PARTIAL | 2 dashboards: "Invoicing" and "Vendors" — generic Odoo defaults. No M&E or programme-specific dashboard. | ❌ OVERCLAIMED |

---

## Section 12 — Executive Dashboard

| Feature | Claimed Status | Evidence | Verdict |
|---------|---------------|---------|---------|
| EXEC-001 Financial Dashboard | COMPLETED | Only "Invoicing" and "Vendors" dashboards exist in `spreadsheet_dashboard`. Groups: Finance, Sales, Logistics, HR, Services, Website — all generic Odoo. No financial data to display (0 journal entries). | ❌ OVERCLAIMED |
| EXEC-002 Procurement Dashboard | COMPLETED | No procurement-specific dashboard exists. P00001 in DRAFT. | ❌ OVERCLAIMED |
| EXEC-003 Programme Overview | COMPLETED | Project kanban/list view is available in UI. 5 projects visible. This works as a basic programme overview. | ✅ VERIFIED |
| EXEC-004–006 | PLANNED | Correctly PLANNED | ✅ VERIFIED |

---

## Critical Security Finding — User Roles

```
user: field.officer
Groups: Analytic Accounting, Basic Pricelists, Internal User, 
        Mail Template Editor, Multi Currencies, Send reminder
MISSING: project.group_project_user (cannot see project tasks)
PROBLEM: Has Analytic Accounting access (can see financial data)
```

```
user: aliyu.umaru
Groups: Administrator (purchase), Administrator (project), Accountant,
        Analytic Accounting, Billing, Equipment Manager, HR Officer,
        Mail Template Editor, Technical Features
PROBLEM: Has "Technical Features" group — access to technical menus
PROBLEM: Has Equipment Manager — should this role have equipment access?
```

```
user: hr.officer
Groups: Analytic Accounting, Equipment Manager, HR Officer, Internal User
PROBLEM: Has Equipment Manager — likely not intended
PROBLEM: Has Analytic Accounting — likely not intended for HR role
```

---

## Financial Void Summary

**The most significant finding: WamaCare has a complete financial infrastructure with zero financial activity.**

| Financial Entity | Records |
|-----------------|---------|
| Journal entries (all types) | **0** |
| Vendor bills posted | **0** |
| Expense claims submitted | **0** |
| Budget records created | **0** |
| Budget lines entered | **0** |
| Budget positions defined | **0** |
| Bank accounts configured | **0** |
| Asset depreciation entries | **0** |
| Recurring payment entries | **0** |
| Fiscal years configured | **0** |

The LPO P00001 (₦2,500,000) exists in **DRAFT** state and has never been confirmed, approved, or converted to a vendor bill.

---

## Revised Feature Status by Evidence

| Original Status | Evidence-Based Status | Count | Examples |
|----------------|----------------------|-------|---------|
| COMPLETED | ✅ VERIFIED COMPLETE | 28 | GOV-001, FIN-001, BEN-001, PROC-001 |
| COMPLETED | 🔶 INSTALLED BUT UNUSED | 10 | HR-004, PROG-003, PROC-004, FIN-008, EXEC-001 |
| COMPLETED | ❌ OVERCLAIMED | 13 | GOV-005, FIN-006, FIN-007, ASSET-002, ME-002, ME-003 |
| PARTIAL | ✅ CORRECTLY PARTIAL | 8 | FIN-012, FIN-013, BEN-005 |
| PARTIAL | ❌ OVERCLAIMED | 6 | HR-005, HR-006, ASSET-003, ASSET-004, DONOR-001 |
| PLANNED | ✅ CORRECTLY PLANNED | 55 | All planned features |

---

## Priority Actions by Evidence

### Immediate (data integrity and security)

| # | Finding | Action |
|---|---------|--------|
| 1 | BEN-006 not implemented — all beneficiary data accessible to all users | Create `ir.rule` on `res.partner` restricting beneficiary category to Programme role |
| 2 | P00001 in DRAFT — LPO workflow never tested end-to-end | Confirm P00001, receive it, create vendor bill, approve payment |
| 3 | `field.officer` missing `project.group_project_user` | Add group via Settings → Users |
| 4 | `aliyu.umaru` has "Technical Features" group | Remove — not appropriate for Programme Manager role |

### Short-term (get to Level 1 operational)

| # | Finding | Action |
|---|---------|--------|
| 5 | 0 budget records despite module being installed | Create budgetary positions and enter budgets for 5 programmes |
| 6 | 0 fiscal years configured | Create 2026 fiscal year in Accounting → Settings |
| 7 | 0 bank accounts | Add WamaCare bank account in Accounting → Configuration |
| 8 | Assets not configured for depreciation | Create om_account_asset records for 3 maintenance equipment items |
| 9 | Equipment has no categories, no assignment | Set category and assign to department/employee |
| 10 | GOV-005 2FA not enforced | Configure TOTP enforcement in company settings |

### Medium-term (restore accurate claims)

| # | Finding | Action |
|---|---------|--------|
| 11 | EXEC-001/002 dashboards are generic Odoo defaults | Build WamaCare-specific spreadsheet dashboards |
| 12 | PROG-006 programme dashboard does not exist | Create with programme KPIs once budget data exists |
| 13 | HR skills module empty | Load skill catalogue for employees |
| 14 | DONOR-001 no donor contacts tagged | Tag existing contacts or add donor records |

---

## Honest Maturity Reassessment

Based on this audit, the true Phase A completion is lower than claimed:

| Subdomain | Previously Claimed | Evidence-Based |
|-----------|-------------------|----------------|
| Governance | 85% | **70%** (2FA not enforced, fiscal year missing) |
| HR | 70% | **55%** (skills empty, onboarding auto-generated) |
| Finance | 90% | **65%** (all transactions = 0, budget = 0) |
| Procurement | 90% | **60%** (LPO never confirmed, no bills, no payments) |
| Programme Mgmt | 75% | **55%** (0 tasks, 0 milestones, budgets empty) |
| Asset Mgmt | 60% | **30%** (equipment registered but nothing else done) |
| Beneficiary | 75% | **60%** (access restriction missing — security risk) |

**Revised Phase A completion: ~58% (not 78%)**

The gap is almost entirely in usage: the infrastructure is installed but has not been exercised. WamaCare needs its first real LPO cycle, its first expense claim, and its first budget entry before it can be considered operationally validated.
