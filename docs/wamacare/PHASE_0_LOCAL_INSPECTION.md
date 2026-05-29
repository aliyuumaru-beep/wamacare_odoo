# PHASE_0_LOCAL_INSPECTION.md — WamaCare Local Inspection Report

**Phase:** 0 | **Date:** 2026-05-29 | **Status:** COMPLETE

---

## 1. Project Folder

| Item | Value |
|------|-------|
| Resolved path | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare` |
| Parent | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/` |
| Platform | macOS Darwin 23.6.0 |
| Git status | NOT a git repository (initialized in Phase -1) |

---

## 2. Full Folder Structure (at inspection)

```
TIKO/
├── 03_CBO_Digital_and_Structural_Transformation.pptx    ← CBO transformation deck
├── We_R_IT_TIKO_Executive_Summary_and_ERP.pptx.pdf      ← executive summary
└── WamaCare/                                             ← Git root (from Phase -1)
    ├── CBO_Mandate_and_Odoo_Deliverables_Tiko.docx       ← CBO mandate document
    ├── DashBoard Executive.png                            ← dashboard screenshot
    ├── Story_Telling_wamaCare.pdf                         ← programme storytelling doc
    ├── Untitled.rtf                                       ← junk file (test text)
    ├── hr_department.txt                                  ← HR department CSV data
    ├── mamacare1.dump.zip                                 ← DATABASE DUMP (19MB)
    ├── wamacare_prompt_setup_and_build_claude_code_prompt.txt ← original setup prompt
    └── Odoo_demo_wamaCare/
        ├── DashBoard Executive.png                        ← duplicate screenshot
        ├── Odoo_module_checklist.xlsx                     ← module checklist
        └── CBO_Odoo_Demo_CSVs/
            ├── activities.csv
            ├── assets.csv
            ├── beneficiaries.csv
            ├── hr_employees.csv
            ├── lpo.csv
            ├── mamacare_analytic_accounts.csv
            ├── mamacare_expenses.csv
            ├── mamacare_products.csv
            ├── mamacare_projects.csv
            ├── projects.csv
            ├── vendor.csv
            ├── wamacare_products.csv
            └── wamacare_vendors.csv
```

---

## 3. Git Repository Status

| Item | Value |
|------|-------|
| Git repo at inspection | None |
| Initialized in Phase -1 | Yes — 2026-05-29 |
| Branch | `main` |
| Remote | `https://github.com/aliyuumaru-beep/wamacare_odoo` |

---

## 4. Odoo Environment

| Item | Value |
|------|-------|
| Odoo binary | `/Users/mac/odoo17/odoo/odoo-bin` |
| Odoo version | 17.0 |
| Python | `/usr/bin/python3` (system) + venv at `/Users/mac/odoo17/odoo/venv/` |
| PostgreSQL | Running (psql accessible, user `odoo`) |
| PostgreSQL version | 16.11 |
| Odoo config | `/Users/mac/odoo17/odoo/odoo.conf` (FamOil — **do not modify**) |
| Active port | 8069 (FamOil) |
| WamaCare port | 8070 (proposed, avoids conflict) |

---

## 5. Existing Databases (full list)

| Database | Owner | Notes |
|----------|-------|-------|
| `Famoil` | odoo | **FamOil ERP — DO NOT TOUCH** |
| `OdooClean` | odoo | FamOil staging — DO NOT TOUCH |
| `OdooTest` | odoo | Test DB |
| `Odootest` | mac | Test DB |
| `aedc_demo` | odoo | AEDC demo DB |
| `odoo` | odoo | Unknown |
| `odoo_farm` | odoo | Farm project DB |
| `your_db_name` | mac | Placeholder/unused |
| `wamacare_local` | — | **Does not exist yet — target for Phase 5** |

---

## 6. Database Dump

| Item | Value |
|------|-------|
| File | `mamacare1.dump.zip` |
| Size (zipped) | 19 MB |
| Size (SQL dump) | 47 MB (`dump.sql`) |
| Filestore files | ~1,271 files in `filestore/` folder |
| Dump date | 2025-12-29 22:34 |
| Format | ZIP archive: `dump.sql` (plain SQL) + `filestore/` (Odoo attachments) |
| Suspected Odoo version | 17.0 (consistent with platform) |
| DB name in dump | Unknown — will be confirmed on restore |
| Restore target | `wamacare_local` (pending operator confirmation) |
| Git status | Excluded from Git (in `.gitignore`) |

---

## 7. CSV / Data Import Files

