"""
Statistical functions for TextRep.
"""

from .words import (
    count_words,
    unique_words,
)

from .characters import (
    count_characters,
    count_letters,
)

from .frequency import (
    character_frequency,
    word_frequency,
    sort_frequency,
)

__all__ = [
    "count_words",
    "unique_words",
    "count_characters",
    "count_letters",
    "character_frequency",
    "word_frequency",
    "sort_frequency",
]