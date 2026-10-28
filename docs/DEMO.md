# RECALLBOUND V1 — Steward Demo Script (90–120 seconds)

Use the exact [Studio test plan](ACCEPTANCE.md) and authentic [CPSC 25-395 notice](<https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage>). The inventory records are fictional and the notice applies only to its own named recall.

1. **0–15s:** Show source contract and official notice; focus on `EFMIS129` serial `A2001–A2308` and the explicit exclusion of `EFMIS129-B`/C.
2. **15–35s:** Signed `register_lot` for `RB-AFFECTED-001` and `RB-EXCLUDED-002`, showing fixed URL, models, serial and notice ref.
3. **35–60s:** Real `assess_lot` on both: expected `AFFECTED` versus `OUT_OF_SCOPE`, with **actual** validator results and transaction hashes.
4. **60–85s:** The first case is blocked. The excluded variant, if consensus confirmed, can be authorized once by registrar only.
5. **85–105s:** Show non-owner rejection or second authorization replay, including rollback reason, and explain why `UNVERIFIABLE` is a fail-closed result.
6. **105–120s:** State the boundary: “This is notice-specific scope adjudication, not proof of general product safety or a real-world shipping permit.”

If GenVM web rendering fails or validators return `UNVERIFIABLE`, show that fact truthfully and stop. Never claim the expected verdicts or signed transactions occurred without evidence.
