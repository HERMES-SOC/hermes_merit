from pathlib import Path
from hermes_merit.io.file_tools import read_file


def test_read_file():
    assert read_file(Path("test_file.cdf")) is None
