"""
Markdown file extraction.
"""

from __future__ import annotations

from pathlib import Path


def extract_text(path: Path) -> str:
    """
    Read Markdown as plain source text.

    Markdown is text already; richer rendering-aware extraction can be added
    later without changing the public load() API.
    """

    return path.read_text(encoding="utf-8")
