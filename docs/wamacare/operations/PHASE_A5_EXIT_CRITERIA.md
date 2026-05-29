# PHASE_A5_EXIT_CRITERIA.md — WamaCare Phase A.5 Exit Criteria

**Version:** 1.0 | **Date:** 2026-05-29
**Authority:** No feature may be marked COMPLETED in FEATURE_REGISTRY.md unless it satisfies all four criteria below. This document governs feature graduation.

---

## The Four-Gate Rule

A feature is COMPLETED only when it passes all four gates:

```
Gate 1: CONFIGURED    → Module installed AND settings applied
Gate 2: TESTED        → End-to-end scenario executed, records in DB
Gate 3: PRODUCES OUTPUT → Expected report/record/audit trail generated
Gate 4: ACCESS-CONTROLLED → Correct users can access; wrong users cannot
```

A feature that passes Gate 1 only is "INSTALLED". It is not PARTIAL. It is not COMPLETED.
A feature that passes Gates 1-2 is "PARTIAL".
A feature that passes Gates 1-3 is "PARTIAL (TESTED)".
A feature that passes all 4 gates is "COMPLETED".

---

## Security Items — Critical Risk Category

Security features (BEN-006, role corrections, 2FA enforcement) are categorised separately as **Critical Risk** items. They do not queue behind operational features. They run in parallel with or before operational validation.

| Critical Risk Item | Status | Gate Blocking |
|-------------------|--------|--------------|
| BEN-006 Beneficiary access restriction | ❌ NOT DONE | ALL Phase B features |
| field.officer missing project.group_project_user | ❌ NOT DONE | Lifecycle 4 (HR), Lifecycle 7 (Programme) |
| aliyu.umaru has Technical Features group | ❌ NOT DONE | Security hygiene |
| hr.officer has Equipment Manager (unintended) | ❌ NOT DONE | Security hygiene |
| Admin password = 'admin' | ❌ NOT DONE | Production readiness |
| 2FA not enforced | ❌ NOT DONE | Production readiness |

**These must be fixed before any production use, regardless of operational validation progress.**

---

## Exit Criteria per Feature Domain

### Governance

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| GOV-001 Department Structure | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| GOV-002 RBAC | ✅ | ⚠️ incomplete | ❌ | ❌ | PARTIAL |
| GOV-003 Audit Trail | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| GOV-004 Purchase Approval | ✅ | ❌ never run | ❌ | ❌ | INSTALLED |
| GOV-005 2FA | ✅ module | ❌ not enforced | ❌ | ❌ | INSTALLED |
| GOV-006 Fiscal Year | ❌ not set up | ❌ | ❌ | ❌ | NOT STARTED |
| GOV-007 Contract Repository | ❌ no module | ❌ | ❌ | ❌ | NOT STARTED |

**GOV-004 exit test:** Confirm P00001 → reject it → create new PO above ₦200k → receive approval notification → approve it → verify state = 'purchase' in DB.

**GOV-005 exit test:** Enable TOTP enforcement in company settings → log out → attempt login without TOTP → confirm blocked → set up TOTP → confirm login succeeds.

**GOV-006 exit test:** Create fiscal year 01/01/2026–31/12/2026 → confirm `account_fiscal_year` COUNT = 1 → lock a period → confirm prior-period entries are blocked.

---

### HR

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| HR-001 Employee Records | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| HR-002 Org Chart | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| HR-003 Job Positions | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| HR-004 Expense Claims | ✅ | ❌ 0 records | ❌ | ❌ | INSTALLED |
| HR-005 Skills Tracking | ✅ | ❌ 0 skills | ❌ | ❌ | INSTALLED |
| HR-006 Onboarding | ❌ no checklist | ❌ | ❌ | ❌ | NOT STARTED |
| HR-007 Training Records | ❌ no data | ❌ | ❌ | ❌ | NOT STARTED |

**HR-004 exit test:** Lifecycle 4 scenario executed → `hr_expense` COUNT >= 1 → Expense Report PDF generated → chatter shows submission/approval chain.

