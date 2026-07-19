import argparse
import sys

from .analyzer import TextAnalyzer
from .report import print_report


def main() -> None:
    """
    Entry point for the CLI.
    """

    parser = argparse.ArgumentParser(
        prog="textrep",
        description="Analyze plain text files.",
    )

    parser.add_argument(
        "file",
        help="Path to the text file",
    )

    args = parser.parse_args()

    try:
        analyzer = TextAnalyzer(args.file)

        report = analyzer.analyze()

        print_report(report)

    except FileNotFoundError:
        print(f"Error: '{args.file}' does not exist.")
        sys.exit(1)

    except Exception as exc:
        print(f"Unexpected error: {exc}")
        sys.exit(1)