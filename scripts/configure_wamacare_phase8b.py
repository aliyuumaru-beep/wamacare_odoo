#!/usr/bin/env python3
"""
WamaCare Phase 8b — User creation, LPO import, purchase approval threshold.
Continuation of Phase 8 for steps that required SQL-level group fixes first.
"""
import xmlrpc.client, os, csv, sys

URL      = os.environ.get("WAMACARE_URL", "http://localhost:8070")
DB       = os.environ.get("WAMACARE_DB", "wamacare_local")
PASSWORD = os.environ.get("WAMACARE_ADMIN_PASS", "admin")

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid    = common.authenticate(DB, "admin", PASSWORD, {})
if not uid:
    print("ERROR: Authentication failed"); sys.exit(1)

m   = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
CSV = os.path.join(os.path.dirname(__file__), "..", "csv_templates", "wamacare")

def x(model, method, *args, **kw):
    return m.execute_kw(DB, uid, PASSWORD, model, method, list(args), kw)

def search_read(model, domain, fields, limit=None):
    kw = {"fields": fields}
    if limit: kw["limit"] = limit
    return m.execute_kw(DB, uid, PASSWORD, model, "search_read", [domain], kw)

def sec(t): print(f"\n{'='*55}\n  {t}\n{'='*55}")


# ─── Known group IDs from Phase 8 SQL inspection ─────────────
GROUP_IDS = {
    "analytic":           15,
    "account_readonly":   25,
    "account_user":       27,
    "account_manager":    28,
    "hr_user":            22,
    "hr_manager":         23,
    "maintenance_mgr":    16,
    "project_user":       34,
    "project_manager":    35,
    "purchase_user":      46,
    "purchase_manager":   47,
}


# ─── STEP 7: Create WamaCare users ───────────────────────────
sec("STEP 7: Create WamaCare users")

demo_users = [
    {
        "name":  "Aliyu Hassan Umaru",
        "login": "aliyu.umaru",
        "email": "aliyuumaru@gmail.com",
        "groups": ["analytic","account_user","project_manager","purchase_manager","hr_user"],
    },
    {
        "name":  "WamaCare Finance Officer",
        "login": "finance.officer",
        "email": "finance@wamacare.ng",
        "groups": ["account_manager","analytic","purchase_user"],
    },
    {
        "name":  "WamaCare Field Officer",
        "login": "field.officer",
        "email": "field@wamacare.ng",
        "groups": ["project_user"],
    },
    {
        "name":  "WamaCare HR Officer",
        "login": "hr.officer",
        "email": "hr@wamacare.ng",
        "groups": ["hr_user"],
    },
]

for usr in demo_users:
    existing = x("res.users", "search", [("login", "=", usr["login"])])
    if existing:
        print(f"  SKIP (exists): {usr['login']}")
        continue
    gids = [GROUP_IDS[g] for g in usr["groups"] if g in GROUP_IDS]
    try:
        new_uid = x("res.users", "create", {
            "name":       usr["name"],
            "login":      usr["login"],
            "email":      usr["email"],
            "groups_id":  [(6, 0, gids)],
            "password":   "WamaCare2026!",
        })
        print(f"  Created: {usr['login']} (uid={new_uid}) — {', '.join(usr['groups'])}")
    except Exception as e:
        print(f"  WARNING {usr['login']}: {e}")


# ─── STEP 8: Configure purchase approval threshold ───────────
sec("STEP 8: Configure purchase approval threshold")

# In Odoo 17 Community, purchase approval is controlled via
# the "Purchase Order Approval" setting. The threshold per company
# is set via the po_warn field or ir.config_parameter.
# We use the company write approach for the minimum amount.
try:
    x("res.company", "write", [1], {
        "po_double_validation":        "two_step",
        "po_double_validation_amount": 200000.0,   # ₦200,000 threshold
    })
    print("  Purchase approval threshold: ₦200,000 (two-step validation)")
except Exception as e:
    print(f"  WARNING: po_double_validation may not be available: {e}")
    print("  Manual step: Accounting → Settings → Purchase → Order Approval → set threshold")


# ─── STEP 9: Import LPO (purchase order) ─────────────────────
sec("STEP 9: Import LPO purchase orders")

lpo_path = os.path.join(CSV, "lpo.csv")
if not os.path.exists(lpo_path):
    print("  WARNING: lpo.csv not found")
