# textrep

A lightweight Python library for text analysis.

TextRep supports three API styles:

- Functional API for quick analysis of raw text
- Document API for reusable document objects
- File API for loading documents from disk

## Installation

```bash
pip install textrep
```

Or using uv:

```bash
uv pip install textrep
```

## Quick Start

```python
import textrep as tr

text = "Hello world. TextRep analyzes text."

print(tr.word_count(text))
print(tr.character_count(text))
print(tr.readability(text))
print(tr.analyze(text))
```

## Functional API

Use the functional API when you already have text and want direct results.

```python
import textrep as tr

text = "Hello world. Hello TextRep."

tr.word_count(text)
tr.character_count(text)
tr.letter_count(text)
tr.word_frequency(text)
tr.character_frequency(text)
tr.reading_time(text)
tr.stats(text)
tr.readability(text)
tr.analyze(text)
```

The functional API is the source of truth. Object methods delegate to these
functions instead of duplicating analysis logic.

## Document API

Use `Document` when you want to keep text and metadata together.

```python
import textrep as tr

doc = tr.Document("Hello world. TextRep analyzes text.")

doc.word_count()
doc.character_count()
doc.readability()
doc.reading_time()
doc.stats()
doc.analyze()
```

## File API

Use `load()` when you want TextRep to read a document from disk and return a
`Document`.

```python
import textrep as tr

doc = tr.load("article.txt")
doc.word_count()
doc.analyze()
```

Supported extensions:

- `.txt`
- `.md`
- `.markdown`
- `.html`
- `.htm`
- `.pdf`
- `.docx`

Plain text, Markdown, and HTML are supported with the Python standard library.
PDF and DOCX detection is built in, but extraction requires optional
dependencies:

- PDF: `pip install textrep[pdf]`
- DOCX: `pip install textrep[docx]`
- Everything: `pip install textrep[all]`

If an optional dependency is missing, TextRep raises
`textrep.MissingDependencyError` with an installation hint.

## Backward Compatibility

The legacy `TextAnalyzer` class still works:

```python
from textrep import TextAnalyzer

analyzer = TextAnalyzer("article.txt")
report = analyzer.analyze()

print(report.word_count)
```

For new code, prefer:

```python
import textrep as tr

doc = tr.load("article.txt")
result = doc.analyze()
```

## Result Objects

`tr.stats(text)` returns a `TextStats` dataclass.

`tr.readability(text)` returns a `ReadabilityStats` dataclass.

`tr.analyze(text)` and `doc.analyze()` return an `AnalysisResult` dataclass.

These objects provide typed attributes instead of loosely structured
dictionaries.

## Documentation

For more usage examples, see [docs/USAGE.md](./docs/USAGE.md).

## Contributing

We welcome contributions. Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
