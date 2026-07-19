from textrep.statistics.characters import (
    count_characters,
    count_letters,
    count_digits,
    count_spaces,
    count_symbols,
)


def test_count_characters():
    assert count_characters("abc") == 3


def test_count_letters():
    assert count_letters("abc123") == 3


def test_count_digits():
    assert count_digits("abc123") == 3


def test_count_spaces():
    assert count_spaces("a b c") == 2


def test_count_symbols():
    assert count_symbols("abc!!!") == 3