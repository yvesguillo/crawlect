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
        self.args = {}

        self.crawler = crawler
        self.args["crawler"] = self.crawler

        self.currentOutputName = ""
        self.composition = ()


    def compose(self):
        """Compose output file."""

        date = datetime.now()
        self.currentOutputName = self.standardOutputName()
        # Add to Crawlect simple path exclusion list.
        self.crawler.simplePathToIgnore.append(self.currentOutputName)

        # Early version.
        with open(self.currentOutputName, self.crawler.writeRight, encoding = "utf-8") as outputFile:

            # Title
            outputFile.write(
                f"# {self.crawler.getTitle()}\n"
                f"{str(date.year)}.{str("{:02d}".format(date.month))}.{str("{:02d}".format(date.day))} "
                f"{str("{:02d}".format(date.hour))}:{str("{:02d}".format(date.minute))}\n\n"
                f"Generated with {type(self.crawler).__name__}.\n\n"
            )

            # Directory tree
            if self.crawler.tree:
                tree = self.crawler.formatService.makeTreeMd(crawler = self.crawler)
                outputFile.write(f"## File structure\n\n{tree}\n\n")

            # Files list

            # sort file
            sorted_files = self.crawler.files
            sorted_files.sort(key = lambda p: (p.parent, p.name))

            outputFile.write("## Files:\n\n")

            for file in sorted_files:
                if file.is_file():
                    outputFile.write(f"### {file.name.replace(".", "&period;")}  \n")
                    outputFile.write(f"[`{file}`]({file})\n\n")

                    try:
                        content = self.crawler.formatService.insertCodebox(file)
                        if not content is None:
                            outputFile.write(self.crawler.formatService.insertCodebox(file))

                    except Exception as error:
                            print(
                                f"\n!! - {type(error).__name__}:\n"
                                f"{type(self).__name__} could not create codebox from {repr(file)}: {error}"
                            )

                    outputFile.write("\n")


    def standardOutputName(self):
        """Return standard output file name if no filename specified."""

        if self.crawler.output is None:
            now = datetime.now()
            return f"{self.crawler.output_prefix}-{self.yearmodahs()}-{"".join(choices(self.__rand_filename_char_list, k = 6))}{self.crawler.output_suffix}"
        else:
            return self.crawler.output


    def yearmodahs(self, date = datetime.now()):
        """Return givent date as yearmoda plus hours and seconds string."""

        return (
            str(date.year)
            + str("{:02d}".format(date.month))
            + str("{:02d}".format(date.day))
            + str("{:02d}".format(date.hour))
            + str("{:02d}".format(date.minute))
            + str("{:02d}".format(date.second))
        )


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"