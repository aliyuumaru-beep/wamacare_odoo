# ROADMAP.md — WamaCare Implementation Roadmap

**Date:** 2026-05-29 | **Version:** 0.1.0

---

## Current Status

| Phase | Name | Status | Date |
|-------|------|--------|------|
| -1 | Repository and project boundary setup | COMPLETE | 2026-05-29 |
| 0 | Local inspection and orientation | COMPLETE | 2026-05-29 |
| 1 | Project identity and template positioning | COMPLETE | 2026-05-29 |
| 2 | Safe backup before work | COMPLETE | 2026-05-29 |
| 3 | Software Factory structure | COMPLETE | 2026-05-29 |
| 4 | Local Odoo environment setup | PENDING | — |
| 5 | Database restore or creation | PENDING | — |
| 6 | Module detection and installation | PENDING | — |
| 7 | Data import | PENDING | — |
| 8 | Functional configuration | PENDING | — |
| 9 | Roadmap and template governance | PENDING | — |
| 10 | Testing and validation | PENDING | — |
| 11 | Backup and restore drill | PENDING | — |
| 12 | Final documentation, GitHub push, handover | PENDING | — |

---

## MVP Definition

WamaCare MVP is achieved when:
- [ ] Odoo 17 running locally on port 8070 with `wamacare_local` database
- [ ] All 5 programmes visible and navigable
- [ ] Beneficiaries importable and searchable by programme/location
- [ ] LPO/purchase order workflow functional
- [ ] Analytic account reporting per programme
- [ ] Staff and departments configured
- [ ] Assets registered
- [ ] Backup and restore drill passed
- [ ] All documentation current
- [ ] GitHub repository up to date

---

## Milestones

See detailed milestone documents:
- [MILESTONE_1_MVP.md](./roadmap/MILESTONE_1_MVP.md) — Working local instance
- [MILESTONE_2_TEMPLATE_HARDENING.md](./roadmap/MILESTONE_2_TEMPLATE_HARDENING.md) — Reproducible template
- [MILESTONE_3_MULTI_ORG_REUSE.md](./roadmap/MILESTONE_3_MULTI_ORG_REUSE.md) — First fork for a second org
- [MILESTONE_4_COMMERCIALIZATION.md](./roadmap/MILESTONE_4_COMMERCIALIZATION.md) — Paid deployment offering

---

## Known Blockers

| # | Blocker | Required Action |
|---|---------|----------------|
| 1 | Database not restored | Confirm DB name and restore `mamacare1.dump.zip` |
| 2 | wamacare.conf not created | Create dedicated Odoo config (Phase 4) |
| 3 | Module list not confirmed | Inspect database post-restore (Phase 6) |
| 4 | No custom addons yet | Assess after Phase 5 if any needed |

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Dump incompatible with Odoo 17 | LOW | HIGH | Confirm version before restore; have clean DB fallback |
| Data in dump is sensitive | MEDIUM | HIGH | Do not commit dump to Git; document storage separately |
| FamOil port conflict (8069) | LOW | MEDIUM | Use 8070 for WamaCare |
| Future laptop loss | MEDIUM | HIGH | GitHub push + offsite backup |
| AI context loss | LOW | MEDIUM | CLAUDE.md is self-contained |

---

*Roadmap will be updated at the end of each phase.*
