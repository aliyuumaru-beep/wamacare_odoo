# PRODUCT_MATURITY_ROADMAP.md — WamaCare Product Maturity Roadmap

**Version:** 1.0 | **Date:** 2026-05-29
**Source:** Feature Registry (125 features), Capability Map, CBO Mandate DOCX, Transformation PPTX, database evidence

> This document replaces release-centric thinking with capability-centric maturity.
> WamaCare evolves through five phases. Each phase must be substantially complete before the next begins.
> Repository evidence determines current position. Strategy determines direction.

---

## The Maturity Model

```
Phase A: NGO/CBO Core          ████████████████████  SUBSTANTIALLY COMPLETE
Phase B: Beneficiary &          ████░░░░░░░░░░░░░░░░  FOUNDATION LAID
         Safeguarding
Phase C: Impact Management      ██░░░░░░░░░░░░░░░░░░  INFRASTRUCTURE ONLY
Phase D: Economic Empowerment   ░░░░░░░░░░░░░░░░░░░░  NOT STARTED
Phase E: Ecosystem Platform     ░░░░░░░░░░░░░░░░░░░░  DEFERRED
```

---

## Phase A — NGO/CBO Core

**Purpose:** Establish the operational foundation that allows the CBO to function with discipline, transparency, and accountability. Without Phase A, no other phase is possible.

**Target:** Any audit-ready donor visit can see organised operations, documented procurement, and financial accountability.

### Capabilities

| Domain | Key Capabilities | Status |
|--------|----------------|--------|
| Governance | Departments, RBAC, audit trail, PO approval, 2FA, fiscal year | ✅ 85% complete |
| HR | Employee records, org chart, expense claims, job positions | ✅ 70% complete |
| Project & Programme | 5 programmes, analytic accounts, budget module, calendar | ✅ 75% complete |
| Procurement | 17 vendors, LPO workflow, two-step approval, vendor bills | ✅ 90% complete |
| Finance | COA (70 accounts), NGN currency, VAT/WHT, full accounting suite | ✅ 90% complete |
| Inventory | Product catalogue (21 items) | 🔶 30% (stock module missing) |
| Assets | 3 assets registered, depreciation module | 🔶 60% (depreciation not configured) |
| Contracts | Nothing yet | 🔲 0% |

### Features Included (from FEATURE_REGISTRY)

GOV-001 through GOV-008, HR-001 through HR-007, PROG-001 through PROG-008,
DONOR-001 through DONOR-005, PROC-001 through PROC-007, FIN-001 through FIN-015,
ASSET-001 through ASSET-006, INV-001 through INV-005

### Dependencies

- PostgreSQL + Odoo 17 Community installed and running ✅
- Nigerian localisation (l10n_ng) applied ✅
- Core accounting configured ✅

### Expected Outcomes

- Every purchase goes through documented LPO approval workflow
- Every expense is charged to a programme analytic account
- Bank statements reconcile to system records
- Donor can see budget vs actual per programme at any point
- Staff records with skills and training documented
- Assets tracked with depreciation schedules

### Exit Criteria

- [ ] Bank account configured (FIN-012)
- [ ] Budget entries set for all 5 programmes (FIN-006 fully configured)
- [ ] Asset depreciation configured for 3 assets (ASSET-006)
- [ ] Contract repository operational (GOV-007)
- [ ] Beneficiary access restriction in place (BEN-006 — gate to Phase B)
- [ ] Admin password changed
- [ ] At least 1 complete LPO cycle executed in production
- [ ] At least 1 full expense cycle executed in production
- [ ] Phase 10 validation report passed ✅

**Current completion: ~78%**

---

## Phase B — Beneficiary & Safeguarding

**Purpose:** Protect the people WamaCare serves. Enable structured case management, safeguarding responses, and privacy-by-design.

**Prerequisite:** Phase A Exit Criteria must be met. Specifically: BEN-006 (access restriction) must be in place BEFORE any case management is built.

**Why this precedes Impact Measurement:** You cannot measure outcomes for beneficiaries whose records are not yet protected, structured, and trusted.

### Capabilities

| Domain | Key Capabilities | Status |
|--------|----------------|--------|
| Beneficiary Registry | Registration, tagging, geolocation, gender, anonymisation | 🔶 60% complete |
| Access Control | Record-level restrictions on beneficiary data | 🔲 0% |
| Case Management | Structured case notes and follow-up per beneficiary | 🔲 0% |
| Safeguarding Alerts | Flag, escalate, evidence, referral | 🔲 0% |
| Privacy Controls | NDPR compliance, consent tracking | 🔶 20% |
| Community Mobilizers | Profiles, credentials, assignment | 🔲 0% |

### Features Included

