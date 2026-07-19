"""
Functions related to character statistics.
"""


def count_characters(text: str) -> int:
    """
    Count every character.
    """

    return len(text)


def count_letters(text: str) -> int:
    """
    Count alphabetic characters only.
    """

    return sum(char.isalpha() for char in text)


def count_digits(text: str) -> int:
    """
    Count numeric digits.
    """

    return sum(char.isdigit() for char in text)


def count_spaces(text: str) -> int:
    """
    Count whitespace characters.
    """

    return sum(char.isspace() for char in text)


def count_symbols(text: str) -> int:
    """
    Count punctuation/symbols.
    """

    return sum(
        not char.isalnum() and not char.isspace()
        for char in text
    )