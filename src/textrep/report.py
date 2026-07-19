from .models import AnalysisReport


def print_report(report: AnalysisReport) -> None:
    """
    Prints the report to the console.
    """

    print("=" * 45)
    print("               TEXTREP")
    print("=" * 45)

    print(f"File        : {report.file_name}")
    print(f"Words       : {report.word_count}")
    print(f"Characters  : {report.character_count}")
    print(f"Letters     : {report.letter_count}")

    print("\nCharacter Frequency")
    print("-" * 45)

    for char, count in report.character_frequency.items():
        if char.isalpha():
            print(f"{char:<5} {count}")

    print("=" * 45)