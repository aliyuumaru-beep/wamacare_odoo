#!/usr/bin/env python3
"""
WamaCare Data Import Script — Phase 7
Imports all CSV templates into wamacare_local via Odoo RPC.
Run while Odoo is running on port 8070.
"""

import xmlrpc.client
import csv
import sys
import os

# ─── Connection ───────────────────────────────────────────────────────────────
# Override via environment: WAMACARE_URL, WAMACARE_DB, WAMACARE_ADMIN_PASS
URL = os.environ.get("WAMACARE_URL", "http://localhost:8070")
DB = os.environ.get("WAMACARE_DB", "wamacare_local")
USER = "admin"
PASSWORD = os.environ.get("WAMACARE_ADMIN_PASS", "admin")  # default only; override in prod

CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "csv_templates", "wamacare")

# ─── Connect ──────────────────────────────────────────────────────────────────
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
try:
    uid = common.authenticate(DB, USER, PASSWORD, {})
except Exception as e:
    print(f"ERROR: Cannot connect to Odoo at {URL}. Is it running?\n{e}")
    sys.exit(1)

if not uid:
    print(f"ERROR: Authentication failed for user '{USER}'. Check password.")
    sys.exit(1)

models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
print(f"Connected to {DB} as uid={uid}\n")


def execute(model, method, *args, **kwargs):
    return models.execute_kw(DB, uid, PASSWORD, model, method, list(args), kwargs)


def read_record(model, ids, fields):
    """Safe read that passes fields as keyword arg."""
    return models.execute_kw(DB, uid, PASSWORD, model, "read", [ids], {"fields": fields})


def read_csv(filename):
    path = os.path.join(CSV_DIR, filename)
    if not os.path.exists(path):
        print(f"  WARNING: {filename} not found at {path}")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ─── Step 1: Configure company ────────────────────────────────────────────────
print("=== Step 1: Configure company ===")
company_id = execute("res.company", "search", [("id", "=", 1)])[0]
execute("res.company", "write", [company_id], {
    "name": "WamaCare (Tiko CBO)",
    "country_id": execute("res.country", "search", [("code", "=", "NG")])[0],
})
# Update the partner linked to company too
company_rec = read_record("res.company", [company_id], ["partner_id"])[0]
execute("res.partner", "write", [company_rec["partner_id"][0]], {"name": "WamaCare (Tiko CBO)"})
print("  Company renamed to 'WamaCare (Tiko CBO)', country set to Nigeria")


# ─── Step 2: Create analytic plan ─────────────────────────────────────────────
print("\n=== Step 2: Create analytic plan 'Programs' ===")
plan_ids = execute("account.analytic.plan", "search", [("name", "=", "Programs")])
if plan_ids:
    plan_id = plan_ids[0]
    print(f"  Plan 'Programs' already exists (id={plan_id})")
else:
    plan_id = execute("account.analytic.plan", "create", {"name": "Programs", "color": 2})
    print(f"  Created plan 'Programs' (id={plan_id})")


