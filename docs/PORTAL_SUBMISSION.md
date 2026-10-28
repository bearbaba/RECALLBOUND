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
- **Explicit exclusion assessment TX (OUT_OF_SCOPE):** https://explorer-studio.genlayer.com/tx/0x49a11d90770225085d48a2a3eb2137464cf715c566009d3dd12d26d1ba663bd4
- **Denied authorization rollback TX:** https://explorer-studio.genlayer.com/tx/0x05205eb32ac7a4af09eb53bce15274510f9b4c11a1c08f8f5d20fb085481ec0e
- **Permitted authorization TX (signed, SUCCESS):** https://explorer-studio.genlayer.com/tx/0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da
- **Replay-protection rollback TX:** https://explorer-studio.genlayer.com/tx/0x5e0ac57bad1355d44b44295172206076c260adbc1ef253acf36f176486b7951b
- **Short reviewer video:** PENDING

**Do not submit yet.** Both AFFECTED and OUT_OF_SCOPE consensus verdicts are supported by builder-supplied finalized transaction details and readbacks; the affected-case authorization was denied as intended. The excluded-case signed authorization completed successfully, and the subsequent readback confirmed persisted `dispatch_authorized_for_this_notice: true`. A signed replay attempt also finalized with expected execution ERROR/rollback. The non-registrar access-control negative case remains to be demonstrated. This template deliberately does not fabricate network activity or a Steward assessment. Use the actual date of submission and only include evidence links that have been checked. The website can change and an OUT_OF_SCOPE verdict never proves full product safety.
