"""
Frequency analysis functions.
"""

from collections import Counter


def character_frequency(text: str) -> dict[str, int]:
    """
    Count character frequency.

    Case-insensitive.
    """

    counter = Counter()

    for char in text.lower():
        counter[char] += 1

    return sort_frequency(counter)


def word_frequency(text: str) -> dict[str, int]:
    """
    Count word frequency.

    Case-insensitive.
    """

    counter = Counter()

    words = text.lower().split()

    for word in words:
        counter[word] += 1

    return sort_frequency(counter)


def sort_frequency(freq: dict[str, int]) -> dict[str, int]:
    """
    Sort a frequency dictionary in descending order.
    """

    return dict(
        sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )