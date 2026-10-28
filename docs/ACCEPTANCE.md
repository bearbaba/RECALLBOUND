# RECALLBOUND V1 — GenLayer Studio Acceptance Plan

**Status: PENDING live validation.** No deployment or GenLayer consensus has been reported yet. Use **GenLayer Studionet (61999)**, **Normal (Full Consensus)**, and **two distinct test wallets**. Do not upgrade or import an address from BIDSEAL; deploy RECALLBOUND as a separate contract.

## Official public source

- **Agency:** U.S. Consumer Product Safety Commission (CPSC)
- **Recall reference:** `25-395`
- **Source:** https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage
- **Published:** 24 July 2025
- **Model family:** `EFMIS129`, `EFMIS137`, `EFMIS149`, `EFMIS175`
- **Relevant rule:** `EFMIS129` serials `A2001`–`A2308` in scope; exact `EFMIS129-B` and `EFMIS129-C` variants expressly excluded from this notice.
- **Scope:** Demo only. Fictional inventory records. An exclusion from this notice does **not** mean product safe to sell or ship.

Before any signed assessment, independently open the notice and confirm that the page has not been altered or made unavailable. It may be blocked by a GenVM validator; then the expected safe state is `UNVERIFIABLE` and the flow must stop.

## 1. Deploy (Wallet A: registrar)

- Open https://studio.genlayer.com/
- Copy [contracts/recallbound.py](../contracts/recallbound.py) **Raw** into Studio.
- Select **Normal (Full Consensus)**.
- Use Wallet A for deployment; `__init__` binds `registrar` to the deployer.
- Click **Deploy new instance** once. Record contract address, Deploy TX and `FINALIZED` plus **GenVM SUCCESS**.
- Do **not** re-label the project V2; first deployed working release is **RECALLBOUND V1**.

## 2. Register affected demo lot — Wallet A

**Write Method:** `register_lot`

| Parameter | Exact input |
|---|---|
| `lot_id` | `RB-AFFECTED-001` |
| `model` | `EFMIS129` |
| `batch` | `A2200` |
| `region` | `US` |
| `official_notice_url` | `https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage` |
| `notice_ref` | `25-395` |

Here, `batch` holds the CPSC **serial number**. Submit, sign and confirm GenVM execution success. Then `get_case("RB-AFFECTED-001")` should show `decision: PENDING` and `dispatch_authorized_for_this_notice: false`.

## 3. AI source adjudication — affected

- **First use Simulation Mode** for `assess_lot("RB-AFFECTED-001")` (avoid consuming the only assessment slot if web fetch fails).
- If it can reach the web source and produce a result, turn off simulation and make a real signed transaction. Capture actual consensus and execution output, including **Equivalence Principle** decision.
- **Expected** `AFFECTED`, but only report whatever on-chain output actually says.
- After success, `get_case` should show `AFFECTED`.
- As registrar, simulate `authorize_dispatch_for_notice("RB-AFFECTED-001")`. It **must fail** with `Not confirmed outside this specific notice`.

If simulation returns `UNVERIFIABLE` or fails, stop; do not treat the notice as verified and do not fabricate positive evidence.

## 4. Register explicitly excluded demo lot — Wallet A

**Write Method:** `register_lot`

| Parameter | Exact input |
|---|---|
| `lot_id` | `RB-EXCLUDED-002` |
| `model` | `EFMIS129-B` |
| `batch` | `A2200` |
| `region` | `US` |
| `official_notice_url` | `https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage` |
| `notice_ref` | `25-395` |

**Simulate** `assess_lot("RB-EXCLUDED-002")`, then sign real assessment if valid. **Expected** `OUT_OF_SCOPE` because the specific model variant is excluded even though the base family and serial interval match. Confirm stored decision from `get_case`.

If and only if the live decision is `OUT_OF_SCOPE`, registrar may execute `authorize_dispatch_for_notice("RB-EXCLUDED-002")` to record a notice-scoped authorization. Confirm `dispatch_authorized_for_this_notice: true`. This has **no real shipping authority**.

## 5. Authorization / replay tests

- Wallet B tries `register_lot("RB-UNAUTHORIZED-003", ...)` in simulation: expect `Only registrar can enroll lots`.
- Wallet B simulates `authorize_dispatch_for_notice("RB-EXCLUDED-002")`: expect `Only registrar can authorize dispatch` (regardless of outcome).
- After a successful notice-scoped authorization, a second attempt by registrar must revert with `Dispatch authorization already issued`.
- `assess_lot` must not allow a second assessment after an outcome is stored.

## 6. Evidence needed for GenLayer Portal

- [ ] GenLayer contract address and deployment transaction
- [ ] Signed `register_lot` TX (two independent cases)
- [ ] Signed `assess_lot` TX returning `AFFECTED` and `OUT_OF_SCOPE`, with consensus details
- [ ] Readback of the two stored verdicts
- [ ] Expected rollback for affected-case dispatch attempt
- [ ] Authorized exclusion (once), and non-owner/replay rollback evidence
- [ ] README + reviewer guide + short screen recording
- [ ] Disclosure that the notice URL is official but **not cryptographically pinned to a snapshot**

Do not submit until real evidence is available. No promises of point allocation or Steward approval.
