"""
PDF file extraction.
"""

from __future__ import annotations

from pathlib import Path

from textrep.exceptions import MissingDependencyError


def extract_text(path: Path) -> str:
    """
    Extract text from a PDF file using pypdf when installed.
    """

    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise MissingDependencyError(
            "PDF loading requires the optional dependency 'pypdf'. "
            "Install it with 'pip install textrep[pdf]' or install 'pypdf' "
            "directly."
        ) from exc

    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
