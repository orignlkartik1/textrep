"""
Public file loading API.
"""

from __future__ import annotations

from pathlib import Path

from textrep.document import Document
from textrep.loaders import get_loader
from textrep.types import DocumentMetadata


def load(path: str | Path) -> Document:
    """
    Load a supported document file and return a Document.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    if not file_path.is_file():
        raise ValueError(f"{file_path} is not a file.")

    loader = get_loader(file_path.suffix)
    text = loader(file_path)

    return Document(
        text,
        metadata=DocumentMetadata(
            source=str(file_path),
            file_name=file_path.name,
            extension=file_path.suffix.lower(),
        ),
    )
