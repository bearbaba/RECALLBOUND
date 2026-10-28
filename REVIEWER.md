# RECALLBOUND V1 — Steward Reviewer Guide

**One-sentence thesis:** RECALLBOUND binds an inventory record to an identified official product recall, independently fetches and interprets natural-language model/serial exclusions through GenLayer validator consensus, then blocks notice-scoped authorization unless an **explicit exclusion** is verified.

## The consequential question

For U.S. CPSC [recall 25-395](<https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage>), a basic model family `EFMIS129` with serial `A2200` falls within the stated affected interval, while the exact suffix variant `EFMIS129-B` is expressly excluded by that same notice. Mere prefix matching or looking only at the serial range would lead to an incorrect result. These are **fictional inventory records** referencing an authentic official notice.

Two anticipated results:

| Case | Model | Serial | Expected AI verdict | Consequence |
|---|---|---|---|---|
| `RB-AFFECTED-001` | `EFMIS129` | `A2200` | `AFFECTED` | Notice-scoped dispatch remains blocked |
| `RB-EXCLUDED-002` | `EFMIS129-B` | `A2200` | `OUT_OF_SCOPE` | Only registrar may authorize once for this exact notice |

**Important:** These are **test expectations**, not on-chain outcomes. No proof of live verdicts exists until the actual Studio transaction and finalized state are recorded.

## Where GenLayer consensus is essential

- A deterministic URL allowlist, caller check and immutable state alone cannot adjudicate overlapping recall models, suffix exceptions and serial qualifiers expressed in prose.
- The leader retrieves the official notice and produces one decision label.
- Every validator independently retrieves the source again and performs the same assessment; only comparable consequential verdicts are accepted.
- The decision becomes stored state, gating a real on-chain authorization method.
- A missing source, reference mismatch, ambiguous or contradictory scope must fail closed to `UNVERIFIABLE`, not “safe”.

Read [source](contracts/recallbound.py), [Studio acceptance plan](docs/ACCEPTANCE.md), and [security limitations](SECURITY.md).

## Threat model and constraints

Data origin is limited by an allowlist of CPSC/FDA HTTPS path prefixes, **but** the contract does not validate post-redirect response origin or pin exact response bytes; website content may change and output may vary between validators. Free-text inputs and website content may contain prompt injection. Only a named notice is considered: being `OUT_OF_SCOPE` cannot establish a product is generally safe, permitted to ship, or unaffected by other notices.

The product is not a logistics application, safety certification, escrow or inventory custody proof. It is an **Intelligent Contract primitive** intended for controlled development and study.

## Live evidence

**Not yet available.** Fill with signed transaction hashes, actual GenVM execution and Equivalence Principle results after Studio tests. Do not insert simulated or synthetic receipts.
