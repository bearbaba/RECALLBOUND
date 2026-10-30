# RECALLBOUND — GenLayer submission

**Category:** Builder / Intelligent Contracts  
**Title:** RECALLBOUND — Recall Notice Scope Check

## Description (911/1000 characters)

Most recall checks aren't as simple as matching a model number. I built RECALLBOUND to see if GenLayer could read an actual recall notice, including serial ranges and model exclusions, before recording a decision on-chain.

A registrar registers a test inventory lot and a CPSC/FDA notice URL. The leader and validators independently fetch the page and compare AFFECTED, OUT_OF_SCOPE or UNVERIFIABLE. Only an explicit OUT_OF_SCOPE result lets the registrar record an authorization for that specific notice, once.

I tested it on Studionet (61999) using CPSC recall 25-395. EFMIS129 / A2200 returned AFFECTED and authorization was blocked. EFMIS129-B / A2200 returned OUT_OF_SCOPE; authorization succeeded and the flag was saved. A repeat call and a call from another wallet both reverted. Code, tests and signed transaction receipts are in the repo. This does not certify product safety or allow real shipments.

## Links for review

- [Code, tests and README](https://github.com/bearbaba/RECALLBOUND)
- [Contract on Studionet (61999)](https://explorer-studio.genlayer.com/address/0xED4C0087B0c85f0445329F1a88d9eC0877aaE353)
- [CPSC recall 25-395 — the source used in both tests](https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage)
- [AFFECTED — finalized assessment](https://explorer-studio.genlayer.com/tx/0x1697b199278595ccf02f126a84e38ef57740e01ee913ad39f4783d6c583f861c)
- [OUT_OF_SCOPE — finalized assessment](https://explorer-studio.genlayer.com/tx/0x49a11d90770225085d48a2a3eb2137464cf715c566009d3dd12d26d1ba663bd4)
- [Authorization succeeded for the excluded variant](https://explorer-studio.genlayer.com/tx/0x985fef53a3a026bbc5120ad85d0ac2012852cd9602bf904032c238494668b4da)
- [Authorization blocked for the affected model](https://explorer-studio.genlayer.com/tx/0x05205eb32ac7a4af09eb53bce15274510f9b4c11a1c08f8f5d20fb085481ec0e)
- [Repeat authorization rejected](https://explorer-studio.genlayer.com/tx/0x5e0ac57bad1355d44b44295172206076c260adbc1ef253acf36f176486b7951b)
- [Non-registrar authorization rejected](https://explorer-studio.genlayer.com/tx/0xe7b2562e9211dd033d7e8b8780ff02e1ff3d93b2fe5f1973f50ec2691fbdffe9)
- [Detailed receipts and reviewer notes](https://github.com/bearbaba/RECALLBOUND/blob/main/docs/LIVE_EVIDENCE.md)

The inventory examples are fictional. The two assessments and signed authorization completed successfully; the three rejected calls finalized with expected execution errors. The web page is referenced by URL, not pinned to a content hash. I haven't recorded a demo video.