**HR-005 exit test:** Load skills catalogue for employees → `hr_employee_skill` COUNT >= 5 → Skill History Report renders via Employees → Departments.

---

### Programme Management

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| PROG-001 Programme Definition | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| PROG-002 Analytic per Programme | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| PROG-003 Budget per Programme | ✅ | ❌ 0 budgets | ❌ | ❌ | INSTALLED |
| PROG-004 Activity Calendar | ✅ | ❌ no events | ❌ | ❌ | INSTALLED |
| PROG-005 Task Tracking | ✅ | ❌ 0 tasks | ❌ | ❌ | INSTALLED |
| PROG-006 Programme Dashboard | ❌ | ❌ | ❌ | ❌ | NOT STARTED |
| PROG-007 Milestones | ✅ | ❌ 0 milestones | ❌ | ❌ | INSTALLED |
| PROG-008 Budget vs Actual | ❌ no data | ❌ | ❌ | ❌ | NOT STARTED |

**PROG-003 exit test:** Lifecycle 3 scenario → `crossovered_budget` COUNT = 5 → Budget Analysis report shows 5 programmes with planned amounts → one programme shows actual after Lifecycle 2.

**PROG-005 exit test:** Lifecycle 7 scenario → `project_task` COUNT >= 5 (one per programme) → at least 1 in state 'done' → chatter shows task progress notes.

---

### Finance

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| FIN-001 COA (NGO) | ✅ 70 accounts | ✅ accounts exist | ⚠️ no transactions | ❌ | PARTIAL |
| FIN-002 NGN Currency | ✅ | ✅ | ✅ | ✅ | **COMPLETED** |
| FIN-003 Nigeria VAT | ✅ | ❌ never applied | ❌ | ❌ | INSTALLED |
| FIN-004 WHT | ✅ | ❌ never applied | ❌ | ❌ | INSTALLED |
| FIN-005 Analytic Accounting | ✅ | ✅ config | ⚠️ no transactions | ❌ | PARTIAL |
| FIN-006 Budget Management | ✅ | ❌ 0 budgets | ❌ | ❌ | INSTALLED |
| FIN-007 Asset Depreciation | ✅ | ❌ 0 configured | ❌ | ❌ | INSTALLED |
| FIN-008 Recurring Payments | ✅ | ❌ 0 records | ❌ | ❌ | INSTALLED |
| FIN-009 Daily Reports | ✅ | ❌ 0 data | ❌ | ❌ | INSTALLED |
| FIN-010 Full Accounting Suite | ✅ | ❌ 0 entries | ❌ | ❌ | INSTALLED |
| FIN-011 FIRS Tax Report | ✅ | ❌ 0 tax entries | ❌ | ❌ | INSTALLED |
| FIN-012 Bank Account | ❌ | ❌ | ❌ | ❌ | NOT STARTED |
| FIN-013 Bank Reconciliation | ❌ | ❌ | ❌ | ❌ | NOT STARTED |
| FIN-014 PAYE/PENCOM | ✅ accounts | ❌ no payroll | ❌ | ❌ | INSTALLED |
| FIN-015 Budget vs Actual Dashboard | ❌ | ❌ | ❌ | ❌ | NOT STARTED |

**FIN-001 exit test:** Lifecycle 2 executed → `account_move_line` includes entries on accounts 5030, 2000 → Trial Balance PDF renders correctly.

**FIN-005 exit test:** After Lifecycle 2 → `account_analytic_line` COUNT >= 1 → Analytic Accounts report shows ₦1,850,000 under Maternal Health.

**FIN-006 exit test:** Lifecycle 3 → `crossovered_budget` COUNT >= 5 → Budget vs Actual shows planned vs actual.

**FIN-012 exit test:** Add bank account → `res_partner_bank` COUNT = 1 → Payment journal uses bank account → bank statement can be imported.

---

