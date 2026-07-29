"""
Structured result types for TextRep.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class TextStats:
    """
    Core quantitative statistics for a text document.
    """

    word_count: int
    character_count: int
    letter_count: int
    digit_count: int
    space_count: int
    symbol_count: int
    unique_word_count: int
    average_word_length: float


@dataclass(slots=True)
class ReadabilityStats:
    """
    Basic readability and reading effort metrics.
    """

    sentence_count: int
    average_sentence_length: float
    reading_time_minutes: float


@dataclass(slots=True)
class DocumentMetadata:
    """
    Metadata describing where a document came from.
    """

    source: str | None = None
    file_name: str | None = None
    extension: str | None = None


@dataclass(slots=True)
class AnalysisResult:
    """
    Combined text analysis result.
    """

    stats: TextStats
    readability: ReadabilityStats
    character_frequency: dict[str, int] = field(default_factory=dict)
    word_frequency: dict[str, int] = field(default_factory=dict)
    metadata: DocumentMetadata = field(default_factory=DocumentMetadata)
