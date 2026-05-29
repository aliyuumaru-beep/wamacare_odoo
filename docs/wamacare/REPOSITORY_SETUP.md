# REPOSITORY_SETUP.md — WamaCare Git and Project Boundary Setup

**Phase:** -1 | **Date:** 2026-05-29 | **Status:** COMPLETE

---

## Local Project Path

| Item | Value |
|------|-------|
| Absolute path | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare` |
| Git root | Same as above |
| Original folder alias | `mac-documents-aliyu-odoo-projects-tiko` |
| Parent folder | `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/` |
| Platform | macOS 23.6.0 (Darwin) |

---

## Git Initialisation

| Item | Value |
|------|-------|
| Initialised | 2026-05-29 |
| Default branch | `main` |
| Remote name | `origin` |
| Remote URL | https://github.com/aliyuumaru-beep/wamacare_odoo |
| Repo state at init | Empty repository (no prior commits) |
| GitHub repo state | Existed but empty (diskUsage=0, isEmpty=true) |
| Push status | Pending Phase -1 commit |

---

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready documentation and configuration |
| `dev` | Active development and phase work |
| `phase/<n>-<name>` | Optional: one branch per phase for isolation |

**Policy:** All phase work happens on `dev` or a phase branch. Merge to `main` only when phase is validated and complete. Never force-push to `main`.

---

## Isolation Rules

This repository is **strictly isolated** from FamOil and all other Odoo projects.

### What must NEVER be in this repository

| Item | Reason |
|------|--------|
| FamOil files, scripts, or addons | Different project — strict isolation |
| `/Users/mac/odoo17/` contents | FamOil project root |
| `Famoil` database dumps | FamOil data — not WamaCare |
| `OdooClean` database | FamOil staging database |
| Credentials, passwords, tokens | Security — never commit secrets |
| `mamacare1.dump.zip` | Large binary — tracked externally |
| `*.dump`, `*.sql`, filestore | Large binaries — excluded in .gitignore |
| `.DS_Store` | macOS noise |

### What this repository MUST contain

| Item | Purpose |
|------|---------|
| `CLAUDE.md` | AI session anchor |
| `README.md` | Human entry point |
| `docs/wamacare/` | All project documentation |
| `csv_templates/wamacare/` | Import-ready data templates |
| `custom_addons/` | WamaCare-specific Odoo modules |
| `scripts/` | Backup, restore, setup scripts |
| `tests/` | Validation scripts |
| `backups/BACKUP_MANIFEST.md` | Backup metadata (not binary dumps) |

---

## What Was Found on Inspection

| Item | Finding |
|------|---------|
| Git repository | None — initialized fresh on 2026-05-29 |
| GitHub remote | Existed but empty |
| FamOil files | None found in TIKO/WamaCare folder |
| Credentials in files | None found |
| Large binaries | `mamacare1.dump.zip` (19MB) — excluded from Git |
| Junk file | `Untitled.rtf` — kept, not deleted (contains test text, not project data) |

---

## Initial Risks

| Risk | Mitigation |
|------|-----------|
| Accidental FamOil contamination | `.gitignore`, isolation rules in CLAUDE.md |
| Credential exposure | `.gitignore` excludes all `.conf`, `.env` files |
| Database dump in Git | `.gitignore` excludes all `*.dump`, `*.sql`, `*.zip` in backups |
| Broken restore if dump is deleted | Document dump location and hash in BACKUP_MANIFEST.md |
| WamaCare port conflict with FamOil | WamaCare uses port 8070; FamOil uses 8069 |

---

## How to Clone and Resume on a New Machine

```bash
git clone https://github.com/aliyuumaru-beep/wamacare_odoo.git wamacare
cd wamacare
# Read CLAUDE.md first
# Obtain mamacare1.dump.zip from secure backup location
# Follow docs/wamacare/DEPLOYMENT_GUIDE.md
```

---

*Phase -1 complete. Repository initialized. Remote set. Isolation documented.*
