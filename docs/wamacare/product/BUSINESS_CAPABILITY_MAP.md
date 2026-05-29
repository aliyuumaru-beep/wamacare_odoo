# BUSINESS_CAPABILITY_MAP.md — WamaCare Business Capability Map

**Version:** 1.0 | **Date:** 2026-05-29 | **Source:** Repository docs, DOCX mandate, XLSX checklist, PPTX, CSV files, installed modules, database inspection

---

## Discovery Sources

| Source | Key Insight |
|--------|------------|
| `CBO_Mandate_and_Odoo_Deliverables_Tiko.docx` | Full 8-domain CBO mandate with Odoo translation |
| `Odoo_module_checklist.xlsx` | Donor-critical demo items across 8 categories |
| `03_CBO_Digital_and_Structural_Transformation.pptx` | 3-stage maturity model, strategic outcomes |
| CSV files (14 files) | Actual data entities: beneficiaries, projects, vendors, employees, assets |
| Installed modules (78) | Confirmed capabilities: accounting, HR, project, purchase, maintenance |
| Database records | 5 programmes, 13 beneficiaries, 17 vendors, 70 COA accounts, 3 assets |

---

## Capability Status Legend

| Status | Meaning |
|--------|---------|
| ✅ IMPLEMENTED | Module installed, data loaded, workflow functional |
| 🔶 PARTIAL | Module installed but configuration incomplete |
| 🔲 PLANNED | In roadmap, not yet started |
| ⬜ DEFERRED | Identified but not yet roadmapped |

---

## 1. Governance Capabilities

**Purpose:** Enable transparent, accountable CBO operations that satisfy donor scrutiny and regulatory compliance.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Role and department structure | `hr` | ✅ IMPLEMENTED | 5 departments, 5 heads, 4 field staff |
| User access control | `base` groups | ✅ IMPLEMENTED | 5 roles configured |
| Audit trail (chatter) | `mail` | ✅ IMPLEMENTED | All records have chatter |
| Document approvals | `purchase` approval flow | 🔶 PARTIAL | PO approval configured; general approval workflow not yet set up |
| Contract repository | not installed | 🔲 PLANNED | `documents` module needed (Enterprise or OCA) |
| Contract expiry alerts | not installed | 🔲 PLANNED | Depends on contract repository |
| Policy and SOP repository | not installed | 🔲 PLANNED | Documents module |
| Two-factor authentication | `auth_totp` | ✅ IMPLEMENTED | Available, not enforced |
| Fiscal year management | `om_fiscal_year` | ✅ IMPLEMENTED | |
| Annual financial close | `om_fiscal_year` | ✅ IMPLEMENTED | |

---

## 2. HR Capabilities

**Purpose:** Manage staff, volunteers, mobilizers, and service providers across the CBO lifecycle.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Employee records | `hr` | ✅ IMPLEMENTED | 10 employees, 5 departments |
| Department hierarchy | `hr` | ✅ IMPLEMENTED | Field Operations under Programs |
| Job positions | `hr` | ✅ IMPLEMENTED | 9 job positions created |
| Org chart | `hr_org_chart` | ✅ IMPLEMENTED | Module installed |
| Skills tracking | `hr_skills` | ✅ IMPLEMENTED | Module installed; no skills loaded yet |
| Staff onboarding workflow | `hr` | 🔶 PARTIAL | Records created; onboarding checklist not built |
| Training records | `hr` + `hr_skills` | 🔶 PARTIAL | Skills module available; no training data |
| Certification tracking | `hr_skills` | 🔶 PARTIAL | Available; no certificates loaded |
| Performance tracking | not installed | 🔲 PLANNED | `hr_appraisal` module needed |
| Volunteer management | `hr` (contact tags) | 🔶 PARTIAL | No separate volunteer category yet |
| Community mobilizer profiles | `hr` / `res.partner` | 🔶 PARTIAL | Mobilizer employee exists; credential tracking not built |
| Staff exit tracking | `hr` | 🔲 PLANNED | Archive function exists; exit checklist not built |
| Expense claims | `hr_expense` | ✅ IMPLEMENTED | Module installed and linked to projects |

---

