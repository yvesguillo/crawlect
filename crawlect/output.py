#! /usr/bin/env python3

# Standard modules.
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

        self.current_output_name = ""


    def compose(self):
        """Generates and writes the output file."""

        content = self.generate_content()
        self.write(content)


    def generate_content(self):
        """Generates the full markdown content as a string."""

        date = datetime.now()
        output_lines = []

        # Header
        output_lines.append(
            f"# {self.crawler.get_title()}\n"
            f"{date.strftime('%Y.%m.%d %H:%M')}\n\n"
            "Generated with ['Crawlect'](https://pypi.org/project/Crawlect/).\n"
        )

        # Tree
        if self.crawler.tree:
            tree = self.crawler.format_service.makeTreeMd(crawler = self.crawler)
            output_lines.append(f"## File structure\n\n{tree}")

        # Files
        sorted_files = sorted(self.crawler.files, key = lambda p: (p.parent, p.name))
        output_lines.append("## Files:\n")

        for file in sorted_files:
            if file.is_file():
                output_lines.append(f"### {file.name.replace('.', '&period;')}  ")
                output_lines.append(f"[`{file.as_posix()}`]({file.as_posix()})")

                try:
                    content = self.crawler.format_service.insert_codebox(file)
                    if content:
                        output_lines.append("")
                        output_lines.append(content)
                        output_lines.append("")
                except Exception as error:
                    print(
                        f"\n!! - {type(error).__name__}:\n"
                        f"{type(self).__name__} could not create codebox from {repr(file)}: {error}"
                    )

        return "\n".join(output_lines)


    def write(self, content):
        """Write provided content to output file."""

        self.current_output_name = self.standard_output_name()

        # Exclude the output file from scan (post-generation)
        self.crawler.simple_path_to_ignore.append(self.current_output_name)

        with open(self.current_output_name, self.crawler.write_right, encoding = "utf-8") as outputFile:
            outputFile.write(content)


    def standard_output_name(self):
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