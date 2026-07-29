"""
Frequency analysis functions.
"""

from textrep.analysis.frequency import (
    character_frequency as _character_frequency,
    sort_frequency as _sort_frequency,
    word_frequency as _word_frequency,
)


def character_frequency(text: str) -> dict[str, int]:
    """
    Count character frequency.

    Case-insensitive.
    """

    return _character_frequency(text)


def word_frequency(text: str) -> dict[str, int]:
    """
    Count word frequency.

    Case-insensitive.
    """

    return _word_frequency(text)


def sort_frequency(freq: dict[str, int]) -> dict[str, int]:
    """
    Sort a frequency dictionary in descending order.
    """

    return _sort_frequency(freq)
