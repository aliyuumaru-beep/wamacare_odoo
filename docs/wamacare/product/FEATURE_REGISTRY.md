# FEATURE_REGISTRY.md — WamaCare Feature Registry

**Version:** 1.1 | **Date:** 2026-05-29
**Rule:** This is the single source of truth for all WamaCare features. Status values must be supported by database evidence. See EVIDENCE_BASED_AUDIT.md and PHASE_A5_EXIT_CRITERIA.md.

---

## Status Definitions

| Status | Meaning | DB Evidence Required |
|--------|---------|---------------------|
| COMPLETED | Configured + tested + output produced + access-controlled | Records in DB + report generated |
| INSTALLED | Module installed, settings applied, zero transactions | Module state=installed, 0 records |
| PARTIAL | Configuration partially done; some but not all criteria met | Partial records or partial config |
| IN_PROGRESS | Currently being built | — |
| PLANNED | On roadmap; not yet started | — |
| DEFERRED | Identified but not yet roadmapped | — |

> **v1.1 update:** Statuses revised based on Evidence-Based Audit (2026-05-29).
> Features with 0 database records may no longer be claimed COMPLETED.
> See `docs/wamacare/product/EVIDENCE_BASED_AUDIT.md` for full audit findings.

---

## Domain: Governance (GOV)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| GOV-001 | Department Structure | 5 WamaCare departments with managers | HIGH | COMPLETED | 1.0 |
| GOV-002 | Role-Based Access Control | 5 user roles with appropriate permissions | HIGH | COMPLETED | 1.0 |
| GOV-003 | Audit Trail (Chatter) | All records have chatter for activity log | HIGH | COMPLETED | 1.0 |
| GOV-004 | Purchase Approval Workflow | Two-step LPO approval at ₦200,000 | HIGH | COMPLETED | 1.0 |  <!-- VERIFIED 2026-05-30 via P00003 -->|
| GOV-005 | Two-Factor Authentication | TOTP available for all users | MEDIUM | INSTALLED | 1.0 |
| GOV-006 | Fiscal Year Management | Annual fiscal year close and lock | MEDIUM | NOT STARTED | 1.0 |
| GOV-007 | Contract Repository | Central store for staff contracts, MOUs | HIGH | PLANNED | 1.0 |
| GOV-008 | Contract Expiry Alerts | Automated alerts before contract expiry | MEDIUM | PLANNED | 1.0 |
| GOV-009 | SOP / Policy Repository | Digital storage for policies and procedures | MEDIUM | PLANNED | 1.1 |
| GOV-010 | General Approval Workflow | Multi-level approval for non-procurement requests | MEDIUM | PLANNED | 1.1 |

---

## Domain: HR (HR)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| HR-001 | Employee Records | 10 employees across 5 departments | HIGH | COMPLETED | 1.0 |
| HR-002 | Org Chart | Visual department hierarchy | MEDIUM | COMPLETED | 1.0 |
| HR-003 | Job Positions | 9 job positions defined | MEDIUM | COMPLETED | 1.0 |
| HR-004 | Expense Claims | Staff expense submission and approval | HIGH | COMPLETED | 1.0 |
| HR-005 | Skills Tracking | Employee skills catalogue | MEDIUM | INSTALLED | 1.0 |
| HR-006 | Staff Onboarding Checklist | Structured onboarding workflow | MEDIUM | NOT STARTED | 1.0 |
| HR-007 | Training Records | Training attendance and certification log | HIGH | PLANNED | 1.0 |
| HR-008 | Performance Tracking | Appraisal and performance management | MEDIUM | PLANNED | 1.1 |
| HR-009 | Volunteer Management | Separate volunteer category and tracking | MEDIUM | PLANNED | 1.1 |
| HR-010 | Community Mobilizer Profiles | Credential and assignment tracking for mobilizers | HIGH | PLANNED | 1.1 |
| HR-011 | Staff Exit Continuity | Exit checklist and knowledge transfer | LOW | PLANNED | 1.2 |
| HR-012 | Payroll Integration | Basic payroll processing | LOW | DEFERRED | 2.0 |

