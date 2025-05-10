#! /usr/bin/env python3

from pathlib import Path
from fnmatch import fnmatch
from math import inf

# UTF-8 settings.
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Third party module.
from gitignore_parser import parse_gitignore as parse_ignorefile

# Custom modules.
from .scan import Scan
from .format import Format
from .output import Output

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self,
        path = None,
        output = None,
        output_prefix = None,
        output_suffix = None,
        recur = True,
        depth = inf,
        crawlectignore = None,
        gitignore = True,
        dockerignore = True,
        xenv = True,
        tree = True
    ):

        # Store the class arguments for __repr__.
        self.args = {}

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

        # Ignore files handling.
        self.crawlectignore = crawlectignore
        self.args["crawlectignore"] = self.crawlectignore
        self.gitignore = gitignore
        self.args["gitignore"] = self.gitignore
        self.dockerignore = dockerignore
        self.args["dockerignore"] = self.dockerignore

        self.simplePathToIgnore = []
        self.ignore_file_list = []

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denied by default.
        self.writeRight = "x"

        self.validateParam()

        self.warmUp()

        self.initServices()

        self.processIgnoreFiles()

        self.generatePathList()


    # To be enhanced. State patern for interactive/module mode?
    def validateParam(self):
        """Validate attributes and regenerate dynamic attributes."""

        # Max depth adaptation if recur is False.
        if not self.recur:
            self.depth = 1

        # Interactive mode.
        if __name__ == "__main__":
            while self.path is None:
                self.path = input(
                    f"\n# Missing argument #\n"
                    f"{type(self).__name__} require a path to crawl.\n"
                    f"Please enter the desired path (e.g.: '.').\n"
                    f"Or [Ctrl]+[C] then [Enter] to abort.\n"
                )

            while not Path(self.path).exists():
                self.path = input(
                    f"\n# Path error #\n"
                    f"{type(self).__name__} could not find {repr(self.path)},\n"
                    f"please enter the path to crawl.\n"
                    f"Or [Ctrl]+[C] then [Enter] to abort.\n"
                )

            while self.output is None and self.output_prefix is None:
                print(
                    f"\n# Missing argument #\n"
                    f"{type(self).__name__} require an output file-name for static output file-name\n"
                    f"(e.g.: './description.md')\n"
                    f"OR\n"
                    f"an output prefix and output suffix for unique output file-name\n"
                    f"(e.g.: './descript' as prefix, and '.md' as suffix),\n"
                    f"this will create a path similar to: './descript-202506041010-g5ef9h.md'."
                )

                while True:
                    _ = input(
                        "Please choose between 'static' and 'unique'.\n"
                        "Or [Ctrl]+[C] then [Enter] to abort.\n"
                    ).lower()

                    if _ == "static":
                        while self.output is None or not self.output:
                            self.output = input(
                            "Please enter a static output file-name, e.g.: './output.md'.\n"
                            "Or [Ctrl]+[C] then [Enter] to abort.\n"
                            )

                        break

                    elif _ == "unique":
                        while self.output_prefix is None or not self.output_prefix:
                            self.output_prefix = input(
                                "Please enter a prefix, e.g.: './output'.\n"
                                "Or [Ctrl]+[C] then [Enter] to abort.\n"
                            )

                        while self.output_suffix is None:
                            self.output_suffix = input(
                                "Please enter a suffix, e.g.: '.md' (suffix can be empty).\n"
                                "Or [Ctrl]+[C] then [Enter] to abort.\n"
                            )

                        break

                    else:
                        continue

            if self.output is not None:
                if Path(self.output).exists():
                        print(
                            f"\n# File overwrite #\n{type(self).__name__} is about to\n"
                            f"overwrite {repr(self.output)}. Its content will be lost!"
                        )

                        while True:
                            _ = input(
                                "Please choose between 'proceed' and 'change'.\n"
                                "Or [Ctrl]+[C] then [Enter] to abort.\n"
                            ).lower()

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

            # File overwrite denied in module mode.
            self.writeRight = "x"

            if self.output is not None:
                if Path(self.output).exists():
                    raise IOError(
                        f"\n# Permission error #\n"
                        f"{type(self).__name__} do not allow file {repr(self.output)} to be overwrited in module mode. "
                        "Please errase the file first if you want to keep this output path."
                    )

            validationMessage = ""
            if self.path is None:
                validationMessage += "- A path to crawl, e.g.: path = '.'\n"

            elif not Path(self.path).exists():
                validationMessage += f"A valid path to crawl, {self.path} cannot be found.\n"

            if self.output is None and self.output_prefix is None:
                validationMessage += "- An output file-name for static output file-name (e.g.: --output = './description.md')\n"
                "OR\n"
                "an output prefix and output suffix for unique output file-name "
                "(e.g.: --output_prefix = './descript', --output_suffix = '.md' as suffix),\n"
                "this will create a path similar to: './descript-202506041010-g5ef9h.md'\n"

            if validationMessage:
                raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires:\n{validationMessage}Got: {self}")


    def warmUp(self):
        """Set needed variable for Crawlect service init phase"""
        try:
            self.pathObj = Path(self.path)

        except:
            print(f"Error: on {type(self).__name__}:\ncould not set its paths from path attribute.")
            raise

        try:
            self.title = self.pathObj.resolve().name

        except:
            print(f"Error: on {type(self).__name__}:\ncould not set its title.")
            raise


    def initServices(self):
        """Build Crawlect services"""
        try:
            self.scanService = Scan(self)

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Scan service.")
            raise

        try:
            self.formatService = Format(self) # Format does not take Crawlect instance as parameter.

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Format service.")
            raise

        try:
            self.outputService = Output(self)

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Output service.")
            raise


    def processIgnoreFiles(self):
        """Check for ignore files settings and fetch ignore list from these."""

        if self.crawlectignore is not None and Path(self.crawlectignore).exists():
            # Ignore the ignore file itselfe.
            self.simplePathToIgnore.append(Path(self.crawlectignore))
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.crawlectignore)))

        if self.gitignore and Path(self.path + "/.gitignore").exists():
            # Ignore the ignore file itselfe and .git folder as it seems logic in this case.
            self.simplePathToIgnore.append(Path(self.path + "/.gitignore"))
            self.simplePathToIgnore.append(Path(self.path + "/.git"))
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.gitignore")))

        if self.dockerignore and Path(self.path + "/.dockerignore").exists():
            # Ignore the ignore file itselfe.
            self.simplePathToIgnore.append(Path(self.path + "/.dockerignore"))
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.dockerignore")))

        # Avoid duplicates.
        self.simplePathToIgnore = list(set(self.simplePathToIgnore))


    def generatePathList(self):
        """Prepare the path list which will be treated and written in output file."""
        try:
            self.files = self.scanService.listPathIn()

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and proceed to paths listing.")
            raise


    def getTitle(self):
        """Simply returns path to crawl's name"""
        return self.title


    # Assess if this should be sent to a common class ("Filter" class ?).
    def isPathIgnored(self, path):
        """Check if path match any .gitignore pattern or path include/exclude list parameter item."""

        for ignored in self.simplePathToIgnore:
            if fnmatch(path, ignored):
                return True

        for ignoreFile in self.ignore_file_list:
            if ignoreFile(path):
                return True

        return False


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"


