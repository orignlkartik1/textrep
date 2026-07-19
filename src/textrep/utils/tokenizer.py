"""
Tokenization utilities.
"""

import re


WORD_PATTERN = re.compile(r"\b[\w']+\b")


def tokenize_words(text: str) -> list[str]:
    """
    Split text into lowercase words.

    Example

    Hello, World!

    becomes

    ["hello", "world"]
    """

    return WORD_PATTERN.findall(text.lower())


def tokenize_letters(text: str) -> list[str]:
    """
    Return only alphabetic characters.

    Example

    Hello123!

    becomes

    ['h','e','l','l','o']
    """

    return [
        char.lower()
        for char in text
        if char.isalpha()
    ]