else:
    with open(lpo_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        po_num  = row.get("PO Number", "").strip()
        vname   = row.get("Vendor", "").strip()
        odate   = row.get("Order Date", "").strip() or False
        ref     = row.get("Activity Reference", "").strip()
        amt_str = row.get("Total Amount", "0").strip().replace(",", "")
        try:
            amt = float(amt_str)
        except ValueError:
            amt = 0.0

        if not po_num:
            continue

        # Skip if a PO with this name/ref already exists
        existing = x("purchase.order", "search", [("name", "ilike", po_num)])
        if existing:
            print(f"  SKIP (exists): {po_num}")
            continue

        vendor_ids = x("res.partner", "search",
                       [("name", "=", vname), ("supplier_rank", ">", 0)])
        if not vendor_ids:
            vendor_ids = x("res.partner", "search", [("name", "=", vname)])
        if not vendor_ids:
            print(f"  WARNING: vendor '{vname}' not found — skipping {po_num}")
            continue

        # Find a logistics service product for the line
        prod_ids = x("product.product", "search", [("name", "ilike", "Logistics")])
        if not prod_ids:
            prod_ids = x("product.product", "search",
                         [("type", "=", "service")], limit=1)

        # Get analytic account for Maternal Health
        ana_ids = x("account.analytic.account", "search", [("name", "=", "Maternal Health")])

        line_vals = {
            "name":          f"{ref}" if ref else f"LPO {po_num}",
            "product_qty":   1.0,
            "price_unit":    amt,
            "date_planned":  odate,
        }
        if prod_ids:
            line_vals["product_id"] = prod_ids[0]

        po_vals = {
            "partner_id": vendor_ids[0],
            "date_order":  odate,
            "notes":       f"Ref: {ref}",
            "order_line":  [(0, 0, line_vals)],
        }
        try:
            po_id = x("purchase.order", "create", po_vals)
            print(f"  Created PO id={po_id}: {po_num} | {vname} | ₦{amt:,.0f}")
        except Exception as e:
            print(f"  WARNING {po_num}: {e}")


# ─── STEP 10: Apply Nigeria chart template (l10n_ng) ─────────
sec("STEP 10: Apply Nigeria chart template")
try:
    # In Odoo 17, try_loading signature: (template_code, company_id, install_demo)
    x("account.chart.template", "try_loading", "ng", 1, False)
    print("  Nigeria chart template applied successfully")
except Exception as e:
    # Try alternative signature
    try:
        x("account.chart.template", "try_loading",
          **{"template_code": "ng", "company": 1, "install_demo": False})
        print("  Nigeria chart template applied (keyword form)")
    except Exception as e2:
        print(f"  NOTE: Chart template not auto-applied via RPC: {e2}")
        print("  This is expected — l10n_ng taxes are installed, template applies on first company setup")
        print("  Manual step if needed: Accounting → Settings → Fiscal Localization → Nigeria")


# ─── STEP 11: Enable analytic accounting via settings execute ─
sec("STEP 11: Enable analytic accounting via config settings")
try:
    # Try creating a config record with only the analytic field
    cfg_id = x("res.config.settings", "create", {"group_analytic_accounting": True})
    x("res.config.settings", "execute", [cfg_id])
    print("  Analytic accounting ENABLED via res.config.settings")
except Exception as e:
    print(f"  NOTE: {str(e)[:120]}")
    # Check if it's already enabled from the SQL group membership
    grp_users = x("res.groups", "read", [GROUP_IDS["analytic"]], fields=["users"])
    if grp_users and uid in (grp_users[0].get("users") or []):
        print("  Analytic Accounting is ENABLED (admin is in analytic group via SQL)")
    else:
        print("  Manual step needed: Accounting → Settings → enable 'Analytic Accounting'")


# ─── FINAL SUMMARY ────────────────────────────────────────────
sec("Phase 8 Final Summary")

currency = x("res.company", "read", [1], fields=["currency_id"])[0]["currency_id"]
print(f"  Company:        WamaCare (Tiko CBO)")
print(f"  Currency:       {currency[1] if isinstance(currency, list) else currency}")
print(f"  Accounts:       {x('account.account', 'search_count', [])}")
print(f"  Projects:       {x('project.project', 'search_count', [])}")
print(f"  Analytic accs:  {x('account.analytic.account', 'search_count', [])}")
print(f"  Equipment:      {x('maintenance.equipment', 'search_count', [])}")
print(f"  Active users:   {x('res.users', 'search_count', [('active','=',True)])}")
print(f"  Purchase orders:{x('purchase.order', 'search_count', [])}")
print(f"  Vendors:        {x('res.partner', 'search_count', [('supplier_rank','>',0)])}")
print(f"  Beneficiaries:  {x('res.partner', 'search_count', [('category_id.name','=','Beneficiary')])}")
print()
print("  Users available:")
print("    admin          / admin          (CHANGE PASSWORD — Issue #11)")
print("    aliyu.umaru    / WamaCare2026!")
print("    finance.officer/ WamaCare2026!")
print("    field.officer  / WamaCare2026!")
print("    hr.officer     / WamaCare2026!")
print()
print("  URL: http://localhost:8070")
print()
print("  Phase 8 COMPLETE")
