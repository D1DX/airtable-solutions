#!/usr/bin/env python3
"""CI hard-fail guard for secret literals and unsafe generated drift."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


DISALLOWED_TRACKED = {
    "deploy/ntfy.conf",
    ".mcp.json",
    ".claude/settings.json",
}

SECRET_PATTERNS = [
    ("Airtable PAT", re.compile(r"\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{16,}\b")),
    ("AWS Access Key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub Token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
    ("OpenAI Key", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    ("Static WAHA API key", re.compile(r"\bWAHA_API_KEY\s*=\s*[\"'][^\"'$]{16,}[\"']")),
    (
        "Static API key/token assignment",
        re.compile(r"\b(API_KEY|TOKEN|SECRET|PASSWORD|PAT)\s*=\s*[\"'][A-Za-z0-9._-]{16,}[\"']"),
    ),
    ("Static ntfy password", re.compile(r"\bNTFY_PASS\s*=\s*\"[^\"$]{8,}\"")),
]

ALLOW_PATH_PARTS = (
    ".template",
    "security-patterns.sh",
)

ALLOW_LINE_MARKERS = (
    "op://",
    "[REDACTED]",
    "REDACTED",
    "example",
    "placeholder",
    "YOUR_",
    "your-",
    "YOUR-",
    "Bearer $",
    "X-Api-Key: ...",
)


def run_git_ls_files(repo: Path) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    repo = Path.cwd()
    tracked = run_git_ls_files(repo)
    failures: list[str] = []

    # Unsafe generated/runtime artifacts tracked in git.
    for path in tracked:
        if path in DISALLOWED_TRACKED and (repo / path).exists():
            failures.append(f"[generated-drift] tracked runtime file: {path}")

    # Secret literal scan.
    for rel in tracked:
        if any(part in rel for part in ALLOW_PATH_PARTS):
            continue
        full = repo / rel
        if not full.is_file():
            continue
        try:
            text = full.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            if any(marker in line for marker in ALLOW_LINE_MARKERS):
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    failures.append(f"[secret] {label}: {rel}:{lineno}")

    if failures:
        print("CI guard failed:")
        for item in failures:
            print(f" - {item}")
        return 1

    print("CI guard passed: no secret literals or unsafe generated drift.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
