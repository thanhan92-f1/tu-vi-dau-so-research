#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="tu-vi-dau-so-research"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCOPE="personal"
PROJECT=""
TARGET=""

usage() {
  cat <<'EOF'
Usage:
  bash scripts/install.sh --scope personal
  bash scripts/install.sh --scope project --project /path/to/project
  bash scripts/install.sh --target /custom/skills/directory
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope) SCOPE="${2:-}"; shift 2 ;;
    --project) PROJECT="${2:-}"; shift 2 ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ -n "$TARGET" ]]; then
  DEST_BASE="$TARGET"
elif [[ "$SCOPE" == "personal" ]]; then
  DEST_BASE="${HOME}/.claude/skills"
elif [[ "$SCOPE" == "project" ]]; then
  if [[ -z "$PROJECT" ]]; then
    echo "--project is required for project scope" >&2
    exit 2
  fi
  DEST_BASE="${PROJECT}/.claude/skills"
else
  echo "Invalid scope: $SCOPE" >&2
  exit 2
fi

DEST="${DEST_BASE}/${SKILL_NAME}"
mkdir -p "$DEST_BASE"
rm -rf "$DEST"
mkdir -p "$DEST"

for item in SKILL.md references assets scripts LICENSE; do
  cp -R "$ROOT/$item" "$DEST/"
done

python3 "$DEST/scripts/validate_skill.py" "$DEST"
echo "Installed to: $DEST"
