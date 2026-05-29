# DECISION_LOG.md — WamaCare Architecture and Design Decisions

**Project:** WamaCare | **Started:** 2026-05-29

---

## DEC-001 — Git Root at WamaCare subfolder

**Date:** 2026-05-29 | **Phase:** -1 | **Status:** ACCEPTED

**Decision:** Initialize Git at `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare` (not at TIKO parent folder).

**Reason:** The TIKO parent folder contains PPTX/PDF files unrelated to the Odoo implementation. The WamaCare subfolder contains all implementation-relevant files. Keeping Git at the WamaCare level gives a cleaner repository scope and avoids including presentation materials in the Odoo deployment repo.

**Alternatives considered:**
- Git at TIKO root — rejected: would include PPTX/PDF presentation files not relevant to the deployment

---

## DEC-002 — WamaCare uses port 8070

**Date:** 2026-05-29 | **Phase:** -1 | **Status:** ACCEPTED

**Decision:** WamaCare Odoo instance runs on port 8070. FamOil uses 8069.

**Reason:** Prevents port conflict when both FamOil and WamaCare are run on the same machine. Both share the same Odoo binary and PostgreSQL instance.

---

## DEC-003 — Database dump excluded from Git

**Date:** 2026-05-29 | **Phase:** -1 | **Status:** ACCEPTED

**Decision:** `mamacare1.dump.zip` (19MB) is excluded from Git via `.gitignore`. Location documented in CLAUDE.md and BACKUP_AND_RECOVERY.md.

**Reason:** Binary dump files should never be in Git. They are large, change frequently, may contain sensitive beneficiary data, and are not human-readable. Git tracks code and documentation, not data.

---

## DEC-004 — WamaCare is NGO/CBO, not healthcare system

**Date:** 2026-05-29 | **Phase:** 1 | **Status:** ACCEPTED

**Decision:** WamaCare is implemented as an NGO/CBO management platform using native Odoo modules. No dedicated healthcare/EMR/pharmacy modules will be installed unless proven necessary by documents or database inspection.

**Reason:** All evidence from CSV files, product definitions, and programme names confirms this is a community-based organisation running health-focused community programmes — not a clinic, hospital, or HMO. Installing clinical modules would add unnecessary complexity and risk.

---

## DEC-005 — Odoo 17.0 Community Edition

**Date:** 2026-05-29 | **Phase:** 1 | **Status:** ACCEPTED

**Decision:** Use Odoo 17.0 Community Edition (same as FamOil on the machine).

**Reason:** Odoo 17.0 is already installed and operational. Community Edition is appropriate for an NGO/CBO template — avoids Enterprise licensing costs. To be confirmed against the database dump version on restore.

---

## DEC-006 — Beneficiaries as res.partner with tags

**Date:** 2026-05-29 | **Phase:** 1 | **Status:** ACCEPTED

**Decision:** Beneficiaries are stored as `res.partner` records tagged with partner categories (Beneficiary, programme name, gender, status).

**Reason:** Native Odoo approach — no custom model needed. `res.partner` already has all required fields (name, phone, city, country, geolocation, tags). A custom beneficiary model would add complexity without meaningful benefit at this stage.

---

---

## DEC-007 — Fresh Community DB instead of Enterprise dump restore

**Date:** 2026-05-29 | **Phase:** 5 | **Status:** ACCEPTED

**Decision:** Create a fresh Odoo 17 Community database (`wamacare_local`) instead of restoring `mamacare1.dump.zip`.

**Reason:** The dump (`mamacare1.dump.zip`) was created on Odoo Enterprise (confirmed by presence of `web_enterprise`, `documents`, `sign`, `planning`, `crm_enterprise`, `ai` modules). The local machine has only Odoo 17 Community Edition. Restoring the Enterprise database to Community caused all core business modules (project, purchase, account, hr_expense) to fail to load. The database was functionally unusable on Community.

**Data confirmed in Enterprise dump before discarding:**
- Company: `mamacare`
- 86 contacts (partners, vendors, beneficiaries)
- 5 projects (matching the 5 programmes in CSVs)
- 15 employees
- 5 purchase orders (LPOs)
- Same vendor and beneficiary data as in the CSV templates

**Alternatives considered:**
- Get Odoo Enterprise license — operator chose Community
- Manually downgrade database — complex, risky

**What was lost:** Any data in the Enterprise dump beyond what's in the CSVs. The CSVs cover the core data. The Enterprise-specific features (Documents, Sign, Planning board, AI) are not available in Community.

**Mitigation:** All data from the Enterprise dump is captured in `csv_templates/wamacare/`. CSV import in Phase 7 will restore the same data to the Community database.

---

## DEC-008 — wamacare.conf on port 8070

**Date:** 2026-05-29 | **Phase:** 4 | **Status:** ACCEPTED

**Decision:** Created dedicated `wamacare.conf` at the project root, using port 8070.

**Reason:** FamOil uses port 8069. Separate config file keeps WamaCare settings independent and avoids overwriting FamOil config at `/Users/mac/odoo17/odoo/odoo.conf`.

---

*New decisions to be added as phases progress.*
