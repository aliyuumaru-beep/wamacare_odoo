# NEXT_FEATURE.md — WamaCare Current Highest Priority Feature

**Version:** 1.0 | **Date:** 2026-05-29
**Rule:** Only one feature appears in this document. It is the highest-priority feature whose dependencies are satisfied. Update this file each time a feature is completed.

---

## Current Next Feature

| Field | Value |
|-------|-------|
| **Feature ID** | PROC-002 / PROC-004 / PROC-005 |
| **Feature Name** | Complete Procurement Cycle — Reconcile Bill with Payment |
| **Domain** | Beneficiary Management |
| **Priority** | HIGH |
| **Current Status** | PLANNED |
| **Target Release** | 1.0 |

---

## Why This Feature Is Next

BEN-006 (Beneficiary Access Restriction) is **COMPLETED** — implemented 2026-05-30, verified: finance.officer=0, aliyu.umaru=13 beneficiaries visible.

The Procurement Lifecycle test (2026-05-30) revealed that `account_analytic_line` records are NOT being generated when vendor bills are posted, despite `analytic_distribution` being set. This means:
- Budget `practical_amount` = ₦0 regardless of actual spend
- Budget vs actual reporting is non-functional
- Programme cost tracking is broken

This is a **Donor Accountability (Rule 3)** and **Financial Control (Rule 4)** issue. Without analytic lines, the organisation cannot prove fund utilisation to donors.

---

## Dependencies

| Dependency | Status |
|-----------|--------|
| FIN-005 analytic module installed | COMPLETED ✅ |
| analytic_distribution set on bill lines | COMPLETED ✅ |
| BILL/2026/06/0001 posted (test bill) | COMPLETED ✅ |
| Accounting → Analytic settings | UNKNOWN — needs investigation |

---

## Implementation Notes

**Investigate:** Go to Accounting → Settings → Analytic Accounting section. Verify:
1. Analytic Accounting is enabled (should be — config param set)
2. The account journal (Purchase Journal) is configured to generate analytic lines

**Test:** After configuration fix, reset and re-post BILL/2026/06/0001. Verify `account_analytic_line` COUNT > 0.

**Expected outcome:** `practical_amount` on Maternal Health budget line shows ₦850,000.

---

## After This Feature Is Complete

Next: reconcile BILL/2026/06/0001 with PWBNK/2026/00001 in the Odoo UI (manual step — XML-RPC reconcile has a bug in Odoo 17). Then proceed with Finance Lifecycle test.

---

*This file is maintained by the operator or AI session implementing WamaCare features.*
