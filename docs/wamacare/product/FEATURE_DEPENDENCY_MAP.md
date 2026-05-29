# FEATURE_DEPENDENCY_MAP.md — WamaCare Feature Dependency Map

**Version:** 1.0 | **Date:** 2026-05-29
**Source:** FEATURE_REGISTRY.md, PRODUCT_MATURITY_ROADMAP.md, BUSINESS_CAPABILITY_MAP.md, database evidence

> This document maps what must be built before each feature can be started.
> A future AI or developer must read this before planning any feature work.
> "Blocks" = features that cannot be started until this feature is complete.

---

## Classification Definitions

| Class | Meaning |
|-------|---------|
| FOUNDATIONAL | Everything else depends on this. Build first. Failure here stops everything. |
| IMPORTANT | Enables a cluster of other features. Should be built early in its phase. |
| OPTIONAL | Adds value but does not gate other features. Build when resources allow. |
| FUTURE | Cannot be built until multiple preceding features are complete. |

---

## Dependency Map

### GOV-001 — Department Structure
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | Odoo HR module installed |
| Blocks | HR-001, GOV-002, all user role assignments |
| Criticality | Without departments, no user can be assigned to a role or team. |

### GOV-002 — Role-Based Access Control
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | GOV-001 (departments), HR-001 (employees) |
| Blocks | BEN-006 (access restriction needs defined roles), SAFE-005 (alerts need restricted access to work) |
| Criticality | Without RBAC, access restriction on sensitive data is impossible. |

### GOV-003 — Audit Trail (Chatter)
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | mail module (base dependency) |
| Blocks | Nothing — but all accountability features depend on it being present |
| Criticality | Every change to every record must be logged. This is non-negotiable for donor accountability. |

### GOV-004 — Purchase Approval Workflow
**Class:** IMPORTANT | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | PROC-001 (vendors), FIN-001 (COA), PROC-002 (LPO) |
| Blocks | PROC-007 (budget pre-check uses approval hooks), DONOR-003 (recurring payments need approval framework) |
| Criticality | Without approval workflow, procurement can be committed without authorisation. |

### GOV-007 — Contract Repository
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | Documents module (OCA or Enterprise), GOV-001 |
| Blocks | GOV-008 (expiry alerts), PROC-009 (contract-linked procurement), DONOR-005 (MOU storage) |
| Criticality | Contracts govern most relationships. Without a repository, documents are offline and untracked. |

---

### HR-001 — Employee Records
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | GOV-001 (departments) |
| Blocks | HR-002, HR-003, HR-004, HR-007, HR-008, HR-010, SAFE-003 |
| Criticality | Without employee records, no role assignment, no expense claims, no safeguarding lead role. |

### HR-007 — Training Records
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | HR-001, HR-005 (skills tracking) |
| Blocks | HR-010 (mobilizer credential verification requires training records), ENT-004 (training programme tracking uses same structure) |
| Criticality | Donor-critical per XLSX checklist. All trainings must be documented. |

### HR-010 — Community Mobilizer Profiles
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | HR-001, HR-007 (training), BEN-001 (mobilizers work with beneficiaries) |
| Blocks | SAFE-008 (referrals involve mobilizers as first contacts), PROG-010 (field activity logs involve mobilizers) |
| Criticality | Mobilizers are the primary interface between CBO and beneficiaries. |

---

### FIN-001 — Chart of Accounts (NGO)
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | account module, l10n_ng |
| Blocks | FIN-002 through FIN-015, PROG-002, DONOR-002, PROC-004 |
| Criticality | Every financial transaction depends on a correctly structured COA. |

### FIN-005 — Analytic Accounting
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | FIN-001, PROG-001 |
| Blocks | PROG-002, FIN-006, PROG-008, FIN-015, DONOR-002, ME-003, ME-006, DONOR-007 |
| Criticality | Without analytic accounting, no expense can be attributed to a programme. Donor accountability fails. |

### FIN-006 — Budget Management
**Class:** IMPORTANT | **Status:** COMPLETED (module) / PARTIAL (budget entries)
| Field | Value |
|-------|-------|
| Depends On | FIN-005 (analytic accounting), PROG-001 |
| Blocks | PROC-007 (budget pre-check), PROG-008 (budget vs actual), FIN-015 (dashboard), ME-006 (cost-per-beneficiary) |
| Criticality | Budget entries must be set before any budget vs actual reporting is meaningful. |

### FIN-012 — Bank Account Configuration
**Class:** IMPORTANT | **Status:** PARTIAL
| Field | Value |
|-------|-------|
| Depends On | FIN-001 (COA), account module |
| Blocks | FIN-013 (bank reconciliation), payment processing |
| Criticality | Without a bank account, vendor payments cannot be properly recorded or reconciled. |

---

