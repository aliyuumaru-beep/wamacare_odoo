# BACKUP_MANIFEST.md — WamaCare Pre-Setup Backup

**Backup date:** 2026-05-29 07:47  
**Phase:** 2 — Safe Backup Before Work  
**Purpose:** Snapshot of all original WamaCare files before Phase 3 structure creation

---

## Files Included

| File | Type | Notes |
|------|------|-------|
| `CBO_Mandate_and_Odoo_Deliverables_Tiko.docx` | Word document | CBO mandate and Odoo deliverables |
| `DashBoard Executive.png` | PNG image | Dashboard screenshot |
| `Story_Telling_wamaCare.pdf` | PDF | Programme storytelling document |
| `hr_department.txt` | Text (CSV format) | HR departments |
| `wamacare_prompt_setup_and_build_claude_code_prompt.txt` | Text | Original Claude setup prompt |
| `Odoo_demo_wamaCare/` | Folder | Complete demo folder with XLSX and 14 CSVs |

---

## Files NOT Included (and Why)

| File | Reason |
|------|--------|
| `mamacare1.dump.zip` (19MB) | Too large; stays in project root; documented separately |
| `Untitled.rtf` | Junk file with test text — no project value |
| `.DS_Store` | macOS metadata — not backed up |

---

## Database Dump Reference

| Item | Value |
|------|-------|
| Dump file | `mamacare1.dump.zip` |
| Location | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/mamacare1.dump.zip` |
| Size | 19 MB (zip) / 47 MB (SQL) |
| Filestore files | ~1,271 |
| Date | 2025-12-29 |
| Format | ZIP: `dump.sql` + `filestore/` |
| Git status | EXCLUDED from Git |

---

## Odoo Version Detected

| Item | Value |
|------|-------|
| Odoo binary | `/Users/mac/odoo17/odoo/odoo-bin` |
| Version | 17.0 |
| Database name (proposed) | `wamacare_local` |

---

## Restore Notes

If starting from scratch:
1. Obtain `mamacare1.dump.zip` from project root or secure backup location
2. Follow `docs/wamacare/BACKUP_AND_RECOVERY.md` restore procedure
3. If dump is lost, import from CSV templates in `csv_templates/wamacare/`

---

## Risks

| Risk | Notes |
|------|-------|
| `mamacare1.dump.zip` is the only database backup | Keep a second copy outside the project folder |
| Dump is 2025-12-29 — 5 months old | May not reflect latest WamaCare configuration |
| Dump Odoo version unconfirmed | Verify on restore |

---

*Backup created as part of Phase 2 — Safe Backup Before Work.*
