from pathlib import Path

from .io import load
from .models import AnalysisReport
from .document import Document


class TextAnalyzer(Document):
    """
    Backward-compatible file analyzer.

    TextAnalyzer keeps the v1.x behavior where the constructor accepts a file
    path. New code should prefer textrep.Document for raw text or textrep.load
    for files.
    """

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        document = load(self.file_path)
        super().__init__(document.text, metadata=document.metadata)

    def analyze(self) -> AnalysisReport:
        """
        Return the legacy AnalysisReport format.
        """

        return AnalysisReport(
            file_name=self.file_path.name,
            word_count=self.word_count(),
            character_count=self.character_count(),
            letter_count=self.letter_count(),
            character_frequency=self.character_frequency(),
        )
