"""
Core text statistics.
"""

from __future__ import annotations

from textrep.types import TextStats

from . import tokenize


def word_count(text: str) -> int:
    """
    Count word tokens in text.
    """

    return len(tokenize.words(text))


def character_count(text: str) -> int:
    """
    Count every character in text.
    """

    return len(text)


def letter_count(text: str) -> int:
    """
    Count alphabetic characters in text.
    """

    return len(tokenize.letters(text))


def digit_count(text: str) -> int:
    """
    Count numeric digits in text.
    """

    return sum(char.isdigit() for char in text)


def space_count(text: str) -> int:
    """
    Count whitespace characters in text.
    """

    return sum(char.isspace() for char in text)


def symbol_count(text: str) -> int:
    """
    Count punctuation and symbols in text.
    """

    return sum(
        not char.isalnum() and not char.isspace()
        for char in text
    )


def unique_word_count(text: str) -> int:
    """
    Count unique words case-insensitively.
    """

    return len(set(tokenize.words(text)))


def average_word_length(text: str) -> float:
    """
    Calculate average word-token length.
    """

    words = tokenize.words(text)

    if not words:
        return 0.0

    return round(sum(len(word) for word in words) / len(words), 2)


def longest_word(text: str) -> str:
    """
    Return the longest word token.
    """

    words = tokenize.words(text)

    if not words:
        return ""

    return max(words, key=len)


def shortest_word(text: str) -> str:
    """
    Return the shortest word token.
    """

    words = tokenize.words(text)

    if not words:
        return ""

    return min(words, key=len)


def stats(text: str) -> TextStats:
    """
    Return core statistics for text.
    """

    return TextStats(
        word_count=word_count(text),
        character_count=character_count(text),
        letter_count=letter_count(text),
        digit_count=digit_count(text),
        space_count=space_count(text),
        symbol_count=symbol_count(text),
        unique_word_count=unique_word_count(text),
        average_word_length=average_word_length(text),
    )