BEN-005 through BEN-009, SAFE-004 through SAFE-009,
HR-009 (Volunteer Management), HR-010 (Mobilizer Profiles),
GOV-009 (SOP Repository), GOV-010 (General Approval Workflow)

### Dependencies

- Phase A substantially complete ✅
- BEN-001 (Beneficiary Registration) COMPLETED ✅
- BEN-002 (Programme Tagging) COMPLETED ✅
- GOV-002 (RBAC) COMPLETED ✅
- BEN-006 (Access Restriction) must be COMPLETED before SAFE-005 begins

### Dependency Chain Within Phase B

```
BEN-006 Access Restriction
    ↓
BEN-007 Consent Tracking    BEN-008 Case Management
                                    ↓
                            BEN-009 Case Notes
                                    ↓
                            SAFE-005 Alert Flags
                                    ↓
                            SAFE-006 Escalation Workflow
                                ↙           ↘
                    SAFE-007 Evidence    SAFE-008 Referral
                                                ↓
                                        SAFE-009 Anon Portal
```

### Expected Outcomes

- Beneficiary data visible only to authorised staff
- Every beneficiary has documented consent for data processing
- Every safeguarding concern is flagged, escalated, and resolved on record
- Referral pathways to external agencies documented
- Community mobilizers profiled and tracked

### Exit Criteria

- [ ] BEN-006 Access restriction enforced (no Finance/HR access to beneficiary records)
- [ ] BEN-007 Consent recorded for all 13 existing beneficiaries
- [ ] BEN-008 Case management operational for at least 1 test case
- [ ] SAFE-005 Alert flag system tested end-to-end
- [ ] SAFE-006 Escalation workflow reaching Safeguarding Lead role
- [ ] SAFE-008 At least 1 external referral pathway documented
- [ ] NDPR privacy policy documented in system

**Current completion: ~18%**

---

## Phase C — Impact Management

**Purpose:** Move from "we did activities" to "we achieved measurable outcomes." Enable the organisation to quantify its impact per beneficiary, per programme, and per naira spent.

**Prerequisite:** Phase B exit criteria met. Specifically: beneficiary case management (BEN-008) must be operational before outcome indicators can be meaningfully measured.

**Why this follows Safeguarding:** Outcome data collected without safeguarding controls is ethically compromised. M&E built on unprotected beneficiary data has no integrity.

### Capabilities

| Domain | Key Capabilities | Status |
|--------|----------------|--------|
| M&E Framework | Programme structure, task completion, budget vs actual | ✅ 40% (infrastructure) |
| Outcome Indicators | Define, track, and report KPIs per programme | 🔲 0% |
| Cost-per-Beneficiary | Compute and trend programme efficiency | 🔲 0% |
| Impact Dashboards | Executive KPI view, programme outcomes | 🔶 25% (engine installed) |
| Donor Reporting | Budget utilisation + impact PDF | 🔶 30% (financial reports only) |
| Field Data Collection | Mobile data entry from field operations | 🔲 0% |

### Features Included

ME-005 through ME-008, EXEC-004 through EXEC-006,
PROG-009 (Outcome Indicators), PROG-010 (Field Activity Logs),
DONOR-006 (Multi-Donor Separation), DONOR-007 (Donor Budget Report), DONOR-008 (Donor Narrative)

### Dependency Chain Within Phase C

```
BEN-008 Case Management (Phase B exit)
    ↓
PROG-009 Outcome Indicator Definition
    ↓
ME-005 KPI Fields on Projects
    ↓                    ↓
ME-006 Cost-per-Ben    ME-007 Field Data
    ↓                    ↓
ME-008 Impact Report (PDF)
    ↓
EXEC-004 KPI Dashboard    DONOR-008 Donor Narrative
```

### Expected Outcomes

- Every programme has defined outcome indicators (e.g. "ANC visits completed: 450/500")
- Cost-per-beneficiary computable per quarter per programme
- Donor can receive a system-generated impact report, not a manually compiled narrative
- Executive dashboard shows programme health at a glance

### Exit Criteria

- [ ] ME-005 Outcome indicators defined for all 5 programmes
- [ ] ME-006 Cost-per-beneficiary calculated for at least 1 completed quarter
- [ ] ME-008 Impact report PDF generated and reviewed by leadership
- [ ] EXEC-004 Custom KPI dashboard operational
- [ ] DONOR-007 Donor budget report generated and reviewed by a donor

**Current completion: ~20%**

---

## Phase D — Economic Empowerment

**Purpose:** Transition WamaCare from a service-delivery organisation to a community enterprise hub. Enable women and girls to generate income, build businesses, and reduce dependency on external aid.

**Prerequisite:** Phase C substantially complete. Specifically: the organisation must be able to measure outcomes before it can track economic empowerment outcomes.

