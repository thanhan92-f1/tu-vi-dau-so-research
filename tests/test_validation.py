from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


skill_validator = load_module("validate_skill", ROOT / "scripts" / "validate_skill.py")
case_validator = load_module("validate_case", ROOT / "scripts" / "validate_case.py")


class SkillValidationTests(unittest.TestCase):
    def test_skill_is_valid(self):
        errors, _warnings = skill_validator.validate(ROOT)
        self.assertEqual(errors, [])

    def test_valid_case(self):
        errors = case_validator.validate_case(
            ROOT / "tests" / "fixtures" / "valid-case.json",
            ROOT / "assets" / "schemas" / "case.schema.json",
        )
        self.assertEqual(errors, [])

    def test_invalid_case(self):
        errors = case_validator.validate_case(
            ROOT / "tests" / "fixtures" / "invalid-case.json",
            ROOT / "assets" / "schemas" / "case.schema.json",
        )
        self.assertTrue(errors)

    def test_exactly_twelve_palaces_in_example(self):
        data = json.loads((ROOT / "examples" / "sample-case.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["palaces"]), 12)


if __name__ == "__main__":
    unittest.main()