# ─── Step 3: Import analytic accounts ─────────────────────────────────────────
print("\n=== Step 3: Import analytic accounts ===")
rows = read_csv("mamacare_analytic_accounts.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("account.analytic.account", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    execute("account.analytic.account", "create", {"name": name, "plan_id": plan_id})
    print(f"  Created analytic account: {name}")


# ─── Step 4: Import HR departments (without managers first) ───────────────────
print("\n=== Step 4: Import HR departments ===")
rows = read_csv("hr_department.csv")
dept_ids = {}
for row in rows:
    name = row.get("name", "").strip()
    if not name:
        continue
    existing = execute("hr.department", "search", [("name", "=", name)])
    if existing:
        dept_ids[name] = existing[0]
        print(f"  SKIP (exists): {name}")
        continue
    vals = {"name": name}
    dept_id = execute("hr.department", "create", vals)
    dept_ids[name] = dept_id
    print(f"  Created department: {name} (id={dept_id})")

# Set parent departments
for row in rows:
    name = row.get("name", "").strip()
    parent_name = row.get("parent_id/id", "").strip()
    if name in dept_ids and parent_name:
        # Find parent by name (external ID format "Programs Department" → look up by name)
        parent_ids = execute("hr.department", "search", [("name", "=", parent_name)])
        if parent_ids:
            execute("hr.department", "write", [dept_ids[name]], {"parent_id": parent_ids[0]})
            print(f"  Set parent of '{name}' → '{parent_name}'")


# ─── Step 5: Create partner categories for beneficiaries ──────────────────────
print("\n=== Step 5: Create partner categories ===")
categories = [
    "Beneficiary", "Active", "Female", "Male",
    "Maternal Health", "Protection", "Community Outreach", "Capacity Building"
]
cat_ids = {}
for cat_name in categories:
    existing = execute("res.partner.category", "search", [("name", "=", cat_name)])
    if existing:
        cat_ids[cat_name] = existing[0]
        print(f"  SKIP (exists): {cat_name}")
    else:
        cat_id = execute("res.partner.category", "create", {"name": cat_name})
        cat_ids[cat_name] = cat_id
        print(f"  Created category: {cat_name}")


# ─── Step 6: Import vendors (basic) ───────────────────────────────────────────
print("\n=== Step 6: Import basic vendors ===")
rows = read_csv("vendor.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("res.partner", "search", [("name", "=", name), ("supplier_rank", ">", 0)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    country_ids = execute("res.country", "search", [("name", "ilike", "Nigeria")])
    vals = {
        "name": name,
        "company_type": "company",
        "supplier_rank": int(row.get("Vendor Rank", 1) or 1),
        "email": row.get("Email", "").strip() or False,
        "phone": row.get("Phone", "").strip() or False,
        "country_id": country_ids[0] if country_ids else False,
    }
    execute("res.partner", "create", vals)
    print(f"  Created vendor: {name}")


# ─── Step 7: Import WamaCare vendors ──────────────────────────────────────────
print("\n=== Step 7: Import WamaCare vendors ===")
rows = read_csv("wamacare_vendors.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("res.partner", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    country_ids = execute("res.country", "search", [("name", "ilike", "Nigeria")])
    vals = {
        "name": name,
        "company_type": "company",
        "supplier_rank": 1,
        "country_id": country_ids[0] if country_ids else False,
    }
    execute("res.partner", "create", vals)
    print(f"  Created vendor: {name}")


# ─── Step 8: Import beneficiaries ─────────────────────────────────────────────
print("\n=== Step 8: Import beneficiaries ===")
rows = read_csv("beneficiaries.csv")
country_ng = execute("res.country", "search", [("code", "=", "NG")])[0]
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("res.partner", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue

    # Build tag IDs from Category Tags column
    tags_raw = row.get("Category Tags", "")
    tag_ids = []
    for tag_name in tags_raw.split(","):
        tag_name = tag_name.strip()
        if tag_name in cat_ids:
            tag_ids.append(cat_ids[tag_name])
        else:
            existing_tag = execute("res.partner.category", "search", [("name", "=", tag_name)])
            if existing_tag:
                tag_ids.append(existing_tag[0])
            elif tag_name:
                new_tag = execute("res.partner.category", "create", {"name": tag_name})
                tag_ids.append(new_tag)
                cat_ids[tag_name] = new_tag

    vals = {
        "name": name,
        "company_type": "person",
        "phone": row.get("Phone", "").strip() or False,
        "city": row.get("City", "").strip() or False,
        "country_id": country_ng,
        "category_id": [(6, 0, tag_ids)],
        "customer_rank": 0,
        "supplier_rank": 0,
    }
    lat = row.get("Latitude", "").strip()
    lon = row.get("Longitude", "").strip()
    if lat:
        vals["partner_latitude"] = float(lat)
    if lon:
        vals["partner_longitude"] = float(lon)

    execute("res.partner", "create", vals)
    print(f"  Created beneficiary: {name} ({row.get('City', '')})")


# ─── Step 9: Import projects ──────────────────────────────────────────────────
print("\n=== Step 9: Import projects/programmes ===")
rows = read_csv("mamacare_projects.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("project.project", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    # Find matching analytic account
    aa_ids = execute("account.analytic.account", "search", [("name", "ilike", name[:20])])
    vals = {
        "name": name,
        "privacy_visibility": "employees",
    }
    execute("project.project", "create", vals)
    print(f"  Created project: {name}")


# ─── Step 10: Import products/services ────────────────────────────────────────
print("\n=== Step 10: Import products (mamacare_products) ===")
rows = read_csv("mamacare_products.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("product.template", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    product_type = "service" if row.get("Product Type", "").lower() == "service" else "consu"
    vals = {
        "name": name,
        "type": product_type,
        "can_be_expensed": row.get("Can be Expensed", "").lower() in ("yes", "true", "1"),
    }
    execute("product.template", "create", vals)
    print(f"  Created product: {name}")


print("\n=== Step 11: Import employees ===")
rows = read_csv("hr_employees.csv")
for row in rows:
    name = row.get("Name", "").strip()
    if not name:
        continue
    existing = execute("hr.employee", "search", [("name", "=", name)])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    vals = {"name": name}
    dept_name = row.get("Department", "").strip()
    if dept_name:
        dept_search = execute("hr.department", "search", [("name", "=", dept_name)])
        if dept_search:
            vals["department_id"] = dept_search[0]
    job_name = row.get("Job Position", "").strip()
    if job_name:
        job_ids = execute("hr.job", "search", [("name", "=", job_name)])
        if not job_ids:
            job_id = execute("hr.job", "create", {"name": job_name})
        else:
            job_id = job_ids[0]
        vals["job_id"] = job_id
    execute("hr.employee", "create", vals)
    print(f"  Created employee: {name}")


print("\n=== Import Complete ===")
print("\nSummary:")
print(f"  Partners (total): {execute('res.partner', 'search_count', [])}")
print(f"  Beneficiaries: {execute('res.partner', 'search_count', [('category_id.name', '=', 'Beneficiary')])}")
print(f"  Vendors: {execute('res.partner', 'search_count', [('supplier_rank', '>', 0)])}")
print(f"  Projects: {execute('project.project', 'search_count', [])}")
print(f"  Employees: {execute('hr.employee', 'search_count', [])}")
print(f"  Products: {execute('product.template', 'search_count', [])}")
print(f"  Analytic accounts: {execute('account.analytic.account', 'search_count', [])}")
print(f"\nWamaCare is running at http://localhost:8070")
print("Login: admin / admin")
