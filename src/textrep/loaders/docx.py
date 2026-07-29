"""
DOCX file extraction.
"""

from __future__ import annotations

from pathlib import Path

from textrep.exceptions import MissingDependencyError


def extract_text(path: Path) -> str:
    """
    Extract text from a DOCX file using python-docx when installed.
    """

    try:
        from docx import Document as DocxDocument
    except ImportError as exc:
        raise MissingDependencyError(
            "DOCX loading requires the optional dependency 'python-docx'. "
            "Install it with 'pip install textrep[docx]' or install "
            "'python-docx' directly."
        ) from exc

    document = DocxDocument(path)
    return "\n".join(paragraph.text for paragraph in document.paragraphs)
