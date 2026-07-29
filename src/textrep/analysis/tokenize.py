"""
Tokenization helpers used by TextRep analysis functions.
"""

from __future__ import annotations

import re


WORD_PATTERN = re.compile(r"\b[\w']+\b")
SENTENCE_PATTERN = re.compile(r"[^.!?]+[.!?]?")


def words(text: str) -> list[str]:
    """
    Return lowercase word tokens.
    """

    return WORD_PATTERN.findall(text.lower())


def letters(text: str) -> list[str]:
    """
    Return lowercase alphabetic characters.
    """

    return [char.lower() for char in text if char.isalpha()]


def sentences(text: str) -> list[str]:
    """
    Return non-empty sentence-like spans.
    """

    return [
        sentence.strip()
        for sentence in SENTENCE_PATTERN.findall(text)
        if sentence.strip()
    ]
