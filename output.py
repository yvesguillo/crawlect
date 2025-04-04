#! /usr/bin/env python3
"""outpu.py contains Crawlect output utilities."""

from pathlib import Path

try:

    path = Path(".")

    with path.open("test.md") as file:
        file.write(f"## {path.name}")
        file.write(f"{path}")
        file.write("last line so far.")

except KeyboardInterrupt:
    print("Interupted by user.")

except Exception as error:
    print(f"\nUnexpected {type(error)} error:\n{error.args}")