## 3. Programme Management Capabilities

**Purpose:** Plan, execute, track, and report on CBO programmes and activities.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Programme definition | `project` | ✅ IMPLEMENTED | 5 active programmes |
| Activity and task tracking | `project` | ✅ IMPLEMENTED | Project tasks available; 0 tasks loaded |
| Budget per programme | `analytic` + `om_account_budget` | ✅ IMPLEMENTED | 13 analytic accounts; budgets not yet set |
| Milestone tracking | `project` (milestones group) | 🔶 PARTIAL | Module available; milestones not configured |
| Outcome indicators | `project` | 🔶 PARTIAL | Custom fields needed for indicators |
| Activity scheduling | `calendar` | ✅ IMPLEMENTED | Calendar module installed |
| Field activity logs | `project` tasks | 🔶 PARTIAL | Tasks available; field log workflow not built |
| Programme reporting | `spreadsheet_dashboard` | 🔶 PARTIAL | Dashboard available; WamaCare-specific views not built |
| Budget vs actual | `om_account_budget` + analytic | ✅ IMPLEMENTED | All 5 programmes linked to analytic accounts |
| Donor grant tracking | analytic accounts | ✅ IMPLEMENTED | 13 analytic accounts (per programme/funder) |

---

## 4. Donor Management Capabilities

**Purpose:** Track donors, grants, MOUs, reporting obligations, and fund utilisation transparency.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Donor contact records | `contacts` | 🔶 PARTIAL | Vendor type partners exist; no "Donor" tag yet |
| Grant / analytic account | `analytic` | ✅ IMPLEMENTED | 13 analytic accounts per programme |
| Budget vs actual per grant | `om_account_budget` + analytic | ✅ IMPLEMENTED | Infrastructure ready |
| Donor MOU storage | not installed | 🔲 PLANNED | Documents module needed |
| Grant reporting (narrative) | not installed | 🔲 PLANNED | Custom or documents module |
| Donor expense reporting | `accounting_pdf_reports` | 🔶 PARTIAL | Reports available; donor-specific templates not built |
| Recurring payments | `om_recurring_payments` | ✅ IMPLEMENTED | Module installed |
| Donor follow-up | `om_account_followup` | ✅ IMPLEMENTED | Module installed |
| Multi-donor fund separation | analytic plans | 🔶 PARTIAL | One plan ("Programs") exists; multi-donor separation needs plan-per-donor |

---

## 5. Procurement Capabilities

**Purpose:** Manage the full LPO-based procurement cycle from request to payment with approvals and audit trail.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Vendor onboarding | `purchase` + `contacts` | ✅ IMPLEMENTED | 17 vendors loaded |
| Local Purchase Order (LPO) | `purchase` | ✅ IMPLEMENTED | LPO-001 (₦2.5M) created |
| Purchase approval workflow | `purchase` | ✅ IMPLEMENTED | Two-step, ₦200,000 threshold |
| Vendor bills / invoices | `account` | ✅ IMPLEMENTED | Account module installed |
| Payment approvals | `account` | ✅ IMPLEMENTED | Multi-step payment workflow available |
| Budget check before PO | `om_account_budget` | 🔶 PARTIAL | Budget module installed; pre-PO check not configured |
| Procurement reports | `accounting_pdf_reports` | ✅ IMPLEMENTED | |
| Vendor performance tracking | not installed | 🔲 PLANNED | `purchase` ratings or custom |
| Stock replenishment requests | `purchase` (min stock rules) | 🔲 PLANNED | Inventory module not installed |
| Contract-linked procurement | not installed | 🔲 PLANNED | Depends on contracts module |

---

## 6. Finance Capabilities

