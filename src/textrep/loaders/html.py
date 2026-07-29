"""
HTML file extraction.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


class _HTMLTextExtractor(HTMLParser):
    """
    Minimal HTML-to-text parser based on the standard library.
    """

    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag in {"script", "style"}:
            self._skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip_depth and data.strip():
            self._parts.append(data.strip())

    def text(self) -> str:
        """
        Return extracted text.
        """

        return " ".join(self._parts)


def extract_text(path: Path) -> str:
    """
    Extract visible text from an HTML file.
    """

    parser = _HTMLTextExtractor()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.text()