### Asset Management

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| ASSET-001 Asset Register | ✅ 3 records | ✅ | ⚠️ incomplete | ❌ | PARTIAL |
| ASSET-002 Depreciation Module | ✅ | ❌ 0 configured | ❌ | ❌ | INSTALLED |
| ASSET-003 Equipment Categories | ❌ all NULL | ❌ | ❌ | ❌ | NOT STARTED |
| ASSET-004 Asset Assignment | ❌ all NULL | ❌ | ❌ | ❌ | NOT STARTED |
| ASSET-005 Maintenance Scheduling | ✅ | ❌ 0 requests | ❌ | ❌ | INSTALLED |
| ASSET-006 Depreciation Config | ❌ | ❌ | ❌ | ❌ | NOT STARTED |

**ASSET-001 complete exit test:** Set categories on all 3 equipment items + assign to departments → `maintenance_equipment.category_id` NOT NULL for all 3.

**ASSET-002 exit test:** Lifecycle 5 → `account_asset_asset` COUNT >= 1 → Depreciation schedule computed → First entry posted → Asset report PDF renders.

---

### Procurement

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| PROC-001 Vendor Management | ✅ | ✅ 17 vendors | ✅ | ✅ | **COMPLETED** |
| PROC-002 LPO | ✅ | ⚠️ draft only | ❌ | ❌ | INSTALLED |
| PROC-003 LPO Approval | ✅ setting | ❌ never tested | ❌ | ❌ | INSTALLED |
| PROC-004 Vendor Invoice | ✅ | ❌ 0 bills | ❌ | ❌ | INSTALLED |
| PROC-005 Payment Approval | ✅ | ❌ 0 payments | ❌ | ❌ | INSTALLED |
| PROC-006 Procurement Reports | ✅ templates | ⚠️ no data | ❌ | ❌ | INSTALLED |

**PROC-002/003 exit test:** Lifecycle 1 → P00001 confirmed → second PO above ₦200k → approval email sent → approver approves → state = 'purchase'.

---

### Beneficiary Management

| Feature | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Exit Status |
|---------|--------|--------|--------|--------|------------|
| BEN-001 Registration | ✅ | ✅ 13 records | ✅ | ❌ | PARTIAL (no access control) |
| BEN-002 Programme Tagging | ✅ | ✅ | ✅ | ❌ | PARTIAL (no access control) |
| BEN-003 Geolocation | ✅ | ✅ | ✅ | ❌ | PARTIAL |
| BEN-004 Gender Tagging | ✅ | ✅ | ✅ | ❌ | PARTIAL |
| BEN-005 Anonymised Naming | ✅ | ✅ | ✅ | ❌ | PARTIAL |
| BEN-006 Access Restriction | ❌ NO RULES | ❌ | ❌ | ❌ | **CRITICAL — NOT STARTED** |

**BEN-001 through BEN-005 cannot reach COMPLETED until BEN-006 is done (Gate 4 always fails without access control).**

**BEN-006 exit test:**
1. Create `ir.rule` on `res.partner` with domain `[('category_id.name', 'ilike', 'Beneficiary')]`
2. Rule applies to: Programme Manager group and above only
3. Log in as `finance.officer` → Contacts → search "BEN-" → confirm 0 results
4. Log in as `aliyu.umaru` → Contacts → search "BEN-" → confirm 13 results
5. Verify: `ir_rule` COUNT for res.partner > 2 (the 2 system defaults)

---

## Re-Ranked Next Actions

### TIER 0 — Critical Risk (do before anything else)

| # | Action | Risk if skipped | Effort |
|---|--------|----------------|--------|
| CR-1 | **BEN-006** Create beneficiary access restriction rule | 13 vulnerable women's data exposed to all users | 2 hrs |
| CR-2 | **field.officer** Add `project.group_project_user` | Field officer cannot log programme activities | 15 min |
| CR-3 | **aliyu.umaru** Remove Technical Features group | Programme Manager has unintended technical access | 5 min |
| CR-4 | **hr.officer** Remove Equipment Manager group | HR role has unintended equipment access | 5 min |
| CR-5 | **Admin password** Change from 'admin/admin' | System fully open to default credential attack | 5 min |

### TIER 1 — Operational Foundation (enables all Lifecycle tests)

