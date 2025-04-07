#! /usr/bin/env python3

import argparse
from pathlib import Path
from math import inf

# Debug.
import traceback

# Custom modules.
from format import Format
from scan import Scan
from output import Output

# From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
class BooleanAction(argparse.Action):
    """This method converts argpars argument string to a boolean (e.g.: "yes" => True)."""

    def __call__(self, parser, namespace, values, option_string = None):
        if values.lower() in ("yes", "y", "true", "t", "1"):
            setattr(namespace, self.dest, True)
        elif values.lower() in ("no", "n", "false", "f", "0"):
            setattr(namespace, self.dest, False)
        else:
            raise argparse.ArgumentTypeError(f"Unsupported boolean value: {values}")

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self, path = None, output = None, output_prefix = None, output_suffix = None, recur = True, depth = inf, excl_ext_li = (), excl_dir_li = (), excl_fil_li = (), excl_ext_wr = (), excl_dir_wr = (), excl_fil_wr = (), incl_ext_li = (), incl_dir_li = (), incl_fil_li = (), incl_ext_wr = (), incl_dir_wr = (), incl_fil_wr = (), xenv = True, tree = True):

        # Store the class arguments for __repr__.
        self.args = dict()

        self.path = path
        self.args["path"] = self.path
        self.output = output
        self.args["output"] = self.output
        self.output_prefix = output_prefix
        self.args["output_prefix"] = self.output_prefix
        self.output_suffix = output_suffix
        self.args["output_suffix"] = self.output_suffix
        self.recur = recur
        self.args["recur"] = self.recur
        self.depth = depth
        self.args["depth"] = self.depth

        # Files and extentions inclusion/exclusions parameters.
        self.excl_ext_li = excl_ext_li
        self.args["excl_ext_li"] = self.excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.args["excl_dir_li"] = self.excl_dir_li
        self.excl_fil_li = excl_fil_li
        self.args["excl_fil_li"] = self.excl_fil_li
        self.excl_ext_wr = excl_ext_wr
        self.args["excl_ext_wr"] = self.excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.args["excl_dir_wr"] = self.excl_dir_wr
        self.excl_fil_wr = excl_fil_wr
        self.args["excl_fil_wr"] = self.excl_fil_wr
        self.incl_ext_li = incl_ext_li
        self.args["incl_ext_li"] = self.incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.args["incl_dir_li"] = self.incl_dir_li
        self.incl_fil_li = incl_fil_li
        self.args["incl_fil_li"] = self.incl_fil_li
        self.incl_ext_wr = incl_ext_wr
        self.args["incl_ext_wr"] = self.incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.args["incl_dir_wr"] = self.incl_dir_wr
        self.incl_fil_wr = incl_fil_wr
        self.args["incl_fil_wr"] = self.incl_fil_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denided by default.
        self.writeRight = "x"

        # Validate attributes parameters.
        self.validate()

        # Build dynamic attributes.
        self.refresh()

    def validate(self):
        """Validate attributes and regenerate dynamic attributes."""

        # Interactive mode.
        if __name__ == "__main__":

            while self.path is None:
                self.path = input(f"\n# Missing argument #\n{type(self).__name__} require a path to crawl. Please enter the desired path (e.g.: '.') or [Ctrl]+[C] then [Enter] to abbort.\n")

            while not Path(self.path).exists():
                self.path = input(f"\n# Path error #\n{type(self).__name__} could not find {repr(self.path)}, please enter the path to crawl.\n")

            while self.output is None and self.output_prefix is None:
                print(f"\n# Missing argument #\n{type(self).__name__} require an output file-name for static output file-name (e.g.: './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: './descript' as prefix, and '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'")
                while True:
                    _ = input("Please choose between 'static' and 'unique', or [Ctrl]+[C] then [Enter] to abbort.\n").lower()
                    if _ == "static":
                        while self.output is None or not self.output:
                            self.output = input("Please enter a static output file-name, e.g.: './output.md' or [Ctrl]+[C] then [Enter] to abbort.\n")
                        break
                    elif _ == "unique":
                        while self.output_prefix is None or not self.output_prefix:
                            self.output_prefix = input("Please enter a prefix, e.g.: './output' or [Ctrl]+[C] then [Enter] to abbort.\n")
                        while self.output_suffix is None:
                            self.output_suffix = input("Please enter a suffix, e.g.: '.md' (suffix can be empty) or [Ctrl]+[C] then [Enter] to abbort.\n")
                        break
                    else:
                        continue

            if self.output is not None:
                if Path(self.output).exists():
                        print(f"\n# File overwrite #\n{type(self).__name__} is about to overwrite {repr(self.output)}. Its content will be lost!")
                        while True:
                            _ = input("Please choose between 'proceed' and 'change', or [Ctrl]+[C] then [Enter] to abbort.\n").lower()
                            if _ == "proceed":
                                # File overwrite permission granted upon request in CLI mode.
                                self.writeRight = "w"
                                break
                            elif _ == "change":
                                self.output = None
                                self.output_prefix = None
                                self.validate()
                                break
                            else:
                                continue

        # Module mode.
        else:

            # File overwrite denided in module mode.
            self.writeRight = "x"

            if self.output is not None:
                if Path(self.output).exists():
                    raise IOError(f"\n# Permission error #\n{type(self).__name__} do not allow file {repr(self.output)} to be overwrited in module mode. Please errase the file first if you want to keep this output path.")

            validationMessage = ""
            if self.path is None:
                validationMessage += "- A path to crawl, e.g.: path = '.'\n"
            elif not Path(self.path).exists():
                validationMessage += f"A valid path to crawl, {self.path} cannot be found.\n"
            if self.output is None and self.output_prefix is None:
                validationMessage += "- An output file-name for static output file-name (e.g.: --output = './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: --output_prefix = './descript', --output_suffix = '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'\n"
            if validationMessage:
                raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires:\n{validationMessage}Got: {self}")

    def refresh(self):
        """Regenerate dynamic attributes."""

        try:
            self.title = Path(self.path).resolve().name
        except:
            print(f"Error: on {self}:\ncould not refresh and set its title.")
            raise

        try:
            self.scan = Scan(self)
        except:
            print(f"Error: on {self}:\ncould not refresh and initiate its scan.")
            raise

        try:
            self.outputService = Output(self)
        except:
            print(f"Error: on {self}:\ncould not refresh and initiate its outputService.")
            raise

        try:
            self.files = self.scan.listFilesIn()
        except:
            print(f"Error: on {self}:\ncould not refresh and proceed to paths listing.")
            raise

    def getTitle(self):
        return self.title

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"

