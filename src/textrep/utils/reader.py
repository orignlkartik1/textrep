"""
Functions for reading text files.
"""

from pathlib import Path


SUPPORTED_EXTENSIONS = {".txt"}


def validate_file(path: str | Path) -> Path:
    """
    Validate that the file exists and has
    a supported extension.

    Returns:
        pathlib.Path
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.")

    if not path.is_file():
        raise ValueError(f"{path} is not a file.")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return path


def read_file(path: str | Path) -> str:
    """
    Read a text file.

    Returns:
        File contents as a string.
    """

    path = validate_file(path)

    with path.open(
            mode="r",
            encoding="utf-8",
    ) as file:
        return file.read()