# TEMPLATE_STRATEGY.md — WamaCare as a Reusable NGO/CBO Odoo Template

**Phase:** 1 | **Date:** 2026-05-29 | **Status:** DRAFT

---

## Purpose

WamaCare is built not just for Tiko CBO but as a **reusable Odoo 17 template** that any Nigerian or African NGO, CBO, donor-funded programme, or social-impact organisation can deploy with minimal customisation.

---

## Template Philosophy

| Principle | Application |
|-----------|------------|
| Native Odoo first | Use standard Odoo modules and configuration before custom code |
| Configuration over customisation | Achieve NGO workflows through tags, analytic accounts, project stages, and partner categories |
| Documented everything | Every decision, configuration, and import sequence is documented so any developer can reproduce the setup |
| Reproducible | Full backup + restore + import sequence documented; a new deployment takes hours not weeks |
| Sector-neutral core | Core patterns (beneficiaries, programmes, procurement, M&E) work for health, education, livelihoods, WASH, protection |
| Nigeria-first | Nigerian procurement norms (LPOs), NGN currency, FCT/state structure, PENCOM/ITF/NSITF compliance |

---

## Template Applicability Matrix

| Organisation Type | Fit | Notes |
|------------------|-----|-------|
| Maternal health CBO | HIGH | WamaCare is the reference |
| Women empowerment NGO | HIGH | Beneficiary + programme patterns apply |
| Child protection NGO | HIGH | Safeguarding workflows directly reusable |
| Community outreach CBO | HIGH | Field operations + mobilizer tracking |
| Donor-funded programme | HIGH | Analytic accounts per donor/grant |
| Food security / WASH NGO | MEDIUM | Products/services need adjustment |
| Education NGO | MEDIUM | Beneficiaries → students; activities → sessions |
| Healthcare NGO (non-clinical) | MEDIUM | Add health service products, keep CBO model |
| Clinical hospital | LOW | Needs dedicated healthcare modules |
| HMO / health insurance | LOW | Fundamentally different model |
| FMCG / manufacturing | NOT FIT | Use FamOil template instead |

---

## Reusable Template Components

### 1. Beneficiary Management
- `res.partner` tagged as Beneficiary + programme tags
- Custom reference format (BEN-XXX)
- Geolocation fields (for FCT/state mapping)
- Filterable by programme, location, gender, status

### 2. Programme / Project Management
- `project.project` with analytic account linkage
- Project stages aligned to NGO delivery phases
- Activity/task tracking per programme
- Budget tracking per project

### 3. Donor and Funder Tracking
- `res.partner` tagged as Donor/Funder
- Analytic accounts per donor/grant
- Expense tracking per analytic account

### 4. Procurement (LPO-based)
- `purchase.order` as Local Purchase Order
- Approval workflow for LPO authorisation
- Vendor management with vendor categories
- Budget check before LPO creation (future enhancement)

### 5. Field Operations
- Field Officer employees linked to programmes
- Activity tasks assigned to field staff
- Community mobilizer tracking

### 6. HR and Payroll (basic)
- Departments aligned to NGO structure
- Employee records with job positions
- Expense reports per employee

### 7. Asset Management
- Equipment register for field assets
- Fixed asset tracking for high-value items
- Asset assignment to programmes

### 8. Analytics and M&E
- Analytic accounts per programme
- Expense vs budget reporting per analytic
- Project progress and task completion reporting

---

## Template Adaptation Guide (for other deployments)

When forking WamaCare for a new NGO/CBO:

1. **Change organisation profile** in Odoo settings (company name, logo, address)
2. **Rename programmes** to match new organisation's projects
3. **Update analytic accounts** to match new grant/donor structure
4. **Load new beneficiary data** using `csv_templates/wamacare/beneficiaries.csv` as template
5. **Load new vendor data** using vendor CSV templates
6. **Configure approval thresholds** to match new organisation's procurement policy
7. **Update department structure** if different
8. **Adjust product/service list** to match new programme services
9. **Adjust user roles** and access rights per new org chart

Estimated adaptation time: **1-3 days** for a similar NGO/CBO.

---

## Template Versioning

| Version | Notes |
|---------|-------|
| `v0.1.0` | Initial setup, Phase -1 to Phase 3 complete |
| `v0.2.0` | Database restored, modules confirmed (Phase 5-6) |
| `v0.3.0` | Data imported, functional configuration complete (Phase 7-8) |
| `v1.0.0` | Tested, validated, backup drill complete — production-ready template |

---

## Related Documents

- [PROJECT_IDENTITY.md](./PROJECT_IDENTITY.md) — what WamaCare is
- [MODULE_REGISTRY.md](./MODULE_REGISTRY.md) — modules in the template
- [REUSE_GUIDE.md](./REUSE_GUIDE.md) — step-by-step fork instructions
- [GOVERNANCE_MODEL.md](./GOVERNANCE_MODEL.md) — governance and maintenance
- [ROADMAP.md](./ROADMAP.md) — milestones to template maturity

---

*Template strategy defined from inspection of CBO mandate documents and CSV data files.*
