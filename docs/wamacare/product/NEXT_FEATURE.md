# NEXT_FEATURE.md — WamaCare Current Highest Priority Feature

**Version:** 1.0 | **Date:** 2026-05-29
**Rule:** Only one feature appears in this document. It is the highest-priority feature whose dependencies are satisfied. Update this file each time a feature is completed.

---

## Current Next Feature

| Field | Value |
|-------|-------|
| **Feature ID** | BEN-006 |
| **Feature Name** | Beneficiary Access Restriction |
| **Domain** | Beneficiary Management |
| **Priority** | HIGH |
| **Current Status** | PLANNED |
| **Target Release** | 1.0 |

---

## Why This Feature Is Next

**Reasoning against PRIORITIZATION_RULES.md:**

1. **Safeguarding (Rule 1):** BEN-006 directly protects beneficiary data. Unrestricted access to 13 beneficiary records (including Maternal Health and Protection cases) is a safeguarding risk. The data is sensitive — women and girls in vulnerable situations should not be visible to all system users.

2. **Beneficiary Protection (Rule 2):** This is a direct beneficiary protection control. Without it, any logged-in user can view all 13 beneficiary names, phones, locations, and programme tags.

3. **Dependencies satisfied:** Beneficiary records exist (BEN-001 COMPLETED), programme tagging exists (BEN-002 COMPLETED), user roles are configured (GOV-002 COMPLETED). The only dependency is an Odoo record rule — no new module needed.

---

## Dependencies

| Dependency | Status |
|-----------|--------|
| BEN-001 Beneficiary Registration | COMPLETED ✅ |
| BEN-002 Programme Tagging | COMPLETED ✅ |
| GOV-002 Role-Based Access Control | COMPLETED ✅ |
| Odoo `ir.rule` (record rules) | Available in base ✅ |

All dependencies satisfied. This feature can be implemented immediately.

---

## Implementation Notes

**Approach:** Create Odoo record rules (`ir.rule`) on `res.partner` to restrict beneficiary visibility:

1. In Odoo: Settings → Technical → Record Rules → New
2. Model: Contact (`res.partner`)
3. Rule: Only users in "Programme Manager" or higher group can see partners tagged as "Beneficiary"
4. Field Officers see only their own assigned beneficiary contacts

**Alternative (simpler):** Create a separate `res.partner.category` access group using Odoo's group-based domain filters.

**Estimated effort:** 1-2 hours of Odoo configuration (no coding required).

---

## Expected Outcome

- Beneficiary records invisible to Finance Officers, HR Officers, and unauthenticated portal users
- Only Programme Managers, Safeguarding Lead, and Admin can view all beneficiaries
- Field Officers see only beneficiaries assigned to their programme tasks
- NDPR compliance improved — data minimisation principle applied

---

## After This Feature Is Complete

Update this file to the next feature. Based on PRIORITIZATION_RULES.md and current state, the next feature after BEN-006 will be:

**SAFE-005 — Safeguarding Alert Flags** (Rule 1: Safeguarding is always top priority once data protection is in place)

---

*This file is maintained by the operator or AI session implementing WamaCare features.*
