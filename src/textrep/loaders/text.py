"""
Plain text file extraction.
"""

from __future__ import annotations

from pathlib import Path


def extract_text(path: Path) -> str:
    """
    Read a plain text file as UTF-8.
    """

    return path.read_text(encoding="utf-8")
