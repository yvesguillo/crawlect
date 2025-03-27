#! /usr/bin/env python3
"""Crawlect is a module intended to describe files from a given path and transcribe these into a single markdown file."""

import argparse
from pathlib import Path

class Crawlect:
    """Crawl a given path to list and describe all files on a single markdown file."""

    # From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
    _languages = {".abap": "abap", ".ada": "ada", ".adb": "ada", ".ads": "ada", ".ahk": "ahk", ".ahkl": "ahk", ".htaccess": "apacheconf", "apache.conf": "apacheconf", "apache2.conf": "apacheconf", ".applescript": "applescript", ".as": "as", ".as": "as3", ".asy": "asy", ".bash": "bash", ".ebuild": "bash", ".eclass": "bash", ".env.example": "bash", ".env.local": "bash", ".env": "bash", ".ksh": "bash", ".sh": "bash", ".bat": "bat", ".cmd": "bat", ".befunge": "befunge", ".bmx": "blitzmax", ".boo": "boo", ".b": "brainfuck", ".bf": "brainfuck", ".c": "c", ".h": "c", ".cfc": "cfm", ".cfm": "cfm", ".cfml": "cfm", ".spt": "cheetah", ".tmpl": "cheetah", ".cl": "cl", ".el": "cl", ".lisp": "cl", ".clj": "clojure", ".cljs": "clojure", ".cmake": "cmake", "CMakeLists.txt": "cmake", ".coffee": "coffeescript", ".sh-session": "console", "control": "control", ".c++": "cpp", ".cc": "cpp", ".cpp": "cpp", ".cxx": "cpp", ".h++": "cpp", ".hh": "cpp", ".hpp": "cpp", ".hxx": "cpp", ".pde": "cpp", ".cs": "csharp", ".css": "css", ".feature": "cucumber", ".pxd": "cython", ".pxi": "cython", ".pyx": "cython", ".d": "d", ".di": "d", ".pas": "delphi", ".diff": "diff", ".patch": "diff", "Dockerfile.": "dockerfile", "Dockerfile": "dockerfile", ".darcspatch": "dpatch", ".dpatch": "dpatch", ".duel": "duel", ".jbst": "duel", ".dyl": "dylan", ".dylan": "dylan", ".erb": "erb", ".erl-sh": "erl", ".erl": "erlang", ".hrl": "erlang", ".evoque": "evoque", ".factor": "factor", ".flx": "felix", ".flxh": "felix", ".f": "fortran", ".f90": "fortran", ".s": "gas", ".S": "gas", ".kid": "genshi", ".gitignore": "gitignore", ".frag": "glsl", ".geo": "glsl", ".vert": "glsl", ".plot": "gnuplot", ".plt": "gnuplot", ".go": "go", ".(1234567)": "groff", ".man": "groff", ".haml": "haml", ".hs": "haskell", ".htm": "html", ".html": "html", ".xhtml": "html", ".xslt": "html", ".hx": "hx", ".hy": "hybris", ".hyb": "hybris", ".cfg": "ini", ".conf": "ini", ".editorconfig": "ini", ".flake8": "ini", ".ini": "ini", ".npmrc": "ini", ".io": "io", ".ik": "ioke", ".weechatlog": "irc", ".jade": "jade", ".java": "java", ".js": "js", ".babelrc": "json", ".eslintrc": "json", ".json": "json", ".json5": "json", ".prettierrc": "json", ".jsp": "jsp", ".lhs": "lhs", ".ll": "llvm", ".lgt": "logtalk", ".lua": "lua", ".wlua": "lua", ".mak": "make", "GNUmakefile": "make", "Makefile.": "make", "Makefile": "make", "makefile": "make", ".mao": "mako", ".maql": "maql", ".md": "markdown", ".mc": "mason", ".mhtml": "mason", ".mi": "mason", "autohandler": "mason", "dhandler": "mason", ".mo": "modelica", ".def": "modula2", ".mod": "modula2", ".moo": "moocode", ".mu": "mupad", ".mxml": "mxml", ".myt": "myghty", "autodelegate": "myghty", ".asm": "nasm", ".ASM": "nasm", ".ns2": "newspeak", ".objdump": "objdump", ".m": "objectivec", ".j": "objectivej", ".ml": "ocaml", ".mli": "ocaml", ".mll": "ocaml", ".mly": "ocaml", ".ooc": "ooc", ".pl": "perl", ".pm": "perl", ".php(345)": "php", ".php": "php", ".eps": "postscript", ".ps": "postscript", ".po": "pot", ".pot": "pot", ".inc": "pov", ".pov": "pov", ".pl": "prolog", ".pro": "prolog", ".prolog": "prolog", ".properties": "properties", ".proto": "protobuf", ".py3tb": "py3tb", ".pytb": "pytb", ".py": "python", ".pyw": "python", ".sc": "python", ".tac": "python", "SConscript": "python", "SConstruct": "python", ".R": "r", ".duby": "rb", ".gemspec": "rb", ".rake": "rb", ".rb": "rb", ".rbw": "rb", ".rbx": "rb", "Rakefile": "rb", ".Rout": "rconsole", ".r": "rebol", ".r3": "rebol", ".cw": "redcode", ".rhtml": "rhtml", ".rest": "rst", ".rst": "rst", "Vagrantfile": "ruby", ".sass": "sass", ".scala": "scala", ".scaml": "scaml", ".scm": "scheme", ".scss": "scss", ".st": "smalltalk", ".tpl": "smarty", "sources.list": "sourceslist", ".R": "splus", ".S": "splus", ".sql": "sql", ".sqlite3-console": "sqlite3", "squid.conf": "squidconf", ".ssp": "ssp", ".tcl": "tcl", ".csh": "tcsh", ".tcsh": "tcsh", ".aux": "tex", ".tex": "tex", ".toc": "tex", ".log": "text", ".txt": "text", "requirements.txt": "text", ".toml": "toml", "Pipfile.lock": "toml", "Pipfile": "toml", "pyproject.toml": "toml", ".sv": "v", ".v": "v", ".vala": "vala", ".vapi": "vala", ".bas": "vbnet", ".vb": "vbnet", ".fhtml": "velocity", ".vm": "velocity", ".vim": "vim", ".vimrc": "vim", ".rss": "xml", ".wsdl": "xml", ".xml": "xml", ".xsd": "xml", ".xsl": "xml", ".xslt": "xml", ".xquery": "xquery", ".xqy": "xquery", ".xsl": "xslt", ".xslt": "xslt", ".yaml": "yaml", ".yarnrc": "yaml", ".yml": "yaml"}

    def __init__(self, path = ".", dest = "description.md", igno = []):
        self.path = path
        self.paths = Path(path)
        self.dest = dest
        self.files = self.listFilesIn(paths = self.paths)
        self.title = self.paths.name
        self.digest = ""

    def listFilesIn(self, paths = None, files = [], recur = False):
        """Append all files in specified path as strings in a list and return it."""
        if paths is None:
            paths = self.paths
        for path in paths.iterdir():
            if path.is_file():
                files.append(path)
            elif path.is_dir() and recur is True:
                self.listFilesIn(path = path, files = files, recur = recur)
        return files