####################
# INTERACTIVE MODE #
####################

if __name__ == "__main__":

    import argparse
    import traceback

    class BooleanAction(argparse.Action):
        """
        This method converts argpars argument string to a boolean (e.g.: "yes" => True).
        From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
        """

        choices = ["yes", "no", "y", "n", "true", "false", "1", "0"]

        def __call__(self, parser, namespace, values, option_string = None):
            if values.lower() in ("yes", "y", "true", "t", "1"):
                setattr(namespace, self.dest, True)
            elif values.lower() in ("no", "n", "false", "f", "0"):
                setattr(namespace, self.dest, False)
            else:
                raise argparse.ArgumentTypeError(f"Unsupported boolean value: {values}")

    try:
        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Filtering rules allow you to forcibly include or exclude certain directories, files names or file extensions. "
            "All files will be listed if there are no rules. "
            "Inclusion overrules exclusion on same caracteristics and file-name rules takes precedence against extension rules."
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
            default = "description",
            help = "Output markdown digest file prefix ('description' by default) "
            "associated with --output_suffix can be use as an alternative to '--output' argument to generate a unique file-name "
            "(e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-os", "--output_suffix", "--output_file_suffix",
            type = str,
            default = ".md",
            
            help = "Output markdown digest file prefix ('.md' by default) "
            "associated with --output_prefix can be use as an alternative to '--output' argument to generate a unique file-name "
            "(e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-r", "--recur", "--recursive_crawling",
            type = str,
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Enable recursive crawling (default is True).")

        parser.add_argument(
            "-d", "--depth", "--recursive_crawling_depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite).")

        # Ignore files handling.
        parser.add_argument(
            "-crawlig", "--crawlectignore", "--crawlectignore_use",
            type = str,
            default = None,
            help = "Crawlect exclusion rules file path (default is None).")

        parser.add_argument(
            "-gitig", "--gitignore", "--gitignore_use",
            type = str,
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Use .gitignore exclusion rules if exist (default is True).")

        parser.add_argument(
            "-dokig", "--dockerignore", "--dockerignore_use",
            type = str,
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Use .dockerignore exclusion rules if exist (default is True).")

        # Advanced features parameters.
        parser.add_argument(
            "-xen", "--xenv", "--sanitize_env_variables",
            type = str,
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Sanitize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(**vars(args))

        # Launch output file composition
        crawlect.outputService.compose()

        # Confirm.
        print(
            f"\n{type(crawlect.outputService).__name__} processed {repr(crawlect.getTitle())} "
            f"and stored description in {repr(crawlect.outputService.currentOutputName)}."
        )

    except KeyboardInterrupt:
        print("Interrupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)