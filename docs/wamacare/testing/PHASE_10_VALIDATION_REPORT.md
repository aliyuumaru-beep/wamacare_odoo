# PHASE_10_VALIDATION_REPORT.md — WamaCare Testing & Validation

**Phase:** 10 | **Date:** 2026-05-29 | **Status:** COMPLETE — OVERALL PASS

---

## Summary

| Result | Count |
|--------|-------|
| PASS   | 20    |
| WARN   | 0     |
| FAIL   | 0     |
| **OVERALL** | **PASS** |

All 20 validation checks passed. WamaCare is ready for Phase 11 (backup/restore drill).

---

## Environment

| Item | Value |
|------|-------|
| Database | `wamacare_local` |
| Odoo version | 17.0 |
| Modules installed | 78 |
| URL | http://localhost:8070 |
| Validation method | Odoo XML-RPC API |
| Validated by | Claude Code automated checks |

---

## Test Results

### Authentication & Startup

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T01 | Admin authentication | **PASS** | uid=2, authenticated successfully |
| T02 | Modules installed count | **PASS** | 78 modules installed |
| T03 | No pending module changes | **PASS** | 0 modules in to_install / to_upgrade / to_remove |
| T04 | All key modules installed | **PASS** | account, analytic, project, purchase, hr, hr_expense, maintenance, l10n_ng, om_account_accountant, om_account_asset, om_account_budget, accounting_pdf_reports, om_fiscal_year — all installed |

### Company Configuration

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T05 | Company name | **PASS** | "WamaCare (Tiko CBO)" |
| T06 | Functional currency | **PASS** | NGN (₦ — Nigerian Naira) |
| T07 | Country | **PASS** | Nigeria |

### Chart of Accounts

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T08 | Total COA accounts | **PASS** | 70 accounts (49 generic + 21 NGO-specific) |
| T09 | NGO-specific accounts | **PASS** | 7/7 spot-checked (4000, 4010, 5000, 5010, 5030, 2100, 3000) |

**NGO accounts confirmed:**

| Code | Name | Type |
|------|------|------|
| 4000 | Grant Income | Income |
| 4010 | Donor Funding | Income |
| 4020 | Programme Income | Income |
| 4030 | Restricted Grant Income | Income |
| 5000 | Programme Expenses | Expense |
| 5010 | Staff Costs | Expense |
| 5020 | Field Operations | Expense |
| 5030 | Maternal Health Costs | Expense |
| 5040 | Safeguarding Costs | Expense |
| 5050 | Capacity Building Costs | Expense |
| 5060 | Monitoring & Evaluation | Expense |
| 5070 | Community Outreach Costs | Expense |
| 5080 | Admin & Overhead | Expense |
| 5090 | Transport & Logistics | Expense |
| 2100 | WHT Payable (FIRS) | Liability |
| 2110 | PAYE Payable (FIRS) | Liability |
| 2120 | VAT Payable (FIRS) | Liability |
| 2130 | PENCOM Payable | Liability |
| 2140 | Deferred Grant Income | Liability |
| 3000 | Retained Surplus | Equity |
| 3010 | Restricted Fund Reserve | Equity |

### Analytic Accounting

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T10 | Analytic accounts | **PASS** | 13 accounts under "Programs" plan |
| T11 | Project → analytic links | **PASS** | All 5 projects linked to analytic accounts |

**Project-analytic mapping confirmed:**

| Project | Analytic Account |
|---------|-----------------|
| Maternal Health Outreach – Tiko | Maternal Health |
| Health Worker Capacity Program | Capacity Building |
| Safeguarding & Protection Program | Safeguarding |
| Monitoring & Evaluation Program | Monitoring |
| Organisation-wide Support | Administration |

### Contacts & Partners

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T12 | Beneficiaries | **PASS** | 13 beneficiaries (BEN-004 to BEN-016, 7 FCT locations) |
| T13 | Vendors | **PASS** | 17 vendors (Health Supplies Ltd, Hope Medical, SafeLife Diagnostics, etc.) |

### HR

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T14 | Active employees | **PASS** | 10 (5 department heads + 4 field staff + Administrator) |
| T15 | Department managers | **PASS** | 5/5 WamaCare departments managed (Administration left unassigned by design) |

**Department assignments confirmed:**

| Department | Manager |
|-----------|---------|
| ICT Department | Head ICT |
| Finance Department | Head Finance |
| Programs Department | Head Programs |
| Legal & Compliance | Head Legal & Compliance |
| Field Operations | Head Field Operations |

### Assets & Equipment

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T16 | Maintenance equipment | **PASS** | 3 assets: Ambulance 01 (₦35M), Ultrasound Machine (₦12M), Laptop – Field Officer (₦850K) |

### Procurement

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T17 | LPO amount | **PASS** | P00001: Health Supplies Ltd — ₦2,500,000 (₦0 tax) |

> **Note:** An incorrect 15% tax (₦375,000) was found on the LPO line during validation and removed. Root cause: Odoo applied a default product tax on creation. Fixed during this validation phase.

### Users & Security

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T18 | Active users | **PASS** | 5 users: admin, aliyu.umaru, finance.officer, field.officer, hr.officer |
| T19 | FamOil isolation | **PASS** | Separate database (`wamacare_local`), separate port (8070), separate addons path |

### Products & Services

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T20 | Products/services | **PASS** | 21 products (Delivery Kits, ANC Services, Training, Safeguarding Framework, etc.) |

---

## Issues Found During Validation (Resolved)

| # | Issue | Severity | Resolution |
|---|-------|---------|-----------|
| V-01 | NGO accounts (4000–5090) not created in Phase 8 — script failed silently | MEDIUM | Recreated during Phase 10 validation — 21 accounts now confirmed |
| V-02 | LPO P00001 had incorrect 15% tax applied on creation (₦375,000) | LOW | Removed during Phase 10 — amount now ₦2,500,000 (₦0 tax) |

---

## Open Items (not blocking)

| # | Item | Phase |
|---|------|-------|
| 1 | Admin password still `admin/admin` | Manual — operator action required |
| 2 | Nigeria fiscal localisation not applied via UI (Accounting → Settings → Fiscal Localization) | Manual |
| 3 | Department managers are placeholder names (Head ICT, etc.) — replace with real names | Manual |
| 4 | Bank account not configured | Manual |

---

## Phase 10 Conclusion

WamaCare is **functionally validated**. All 20 automated checks pass. Two data issues were found and fixed during this phase (V-01, V-02). Four manual UI steps remain (see Open Items) but are non-blocking for template use.

**Proceed to Phase 11 — Backup & Restore Drill.**
