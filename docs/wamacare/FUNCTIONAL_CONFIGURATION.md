# FUNCTIONAL_CONFIGURATION.md — WamaCare Functional Configuration

**Phase:** 8 | **Date:** 2026-05-29 | **Status:** COMPLETE

---

## Company Profile

| Field | Value |
|-------|-------|
| Company Name | WamaCare (Tiko CBO) |
| Country | Nigeria |
| State | Federal Capital Territory (FCT) |
| City | Abuja |
| Postal Code | 900001 |
| Phone | +234 800 000 0001 |
| Email | info@wamacare.ng |
| Website | https://wamacare.ng |
| Functional Currency | NGN (₦ — Nigerian Naira) |
| Fiscal Country | Nigeria |

---

## Localisation

| Module | Status | Purpose |
|--------|--------|---------|
| `l10n_ng` | Installed | Nigerian fiscal localisation — VAT, WHT, FIRS reporting |
| `base_vat` | Installed | VAT number validation |

### Nigeria Taxes Configured (l10n_ng)
| Tax | Type | Rate | Use |
|-----|------|------|-----|
| 7.5% VAT | Sale & Purchase | 7.5% | Standard Nigerian VAT (FIRS) |
| Withholding Tax | Purchase | Various rates | WHT on vendor invoices |

**Manual step required:** To fully apply the Nigeria chart template (additional tax accounts),
go to: Accounting → Settings → Fiscal Localization → select Nigeria → Apply.

---

## Chart of Accounts

**Total accounts:** 68 (47 generic + 21 NGO/Nigeria-specific)

### NGO-Specific Accounts Created in Phase 8

**Income (4xxx)**
| Code | Name |
|------|------|
| 4000 | Grant Income |
| 4010 | Donor Funding |
| 4020 | Programme Income |
| 4030 | Restricted Grant Income |

**Expenses (5xxx)**
| Code | Name |
|------|------|
| 5000 | Programme Expenses |
| 5010 | Staff Costs |
| 5020 | Field Operations |
| 5030 | Maternal Health Costs |
| 5040 | Safeguarding Costs |
| 5050 | Capacity Building Costs |
| 5060 | Monitoring & Evaluation |
| 5070 | Community Outreach Costs |
| 5080 | Admin & Overhead |
| 5090 | Transport & Logistics |

**Liabilities (2xxx) — Nigeria Specific**
| Code | Name |
|------|------|
| 2100 | WHT Payable (FIRS) |
| 2110 | PAYE Payable (FIRS) |
| 2120 | VAT Payable (FIRS) |
| 2130 | PENCOM Payable |
| 2140 | Deferred Grant Income |

**Equity (3xxx)**
| Code | Name |
|------|------|
| 3000 | Retained Surplus |
| 3010 | Restricted Fund Reserve |

---

## Analytic Accounting

**Status:** ENABLED  
**Plan:** `Programs`

| Analytic Account | Linked Project |
|-----------------|---------------|
| Maternal Health | Maternal Health Outreach – Tiko |
| Capacity Building | Health Worker Capacity Program |
| Safeguarding | Safeguarding & Protection Program |
| Monitoring | Monitoring & Evaluation Program |
| Administration | Organisation-wide Support |
| Community Outreach | (standalone — no project) |
| Operations | (standalone) |
| Digital Systems | (standalone) |
| Assets | (standalone) |
| Human Resources | (standalone) |
| Infrastructure | (standalone) |
| Compliance | (standalone) |
| Staff Welfare | (standalone) |

---

## Procurement (Purchase)

### Purchase Approval Workflow
| Setting | Value |
|---------|-------|
| Order Approval | Enabled (two-step) |
| Approval Threshold | ₦200,000 |
| Approval Required Above | ₦200,000 |
| Approval Not Required Below | ₦200,000 |

**How it works:** Purchase orders below ₦200,000 are confirmed directly. Orders at or above ₦200,000 require manager approval before confirmation.

### LPO Data Imported
| PO Number | Vendor | Amount | Status |
|-----------|--------|--------|--------|
| LPO-001 | Health Supplies Ltd | ₦2,500,000 | Draft |

