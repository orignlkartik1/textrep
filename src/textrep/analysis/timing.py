"""
Reading time estimates.
"""

from __future__ import annotations

from .statistics import word_count


def reading_time(text: str, words_per_minute: int = 200) -> float:
    """
    Estimate reading time in minutes.
    """

    if words_per_minute <= 0:
        raise ValueError("words_per_minute must be greater than zero.")

    return round(word_count(text) / words_per_minute, 2)
