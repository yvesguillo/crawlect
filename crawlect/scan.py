#! /usr/bin/env python3

from pathlib import Path

class Scan:
    """
    Scan class contains Crawlect directories tree scan utilities.
    It require and only accept one instance of Crawlect as argument.
    """

    def __init__(self, crawler = None):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = {}

        self.crawler = crawler
        self.args["crawler"] = self.crawler


    def listPathIn(self, path = None, depth = None, files = None):
        """Append all eligible paths from `crawler.path` as Path object in a list and return it."""

        if files is None:
            files = []

        if depth is None:
            depth = self.crawler.depth

        if path is None:
            path = self.crawler.pathObj

        for candidatePath in path.iterdir():
            try:
                if (
                    candidatePath.is_file()
                    and not self.crawler.isPathIgnored(candidatePath)
                ):
                    files.append(candidatePath)

                elif (
                    candidatePath.is_dir()
                    and self.crawler.recur
                    and depth >= 1
                    and not self.crawler.isPathIgnored(candidatePath)
                ):
                    files.append(candidatePath)
                    self.listPathIn(path = candidatePath, depth = depth-1, files = files)

            except PermissionError as error:
                print(f"\n!! - {type(error).__name__} :\n{type(self) .__name__} Could not list path due to permission {repr(candidatePath)}: {error} ")

            except Exception as error:
                print(f"\n!! - {type(error).__name__} :\n{type(self) .__name__} Could not list path due unexpected error {repr(candidatePath)}: {error} ")

        return files


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"