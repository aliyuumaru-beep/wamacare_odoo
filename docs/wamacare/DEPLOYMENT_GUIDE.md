# DEPLOYMENT_GUIDE.md — WamaCare Local Deployment Guide

**Date:** 2026-05-29 | **Status:** DRAFT — Phase 4 will complete this

---

## Prerequisites

| Item | Required | Notes |
|------|---------|-------|
| macOS | Yes | Tested on macOS 23.6.0 (Darwin) |
| Odoo 17.0 | Yes | At `/Users/mac/odoo17/odoo/` |
| Python venv | Yes | At `/Users/mac/odoo17/odoo/venv/` |
| PostgreSQL 16+ | Yes | Running, user `odoo` |
| Git | Yes | Repo at WamaCare root |
| `wamacare1.dump.zip` | For restore | Keep in secure local location |

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/aliyuumaru-beep/wamacare_odoo.git wamacare
cd wamacare
```

---

## Step 2 — Restore Database (if dump available)

```bash
# Unzip the dump
unzip mamacare1.dump.zip -d /tmp/wamacare_restore/

# Create target database
createdb -U odoo wamacare_local

# Restore SQL
psql -U odoo -d wamacare_local -f /tmp/wamacare_restore/dump.sql

# Restore filestore
cp -r /tmp/wamacare_restore/filestore/ \
  ~/Library/Application\ Support/Odoo/filestore/wamacare_local/

# Clean up
rm -rf /tmp/wamacare_restore/
```

---

## Step 3 — Create Config File

Create `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/wamacare.conf`:

```ini
[options]
db_name = wamacare_local
db_user = odoo
db_host = False
db_port = False
http_port = 8070
addons_path = /Users/mac/odoo17/odoo/odoo/addons,/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/custom_addons
log_level = info
```

> **Security note:** Do NOT add `admin_passwd` or `db_password` to this file if committing nearby. The conf file is excluded from Git via `.gitignore`.

---

## Step 4 — Start Odoo

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate
python /Users/mac/odoo17/odoo/odoo-bin \
  -d wamacare_local \
  -r odoo \
  --config=/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/wamacare.conf
```

Open: http://localhost:8070

---

## Step 5 — Fresh Database (if no dump)

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate
python /Users/mac/odoo17/odoo/odoo-bin \
  -d wamacare_local \
  -r odoo \
  --addons-path=/Users/mac/odoo17/odoo/odoo/addons,/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/custom_addons \
  --http-port=8070 \
  -i base,contacts,project,purchase,account,hr,hr_expense,maintenance
```

---

## Isolation Check

Before starting WamaCare, confirm FamOil is NOT running on 8070:
```bash
lsof -i :8070
```
If something is running on 8070, stop it or choose a different port and update `wamacare.conf`.

---

## Stopping WamaCare

```bash
# Find the process
lsof -i :8070
# Kill it
kill <PID>
```

---

*Full deployment guide will be completed in Phase 4.*
