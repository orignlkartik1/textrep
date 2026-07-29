"""
Text analysis functions.
"""

from .frequency import character_frequency, top_words, word_frequency
from .readability import readability, sentence_count
from .statistics import (
    average_word_length,
    character_count,
    digit_count,
    letter_count,
    longest_word,
    shortest_word,
    space_count,
    stats,
    symbol_count,
    unique_word_count,
    word_count,
)
from .timing import reading_time

__all__ = [
    "average_word_length",
    "character_count",
    "character_frequency",
    "digit_count",
    "letter_count",
    "longest_word",
    "readability",
    "reading_time",
    "sentence_count",
    "shortest_word",
    "space_count",
    "stats",
    "symbol_count",
    "top_words",
    "unique_word_count",
    "word_count",
    "word_frequency",
]
