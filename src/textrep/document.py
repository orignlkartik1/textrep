"""
Document object API.
"""

from __future__ import annotations

from dataclasses import asdict

from textrep.analysis import (
    average_word_length,
    character_count,
    character_frequency,
    digit_count,
    letter_count,
    longest_word,
    readability,
    reading_time,
    shortest_word,
    space_count,
    stats,
    symbol_count,
    unique_word_count,
    word_count,
    word_frequency,
)
from textrep.types import AnalysisResult, DocumentMetadata, ReadabilityStats, TextStats


class Document:
    """
    A text document with convenience analysis methods.

    The document stores plain text. Analysis logic lives in the functional API;
    methods on this class delegate to those functions.
    """

    def __init__(
        self,
        text: str,
        metadata: DocumentMetadata | None = None,
    ) -> None:
        self.text = text
        self.metadata = metadata or DocumentMetadata()

    def word_count(self) -> int:
        """
        Count word tokens in the document.
        """

        return word_count(self.text)

    def character_count(self) -> int:
        """
        Count every character in the document.
        """

        return character_count(self.text)

    def letter_count(self) -> int:
        """
        Count alphabetic characters in the document.
        """

        return letter_count(self.text)

    def digit_count(self) -> int:
        """
        Count numeric digits in the document.
        """

        return digit_count(self.text)

    def space_count(self) -> int:
        """
        Count whitespace characters in the document.
        """

        return space_count(self.text)

    def symbol_count(self) -> int:
        """
        Count punctuation and symbols in the document.
        """

        return symbol_count(self.text)

    def unique_word_count(self) -> int:
        """
        Count unique words in the document.
        """

        return unique_word_count(self.text)

    def average_word_length(self) -> float:
        """
        Calculate average word length in the document.
        """

        return average_word_length(self.text)

    def longest_word(self) -> str:
        """
        Return the longest word in the document.
        """

        return longest_word(self.text)

    def shortest_word(self) -> str:
        """
        Return the shortest word in the document.
        """

        return shortest_word(self.text)

    def character_frequency(self) -> dict[str, int]:
        """
        Count character frequency in the document.
        """

        return character_frequency(self.text)

    def word_frequency(self) -> dict[str, int]:
        """
        Count word frequency in the document.
        """

        return word_frequency(self.text)

    def reading_time(self, words_per_minute: int = 200) -> float:
        """
        Estimate reading time in minutes.
        """

        return reading_time(self.text, words_per_minute=words_per_minute)

    def readability(self) -> ReadabilityStats:
        """
        Return readability metrics for the document.
        """

        return readability(self.text)

    def stats(self) -> TextStats:
        """
        Return core document statistics.
        """

        return stats(self.text)

    def analyze(self) -> AnalysisResult:
        """
        Return a complete analysis result for the document.
        """

        return AnalysisResult(
            stats=self.stats(),
            readability=self.readability(),
            character_frequency=self.character_frequency(),
            word_frequency=self.word_frequency(),
            metadata=self.metadata,
        )

    def to_dict(self) -> dict[str, object]:
        """
        Return document analysis as plain Python dictionaries.
        """

        return asdict(self.analyze())
