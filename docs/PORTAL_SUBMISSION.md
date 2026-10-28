# RECALLBOUND V1 — Portal submission (ready for Steward review)

**Category:** Builder → Intelligent Contracts

**Title:** RECALLBOUND — Consensus-Verified Recall Scope Gate

## Notes / Description (943/1000 characters)

RECALLBOUND V1 is a standalone GenLayer Intelligent Contract for notice-scoped recall decisions. A registrar locks a fictional inventory lot's model, serial, region, and a specific CPSC/FDA notice URL/reference. A leader fetches the official page; independent validators refetch and assess whether the exact lot is AFFECTED, explicitly OUT_OF_SCOPE, or UNVERIFIABLE. The verdict is stored on-chain and controls a one-time, registrar-only notice-scoped authorization. On Studionet (61999), authentic CPSC notice 25-395 yielded AFFECTED for EFMIS129/A2200 and OUT_OF_SCOPE for excluded variant EFMIS129-B/A2200. The affected case's authorization was rejected; the excluded case's authorization finalized successfully and persisted. A repeated authorization and a non-registrar attempt both finalized with expected rollbacks. Source, signed TXs, tests and reviewer guide are linked. No general product-safety, shipment or ownership certification.

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
- **Non-registrar authorization rollback TX:** https://explorer-studio.genlayer.com/tx/0xe7b2562e9211dd033d7e8b8780ff02e1ff3d93b2fe5f1973f50ec2691fbdffe9
- **Short reviewer video:** optional, not recorded

**Submission status:** Core live Studionet acceptance scenarios are complete: two independent source-backed consensus decisions, signed successful notice-scoped authorization, and signed expected rollbacks for affected-lot denial, replay, and non-registrar callers. Post-revert readbacks and a demo video are optional additional evidence, not claimed as completed. The publication is authentic CPSC 25-395, but page content is not cryptographically pinned. The recorded decision is confined to a single notice, never a general safety clearance. No Steward review or point award has occurred yet.
