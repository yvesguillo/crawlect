#! /usr/bin/env python3

# Custom modules.
from .crawlect import Crawlect

# Conditionnal Imports.
from .llm_api_loader import get_llm_api_class_map

# Standard modules.
from pathlib import Path
import os
import platform
import subprocess

def resolve_missing_path(args):
    """Ensure args.path is valid and exists, prompt if missing or incorrect."""

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


def prompt_overwrite_if_needed(args):
    """Prompt user if output file already exists and confirm overwrite or restart."""

    if args.output and Path(args.output).exists():
        print(
            f"\n# File overwrite warning #\nCrawlect is about to overwrite {repr(args.output)}.\n"
            "Its content will be lost!"
        )

        while True:
            decision = input("Choose 'proceed' or 'change':\n").strip().lower()

            if decision == "proceed":
                args.write_right = "w"
                break

            elif decision == "change":
                args.output = None
                args.output_prefix = None
                break

            else:
                print("Invalid choice. Please type 'proceed' or 'change'.")


def validate_crawlect_params(args):
    """Validate CLI args and return a Crawlect instance."""

    if not hasattr(args, 'write_right'):
        args.write_right = "x"

    if not args.recur:
        args.depth = 1

    resolve_missing_path(args)

    if args.output:
        prompt_overwrite_if_needed(args)

    return build_crawlect_instance(args)


def build_crawlect_instance(args):
    """Safely initialize and return a Crawlect instance from validated args."""

    try:
        args_dict = vars(args).copy()
        args_dict.pop("llm_config", None)  # Legacy field, kept for compatibility

        return Crawlect(**args_dict)

    except Exception as error:
        raise Exception(
            f"\n!! - {type(error).__name__} :\n"
            f"validate_crawlect_params could not initialize Crawlect:\n{error}"
        )


def get_llm_class(api_name):
    """Fetch the corresponding LLM class for the selected API."""

    llm_class_factory = get_llm_api_class_map().get(api_name)

    if not llm_class_factory:
        raise ValueError(f"Unknown LLM API: {api_name}")

    return llm_class_factory()


def build_llm_kwargs(args):
    """Construct keyword arguments to initialize the LLM instance."""
    kwargs = {"model": args.llm_model}

    if args.llm_api == "openai":
        kwargs["api_key"] = args.llm_api_key

    elif args.llm_api == "ollama":
        kwargs["host"] = args.llm_host

    return kwargs


def validate_llm_params(args):
    """Validate LLM-related CLI arguments and return an LLM instance."""

    validate_llm_required_fields(args)

    llm_class = get_llm_class(args.llm_api)
    llm_kwargs = build_llm_kwargs(args)

    return llm_class(**llm_kwargs)


def validate_llm_required_fields(args):
    """Ensure that all required parameters for the selected LLM are provided."""

    if not args.llm_api:
        raise ValueError("Missing LLM API: use --llm-api with either 'openai' or 'ollama'.")

    if not args.llm_model:
        raise ValueError("Missing LLM model: use --llm-model to specify a model name.")

    if args.llm_api == "openai" and not args.llm_api_key:
        raise ValueError("OpenAI requires --llm-api-key.")

    if args.llm_api == "ollama" and not args.llm_host:
        raise ValueError("Ollama requires --llm-host.")


def get_llm_analysis_methods():
    """Return a set of all method names from LLM_Code_Analysis that can be used as requests."""

    from .llm_code_analysis import LLM_Code_Analysis

    return {
        name for name in dir(LLM_Code_Analysis)
        if callable(getattr(LLM_Code_Analysis, name))
        and not name.startswith("_")
    }


def validate_llm_requests(args):
    """
    Validate that each requested analysis task corresponds to a method in LLM_Code_Analysis.
    Returns the list of valid method names.
    Raises ValueError if any invalid methods are found.
    """

    if not args.llm_request:
        return []

    valid_methods = get_llm_analysis_methods()
    unknown = [name for name in args.llm_request if name not in valid_methods]

    if unknown:
        raise ValueError(f"Unknown LLM request(s): {', '.join(unknown)}. "
                         f"Available: {', '.join(sorted(valid_methods))}")

    return args.llm_request


def validate_llm_custom_requests(args):
    """Validate and return custom LLM prompts."""

    if not args.llm_custom_requests:
        return []

    if not all(isinstance(prompt, str) for prompt in args.llm_custom_requests):
        raise ValueError("All --llm-custom-requests entries must be strings.")

    return args.llm_custom_requests


def open_file(path):
    """Open the given file with the system's default program."""

    system = platform.system()

    try:
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin": # macOS
            subprocess.run(["open", path])
        elif system == "Linux":
            subprocess.run(["xdg-open", path])
        else:
            raise Exception(f"Unsupported platform: {system}")
    except Exception as error:
        raise Exception(f"Failed to open file {path}: {error}")