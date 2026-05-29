# ARCHITECTURE.md — WamaCare Technical Architecture

**Date:** 2026-05-29 | **Status:** DRAFT (Phase 5 will confirm after database restore)

---

## Deployment Architecture

```
MacBook Air (macOS 23.6.0)
│
├── PostgreSQL 16.11 (shared, user: odoo)
│   ├── Famoil          ← FamOil (DO NOT TOUCH)
│   └── wamacare_local  ← WamaCare (this project)
│
├── Odoo 17.0 — /Users/mac/odoo17/odoo/
│   └── venv: /Users/mac/odoo17/odoo/venv/
│
├── WamaCare Project Root
│   └── /Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/
│       ├── custom_addons/    ← WamaCare-specific modules
│       ├── scripts/          ← operational scripts
│       └── backups/          ← backup manifests
│
└── Filestore
    └── ~/Library/Application Support/Odoo/filestore/wamacare_local/
```

---

## Port Assignments

| Service | Port | Database | Notes |
|---------|------|---------|-------|
| FamOil Odoo | 8069 | Famoil | DO NOT CHANGE |
| WamaCare Odoo | 8070 | wamacare_local | Avoids conflict |

---

## Addons Path (WamaCare)

```
/Users/mac/odoo17/odoo/odoo/addons      ← Odoo core
/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/custom_addons  ← WamaCare custom
```

---

## Data Architecture

### Beneficiary Model
- Stored as `res.partner` with category tag `Beneficiary`
- Programme association via partner tags
- No dedicated clinical model — NGO/CBO pattern only

### Programme Model
- `project.project` — one project per programme
- `account.analytic.account` — one analytic account per programme
- Expenses, purchases, and activities linked to analytic accounts

### Procurement Model
- `purchase.order` = Local Purchase Order (LPO)
- Vendor master via `res.partner` (type: vendor)
- Approval workflow configured in Odoo purchase settings

### HR Model
- `hr.department` — 5 departments
- `hr.employee` — field staff, health workers, admin
- `hr.expense` or `account.move` for staff expense claims

### Asset Model
- `maintenance.equipment` or `account.asset` (to be confirmed after restore)
- Fixed assets: Ambulance, Ultrasound, Laptops

---

## Security Architecture

- Role-based access control via Odoo user groups
- Beneficiary data restricted to Programs and Field Operations roles
- Finance data restricted to Finance role
- Admin/Manager role: full access
- No patient-level clinical records — CBO-appropriate privacy model

See: [SECURITY_AND_PRIVACY.md](./SECURITY_AND_PRIVACY.md)

---

## Backup Architecture

| Component | Method | Location |
|-----------|--------|---------|
| Database | `pg_dump` (custom format) | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/backups/` |
| Filestore | `cp -r` or `tar.gz` | Same backup folder |
| Config | Sanitised copy | Same backup folder |
| Code/Docs | Git push | GitHub |
| Offsite | Manual/cloud (future) | TBD |

---

*Architecture to be updated after Phase 5 database restore confirms module list.*