---

## HR Configuration

### Departments
| Department | Parent | Manager |
|-----------|--------|---------|
| ICT Department | — | (to be assigned) |
| Finance Department | — | (to be assigned) |
| Programs Department | — | (to be assigned) |
| Legal & Compliance | — | (to be assigned) |
| Field Operations | Programs Department | (to be assigned) |

### Employees
| Name | Job Title | Department |
|------|----------|-----------|
| Field Officer A | Field Officer | Operations |
| Nurse B | Nurse/Midwife | Health Services |
| Safeguarding Lead C | Safeguarding Lead | Compliance |
| Community Mobilizer D | Mobilizer | Community Outreach |

---

## Assets (Maintenance Equipment)

| Asset | Type | Value (₦) |
|-------|------|----------|
| Ambulance 01 | Fixed Asset | 35,000,000 |
| Ultrasound Machine | Fixed Asset | 12,000,000 |
| Laptop – Field Officer | Fixed Asset | 850,000 |

**Total asset value:** ₦47,850,000

---

## User Roles and Access

### Users Configured

| Login | Name | Role | Access |
|-------|------|------|--------|
| `admin` | Administrator | System Admin | Full access |
| `aliyu.umaru` | Aliyu Hassan Umaru | Programme Manager | Projects, Purchase, HR, Analytic |
| `finance.officer` | WamaCare Finance Officer | Finance | Accounting, Analytic, Purchase |
| `field.officer` | WamaCare Field Officer | Field | Project tasks only |
| `hr.officer` | WamaCare HR Officer | HR | HR records only |

### Default Passwords
All new users: `WamaCare2026!`  
Admin: `admin` — **MUST BE CHANGED before any non-local use (Issue #11)**

### Access Groups by Role

| Group | admin | aliyu.umaru | finance.officer | field.officer | hr.officer |
|-------|-------|-------------|-----------------|---------------|------------|
| Analytic Accounting | ✓ | ✓ | ✓ | — | — |
| Show Full Accounting | ✓ | ✓ | — | — | — |
| Billing Administrator | ✓ | — | ✓ | — | — |
| Project Administrator | ✓ | ✓ | — | — | — |
| Project User | ✓ | ✓ | — | ✓ | — |
| Purchase Administrator | ✓ | ✓ | — | — | — |
| Purchase User | ✓ | ✓ | ✓ | — | — |
| HR Officer | ✓ | ✓ | — | — | ✓ |
| HR Manager | ✓ | — | — | — | — |
| Maintenance Manager | ✓ | — | — | — | — |

---

## Beneficiary Configuration

**Model:** `res.partner` (type=person)  
**Identification:** Category tag `Beneficiary`  
**Programme tags:** Maternal Health, Protection, Community Outreach, Capacity Building  
**Access:** Restricted to users with Programme Manager or higher role

### Beneficiary Partner Categories
- Beneficiary, Active, Female, Male
- Maternal Health, Protection, Community Outreach, Capacity Building

---

## Remaining Manual Configuration Steps

These steps require the Odoo web UI — they cannot be done via RPC:

1. **Fiscal Localisation:** Accounting → Settings → Fiscal Localization → Nigeria → Apply
2. **Change admin password:** Settings → Users → Admin → Change Password
3. **Set department managers:** Employees → Departments → assign managers to each dept
4. **Bank account:** Accounting → Configuration → Bank Accounts → add WamaCare bank
5. **Email server:** Settings → Technical → Email → configure outgoing mail server
6. **Beneficiary access rule:** Settings → Technical → Record Rules → restrict beneficiary visibility

---

## Configuration Applied via Scripts

| Script | What it does |
|--------|-------------|
| `scripts/import_wamacare_data.py` | Phase 7 — all base data |
| `scripts/configure_wamacare_phase8.py` | Phase 8a — company, currency, COA, project links, assets |
| `scripts/configure_wamacare_phase8b.py` | Phase 8b — users, purchase approval, LPO, analytic enable |

---

*Phase 8 functional configuration complete. 6 manual steps remain for full production readiness.*
