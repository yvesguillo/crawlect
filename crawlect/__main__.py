#! /usr/bin/env python3

# Custom modules.
from .crawlect import Crawlect
from .llm_code_analysis import LLM_Code_Analysis
from .cli import (
    validate_crawlect_params,
    validate_llm_params,
    run_llm_analysis,
    open_file
)

# Conditionnal Imports.
from .llm_api_loader import get_llm_api_class_map

# Standard modules.
from pathlib import Path
import argparse
import traceback
from math import inf

def verbose(message):
    """Handle verbosity"""

    if VERBOSE:
        print("// " + message, flush = True)

def main():
    try:
        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect is a Python module designed to crawl a given directory, collect relevant files and contents, and document the entire structure in a clean, readable Markdown file.",
            epilog = "By default, Crawlect applies filtering rules from any .gitignore, .dockerignore or .crawlectignore present in the scanned path's first level."
        )

        parser.add_argument(
            "-p", "--path",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder '.'').")

        output_group = parser.add_argument_group("Output options")

        exclusive = output_group.add_mutually_exclusive_group()

        exclusive.add_argument(
            "-o", "--output",
            type = str,
            help = "Static output file path (e.g. './digest.md')."
        )

        exclusive.add_argument(
            "-op", "--output_prefix",
            type = str,
            help = "Prefix for dynamically generated output file name (e.g. './digest')."
        )

        # Suffix is optional only if prefix is provided
        output_group.add_argument(
            "-os", "--output_suffix",
            type = str,
            default = ".md",
            help = "Suffix for dynamic filename (e.g. '.md')."
        )

        parser.add_argument(
            "--recur",
            type = str,
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Enable recursive crawling (default: enabled). Use --no-recur to disable."
        )

        parser.add_argument(
            "-d", "--depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite)."
        )

        # Ignore files handling.
        parser.add_argument(
            "--crawlig",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Use .crawlectignore exclusion rules if exist (default: enabled). Use --no-crawlig to disable."
        )

        parser.add_argument(
            "--gitig",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Use .gitignore exclusion rules if exist (default: enabled). Use --no-gitig to disable."
        )

        parser.add_argument(
            "--dockig",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Use .dockerignore exclusion rules if exist (default: enabled). Use --no-dockig to disable."
        )

        # Advanced features parameters.
        parser.add_argument(
            "--xenv",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Sanitize .env variables to mitigate sensitive info leak risk (default: enabled). Use --no-xenv to disable."
        )

        parser.add_argument(
            "--tree",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Visualize directory tree in the output file (default: enabled). Use --no-tree to disable."
        )

        # LLM parameters.
        parser.add_argument(
            "-llmapi", "--llm-api",
            choices = get_llm_api_class_map().keys(),
            help = "LLM provider to use (e.g., 'openai' or 'ollama')."
        )

        parser.add_argument(
            "-llmhost", "--llm-host",
            help = "Host URL for the LLM API (only required for Ollama)."
        )

        parser.add_argument(
            "-llmkey", "--llm-api-key",
            help = "API key for the LLM (only required for OpenAI)."
        )

        parser.add_argument(
            "-llmmod", "--llm-model",
            help = "Model name to use (e.g., 'gpt-4' or 'llama3')."
        )

        parser.add_argument(
            "-llmreq", "--llm-request",
            nargs = "+",
            help = "LLM tasks to perform: review, docstring, readme."
        )

        parser.add_argument(
            "-open", "--open",
            action = argparse.BooleanOptionalAction,
            default = False,
            help = "Open the output files once generated (default: disabled)."
        )

        parser.add_argument(
            "-verbose", "--verbose",
            action = argparse.BooleanOptionalAction,
            default = True,
            help = "Toggle verbosity (default: enabled). Use --no-verbose to disable."
        )

        args = parser.parse_args()

        # Global.
        global VERBOSE
        VERBOSE = args.verbose

        # Execute.
        try:
            # Digest.
            crawlect = validate_crawlect_params(args)

            # Launch output file composition.
            verbose(f"Launched {repr(crawlect.getTitle())} processing.")
            crawlect.outputService.compose()

            # Confirm digest creation.
            verbose(f"Processed {repr(crawlect.getTitle())} and stored digest in {repr(crawlect.outputService.currentOutputName)}.")

            # Open the generated file if requested.
            if args.open:
                open_file(Path(crawlect.outputService.currentOutputName))

        except Exception as error:
            raise Exception(f"\n!! - {type(error).__name__} :\nCrawlect composition failed:\n{error}")


        # Analysis.
        if args.llm_request:
            try:
                verbose(f"Launched {repr(crawlect.getTitle())} analysis.")
                run_llm_analysis(crawlect, args)

                # Confirm analysis.
                verbose(f"Processed {repr(crawlect.getTitle())} and stored analysis in {repr(crawlect.outputService.analysisPathName)}.")

                # Open the generated file if requested.
                if args.open:
                    open_file(Path(crawlect.outputService.analysisPathName))

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