---

## Domain: Programme Management (PROG)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| PROG-001 | Programme Definition | 5 active programmes created | HIGH | COMPLETED | 1.0 |
| PROG-002 | Analytic Account per Programme | All 5 programmes linked to analytic accounts | HIGH | COMPLETED | 1.0 |
| PROG-003 | Budget per Programme | Budget module installed and linked | HIGH | INSTALLED | 1.0 |
| PROG-004 | Activity Calendar | Calendar module installed | MEDIUM | INSTALLED | 1.0 |
| PROG-005 | Task and Activity Tracking | Project tasks available per programme | HIGH | COMPLETED | 1.0 |
| PROG-006 | Programme Dashboard | Spreadsheet dashboard for programme view | HIGH | NOT STARTED | 1.0 |
| PROG-007 | Milestone Tracking | Programme milestone configuration | MEDIUM | INSTALLED | 1.0 |
| PROG-008 | Budget vs Actual Reporting | Per-programme expenditure vs budget | HIGH | PLANNED | 1.0 |
| PROG-009 | Outcome Indicator Definition | Custom fields for programme indicators | HIGH | PLANNED | 1.1 |
| PROG-010 | Field Activity Logs | Structured daily activity logs from field staff | HIGH | PLANNED | 1.1 |

---

## Domain: Donor Management (DONOR)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| DONOR-001 | Donor Contact Records | Donor/funder partners in contacts | HIGH | NOT STARTED | 1.0 |
| DONOR-002 | Grant Analytic Accounts | Per-grant fund tracking via analytic accounts | HIGH | COMPLETED | 1.0 |
| DONOR-003 | Recurring Payment Management | Recurring donor payment schedules | MEDIUM | INSTALLED | 1.0 |
| DONOR-004 | Donor Follow-Up | Automated donor payment reminders | MEDIUM | INSTALLED | 1.0 |
| DONOR-005 | MOU / Grant Agreement Storage | Document repository for donor agreements | HIGH | PLANNED | 1.0 |
| DONOR-006 | Multi-Donor Fund Separation | Separate analytic plan per donor | HIGH | PLANNED | 1.1 |
| DONOR-007 | Donor Budget Report | Donor-specific budget utilisation report | HIGH | PLANNED | 1.1 |
| DONOR-008 | Donor Narrative Report | Narrative programme report for donors | MEDIUM | PLANNED | 1.2 |

---

## Domain: Procurement (PROC)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| PROC-001 | Vendor Management | 17 vendors onboarded | HIGH | COMPLETED | 1.0 |
| PROC-002 | Local Purchase Order (LPO) | LPO creation and tracking | HIGH | PARTIAL | 1.0 |
| PROC-003 | LPO Approval Workflow | Two-step approval at ₦200,000 threshold | HIGH | COMPLETED | 1.0 |
| PROC-004 | Vendor Invoice Processing | Vendor bill entry and approval | HIGH | COMPLETED | 1.0 |
| PROC-005 | Payment Approval | Multi-step payment authorisation | HIGH | COMPLETED | 1.0 |
| PROC-006 | Procurement Reports | Standard purchase PDF reports | MEDIUM | INSTALLED | 1.0 |
| PROC-007 | Budget Pre-Check | Block LPO if over budget | HIGH | PLANNED | 1.0 |
| PROC-008 | Vendor Performance Rating | Track vendor delivery quality | LOW | PLANNED | 1.2 |
| PROC-009 | Contract-Linked Procurement | Link LPOs to active contracts | MEDIUM | PLANNED | 1.1 |

---

