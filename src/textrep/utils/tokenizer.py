"""
Tokenization utilities.
"""

import re

from textrep.analysis.tokenize import letters, words


WORD_PATTERN = re.compile(r"\b[\w']+\b")


def tokenize_words(text: str) -> list[str]:
    """
    Split text into lowercase words.

    Example

    Hello, World!

    becomes

    ["hello", "world"]
    """

    return words(text)


def tokenize_letters(text: str) -> list[str]:
    """
    Return only alphabetic characters.

    Example

    Hello123!

    becomes

    ['h','e','l','l','o']
    """

    return letters(text)
