from textrep.statistics.words import (
    count_words,
    unique_words,
    average_word_length,
    longest_word,
    shortest_word,
)


def test_count_words():
    assert count_words("Hello World") == 2


def test_unique_words():
    assert unique_words("hello Hello world") == 2


def test_average_word_length():
    assert average_word_length("hi hello") == 3.5


def test_longest_word():
    assert longest_word("cat elephant dog") == "elephant"


def test_shortest_word():
    assert shortest_word("cat elephant dog") == "cat"