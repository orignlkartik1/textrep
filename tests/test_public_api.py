from pathlib import Path

import pytest

import textrep as tr
from textrep.exceptions import UnsupportedFileTypeError


def test_functional_api_analyzes_raw_text():
    text = "Hello world. Hello TextRep."

    assert tr.word_count(text) == 4
    assert tr.character_count(text) == len(text)
    assert tr.reading_time(text) == 0.02

    result = tr.analyze(text)

    assert result.stats.word_count == 4
    assert result.readability.sentence_count == 2
    assert result.word_frequency["hello"] == 2


def test_document_api_delegates_to_functional_api():
    doc = tr.Document("Hello world")

    assert doc.word_count() == tr.word_count(doc.text)
    assert doc.character_count() == tr.character_count(doc.text)
    assert doc.stats().word_count == 2
    assert doc.analyze().stats.character_count == 11


def test_load_returns_document_for_text_file(tmp_path: Path):
    path = tmp_path / "article.txt"
    path.write_text("Hello from a file.", encoding="utf-8")

    doc = tr.load(path)

    assert isinstance(doc, tr.Document)
    assert doc.text == "Hello from a file."
    assert doc.metadata.file_name == "article.txt"
    assert doc.word_count() == 4


def test_load_returns_document_for_markdown_file(tmp_path: Path):
    path = tmp_path / "README.md"
    path.write_text("# Title\n\nHello markdown.", encoding="utf-8")

    doc = tr.load(path)

    assert doc.metadata.extension == ".md"
    assert "Hello markdown." in doc.text


def test_load_returns_document_for_html_file(tmp_path: Path):
    path = tmp_path / "page.html"
    path.write_text(
        "<html><body><h1>Hello</h1><script>ignored()</script></body></html>",
        encoding="utf-8",
    )

    doc = tr.load(path)

    assert doc.text == "Hello"


def test_load_rejects_unknown_extension(tmp_path: Path):
    path = tmp_path / "data.xyz"
    path.write_text("Hello", encoding="utf-8")

    with pytest.raises(UnsupportedFileTypeError):
        tr.load(path)
