# PROJECT_IDENTITY.md — WamaCare Project Identity

**Phase:** 1 | **Date:** 2026-05-29 | **Status:** COMPLETE

---

## What Is WamaCare?

WamaCare is an Odoo 17 Community Edition implementation for **Tiko**, a Nigerian Community-Based Organisation (CBO) operating in the Federal Capital Territory (Abuja). The organisation delivers community health and social protection programmes targeting women and vulnerable populations.

**WamaCare is not a hospital, clinic, HMO, or pharmacy system.** It is an NGO/CBO management platform that:
- Tracks beneficiaries and programme enrolment
- Manages projects, activities, and field operations
- Handles procurement (Local Purchase Orders)
- Tracks staff and their assignments
- Manages assets and equipment
- Tracks programme budgets and expenses via analytic accounts
- Supports monitoring, evaluation, and reporting

---

## Organisation Profile (Tiko)

| Field | Value |
|-------|-------|
| Organisation name | Tiko (WamaCare project) |
| Organisation type | Community-Based Organisation (CBO) |
| Legal form | NGO/CBO (Nigeria) |
| Country | Nigeria |
| State/Territory | Federal Capital Territory (FCT), Abuja |
| Operating areas | Kubwa, Karmo, Lugbe, Nyanya, Nyanya-Gwagwa, Dutse, Jahi |
| Primary focus | Maternal health and women's protection |
| Target beneficiaries | Women and girls (maternal health, protection, capacity-building) |
| Currency | NGN (Nigerian Naira, ₦) |

---

## Programmes

| Programme | Focus Area | Analytic Account |
|-----------|-----------|-----------------|
| Maternal Health Outreach – Tiko | ANC, delivery kits, mobile clinic | Maternal Health |
| Health Worker Capacity Program | Training healthcare workers | Capacity Building |
| Safeguarding & Protection Program | Protection, legal advisory, safeguarding framework | Safeguarding |
| Monitoring & Evaluation Program | Data collection, reporting, impact assessment | Monitoring |
| Organisation-wide Support | Admin, ICT, HR, finance | Administration |

---

## Departmental Structure

| Department | Parent | Focus |
|-----------|--------|-------|
| Programs Department | — | Programme management |
| Field Operations | Programs | Field delivery |
| Finance Department | — | Budgeting, expenses, procurement |
| ICT Department | — | Digital systems |
| Legal & Compliance | — | Safeguarding, data protection |

---

## Service Types (from CSV inspection)

**Maternal health services:**
- Delivery Kits, Antenatal Screening Services, Mobile Clinic Equipment
- Solar Power Units (for remote sites)

**Capacity and training:**
- Training Services, Community Engagement Sessions, Field Mobilizer Stipends

**Safeguarding and protection:**
- Safeguarding Framework, Data Protection Tools, Legal Advisory Services

**Organisational:**
- Logistics Services, Transport Services, Monitoring Services
- Staff Health Insurance, Admin Support Services

**Procurement/vendor services:**
- Diagnostic Services, Medical Equipment, Energy Solutions, IT Services
- Consultancy Services, Audit Services

---

## Staff Profile (detected)

| Role | Department | Notes |
|------|-----------|-------|
| Field Officer | Operations | Community outreach |
| Nurse/Midwife | Health Services | Maternal health delivery |
| Safeguarding Lead | Compliance | Protection programme |
| Community Mobilizer | Community Outreach | Beneficiary engagement |

---

## Beneficiary Profile (detected)

- Female beneficiaries only (from CSV: all tagged "Female")
- Located across FCT: Kubwa, Karmo, Lugbe, Nyanya, Jahi, Dutse
- Tagged by programme: Maternal Health, Protection, Community Outreach, Capacity Building
- Reference format: BEN-XXX (BEN-004 to BEN-016 in demo data)

---

## Asset Types (detected)

| Asset | Type | Value (₦) |
|-------|------|----------|
| Ambulance 01 | Fixed Asset | 35,000,000 |
| Ultrasound Machine | Fixed Asset | 12,000,000 |
| Laptop – Field Officer | Fixed Asset | 850,000 |

---

## Odoo Model-to-Use Mapping

| Real-world concept | Odoo model | Module |
|-------------------|-----------|--------|
| Beneficiaries | `res.partner` (tagged) | `contacts` |
| Programmes/Projects | `project.project` | `project` |
| Activities/Tasks | `project.task` | `project` |
| Donors/Funders | `res.partner` (tagged) | `contacts` |
| Vendors | `res.partner` (vendor) | `purchase` |
| LPOs / Purchase Orders | `purchase.order` | `purchase` |
| Budget Analytic Accounts | `account.analytic.account` | `analytic` |
| Staff Expenses | `hr.expense` or `account.move` | `hr_expense` / `account` |
| HR Departments | `hr.department` | `hr` |
| Employees | `hr.employee` | `hr` |
| Assets / Equipment | `maintenance.equipment` or `account.asset` | `maintenance` / `account` |
| Services/Products | `product.template` | `product` |

---

## What WamaCare Is NOT

To prevent scope creep and wrong module installation:

| Not this | Reason |
|---------|--------|
| Hospital/clinic system | No patient records, prescriptions, or clinical pathways |
| Pharmacy | No drug dispensing, drug master, or stock controlled for medications |
| HMO | No insurance claims, premium management, or enrolment plans |
| Manufacturing ERP | No bill of materials, work orders, or production routing |
| Retail | No point-of-sale, retail pricing, or B2C transactions |

---

## Template Positioning

WamaCare is designed as the **reference implementation** for a reusable Odoo NGO/CBO template. Its core patterns (beneficiary tracking, programme management, donor-funded analytic accounts, LPO-based procurement) are generic enough to serve any Nigerian or African NGO/CBO running community programmes.

See: [TEMPLATE_STRATEGY.md](./TEMPLATE_STRATEGY.md)

---

*Phase 1 — Project Identity confirmed from inspection of local documents and CSV files.*
