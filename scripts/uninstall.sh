#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="tu-vi-dau-so-research"
SCOPE="personal"
PROJECT=""
TARGET=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope) SCOPE="${2:-}"; shift 2 ;;
    --project) PROJECT="${2:-}"; shift 2 ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [[ -n "$TARGET" ]]; then
  DEST="${TARGET}/${SKILL_NAME}"
elif [[ "$SCOPE" == "personal" ]]; then
  DEST="${HOME}/.claude/skills/${SKILL_NAME}"
elif [[ "$SCOPE" == "project" && -n "$PROJECT" ]]; then
  DEST="${PROJECT}/.claude/skills/${SKILL_NAME}"
else
  echo "Invalid arguments" >&2
  exit 2
fi

if [[ -d "$DEST" ]]; then
  rm -rf "$DEST"
  echo "Removed: $DEST"
else
  echo "Not installed: $DEST"
fi
