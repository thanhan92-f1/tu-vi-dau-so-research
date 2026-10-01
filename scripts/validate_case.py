#!/usr/bin/env python3
"""Validate a Tử Vi research case JSON file."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:  # pragma: no cover
    Draft202012Validator = None
    FormatChecker = None


def validate_case(case_path: Path, schema_path: Path) -> list[str]:
    try:
        data = json.loads(case_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Không đọc được JSON: {exc}"]
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Không đọc được schema: {exc}"]

    if Draft202012Validator is None:
        errors = []
        for key in ("project_version", "profile", "core", "palaces"):
            if key not in data:
                errors.append(f"Thiếu trường bắt buộc: {key}")
        if not isinstance(data.get("palaces"), list) or len(data.get("palaces", [])) != 12:
            errors.append("palaces phải có đúng 12 phần tử")
        return errors

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    result = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        path = ".".join(str(x) for x in error.absolute_path) or "<root>"
        result.append(f"{path}: {error.message}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", help="Tệp JSON cần kiểm tra")
    parser.add_argument("--schema", default=None, help="Đường dẫn JSON Schema")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    root = script_dir.parent
    schema = Path(args.schema).resolve() if args.schema else root / "assets" / "schemas" / "case.schema.json"
    case = Path(args.case).expanduser().resolve()
    errors = validate_case(case, schema)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} lỗi")
        return 1
    print(f"OK: {case.name} hợp lệ")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
