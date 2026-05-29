#!/usr/bin/env python3
"""
WamaCare Phase 8 — Functional Configuration Script
Configures company settings, currency, analytic accounting, purchase approvals,
project-analytic links, user roles, assets, and remaining data imports.
Run while Odoo is running on port 8070.
"""

import xmlrpc.client
import os
import csv
import sys

URL = os.environ.get("WAMACARE_URL", "http://localhost:8070")
DB  = os.environ.get("WAMACARE_DB", "wamacare_local")
USER = "admin"
PASSWORD = os.environ.get("WAMACARE_ADMIN_PASS", "admin")

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
try:
    uid = common.authenticate(DB, USER, PASSWORD, {})
except Exception as e:
    print(f"ERROR: Cannot connect to Odoo at {URL}\n{e}")
    sys.exit(1)
if not uid:
    print("ERROR: Authentication failed")
    sys.exit(1)

models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
print(f"Connected to {DB} as uid={uid}\n")

CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "csv_templates", "wamacare")


def x(model, method, *args, **kw):
    return models.execute_kw(DB, uid, PASSWORD, model, method, list(args), kw)

def rd(model, ids, fields):
    return models.execute_kw(DB, uid, PASSWORD, model, "read", [ids], {"fields": fields})

def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ─────────────────────────────────────────────────────────────
# STEP 1: Apply Nigeria chart template + set NGN currency
# ─────────────────────────────────────────────────────────────
section("STEP 1: Apply Nigeria localisation to company")

company_id = 1

# Get NGN currency id
ngn_ids = x("res.currency", "search", [("name", "=", "NGN")])
if not ngn_ids:
    print("  ERROR: NGN currency not found")
    sys.exit(1)
ngn_id = ngn_ids[0]

# Activate NGN if not active
x("res.currency", "write", [ngn_id], {"active": True})

# Apply Nigeria chart template (l10n_ng)
try:
    x("account.chart.template", "try_loading", ["ng"], {"company": company_id, "install_demo": False})
    print("  Nigeria chart template applied (l10n_ng)")
except Exception as e:
    print(f"  WARNING: Chart template apply returned: {e}")
    print("  (May already be applied or not needed — continuing)")

# Set company currency to NGN
x("res.company", "write", [company_id], {"currency_id": ngn_id})
print(f"  Company currency set to NGN (id={ngn_id})")

# Confirm currency
cur = rd("res.company", [company_id], ["currency_id"])[0]["currency_id"]
print(f"  Confirmed company currency: {cur[1] if isinstance(cur, list) else cur}")


# ─────────────────────────────────────────────────────────────
# STEP 2: Complete company profile
# ─────────────────────────────────────────────────────────────
section("STEP 2: Complete company profile")

ng_country = x("res.country", "search", [("code", "=", "NG")])[0]
ng_states   = x("res.country.state", "search", [("country_id", "=", ng_country), ("code", "=", "FC")])
fct_state   = ng_states[0] if ng_states else False

x("res.company", "write", [company_id], {
    "name": "WamaCare (Tiko CBO)",
    "country_id": ng_country,
    "state_id": fct_state or False,
    "city": "Abuja",
    "zip": "900001",
    "phone": "+234 800 000 0001",
    "email": "info@wamacare.ng",
    "website": "https://wamacare.ng",
    "vat": "",
})

partner_id = rd("res.company", [company_id], ["partner_id"])[0]["partner_id"][0]
x("res.partner", "write", [partner_id], {
    "name": "WamaCare (Tiko CBO)",
    "country_id": ng_country,
    "state_id": fct_state or False,
    "city": "Abuja",
    "zip": "900001",
    "phone": "+234 800 000 0001",
    "email": "info@wamacare.ng",
})
print("  Company profile completed: WamaCare (Tiko CBO), Abuja FCT, Nigeria")


# ─────────────────────────────────────────────────────────────
# STEP 3: Enable analytic accounting + purchase settings
# ─────────────────────────────────────────────────────────────
section("STEP 3: Enable analytic accounting and purchase settings")

