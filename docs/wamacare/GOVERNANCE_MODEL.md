# GOVERNANCE_MODEL.md — WamaCare Governance Model

**Date:** 2026-05-29 | **Status:** DRAFT

---

## Governance Principles

1. **Repository is the source of truth.** Any undocumented change is an unauthorised change.
2. **No destructive action without approval.** Dropping databases, deleting files, or force-pushing requires explicit operator sign-off.
3. **Every phase ends with a commit.** Code and documentation are committed to Git at the end of every phase.
4. **CLAUDE.md stays current.** Any AI session that ends without updating CLAUDE.md has not followed governance.
5. **Isolation is non-negotiable.** WamaCare and FamOil must never share files, databases, or config.

---

## Decision Authority

| Type of Decision | Who Can Authorise |
|-----------------|------------------|
| Drop or overwrite a database | Operator only |
| Delete files from the repository | Operator only |
| Install third-party modules | Operator approval required |
| Force push to GitHub | NOT PERMITTED |
| Add new phases or change scope | Operator approval |
| Architecture changes | Must be recorded in DECISION_LOG.md |
| Credential changes | Operator only — never committed to Git |

---

## Change Management

All significant changes must be:
1. Documented in the relevant phase document
2. Recorded in `DECISION_LOG.md` if architectural
3. Recorded in `KNOWN_ISSUES.md` if a bug or blocker
4. Committed to Git with a clear commit message
5. Pushed to GitHub after phase validation

---

## Branch Protection

| Branch | Protection Level |
|--------|----------------|
| `main` | No direct push; PR required (future) |
| `dev` | Direct push allowed during active development |

---

## AI Session Rules

At the start of every session:
1. Read `CLAUDE.md` — this is the session anchor
2. Check `KNOWN_ISSUES.md` for open blockers
3. Check `ROADMAP.md` for current phase
4. Do NOT proceed with database work without operator confirmation

At the end of every session:
1. Update `CLAUDE.md` with current phase status
2. Commit all changes
3. Push to GitHub

---

## Escalation

If Claude Code is uncertain about any action, the rule is: **STOP and ask the operator**.

Contact: aliyuumaru@gmail.com
