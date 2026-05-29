# CLAUDE.md — WamaCare Software Factory Session Anchor
# Version: 0.1.0 | Last updated: 2026-05-29

> This file is read automatically by Claude Code at the start of every session.
> It is the single source of truth for project state. Keep it current.
> Update this file at the end of every phase before stopping.

---

## PROJECT IDENTITY

| Field | Value |
|-------|-------|
| Project Name | WamaCare |
| Organisation Type | Community-Based Organisation (CBO) |
| Sector | NGO / CBO — Maternal Health, Safeguarding, Community Outreach |
| Application | Odoo 17.0 Community Edition |
| Database Name | `wamacare_local` (pending restore from `mamacare1.dump.zip`) |
| Country | Nigeria (FCT — Abuja) |
| Currency | NGN (Nigerian Naira, ₦) |
| Deployment | Local — macOS (MacBook Air) |
| Project Directory | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare` |
| Odoo Binary | `/Users/mac/odoo17/odoo/odoo-bin` |
| Odoo Venv | `/Users/mac/odoo17/odoo/venv/` |
| GitHub | https://github.com/aliyuumaru-beep/wamacare_odoo |
| Local URL | http://localhost:8069 |

**IMPORTANT:** WamaCare is NOT a healthcare/HMO/clinic/hospital system.
It is an NGO/CBO that runs health-focused community programmes.
Do not install or configure healthcare-specific clinical modules unless proven necessary.

---

## START COMMAND

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate
python /Users/mac/odoo17/odoo/odoo-bin \
  -d wamacare_local \
  -r odoo \
  --addons-path=/Users/mac/odoo17/odoo/odoo/addons,/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/custom_addons \
  --http-port=8070
```

> Use port 8070 to avoid conflict with FamOil on 8069.

---

## ACTIVE PHASE

**Current phase:** Phase 11 COMPLETE — restore drill PASS, RTO 45 seconds. Phase 12 (final push) next.

**Completed phases:**
- [x] Phase -1 — Repository and project boundary setup
- [x] Phase 0 — Local inspection and orientation
- [x] Phase 1 — Project identity and template positioning
- [x] Phase 2 — Safe backup before work
- [x] Phase 3 — Software Factory structure created
- [x] Phase 4 — Odoo environment setup (wamacare.conf, port 8070)
- [x] Phase 5 — Database created (fresh Community — see DECISION_LOG DEC-007)

**Next phase:** Phase 12 — Final documentation, version tag, governance registration

**Database status:** `wamacare_local` — LIVE with data.
- 65 modules installed (+ l10n_ng + base_vat for Nigeria VAT/WHT)
- Currency: NGN (₦)
- Company: WamaCare (Tiko CBO), Abuja FCT, Nigeria
- 13 analytic accounts linked to 5 projects
- 68 chart of accounts (47 generic + 21 NGO/Nigeria-specific)
- 5 HR departments, 4 employees
- 5 projects/programmes
- 13 beneficiaries (BEN-004 to BEN-016, Abuja FCT)
- 17 vendors, 1 LPO (₦2.5M)
- 3 assets: Ambulance, Ultrasound, Laptop
- 15 products/services
- 5 users: admin, aliyu.umaru, finance.officer, field.officer, hr.officer
- Purchase approval: enabled, threshold ₦200,000
- Analytic accounting: ENABLED
- URL: http://localhost:8070 | admin/admin (CHANGE PASSWORD)

---

## DATABASE STATUS

**Active database:** `wamacare_local` — fresh Odoo 17 Community Edition
- 63 modules installed (Community)
- Port: 8070
- Login: http://localhost:8070
- Company name: "My Company" (to be renamed to WamaCare/Tiko in Phase 8)
- No data yet — CSV import pending (Phase 7)

