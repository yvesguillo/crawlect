# Custom modules.
from .crawlect import Crawlect

# Standard modules.
from pathlib import Path
import argparse
import traceback
from math import inf

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


# To be enhanced. State patern for interactive/module mode?
def validateCrawlectParams(args):
    """Validate attributes and regenerate dynamic attributes."""

    # Add writeRight attribute to be passed to Crawlect upon file overwrite request prompt.
    if not hasattr(args, 'writeRight'):
        args.writeRight = "x"

    # Max depth adaptation if recur is False.
    if not args.recur:
        args.depth = 1

    while args.path is None:
        args.path = input(
            "\n# Missing argument #\n"
            "Crawlect require a path to crawl.\n"
            "Please enter the desired path (e.g.: '.').\n"
            "Or [Ctrl]+[C] then [Enter] to abort.\n"
        )

    while not Path(args.path).exists():
        args.path = input(
            "\n# Path error #\n"
            f"Crawlect could not find {repr(args.path)},\n"
            "please enter the path to crawl.\n"
            "Or [Ctrl]+[C] then [Enter] to abort.\n"
        )

    while args.output is None and args.output_prefix is None:
        print(
            "\n# Missing argument #\n"
            "Crawlect require an output file-name for static output file-name\n"
            "(e.g.: './description.md')\n"
            "OR\n"
            "an output prefix and output suffix for unique output file-name\n"
            "(e.g.: './descript' as prefix, and '.md' as suffix),\n"
            "this will create a path similar to: './descript-202506041010-g5ef9h.md'."
        )

        while True:
            _ = input(
                "Please choose between 'static' and 'unique'.\n"
                "Or [Ctrl]+[C] then [Enter] to abort.\n"
            ).lower()

            if _ == "static":
                while args.output is None or not args.output:
                    args.output = input(
                    "Please enter a static output file-name, e.g.: './output.md'.\n"
                    "Or [Ctrl]+[C] then [Enter] to abort.\n"
                    )

                break

            elif _ == "unique":
                while args.output_prefix is None or not args.output_prefix:
                    args.output_prefix = input(
                        "Please enter a prefix, e.g.: './output'.\n"
                        "Or [Ctrl]+[C] then [Enter] to abort.\n"
                    )

                while args.output_suffix is None:
                    args.output_suffix = input(
                        "Please enter a suffix, e.g.: '.md' (suffix can be empty).\n"
                        "Or [Ctrl]+[C] then [Enter] to abort.\n"
                    )

                break

            else:
                continue

    if args.output is not None:
        if Path(args.output).exists():
                print(
                    "\n# File overwrite #\nCrawlect is about to\n"
                    f"overwrite {repr(args.output)}. Its content will be lost!"
                )

                while True:
                    _ = input(
                        "Please choose between 'proceed' and 'change'.\n"
                        "Or [Ctrl]+[C] then [Enter] to abort.\n"
                    ).lower()

                    if _ == "proceed":
                        # File overwrite permission granted upon request in CLI mode.
                        args.writeRight = "w"
                        break

                    elif _ == "change":
                        args.output = None
                        args.output_prefix = None
                        validateCrawlectParams(args)
                        break

                    else:
                        continue

    return args


def main():
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
            choices = BooleanAction.choices,
            action = BooleanAction,
            default = True,
            help = "Use .crawlectignore exclusion rules if exist (default is True).")

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

        args = validateCrawlectParams(args)

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