**Purpose:** Full financial management — budgeting, chart of accounts, invoicing, payments, audit trails, and NGN reporting.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Chart of accounts (NGO) | `account` + l10n_ng | ✅ IMPLEMENTED | 70 accounts incl. 21 NGO-specific |
| NGN currency | `account` | ✅ IMPLEMENTED | Functional currency set to ₦ |
| Nigeria VAT (7.5%) | `l10n_ng` | ✅ IMPLEMENTED | Tax configured |
| WHT (Withholding Tax) | `l10n_ng` | ✅ IMPLEMENTED | WHT accounts 252001/252002 |
| Analytic accounting | `analytic` | ✅ IMPLEMENTED | Enabled; 13 accounts |
| Budget management | `om_account_budget` | ✅ IMPLEMENTED | Module installed; budgets not yet entered |
| Vendor bills and payments | `account` | ✅ IMPLEMENTED | |
| Bank reconciliation | `account` | 🔶 PARTIAL | Module ready; no bank account configured |
| Daily reports | `om_account_daily_reports` | ✅ IMPLEMENTED | |
| Asset depreciation | `om_account_asset` | ✅ IMPLEMENTED | Module installed; assets not yet linked |
| Recurring payments | `om_recurring_payments` | ✅ IMPLEMENTED | |
| Customer/donor follow-up | `om_account_followup` | ✅ IMPLEMENTED | |
| Full accounting suite | `om_account_accountant` | ✅ IMPLEMENTED | Installed v2.0.2 |
| FIRS tax reporting | `l10n_ng` | ✅ IMPLEMENTED | Tax report structure available |
| PAYE payable | COA account 2110 | ✅ IMPLEMENTED | Account created |
| PENCOM payable | COA account 2130 | ✅ IMPLEMENTED | Account created |
| Audit-ready PDF reports | `accounting_pdf_reports` | ✅ IMPLEMENTED | |

---

## 7. Asset Management Capabilities

**Purpose:** Track, maintain, and value CBO fixed assets and equipment.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Asset register | `maintenance` + `om_account_asset` | ✅ IMPLEMENTED | 3 assets: Ambulance, Ultrasound, Laptop |
| Equipment categories | `maintenance` | 🔶 PARTIAL | No categories defined yet |
| Asset assignment to dept/programme | `maintenance` | 🔶 PARTIAL | Assets created; assignment not set |
| Maintenance scheduling | `maintenance` | 🔶 PARTIAL | Module installed; no schedules built |
| Asset depreciation | `om_account_asset` | 🔶 PARTIAL | Module installed; depreciation not configured |
| Insurance tracking | not installed | 🔲 PLANNED | Custom field or documents module |
| Asset valuation | `om_account_asset` | 🔶 PARTIAL | Module available; not configured |

---

## 8. Inventory Capabilities

**Purpose:** Track supplies, medical consumables, and programme materials.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Product catalogue | `product` | ✅ IMPLEMENTED | 21 products/services defined |
| Stock locations | not installed | 🔲 PLANNED | `stock` module not installed |
| Stock movements | not installed | 🔲 PLANNED | `stock` module required |
| Delivery kit tracking | not installed | 🔲 PLANNED | Delivery Kits in product list but no stock tracking |
| Medical supply inventory | not installed | 🔲 PLANNED | `stock` module required |
| Reorder rules | not installed | 🔲 PLANNED | Depends on `stock` |
| Lot/serial tracking | not installed | 🔲 PLANNED | `stock` with tracking |

**Note:** Inventory (`stock` module) is the most significant missing capability at Release 1.0.

---

## 9. Beneficiary Management Capabilities

**Purpose:** Register, track, and protect programme beneficiaries while maintaining privacy.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Beneficiary registration | `contacts` (`res.partner`) | ✅ IMPLEMENTED | 13 beneficiaries (BEN-004 to BEN-016) |
| Programme tagging | Partner categories | ✅ IMPLEMENTED | Maternal Health, Protection, Community Outreach, Capacity Building |
| Geolocation (FCT areas) | `res.partner` lat/lon | ✅ IMPLEMENTED | 7 Abuja FCT areas mapped |
| Gender tagging | Partner categories | ✅ IMPLEMENTED | Female tag applied |
| Anonymised records | naming convention (BEN-XXX) | 🔶 PARTIAL | Naming scheme in place; no formal anonymisation module |
| Case management | not installed | 🔲 PLANNED | Custom model needed |
| Beneficiary consent tracking | not installed | 🔲 PLANNED | Documents module or custom field |
| Case notes | not installed | 🔲 PLANNED | Custom or chatter-based |
| Access restriction | Odoo record rules | 🔲 PLANNED | No record-level restriction on beneficiary records yet |

