"""Run: python3 -m unittest discover -s tests -p 'test_aiq_context_router.py'"""
import importlib.util
import pathlib
import tempfile
import unittest

MODULE = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "aiq_context_router.py"
spec = importlib.util.spec_from_file_location("aiq_context_router", MODULE)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)

class RouterTests(unittest.TestCase):
    def make_repo(self, parent, name, files):
        root = pathlib.Path(parent) / name
        root.mkdir()
        for filename in files:
            path = root / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("safe fixture", encoding="utf-8")
        return root

    def test_hairplan_routes_ui(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, "HairPlanPro", router.ROUTES["hairplan"]["entry"])
            result = router.route(root, "hairplan", "ui")
            self.assertEqual(result["suggested_skill"], "aiq-web-product-quality")
            self.assertEqual(result["status"], "ROUTED_NOT_EXECUTED")

    def test_missing_mandatory_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, "HairPlanPro", ("CLAUDE.md",))
            with self.assertRaises(ValueError):
                router.route(root, "hairplan", "ui")

    def test_wrong_repo_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, "not-hairplan", router.ROUTES["hairplan"]["entry"])
            with self.assertRaises(ValueError):
                router.route(root, "hairplan", "ui")

    def test_lead_radar_missing_entry_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, "lead-radar", ())
            with self.assertRaises(ValueError):
                router.route(root, "lead-radar", "booking")

    def test_sensitive_task_requires_go(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, "MrAI-Private-Brain", router.ROUTES["mrai"]["entry"])
            result = router.route(root, "mrai", "backup")
            self.assertEqual(result["risk_gate"], "OWNER_GO_REQUIRED")

    def test_unknown_product_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                router.route(tmp, "unknown", "ui")

if __name__ == "__main__":
    unittest.main()
