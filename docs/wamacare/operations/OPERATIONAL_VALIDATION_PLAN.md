# OPERATIONAL_VALIDATION_PLAN.md — WamaCare Phase A.5 Validation Plan

**Version:** 1.0 | **Date:** 2026-05-29
**Purpose:** Define complete end-to-end test scenarios for every lifecycle in Phase A. A capability is not COMPLETED until it passes its scenario and leaves verifiable evidence in the database.

**Context:** The Evidence-Based Audit found 0 journal entries, 0 vendor bills, 0 expenses, 0 budgets, and 0 tasks. All Phase A financial and operational features are configured but untested.

---

## Gate Rule

> A feature status may not be set to COMPLETED unless:
> 1. The test scenario below has been executed in `wamacare_local`
> 2. Expected records exist in the database (verified by SQL)
> 3. Expected report or output was generated and reviewed
> 4. Audit trail (chatter) shows the workflow steps

---

## Lifecycle 1 — Procurement Lifecycle

**Business scenario:** Tiko CBO needs to purchase 100 Delivery Kits for the ANC Outreach programme. The purchase must follow the two-step LPO approval process.

### Preconditions
- [ ] Vendor "Hope Medical Supplies Ltd" exists (`supplier_rank > 0`)
- [ ] Product "Delivery Kits" exists in product catalogue
- [ ] Analytic account "Maternal Health" exists and is active
- [ ] `aliyu.umaru` has Purchase Administrator group
- [ ] `finance.officer` has Accounting permissions
- [ ] Purchase approval threshold = ₦200,000 (verified in `res_company`)

### Test Data
| Field | Value |
|-------|-------|
| Vendor | Hope Medical Supplies Ltd |
| Product | Delivery Kits |
| Quantity | 100 units |
| Unit price | ₦8,000 |
| Total | ₦800,000 |
| Analytic account | Maternal Health |
| Delivery date | 2026-06-15 |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `aliyu.umaru` | Create RFQ, fill in vendor/product/qty/price |
| 2 | `aliyu.umaru` | Send RFQ to vendor (confirm to "RFQ Sent") |
| 3 | `aliyu.umaru` | Convert to Purchase Order → Status: "To Approve" |
| 4 | `admin` | Open PO → Click "Approve Order" → Status: "Purchase Order" |
| 5 | `finance.officer` | Receive goods (validate receipt) |
| 6 | `finance.officer` | Create vendor bill from PO → Post bill |
| 7 | `admin` | Register payment → Mark as paid |

### Expected Transactions
- 1 `purchase.order` record in state `purchase` (confirmed)
- 1 `account.move` (vendor bill) in state `posted`
- 1 `account.payment` record
- Analytic line in "Maternal Health" account

### Expected Accounting Impact
| Account | Direction | Amount |
|---------|-----------|--------|
| 5000 Programme Expenses OR product expense account | Debit | ₦800,000 |
| 2000 Accounts Payable | Credit | ₦800,000 |
| (On payment) 2000 Accounts Payable | Debit | ₦800,000 |
| (On payment) 1010 Bank Account | Credit | ₦800,000 |

### Expected Reports
- Purchase Order PDF (from P00001 → Print)
- Vendor Bills list (Accounting → Vendors → Bills)
- Analytic report showing ₦800,000 under Maternal Health

### Pass Criteria
- [ ] `purchase_order` state = 'purchase'
- [ ] `account_move` (vendor bill) state = 'posted'
- [ ] `account_move_line` contains debit to expense account
- [ ] `account_analytic_line` entry for Maternal Health exists
- [ ] Chatter on PO shows: Draft → Sent → To Approve → Approved
- [ ] Chatter on Bill shows: Draft → Posted
- [ ] Purchase Order PDF renders without error

### Fail Conditions
- Approval button not visible to approver
- Bill cannot be created from confirmed PO
- Analytic account not available on bill line
- PDF report errors on generation

---

## Lifecycle 2 — Finance Lifecycle

**Business scenario:** Process the existing expense from `mamacare_expenses.csv` — GreenPower Solutions bill (MC-EXP-002) for ₦1,850,000, Maternal Health programme.

### Preconditions
- [ ] `finance.officer` has Accounting (Accountant) group
- [ ] Vendor "GreenPower Solutions" exists with `supplier_rank > 0`
- [ ] Bank account configured (FIN-012 must be done first)
- [ ] Analytic account "Maternal Health" active
- [ ] COA account "5000 Programme Expenses" exists

