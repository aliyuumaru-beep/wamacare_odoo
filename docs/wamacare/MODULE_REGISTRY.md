# MODULE_REGISTRY.md — WamaCare Odoo Module Registry

**Date:** 2026-05-29 | **Status:** DRAFT — to be confirmed after database restore

---

## Module Matrix

| Module Name | Technical Name | Purpose | Required | Type | Status | Notes |
|------------|---------------|---------|---------|------|--------|-------|
| Contacts | `contacts` | Beneficiaries, donors, vendors, partners | YES | Community | TBC | Core — must be first |
| Discuss | `mail` | Internal messaging, chatter | YES | Community | TBC | Base dependency |
| Project | `project` | Programme and activity management | YES | Community | TBC | Core NGO workflow |
| Purchase | `purchase` | LPO / procurement workflow | YES | Community | TBC | Nigerian procurement norm |
| Accounting | `account` | Invoices, bills, journals | YES | Community | TBC | Financial management |
| Analytic Accounting | `analytic` | Per-programme budget tracking | YES | Community | TBC | Donor/grant tracking |
| HR | `hr` | Employee records, departments | YES | Community | TBC | Staff management |
| Expenses | `hr_expense` | Staff expense claims | YES | Community | TBC | Programme expense tracking |
| Inventory | `stock` | Assets and equipment tracking | OPTIONAL | Community | TBC | If medical supply tracking needed |
| Maintenance | `maintenance` | Equipment register (ambulance, ultrasound) | OPTIONAL | Community | TBC | Preferred for fixed assets |
| Calendar | `calendar` | Field activity scheduling | OPTIONAL | Community | TBC | Programme calendar |
| Approvals | `approvals` | LPO and expense approval flows | OPTIONAL | Community | TBC | May be covered by purchase settings |
| Documents | `documents` | Attachment and document management | OPTIONAL | Community | TBC | Beneficiary consent forms, reports |
| Website/Portal | `website` | Beneficiary/partner self-service | NO | Community | — | Not required for CBO |
| Payroll | `hr_payroll` | Full payroll processing | OPTIONAL | Community | TBC | Assess after Phase 6 |

---

## Modules NOT to Install

| Module | Reason |
|--------|--------|
| Healthcare/EMR modules | WamaCare is NOT a clinic — no patient records |
| Pharmacy/POS modules | Not applicable |
| Manufacturing (MRP) | No production workflow |
| Sales (CRM→Sales) | CBOs generally don't sell — use `purchase` side only |
| E-commerce | Not required |
| Unknown third-party modules | Require explicit operator approval |

---

## Confirmed After Restore

This table will be updated in Phase 6 with actual installed modules from the restored database.

| Module Technical Name | Installed in Dump? | Status |
|----------------------|-------------------|--------|
| (to be filled after Phase 5) | — | — |

---

## Custom Addons

| Module | Purpose | Status |
|--------|---------|--------|
| None detected at Phase 0 | — | No custom addons found |

---

*Module registry is provisional until Phase 5 database restore confirms actual installed modules.*
