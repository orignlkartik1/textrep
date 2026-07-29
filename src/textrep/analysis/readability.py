"""
Basic readability metrics.
"""

from __future__ import annotations

from textrep.types import ReadabilityStats

from . import tokenize
from .statistics import word_count
from .timing import reading_time


def sentence_count(text: str) -> int:
    """
    Count sentence-like spans in text.
    """

    return len(tokenize.sentences(text))


def readability(text: str) -> ReadabilityStats:
    """
    Return basic readability metrics.
    """

    sentences = sentence_count(text)
    words = word_count(text)
    average_sentence_length = 0.0

    if sentences:
        average_sentence_length = round(words / sentences, 2)

    return ReadabilityStats(
        sentence_count=sentences,
        average_sentence_length=average_sentence_length,
        reading_time_minutes=reading_time(text),
    )
