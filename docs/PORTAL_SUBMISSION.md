# RECALLBOUND V1 — Portal submission draft (not yet ready)

**Category:** Builder → Intelligent Contracts

**Title:** RECALLBOUND — Consensus-Verified Recall Scope Gate

## Notes / Description (941/1000 characters)

RECALLBOUND V1 is a reusable GenLayer Intelligent Contract that adjudicates whether a registered inventory lot is covered by one named official product recall notice. The registrar locks model, serial/lot, region, notice URL and reference. A leader fetches the CPSC/FDA source; independent validators re-fetch and assess the consequential AFFECTED/OUT_OF_SCOPE/UNVERIFIABLE verdict. Only an explicit, notice-specific exclusion permits a one-time registrar-only authorization; affected, uncertain or unavailable evidence remains blocked. The reviewer demo uses authentic CPSC recall 25-395: EFMIS129 serial A2200 versus the expressly excluded EFMIS129-B variant. Synthetic inventory data and on-chain decision gates are used for testing. The contract does not establish general product safety, inventory custody or legal shipping clearance. Source, adversarial tests, security limitations and live consensus evidence are documented in GitHub.

## Required links when live acceptance succeeds

- GitHub repository: https://github.com/bearbaba/RECALLBOUND
- Technical reviewer guide: https://github.com/bearbaba/RECALLBOUND/blob/main/REVIEWER.md
- Official source (CPSC 25-395): https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage
- **GenLayer contract explorer:** https://explorer-studio.genlayer.com/address/0xED4C0087B0c85f0445329F1a88d9eC0877aaE353
- **Affected assessment TX (AFFECTED):** https://explorer-studio.genlayer.com/tx/0x1697b199278595ccf02f126a84e38ef57740e01ee913ad39f4783d6c583f861c
- **Explicit exclusion assessment TX (OUT_OF_SCOPE):** PENDING
- **Denied authorization rollback TX:** PENDING
- **One-time permitted authorization TX:** PENDING
- **Short reviewer video:** PENDING

**Do not submit yet.** The first affected-case AI assessment is verified from builder-supplied transaction details; the excluded-model and authorization-gate cases remain to be demonstrated. This template deliberately does not fabricate network activity or a Steward assessment. Use the actual date of submission and only include evidence links that have been checked. The website can change and an OUT_OF_SCOPE verdict never proves full product safety.
