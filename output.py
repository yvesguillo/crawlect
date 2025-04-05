#! /usr/bin/env python3
"""outpu.py contains Crawlect output utilities."""

from pathlib import Path
from datetime import datetime

class Output:
    """Output class provide standard Crawlec output features."""
    def __init__(self, name = None, prefix = "output", suffix = ".md"):
        self.name = name
        self.prefix = prefix
        self.suffix = suffix

    def standardOutputName(cls):
        """Return standard output file name if no filename specified."""
        if cls.name is None:
            now = datetime.now()
            return cls.prefix + "-" + yearmodahs() + cls.suffix
        else:
            return cls.name

    def appendComposition(cls, path = None, *composition):
        """Append composition to output file."""
        if path == None:
            path = Path(cls.standardOutputName())
        elif isinstance(path, Path) is False:
            path = Path(path)
        for element in composition:
            pass


def yearmodahs(date = datetime.now()):
    """Return givent date as yearmoda plus hours and seconds string."""
    return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

try:

    print(yearmodahs())

    output = Output()
    print(output.standardOutputName())

    path = Path("test.md")
    print(isinstance(path, Path))

    # with path.open("a") as file:
    #     file.write(f"## {path.name}\n")
    #     file.write(f"{path}\n")
    #     file.write("last line so far.\n")

    # print(path.exists())

except KeyboardInterrupt:
    print("Interupted by user.")

except Exception as error:
    print(f"\nUnexpected {type(error)} error:\n{error.args}")