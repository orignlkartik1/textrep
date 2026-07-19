from dataclasses import dataclass
from typing import Dict


@dataclass(slots=True)
class AnalysisReport:
    """
    Stores the analysis results.
    """

    file_name: str

    word_count: int

    character_count: int

    letter_count: int

    character_frequency: Dict[str, int]