### PROG-001 — Programme Definition
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | project module |
| Blocks | PROG-002, PROG-003, PROG-005, BEN-002, ME-001, ME-002, DONOR-002 |
| Criticality | All activities, expenses, and outcomes are linked to a programme. Without programmes, nothing is attributed. |

### PROG-002 — Analytic Account per Programme
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | PROG-001, FIN-005 |
| Blocks | PROG-008 (reporting), FIN-015 (dashboard), ME-003, DONOR-007 |
| Criticality | The link between programme activity and financial cost. Without this, donor accountability is impossible. |

### PROG-008 — Budget vs Actual Reporting
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | PROG-002, FIN-006 (budget entries set), PROC-004 (bills recorded) |
| Blocks | FIN-015 (dashboard), DONOR-007 (donor report), ME-006 (cost-per-ben uses this data) |
| Criticality | First thing a donor asks for: how much was budgeted and how much was spent? |

---

### BEN-001 — Beneficiary Registration
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | contacts module |
| Blocks | BEN-002, BEN-003, BEN-004, BEN-005, BEN-006, BEN-007, BEN-008, BEN-009, SAFE-005, ME-006 |
| Criticality | All beneficiary-related features are impossible without a beneficiary record. |

### BEN-002 — Programme Tagging
**Class:** FOUNDATIONAL | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | BEN-001, PROG-001 |
| Blocks | BEN-008 (case management needs programme context), ME-005 (indicators need programme-beneficiary link), EXEC-005 |
| Criticality | Without programme tagging, you cannot know which beneficiaries belong to which programme. |

### BEN-006 — Access Restriction
**Class:** FOUNDATIONAL (for Phase B) | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | BEN-001, GOV-002 (RBAC must be configured) |
| Blocks | SAFE-005 (alerts are useless if unauthorised users can see the records), BEN-007 (consent needs access control), all Phase B features |
| Criticality | CRITICAL GATE. Without this, every case management, safeguarding, and consent feature exposes sensitive data to all users. BEN-006 is the Phase A → Phase B gate. |

### BEN-008 — Case Management
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | BEN-001, BEN-006, BEN-009 |
| Blocks | SAFE-005 (flags are added to cases), SAFE-006 (escalation is a case workflow), SAFE-007 (evidence attaches to cases), ME-005 (outcomes recorded per case) |
| Criticality | Without structured case management, safeguarding has no record system. Every incident is undocumented. |

---

### SAFE-001 — Safeguarding Programme
**Class:** IMPORTANT | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | PROG-001 |
| Blocks | SAFE-002, SAFE-003, SAFE-005 (must have programme to flag against) |
| Criticality | Establishes safeguarding as a formal CBO programme — not just a policy. |

### SAFE-004 — NDPR Privacy Module
**Class:** IMPORTANT | **Status:** PARTIAL
| Field | Value |
|-------|-------|
| Depends On | privacy_lookup module (installed) |
| Blocks | BEN-007 (consent tracking uses privacy framework) |
| Criticality | Legal requirement for Nigerian organisations processing personal data. |

### SAFE-005 — Safeguarding Alert Flags
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | BEN-001, BEN-006, BEN-008, SAFE-001, SAFE-002, SAFE-003 |
| Blocks | SAFE-006 (escalation starts from a flag) |
| Criticality | The primary tool by which harm is detected and acted upon. Cannot be skipped. |

### SAFE-006 — Case Escalation Workflow
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | SAFE-005, GOV-002 (Safeguarding Lead role), BEN-008 |
| Blocks | SAFE-007 (evidence attaches to escalated case), SAFE-008 (referral follows escalation) |
| Criticality | Detection without escalation is failure. Flags that go nowhere protect no one. |

### SAFE-008 — Referral Pathway Tracking
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | SAFE-006, HR-010 (mobilizers make referrals), HEALTH-001 (referral destinations) |
| Blocks | SAFE-009 (anonymous portal generates referrals), SAFE-010 (safe house is a referral destination) |
| Criticality | Without documented referral pathways, the CBO cannot prove it acted on safeguarding concerns. |

---

### ME-001 — M&E Programme
**Class:** IMPORTANT | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | PROG-001 |
| Blocks | ME-002, ME-005, ME-006 |
| Criticality | Establishes M&E as a formal programme. Without it, measurement is ad hoc. |

### ME-005 — Outcome Indicator Fields
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | ME-001, PROG-001, BEN-008 (case data feeds indicators), PROG-009 |
| Blocks | ME-006 (cost-per-ben needs indicator data), ME-008 (impact report uses indicators) |
| Criticality | Without defined indicators, there is nothing to measure. This is the foundation of Phase C. |