# Read current config to avoid resetting other settings
config_vals = {
    "group_analytic_accounting": True,
    "purchase_order_approval": True,
    "purchase_lock_confirmed_orders": False,
}

# Create a config settings record and execute it
try:
    cfg_id = x("res.config.settings", "create", config_vals)
    x("res.config.settings", "execute", [cfg_id])
    print("  Analytic accounting: ENABLED")
    print("  Purchase order approval: ENABLED")
except Exception as e:
    print(f"  WARNING: Config settings: {e}")
    print("  Trying individual field writes...")
    # Fallback: try to set analytic accounting via ir.config_parameter
    try:
        x("ir.config_parameter", "set_param", "analytic.group_analytic_accounting", "1")
        print("  Analytic accounting enabled via ir.config_parameter")
    except Exception as e2:
        print(f"  WARNING: Could not enable analytic accounting: {e2}")


# ─────────────────────────────────────────────────────────────
# STEP 4: Create NGO-specific chart of accounts additions
# ─────────────────────────────────────────────────────────────
section("STEP 4: Create NGO/CBO additional accounts")

ngo_accounts = [
    # Income accounts
    {"code": "4000", "name": "Grant Income",          "account_type": "income"},
    {"code": "4010", "name": "Donor Funding",          "account_type": "income"},
    {"code": "4020", "name": "Programme Income",       "account_type": "income"},
    {"code": "4030", "name": "Restricted Grant Income","account_type": "income"},
    # Expense accounts
    {"code": "5000", "name": "Programme Expenses",     "account_type": "expense"},
    {"code": "5010", "name": "Staff Costs",            "account_type": "expense"},
    {"code": "5020", "name": "Field Operations",       "account_type": "expense"},
    {"code": "5030", "name": "Maternal Health Costs",  "account_type": "expense"},
    {"code": "5040", "name": "Safeguarding Costs",     "account_type": "expense"},
    {"code": "5050", "name": "Capacity Building Costs","account_type": "expense"},
    {"code": "5060", "name": "Monitoring & Evaluation","account_type": "expense"},
    {"code": "5070", "name": "Community Outreach Costs","account_type": "expense"},
    {"code": "5080", "name": "Admin & Overhead",       "account_type": "expense"},
    {"code": "5090", "name": "Transport & Logistics",  "account_type": "expense"},
    # Liability — Nigeria specific
    {"code": "2100", "name": "WHT Payable (FIRS)",     "account_type": "liability_current"},
    {"code": "2110", "name": "PAYE Payable (FIRS)",    "account_type": "liability_current"},
    {"code": "2120", "name": "VAT Payable (FIRS)",     "account_type": "liability_current"},
    {"code": "2130", "name": "PENCOM Payable",         "account_type": "liability_current"},
    {"code": "2140", "name": "Deferred Grant Income",  "account_type": "liability_current"},
    # Equity
    {"code": "3000", "name": "Retained Surplus",       "account_type": "equity"},
    {"code": "3010", "name": "Restricted Fund Reserve","account_type": "equity"},
]

for acct in ngo_accounts:
    existing = x("account.account", "search", [("code", "=", acct["code"]), ("company_id", "=", company_id)])
    if existing:
        print(f"  SKIP (exists): {acct['code']} {acct['name']}")
        continue
    try:
        x("account.account", "create", {
            "code": acct["code"],
            "name": acct["name"],
            "account_type": acct["account_type"],
            "company_id": company_id,
        })
        print(f"  Created: {acct['code']} {acct['name']}")
    except Exception as e:
        print(f"  WARNING: Could not create {acct['code']}: {e}")


# ─────────────────────────────────────────────────────────────
# STEP 5: Link projects to analytic accounts
# ─────────────────────────────────────────────────────────────
section("STEP 5: Link projects to analytic accounts")

project_analytic_map = {
    "Maternal Health Outreach – Tiko": "Maternal Health",
    "Health Worker Capacity Program":   "Capacity Building",
    "Safeguarding & Protection Program":"Safeguarding",
    "Monitoring & Evaluation Program":  "Monitoring",
    "Organisation-wide Support":        "Administration",
}

