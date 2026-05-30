# BACKUP_MANIFEST.md — After Procurement Lifecycle Test

**Date:** 2026-05-30 12:04 | **Type:** Post procurement lifecycle test

## Records Created
- P00002: Purchase Order ₦850,000 (state=purchase)
- P00003: Demo PO ₦425,000 (state=cancel — approval flow demo)
- BILL/2026/06/0001: Vendor Bill ₦850,000 (state=posted)
- PWBNK/2026/00001: Payment ₦850,000 (state=posted, WamaCare Bank)

## Defects Found
- D-1: Product purchase_method fixed (receive→purchase for 15 service products)
- D-2: Analytic lines not generated from posted bills
- D-3: Reconciliation failed via XML-RPC (manual UI step needed)
