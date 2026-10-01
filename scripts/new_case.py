#!/usr/bin/env python3
"""Create a blank 12-palace research case JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PALACES = [
    "Mệnh", "Phụ Mẫu", "Phúc Đức", "Điền Trạch", "Quan Lộc", "Nô Bộc",
    "Thiên Di", "Tật Ách", "Tài Bạch", "Tử Tức", "Phu Thê", "Huynh Đệ"
]


def make_case(case_id: str) -> dict:
    return {
        "project_version": "1.0.0",
        "profile": {
            "case_id": case_id,
            "name_alias": "",
            "sex_for_chart": "",
            "birth": {
                "calendar_type": "solar",
                "date": "2000-01-01",
                "lunar_leap_month": False,
                "clock_time": "00:00",
                "time_branch": "",
                "place": "",
                "timezone": "Asia/Ho_Chi_Minh",
                "source_of_time": "unknown",
                "estimated_error_minutes": 0
            },
            "input_confidence": "D",
            "chart_source": "",
            "school": ""
        },
        "core": {
            "life_element": "",
            "bureau": "",
            "life_bureau_relation": "",
            "yin_yang_direction": "",
            "life_palace_branch": "",
            "body_palace": ""
        },
        "palaces": [
            {
                "name": name,
                "branch": "",
                "stem": "",
                "major_stars": [],
                "supporting_stars": [],
                "challenging_stars": [],
                "transformations": [],
                "tuan_triet": [],
                "growth_cycle": "",
                "decade_range": "",
                "source_notes": []
            } for name in PALACES
        ],
        "analysis": {"topic": "", "mode": "INGEST", "conclusions": []},
        "validation": {"predictions_locked_at": "", "real_events_revealed_at": "", "events": []}
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-id", required=True, help="Ví dụ TV-1990-001")
    parser.add_argument("--output", required=True, help="Tệp JSON đầu ra")
    parser.add_argument("--force", action="store_true", help="Cho phép ghi đè")
    args = parser.parse_args()

    if not args.case_id.startswith("TV-"):
        parser.error("case-id phải bắt đầu bằng TV-")
    output = Path(args.output).expanduser().resolve()
    if output.exists() and not args.force:
        parser.error(f"Tệp đã tồn tại: {output}. Dùng --force để ghi đè.")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(make_case(args.case_id), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã tạo {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