if __name__ == "__main__":
    try:

        # Parameters.
        parser = argparse.ArgumentParser(
            description = "Crawlect crawl a given path to list and describe all files on a single markdown file.",
            epilog = "Inclusions parameters overrule exclusions parameters. Example usage: TBD"
        )

        parser.add_argument(
            "-p", "--path", "--path-to-crawl",
            type = str,
            default = ".",
            help = "Path to crawl (default is current folder \".\")")

        parser.add_argument(
            "-d", "--digest", "--digest-output-file",
            type = str,
            default = "description.md",
            help = "Output markdown digest file.")

        parser.add_argument(
            "-r", "--recur", "--recursive-crawling",
            action = "store_true",
            help = "Enable recursive crawling.")

        parser.add_argument(
            "-xel", "--excl-ext-li", "--excluded-extentions-from-listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from listing (e.g., .jpg .png).")

        parser.add_argument(
            "-xdl", "--excl-dir-li", "--excluded-directories-from-listing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from listing (e.g., bin render).")

        parser.add_argument(
            "-xfl", "--excl-fil-li", "--excluded-files-from-listing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from listing (e.g., README.md .png).")

        parser.add_argument(
            "-xew", "--excl-ext-wr", "--excluded-extentions-from-writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from writing (e.g., .jpg .png).")

        parser.add_argument(
            "-xdw", "--excl-dir-wr", "--excluded-directories-from-writing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from writing (e.g., bin render).")

        parser.add_argument(
            "-xfw", "--excl-fil-wr", "--excluded-files-from-writing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from writing (e.g., README.md .png).")

        parser.add_argument(
            "-iel", "--incl-ext-li", "--include-extentions-from-listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include in listing (e.g., .jpg .png).")

        parser.add_argument(
            "-idl", "--incl-dir-li", "--include-directories-from-listing",
            nargs = "*",
            default = [],
            help = "List of directories to include in listing (e.g., bin render).")

        parser.add_argument(
            "-ifl", "--incl-fil-li", "--include-files-from-listing",
            nargs = "*",
            default = [],
            help = "List of files to include in listing (e.g., README.md .png).")

        parser.add_argument(
            "-iew", "--incl-ext-wr", "--include-extentions-from-writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for writing (e.g., .jpg .png).")

        parser.add_argument(
            "-idw", "--incl-dir-wr", "--include-directories-from-writing",
            nargs = "*",
            default = [],
            help = "List of directories to include for writing (e.g., bin render).")

        parser.add_argument(
            "-ifw", "--incl-fil-wr", "--include-files-from-writing",
            nargs = "*",
            default = [],
            help = "List of files to include for writing (e.g., README.md .png).")

        args = parser.parse_args()

        from inspect import getmembers
        from pprint import pprint
        pprint(getmembers(args))

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error)} error:\n{error.args}")