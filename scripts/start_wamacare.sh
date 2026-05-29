#!/bin/bash
# WamaCare Odoo Startup Script
# Database: wamacare_local | Port: 8070
# Run from any directory. Do NOT run as root.

WROOT="/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare"
ODOO_BIN="/Users/mac/odoo17/odoo/odoo-bin"
VENV="/Users/mac/odoo17/odoo/venv/bin/activate"
CONFIG="$WROOT/wamacare.conf"

# Safety check: never start against FamOil database
if grep -q "db_name = Famoil" "$CONFIG" 2>/dev/null; then
  echo "ERROR: Config points to Famoil database. Aborting."
  exit 1
fi

# Check port 8070 is free
if lsof -i :8070 > /dev/null 2>&1; then
  echo "ERROR: Port 8070 is already in use. Stop the existing service first."
  lsof -i :8070
  exit 1
fi

source "$VENV"
python "$ODOO_BIN" -d wamacare_local -r odoo --config="$CONFIG"
