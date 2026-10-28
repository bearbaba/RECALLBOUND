# SECURITY — RECALLBOUND V1

**Security status:** Research-stage Intelligent Contract, **unaudited**. Not approved for real logistics, compliance certification, or public safety decisions.

## Intended guarantee

The registrar records a *fixed notice URL/reference and fictional inventory metadata*. Validators independently decide whether that specific notice explicitly affects or excludes the referenced item. The on-chain gate allows a **single notice-scoped authorization**, and only to the registrar, if the decision is `OUT_OF_SCOPE`.

This is not evidence of actual ownership, a valid serial number, physical provenance, general safety, compliance, sale or shipment legality, or that other recalls do not exist.

## Known risks

- **Unpinned external content:** the URL is immutable in contract state, **not** a cryptographically pinned source snapshot. Content may change, disappear or be inconsistent across validators.
- **URL redirects:** approved registration prefixes do not guarantee the final redirected URL has the same origin. The source trust policy needs additional hardening for real-world use.
- **Prompt injection:** a real government-hosted page can contain attacker-influenced or unrelated text; model instructions and textual fences are insufficient to guarantee injection immunity.
- **Model/serial ambiguity:** mixed naming conventions, suffixes, serial ranges, regional restrictions and overlapping notices may yield uncertain judgments; do not equate missing data with explicit exclusion.
- **Registrar trust:** registration is owner-controlled. There is no proof that the registered inventory record matches a physical unit.
- **Historical decision:** the contract does not automatically re-evaluate old decisions as notices are updated, nor does it prove no additional notice exists.
- **Validator availability:** fetching official websites may fail or yield different HTML/text in different validators. `UNVERIFIABLE` and rejection are safer than unsupported authorization.
- **One-time authorization:** an authorized notice-specific state does not imply a shipping permit and is irreversible in V1.

## Operational restrictions

Do not connect to real shipping, inventory clearance, commerce, regulatory reporting or financial settlement. Use only fictional inventory data and testnet wallets. Never publish private keys, personal customer details or credentials in repository issues. Report security concerns privately to the repository maintainer.

Local shim tests provide logic regressions only; GenVM, browser fetch, validator consensus and wallet signature behavior must be tested separately.
