# Portal — DRAFT ONLY / DO NOT SUBMIT BEFORE LIVE EVIDENCE

**Type:** Builder → Intelligent Contracts

**Title:** RECALLBOUND — Official-Notice Inventory Scope Adjudication

**Notes (under 1000 characters):**

RECALLBOUND is a reusable GenLayer Intelligent Contract for checking inventory lots against a single, explicitly identified official product recall notice. The registrar binds immutable model, batch, region, notice URL and reference. A GenLayer leader reads the allowlisted CPSC/FDA source and judges notice applicability; validators independently fetch the same page and reevaluate the exact AFFECTED/OUT_OF_SCOPE/UNVERIFIABLE outcome. The contract blocks notice-scoped dispatch authorization unless an exclusion is explicitly established, and enforces a one-time registrar-only authorization. Source errors and ambiguity fail closed. The repo documents threat boundaries, prompt-injection defenses, negative-path tests and limitations: this does not establish overall safety or physical ownership. See contract and signed consensus evidence.

**Evidence links, to add when real:** GitHub repo; real official notice; contract explorer; signed TXs, including fail-closed cases; GenVM lint/integration test results; short video.