| File | Rows (approx) | Target Model | Notes |
|------|--------------|-------------|-------|
| `beneficiaries.csv` | 13 | `res.partner` | BEN-004 to BEN-016, female beneficiaries, Abuja FCT |
| `projects.csv` | 3 | `project.project` | Maternal Health, Protection, Women Entrepreneurship |
| `mamacare_projects.csv` | 5 | `project.project` | 5 WamaCare programmes |
| `activities.csv` | 1 | `project.task` | ANC Outreach, ₦2.5M budget |
| `hr_employees.csv` | 4 | `hr.employee` | Field Officer, Nurse, Safeguarding Lead, Mobilizer |
| `hr_department.txt` | 5 | `hr.department` | ICT, Finance, Programs, Legal, Field Ops |
| `assets.csv` | 3 | `maintenance.equipment`/`account.asset` | Ambulance, Ultrasound, Laptop |
| `vendor.csv` | 2 | `res.partner` (vendor) | Health Supplies Ltd, Community Services Co |
| `wamacare_vendors.csv` | 15 | `res.partner` (vendor) | 15 specialist vendors |
| `lpo.csv` | 1 | `purchase.order` | LPO-001, ANC Outreach – Kubwa, ₦2.5M |
| `mamacare_analytic_accounts.csv` | 13 | `account.analytic.account` | Per programme accounts |
| `mamacare_expenses.csv` | 1 | `account.move` (bill) | MC-EXP-002, GreenPower, ₦1.85M |
| `mamacare_products.csv` | 15 | `product.template` | Services (Delivery Kits, ANC, Training, etc.) |
| `wamacare_products.csv` | 10 | `product.template` | Diagnostic, Staff Costs, Insurance, IT, etc. |

**All CSV files copied to `csv_templates/wamacare/` for import use.**

---

## 8. Documentation Files

| File | Type | Notes |
|------|------|-------|
| `CBO_Mandate_and_Odoo_Deliverables_Tiko.docx` | Word | CBO mandate and Odoo deliverables spec |
| `Story_Telling_wamaCare.pdf` | PDF | Programme storytelling / impact narrative |
| `03_CBO_Digital_and_Structural_Transformation.pptx` | PowerPoint | CBO digital transformation deck |
| `We_R_IT_TIKO_Executive_Summary_and_ERP.pptx.pdf` | PDF | Executive summary and ERP overview |
| `Odoo_demo_wamaCare/Odoo_module_checklist.xlsx` | Excel | Module checklist (not yet parsed) |
| `wamacare_prompt_setup_and_build_claude_code_prompt.txt` | Text | Original Claude Code setup prompt |
| `hr_department.txt` | Text | HR departments in CSV format |

---

## 9. Custom Addons

**None found.** No `__manifest__.py` files detected in the project folder.
WamaCare does not have custom Odoo modules at this stage.

---

## 10. Scripts

**None found.** No `.sh`, `.py` scripts in the project folder at inspection.
Scripts will be created in Phase 4 and Phase 11.

---

## 11. Config Files

**None found.** No `odoo.conf` or `wamacare.conf` in the project folder.
A dedicated `wamacare.conf` will be created in Phase 4.

---

## 12. Project Identity Evidence

| Evidence | Inference |
|----------|----------|
| Beneficiaries tagged "Maternal Health", "Protection", "Community Outreach" | NGO/CBO focus, not clinical |
| Programmes: Maternal Health Outreach, Safeguarding, Capacity Building, M&E | Humanitarian/development CBO |
| Beneficiaries are female, in Abuja FCT locations | Women-focused community programme |
| Assets: Ambulance, Ultrasound — but managed as CBO assets, not patient records | Field operations, not hospital |
| Products are all "Service" type — no dispensing, prescription, or clinical coding | NGO programme services |
| Vendors include health trainers, diagnostics suppliers, NGOs | Programme procurement, not pharmacy |
| Analytic accounts named after programmes (not cost centres or departments) | Donor/programme fund tracking |
| LPO model used (Local Purchase Order) | Nigerian procurement norm |
| Currency context: NGN (₦) | Nigeria-based |
| "Tiko" appears in programme name "Maternal Health Outreach – Tiko" | Tiko = the client CBO name |

**Conclusion:** WamaCare is an **NGO/CBO Odoo implementation** for a Nigerian CBO (Tiko) focused on maternal health and safeguarding. It is NOT a hospital, clinic, HMO, or pharmacy system. Healthcare references are limited to programme services delivered by the CBO.

---

## 13. References to Database Name, Odoo Version, Ports, Credentials

| Reference | Value | Source |
|-----------|-------|--------|
| Dump filename | `mamacare1` | `mamacare1.dump.zip` |
| Odoo version | 17.0 (inferred from platform) | `/Users/mac/odoo17/odoo/odoo-bin --version` |
| Port | 8069 (FamOil) → 8070 (WamaCare proposed) | Odoo config inspection |
| Credentials | None found in project files | Inspection |
| DB name in dump | Unknown — confirm on restore | `dump.sql` not inspected |

---

## 14. FamOil Contamination Check

| Check | Result |
|-------|--------|
| FamOil files in TIKO folder | **None found** |
| FamOil database references | **None found** |
| FamOil addons | **None found** |
| FamOil-specific config | **None found** |

**PASS — No FamOil contamination detected.**

---

## 15. Blockers and Risks

| # | Blocker/Risk | Priority |
|---|-------------|---------|
| 1 | Database dump (`mamacare1.dump.zip`) not yet restored | HIGH |
| 2 | Odoo version in dump not confirmed | MEDIUM |
| 3 | Module checklist XLSX not parsed (no CLI XLSX reader) | LOW |
| 4 | `Untitled.rtf` is junk — kept pending operator decision | LOW |
| 5 | No wamacare.conf created yet | MEDIUM |
| 6 | No WamaCare-specific custom addons found | LOW |

---

*Phase 0 inspection complete. No changes made to existing files during inspection.*
