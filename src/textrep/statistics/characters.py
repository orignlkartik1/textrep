"""
Functions related to character statistics.
"""

from textrep.analysis.statistics import (
    character_count,
    digit_count,
    letter_count,
    space_count,
    symbol_count,
)


def count_characters(text: str) -> int:
    """
    Count every character.
    """

    return character_count(text)


def count_letters(text: str) -> int:
    """
    Count alphabetic characters only.
    """

    return letter_count(text)


def count_digits(text: str) -> int:
    """
    Count numeric digits.
    """

    return digit_count(text)


def count_spaces(text: str) -> int:
    """
    Count whitespace characters.
    """

    return space_count(text)


def count_symbols(text: str) -> int:
    """
    Count punctuation/symbols.
    """

    return symbol_count(text)
