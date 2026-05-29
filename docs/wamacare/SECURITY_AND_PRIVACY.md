# SECURITY_AND_PRIVACY.md — WamaCare Data Security and Privacy

**Date:** 2026-05-29 | **Status:** DRAFT

---

## Data Sensitivity Classification

| Data Type | Sensitivity | Who Can Access |
|-----------|------------|----------------|
| Beneficiary names, phones, locations | HIGH | Programs team, Field Operations, Manager |
| Beneficiary programme tags (Maternal Health, Protection) | HIGH | Programs team only |
| Employee personal details | MEDIUM | HR and Manager only |
| Vendor/supplier data | LOW | Finance, Programs, Manager |
| Financial records | MEDIUM | Finance and Manager only |
| Analytic reports | MEDIUM | Finance and Manager only |
| General contacts | LOW | All staff |

---

## Role-Based Access Control (Planned)

| Role | Odoo Group | Permissions |
|------|-----------|------------|
| Administrator | `base.group_system` | Full access |
| Programme Manager | `project.group_project_manager` + analytic | Projects, beneficiaries, expenses |
| Field Officer | `project.group_project_user` | Assigned tasks, own beneficiaries |
| Finance Officer | `account.group_account_user` | Bills, payments, analytic reports |
| HR Officer | `hr.group_hr_user` | Employees, expenses |
| Read-only / Reporting | Custom | Dashboard and reports only |

---

## Beneficiary Data Privacy Rules

1. Beneficiary records (res.partner) must not be visible to external portal users.
2. Beneficiary tags revealing programme participation (e.g., "Maternal Health", "Protection") must not appear in any public-facing interface.
3. Beneficiary phone numbers are used only for field operations — not exported without authorization.
4. No clinical records, medical history, or prescription data is stored (WamaCare is a CBO, not a clinic).

---

## Data Retention

| Data Type | Retention Period | Notes |
|-----------|----------------|-------|
| Beneficiary records | Programme duration + 2 years | Per Nigerian data protection norms |
| Financial records | 7 years | Statutory requirement |
| HR records | Employment period + 5 years | Statutory requirement |
| Database backups | Latest 3 copies + annual snapshot | Rotate older backups |

---

## Credential Management

- Database password: never committed to Git
- Admin password: never committed to Git
- `wamacare.conf` is excluded from Git via `.gitignore`
- No API keys or tokens stored in the repository

---

## Audit Trail

Odoo's built-in chatter (`mail.thread`) provides an audit trail on:
- All partner (beneficiary/vendor) changes
- All purchase order changes and approvals
- All financial record changes
- All expense approvals

Custom audit logging may be added in a future phase.

---

## Nigeria Data Protection

| Requirement | Status |
|------------|--------|
| NDPR (Nigeria Data Protection Regulation) | Applicable — beneficiary data collected |
| Consent for data collection | Must be documented for each beneficiary |
| Right to erasure | Supported via Odoo archive/delete |
| Data breach response | To be defined in SOP |

---

*Full security configuration will be completed in Phase 8.*
