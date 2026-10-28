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
| `authorize_dispatch_for_notice("RB-AFFECTED-001")` | [`0x05205eb32ac7a4af09eb53bce15274510f9b4c11a1c08f8f5d20fb085481ec0e`](https://explorer-studio.genlayer.com/tx/0x05205eb32ac7a4af09eb53bce15274510f9b4c11a1c08f8f5d20fb085481ec0e) | FINALIZED; consensus Accepted; GenVM ERROR with Rollback `Not confirmed outside this specific notice` (registrar Wallet A, 2026-10-28 21:12:47 local) | PASS — expected rejection |
| `register_lot("RB-EXCLUDED-002")` | [`0xe70758cb117662808cc347544c1b9549ddc32f9c07e68e33653dc274639c70de`](https://explorer-studio.genlayer.com/tx/0xe70758cb117662808cc347544c1b9549ddc32f9c07e68e33653dc274639c70de) | FINALIZED; GenVM SUCCESS; consensus Accepted; `EFMIS129-B`, serial `A2200`, US, CPSC 25-395 | PASS — registration only |
| `assess_lot("RB-EXCLUDED-002")` | [`0x49a11d90770225085d48a2a3eb2137464cf715c566009d3dd12d26d1ba663bd4`](https://explorer-studio.genlayer.com/tx/0x49a11d90770225085d48a2a3eb2137464cf715c566009d3dd12d26d1ba663bd4) | FINALIZED; GenVM SUCCESS; consensus Accepted; return `OUT_OF_SCOPE`; Equivalence Principle `OUT_OF_SCOPE`; 3 Agree (GLM, Gemini, GPT-5.4) and 2 Idle after quorum | PASS |
| `authorize_dispatch_for_notice("RB-EXCLUDED-002")` | [`0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da`](https://explorer-studio.genlayer.com/tx/0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da) | FINALIZED; GenVM SUCCESS; consensus Accepted; returned `null`; 4 validator Agree (Minimax, GLM, GPT-5.4, DeepSeek), 1 Idle after quorum | PASS — signed authorization call |

**Readback before assessment:** `get_case("RB-AFFECTED-001")` returned `decision: PENDING` and `dispatch_authorized_for_this_notice: false`.

**Subsequent finalized-state readback (builder-provided, 28 October 2026):** `get_case("RB-AFFECTED-001")` returned `model: EFMIS129`, `batch: A2200`, `region: US`, `notice_reference: 25-395`, **`decision: AFFECTED`**, and **`dispatch_authorized_for_this_notice: false`**. This confirms the consensus verdict persisted; it is not a new transaction.

**Readback for excluded demo lot (before assessment):** `get_case("RB-EXCLUDED-002")` returned `model: EFMIS129-B`, `batch: A2200`, `region: US`, `notice_reference: 25-395`, `decision: PENDING`, and `dispatch_authorized_for_this_notice: false`. This was the pre-assessment state.

**Post-assessment, pre-authorization readback (builder-provided, 28 October 2026):** `get_case("RB-EXCLUDED-002")` returned model `EFMIS129-B`, batch/serial `A2200`, region `US`, notice reference `25-395`, **`decision: OUT_OF_SCOPE`**, and **`dispatch_authorized_for_this_notice: false`**. This confirmed the verdict was stored before the later signed authorization call. A fresh post-authorization readback is still required.

**Post-authorization readback (builder-provided, 28 October 2026):** after signed authorization TX `0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da`, `get_case("RB-EXCLUDED-002")` returned `model: EFMIS129-B`, `batch: A2200`, `region: US`, `notice_reference: 25-395`, **`decision: OUT_OF_SCOPE`**, and **`dispatch_authorized_for_this_notice: true`**. This confirms persisted authorization. This read-only call is not a separate signed transaction.

## Evidence still required before Steward submission

- [x] Finalized `get_case("RB-AFFECTED-001")` shows `decision: AFFECTED`, authorization `false` (builder-provided response).
- [x] Signed `authorize_dispatch_for_notice("RB-AFFECTED-001")` finalized with expected execution ERROR and Rollback `Not confirmed outside this specific notice` (TX above).
- [ ] After rollback, fresh `get_case("RB-AFFECTED-001")` still shows `decision: AFFECTED`, `dispatch_authorized_for_this_notice: false`.
- [x] Register fictional `RB-EXCLUDED-002` (`EFMIS129-B`, serial `A2200`, US) tied to the **same** notice; signed registration finalized successfully (TX above).
- [x] Real `assess_lot("RB-EXCLUDED-002")` returned `OUT_OF_SCOPE` with independent consensus and verified view readback (TX above).
- [x] Registrar authorization call after a signed `OUT_OF_SCOPE` verdict finalized with GenVM SUCCESS and consensus Accepted (TX above).
- [x] **Post-authorization readback:** builder-provided `get_case("RB-EXCLUDED-002")` confirms `decision: OUT_OF_SCOPE`, `dispatch_authorized_for_this_notice: true`, model `EFMIS129-B`, serial `A2200`, and recall `25-395`.
- [ ] Second authorization attempt by registrar is rejected with `Dispatch authorization already issued`, and authorization remains `true` after rollback.
- [ ] Negative caller-permission scenario and short reviewer video; independent Explorer review where accessible.

## Interpretation and limits

`AFFECTED` is a decision about **one named government recall notice**. `OUT_OF_SCOPE` would mean an explicit exclusion *from that notice only* and never a broad finding of safety, permission to ship or proof of physical inventory. This project holds no funds, cannot verify manufacturer serial authenticity, and cannot replace official product-safety advice. No real inventory is represented.
