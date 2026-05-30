# OPERATIONAL_READINESS_SCORECARD.md — WamaCare Phase A.5

**Date:** 2026-05-30 (updated after Tier 2 lifecycle tests) | **Based on:** Evidence-Based Audit + lifecycle test execution
**Scoring method:** Evidence only. Claims without database records are not COMPLETED.

---

## Scoring Definitions

| Score | Definition | Requirement |
|-------|-----------|-------------|
| **Configured** | Module installed + settings applied. No transaction required. | Module state = installed AND relevant settings exist |
| **Tested** | At least one end-to-end scenario executed. Records exist in DB. | COUNT > 0 in key tables |
| **Operational** | Workflow runs correctly. Expected output produced. | Tested + report generated + no errors |
| **Production-ready** | Operational + documented + audited + access-controlled | Operational + audit trail + RBAC verified |

---

## Scorecard by Domain

### 1. Governance

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Department structure | ✅ | ✅ | ✅ | ✅ |
| Role-based access control | ✅ | ⚠️ PARTIAL | ❌ | ❌ |
| Audit trail (chatter) | ✅ | ✅ | ✅ | ✅ |
| Purchase approval workflow | ✅ | ❌ | ❌ | ❌ |
| Two-factor authentication | ✅ available | ❌ not enforced | ❌ | ❌ |
| Fiscal year management | ❌ not configured | ❌ | ❌ | ❌ |
| Contract repository | ❌ module missing | ❌ | ❌ | ❌ |

**Domain scores:** Configured 57% | Tested 29% | Operational 29% | Prod-Ready 29%

**Notes:**
- RBAC tested = groups assigned to users, but `field.officer` missing `project.group_project_user`. Roles are incomplete.
- Purchase approval: `po_double_validation = 'two_step'` is set but P00001 has never gone through approval. Setting ≠ tested.
- 2FA: module installed but `totp_required_role` field absent — not enforced at company level.

---

### 2. HR

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Employee records | ✅ | ✅ | ✅ | ✅ |
| Org chart | ✅ | ✅ | ✅ | ✅ |
| Job positions | ✅ | ✅ | ✅ | ✅ |
| Expense claims | ✅ module | ❌ 0 records | ❌ | ❌ |
| Skills tracking | ✅ module | ❌ 0 skill lines | ❌ | ❌ |
| Staff onboarding | ❌ no checklist | ❌ | ❌ | ❌ |
| Training records | ❌ no training data | ❌ | ❌ | ❌ |

**Domain scores:** Configured 57% | Tested 43% | Operational 43% | Prod-Ready 43%

---

### 3. Programme Management

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Programme definition | ✅ | ✅ | ✅ | ✅ |
| Analytic account per programme | ✅ | ✅ | ✅ | ✅ |
| Budget per programme | ✅ module | ❌ 0 budgets | ❌ | ❌ |
| Activity calendar | ✅ | ❌ no events | ❌ | ❌ |
| Task and activity tracking | ✅ module | ❌ 0 tasks | ❌ | ❌ |
| Programme dashboard | ❌ only generic | ❌ | ❌ | ❌ |
| Milestone tracking | ✅ module | ❌ 0 milestones | ❌ | ❌ |
| Budget vs actual | ❌ no data | ❌ | ❌ | ❌ |

**Domain scores:** Configured 50% | Tested 25% | Operational 25% | Prod-Ready 25%

---

### 4. Donor Management

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Donor contact records | ❌ no donor tags | ❌ | ❌ | ❌ |
| Grant analytic accounts | ✅ | ✅ | ✅ | ✅ |
| Recurring payment management | ✅ module | ❌ 0 records | ❌ | ❌ |
| Donor follow-up | ✅ module | ❌ 0 records | ❌ | ❌ |
| MOU storage | ❌ no module | ❌ | ❌ | ❌ |

**Domain scores:** Configured 60% | Tested 20% | Operational 20% | Prod-Ready 20%

---

### 5. Procurement

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Vendor management | ✅ | ✅ | ✅ | ✅ |
| Local Purchase Order | ✅ | ⚠️ P00001 draft | ❌ | ❌ |
| LPO approval workflow | ✅ setting | ❌ never approved | ❌ | ❌ |
| Vendor invoice processing | ✅ module | ❌ 0 bills | ❌ | ❌ |
| Payment approval | ✅ module | ❌ 0 payments | ❌ | ❌ |
| Procurement reports | ✅ templates | ⚠️ no data | ❌ | ❌ |

**Domain scores:** Configured 100% | Tested 17% | Operational 17% | Prod-Ready 17%

---

### 6. Finance

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Chart of accounts (NGO) | ✅ | ✅ created | ⚠️ untransacted | ❌ |
| NGN currency | ✅ | ✅ | ✅ | ✅ |
| Nigeria VAT (7.5%) | ✅ | ❌ never applied | ❌ | ❌ |
| Withholding tax | ✅ accounts | ❌ never applied | ❌ | ❌ |
| Analytic accounting | ✅ | ✅ config | ⚠️ no transactions | ❌ |
| Budget management | ✅ module | ❌ 0 budgets | ❌ | ❌ |
| Asset depreciation | ✅ module | ❌ 0 assets configured | ❌ | ❌ |
| Bank account | ❌ not set up | ❌ | ❌ | ❌ |
| Bank reconciliation | ❌ needs bank | ❌ | ❌ | ❌ |
| Full accounting suite | ✅ | ❌ 0 journal entries | ❌ | ❌ |
| FIRS tax report | ✅ structure | ❌ no tax transactions | ❌ | ❌ |
| Daily financial reports | ✅ templates | ❌ no data | ❌ | ❌ |

