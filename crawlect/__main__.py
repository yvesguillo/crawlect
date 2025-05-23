#! /usr/bin/env python3

# Custom modules.
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
        from argparse import ArgumentParser, BooleanOptionalAction, RawTextHelpFormatter

        parser = ArgumentParser(
            description="Crawlect CLI — Crawl, collect and document your codebase in Markdown.",
            formatter_class = argparse.RawTextHelpFormatter
        )


        # Verssion.
        parser.add_argument(
            "--version",
            action = "version",
            version = "Crawlect 1.0.5")


        # Core Parameters.
        core_group = parser.add_argument_group("Core Parameters")

        core_group.add_argument(
            "-p", "--path",
            type = str,
            default = ".",
            metavar = "path",
            help = (
                ">> Group: Core\n"
                ">> Description: Path to crawl.\n"
                ">> Values: any valid path\n"
                ">> Required: false\n"
                ">> Default: '.'"
            )
        )

        core_group.add_argument(
            "-o", "--output",
            type = str,
            metavar = "output",
            help = (
                ">> Group: Core\n"
                ">> Description: Static output file path.\n"
                ">> Values: e.g. './digest.md'\n"
                ">> Required: false"
            )
        )

        core_group.add_argument(
            "-op", "--output-prefix",
            type = str,
            metavar = "prefix",
            help = (
                ">> Group: Core\n"
                ">> Description: Prefix for dynamic output filename.\n"
                ">> Values: e.g. './digest'\n"
                ">> Required: false"
            )
        )

        core_group.add_argument(
            "-os", "--output-suffix",
            type = str,
            default = ".md",
            metavar = "suffix",
            help = (
                ">> Group: Core\n"
                ">> Description: Suffix for dynamic filename.\n"
                ">> Values: e.g. '.md'\n"
                ">> Required: false"
            )
        )


        # Crawling Options.
        crawl_group = parser.add_argument_group("Crawling Options")

        crawl_group.add_argument(
            "--recur",
            action = BooleanOptionalAction,
            default = True,
            metavar = "recur",
            help = (
                ">> Group: Crawling\n"
                ">> Description: Enable recursive crawling.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )

        crawl_group.add_argument(
            "-d", "--depth",
            type = int,
            default = inf,
            metavar = "depth",
            help = (
                ">> Group: Crawling\n"
                ">> Description: Maximum scan depth.\n"
                ">> Values: integer >= 1\n"
                ">> Default: inf"
            )
        )

        crawl_group.add_argument(
            "--crawlig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "crawlig",
            help = (
                ">> Group: Crawling\n"
                ">> Description: Use .crawlectignore rules.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )

        crawl_group.add_argument(
            "--gitig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "gitig",
            help = (
                ">> Group: Crawling\n"
                ">> Description: Use .gitignore rules.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )

        crawl_group.add_argument(
            "--dockig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "dockig",
            help = (
                ">> Group: Crawling\n"
                ">> Description: Use .dockerignore rules.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )


        # Output Formatting.
        output_group = parser.add_argument_group("Output Formatting")

        output_group.add_argument(
            "--xenv",
            action = BooleanOptionalAction,
            default = True,
            metavar = "xenv",
            help = (
                ">> Group: Output\n"
                ">> Description: Sanitize .env values.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )

        output_group.add_argument(
            "--tree",
            action = BooleanOptionalAction,
            default = True,
            metavar = "tree",
            help = (
                ">> Group: Output\n"
                ">> Description: Include file tree structure.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )


        # LLM Options.
        llm_group = parser.add_argument_group("LLM Options")

        llm_group.add_argument(
            "-llmapi", "--llm-api",
            choices=get_llm_api_class_map().keys(),
            metavar = "api",
            help = (
                ">> Group: LLM\n"
                ">> Description: LLM provider.\n"
                ">> Values: openai | ollama"
            )
        )

        llm_group.add_argument(
            "-llmhost", "--llm-host",
            metavar = "host",
            help = (
                ">> Group: LLM\n"
                ">> Description: LLM host URL (Ollama only)."
            )
        )

        llm_group.add_argument(
            "-llmkey", "--llm-api-key",
            metavar = "key",
            help = (
                ">> Group: LLM\n"
                ">> Description: LLM API key (OpenAI only)."
            )
        )
        llm_group.add_argument(
            "-llmmod", "--llm-model",
            metavar = "model",
            help = (
                ">> Group: LLM\n"
                ">> Description: Model name."
            )
        )

        llm_group.add_argument(
            "-llmreq", "--llm-request",
            nargs = "+",
            metavar = "request",
            help = (
                ">> Group: LLM\n"
                ">> Description: LLM tasks to perform.\n"
                ">> Values: review, docstring, readme"
            )
        )

        llm_group.add_argument(
            "-llmcust", "--llm-custom-requests",
            nargs = "+",
            metavar = "requests",
            help = (
                ">> Group: LLM\n"
                ">> Description: Custom LLM prompts."
            )
        )


        # UX Options.
        ux_group = parser.add_argument_group("User Experience")

        ux_group.add_argument(
            "-verbose", "--verbose",
            action = BooleanOptionalAction,
            default = True,
            metavar = "verbose",
            help = (
                ">> Group: UX\n"
                ">> Description: Toggle verbosity.\n"
                ">> Values: true | false\n"
                ">> Default: true"
            )
        )

        ux_group.add_argument(
            "-open", "--open",
            action = BooleanOptionalAction,
            default = False,
            metavar = "open",
            help = (
                ">> Group: UX\n"
                ">> Description: Open output after generation.\n"
                ">> Values: true | false\n"
                ">> Default: false"
            )
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
        if args.llm_request:
            try:
                # LLM validation and injection
                if args.llm_request:
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