### ME-006 — Cost-per-Beneficiary
**Class:** IMPORTANT | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | ME-005, FIN-006 (budget entries), PROG-002 (analytic), BEN-001 (count) |
| Blocks | ME-008 (impact report includes cost efficiency), EXEC-004 (KPI dashboard), DONOR-008 |
| Criticality | The single most powerful number for donor accountability. "₦X per beneficiary served." |

### ME-008 — Impact Report (PDF)
**Class:** FUTURE | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | ME-005, ME-006, ME-007 (field data), PROG-008, SAFE-006 (safeguarding data) |
| Blocks | DONOR-008 (narrative uses impact data) |
| Criticality | The deliverable that justifies continued donor funding. |

---

### ENT-001 — Entrepreneurship Programme
**Class:** IMPORTANT (for Phase D) | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | PROG-001, BEN-001 (beneficiaries become entrepreneurs), ME-001 (outcomes tracked) |
| Blocks | ENT-002 through ENT-007 (all ENT features depend on programme existing) |
| Criticality | Cannot track clubs, members, or outcomes without a programme container. |

### ENT-007 — Livelihood Outcome Tracking
**Class:** FUTURE | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | ENT-001, ENT-002, ENT-003, ENT-004, ME-005 |
| Blocks | Nothing within current scope (but feeds Phase E sustainability metrics) |
| Criticality | The ultimate proof of economic empowerment. "X women now run registered businesses." |

---

### HEALTH-001 — Healthcare Vendor Network
**Class:** IMPORTANT | **Status:** COMPLETED
| Field | Value |
|-------|-------|
| Depends On | contacts module, PROC-001 |
| Blocks | HEALTH-002, HEALTH-004, HEALTH-005, SAFE-008 (health providers are referral targets) |
| Criticality | Healthcare providers must be in the system before referrals or procurement can happen. |

### HEALTH-006 — Digital Blood Bank
**Class:** FUTURE | **Status:** PLANNED
| Field | Value |
|-------|-------|
| Depends On | HEALTH-001, HEALTH-005 (referral network), Phase D substantially complete |
| Blocks | Nothing — ecosystem feature |
| Criticality | Long-term ecosystem play. Not critical for Phase A–C delivery. |

---

## Dependency Graph Summary

```
FOUNDATIONAL LAYER (must exist first):
──────────────────────────────────────
GOV-001 Departments
  └→ HR-001 Employees
       └→ GOV-002 RBAC
            └→ BEN-006 Access Restriction  ← PHASE A→B GATE
                 └→ Phase B begins

FIN-001 Chart of Accounts
  └→ FIN-005 Analytic Accounting
       └→ PROG-002 Programme-Analytic Link
            └→ PROG-008 Budget vs Actual
                 └→ ME-006 Cost-per-Beneficiary

PROG-001 Programme Definition
  └→ BEN-002 Programme Tagging
       └→ BEN-001 Beneficiary Registration
            └→ BEN-008 Case Management  ← PHASE B CORE
                 └→ SAFE-005 Alert Flags
                      └→ SAFE-006 Escalation
                           └→ SAFE-008 Referral  ← PHASE E entry

ME-001 M&E Programme
  └→ ME-005 Outcome Indicators  ← PHASE C CORE
       └→ ME-006 Cost-per-Ben
            └→ ME-008 Impact Report
                 └→ DONOR-008 Donor Narrative

ENT-001 Entrepreneurship Programme  ← PHASE D ENTRY
  └→ ENT-002 Club Registration
       └→ ENT-003 Member Management
            └→ ENT-007 Livelihood Outcomes  ← PHASE E feeds
```

---

## Top Dependency Bottlenecks

Features that block the most other features — highest leverage for unblocking:

| Rank | Feature | Blocks Count | Current Status | Impact of Delay |
|------|---------|------------|----------------|-----------------|
| 1 | BEN-006 Access Restriction | 9+ features | PLANNED | Phase B cannot start |
| 2 | BEN-008 Case Management | 5 features | PLANNED | Safeguarding has no record system |
| 3 | SAFE-005 Alert Flags | 3 features | PLANNED | No safeguarding detection mechanism |
| 4 | ME-005 Outcome Indicators | 3 features | PLANNED | Phase C cannot start |
| 5 | FIN-006 Budget Entries | 4 features | PARTIAL | No budget vs actual possible |
| 6 | GOV-007 Contract Repository | 3 features | PLANNED | MOUs and contracts untracked |
| 7 | PROG-008 Budget vs Actual | 3 features | PLANNED | Donor accountability incomplete |
| 8 | SAFE-006 Escalation Workflow | 3 features | PLANNED | Alerts go nowhere |
| 9 | HR-007 Training Records | 2 features | PLANNED | XLSX donor-critical item unmet |
| 10 | ME-006 Cost-per-Beneficiary | 3 features | PLANNED | Impact efficiency unmeasurable |
