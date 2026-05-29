# NGO_CBO_PROCESS_MAP.md — WamaCare Business Process Map

**Date:** 2026-05-29 | **Status:** DRAFT — Phase 8 will complete

---

## Core Business Processes

### 1. Beneficiary Enrolment

```
Field Mobilizer identifies beneficiary
        │
        ▼
Record beneficiary in Odoo (res.partner + tags)
        │
        ▼
Assign to programme (partner category tag)
        │
        ▼
Track activity/service delivery (project.task)
        │
        ▼
Record outcome in M&E programme
```

**Odoo objects:** `res.partner`, `res.partner.category`, `project.task`

---

### 2. Programme Activity Management

```
Programme defined (project.project)
        │
        ▼
Activity planned (project.task + budget)
        │
        ▼
LPO raised for goods/services (purchase.order)
        │
        ▼
LPO approved (purchase workflow)
        │
        ▼
Vendor delivers / service rendered
        │
        ▼
Vendor bill entered (account.move)
        │
        ▼
Expense charged to analytic account (programme)
        │
        ▼
M&E report generated
```

**Odoo objects:** `project.project`, `project.task`, `purchase.order`, `account.move`, `account.analytic.account`

---

### 3. Procurement (LPO) Workflow

```
Programme staff identifies need
        │
        ▼
Request for Quotation (purchase.order draft)
        │
        ▼
Manager reviews and approves LPO
        │
        ▼
LPO sent to vendor
        │
        ▼
Goods/services received
        │
        ▼
Vendor bill matched to LPO
        │
        ▼
Finance approves payment
```

**Odoo objects:** `purchase.order`, `stock.picking` (if inventory), `account.move`

---

### 4. Expense Claim Workflow

```
Field staff incurs programme expense
        │
        ▼
Staff submits expense claim (hr.expense)
        │
        ▼
Programme manager approves
        │
        ▼
Finance reviews and posts
        │
        ▼
Staff reimbursed or expense written off
```

**Odoo objects:** `hr.expense`, `hr.expense.sheet`, `account.move`

---

### 5. Donor/Grant Fund Tracking

```
Grant received (analytic account per donor/programme)
        │
        ▼
Budget set per analytic account
        │
        ▼
All purchases, bills, expenses tagged to analytic account
        │
        ▼
Budget vs actual report generated per programme
        │
        ▼
Donor report created
```

**Odoo objects:** `account.analytic.account`, `account.analytic.line`, reporting

---

### 6. Asset Management

```
Asset procured (purchase.order or manual entry)
        │
        ▼
Asset registered (maintenance.equipment or account.asset)
        │
        ▼
Asset assigned to department/programme
        │
        ▼
Maintenance scheduled (if using maintenance module)
        │
        ▼
Depreciation tracked (if using account.asset)
```

**Odoo objects:** `maintenance.equipment` or `account.asset`

---

## Programme Analytic Account Structure

```
analytic.plan: Programs
├── Maternal Health
├── Capacity Building
├── Safeguarding
├── Monitoring
├── Community Outreach
├── Digital Systems
├── Assets
├── Human Resources
├── Infrastructure
├── Compliance
├── Staff Welfare
├── Administration
└── Operations
```

---

*Full process maps with screenshots to be completed in Phase 8 after functional configuration.*
