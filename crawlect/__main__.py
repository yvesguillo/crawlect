#! /usr/bin/env python3

# Custom modules.
from . import __version__
from .crawlect import Crawlect
from .llm_code_analysis import LLM_Code_Analysis
from .cli import (
    validate_crawlect_params,
    validate_llm_params,
    validate_llm_requests,
    validate_llm_custom_requests,
    open_file
)

# Conditionnal Imports.
from .llm_api_loader import get_llm_api_class_map

# Standard modules.
import sys
from pathlib import Path
import traceback
from math import inf

def verbose(message):
    """Handle verbosity"""

    if VERBOSE:
        print("// " + message, flush = True)

def main():
    try:
        # Parameters.
        import argparse
        from argparse import ArgumentParser, BooleanOptionalAction

        def handle_custom_gui_kwargs(add_func, *args, **kwargs):
            gui_fields = ["guitype","guilabel", "guitooltip"]
            gui_metadata = {key: kwargs.pop(key, "") for key in gui_fields}

            action = add_func(*args, **kwargs)
            for key, value in gui_metadata.items():
                setattr(action, key, value)
            return action

        # Custom subclass for Add Arg for CLI schema tailored parameters.
        class CustomArgumentParser(argparse.ArgumentParser):
            def add_argument(self, *args, **kwargs):
                # Remove custom param so argparse won't choke.
                return handle_custom_gui_kwargs(super().add_argument, *args, **kwargs)

            # Uses custom Group Add Arg.
            def add_argument_group(self, *args, **kwargs):
                group = super().add_argument_group(*args, **kwargs)
                group.__class__ = CustomArgumentGroup  # Inject our custom logic
                return group

        # Custom subclass for Group Add Arg for CLI schema tailored parameters.
        class CustomArgumentGroup(argparse._ArgumentGroup):
            def add_argument(self, *args, **kwargs):
                # Remove custom param so argparse won't choke.
                return handle_custom_gui_kwargs(super().add_argument, *args, **kwargs)

        parser = CustomArgumentParser(
            description = f"Crawlect CLI v{__version__} - Crawl, collect and document your codebase in Markdown.",
            epilog = "For more information, visit: https://github.com/yvesguillo/crawlect"
        )


        # Verssion.
        parser.add_argument(
            "-v", "--version",
            action = "version",
            version = f"Crawlect v{__version__}",
            help = "show Crawlects's version number and exit"
        )


        # Core Parameters.
        core_group = parser.add_argument_group("Core Parameters")

        core_group.add_argument(
            "-p", "--path",
            type = str,
            default = ".",
            metavar = "path",
            help = "Path to crawl (default: '.').",
            guitype = "folderpath",
            guilabel = "Path to crawl",
            guitooltip = "Select the path you want to crawl."
        )

        core_group.add_argument(
            "-o", "--output",
            type = str,
            metavar = "output",
            help = "Output file path (e.g. './digest.md').",
            guitype = "filepath",
            guilabel = "Output file",
            guitooltip = "Choose the file you want the Markdown digest to be saved on."
        )

        core_group.add_argument(
            "-op", "--output-prefix",
            type = str,
            metavar = "prefix",
            help = "Prefix for dynamic output filename (e.g. './digest')."
        )

        core_group.add_argument(
            "-os", "--output-suffix",
            type = str,
            default = ".md",
            metavar = "suffix",
            help = "Suffix for dynamic filename (e.g. '.md')."
        )


        # Crawling Options.
        crawl_group = parser.add_argument_group("Crawling Options")

        crawl_group.add_argument(
            "--recur",
            action = BooleanOptionalAction,
            default = True,
            metavar = "recur",
            help = "Enable recursive crawling (default: enabled).",
            guilabel = "Recursive crawl",
            guitooltip = "Allow subfolder crawling."
        )

        crawl_group.add_argument(
            "-d", "--depth",
            type = int,
            default = inf,
            metavar = "depth",
            help = "Maximum crawl depth (default: infinity).",
            guilabel = "Crawl depth",
            guitooltip = "Select the maximum crawling depth (if recursive crawl is allowed)."
        )

        crawl_group.add_argument(
            "--crawlig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "crawlig",
            help = "Use `.crawlectignore` rules (default: enabled).",
            guilabel = "Use `.crawlectignore`",
            guitooltip = "Use `.crawlectignore` filtering rules if the file exists on the path to crawl's root.\n `.crawlectignore` follow the gitignore standard filtering definitions."
        )

        crawl_group.add_argument(
            "--gitig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "gitig",
            help = "Use `.gitignore` rules (default: enabled).",
            guilabel = "Use `.gitignore`",
            guitooltip = "Use `.gitignore` filtering rules if the file exists on the path to crawl's root."
        )

        crawl_group.add_argument(
            "--dockig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "dockig",
            help = "Use `.dockerignore` rules (default: enabled).",
            guilabel = "Use `.dockerignore`",
            guitooltip = "Use `.dockerignore` filtering rules if the file exists on the path to crawl's root."
        )


        # Output Formatting.
        output_group = parser.add_argument_group("Output Formatting")

        output_group.add_argument(
            "--xenv",
            action = BooleanOptionalAction,
            default = True,
            metavar = "xenv",
            help = "Sanitize `.env` values (default: enabled).",
            guilabel = "Sanitize `.env`",
            guitooltip = "Sanitize `*.env` files values for security purposes."
        )

        output_group.add_argument(
            "--tree",
            action = BooleanOptionalAction,
            default = True,
            metavar = "tree",
            help = "Include file tree structure (default: enabled).",
            guilabel = "File tree",
            guitooltip = "Add a crawled file tree to the Markdown digest."
        )


        # LLM Options.
        llm_group = parser.add_argument_group("LLM Options")

        llm_group.add_argument(
            "-llmapi", "--llm-api",
            choices = get_llm_api_class_map().keys(),
            metavar = "api",
            help = "LLM provider ('openai' | 'ollama').",
            guilabel = "LLM engine",
            guitooltip = "Choose the LLM engine to use for analysis requests."
        )

        llm_group.add_argument(
            "-llmhost", "--llm-host",
            metavar = "host",
            help = "LLM host URL (Ollama only).",
            guilabel = "LLM host URL",
            guitooltip = "For Ollama only, set the LLM engine host URL."
        )

        llm_group.add_argument(
            "-llmkey", "--llm-api-key",
            metavar = "key",
            help = "LLM API key (OpenAI only).",
            guilabel = "LLM API key",
            guitooltip = "For OpenAi only, set your API key."
        )

        llm_group.add_argument(
            "-llmmod", "--llm-model",
            metavar = "model",
            help = "Model name.",
            guilabel = "LLM model",
            guitooltip = "Choose the LLM model to use for analysis requests."
        )

        llm_group.add_argument(
            "-llmreq", "--llm-request",
            nargs = "+",
            metavar = "request",
            help = "LLM tasks list to perform.",
            guilabel = "LLM scripted tasks",
            guitooltip = "List the scripted LLM analysis to perform."
        )

        llm_group.add_argument(
            "-llmcust", "--llm-custom-requests",
            nargs = "+",
            metavar = "requests",
            help = "Custom LLM prompts list.",
            guilabel = "Custom LLM prompts",
            guitooltip = "List the custom LLM prompts to execute.\nPrompts shall be wrapped in quotation marks and separated with a white space."
        )


        # UX Options.
        ux_group = parser.add_argument_group("User Experience")

        ux_group.add_argument(
            "-verbose", "--verbose",
            action = BooleanOptionalAction,
            default = True,
            metavar = "verbose",
            help = "Toggle verbosity (default: enabled).",
            guilabel = "Verbosity",
            guitooltip = "Enable Crawlect Pyton core verbosity."
        )

        ux_group.add_argument(
            "-open", "--open",
            action = BooleanOptionalAction,
            default = True,
            metavar = "open",
            help = "Open output after generation (default: enabled).",
            guilabel = "Open digest",
            guitooltip = "Open digest file upon analysis completion."
        )

        ux_group.add_argument(
            "-clischem", "--cli-schema",
            action = BooleanOptionalAction,
            default = False,
            metavar = "schema",
            help = "Output CLI options shema (default: disabled)."
        )

        args = parser.parse_args()

        # Global.
        global VERBOSE
        VERBOSE = args.verbose

        # Introspect CLI parameters.
        if args.cli_schema:
            import json
            from .cli_option_schema import cli_option_schema
            # Ignored parameters are listed in the ignore list.
            schema = cli_option_schema(parser, ignore = ["--cli-schema", "--help", "--version", "--output-prefix", "--output-suffix"])
            print(json.dumps(schema, indent = 2))
            # Exit as this output is the only expected one.
            sys.exit(0)

        # Execute.
        try:
            # Digest.
            crawlect = validate_crawlect_params(args)

            # Launch output file composition.
            verbose(f"Launched {repr(crawlect.get_title())} processing.")
            crawlect.output_service.compose()

            # Confirm digest creation.
            verbose(f"Processed {repr(crawlect.get_title())} and stored digest in {repr(crawlect.output_service.current_output_name)}.")

            # Open the generated file if requested.
            if args.open:
                open_file(Path(crawlect.output_service.current_output_name))

        except Exception as error:
            raise Exception(f"\n!! - {type(error).__name__} :\nCrawlect composition failed:\n{error}")


        # Analysis.
        if args.llm_request or args.llm_custom_requests:
            try:
                # LLM validation and injection
                verbose(f"Launched {repr(crawlect.get_title())} analysis.")

                llm_instance = validate_llm_params(args)
                llm_requests = validate_llm_requests(args)
                llm_custom_prompts = validate_llm_custom_requests(args)

                crawlect.init_llm_service(llm_instance, llm_requests, llm_custom_prompts, crawlect.output_service.current_output_name)
                crawlect.run_llm_requests()
                verbose(f"Stored analysis in {repr(crawlect.output_service.analysisPathName)}.")

                if args.open:
                    open_file(Path(crawlect.output_service.analysisPathName))

            except Exception as error:
                raise Exception(f"\n!! - {type(error).__name__} :\nAnalysis failed:\n{error}")


    except KeyboardInterrupt:
        verbose("Interrupted by user.")

    except Exception as error:
        verbose(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            verbose(line)


if __name__ == "__main__":
    main()