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
import sys
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
            "-v", "--version",
            action = "version",
            version = "Crawlect 1.0.5",
            help = "show Crawlects's version number and exit"
        )


        # Core Parameters.
        core_group = parser.add_argument_group("Core Parameters")

        core_group.add_argument(
            "-p", "--path",
            type = str,
            default = ".",
            metavar = "path",
            help = (
                "Path to crawl.\n"
                "Values: any valid path\n"
                "Required: false\n"
                "Default: '.'\n\n"
            )
        )

        core_group.add_argument(
            "-o", "--output",
            type = str,
            metavar = "output",
            help = (
                "Static output file path.\n"
                "Values: e.g. './digest.md'\n\n"
            )
        )

        core_group.add_argument(
            "-op", "--output-prefix",
            type = str,
            metavar = "prefix",
            help = (
                "Prefix for dynamic output filename.\n"
                "Values: e.g. './digest'\n\n"
            )
        )

        core_group.add_argument(
            "-os", "--output-suffix",
            type = str,
            default = ".md",
            metavar = "suffix",
            help = (
                "Suffix for dynamic filename.\n"
                "Values: e.g. '.md'\n\n"
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
                "Enable recursive crawling.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )

        crawl_group.add_argument(
            "-d", "--depth",
            type = int,
            default = inf,
            metavar = "depth",
            help = (
                "Maximum scan depth.\n"
                "Values: integer >= 1\n"
                "Default: inf\n\n"
            )
        )

        crawl_group.add_argument(
            "--crawlig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "crawlig",
            help = (
                "Use .crawlectignore rules.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )

        crawl_group.add_argument(
            "--gitig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "gitig",
            help = (
                "Use .gitignore rules.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )

        crawl_group.add_argument(
            "--dockig",
            action = BooleanOptionalAction,
            default = True,
            metavar = "dockig",
            help = (
                "Use .dockerignore rules.\n"
                "Values: true | false\n"
                "Default: true\n\n"
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
                "Sanitize .env values.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )

        output_group.add_argument(
            "--tree",
            action = BooleanOptionalAction,
            default = True,
            metavar = "tree",
            help = (
                "Include file tree structure.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )


        # LLM Options.
        llm_group = parser.add_argument_group("LLM Options")

        llm_group.add_argument(
            "-llmapi", "--llm-api",
            choices=get_llm_api_class_map().keys(),
            metavar = "api",
            help = (
                "LLM provider.\n"
                "Values: openai | ollama\n\n"
            )
        )

        llm_group.add_argument(
            "-llmhost", "--llm-host",
            metavar = "host",
            help = (
                "LLM host URL (Ollama only).\n\n"
            )
        )

        llm_group.add_argument(
            "-llmkey", "--llm-api-key",
            metavar = "key",
            help = (
                "LLM API key (OpenAI only).\n\n"
            )
        )
        llm_group.add_argument(
            "-llmmod", "--llm-model",
            metavar = "model",
            help = (
                "Model name.\n\n"
            )
        )

        llm_group.add_argument(
            "-llmreq", "--llm-request",
            nargs = "+",
            metavar = "request",
            help = (
                "LLM tasks to perform.\n"
                "Values: review, docstring, readme\n\n"
            )
        )

        llm_group.add_argument(
            "-llmcust", "--llm-custom-requests",
            nargs = "+",
            metavar = "requests",
            help = (
                "Custom LLM prompts.\n\n"
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
                "Toggle verbosity.\n"
                "Values: true | false\n"
                "Default: true\n\n"
            )
        )

        ux_group.add_argument(
            "-open", "--open",
            action = BooleanOptionalAction,
            default = False,
            metavar = "open",
            help = (
                "Open output after generation.\n"
                "Values: true | false\n"
                "Default: false\n\n"
            )
        )

        ux_group.add_argument(
            "-clischem", "--cli-schema",
            action = BooleanOptionalAction,
            default = False,
            metavar = "schema",
            help = (
                "Output CLI options shema.\n"
                "Values: true | false\n"
                "Default: false\n\n"
            )
        )

        args = parser.parse_args()

        # Global.
        global VERBOSE
        VERBOSE = args.verbose

        # Introspect CLI parameters.
        if args.cli_schema:
            import json
            from .cli_option_schema import cli_option_schema
            schema = cli_option_schema(parser)
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