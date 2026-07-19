from pathlib import Path

from .models import AnalysisReport
from .statistics.words import count_words
from .statistics.characters import (
    count_characters,
    count_letters,
)
from .statistics.frequency import character_frequency
from .utils.reader import read_file


class TextAnalyzer:
    """
    Main analysis class.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def analyze(self) -> AnalysisReport:

        text = read_file(self.file_path)

        return AnalysisReport(
            file_name=self.file_path.name,
            word_count=count_words(text),
            character_count=count_characters(text),
            letter_count=count_letters(text),
            character_frequency=character_frequency(text),
        )