if __name__ == "__main__":
    try:

        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Filtering rules allow you to forcibly include or exclude certain directories, files names or file extensions. All files will be listed if there are no rules. Inclusion overrules exclusion on same caracteristics and file-name rules takes precedence against extension rules."
        )

        parser.add_argument(
            "-p", "--path", "--path_to_crawl",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder \".\").")

        parser.add_argument(
            "-o", "--output", "--output_file",
            type = str,
            default = None,
            help = "Output markdown digest file (default is None).")

        parser.add_argument(
            "-op", "--output_prefix", "--output_file_prefix",
            type = str,
            default = "crawlect_description",
            help = "Output markdown digest file prefix ('description' by default) asociated with --output_suffix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-os", "--output_suffix", "--output_file_suffix",
            type = str,
            default = ".md",
            
            help = "Output markdown digest file prefix ('.md' by default) asociated with --output_prefix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-r", "--recur", "--recursive_crawling",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Enable recursive crawling (default is True).")

        parser.add_argument(
            "-d", "--depth", "--recursive_crawling_depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite).")

        parser.add_argument(
            "-xel", "--excl_ext_li", "--excluded_extentions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_extentions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_extentions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include in listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to include in listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to include in listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_extentions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to include for writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to include for writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xen", "--xenv", "--randomize_env_variables",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Randomize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(path = args.path, output = args.output, output_prefix = args.output_prefix, output_suffix = args.output_suffix, recur = args.recur, depth = args.depth, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_li = args.excl_fil_li, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, excl_fil_wr = args.excl_fil_wr, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_li = args.incl_fil_li, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, incl_fil_wr = args.incl_fil_wr, xenv = args.xenv, tree = args.tree)

        # Launch output file composition
        crawlect.outputService.compose()

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)