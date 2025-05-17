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
        self.output_prefix = kwargs.get("output_prefix", "digest")
        self.output_suffix = kwargs.get("output_suffix", ".md")
        self.recur = kwargs.get("recur", True)
        self.depth = kwargs.get("depth", inf)

        # Ignore files handling.
        self.crawlectignore = kwargs.get("crawlectignore", True)
        self.gitignore = kwargs.get("gitignore", True)
        self.dockerignore = kwargs.get("dockerignore", True)

        self.simplePathToIgnore = []
        self.ignore_file_list = []

        # Advanced features parameters.
        self.xenv = kwargs.get("xenv", True)
        self.tree = kwargs.get("tree", True)

        # File overwrite setings.
        self.writeRight = kwargs.get("writeRight", )

        self.warmUp()

        self.initServices()

        self.processIgnoreFiles()

        self.generatePathList()

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

        if self.crawlectignore and Path(self.path + "/.crawlectignore").exists():
            # Ignore the ignore file itselfe.
            self.simplePathToIgnore.append(self.path + "/.crawlectignore")
            # Append the ignore file path to the list of ignorefile to interogate for exclusion rules.
            self.ignore_file_list.append(parse_ignorefile(Path(self.path + "/.crawlectignore")))

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
        parameters = ", ".join(f"{k} = {repr(v)}" for k, v in self.args.items())
        return f"{type(self).__name__}({parameters})"