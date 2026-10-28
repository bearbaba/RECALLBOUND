# RECALLBOUND — Verifiable Recall-Notice Scope Gate

**Standalone GenLayer Intelligent Contract primitive · Season 2 candidate (v0.2)**

RECALLBOUND determines whether a registered product lot is explicitly affected by, or excluded from, **one specific official recall notice**. It blocks notice-scoped dispatch authorization until independent GenLayer validators confirm an explicit exclusion.

## What it does

1. `register_lot(lot_id, model, batch, region, official_notice_url, notice_ref)` — registrar binds inventory metadata to one official notice.
2. `assess_lot(lot_id)` — leader and validators separately read the notice and judge the model, batch and region.
3. `authorize_dispatch_for_notice(lot_id)` — registrar may authorize once only when `OUT_OF_SCOPE`.
4. `get_case(lot_id)` exposes auditable notice and decision state.

Decisions: **AFFECTED**, **OUT_OF_SCOPE**, **UNVERIFIABLE**.

### Example

A synthetic notice identifies product PX-60, lots BA001–BA100, in the US as recalled and explicitly excludes BA200 and later. Lot BA050 is affected, BA200 is out of scope (if the live notice actually states that exclusion); an inaccessible notice is unverifiable. **This is a synthetic example, not a real-world recall claim.**

## Why GenLayer consensus

Real recall notices contain prose, exclusions, model variants and lot ranges. Independent validators fetch the **same pinned official URL** and separately evaluate whether the scope applies. A missing/uncertain source fails closed; a bare absence of evidence is never proof of safety.

### Strict scope and safety boundary

- Approved URL prefixes: CPSC Recalls and FDA recall notices.
- Rejects basic domain spoofing, userinfo, query, traversal and fragment tricks at registration.
- **OUT_OF_SCOPE means only that one chosen notice explicitly excludes the lot.** It does not certify product safety, physical provenance or absence of other recalls.
- Dynamic web pages, redirects, source availability and prompt injection require live adversarial GenVM testing.
- This contract neither transports goods nor supplies a comprehensive safety clearance. Do not use it for real shipments without independent regulatory/operational review.

## Run local tests

```bash
python -m unittest discover -s tests -v
```

**Local shim regression status: 20/20 passed on 2026-10-28.** These are pure-Python simulated tests, **not** GenVM compilation, deployment, validator consensus or signed blockchain transactions.

## Evidence required before Portal submission

- [ ] GenVM lint/compile and pinned runtime
- [ ] Accessible, genuine official recall notice with explicit model/lot scope
- [ ] Deploy and assess on real GenLayer validators, explorer links
- [ ] Blocked dispatch authorization for affected or unclear scope
- [ ] An explicit-exclusion case authorized by registrar
- [ ] Source failure and independent validator evidence
- [ ] Reviewer demo and actual deployed contract URL

**Current status:** Source candidate, not chain-tested or production-ready. Never use as sole safety clearance.

MIT License. Please review [SECURITY.md](SECURITY.md).
