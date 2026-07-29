"""
Functions related to word statistics.
"""

from textrep.analysis.frequency import top_words as _top_words
from textrep.analysis.statistics import (
    average_word_length as _average_word_length,
    longest_word as _longest_word,
    shortest_word as _shortest_word,
    unique_word_count,
    word_count,
)


def count_words(text: str) -> int:
    """
    Count the total number of words.
    """

    return word_count(text)


def unique_words(text: str) -> int:
    """
    Count unique words (case-insensitive).
    """

    return unique_word_count(text)


def average_word_length(text: str) -> float:
    """
    Calculate average word length.
    """

    return _average_word_length(text)


def longest_word(text: str) -> str:
    """
    Return the longest word.
    """

    return _longest_word(text)


def shortest_word(text: str) -> str:
    """
    Return the shortest word.
    """

    return _shortest_word(text)


def top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    """
    Return the n most common words.
    """

    return _top_words(text, n=n)