| # | Action | Lifecycle Unlocked | Effort |
|---|--------|-------------------|--------|
| OP-1 | **FIN-012** Configure bank account | All payment workflows | 30 min |
| OP-2 | **FIN-006** Create fiscal year 2026 | Period locking, reporting | 15 min |
| OP-3 | **Link employees to users** (field.officer → Field Officer A) | Lifecycle 4 HR | 15 min |
| OP-4 | **PROG-003** Create budgetary positions (5 accounts) | Lifecycle 3 Budget | 30 min |
| OP-5 | **PROG-003** Enter programme budgets (5 programmes) | Budget vs actual reporting | 30 min |
| OP-6 | **ASSET-003** Set categories on 3 equipment items | ASSET-001 completion | 15 min |
| OP-7 | **ASSET-004** Assign equipment to departments | ASSET-001 completion | 15 min |

### TIER 2 — Lifecycle Execution (in order per OPERATIONAL_VALIDATION_PLAN)

| # | Lifecycle | Key DB Evidence | Effort |
|---|-----------|----------------|--------|
| L-1 | Procurement Lifecycle (new PO) | `purchase_order` state='purchase' | 1 hr |
| L-2 | Finance Lifecycle (post MC-EXP-002 bill) | `account_move` COUNT >= 1 | 30 min |
| L-3 | Budget Lifecycle | `crossovered_budget` COUNT = 5 | 45 min |
| L-4 | HR Lifecycle (expense claim) | `hr_expense_sheet` COUNT >= 1 | 30 min |
| L-5 | Asset Lifecycle (configure Ambulance) | `account_asset_asset` COUNT >= 1 | 45 min |
| L-6 | Programme Lifecycle (create+complete tasks) | `project_task` COUNT >= 5 | 30 min |
| L-7 | Donor Report (budget vs actual PDF) | Report renders with correct data | 30 min |

### TIER 3 — Feature Completions (after Lifecycle tests pass)

| # | Feature | Becomes COMPLETED after |
|---|---------|------------------------|
| GOV-004 | Purchase Approval | Lifecycle 1 approval chain tested |
| PROC-002 | LPO | Lifecycle 1 confirmed PO exists |
| PROC-003 | LPO Approval | Lifecycle 1 approval verified |
| PROC-004 | Vendor Invoice | Lifecycle 2 bill posted |
| FIN-001 | COA (operational) | Lifecycle 2 journal entries created |
| FIN-005 | Analytic Accounting | Lifecycle 2 analytic lines created |
| FIN-006 | Budget Management | Lifecycle 3 budgets created |
| HR-004 | Expense Claims | Lifecycle 4 claim submitted/approved |
| ASSET-002 | Asset Depreciation | Lifecycle 5 asset configured |
| PROG-005 | Task Tracking | Lifecycle 6 tasks created/completed |
| ME-002 | Task Completion | Lifecycle 6 task marked done |

### TIER 4 — Security Hardening (after TIER 1-3 complete)

| # | Action | Feature |
|---|--------|---------|
| S-1 | Enforce TOTP in company settings | GOV-005 |
| S-2 | Configure NDPR privacy policies | SAFE-004 |
| S-3 | Set up contract repository (hr_contract) | GOV-007 |

---

## Phase A.5 Exit Gate

Phase B (Beneficiary & Safeguarding) may begin only when:

| Gate | Criterion | How to verify |
|------|-----------|--------------|
| G1 | All TIER 0 Critical Risk items done | BEN-006 rule in DB; user groups corrected |
| G2 | All 7 Lifecycle tests pass their pass criteria | SQL counts match expected minimums |
| G3 | Donor Report (Lifecycle 8) produces correct PDF | PDF reviewed by `aliyu.umaru` |
| G4 | FEATURE_REGISTRY updated to reflect true status | No features marked COMPLETED without DB evidence |
| G5 | This scorecard shows Operational % >= 70% | OPERATIONAL_READINESS_SCORECARD recalculated |

---

*This document is the gating authority for Phase A → Phase B transition.*
*No Phase B feature (BEN-007 through SAFE-009) may be started until all gates above are confirmed.*
