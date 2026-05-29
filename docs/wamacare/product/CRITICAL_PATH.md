# CRITICAL_PATH.md — WamaCare Critical Path Analysis

**Version:** 1.0 | **Date:** 2026-05-29
**Source:** FEATURE_REGISTRY.md, FEATURE_DEPENDENCY_MAP.md, PRODUCT_MATURITY_ROADMAP.md, BUSINESS_CAPABILITY_MAP.md

> This document defines the minimum viable feature set for each level of organisational readiness.
> It is the answer to: "What is the absolute minimum we must build to reach each level?"

---

## Level 1 — Operational NGO/CBO

**Definition:** The organisation can run daily operations — staff, procurement, finance, programmes — with documentation, accountability, and auditability. A visiting auditor would find organised, traceable records.

**This is the exit criteria for Phase A.**

### Required Features

| Feature ID | Feature | Status | Gap |
|-----------|---------|--------|-----|
| GOV-001 | Department Structure | ✅ COMPLETED | — |
| GOV-002 | Role-Based Access Control | ✅ COMPLETED | — |
| GOV-003 | Audit Trail | ✅ COMPLETED | — |
| GOV-004 | Purchase Approval Workflow | ✅ COMPLETED | — |
| HR-001 | Employee Records | ✅ COMPLETED | — |
| HR-004 | Expense Claims | ✅ COMPLETED | — |
| FIN-001 | Chart of Accounts | ✅ COMPLETED | — |
| FIN-002 | NGN Functional Currency | ✅ COMPLETED | — |
| FIN-005 | Analytic Accounting | ✅ COMPLETED | — |
| FIN-006 | Budget Management | ✅ COMPLETED (module) | Budget entries not set |
| FIN-012 | Bank Account | 🔶 PARTIAL | Bank account not configured |
| FIN-013 | Bank Reconciliation | 🔶 PARTIAL | Depends on FIN-012 |
| PROG-001 | Programme Definition | ✅ COMPLETED | — |
| PROG-002 | Analytic Account per Programme | ✅ COMPLETED | — |
| PROG-003 | Budget per Programme | ✅ COMPLETED | Budget amounts not entered |
| PROC-001 | Vendor Management | ✅ COMPLETED | — |
| PROC-002 | Local Purchase Order | ✅ COMPLETED | — |
| PROC-003 | LPO Approval Workflow | ✅ COMPLETED | — |
| PROC-004 | Vendor Invoice Processing | ✅ COMPLETED | — |
| ASSET-001 | Asset Register | ✅ COMPLETED | — |
| ASSET-006 | Depreciation Configuration | 🔲 PLANNED | Must configure for 3 assets |
| INV-001 | Product Catalogue | ✅ COMPLETED | — |
| BEN-001 | Beneficiary Registration | ✅ COMPLETED | — |
| BEN-006 | Access Restriction | 🔲 PLANNED | **BLOCKER — must complete** |

### Blockers at Level 1

| Blocker | Action Required |
|---------|----------------|
| FIN-012 Bank account not configured | Add WamaCare bank account in Accounting settings |
| FIN-006 Budget entries not set | Enter programme budgets for all 5 programmes |
| ASSET-006 Depreciation not configured | Set depreciation method and rate for 3 assets |
| BEN-006 Beneficiary access not restricted | Create Odoo record rule on res.partner |
| Admin password still `admin/admin` | Change via Settings → Users |

### Level 1 Completion: **78%**

**Remaining effort:** ~8 hours of configuration (no coding required)

---

## Level 2 — Donor-Ready Organisation

**Definition:** A donor can visit, request a programme report, and receive a system-generated document showing: budgeted amount, actual expenditure, beneficiaries served, and programme activities completed. Every purchase has an approval trail. No manual spreadsheet is needed.

**This is the exit criteria for Phase A fully completed + Phase C partially complete.**

### Required Features (includes all Level 1, plus:)

