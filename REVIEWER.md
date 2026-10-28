# RECALLBOUND V1 — Steward Reviewer Guide

**One-sentence thesis:** RECALLBOUND binds an inventory record to an identified official product recall, independently fetches and interprets natural-language model/serial exclusions through GenLayer validator consensus, then blocks notice-scoped authorization unless an **explicit exclusion** is verified.

## The consequential question

For U.S. CPSC [recall 25-395](<https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage>), a basic model family `EFMIS129` with serial `A2200` falls within the stated affected interval, while the exact suffix variant `EFMIS129-B` is expressly excluded by that same notice. Mere prefix matching or looking only at the serial range would lead to an incorrect result. These are **fictional inventory records** referencing an authentic official notice.

Two live, distinct AI consensus verdicts (builder-provided Explorer receipts):

| Case | Model | Serial | Live AI verdict | Consequence |
|---|---|---|---|---|
| `RB-AFFECTED-001` | `EFMIS129` | `A2200` | `AFFECTED` — [finalized evaluation](https://explorer-studio.genlayer.com/tx/0x1697b199278595ccf02f126a84e38ef57740e01ee913ad39f4783d6c583f861c) | [Expected rollback](https://explorer-studio.genlayer.com/tx/0x05205eb32ac7a4af09eb53bce15274510f9b4c11a1c08f8f5d20fb085481ec0e): dispatch blocked |
| `RB-EXCLUDED-002` | `EFMIS129-B` | `A2200` | `OUT_OF_SCOPE` — [finalized evaluation](https://explorer-studio.genlayer.com/tx/0x49a11d90770225085d48a2a3eb2137464cf715c566009d3dd12d26d1ba663bd4) | [Signed authorization SUCCESS](https://explorer-studio.genlayer.com/tx/0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da); persisted `true` confirmed; [replay rejected](https://explorer-studio.genlayer.com/tx/0x5e0ac57bad1355d44b44295172206076c260adbc1ef253acf36f176486b7951b) |

**Live status:** Both evaluations finalized, GenVM SUCCESS and consensus Accepted; Equivalence Principle outputs were `AFFECTED` and `OUT_OF_SCOPE`. The latter had three agreeing validators (GLM, Gemini, GPT-5.4) and two idle after quorum. Builder-provided `get_case` readback confirmed stored values. A signed [excluded-case authorization transaction](https://explorer-studio.genlayer.com/tx/0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da) subsequently finalized with GenVM SUCCESS (4 validators Agree, 1 Idle); a subsequent `get_case` readback confirmed `decision: OUT_OF_SCOPE` and `dispatch_authorized_for_this_notice: true`. Replay resistance is now supported by a signed [FINALIZED/ERROR rollback](https://explorer-studio.genlayer.com/tx/0x5e0ac57bad1355d44b44295172206076c260adbc1ef253acf36f176486b7951b), with three validators agreeing on `Dispatch authorization already issued`. Unauthorized-wallet rejection remains pending.

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

[Signed transaction evidence and remaining acceptance checks](docs/LIVE_EVIDENCE.md). Two opposite AI verdicts are supported by real Studionet receipts, and the affected-case authorization rollback is supported by a finalized ERROR transaction. Signed excluded-case authorization has succeeded; **persisted `true` is supported by the builder's readback; replay was rejected in a signed finalized transaction; unauthorized-wallet rejection remains untested live**.