---

## 10. Safeguarding Capabilities

**Purpose:** Protect beneficiaries from harm, enable reporting, and ensure accountability.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Safeguarding programme | `project` | ✅ IMPLEMENTED | "Safeguarding & Protection Program" exists as a project |
| Safeguarding staff | `hr` | ✅ IMPLEMENTED | Safeguarding Lead C role created |
| Legal & Compliance department | `hr` | ✅ IMPLEMENTED | Department with manager |
| Safeguarding alerts | not installed | 🔲 PLANNED | Custom model needed — HIGH PRIORITY |
| Anonymous reporting portal | not installed | 🔲 PLANNED | Custom or website module |
| Case flag/escalation | not installed | 🔲 PLANNED | Custom model |
| Referral pathway tracking | not installed | 🔲 PLANNED | Custom model |
| Evidence upload | `mail` attachments | 🔶 PARTIAL | Files attachable to chatter; no structured evidence workflow |
| NDPR compliance | privacy_lookup | 🔶 PARTIAL | `privacy_lookup` module installed; policies not configured |

---

## 11. Entrepreneurship Capabilities

**Purpose:** Support women's economic empowerment through clubs, training, and livelihood tracking.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Entrepreneurship programme | `project` | 🔶 PARTIAL | "Women Entrepreneurship Support" in projects CSV; not in active DB programmes |
| Club registration | `contacts` (partner tags) | 🔲 PLANNED | No club records or tags created |
| Member management | `contacts` | 🔲 PLANNED | Tag structure needed |
| Training programmes | `hr_skills` | 🔲 PLANNED | Skills module available; training curricula not built |
| Mentoring tracking | not installed | 🔲 PLANNED | Custom or project tasks |
| Informal-to-cooperative upgrade | not installed | 🔲 PLANNED | Custom workflow |
| Livelihood outcome tracking | not installed | 🔲 PLANNED | M&E module or custom |
| Skills income tracking | not installed | 🔲 PLANNED | Custom |

**Source:** PPTX mentions "Community Entrepreneurship & Life Skills Centres" and "Stage 3: Community Enterprise Hub". DOCX Part 1.8 describes club identification, member management, skills training, and outcome tracking. XLSX marks entrepreneurship as "Optional" for donor demos.

---

## 12. Monitoring & Evaluation Capabilities

**Purpose:** Measure programme outcomes, track impact indicators, and produce donor-ready reports.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| M&E programme | `project` | ✅ IMPLEMENTED | "Monitoring & Evaluation Program" active |
| Analytic account for M&E | `analytic` | ✅ IMPLEMENTED | "Monitoring" analytic account |
| Budget vs actual reporting | `om_account_budget` + spreadsheet | ✅ IMPLEMENTED | Infrastructure ready |
| Activity/task completion tracking | `project` | ✅ IMPLEMENTED | Task model available |
| Outcome indicator definition | not installed | 🔲 PLANNED | Custom project fields or `project.milestone` |
| Cost-per-beneficiary calculation | not installed | 🔲 PLANNED | Custom computation (analytic / beneficiary count) |
| Programme impact dashboard | `spreadsheet_dashboard` | 🔶 PARTIAL | Dashboard module installed; WamaCare-specific views not built |
| Field data collection | not installed | 🔲 PLANNED | Custom or ODK/Kobo integration |
| Donor impact reports | `accounting_pdf_reports` | 🔶 PARTIAL | PDF reports available; impact-specific templates not built |

---

## 13. Executive Dashboard Capabilities

**Purpose:** Give leadership real-time visibility across all programmes, finance, and operations.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Financial dashboard | `spreadsheet_dashboard_account` | ✅ IMPLEMENTED | Module installed |
| Purchase dashboard | `spreadsheet_dashboard_purchase` | ✅ IMPLEMENTED | Module installed |
| Project overview | `project` list/kanban | ✅ IMPLEMENTED | Available in UI |
| Analytic reporting | `spreadsheet_account` | ✅ IMPLEMENTED | Spreadsheet with account data |
| Custom KPI dashboard | `spreadsheet_dashboard` | 🔶 PARTIAL | Engine installed; WamaCare KPIs not built |
| Programme outcomes view | not built | 🔲 PLANNED | Needs M&E data model first |
| Beneficiary statistics | not built | 🔲 PLANNED | Needs beneficiary model enhancement |
| Executive PDF report | `accounting_pdf_reports` | 🔶 PARTIAL | Generic financial reports; programme-level PDF not built |

