"""RECALLBOUND V1: controlled fixture derived from official CPSC recall 25-395.

This is a Python shim test: LLM verdicts are mocked. It checks source/decision
wiring, state guards, and prompt boundaries, NOT a live GenLayer AI judgment.
Source: https://www.cpsc.gov/Recalls/2025/Curtis-International-Recalls-Frigidaire-brand-Minifridges-Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage
"""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from test_shim import Driver, UserError

NOTICE_URL = (
    "https://www.cpsc.gov/Recalls/2025/"
    "Curtis-International-Recalls-Frigidaire-brand-Minifridges-"
    "Due-to-Fire-and-Burn-Hazards-More-Than-700-000-Reported-in-Property-Damage"
)
NOTICE_TEXT = (
    "CPSC recall number 25-395. Curtis International Frigidaire-brand "
    "mini-refrigerators, models EFMIS129, EFMIS137, EFMIS149 and EFMIS175, "
    "with relevant serial-number ranges, are recalled for fire and burn hazards. "
    "EFMIS129 serial numbers A2001 to A2308 are included, EXCEPT exact model "
    "variants EFMIS129-B and EFMIS129-C which the notice explicitly excludes. "
    "Affected devices must not be offered for shipment. "
    "These fixtures summarize a public notice; they do not prove the actual "
    "web-rendering or AI decisions on GenLayer."
)

class CpscNoticeFixtureTests(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().load(ROOT / "contracts/recallbound.py")
        self.contract = self.driver.contract
        self.driver.pages[NOTICE_URL] = NOTICE_TEXT

    def enroll(self, lot_id, model):
        self.contract.register_lot(
            lot_id, model, "A2200", "US", NOTICE_URL, "25-395"
        )

    def test_real_notice_url_allowed_and_immutable(self):
        self.enroll("CPSC-AFFECTED-001", "EFMIS129")
        case = self.contract.get_case("CPSC-AFFECTED-001")
        self.assertEqual(case["notice_url"], NOTICE_URL)
        self.assertEqual(case["notice_reference"], "25-395")
        with self.assertRaises(UserError):
            self.enroll("CPSC-AFFECTED-001", "EFMIS129-B")

    def test_explicit_model_variant_exclusion_is_prominent_in_prompt(self):
        self.enroll("CPSC-EXCLUDED-002", "EFMIS129-B")
        def simulate_model(prompt, call):
            self.assertIn("Exact model exclusions take precedence", prompt)
            self.assertIn("<MODEL>EFMIS129-B</MODEL>", prompt)
            self.assertIn("<BATCH>A2200</BATCH>", prompt)
            self.assertIn("<NOTICE_REFERENCE>25-395</NOTICE_REFERENCE>", prompt)
            self.assertIn("EFMIS129-B", prompt)
            return "OUT_OF_SCOPE"
        self.driver.llm = simulate_model
        self.assertEqual(self.contract.assess_lot("CPSC-EXCLUDED-002"), "OUT_OF_SCOPE")
        self.contract.authorize_dispatch_for_notice("CPSC-EXCLUDED-002")
        self.assertTrue(self.contract.get_case("CPSC-EXCLUDED-002")["dispatch_authorized_for_this_notice"])

    def test_affected_lot_cannot_be_authorized(self):
        self.enroll("CPSC-AFFECTED-001", "EFMIS129")
        self.driver.llm = lambda prompt, call: "AFFECTED"
        self.assertEqual(self.contract.assess_lot("CPSC-AFFECTED-001"), "AFFECTED")
        with self.assertRaises(UserError):
            self.contract.authorize_dispatch_for_notice("CPSC-AFFECTED-001")

    def test_missing_reference_fails_closed_without_model_call(self):
        self.enroll("CPSC-UNKNOWN-003", "EFMIS129")
        self.driver.pages[NOTICE_URL] = NOTICE_TEXT.replace("25-395", "25-999")
        self.driver.llm = lambda prompt, call: "OUT_OF_SCOPE"
        self.assertEqual(self.contract.assess_lot("CPSC-UNKNOWN-003"), "UNVERIFIABLE")
        self.assertEqual(self.driver.calls, 0)

    def test_unavailable_official_notice_fails_closed(self):
        self.enroll("CPSC-NOSOURCE-004", "EFMIS129-B")
        self.driver.pages.pop(NOTICE_URL)
        self.assertEqual(self.contract.assess_lot("CPSC-NOSOURCE-004"), "UNVERIFIABLE")
        with self.assertRaises(UserError):
            self.contract.authorize_dispatch_for_notice("CPSC-NOSOURCE-004")

if __name__ == "__main__":
    unittest.main()