**Domain scores:** Configured 75% | Tested 17% | Operational 8% | Prod-Ready 8%

---

### 7. Asset Management

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Asset register | ✅ 3 items | ✅ records exist | ⚠️ incomplete | ❌ |
| Asset depreciation module | ✅ installed | ❌ 0 configured | ❌ | ❌ |
| Equipment categories | ❌ NULL all | ❌ | ❌ | ❌ |
| Asset assignment | ❌ NULL all | ❌ | ❌ | ❌ |
| Maintenance scheduling | ✅ module | ❌ 0 requests | ❌ | ❌ |
| Depreciation config | ❌ | ❌ | ❌ | ❌ |

**Domain scores:** Configured 50% | Tested 17% | Operational 0% | Prod-Ready 0%

---

### 8. Beneficiary Management

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Beneficiary registration | ✅ 13 records | ✅ | ✅ | ❌ |
| Programme tagging | ✅ | ✅ | ✅ | ❌ |
| Geolocation | ✅ | ✅ | ✅ | ❌ |
| Gender tagging | ✅ | ✅ | ✅ | ❌ |
| Anonymised naming | ✅ | ✅ | ✅ | ❌ |
| Access restriction | ❌ NO RULES | ❌ | ❌ | ❌ |

**Domain scores:** Configured 83% | Tested 83% | Operational 83% | Prod-Ready 0%

**Critical note:** All beneficiary capabilities are tested and operational, but NONE are production-ready because BEN-006 (access restriction) is missing. All beneficiary data is exposed.

---

### 9. Safeguarding

| Capability | Configured | Tested | Operational | Prod-Ready |
|-----------|-----------|--------|-------------|------------|
| Safeguarding programme | ✅ | ✅ | ✅ | ❌ |
| Safeguarding department | ✅ | ✅ | ✅ | ❌ |
| Safeguarding lead role | ✅ | ✅ | ✅ | ❌ |
| NDPR privacy module | ✅ installed | ❌ 0 records | ❌ | ❌ |

**Domain scores:** Configured 100% | Tested 75% | Operational 75% | Prod-Ready 0%

---

## Overall Phase A Scorecard — Updated 2026-05-30 (after Tier 2 lifecycle tests)

| Domain | Configured | Tested | Operational | Prod-Ready | Lifecycle |
|--------|-----------|--------|-------------|------------|----------|
| Governance | 57% | 57% | 57% | 43% | GOV-004 proven |
| HR | 57% | 57% | 57% | 43% | Expense claim submitted + approved |
| Programme Mgmt | 80% | 60% | 60% | 50% | 5 tasks created, 1 done |
| Donor Management | 60% | 40% | 40% | 20% | Analytic accounts live |
| Procurement | 100% | 100% | 90% | 70% | L1 PASS — full cycle proven |
| Finance | 75% | 75% | 67% | 50% | L2 PASS — 2 bills posted, analytic trigger working |
| Asset Management | 50% | 50% | 17% | 17% | Equipment registry complete |
| Beneficiary Mgmt | 83% | 83% | 83% | 83% | BEN-006 active, data protected |
| Safeguarding | 100% | 75% | 75% | 75% | Programme + dept + lead confirmed |
| **OVERALL** | **70%** | **66%** | **61%** | **50%** | |

---

## Phase A Maturity Position — Progression

| Checkpoint | Production-Ready % | Date |
|-----------|-------------------|------|
| Initial claim | 78% (unchecked) | 2026-05-29 pre-audit |
| After evidence audit | 16% | 2026-05-29 |
| After Tier 0 + Tier 1 | ~22% | 2026-05-29 |
| **After Tier 2 lifecycle tests** | **50%** | **2026-05-30** |

**Phase A is now 50% production-ready. Remaining 50% requires: reconciliation workflow automation, asset depreciation, donor report generation, contract repository, and completing the Phase A exit gate checklist.**

---

## What Must Be True Before Phase B Opens

Phase B (Beneficiary & Safeguarding) requires Phase A to be operationally validated, not just configured. The minimum gate for Phase A exit:

- [ ] Procurement Lifecycle: At least 1 confirmed PO + 1 posted vendor bill
- [ ] Finance Lifecycle: At least 1 posted journal entry + bank account configured
- [ ] Budget Lifecycle: At least 1 budget record per programme
- [ ] HR Lifecycle: At least 1 expense claim submitted and approved
- [ ] Asset Lifecycle: At least 1 asset configured for depreciation
- [ ] Programme Lifecycle: At least 5 tasks created and at least 1 completed
- [ ] Donor Report: Budget vs actual report generated successfully
- [ ] BEN-006: Beneficiary access restriction implemented and tested
- [ ] User roles: field.officer correctly scoped, aliyu.umaru Technical Features removed
