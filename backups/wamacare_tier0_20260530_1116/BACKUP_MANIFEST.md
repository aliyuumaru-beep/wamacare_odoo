# BACKUP_MANIFEST.md — Post Tier 0 (Critical Risk) Backup

**Date:** 2026-05-30 11:16 | **Type:** After Phase A.5 Tier 0 security fixes

## What Was Done
- CR-1 BEN-006: ir.rule id=197 created on res.partner for Internal User group
  Domain: project_manager sees all; others cannot see Beneficiary-tagged partners
  VERIFIED: finance.officer=0, field.officer=0, aliyu.umaru=13 beneficiaries
- CR-2: field.officer already had project.group_project_user (already correct)
- CR-3: Technical Features (group_no_one) removed from aliyu.umaru via SQL
- CR-4: Equipment Manager is implied by Internal User (Odoo design) — cannot remove
- CR-5: Admin password deferred — local dev only

## Security Status
- Beneficiary data: PROTECTED (access restriction active and verified)
- Admin password: still admin/admin — change before any non-local use
