"""
Loader registry for file extension detection.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from textrep.exceptions import UnsupportedFileTypeError

from . import docx, html, markdown, pdf, text


Loader = Callable[[Path], str]

_LOADERS: dict[str, Loader] = {
    ".txt": text.extract_text,
    ".md": markdown.extract_text,
    ".markdown": markdown.extract_text,
    ".html": html.extract_text,
    ".htm": html.extract_text,
    ".pdf": pdf.extract_text,
    ".docx": docx.extract_text,
}


def get_loader(extension: str) -> Loader:
    """
    Return the loader registered for a file extension.
    """

    normalized = extension.lower()

    try:
        return _LOADERS[normalized]
    except KeyError as exc:
        raise UnsupportedFileTypeError(
            f"Unsupported file type: {extension}"
        ) from exc


def supported_extensions() -> tuple[str, ...]:
    """
    Return supported file extensions.
    """

    return tuple(sorted(_LOADERS))