### Test Data
| Field | Value |
|-------|-------|
| Bill reference | MC-EXP-002 |
| Vendor | GreenPower Solutions |
| Bill date | 2025-01-10 |
| Due date | 2025-01-25 |
| Line: description | Procurement of clean delivery kits for maternal health outreach |
| Line: amount | ₦1,850,000 |
| Analytic account | Maternal Health |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `finance.officer` | Accounting → Vendors → Bills → New |
| 2 | `finance.officer` | Fill in vendor, date, line items, analytic account |
| 3 | `finance.officer` | Confirm bill → Post |
| 4 | `finance.officer` | Register Payment → Bank Journal → Validate |

### Expected Transactions
- 1 `account.move` (vendor bill) posted
- 1 `account.payment` posted
- 2 journal entry lines (debit expense, credit payable)
- 1 analytic line under Maternal Health

### Expected Accounting Impact
| Account | Direction | Amount |
|---------|-----------|--------|
| 5030 Maternal Health Costs | Debit | ₦1,850,000 |
| 2000 Accounts Payable | Credit | ₦1,850,000 |

### Expected Reports
- Vendor Bills list shows MC-EXP-002
- General Ledger (om reports) shows the entry
- Partner Ledger shows GreenPower Solutions balance

### Pass Criteria
- [ ] `account_move` with ref MC-EXP-002 exists and state = 'posted'
- [ ] `account_move_line` shows debit to 5030
- [ ] `account_analytic_line` shows ₦1,850,000 under Maternal Health
- [ ] Partner Ledger PDF renders with correct amounts
- [ ] General Ledger PDF renders without error

---

## Lifecycle 3 — Budget Lifecycle

**Business scenario:** Create the 2026 programme budgets for all 5 WamaCare programmes, then verify budget vs actual after recording the MC-EXP-002 bill above.

### Preconditions
- [ ] `om_account_budget` module installed
- [ ] Analytic accounts exist for all 5 programmes
- [ ] COA expense accounts (5000–5090) exist
- [ ] Lifecycle 2 (Finance) has been completed to provide "actual" data

### Test Data — Budget Positions (create these first)
| Budget Position | Linked Account |
|----------------|---------------|
| Programme Delivery | 5000 Programme Expenses |
| Staff & HR | 5010 Staff Costs |
| Maternal Health | 5030 Maternal Health Costs |
| Safeguarding | 5040 Safeguarding Costs |
| M&E | 5060 Monitoring & Evaluation |

### Test Data — Budgets (one per programme)
| Programme | Budget Position | Period | Planned Amount |
|-----------|----------------|--------|---------------|
| Maternal Health Outreach – Tiko | Maternal Health | 01/01/2026–31/12/2026 | ₦12,000,000 |
| Health Worker Capacity Program | Programme Delivery | 01/01/2026–31/12/2026 | ₦6,000,000 |
| Safeguarding & Protection Program | Safeguarding | 01/01/2026–31/12/2026 | ₦4,000,000 |
| Monitoring & Evaluation Program | M&E | 01/01/2026–31/12/2026 | ₦3,000,000 |
| Organisation-wide Support | Staff & HR | 01/01/2026–31/12/2026 | ₦8,000,000 |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `finance.officer` | Accounting → Budget → Budgetary Positions → Create each position |
| 2 | `finance.officer` | Accounting → Budget → Budgets → New budget per programme |
| 3 | `finance.officer` | Confirm each budget |
| 4 | `finance.officer` | Accounting → Budget → Budget Analysis → view vs actual |

### Expected Transactions
- 5 `crossovered.budget` records in state 'validate'
- `crossovered.budget.lines` with planned amounts
- Budget Analysis report shows ₦1,850,000 actual vs ₦12,000,000 budget for Maternal Health

### Pass Criteria
- [ ] `crossovered_budget` COUNT = 5 (one per programme)
- [ ] `crossovered_budget_lines` COUNT >= 5
- [ ] Budget Analysis shows correct planned amounts
- [ ] After Lifecycle 2: Maternal Health shows 15.4% utilisation (₦1.85M / ₦12M)
- [ ] Budget Analysis PDF renders

---

## Lifecycle 4 — HR Lifecycle

**Business scenario:** Field Officer A attends an ANC training day in Kubwa and claims ₦15,000 for transport.

