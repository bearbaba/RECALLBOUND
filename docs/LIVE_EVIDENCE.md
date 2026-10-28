# RECALLBOUND V1 — Live Studionet Evidence

**Collected:** 28 October 2026 from builder-provided GenLayer Studio / Explorer screenshots and transaction details. The official CPSC recall was separately inspected; the GenLayer Explorer pages were not independently accessible to the documentation author.

## Deployment and evidence context

- **Network:** GenLayer Studionet (chain ID 61999), Normal (Full Consensus)
- **Contract:** `0xED4C0087B0c85f0445329F1a88d9eC0877aaE353`
- **Studio:** https://studio.genlayer.com/?import-contract=0xED4C0087B0c85f0445329F1a88d9eC0877aaE353
- **Explorer contract:** https://explorer-studio.genlayer.com/address/0xED4C0087B0c85f0445329F1a88d9eC0877aaE353
- **Registrar:** `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`
- **Source:** https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage
- **Official notice reference:** CPSC `25-395`, July 24, 2025
- **Input demo inventory:** fictional `RB-AFFECTED-001`; model `EFMIS129`; serial/batch `A2200`; region `US`

## Verified-from-submitted-evidence transactions

| Step | Transaction | Observed execution | Status |
|---|---|---|---|
| `register_lot` | [`0xaf11e3b43748f0e6d8fae667968697ef28040fbe61613332774ed0110a1d56cb`](https://explorer-studio.genlayer.com/tx/0xaf11e3b43748f0e6d8fae667968697ef28040fbe61613332774ed0110a1d56cb) | FINALIZED; GenVM SUCCESS; consensus Accepted; `null` return | PASS |
| `assess_lot("RB-AFFECTED-001")` | [`0x1697b199278595ccf02f126a84e38ef57740e01ee913ad39f4783d6c583f861c`](https://explorer-studio.genlayer.com/tx/0x1697b199278595ccf02f126a84e38ef57740e01ee913ad39f4783d6c583f861c) | FINALIZED; SUCCESS; consensus Accepted; result **`AFFECTED`**; Equivalence Principle output `AFFECTED`; 4 validator SUCCESS, 1 Idle following quorum | PASS |

**Readback before assessment:** `get_case("RB-AFFECTED-001")` returned `decision: PENDING` and `dispatch_authorized_for_this_notice: false`.

**Subsequent finalized-state readback (builder-provided, 28 October 2026):** `get_case("RB-AFFECTED-001")` returned `model: EFMIS129`, `batch: A2200`, `region: US`, `notice_reference: 25-395`, **`decision: AFFECTED`**, and **`dispatch_authorized_for_this_notice: false`**. This confirms the consensus verdict persisted; it is not a new transaction.

## Evidence still required before Steward submission

- [x] Finalized `get_case("RB-AFFECTED-001")` shows `decision: AFFECTED`, authorization `false` (builder-provided response).
- [ ] Record a **signed, finalized** rejection of `authorize_dispatch_for_notice("RB-AFFECTED-001")` and confirm state unchanged. A prior Studio **Simulation Mode** call returned generic RPC `gen_call` -32000 `execution failed`, consistent with an intentional `UserError` but not proof of the precise rollback reason; simulation produced no on-chain TX.
- [ ] Register fictional `RB-EXCLUDED-002` (`EFMIS129-B`, serial `A2200`, US) tied to the **same** notice, and capture signed transaction.
- [ ] Real `assess_lot("RB-EXCLUDED-002")` returns **`OUT_OF_SCOPE`** with independent consensus, if and only if the live model actually reaches that outcome. An unexpected `UNVERIFIABLE` is not a PASS.
- [ ] Registrar executes one-time notice-scoped authorization only after an on-chain `OUT_OF_SCOPE` verdict; capture state and replay rejection.
- [ ] Negative caller-permission scenario and short reviewer video; independent Explorer review where accessible.

## Interpretation and limits

`AFFECTED` is a decision about **one named government recall notice**. `OUT_OF_SCOPE` would mean an explicit exclusion *from that notice only* and never a broad finding of safety, permission to ship or proof of physical inventory. This project holds no funds, cannot verify manufacturer serial authenticity, and cannot replace official product-safety advice. No real inventory is represented.