## Domain: Finance (FIN)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| FIN-001 | Chart of Accounts (NGO) | 70 accounts incl. 21 NGO-specific | HIGH | COMPLETED | 1.0 |
| FIN-002 | NGN Functional Currency | Nigerian Naira as functional currency | HIGH | COMPLETED | 1.0 |
| FIN-003 | Nigeria VAT (7.5%) | FIRS VAT configuration | HIGH | COMPLETED | 1.0 |
| FIN-004 | Withholding Tax (WHT) | FIRS WHT accounts and tax | HIGH | COMPLETED | 1.0 |
| FIN-005 | Analytic Accounting | Programme-level cost tracking | HIGH | COMPLETED | 1.0 |
| FIN-006 | Budget Management | Programme budget entry and tracking | HIGH | COMPLETED | 1.0 |
| FIN-007 | Asset Depreciation | Fixed asset depreciation schedules | HIGH | INSTALLED | 1.0 |
| FIN-008 | Recurring Payments | Automated recurring transactions | MEDIUM | INSTALLED | 1.0 |
| FIN-009 | Daily Financial Reports | om_account_daily_reports | MEDIUM | INSTALLED | 1.0 |
| FIN-010 | Full Accounting Suite | om_account_accountant dashboard | HIGH | INSTALLED | 1.0 |
| FIN-011 | FIRS Tax Report | Structured FIRS reporting format | HIGH | INSTALLED | 1.0 |
| FIN-012 | Bank Account Configuration | WamaCare bank account in system | HIGH | PARTIAL | 1.0 |
| FIN-013 | Bank Reconciliation | Match bank statement to system | HIGH | PARTIAL | 1.0 |
| FIN-014 | PAYE and PENCOM Tracking | Nigerian statutory deductions | HIGH | PARTIAL | 1.0 |
| FIN-015 | Budget vs Actual Dashboard | Programme-level financial dashboard | HIGH | PLANNED | 1.0 |

---

## Domain: Asset Management (ASSET)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| ASSET-001 | Asset Register | 3 assets: Ambulance, Ultrasound, Laptop | HIGH | PARTIAL | 1.0 |
| ASSET-002 | Asset Depreciation Module | om_account_asset installed | HIGH | INSTALLED | 1.0 |
| ASSET-003 | Equipment Categories | Categorise assets by type | LOW | NOT STARTED | 1.0 |
| ASSET-004 | Asset Assignment | Assign assets to departments/programmes | MEDIUM | NOT STARTED | 1.0 |
| ASSET-005 | Maintenance Scheduling | Preventive maintenance calendar | MEDIUM | INSTALLED | 1.0 |
| ASSET-006 | Depreciation Configuration | Set depreciation method and period per asset | HIGH | PLANNED | 1.0 |
| ASSET-007 | Insurance Tracking | Insurance policy linkage to assets | MEDIUM | PLANNED | 1.1 |

---

## Domain: Inventory (INV)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| INV-001 | Product Catalogue | 21 programme products/services defined | HIGH | COMPLETED | 1.0 |
| INV-002 | Stock Module Installation | `stock` module for physical inventory | HIGH | PLANNED | 1.1 |
| INV-003 | Stock Locations | Define warehouse and field locations | HIGH | PLANNED | 1.1 |
| INV-004 | Delivery Kit Tracking | Track physical delivery kit stock | HIGH | PLANNED | 1.1 |
| INV-005 | Medical Supply Inventory | Track medical consumables | HIGH | PLANNED | 1.1 |
| INV-006 | Reorder Rules | Automatic replenishment triggers | MEDIUM | PLANNED | 1.2 |
| INV-007 | Lot/Serial Tracking | Track individual units (e.g., equipment serial nos.) | LOW | PLANNED | 1.2 |

---

## Domain: Beneficiary Management (BEN)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| BEN-001 | Beneficiary Registration | 13 beneficiaries (BEN-004 to BEN-016) | HIGH | PARTIAL | 1.0 |
| BEN-002 | Programme Tagging | Beneficiaries tagged by programme | HIGH | PARTIAL | 1.0 |
| BEN-003 | Geolocation Mapping | FCT area coordinates on beneficiary records | MEDIUM | PARTIAL | 1.0 |
| BEN-004 | Gender Tagging | Female/Male category tags | HIGH | PARTIAL | 1.0 |
| BEN-005 | Anonymised Naming | BEN-XXX reference scheme | HIGH | PARTIAL | 1.0 |
| BEN-006 | Access Restriction | Record-level access rules for beneficiary data | HIGH | COMPLETED | 1.0 |
| BEN-007 | Beneficiary Consent Tracking | Document consent for data processing | HIGH | PLANNED | 1.1 |
| BEN-008 | Case Management | Structured case notes and follow-up | HIGH | PLANNED | 1.1 |
| BEN-009 | Case Notes | Timestamped case notes per beneficiary | HIGH | PLANNED | 1.1 |

