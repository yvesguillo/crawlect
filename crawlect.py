#! /usr/bin/env python3
"""Crawlect is a module intended to describe files from a given path and transcribe these into a single markdown file."""

import argparse
from pathlib import Path
from math import inf

# Custom modules.
from format import Format
from scan import listFilesIn

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
    """Crawl a given path to list and describe all files on a single markdown file."""

    # From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
    with open("languages.json","rt") as file:
        _languages = file.read()

    def __init__(self, path = ".", output = "description.md", recur = True, depth = inf, excl_ext_li = [], excl_dir_li = [], excl_fil_li = [], excl_ext_wr = [], excl_dir_wr = [], excl_fil_wr = [], incl_ext_li = [], incl_dir_li = [], incl_fil_li = [], incl_ext_wr = [], incl_dir_wr = [], incl_fil_wr = [], xenv = True, tree = True):
        self.path = path
        self.paths = Path(path)
        self.output = output
        self.recur = recur
        self.depth = depth

        # Files and extentions inclusion/exclusions parameters.
        self.excl_ext_li = excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.excl_fil_li = excl_fil_li
        self.excl_ext_wr = excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.excl_fil_wr = excl_fil_wr
        self.incl_ext_li = incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.incl_fil_li = incl_fil_li
        self.incl_ext_wr = incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.incl_fil_wr = incl_fil_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.tree = tree

        # Build path list and attributes.
        self.refresh()

    def refresh(self):
        """Regenerate the files list, name, output etc., based on current parameters."""
        self.title = self.paths.name
        self.files = listFilesIn(paths = self.paths, recur = self.recur, depth = self.depth, excl_ext_li = self.excl_ext_li, excl_dir_li = self.excl_dir_li, excl_fil_li = self.excl_fil_li, incl_ext_li = self.incl_ext_li, incl_dir_li = self.incl_dir_li, incl_fil_li = self.incl_fil_li)

if __name__ == "__main__":
    try:

        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Inclusions parameters overrule exclusions parameters. Example usage: TBD"
        )

        parser.add_argument(
            "-p", "--path", "--path_to_crawl",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder \".\").")

        parser.add_argument(
            "-o", "--output", "--output_file",
            type = str,
            default = "description.md",
            help = "Output markdown digest file (default is description.md).")

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
            default = [],
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_extentions_from_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_extentions_from_listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include in listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_from_listing",
            nargs = "*",
            default = [],
            help = "List of directories to include in listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_from_listing",
            nargs = "*",
            default = [],
            help = "List of files to include in listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_extentions_from_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_from_writing",
            nargs = "*",
            default = [],
            help = "List of directories to include for writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_from_writing",
            nargs = "*",
            default = [],
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

        toto = Crawlect(path = args.path, output = args.output, recur = args.recur, depth = args.depth, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_li = args.excl_fil_li, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, excl_fil_wr = args.excl_fil_wr, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_li = args.incl_fil_li, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, incl_fil_wr = args.incl_fil_wr, xenv = args.xenv, tree = args.tree)

        a = Format().makeTreeMd(Path(args.path), [".git"],2)
        print(a)
        #Format().markdownGen(a)


        #     print(f"# {file.name}\n")
        #     instance = Format().insertCodebox(file)
        #     print(instance)

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error)} error:\n{error.args}")