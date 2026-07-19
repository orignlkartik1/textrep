from pathlib import Path

from textrep.analyzer import TextAnalyzer


def test_analyze(tmp_path: Path):

    file = tmp_path / "sample.txt"

    file.write_text("Hello World Hello")

    analyzer = TextAnalyzer(file)

    report = analyzer.analyze()

    assert report.word_count == 3
    assert report.character_count == 17
    assert report.letter_count == 15