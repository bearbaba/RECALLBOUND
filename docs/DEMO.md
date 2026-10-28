# RECALLBOUND — Steward Demo Script (1–2 minutes)

1. Display a real CPSC/FDA notice URL and the model, lot, region, explicit exclusion (if there is one). The synthetic unit-test example is **not valid real-world evidence**.
2. REGISTRAR enrolls affected lot and notice reference using `register_lot`; show signed transaction and immutable read state.
3. Run `assess_lot` and show validator consensus + `AFFECTED` and blocked dispatch.
4. For a legitimately *explicitly excluded* lot in that same official notice, enroll separately, independently assess and show `OUT_OF_SCOPE`.
5. Registrar signs `authorize_dispatch_for_notice` once; show successful transition, then replay attempt rejected.
6. Disconnect the official source or test a conflicting notice in simulator; demonstrate fail-closed `UNVERIFIABLE`.
7. Explain exactly what is proven: **only scope relative to one named notice**, not total product safety or ownership. Do not claim any product is safe based on a single notice.

Capture actual signed TX and `FINISHED_WITH_RETURN` (when v0.6 applies). No live deployment is included in this package.