### Preconditions
- [ ] `field.officer` has `project.group_project_user` group (FIX FIRST)
- [ ] `field.officer` user linked to "Field Officer A" employee
- [ ] Product "Transport Services" in expense product catalogue
- [ ] Analytic account "Maternal Health" active
- [ ] Lifecycle 2 (Finance) completed to verify accounting chain

### Link User to Employee (precondition fix required)
Currently "Field Officer A" employee has no Odoo user linked. Must set:
- `hr_employee.user_id` = `field.officer` user ID

### Test Data
| Field | Value |
|-------|-------|
| Employee | Field Officer A |
| Expense product | Transport Services |
| Description | Transport to ANC Outreach – Kubwa |
| Amount | ₦15,000 |
| Date | 2026-06-01 |
| Analytic account | Maternal Health |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `field.officer` | My Expenses → New → fill in product, amount, analytic |
| 2 | `field.officer` | Submit expense report |
| 3 | `aliyu.umaru` | Approve expense report |
| 4 | `finance.officer` | Post journal entries |
| 5 | `finance.officer` | Register payment |

### Expected Transactions
- 1 `hr.expense` record
- 1 `hr.expense.sheet` in state 'post'
- 1 `account.move` posted
- 1 analytic line under Maternal Health

### Pass Criteria
- [ ] `hr_expense` COUNT = 1
- [ ] `hr_expense_sheet` state = 'post'
- [ ] `account_analytic_line` shows Field Officer A transport under Maternal Health
- [ ] Expense Report PDF renders
- [ ] Chatter shows: Draft → Submitted → Approved → Posted

---

## Lifecycle 5 — Asset Lifecycle

**Business scenario:** Configure Ambulance 01 as a financial asset for depreciation, then run first depreciation.

### Preconditions
- [ ] `om_account_asset` installed (confirmed)
- [ ] "Ambulance 01" exists in `maintenance_equipment`
- [ ] COA account "1500 Fixed Assets" exists (check/create)
- [ ] COA account for accumulated depreciation exists (check/create)

### Test Data
| Field | Value |
|-------|-------|
| Asset name | Ambulance 01 |
| Category | Vehicle |
| Gross value | ₦35,000,000 |
| Salvage value | ₦3,500,000 |
| Purchase date | 2024-01-15 |
| Depreciation method | Straight-line |
| Duration | 5 years |
| Linked to Maternal Health programme | Yes |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `finance.officer` | Accounting → Assets → New Asset |
| 2 | `finance.officer` | Set all fields, compute depreciation |
| 3 | `finance.officer` | Confirm asset |
| 4 | `finance.officer` | Create first depreciation entry |

### Expected Transactions
- 1 `account_asset_asset` record in state 'open'
- Depreciation schedule: ₦35M - ₦3.5M = ₦31.5M over 5 years = ₦525,000/month
- 1 posted depreciation journal entry (₦525,000)

### Pass Criteria
- [ ] `account_asset_asset` COUNT = 1 (minimum; all 3 assets should be configured)
- [ ] Depreciation board shows monthly schedule
- [ ] First depreciation entry posted to journals
- [ ] Asset report PDF renders

---

## Lifecycle 6 — Contract Lifecycle

**Business scenario:** Store Field Officer A's employment contract.

### Preconditions
- Note: `documents` module is NOT installed. `hr_contract` is uninstalled.
- Two options: (A) Install `hr_contract` for staff contracts, (B) Use chatter attachments as interim.

### Option A — Install hr_contract (recommended)
| Step | User | Action |
|------|------|--------|
| 1 | `admin` | Apps → install `hr_contract` |
| 2 | `hr.officer` | Employees → Field Officer A → Contracts → New |
| 3 | `hr.officer` | Enter start date, wage, contract type |
| 4 | `hr.officer` | Confirm contract |

### Option B — Interim (chatter attachment)
- Attach contract PDF to employee record via chatter
- Not a formal contract management system, but creates an audit record

### Pass Criteria (Option A)
- [ ] `hr_contract` COUNT >= 1
- [ ] Contract linked to employee record
- [ ] Contract expiry alert mechanism identified (may require custom automation)

### Pass Criteria (Option B — interim)
- [ ] PDF attachment exists on employee chatter
- [ ] Attachment is date-stamped and user-attributed

---

## Lifecycle 7 — Programme Lifecycle