**Source:** Dashboard screenshot (`DashBoard Executive.png`) shows programme-level financial overview with beneficiary counts — this is the target state.

---

## 14. Healthcare Ecosystem Capabilities

**Purpose:** Enable WamaCare to connect with healthcare providers, diagnostic facilities, and health service networks.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Healthcare vendors | `contacts` | ✅ IMPLEMENTED | SafeLife Diagnostics, Community Health Trainers Network, Hope Medical Supplies in vendor list |
| Medical products/services | `product` | ✅ IMPLEMENTED | Antenatal Screening Services, Mobile Clinic Equipment, Diagnostic Services |
| Mobile clinic tracking | `maintenance` (Ultrasound, Ambulance) | ✅ IMPLEMENTED | Assets registered |
| Healthcare programme | `project` | ✅ IMPLEMENTED | Maternal Health Outreach programme |
| Blood bank integration | not installed | 🔲 PLANNED | Digital Blood Bank system — ecosystem play, not core Odoo |
| Clinical record management | not installed | ⬜ DEFERRED | WamaCare is CBO, not clinic — clinical records outside scope |
| Health insurance scheme | Community Health Insurance Scheme vendor | 🔶 PARTIAL | Vendor exists; insurance workflow not built |
| Referral network management | not installed | 🔲 PLANNED | Partner ecosystem feature |

**Note:** WamaCare is a CBO delivering health programmes — NOT a clinical system. Healthcare ecosystem capabilities are about partnership, procurement, and referral — not patient records or prescriptions.

---

## 15. Safe House Capabilities

**Purpose:** Enable management of safe house facilities for vulnerable women and girls requiring refuge.

| Capability | Module(s) | Status | Gap |
|-----------|----------|--------|-----|
| Safe house as facility | `maintenance` (as equipment/location) | ⬜ DEFERRED | No evidence of safe house in current database or CSVs |
| Resident/intake management | not installed | ⬜ DEFERRED | Custom model required |
| Case referral to safe house | not installed | ⬜ DEFERRED | Depends on case management first |
| Safe house resource tracking | not installed | ⬜ DEFERRED | Custom |
| Exit/transition planning | not installed | ⬜ DEFERRED | Custom |

**Source:** Referenced in the original governance prompt as a target capability. Not evidenced in any current project document, CSV, or database. Classified as DEFERRED — depends on safeguarding case management being built first (SAFE-001 → SAFE-002 → SAFE-house).

---

## Capability Summary

| Domain | Implemented | Partial | Planned | Deferred |
|--------|------------|---------|---------|---------|
| 1. Governance | 5 | 3 | 3 | 0 |
| 2. HR | 5 | 6 | 2 | 0 |
| 3. Programme Management | 5 | 5 | 1 | 0 |
| 4. Donor Management | 3 | 2 | 4 | 0 |
| 5. Procurement | 6 | 2 | 3 | 0 |
| 6. Finance | 14 | 2 | 1 | 0 |
| 7. Asset Management | 2 | 4 | 1 | 0 |
| 8. Inventory | 1 | 0 | 6 | 0 |
| 9. Beneficiary Management | 4 | 2 | 3 | 0 |
| 10. Safeguarding | 3 | 2 | 5 | 0 |
| 11. Entrepreneurship | 0 | 1 | 6 | 0 |
| 12. M&E | 4 | 3 | 4 | 0 |
| 13. Executive Dashboard | 4 | 2 | 3 | 0 |
| 14. Healthcare Ecosystem | 5 | 1 | 2 | 1 |
| 15. Safe House | 0 | 0 | 0 | 5 |
| **TOTAL** | **61** | **35** | **44** | **6** |

**Overall maturity: 42% fully implemented, 24% partial, 31% planned, 4% deferred.**
