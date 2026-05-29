# PRIORITIZATION_RULES.md — WamaCare Feature Prioritization Engine

**Version:** 1.0 | **Date:** 2026-05-29
**Authority:** These rules govern all future feature development and AI recommendations. Repository governance overrides AI preference.

---

## Priority Order

Any feature request — whether from an operator, donor, developer, or AI — must be evaluated against this priority order:

| Rank | Domain | Rationale |
|------|--------|-----------|
| **1** | **Safeguarding** | Women and girls may be harmed if safeguarding systems fail. No other priority can override this. |
| **2** | **Beneficiary Protection** | Personal data of vulnerable individuals must be protected before expanding functionality. |
| **3** | **Donor Accountability** | Financial transparency is an existential requirement — loss of donor trust ends the programme. |
| **4** | **Financial Control** | Budget integrity, procurement discipline, and audit trails protect the organisation. |
| **5** | **Programme Delivery** | Activities must be planned, tracked, and reported before measuring impact. |
| **6** | **Impact Measurement** | Measuring outcomes requires delivery infrastructure to be stable first. |
| **7** | **Sustainability** | Economic empowerment and entrepreneurship build the path off donor dependency. |
| **8** | **Ecosystem Expansion** | External integrations (Blood Bank, Safe House, partners) come last — core must be stable first. |

---

## How to Apply These Rules

### When a new feature is requested:

**Step 1:** Check FEATURE_REGISTRY.md — does this feature already exist?
- If YES (status = COMPLETED): do not re-implement.
- If YES (status = PARTIAL or PLANNED): continue to Step 2.
- If NO: add it to the registry before implementing.

**Step 2:** Identify the feature's domain and check which Priority Rank it falls under.

**Step 3:** Check that all features of higher rank are at least PARTIAL before implementing lower-rank features.

**Exception:** A lower-rank feature may be implemented before higher-rank features only if:
1. The higher-rank feature depends on infrastructure not yet available, AND
2. The lower-rank feature is a prerequisite for the higher-rank feature, AND
3. The decision is recorded in DECISION_LOG.md.

---

## Priority Application Examples

### Example 1: Donor requests a custom impact report
- Domain: Impact Measurement (Rank 6)
- Check: Are Safeguarding (1), Beneficiary Protection (2), Donor Accountability (3), Financial Control (4), and Programme Delivery (5) stable?
- If Safeguarding alerts (SAFE-005) are not yet built → **DEFER** the impact report until SAFE-005 is done.

### Example 2: Operator wants to add inventory tracking
- Domain: Programme Delivery support (Rank 5)
- Check: Are Safeguarding features stable? Is beneficiary data protected (BEN-006)?
- If BEN-006 is not done → build BEN-006 first, then inventory.

### Example 3: Request for Blood Bank integration
- Domain: Ecosystem Expansion (Rank 8)
- Check: Is the entire v1.x platform stable and validated?
- Until v1.3 is released → **DEFER** Blood Bank to Release 2.0.

---

## Absolute Rules

These rules cannot be overridden by any request:

| Rule | Description |
|------|------------|
| SAFE-FIRST | Safeguarding alert flags (SAFE-005) must be built before any Release 1.1 feature can ship |
| DATA-PROTECT | Beneficiary access restriction (BEN-006) must be in place before beneficiary data grows beyond 50 records |
| NO-CLINIC | WamaCare will never implement clinical patient records, prescription management, or diagnostic workflows |
| NO-ENTERPRISE | WamaCare uses Odoo Community Edition. Enterprise modules require explicit operator decision and licence acquisition |
| SEQUENCE | Releases ship in order: 1.0 → 1.1 → 1.2 → 1.3 → 2.0. No skipping |
| DOCUMENT-FIRST | No feature is built without a corresponding Feature ID in FEATURE_REGISTRY.md |
| NEXT-FEATURE | Only one feature is ever "next". See NEXT_FEATURE.md |

---

## Evaluating AI Feature Suggestions

When an AI (including Claude Code) suggests a new feature:

1. The AI must first read BUSINESS_CAPABILITY_MAP.md, FEATURE_REGISTRY.md, WAMACARE_PRODUCT_ROADMAP.md, NEXT_FEATURE.md, and this document.
2. The AI must check if the feature already exists.
3. The AI must verify the feature fits the current release scope.
4. The AI must not recommend a feature that violates sequence or these absolute rules.
5. If the AI recommends a feature not in the registry, it must first propose the Feature ID and get operator confirmation before proceeding.

---

## Updating These Rules

These rules may only be updated by:
1. Operator explicit instruction, AND
2. A recorded entry in DECISION_LOG.md explaining why the update was made.

AI sessions may not update this file without explicit operator authorisation.