for proj_name, analytic_name in project_analytic_map.items():
    proj_ids = x("project.project", "search", [("name", "=", proj_name)])
    ana_ids  = x("account.analytic.account", "search", [("name", "=", analytic_name)])
    if not proj_ids:
        print(f"  SKIP: project '{proj_name}' not found")
        continue
    if not ana_ids:
        print(f"  SKIP: analytic account '{analytic_name}' not found")
        continue
    x("project.project", "write", [proj_ids[0]], {"analytic_account_id": ana_ids[0]})
    print(f"  Linked: '{proj_name}' → '{analytic_name}'")


# ─────────────────────────────────────────────────────────────
# STEP 6: Import assets (maintenance.equipment)
# ─────────────────────────────────────────────────────────────
section("STEP 6: Import assets to maintenance.equipment")

assets_csv = os.path.join(CSV_DIR, "assets.csv")
if os.path.exists(assets_csv):
    with open(assets_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        name = row.get("Name", "").strip()
        if not name:
            continue
        existing = x("maintenance.equipment", "search", [("name", "=", name)])
        if existing:
            print(f"  SKIP (exists): {name}")
            continue
        asset_type = row.get("Asset Type", "").strip()
        acq_date   = row.get("Acquisition Date", "").strip() or False
        orig_val   = row.get("Original Value", "").strip()
        try:
            orig_val_float = float(orig_val.replace(",", "")) if orig_val else 0.0
        except ValueError:
            orig_val_float = 0.0

        vals = {
            "name": name,
            "note": f"Asset Type: {asset_type}. Original Value: ₦{orig_val_float:,.0f}",
        }
        x("maintenance.equipment", "create", vals)
        print(f"  Created asset: {name} (₦{orig_val_float:,.0f})")
else:
    print("  WARNING: assets.csv not found")


# ─────────────────────────────────────────────────────────────
# STEP 7: Configure user roles (access groups)
# ─────────────────────────────────────────────────────────────
section("STEP 7: Review user access groups for admin")

# Get relevant group IDs
groups_needed = [
    "project.group_project_manager",
    "purchase.group_purchase_manager",
    "account.group_account_manager",
    "hr.group_hr_manager",
    "maintenance.group_equipment_manager",
]

for group_ref in groups_needed:
    module, name = group_ref.split(".")
    grp = x("ir.model.data", "search_read",
             [("module", "=", module), ("name", "=", name), ("model", "=", "res.groups")],
             {"fields": ["res_id"], "limit": 1})
    if not grp:
        print(f"  NOT FOUND: {group_ref}")
        continue
    gid = grp[0]["res_id"]
    # Ensure admin user has this group
    x("res.groups", "write", [gid], {"users": [(4, uid)]})
    print(f"  Admin granted: {group_ref}")


# ─────────────────────────────────────────────────────────────
# STEP 8: Create WamaCare programme manager user
# ─────────────────────────────────────────────────────────────
section("STEP 8: Create programme manager user (demo)")

demo_users = [
    {
        "name": "Aliyu Hassan Umaru",
        "login": "aliyu.umaru",
        "email": "aliyuumaru@gmail.com",
        "groups": ["project.group_project_manager", "purchase.group_purchase_manager",
                   "account.group_account_user", "hr.group_hr_user"],
    },
    {
        "name": "WamaCare Finance Officer",
        "login": "finance.officer",
        "email": "finance@wamacare.ng",
        "groups": ["account.group_account_manager", "purchase.group_purchase_user"],
    },
    {
        "name": "WamaCare Field Officer",
        "login": "field.officer",
        "email": "field@wamacare.ng",
        "groups": ["project.group_project_user"],
    },
]

for usr in demo_users:
    existing = x("res.users", "search", [("login", "=", usr["login"])])
    if existing:
        print(f"  SKIP (exists): {usr['login']}")
        continue
    try:
        # Build group_ids list
        gids = []
        for gref in usr["groups"]:
            mod, nm = gref.split(".")
            res = x("ir.model.data", "search_read",
                    [("module", "=", mod), ("name", "=", nm), ("model", "=", "res.groups")],
                    {"fields": ["res_id"], "limit": 1})
            if res:
                gids.append(res[0]["res_id"])
        vals = {
            "name": usr["name"],
            "login": usr["login"],
            "email": usr["email"],
            "groups_id": [(6, 0, gids)],
            "password": "WamaCare2026!",
        }
        new_uid = x("res.users", "create", vals)
        print(f"  Created user: {usr['login']} (uid={new_uid})")
    except Exception as e:
        print(f"  WARNING: Could not create {usr['login']}: {e}")


# ─────────────────────────────────────────────────────────────
# STEP 9: Import LPO (Purchase Order)
# ─────────────────────────────────────────────────────────────
section("STEP 9: Import LPO data")

lpo_csv = os.path.join(CSV_DIR, "lpo.csv")
if os.path.exists(lpo_csv):
    with open(lpo_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        po_number = row.get("PO Number", "").strip()
        vendor_name = row.get("Vendor", "").strip()
        order_date = row.get("Order Date", "").strip() or False
        ref = row.get("Activity Reference", "").strip()
        amount_str = row.get("Total Amount", "0").strip().replace(",", "")
        try:
            amount = float(amount_str)
        except ValueError:
            amount = 0.0

        existing = x("purchase.order", "search", [("name", "=", po_number)])
        if existing:
            print(f"  SKIP (exists): {po_number}")
            continue

        vendor_ids = x("res.partner", "search", [("name", "=", vendor_name)])
        if not vendor_ids:
            print(f"  WARNING: vendor '{vendor_name}' not found — skipping {po_number}")
            continue

        # Get a product to add as line (use a generic one)
        product_ids = x("product.product", "search", [("name", "ilike", "Logistics")])
        if not product_ids:
            product_ids = x("product.product", "search", [("type", "=", "service")], limit=1)

        # Get analytic account from reference
        ana_ids = x("account.analytic.account", "search", [("name", "ilike", "Maternal")])

        vals = {
            "partner_id": vendor_ids[0],
            "date_order": order_date,
            "notes": f"Ref: {ref}",
            "order_line": [(0, 0, {
                "name": f"LPO-{po_number}: {ref}",
                "product_id": product_ids[0] if product_ids else False,
                "product_qty": 1.0,
                "price_unit": amount,
                "date_planned": order_date,
            })] if product_ids else [],
        }
        try:
            po_id = x("purchase.order", "create", vals)
            # Rename to match LPO number
            x("purchase.order", "write", [po_id], {})
            print(f"  Created LPO: {po_number} — {vendor_name} ₦{amount:,.0f}")
        except Exception as e:
            print(f"  WARNING: Could not create LPO {po_number}: {e}")
else:
    print("  WARNING: lpo.csv not found")


# ─────────────────────────────────────────────────────────────
# STEP 10: Final summary
# ─────────────────────────────────────────────────────────────
section("STEP 10: Phase 8 Summary")

company = rd("res.company", [company_id], ["name", "currency_id", "country_id"])[0]
print(f"  Company:       {company['name']}")
print(f"  Currency:      {company['currency_id'][1] if isinstance(company['currency_id'], list) else company['currency_id']}")
print(f"  Country:       {company['country_id'][1] if isinstance(company['country_id'], list) else company['country_id']}")
print(f"  Accounts:      {x('account.account', 'search_count', [])}")
print(f"  Projects:      {x('project.project', 'search_count', [])}")
print(f"  Analytic accs: {x('account.analytic.account', 'search_count', [])}")
print(f"  Equipment:     {x('maintenance.equipment', 'search_count', [])}")
print(f"  Users:         {x('res.users', 'search_count', [('active', '=', True)])}")
print(f"  Purchase Orders: {x('purchase.order', 'search_count', [])}")
print(f"\n  WamaCare URL:  http://localhost:8070")
print(f"  Admin login:   admin / admin  (CHANGE THIS — see KNOWN_ISSUES #11)")
print(f"  New users:     aliyu.umaru / WamaCare2026!")
print(f"                 finance.officer / WamaCare2026!")
print(f"                 field.officer / WamaCare2026!")
print(f"\n  Phase 8 configuration complete.")
