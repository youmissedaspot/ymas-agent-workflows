"""Synthetic identity/finding failures, not actual integration evidence."""

from pathlib import Path
import tempfile
import unittest

from check_receipt import package_inventory, validate_receipt


def ready():
    source = {"commit": "a" * 40, "tree": "b" * 40}
    return {"state": "ready", "source": source,
            "tested": {"source": source, "artifact": "test-log"},
            "reviewed": {"source": source, "artifact": "review-report"},
            "authorization": {"status": "granted", "source": source,
                              "action": "integrate", "evidence": "owner-instruction"},
            "findings": [], "checks": [{"command": "check", "outcome": "passed", "artifact": "log"}]}


class ReceiptTest(unittest.TestCase):
    def test_ready_and_integrated(self):
        receipt = ready()
        self.assertEqual(validate_receipt(receipt, receipt["source"]), [])
        receipt["state"] = "integrated"
        receipt["integration"] = {"candidate": receipt["source"], "commit": "c" * 40,
                                  "tree": "b" * 40, "artifact": "integration-log"}
        self.assertEqual(validate_receipt(receipt, receipt["source"],
                                         {"commit": "c" * 40, "tree": "b" * 40}), [])

    def test_incomplete_blocked_superseded_denied_stale_sources(self):
        for state in ("draft", "blocked", "superseded", "invented"):
            receipt = ready()
            receipt["state"] = state
            with self.subTest(state=state):
                self.assertTrue(validate_receipt(receipt))
        for role in ("tested", "reviewed", "authorization"):
            receipt = ready()
            receipt[role] = {**receipt[role], "source": {"commit": "d" * 40, "tree": "b" * 40}}
            with self.subTest(role=role):
                self.assertTrue(validate_receipt(receipt))
        receipt = ready()
        receipt["authorization"]["status"] = "denied"
        self.assertTrue(validate_receipt(receipt))
        self.assertTrue(validate_receipt(ready(), {"commit": "d" * 40, "tree": "b" * 40}))

    def test_open_blocking_findings_and_failed_checks(self):
        receipt = ready()
        receipt["findings"] = [{"id": "F1", "blocking": True, "status": "deferred", "evidence": "report"}]
        self.assertTrue(validate_receipt(receipt))
        receipt["findings"][0]["status"] = "resolved"
        self.assertEqual(validate_receipt(receipt), [])
        receipt["checks"][0]["outcome"] = "failed"
        self.assertTrue(validate_receipt(receipt))

    def test_integration_tree_drift(self):
        receipt = ready()
        receipt["state"] = "integrated"
        receipt["integration"] = {"candidate": receipt["source"], "commit": "c" * 40,
                                  "tree": "d" * 40, "artifact": "log"}
        self.assertTrue(validate_receipt(receipt))

    def test_inventory_exact_bytes_order_and_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one").write_bytes(b"a\r\n")
            (root / "two").write_bytes(b"b\n")
            first = package_inventory(root, ["one", "two"])
            self.assertEqual(first, package_inventory(root, ["two", "one"]))
            (root / "one").write_bytes(b"a\n")
            self.assertNotEqual(first["digest"], package_inventory(root, ["one", "two"])["digest"])
            with self.assertRaises(ValueError):
                package_inventory(root, ["../outside"])


if __name__ == "__main__":
    unittest.main()