| Feature ID | Feature | Status | Gap |
|-----------|---------|--------|-----|
| *All Level 1 features* | | | |
| GOV-007 | Contract Repository | 🔲 PLANNED | Staff contracts and donor MOUs must be stored |
| HR-007 | Training Records | 🔲 PLANNED | Donor-critical per XLSX checklist |
| PROG-005 | Task and Activity Tracking | 🔶 PARTIAL | Tasks must be loaded and completed |
| PROG-008 | Budget vs Actual Reporting | 🔲 PLANNED | Core donor-facing report |
| FIN-015 | Budget vs Actual Dashboard | 🔲 PLANNED | Executive view |
| DONOR-001 | Donor Contact Records | 🔶 PARTIAL | Donor must be in system with "Donor" tag |
| DONOR-002 | Grant Analytic Accounts | ✅ COMPLETED | — |
| DONOR-005 | MOU / Grant Agreement | 🔲 PLANNED | Agreement must be on file |
| DONOR-007 | Donor Budget Report | 🔲 PLANNED | Donor-specific PDF |
| PROC-007 | Budget Pre-Check | 🔲 PLANNED | Cannot commit funds over budget |
| ME-001 | M&E Programme | ✅ COMPLETED | — |
| ME-002 | Task Completion Tracking | ✅ COMPLETED | — |
| ME-003 | Budget vs Actual (M&E) | ✅ COMPLETED | — |
| EXEC-001 | Financial Dashboard | ✅ COMPLETED | — |
| EXEC-002 | Procurement Dashboard | ✅ COMPLETED | — |
| EXEC-003 | Programme Overview | ✅ COMPLETED | — |

### Blockers at Level 2

| Blocker | Action Required |
|---------|----------------|
| GOV-007 No contract repository | Install OCA Documents or alternative module |
| PROG-008 No budget vs actual report | Set budget entries → validate report generates |
| DONOR-005 No MOU stored | Upload donor MOUs to contract repository |
| DONOR-007 No donor report | Build donor-specific report template |
| PROC-007 No budget pre-check | Configure budget alert on purchase orders |
| HR-007 No training records | Create training events for staff — donor-critical |

### Level 2 Completion: **52%**

**Remaining effort:** ~3-5 days of configuration and module setup

---

## Level 3 — Safeguarding-Ready Organisation

**Definition:** Every beneficiary record is protected. Every safeguarding concern is flagged, escalated, documented, and referred. The organisation can demonstrate to any donor, government, or NGO reviewer that it has a functioning safeguarding system — not just a policy.

**This is the exit criteria for Phase B.**

### Required Features (includes all Level 2, plus:)

| Feature ID | Feature | Status | Gap |
|-----------|---------|--------|-----|
| *All Level 2 features* | | | |
| BEN-006 | Access Restriction | 🔲 PLANNED | **Gate — must be first** |
| BEN-007 | Beneficiary Consent | 🔲 PLANNED | Consent for existing 13 beneficiaries |
| BEN-008 | Case Management | 🔲 PLANNED | Custom Odoo model or structured workflow |
| BEN-009 | Case Notes | 🔲 PLANNED | Timestamped notes per case |
| SAFE-004 | NDPR Privacy | 🔶 PARTIAL | Privacy policies not yet configured |
| SAFE-005 | Safeguarding Alert Flags | 🔲 PLANNED | **Critical feature** |
| SAFE-006 | Case Escalation | 🔲 PLANNED | Must reach Safeguarding Lead |
| SAFE-007 | Evidence Upload | 🔲 PLANNED | Files attached to escalated cases |
| SAFE-008 | Referral Pathway | 🔲 PLANNED | Documented referral to external agencies |
| HR-009 | Volunteer Management | 🔲 PLANNED | Volunteers tracked separately |
| HR-010 | Mobilizer Profiles | 🔲 PLANNED | Credential-verified mobilizers |

### Dependency Chain to Level 3

```
BEN-006 → BEN-007 → BEN-008 → BEN-009 → SAFE-005 → SAFE-006 → SAFE-007
                                                              → SAFE-008
```

### Blockers at Level 3

