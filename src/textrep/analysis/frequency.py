"""
Frequency analysis functions.
"""

from __future__ import annotations

from collections import Counter

from . import tokenize


def sort_frequency(freq: dict[str, int]) -> dict[str, int]:
    """
    Sort a frequency mapping by descending count.
    """

    return dict(
        sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )


def character_frequency(text: str) -> dict[str, int]:
    """
    Count character frequency case-insensitively.
    """

    return sort_frequency(dict(Counter(text.lower())))


def word_frequency(text: str) -> dict[str, int]:
    """
    Count word frequency case-insensitively.
    """

    return sort_frequency(dict(Counter(tokenize.words(text))))


def top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    """
    Return the n most common words.
    """

    return Counter(tokenize.words(text)).most_common(n)
