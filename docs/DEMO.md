# RECALLBOUND V1 — Steward Demo Script (90–120 seconds)

Use the exact [Studio test plan](ACCEPTANCE.md) and authentic [CPSC 25-395 notice](<https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage>). The inventory records are fictional and the notice applies only to its own named recall.

1. **0–15s:** Show source contract and official notice; focus on `EFMIS129` serial `A2001–A2308` and the explicit exclusion of `EFMIS129-B`/C.
2. **15–35s:** Signed `register_lot` for `RB-AFFECTED-001` and `RB-EXCLUDED-002`, showing fixed URL, models, serial and notice ref.
3. **35–60s:** Show the **already finalized** `assess_lot` transactions: `AFFECTED` versus `OUT_OF_SCOPE`, with actual Equivalence Principle outputs and transaction hashes from [LIVE_EVIDENCE](LIVE_EVIDENCE.md).
4. **60–85s:** Show the recorded affected-lot authorization rollback, the excluded-lot signed authorization SUCCESS and stored `true` readback.
5. **85–105s:** Show the two recorded signed rollbacks: [replay rejected](https://explorer-studio.genlayer.com/tx/0x5e0ac57bad1355d44b44295172206076c260adbc1ef253acf36f176486b7951b) and [non-registrar rejected](https://explorer-studio.genlayer.com/tx/0xe7b2562e9211dd033d7e8b8780ff02e1ff3d93b2fe5f1973f50ec2691fbdffe9); explain why `UNVERIFIABLE` is fail-closed.
6. **105–120s:** State the boundary: “This is notice-specific scope adjudication, not proof of general product safety or a real-world shipping permit.”

If GenVM web rendering fails or validators return `UNVERIFIABLE`, show that fact truthfully and stop. Never claim the expected verdicts or signed transactions occurred without evidence.