**Original Enterprise dump (reference only):**
| Field | Value |
|-------|-------|
| File | `mamacare1.dump.zip` |
| Location | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/mamacare1.dump.zip` |
| Zip size | 19 MB |
| Dump date | 2025-12-29 |
| Origin | Odoo Enterprise (Odoo.sh/Ubuntu) — 284 modules |
| Status | Incompatible with local Community — NOT restored (see DEC-007) |
| Data mined | 86 contacts, 5 projects, 15 employees, 5 LPOs confirmed in dump |

---

## PROGRAMMES DETECTED (from CSV inspection)

| Programme | Status |
|-----------|--------|
| Maternal Health Outreach – Tiko | Active |
| Health Worker Capacity Program | Active |
| Safeguarding & Protection Program | Active |
| Monitoring & Evaluation Program | Active |
| Organisation-wide Support | Active |

---

## HR STRUCTURE DETECTED

| Department | Parent | Manager |
|-----------|--------|---------|
| ICT Department | — | emp_aliyu |
| Finance Department | — | emp_zainab |
| Programs Department | — | emp_musa |
| Legal & Compliance | — | emp_fatima |
| Field Operations | Programs Department | emp_sadiq |

---

## MODULES (to be confirmed after database restore)

**Expected from CSV inspection:**
- `contacts` / `base`
- `project` (programmes/projects)
- `purchase` (LPOs, vendors)
- `account` / `account_analytic` (analytic accounts per programme)
- `hr` / `hr_expense` (staff costs, expenses)
- `stock` / `stock_account` (assets, medical equipment)
- `crm` or custom beneficiary tracking

**Not yet confirmed — requires database inspection post-restore.**

---

## CSV DATA FILES AVAILABLE

| File | Target Model | Location |
|------|-------------|----------|
| `beneficiaries.csv` | `res.partner` (Beneficiary) | `csv_templates/wamacare/` |
| `projects.csv` | `project.project` | `csv_templates/wamacare/` |
| `mamacare_projects.csv` | `project.project` | `csv_templates/wamacare/` |
| `activities.csv` | `project.task` | `csv_templates/wamacare/` |
| `hr_employees.csv` | `hr.employee` | `csv_templates/wamacare/` |
| `hr_department.csv` | `hr.department` | `csv_templates/wamacare/` |
| `assets.csv` | `account.asset` or `maintenance.equipment` | `csv_templates/wamacare/` |
| `vendor.csv` | `res.partner` (Vendor) | `csv_templates/wamacare/` |
| `wamacare_vendors.csv` | `res.partner` (Vendor) | `csv_templates/wamacare/` |
| `lpo.csv` | `purchase.order` | `csv_templates/wamacare/` |
| `mamacare_analytic_accounts.csv` | `account.analytic.account` | `csv_templates/wamacare/` |
| `mamacare_expenses.csv` | `account.move` (Vendor Bill) | `csv_templates/wamacare/` |
| `mamacare_products.csv` | `product.template` | `csv_templates/wamacare/` |
| `wamacare_products.csv` | `product.template` | `csv_templates/wamacare/` |

---

## ISOLATION RULES (CRITICAL)

This project is **strictly isolated** from FamOil and all other Odoo projects.

**NEVER touch:**
- `/Users/mac/odoo17/` — FamOil project directory
- `Famoil` — FamOil PostgreSQL database
- `/Users/mac/odoo17/custom_addons/` — FamOil custom addons
- `/Users/mac/odoo_backups/` — FamOil backup archives
- `/Users/mac/oca_web/` — FamOil OCA web addons
- `OdooClean` database
- Any FamOil Git repository or GitHub remote

**WamaCare uses a separate port: 8070** (FamOil runs on 8069).

---

## CRITICAL DO NOT RULES

- DO NOT run destructive git operations (force push, history rewrite, branch delete)
- DO NOT expose passwords, API keys, or database credentials in any output
- DO NOT drop or overwrite any database without explicit operator confirmation
- DO NOT install third-party modules not found in inspection documents without approval
- DO NOT modify `/Users/mac/odoo17/odoo.conf` — that is FamOil's config
- DO NOT commit `mamacare1.dump.zip` or any dump/filestore to Git

---

## REPOSITORY STRUCTURE

```
WamaCare/                             ← Git root
├── CLAUDE.md                         ← this file
├── README.md
├── .gitignore
├── docs/wamacare/                    ← all project documentation
│   ├── REPOSITORY_SETUP.md
│   ├── PHASE_0_LOCAL_INSPECTION.md
│   ├── PROJECT_IDENTITY.md
│   ├── TEMPLATE_STRATEGY.md
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── MODULE_REGISTRY.md
│   ├── DATA_IMPORT_PLAN.md
│   ├── TESTING_GUIDE.md
│   ├── BACKUP_AND_RECOVERY.md
│   ├── IMPLEMENTATION_HISTORY.md
│   ├── DECISION_LOG.md
│   ├── KNOWN_ISSUES.md
│   ├── NGO_CBO_PROCESS_MAP.md
│   ├── SECURITY_AND_PRIVACY.md
│   ├── GOVERNANCE_MODEL.md
│   ├── REUSE_GUIDE.md
│   ├── data_imports/IMPORT_SEQUENCE.md
│   └── roadmap/
│       ├── MILESTONE_1_MVP.md
│       ├── MILESTONE_2_TEMPLATE_HARDENING.md
│       ├── MILESTONE_3_MULTI_ORG_REUSE.md
│       └── MILESTONE_4_COMMERCIALIZATION.md
├── csv_templates/wamacare/           ← 14 import-ready CSV files
├── custom_addons/                    ← WamaCare-specific Odoo modules
├── scripts/                          ← operational scripts
├── tests/                            ← validation scripts
├── backups/                          ← manifests only (no dumps in Git)
└── .github/workflows/                ← CI/CD
```

---

## KNOWN ISSUES

| # | Issue | Status |
|---|-------|--------|
| 1 | Database created fresh (Community) — CSV import pending | OPEN — Phase 7 |
| 2 | Dump was Enterprise — not compatible with local Community | RESOLVED — DEC-007 |
| 3 | Company name is "My Company" — needs rename to Tiko/WamaCare | OPEN — Phase 8 |
| 4 | No chart of accounts for Nigeria configured | OPEN — Phase 8 |
| 5 | `Untitled.rtf` in project root is junk | OPEN — do not delete without operator OK |
| 6 | No custom addons detected | OPEN — will assess post Phase 7 |
| 7 | Module checklist XLSX not yet parsed | LOW — inspect manually |

---

## ESCALATION

If Claude is unsure about any destructive action: STOP. Do not proceed.
Report the uncertainty clearly and wait for operator instruction.

**Operator:** aliyuumaru@gmail.com

---

## PHASE HISTORY

| Phase | Name | Date | Status |
|-------|------|------|--------|
| -1 | Repository and project boundary setup | 2026-05-29 | COMPLETE |
| 0 | Local inspection and orientation | 2026-05-29 | COMPLETE |
| 1 | Project identity and template positioning | 2026-05-29 | COMPLETE |
| 2 | Safe backup before work | 2026-05-29 | COMPLETE |
| 3 | Software Factory structure created | 2026-05-29 | COMPLETE |
| 4 | Local Odoo environment setup | 2026-05-29 | COMPLETE |
| 5 | Database creation (fresh Community) | 2026-05-29 | COMPLETE |
| 6 | Module detection and installation | 2026-05-29 | COMPLETE |
| 7 | Data import | 2026-05-29 | COMPLETE |
| 8 | Functional configuration | 2026-05-29 | COMPLETE |
| 9 | Roadmap and template governance | 2026-05-29 | COMPLETE (docs exist) |
| 10 | Testing and validation | 2026-05-29 | COMPLETE — 20/20 PASS |
| 11 | Backup and restore drill | 2026-05-29 | COMPLETE — PASS, RTO 45s |
| 12 | Final documentation, GitHub push, handover | — | PENDING |
