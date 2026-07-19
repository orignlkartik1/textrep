from textrep.statistics.frequency import (
    character_frequency,
    word_frequency,
)


def test_character_frequency():

    freq = character_frequency("Hello")

    assert freq["l"] == 2
    assert freq["h"] == 1


def test_word_frequency():

    freq = word_frequency("dog cat dog")

    assert freq["dog"] == 2
    assert freq["cat"] == 1