**Source evidence:** The PPTX "CBO Digital & Structural Transformation" explicitly defines Stage 3 as "Community Enterprise Hub — skills, livelihoods & local sustainability." The DOCX Part 1.8 defines: club identification, establishment, upgrading to cooperatives, skills training, and outcome tracking.

### Capabilities

| Domain | Key Capabilities | Status |
|--------|----------------|--------|
| Entrepreneurship Clubs | Registration, member management | 🔲 Not started |
| Training Programmes | Curricula, attendance, certification | 🔲 Not started |
| Cooperative Formation | Formalisation milestone tracking | 🔲 Not started |
| Livelihood Tracking | Income, employment, business outcomes | 🔲 Not started |
| Graduation Tracking | Exit from programme to independence | 🔲 Not started |

### Features Included

ENT-001 through ENT-007, HR-007 (Training Records as enabler),
HR-008 (Performance as model for empowerment tracking)

### Dependency Chain Within Phase D

```
Phase C Impact Measurement (exit)
    ↓
ENT-001 Entrepreneurship Programme
    ↓
ENT-002 Club Registration
    ↓
ENT-003 Member Management
    ↙                ↘
ENT-004 Training    ENT-005 Mentoring
    ↓
ENT-006 Cooperative Upgrade
    ↓
ENT-007 Livelihood Outcome Tracking
```

### Expected Outcomes

- Every entrepreneurship club registered with member list
- Every training session recorded with attendance
- Progression from informal group → registered cooperative documented
- Income outcomes tracked per graduate
- Programme can demonstrate reduced donor dependency over time

### Exit Criteria

- [ ] ENT-001 Entrepreneurship programme active with at least 3 clubs
- [ ] ENT-003 At least 20 members tracked across clubs
- [ ] ENT-004 At least 1 training programme completed and recorded
- [ ] ENT-007 At least 1 livelihood outcome recorded
- [ ] Phase D outcomes feeding into Phase C impact reports

**Current completion: 0%**

---

## Phase E — Ecosystem Platform

**Purpose:** Connect WamaCare to the broader community ecosystem — healthcare providers, safe houses, government systems, partner organisations, and the Digital Blood Bank. Transform from a single-CBO platform to a community infrastructure.

**Prerequisite:** Phase D in progress. Core platform must be proven, stable, and trusted before ecosystem integrations are built.

**Source evidence:** PPTX mentions "Social media & outreach campaign planning and analytics." DOCX mentions "Digital Blood Bank" and "Safe Houses" as ecosystem components. XLSX mentions healthcare provider linkages.

### Capabilities

| Domain | Key Capabilities | Status |
|--------|----------------|--------|
| Safe House Management | Intake, residence, exit tracking | ⬜ DEFERRED |
| Digital Blood Bank | Integration with blood bank system | 🔲 PLANNED |
| Healthcare Referral Network | Track referrals to health providers | 🔲 PLANNED |
| Partner Ecosystem | Shared data with partner CBOs/NGOs | ⬜ Not yet defined |
| Government Integration | FIRS, PENCOM, NHF statutory reporting | 🔶 PARTIAL (accounts exist) |

### Features Included

HEALTH-005 (Healthcare Referral), HEALTH-006 (Blood Bank),
SAFE-010 (Safe House), HR-012 (Payroll for government filing)

### Note on Safe House

Safe House management is NOT independent — it is the final destination of the safeguarding referral chain (SAFE-008 → SAFE-009 → SAFE-010). It cannot be built until Phase B's referral tracking (SAFE-008) is fully operational and the organisation has physical safe house facilities.

### Expected Outcomes

- WamaCare becomes a coordination platform, not just a management tool
- Blood bank requests traceable from programme need to fulfilment
- Safe house capacity and occupancy managed in system
- Partner organisations can share beneficiary referral data securely
- Statutory filings generated directly from system data

### Exit Criteria

- TBD — Phase E scope to be defined when Phase D reaches 50% completion

**Current completion: ~10% (vendor and asset records only)**

---

## Maturity Summary

| Phase | Name | Completion | Gate |
|-------|------|-----------|------|
| A | NGO/CBO Core | **78%** | Bank account, budgets, depreciation, BEN-006 |
| B | Beneficiary & Safeguarding | **18%** | BEN-006 first; then case mgmt and alerts |
| C | Impact Management | **20%** | Phase B case management exit |
| D | Economic Empowerment | **0%** | Phase C impact measurement operational |
| E | Ecosystem Platform | **10%** | Phase D in progress + partner readiness |

**Current position: Late Phase A → entering Phase B**

---

*This document supersedes release-centric thinking. Feature development must advance current phase exit criteria before opening the next phase.*