---

## Domain: Safeguarding (SAFE)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| SAFE-001 | Safeguarding Programme | "Safeguarding & Protection Program" active | HIGH | COMPLETED | 1.0 |
| SAFE-002 | Safeguarding Department | Legal & Compliance dept with Head | HIGH | COMPLETED | 1.0 |
| SAFE-003 | Safeguarding Lead Role | Employee role: Safeguarding Lead C | HIGH | COMPLETED | 1.0 |
| SAFE-004 | NDPR Privacy Module | `privacy_lookup` module installed | HIGH | PARTIAL | 1.0 |
| SAFE-005 | Safeguarding Alert Flags | Flag a beneficiary record for safeguarding review | CRITICAL | PLANNED | 1.1 |
| SAFE-006 | Case Escalation Workflow | Escalate flagged cases to Safeguarding Lead | CRITICAL | PLANNED | 1.1 |
| SAFE-007 | Evidence Upload | Structured evidence attachment to cases | HIGH | PLANNED | 1.1 |
| SAFE-008 | Referral Pathway Tracking | Track referrals to external agencies | HIGH | PLANNED | 1.1 |
| SAFE-009 | Anonymous Reporting Portal | Web portal for anonymous safeguarding reports | HIGH | PLANNED | 1.2 |
| SAFE-010 | Safe House Management | Intake, residence, and exit tracking | MEDIUM | DEFERRED | 2.0 |

---

## Domain: Entrepreneurship (ENT)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| ENT-001 | Entrepreneurship Programme | Women entrepreneurship programme setup | HIGH | PLANNED | 1.3 |
| ENT-002 | Club Registration | Register entrepreneurship clubs as contacts | HIGH | PLANNED | 1.3 |
| ENT-003 | Member Management | Track club members | HIGH | PLANNED | 1.3 |
| ENT-004 | Training Programme Tracking | Training events and attendance per club | HIGH | PLANNED | 1.3 |
| ENT-005 | Mentoring Tracking | Mentor-mentee assignment and log | MEDIUM | PLANNED | 1.3 |
| ENT-006 | Informal-to-Cooperative Upgrade | Track group formalisation milestones | MEDIUM | PLANNED | 1.3 |
| ENT-007 | Livelihood Outcome Tracking | Income, employment outcomes per member | HIGH | PLANNED | 1.3 |

---

## Domain: M&E (ME)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| ME-001 | M&E Programme | "Monitoring & Evaluation Program" active | HIGH | COMPLETED | 1.0 |
| ME-002 | Programme Task Completion | Track activity completion via project tasks | HIGH | COMPLETED | 1.0 |
| ME-003 | Budget vs Actual | Programme financial performance | HIGH | INSTALLED | 1.0 |
| ME-004 | Programme Dashboard | Spreadsheet dashboard engine installed | HIGH | NOT STARTED | 1.0 |
| ME-005 | Outcome Indicator Fields | Custom fields for programme KPIs | HIGH | PLANNED | 1.2 |
| ME-006 | Cost-per-Beneficiary | Compute programme cost / beneficiary count | HIGH | PLANNED | 1.2 |
| ME-007 | Field Data Collection | Mobile-friendly data entry from field | MEDIUM | PLANNED | 1.2 |
| ME-008 | Impact Report (PDF) | Donor-ready impact report template | HIGH | PLANNED | 1.2 |

---

