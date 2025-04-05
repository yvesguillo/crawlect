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
        if cls.name is None:
            now = datetime.now()
            return cls.prefix + "-" + str(now.year) + str("{:02d}".format(now.month)) + str("{:02d}".format(now.day)) + str("{:02d}".format(now.hour)) + str("{:02d}".format(now.minute)) + str("{:02d}".format(now.second)) + cls.suffix
        else:
            return cls.name

    @classmethod
    def compose(cls, path = None, composition = []):
        """Append composition to output file."""
        if path == None:
            path = cls.standardOutputName()
        pass

try:

    output = Output()
    print(output.standardOutputName())

    # path = Path("test.md")
    # print(path.exists())

    # with path.open("a") as file:
    #     file.write(f"## {path.name}\n")
    #     file.write(f"{path}\n")
    #     file.write("last line so far.\n")

    # print(path.exists())

except KeyboardInterrupt:
    print("Interupted by user.")

except Exception as error:
    print(f"\nUnexpected {type(error)} error:\n{error.args}")