# WAMACARE_PRODUCT_ROADMAP.md — WamaCare Product Roadmap

**Version:** 1.0 | **Date:** 2026-05-29
**Authority:** This roadmap governs all future feature development. Deviations require a recorded decision in DECISION_LOG.md.

---

## Roadmap Principles

1. Safeguarding features are never deprioritised.
2. No release ships without its predecessor being stable and validated.
3. Inventory cannot be built until Procurement is solid.
4. Case management cannot be built until Beneficiary Management is complete.
5. Safe House is only built after Safeguarding case management is operational.
6. Ecosystem integration is only built after the core platform is production-stable.

---

## RELEASE 1.0 — GOVERNANCE FOUNDATION
**Status:** IN PROGRESS (Phases 1–11 complete)
**Target:** v1.0.0 — stable, validated, backed up, documented

### Scope

| Domain | Features |
|--------|---------|
| Governance | Department structure, RBAC, audit trail, PO approval, 2FA, fiscal year |
| HR | Employee records, org chart, expense claims, job positions |
| Programme Management | 5 programmes, analytic accounts, budget module, calendar |
| Donor Management | Grant analytic accounts, recurring payments, donor follow-up |
| Procurement | 17 vendors, LPO workflow, two-step approval at ₦200k, vendor bills |
| Finance | 70 COA accounts, NGN currency, Nigeria VAT/WHT, full accounting suite, FIRS reporting |
| Asset Management | 3 assets registered, depreciation module installed |
| Inventory | Product catalogue (21 items) |
| Beneficiary Management | 13 beneficiaries, programme tags, geolocation, gender tagging |
| Safeguarding | Programme + department + Safeguarding Lead role |
| Executive Dashboard | Financial + procurement spreadsheet dashboards |
| Healthcare Ecosystem | Healthcare vendor network, medical product catalogue, mobile clinic assets |

### v1.0.0 Remaining Items

| Item | Status | Priority |
|------|--------|---------|
| Bank account configuration | PARTIAL | HIGH |
| Budget entries per programme | PARTIAL | HIGH |
| Depreciation configuration for 3 assets | PARTIAL | HIGH |
| Beneficiary access restriction (record rules) | PLANNED | HIGH |
| Contract repository (GOV-007) | PLANNED | HIGH |
| Admin password change | Manual | CRITICAL |
| Nigeria fiscal localisation applied in UI | Manual | HIGH |

---

## RELEASE 1.1 — BENEFICIARY & SAFEGUARDING
**Status:** PLANNED
**Target:** After v1.0.0 validation and at least 30 days of production operation

### Scope

| Domain | Features |
|--------|---------|
| Safeguarding | SAFE-005 Alert flags, SAFE-006 Escalation workflow, SAFE-007 Evidence upload, SAFE-008 Referral tracking |
| Beneficiary Management | BEN-006 Access restriction, BEN-007 Consent tracking, BEN-008 Case management, BEN-009 Case notes |
| HR | HR-009 Volunteer management, HR-010 Mobilizer profiles |
| Procurement | PROC-009 Contract-linked procurement |
| Governance | GOV-010 General approval workflow, GOV-009 SOP repository |
| Inventory | INV-002 Stock module, INV-003 Locations, INV-004 Delivery kit tracking, INV-005 Medical supplies |
| Donor | DONOR-006 Multi-donor fund separation, DONOR-007 Donor budget report |
| Programme | PROG-009 Outcome indicators, PROG-010 Field activity logs |

### Gate Criteria (before Release 1.1 starts)
- [ ] v1.0.0 validated and in production
- [ ] At least 1 complete LPO cycle (order → approve → receive → pay) executed
- [ ] At least 1 full programme cycle (plan → activities → report) executed
- [ ] Admin password changed
- [ ] Bank account configured

---

## RELEASE 1.2 — IMPACT MEASUREMENT
**Status:** PLANNED
**Target:** After Release 1.1 stable

### Scope

| Domain | Features |
|--------|---------|
| M&E | ME-005 Outcome indicators, ME-006 Cost-per-beneficiary, ME-007 Field data collection, ME-008 Impact report |
| Safeguarding | SAFE-009 Anonymous reporting portal |
| HR | HR-008 Performance tracking, HR-011 Staff exit continuity |
| Governance | GOV-008 Contract expiry alerts |
| Donor | DONOR-008 Donor narrative report |
| Asset | ASSET-007 Insurance tracking |
| Inventory | INV-006 Reorder rules, INV-007 Lot tracking |
| Executive Dashboard | EXEC-004 Custom KPI dashboard, EXEC-005 Beneficiary statistics, EXEC-006 Executive PDF report |

### Gate Criteria
- [ ] Release 1.1 validated and stable
- [ ] Beneficiary case management operational (BEN-008)
- [ ] Safeguarding alert workflow tested (SAFE-005, SAFE-006)

---

## RELEASE 1.3 — ECONOMIC EMPOWERMENT
**Status:** PLANNED
**Target:** After Release 1.2 stable

### Scope

| Domain | Features |
|--------|---------|
| Entrepreneurship | ENT-001 through ENT-007 — complete entrepreneurship module |
| HR | HR-012 Payroll integration (basic) |

### Gate Criteria
- [ ] Release 1.2 validated
- [ ] At least 1 active entrepreneurship club in the community
- [ ] Operator decision: build in Odoo or integrate with external tool

---

## RELEASE 2.0 — ECOSYSTEM INTEGRATION
**Status:** DEFERRED — depends on v1.x stability
**Target:** After v1.3 and community validation

### Scope

| Domain | Features |
|--------|---------|
| Healthcare | HEALTH-005 Referral network, HEALTH-006 Digital Blood Bank |
| Safeguarding | SAFE-010 Safe House management |
| Ecosystem | Partner CBO integration, data sharing API |
| HR | Advanced payroll, statutory submissions to FIRS/PENCOM/NHF |

### Gate Criteria
- [ ] Full v1.x platform validated and used in production for 6+ months
- [ ] Blood Bank and Safe House partners identified
- [ ] Technical API integration scoped and funded

---

## Roadmap Summary

```
v1.0.0  Governance Foundation       ████████████████░░░░  IN PROGRESS
v1.1    Beneficiary & Safeguarding  ░░░░░░░░░░░░░░░░░░░░  PLANNED
v1.2    Impact Measurement          ░░░░░░░░░░░░░░░░░░░░  PLANNED
v1.3    Economic Empowerment        ░░░░░░░░░░░░░░░░░░░░  PLANNED
v2.0    Ecosystem Integration       ░░░░░░░░░░░░░░░░░░░░  DEFERRED
```

---

## Releases Not in Roadmap

The following have been considered but excluded:

| Item | Reason |
|------|--------|
| Clinical patient records | WamaCare is CBO not clinic |
| HMO claims processing | Out of scope |
| E-commerce | Not applicable |
| Generic donation platform | Different product category |

---

*Roadmap derived from: CBO_Mandate_and_Odoo_Deliverables_Tiko.docx, Odoo_module_checklist.xlsx, FEATURE_REGISTRY.md, and implementation evidence.*
