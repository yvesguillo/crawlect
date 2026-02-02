#! /usr/bin/env python3

# Custom modules.
from .scan import Scan
from .format import Format
from .output import Output

# Standard modules.
from pathlib import Path
from fnmatch import fnmatch
from math import inf
import sys
import io

# UTF-8 settings.
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Third party module.
from gitignore_parser import parse_gitignore as parse_ignorefile

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self, **kwargs):

        # Store the class arguments for __repr__.
        self.args = kwargs

        self.path = kwargs.get("path", ".")
        self.output = kwargs.get("output", "digest.md")
        self.output_prefix = kwargs.get("output-prefix", "digest")
        self.output_suffix = kwargs.get("output-suffix", ".md")
        self.recur = kwargs.get("recur", True)
        self.depth = kwargs.get("depth", inf)

        # Ignore files handling.
        self.crawlectignore = kwargs.get("crawlectignore", True)
        self.gitignore = kwargs.get("gitignore", True)
        self.dockerignore = kwargs.get("dockerignore", True)

        self.simple_path_to_ignore = []
        self.ignore_file_list = []

        # Advanced features parameters.
        self.xenv = kwargs.get("xenv", True)
        self.tree = kwargs.get("tree", True)

        # File overwrite setings.
        self.write_right = kwargs.get("write_right", )

        # LLM
        self.llm_service = None
        self.llm_requested_tasks = []
        self.llm_custom_requests = []

        self.warmup()

        self.init_services()

        self.process_ignore_files()

        self.generate_path_list()

    def warmup(self):
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


    def init_services(self):
        """Build Crawlect services"""
        try:
            self.scan_service = Scan(self)

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Scan service.")
            raise

        try:
            self.format_service = Format(self) # Format does not take Crawlect instance as parameter.

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Format service.")
            raise

        try:
            self.output_service = Output(self)

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Output service.")
            raise


    def init_llm_service(self, llm_instance, requests, custom_prompts, codebase_path):
        """Assign LLM service and tasks from already validated CLI arguments."""

        from .llm_code_analysis import LLM_Code_Analysis

        with open(Path(codebase_path), "r", encoding="utf-8") as f:
            codebase = f.read()

        self.llm_service = LLM_Code_Analysis(llm_instance, codebase)
        self.llm_requested_tasks = requests
        self.llm_custom_requests = custom_prompts


    def run_llm_requests(self):
        """Execute previously requested LLM tasks and write analysis to file."""

        if not self.llm_service or (not self.llm_requested_tasks and not self.llm_custom_requests):
            return

        from pathlib import Path

        output_path = Path(self.output_service.current_output_name).with_suffix(".md.analysis.md")

        # Handle scripted requests.
        with open(output_path, "w", encoding="utf-8") as f:
            for request in self.llm_requested_tasks:
                header = (
                    f"///{len(request) * '/'}///\n"
                    f"// {request.upper()} //\n"
                    f"///{len(request) * '/'}///\n"
                )
                f.write(f"{header}\n{getattr(self.llm_service, request)()}\n\n")

            # Handle custom prompts.
            for index, prompt in enumerate(self.llm_custom_requests):
                header = (
                    f"/////////////////{'/' * len(str(index + 1))}///\n"
                    f"// CUSTOM_PROMPT_{str(index + 1)} //\n"
                    f"/////////////////{'/' * len(str(index + 1))}///\n\n"
                    f"**Prompt**: `{prompt[:50]}{'…' if len(prompt) > 50 else ''}`\n\n"
                )

                response = self.llm_service.llm.request(prompt)

                f.write(f"{header}\n{response}\n\n")

        self.output_service.analysisPathName = str(output_path)


    def process_ignore_files(self):
        """Check for ignore files settings and fetch ignore list from these."""

        if self.crawlectignore and Path(self.path + "/.crawlectignore").exists():
            # Ignore the ignore file itselfe.
            self.simple_path_to_ignore.append(self.path + "/.crawlectignore")
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.crawlectignore")))

        if self.gitignore and Path(self.path + "/.gitignore").exists():
            # Ignore the ignore file itselfe and .git folder as it seems logic in this case.
            self.simple_path_to_ignore.append(Path(self.path + "/.gitignore"))
            self.simple_path_to_ignore.append(Path(self.path + "/.git"))
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.gitignore")))

        if self.dockerignore and Path(self.path + "/.dockerignore").exists():
            # Ignore the ignore file itselfe.
            self.simple_path_to_ignore.append(Path(self.path + "/.dockerignore"))
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.dockerignore")))

        # Avoid duplicates.
        self.simple_path_to_ignore = list(set(self.simple_path_to_ignore))


    def generate_path_list(self):
        """Prepare the path list which will be treated and written in output file."""
        try:
            self.files = self.scan_service.list_path_in()

        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and proceed to paths listing.")
            raise

    def get_title(self):
        """Simply returns path to crawl's name"""
        return self.title


    # Assess if this should be sent to a common class ("Filter" class ?).
    def is_path_ignored(self, path):
        """Check if path match any .gitignore pattern or path include/exclude list parameter item."""

        for ignored in self.simple_path_to_ignore:
            if fnmatch(path, ignored):
                return True

        for ignoreFile in self.ignore_file_list:
            if ignoreFile(path):
                return True

        return False


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        parameters = ", ".join(f"{k} = {repr(v)}" for k, v in self.args.items())
        return f"{type(self).__name__}({parameters})"