**Business scenario:** Plan and execute the ANC Outreach activity in Kubwa.

### Preconditions
- [ ] Project "Maternal Health Outreach – Tiko" exists
- [ ] `aliyu.umaru` has Project Administrator role
- [ ] `field.officer` has project.group_project_user (FIX FIRST)

### Test Data
| Field | Value |
|-------|-------|
| Project | Maternal Health Outreach – Tiko |
| Task name | ANC Outreach Visit – Kubwa |
| Assignee | Nurse B / Field Officer A |
| Planned date | 2026-06-10 |
| Description | Antenatal screening session for 20 beneficiaries |
| Planned hours | 8 |
| Linked analytic | Maternal Health |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `aliyu.umaru` | Project → Maternal Health → New Task |
| 2 | `aliyu.umaru` | Set assignee, deadline, description |
| 3 | `field.officer` | View and accept assigned task |
| 4 | `field.officer` | Mark task as In Progress |
| 5 | `field.officer` | Log note: "20 beneficiaries screened, Kubwa" |
| 6 | `aliyu.umaru` | Mark task as Done |

### Expected Transactions
- 1 `project.task` in state 'done'
- Chatter note with field log
- Calendar event (if used)

### Pass Criteria
- [ ] `project_task` COUNT >= 1
- [ ] Task state = 'done'
- [ ] Chatter shows task progress notes
- [ ] Task visible to both `aliyu.umaru` and `field.officer`

---

## Lifecycle 8 — Donor Reporting Lifecycle

**Business scenario:** Generate a quarterly donor report for the Maternal Health programme showing budget vs actual.

### Preconditions
- [ ] Lifecycle 2 (Finance) completed — at least 1 bill posted
- [ ] Lifecycle 3 (Budget) completed — budget records exist
- [ ] Analytic accounting enabled (confirmed: `account.analytic_accounting = 1`)
- [ ] Donor contact record exists with "Donor" tag

### Test Data
| Field | Value |
|-------|-------|
| Programme | Maternal Health Outreach – Tiko |
| Period | Q2 2026 (01/04/2026 – 30/06/2026) |
| Budget | ₦12,000,000 (from Lifecycle 3) |
| Actual spend | ₦1,850,000 (MC-EXP-002 from Lifecycle 2) |
| Expected utilisation | 15.4% |

### User Roles Involved
| Step | User | Action |
|------|------|--------|
| 1 | `finance.officer` | Accounting → Budget → Budget Analysis → filter by Maternal Health |
| 2 | `finance.officer` | Accounting → Analytic → Analytic Accounts → Maternal Health → view lines |
| 3 | `finance.officer` | Run General Ledger report filtered to 5030 account |
| 4 | `aliyu.umaru` | Review programme task completion (Lifecycle 7 data) |
| 5 | `finance.officer` | Compile and export PDF reports |

### Expected Output
- Budget Analysis report: Planned ₦12,000,000 vs Actual ₦1,850,000
- Analytic Lines report: shows MC-EXP-002 under Maternal Health
- General Ledger: account 5030 entries
- Project task report: ANC Outreach Visit – Kubwa DONE

### Pass Criteria
- [ ] Budget Analysis shows correct planned and actual amounts
- [ ] Analytic report shows expenses tagged to Maternal Health
- [ ] General Ledger PDF renders with Maternal Health entries
- [ ] At least 1 programme task shows as completed
- [ ] Finance officer can export all reports to PDF
- [ ] Reports show WamaCare (Tiko CBO) as company header

---

## Execution Order

The lifecycles have dependencies. Execute in this order:

```
Step 1: Fix user roles (field.officer → add project user; aliyu.umaru → remove Technical Features)
Step 2: Configure bank account (FIN-012) — required for payment steps
Step 3: Lifecycle 5 (Assets) — independent, no financial data needed
Step 4: Lifecycle 7 (Programme) — independent, creates task data
Step 5: Lifecycle 3 (Budget) — create budget positions and budgets
Step 6: Lifecycle 1 (Procurement) — creates first financial transaction
Step 7: Lifecycle 2 (Finance) — post MC-EXP-002 bill
Step 8: Lifecycle 4 (HR) — expense claim (depends on user-employee link)
Step 9: Lifecycle 6 (Contract) — install hr_contract or use interim
Step 10: Lifecycle 8 (Donor Report) — compile all outputs
```
