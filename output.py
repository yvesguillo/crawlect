#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string
import hashlib

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

        # Early version.
        with open(self.currentOutputName, self.crawler.writeRight) as outputFile:

            # Title
            outputFile.write(f"# {self.crawler.getTitle()}\n{str(date.year)}.{str("{:02d}".format(date.month))}.{str("{:02d}".format(date.day))} {str("{:02d}".format(date.hour))}:{str("{:02d}".format(date.minute))}\n\nGenerated with {type(self.crawler).__name__}.\n\n")

            # Directory tree
            if self.crawler.tree:
                exclude = self.crawler.excl_dir_li
                exclude.append(self.currentOutputName)
                outputFile.write(f"## File structure\n\nDirectory tree.\n\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer = exclude, deep = self.crawler.depth)}\n\n")

            # Files list

            # sort file
            sorted_files = self.crawler.files
            sorted_files.sort(key = lambda p: (p.parent, p.name))

            outputFile.write("## Files:\n\n")
            for file in sorted_files:

                chemin_id = hashlib.md5(str(file.resolve()).encode()).hexdigest()

                if file.is_file() and str(file) != self.currentOutputName:
                    outputFile.write(f"<h3 id=\"{chemin_id}\">{file.name}</h3>  \n")
                    outputFile.write(f"`{file}`\n\n")
                    if self.isFileToInclude(file):
                        try:
                            content = self.crawler.formatService.insertCodebox(file)
                            if not content is None:
                                outputFile.write(self.crawler.formatService.insertCodebox(file))

                        except Exception as error:
                            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not create codebox from {repr(file)}: {error}")
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

        return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_wr == [] and self.crawler.excl_fil_wr == [] and self.crawler.incl_ext_wr == [] and self.crawler.incl_fil_wr == []:
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_wr:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_wr and path.name not in self.crawler.excl_fil_wr:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_wr and path.name not in self.crawler.incl_fil_wr:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_wr:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_wr != [] or self.crawler.incl_fil_wr != []:
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"