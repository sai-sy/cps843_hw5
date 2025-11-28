#!/usr/bin/env python3
"""Replace characters in report.md according to a configurable mapping."""

from __future__ import annotations

from pathlib import Path

# Update this dictionary with the replacements you need.
# Each key will be replaced globally by its corresponding value.
REPLACEMENTS: dict[str, str] = {
    # superscript
    "ᵀ": "^{T}",
    "∞":"_{\infty{}}",
    "²":"^{2}",
    # subscript
    # regular
    "×":"\\times{}",
    "−":"-",
    "∈":"\in{}",
    "ℝ": "\mathbb{R}",
    "≠": "\\neq{}",
    "ℓ":"\ell{}",
    "⊤": "T", 
    "≈": "\\approx{}"
    # "–": "-",
    # "—": "-",
}

REPORT_PATH = Path("report.md")


def apply_replacements(text: str, replacements: dict[str, str]) -> str:
    """Apply all replacements to the provided text."""
    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result


def main() -> None:
    if not REPORT_PATH.exists():
        raise FileNotFoundError(f"Could not find {REPORT_PATH.resolve()}")

    content = REPORT_PATH.read_text(encoding="utf-8")
    updated = apply_replacements(content, REPLACEMENTS)

    if updated != content:
        REPORT_PATH.write_text(updated, encoding="utf-8")
        print(f"Updated {REPORT_PATH} with {len(REPLACEMENTS)} replacements.")
    else:
        print("No changes made; replacements produced identical content.")


if __name__ == "__main__":
    main()
