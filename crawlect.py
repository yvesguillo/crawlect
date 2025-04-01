#! /usr/bin/env python3
"""Crawlect is a module intended to describe files from a given path and transcribe these into a single markdown file."""

import argparse
from pathlib import Path

class Crawlect:
    """Crawl a given path to list and describe all files on a single markdown file."""

    # From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
    with open("languages.json","rt") as file:
        _languages = file.read()

    def __init__(self, path = ".", dest = "description.md", igno = []):
        self.path = path
        self.paths = Path(path)
        self.dest = dest
        self.files = self.listFilesIn(paths = self.paths,recur=True)
        self.title = self.paths.name
        self.digest = ""

    def listFilesIn(self, paths = None, files = [], recur = False):
        """Append all files in specified path as strings in a list and return it."""
        if paths is None:
            paths = self.paths
        for path in paths.iterdir():
            if path.is_file():
                files.append(path)
            elif path.is_dir() and recur is True:
                self.listFilesIn(paths = path, files = files, recur = recur)
        return files




if __name__ == "__main__":
    try:

        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Inclusions parameters overrule exclusions parameters. Example usage: TBD"
        )

        parser.add_argument(
            "-p", "--path", "--path-to-crawl",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder \".\")")

        parser.add_argument(
            "-d", "--digest", "--digest-output-file",
            type = str,
            default = "description.md",
            help = "Output markdown digest file.")

        parser.add_argument(
            "-r", "--recur", "--recursive-crawling",
            action = "store_true",
            help = "Enable recursive crawling.")

        parser.add_argument(
            "-xel", "--excl-ext-li", "--excluded-extentions-from-listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from listing (e.g., .jpg .png).")

        parser.add_argument(
            "-xdl", "--excl-dir-li", "--excluded-directories-from-listing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from listing (e.g., bin render).")

        parser.add_argument(
            "-xfl", "--excl-fil-li", "--excluded-files-from-listing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from listing (e.g., README.md .png).")

        parser.add_argument(
            "-xew", "--excl-ext-wr", "--excluded-extentions-from-writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from writing (e.g., .jpg .png).")

        parser.add_argument(
            "-xdw", "--excl-dir-wr", "--excluded-directories-from-writing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from writing (e.g., bin render).")

        parser.add_argument(
            "-xfw", "--excl-fil-wr", "--excluded-files-from-writing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from writing (e.g., README.md .png).")

        parser.add_argument(
            "-iel", "--incl-ext-li", "--include-extentions-from-listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include in listing (e.g., .jpg .png).")

        parser.add_argument(
            "-idl", "--incl-dir-li", "--include-directories-from-listing",
            nargs = "*",
            default = [],
            help = "List of directories to include in listing (e.g., bin render).")

        parser.add_argument(
            "-ifl", "--incl-fil-li", "--include-files-from-listing",
            nargs = "*",
            default = [],
            help = "List of files to include in listing (e.g., README.md .png).")

        parser.add_argument(
            "-iew", "--incl-ext-wr", "--include-extentions-from-writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for writing (e.g., .jpg .png).")

        parser.add_argument(
            "-idw", "--incl-dir-wr", "--include-directories-from-writing",
            nargs = "*",
            default = [],
            help = "List of directories to include for writing (e.g., bin render).")

        parser.add_argument(
            "-ifw", "--incl-fil-wr", "--include-files-from-writing",
            nargs = "*",
            default = [],
            help = "List of files to include for writing (e.g., README.md .png).")

        args = parser.parse_args()

        # from inspect import getmembers
        # from pprint import pprint
        # pprint(getmembers(args))
    
        crawlect = Crawlect(args.path)
        

        for path in crawlect.files:
            print(path)

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error)} error:\n{error.args}")