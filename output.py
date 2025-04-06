#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string

class Output:
    """
    Output class provide standard Crawlec output features.
    It require and only accept one instance of Crawlect as argument.
    """

    __rand_filename_char_list = string.ascii_lowercase + string.digits

    def __init__(self, crawler):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = crawler

    def appendComposition(self):
        """Append composition to output file."""
        print(crawler.getTitle())
        pass

    def standardOutputName(self):
        """Return standard output file name if no filename specified."""

        if self.crawler.output is None:
            now = datetime.now()
            return f"{self.crawler.prefix}-{self.yearmodahs()}-{"".join(choices(self.__rand_filename_char_list, k = 6))}{self.crawler.suffix}"
        else:
            return self.crawler.output

    def yearmodahs(self, date = datetime.now()):
        """Return givent date as yearmoda plus hours and seconds string."""

        return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"