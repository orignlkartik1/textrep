from pathlib import Path

from textrep.utils.reader import (
    read_file,
)


def test_read_file(tmp_path: Path):

    file = tmp_path / "sample.txt"

    file.write_text("Hello World")

    assert read_file(file) == "Hello World"