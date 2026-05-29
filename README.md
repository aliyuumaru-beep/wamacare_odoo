# WamaCare — Odoo NGO/CBO Template

**WamaCare** is an Odoo 17 Community Edition implementation for a Nigerian Community-Based Organisation (CBO) operating maternal health, safeguarding, capacity-building, and community outreach programmes.

Beyond the single deployment, WamaCare is designed as a **reusable Odoo template** for NGOs, CBOs, humanitarian organisations, donor-funded programmes, and social-impact service delivery organisations.

---

## Quick Reference

| Item | Value |
|------|-------|
| Odoo Version | 17.0 Community Edition |
| Database | `wamacare_local` |
| Local URL | http://localhost:8069 |
| Project Root | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare` |
| GitHub | https://github.com/aliyuumaru-beep/wamacare_odoo |
| Primary Sector | NGO / CBO — Maternal Health & Safeguarding |
| Country | Nigeria (FCT Abuja) |
| Currency | NGN (₦) |

---

## Start Command

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate
python /Users/mac/odoo17/odoo/odoo-bin \
  -d wamacare_local \
  -r odoo \
  --addons-path=/Users/mac/odoo17/odoo/odoo/addons,/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/custom_addons \
  --config=/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/wamacare.conf
```

---

## Repository Structure

```
WamaCare/
├── CLAUDE.md                         ← AI session anchor (read this first)
├── README.md                         ← this file
├── .gitignore
├── docs/wamacare/                    ← all project documentation
│   ├── README.md
│   ├── REPOSITORY_SETUP.md
│   ├── PROJECT_IDENTITY.md
│   ├── TEMPLATE_STRATEGY.md
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── MODULE_REGISTRY.md
│   ├── DATA_IMPORT_PLAN.md
│   ├── BACKUP_AND_RECOVERY.md
│   ├── KNOWN_ISSUES.md
│   ├── DECISION_LOG.md
│   ├── IMPLEMENTATION_HISTORY.md
│   ├── NGO_CBO_PROCESS_MAP.md
│   ├── SECURITY_AND_PRIVACY.md
│   ├── GOVERNANCE_MODEL.md
│   ├── REUSE_GUIDE.md
│   ├── data_imports/
│   │   └── IMPORT_SEQUENCE.md
│   └── roadmap/
│       ├── MILESTONE_1_MVP.md
│       ├── MILESTONE_2_TEMPLATE_HARDENING.md
│       ├── MILESTONE_3_MULTI_ORG_REUSE.md
│       └── MILESTONE_4_COMMERCIALIZATION.md
├── csv_templates/wamacare/           ← import-ready CSV files
├── custom_addons/                    ← WamaCare-specific Odoo modules
├── scripts/                          ← backup, restore, setup scripts
├── tests/                            ← validation scripts
├── backups/                          ← backup manifests only (no dumps in Git)
│   └── BACKUP_MANIFEST.md
└── .github/workflows/                ← CI/CD (future)
```

---

## Documentation Index

| Document | Purpose |
|----------|---------|
| [CLAUDE.md](./CLAUDE.md) | AI session anchor — start here |
| [docs/wamacare/PROJECT_IDENTITY.md](docs/wamacare/PROJECT_IDENTITY.md) | What WamaCare is |
| [docs/wamacare/TEMPLATE_STRATEGY.md](docs/wamacare/TEMPLATE_STRATEGY.md) | Reuse model for other NGOs/CBOs |
| [docs/wamacare/DEPLOYMENT_GUIDE.md](docs/wamacare/DEPLOYMENT_GUIDE.md) | How to install and run |
| [docs/wamacare/MODULE_REGISTRY.md](docs/wamacare/MODULE_REGISTRY.md) | All Odoo modules used |
| [docs/wamacare/DATA_IMPORT_PLAN.md](docs/wamacare/DATA_IMPORT_PLAN.md) | CSV import sequence |
| [docs/wamacare/BACKUP_AND_RECOVERY.md](docs/wamacare/BACKUP_AND_RECOVERY.md) | Backup and restore procedures |
| [docs/wamacare/ROADMAP.md](docs/wamacare/ROADMAP.md) | What has been done and what remains |
| [docs/wamacare/KNOWN_ISSUES.md](docs/wamacare/KNOWN_ISSUES.md) | Open issues and blockers |

---

## Software Factory Principles

1. Repository memory is more important than AI memory.
2. Documentation first.
3. Backup before change.
4. No undocumented architecture change.
5. Prefer native Odoo before custom code.
6. Custom code only if native/configuration options are insufficient.
7. Every phase must leave the project more reproducible.
8. The project must survive AI failure, developer replacement, laptop loss, and future migration.
9. Use Git discipline and preserve rollback capability.
10. At the end of every phase, update CLAUDE.md.

---

## Isolation Rule

This repository is **completely independent** from FamOil and all other Odoo projects on this machine.

Never import, copy, or reference:
- `/Users/mac/odoo17/` (FamOil project)
- `Famoil` PostgreSQL database
- FamOil custom addons
- FamOil backups or filestores

---

*Generated: 2026-05-29 | WamaCare Template v0.1.0*