| Blocker | Action Required | Effort |
|---------|----------------|--------|
| BEN-006 no access restriction | Odoo record rules on res.partner | 2 hours |
| BEN-008 no case management | Custom model or structured project task | 1-2 days |
| SAFE-005 no alert flags | Custom field + automated action | 1 day |
| SAFE-006 no escalation | Odoo automated action + email | 1 day |

### Level 3 Completion: **28%**

**Remaining effort:** ~5-8 days (mix of configuration and custom module work)

---

## Level 4 — Sustainable Empowerment Organisation

**Definition:** The CBO can demonstrate measurable impact AND a pathway to reduced donor dependency. Outcome indicators are tracked per programme, cost-per-beneficiary is computed, and at least one entrepreneurship cluster is operational.

**This is the exit criteria for Phase C substantially complete + Phase D entry.**

### Required Features (includes all Level 3, plus:)

| Feature ID | Feature | Status | Gap |
|-----------|---------|--------|-----|
| *All Level 3 features* | | | |
| ME-005 | Outcome Indicators | 🔲 PLANNED | Define KPIs for all 5 programmes |
| ME-006 | Cost-per-Beneficiary | 🔲 PLANNED | Compute per quarter |
| ME-007 | Field Data Collection | 🔲 PLANNED | Mobile-friendly field entry |
| ME-008 | Impact Report PDF | 🔲 PLANNED | Donor-ready summary |
| EXEC-004 | Custom KPI Dashboard | 🔲 PLANNED | Leadership visibility |
| EXEC-005 | Beneficiary Statistics | 🔲 PLANNED | Beneficiary count by area/programme |
| DONOR-008 | Donor Narrative Report | 🔲 PLANNED | Narrative + data combined |
| ENT-001 | Entrepreneurship Programme | 🔲 PLANNED | Activate entrepreneurship |
| ENT-002 | Club Registration | 🔲 PLANNED | At least 3 clubs |
| ENT-003 | Member Management | 🔲 PLANNED | At least 20 members |
| ENT-007 | Livelihood Outcome Tracking | 🔲 PLANNED | Income/employment outcomes |

### Level 4 Completion: **15%**

**Remaining effort:** ~4-6 weeks (significant new feature development)

---

## Summary Table

| Level | Name | Completion | Key Blocker | Effort to Unblock |
|-------|------|-----------|-------------|-------------------|
| 1 | Operational NGO/CBO | **78%** | BEN-006 (access restriction) | ~8 hours config |
| 2 | Donor-Ready | **52%** | PROG-008 (budget vs actual) | ~3-5 days |
| 3 | Safeguarding-Ready | **28%** | BEN-008 (case management) | ~1-2 weeks |
| 4 | Sustainable Empowerment | **15%** | ME-005 (outcome indicators) | ~4-6 weeks |

---

## Critical Path Sequence

The absolute minimum sequence to advance through all 4 levels:

```
Step 1: BEN-006 (Access Restriction)      → unlocks Phase B, Level 1 complete
Step 2: FIN-012 + FIN-006 config          → unlocks bank reconciliation, budgets
Step 3: ASSET-006 (Depreciation)          → completes asset management
Step 4: GOV-007 (Contract Repository)     → unlocks DONOR-005, GOV-008
Step 5: PROG-008 (Budget vs Actual)       → Level 2 milestone
Step 6: DONOR-007 (Donor Report)          → Level 2 complete
Step 7: BEN-008 (Case Management)         → unlocks safeguarding chain
Step 8: SAFE-005 + SAFE-006 (Alerts+Escalation) → Level 3 core
Step 9: SAFE-008 (Referral)               → Level 3 complete
Step 10: ME-005 (Outcome Indicators)      → unlocks Phase C
Step 11: ME-006 (Cost-per-Beneficiary)    → impact proof
Step 12: ME-008 (Impact Report)           → Level 4 core
Step 13: ENT-001→ENT-007                  → Level 4 complete
```

---

*Critical path is derived from FEATURE_REGISTRY.md and FEATURE_DEPENDENCY_MAP.md. Any deviation must be recorded in DECISION_LOG.md.*