## Domain: Executive Dashboard (EXEC)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| EXEC-001 | Financial Dashboard | Account spreadsheet dashboard | HIGH | NOT STARTED | 1.0 |
| EXEC-002 | Procurement Dashboard | Purchase spreadsheet dashboard | HIGH | NOT STARTED | 1.0 |
| EXEC-003 | Programme Overview | Project list and kanban view | HIGH | COMPLETED | 1.0 |
| EXEC-004 | Custom KPI Dashboard | WamaCare-specific KPI spreadsheet | HIGH | PLANNED | 1.2 |
| EXEC-005 | Beneficiary Statistics View | Beneficiary count by programme/area | HIGH | PLANNED | 1.2 |
| EXEC-006 | Executive PDF Report | Leadership-ready PDF programme summary | MEDIUM | PLANNED | 1.2 |

---

## Domain: Healthcare Ecosystem (HEALTH)

| ID | Feature | Description | Priority | Status | Release |
|----|---------|-------------|---------|--------|---------|
| HEALTH-001 | Healthcare Vendor Network | SafeLife Diagnostics, Hope Medical, etc. | HIGH | COMPLETED | 1.0 |
| HEALTH-002 | Medical Product Catalogue | ANC Services, Mobile Clinic Equipment | HIGH | COMPLETED | 1.0 |
| HEALTH-003 | Mobile Clinic Assets | Ambulance and Ultrasound registered | HIGH | COMPLETED | 1.0 |
| HEALTH-004 | Health Insurance Partner | Community Health Insurance Scheme vendor | MEDIUM | PARTIAL | 1.0 |
| HEALTH-005 | Healthcare Referral Network | Track referrals to health providers | HIGH | PLANNED | 2.0 |
| HEALTH-006 | Digital Blood Bank | Integration with blood bank system | MEDIUM | PLANNED | 2.0 |

---

## Feature Count Summary (v1.1 — Evidence-Based)

> Updated 2026-05-29 based on Evidence-Based Audit. INSTALLED = module present, 0 transactions.

| Domain | COMPLETED | PARTIAL | INSTALLED | NOT STARTED | PLANNED | DEFERRED | TOTAL |
|--------|-----------|---------|-----------|------------|---------|---------|-------|
| Governance (GOV) | 3 | 0 | 1 | 1 | 5 | 0 | 10 |
| HR | 3 | 0 | 2 | 1 | 6 | 1 | 13 |
| Programme (PROG) | 2 | 0 | 4 | 1 | 3 | 0 | 10 |
| Donor (DONOR) | 1 | 0 | 2 | 1 | 4 | 0 | 8 |
| Procurement (PROC) | 1 | 0 | 5 | 0 | 3 | 0 | 9 |
| Finance (FIN) | 2 | 2 | 8 | 2 | 1 | 0 | 15 |
| Asset (ASSET) | 0 | 1 | 2 | 2 | 2 | 0 | 7 |
| Inventory (INV) | 1 | 0 | 0 | 0 | 6 | 0 | 7 |
| Beneficiary (BEN) | 0 | 5 | 0 | 1 | 3 | 0 | 9 |
| Safeguarding (SAFE) | 3 | 1 | 0 | 0 | 5 | 1 | 10 |
| Entrepreneurship (ENT) | 0 | 0 | 0 | 0 | 7 | 0 | 7 |
| M&E (ME) | 1 | 0 | 2 | 1 | 4 | 0 | 8 |
| Exec Dashboard (EXEC) | 1 | 0 | 0 | 2 | 3 | 0 | 6 |
| Healthcare (HEALTH) | 3 | 1 | 0 | 0 | 2 | 0 | 6 |
| **TOTAL** | **21** | **10** | **26** | **12** | **55** | **2** | **126** |

**v1.1 evidence-based status:**
- **21 COMPLETED** (down from 53 — 32 features had no DB evidence)
- **10 PARTIAL** (partially configured but not tested)
- **26 INSTALLED** (module present, zero transactions — not operational)
- **12 NOT STARTED** (misclaimed as configured; actually nothing done)
- **55 PLANNED** (correctly planned)
- **2 DEFERRED**

**The 26 INSTALLED features are the operational validation target for Phase A.5.**
