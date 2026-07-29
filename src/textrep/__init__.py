"""
TextRep

A lightweight Python library for text analysis.
"""

from .analysis import (
    average_word_length,
    character_count,
    character_frequency,
    digit_count,
    letter_count,
    longest_word,
    readability,
    reading_time,
    sentence_count,
    shortest_word,
    space_count,
    stats,
    symbol_count,
    top_words,
    unique_word_count,
    word_count,
    word_frequency,
)
from .analyzer import TextAnalyzer
from .document import Document
from .exceptions import (
    MissingDependencyError,
    TextRepError,
    UnsupportedFileTypeError,
)
from .io import load
from .types import (
    AnalysisResult,
    DocumentMetadata,
    ReadabilityStats,
    TextStats,
)


def analyze(text: str) -> AnalysisResult:
    """
    Analyze raw text and return a complete analysis result.
    """

    return Document(text).analyze()

__version__ = "1.2.0"

__all__ = [
    "AnalysisResult",
    "Document",
    "DocumentMetadata",
    "MissingDependencyError",
    "ReadabilityStats",
    "TextAnalyzer",
    "TextRepError",
    "TextStats",
    "UnsupportedFileTypeError",
    "analyze",
    "average_word_length",
    "character_count",
    "character_frequency",
    "digit_count",
    "letter_count",
    "load",
    "longest_word",
    "readability",
    "reading_time",
    "sentence_count",
    "shortest_word",
    "space_count",
    "stats",
    "symbol_count",
    "top_words",
    "unique_word_count",
    "word_count",
    "word_frequency",
]
