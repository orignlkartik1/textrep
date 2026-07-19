"""
Functions related to word statistics.
"""

from collections import Counter


def count_words(text: str) -> int:
    """
    Count the total number of words.
    """

    return len(text.split())


def unique_words(text: str) -> int:
    """
    Count unique words (case-insensitive).
    """

    words = text.lower().split()

    return len(set(words))


def average_word_length(text: str) -> float:
    """
    Calculate average word length.
    """

    words = text.split()

    if not words:
        return 0.0

    total = sum(len(word) for word in words)

    return round(total / len(words), 2)


def longest_word(text: str) -> str:
    """
    Return the longest word.
    """

    words = text.split()

    if not words:
        return ""

    return max(words, key=len)


def shortest_word(text: str) -> str:
    """
    Return the shortest word.
    """

    words = text.split()

    if not words:
        return ""

    return min(words, key=len)


def top_words(text: str, n: int = 10):
    """
    Return the n most common words.
    """

    words = text.lower().split()

    counter = Counter(words)

    return counter.most_common(n)