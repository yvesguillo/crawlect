# crawlect
2025.04.09 18:15

Generated with Crawlect.

## File structure

Directory tree.

- **crawlect/**  
    - [.env](#{1})  
    - [.gitignore](#{2})  
    - [README.md](#{3})  
    - [crawlect.py](#{4})  
    - [description.md](#{5})  
    - [essai1.md](#{6})  
    - [format.py](#{7})  
    - [languages.json](#{8})  
    - [note.md](#{9})  
    - [output.py](#{10})  
    - [scan.py](#{11})  
    - `.idea/`  
        - [.gitignore](#{12})  
        - [crawlect.iml](#{13})  
        - [misc.xml](#{14})  
        - [modules.xml](#{15})  
        - [vcs.xml](#{16})  
        - [workspace.xml](#{17})  
        - `inspectionProfiles/`  
            - [profiles_settings.xml](#{18})  
    - `__pycache__/`  
        - [format.cpython-312.pyc](#{19})  
        - [output.cpython-312.pyc](#{20})  
        - [scan.cpython-312.pyc](#{21})  
    - `tata/`  
        - `toto1/`  
    - `toto/`  
        - `toto1/`  


## Files:

### **scan.cpython-312.pyc**{1}   
`__pycache__/scan.cpython-312.pyc`

### **output.cpython-312.pyc**{2}   
`__pycache__/output.cpython-312.pyc`

### **format.cpython-312.pyc**{3}   
`__pycache__/format.cpython-312.pyc`

<h3 id="4">output.py](output.py)</h3> 
`output.py`
```python
#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string

class Output:
    """
    Output class provide standard Crawlec output features.
    It require and only accept one instance of Crawlect as argument.
    """

    __rand_filename_char_list = string.ascii_lowercase + string.digits

    def __init__(self, crawler):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler = crawler

        self.currentOutputName = ""
        self.composition = ()

    def compose(self):
        """Compose output file."""

        date = datetime.now()
        self.currentOutputName = self.standardOutputName()

        # Early version.
        with open(self.currentOutputName, self.crawler.writeRight) as outputFile:

            # Title
            outputFile.write(f"# {self.crawler.getTitle()}\n{str(date.year)}.{str("{:02d}".format(date.month))}.{str("{:02d}".format(date.day))} {str("{:02d}".format(date.hour))}:{str("{:02d}".format(date.minute))}\n\nGenerated with {type(self.crawler).__name__}.\n\n")

            # Directory tree
            if self.crawler.tree:
                outputFile.write(f"## File structure\n\nDirectory tree.\n\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer = self.crawler.excl_dir_li, deep = self.crawler.depth)}\n\n")

            counter = 0
            # Files list
            outputFile.write("## Files:\n\n")
            for file in self.crawler.files:
                
                fileDepth = len(file.parents) -1
                
                idmd = "{" + str(counter) + "}"
                if file.is_file() and str(file) != self.currentOutputName:
                    if not self.crawler.formatService.searchType(file) is None:
                        outputFile.write(f"<h3 id=\"{counter}\">{file.name}]({file})</h3> \n")
                    else:
                        outputFile.write(f"### **{file.name}**{idmd}   \n")
                    outputFile.write(f"`{file}`\n")
                    if self.isFileToInclude(file):
                        try:
                            content = self.crawler.formatService.insertCodebox(file)
                            if not content is None:
                                outputFile.write(self.crawler.formatService.insertCodebox(file))
                        except Exception as error:
                            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not create codebox from {repr(file)}: {error}")
                    outputFile.write("\n")
                counter += 1

    def standardOutputName(self):
        """Return standard output file name if no filename specified."""

        if self.crawler.output is None:
            now = datetime.now()
            return f"{self.crawler.output_prefix}-{self.yearmodahs()}-{"".join(choices(self.__rand_filename_char_list, k = 6))}{self.crawler.output_suffix}"
        else:
            return self.crawler.output

    def yearmodahs(self, date = datetime.now()):
        """Return givent date as yearmoda plus hours and seconds string."""

        return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_wr == () and self.crawler.excl_fil_wr == () and self.crawler.incl_ext_wr == () and self.crawler.incl_fil_wr == ():
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_wr:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_wr and path.name not in self.crawler.excl_fil_wr:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_wr and path.name not in self.crawler.incl_fil_wr:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_wr:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_wr != () or self.crawler.incl_fil_wr != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
<h3 id="5">description.md](description.md)</h3> 
`description.md`
``````````````````````markdown
# crawlect
2025.04.09 16:58

Generated with Crawlect.

## File structure

Directory tree.

- **crawlect/**  
    - [.env](#env)  
    - [.gitignore](#gitignore)  
    - [README.md](#READMEmd)  
    - [crawlect.py](#crawlectpy)  
    - [description.md](#descriptionmd)  
    - [format.py](#formatpy)  
    - [languages.json](#languagesjson)  
    - [note.md](#notemd)  
    - [output.py](#outputpy)  
    - [scan.py](#scanpy)  
    - `.idea/`  
        - [.gitignore](#gitignore)  
        - [crawlect.iml](#crawlectiml)  
        - [misc.xml](#miscxml)  
        - [modules.xml](#modulesxml)  
        - [vcs.xml](#vcsxml)  
        - [workspace.xml](#workspacexml)  
        - `inspectionProfiles/`  
            - [profiles_settings.xml](#profiles_settingsxml)  
    - `__pycache__/`  
        - [format.cpython-312.pyc](#formatcpython-312pyc)  
        - [output.cpython-312.pyc](#outputcpython-312pyc)  
        - [scan.cpython-312.pyc](#scancpython-312pyc)  
    - `tata/`  
        - `toto1/`  
    - `toto/`  
        - `toto1/`  


## Files:

### **scan.cpython-312.pyc**  
`__pycache__/scan.cpython-312.pyc`

### **output.cpython-312.pyc**  
`__pycache__/output.cpython-312.pyc`

### **format.cpython-312.pyc**  
`__pycache__/format.cpython-312.pyc`

### **[output.py](output.py)**  
`output.py`
```python
#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string

class Output:
    """
    Output class provide standard Crawlec output features.
    It require and only accept one instance of Crawlect as argument.
    """

    __rand_filename_char_list = string.ascii_lowercase + string.digits

    def __init__(self, crawler):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler = crawler

        self.currentOutputName = ""
        self.composition = ()

    def compose(self):
        """Compose output file."""

        date = datetime.now()
        self.currentOutputName = self.standardOutputName()

        # Early version.
        with open(self.currentOutputName, self.crawler.writeRight) as outputFile:

            # Title
            outputFile.write(f"# {self.crawler.getTitle()}\n{str(date.year)}.{str("{:02d}".format(date.month))}.{str("{:02d}".format(date.day))} {str("{:02d}".format(date.hour))}:{str("{:02d}".format(date.minute))}\n\nGenerated with {type(self.crawler).__name__}.\n\n")

            # Directory tree
            if self.crawler.tree:
                outputFile.write(f"## File structure\n\nDirectory tree.\n\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer = self.crawler.excl_dir_li, deep = self.crawler.depth)}\n\n")

            # Files list
            outputFile.write("## Files:\n\n")
            for file in self.crawler.files:

                fileDepth = len(file.parents) -1

                if file.is_file() and str(file) != self.currentOutputName:
                    if not self.crawler.formatService.searchType(file) is None:
                        outputFile.write(f"### **[{file.name}]({file})**  \n")
                    else:
                        outputFile.write(f"### **{file.name}**  \n")
                    outputFile.write(f"`{file}`\n")
                    if self.isFileToInclude(file):
                        try:
                            content = self.crawler.formatService.insertCodebox(file)
                            if not content is None:
                                outputFile.write(self.crawler.formatService.insertCodebox(file))
                        except Exception as error:
                            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not create codebox from {repr(file)}: {error}")
                    outputFile.write("\n")

    def standardOutputName(self):
        """Return standard output file name if no filename specified."""

        if self.crawler.output is None:
            now = datetime.now()
            return f"{self.crawler.output_prefix}-{self.yearmodahs()}-{"".join(choices(self.__rand_filename_char_list, k = 6))}{self.crawler.output_suffix}"
        else:
            return self.crawler.output

    def yearmodahs(self, date = datetime.now()):
        """Return givent date as yearmoda plus hours and seconds string."""

        return str(date.year) + str("{:02d}".format(date.month)) + str("{:02d}".format(date.day)) + str("{:02d}".format(date.hour)) + str("{:02d}".format(date.minute)) + str("{:02d}".format(date.second))

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_wr == () and self.crawler.excl_fil_wr == () and self.crawler.incl_ext_wr == () and self.crawler.incl_fil_wr == ():
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_wr:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_wr and path.name not in self.crawler.excl_fil_wr:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_wr and path.name not in self.crawler.incl_fil_wr:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_wr:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_wr != () or self.crawler.incl_fil_wr != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
### **[crawlect.py](crawlect.py)**  
`crawlect.py`
```python
#! /usr/bin/env python3

from pathlib import Path
from math import inf

# Custom modules.
from scan import Scan
from format import Format
from output import Output

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self, path = None, output = None, output_prefix = None, output_suffix = None, recur = True, depth = inf, excl_ext_li = (), excl_dir_li = (), excl_fil_li = (), excl_ext_wr = (), excl_dir_wr = (), excl_fil_wr = (), incl_ext_li = (), incl_dir_li = (), incl_fil_li = (), incl_ext_wr = (), incl_dir_wr = (), incl_fil_wr = (), xenv = True, tree = True):

        # Store the class arguments for __repr__.
        self.args = dict()

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

        # Files and xtensions inclusion/exclusions parameters.
        self.excl_ext_li = excl_ext_li
        self.args["excl_ext_li"] = self.excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.args["excl_dir_li"] = self.excl_dir_li
        self.excl_fil_li = excl_fil_li
        self.args["excl_fil_li"] = self.excl_fil_li
        self.excl_ext_wr = excl_ext_wr
        self.args["excl_ext_wr"] = self.excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.args["excl_dir_wr"] = self.excl_dir_wr
        self.excl_fil_wr = excl_fil_wr
        self.args["excl_fil_wr"] = self.excl_fil_wr
        self.incl_ext_li = incl_ext_li
        self.args["incl_ext_li"] = self.incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.args["incl_dir_li"] = self.incl_dir_li
        self.incl_fil_li = incl_fil_li
        self.args["incl_fil_li"] = self.incl_fil_li
        self.incl_ext_wr = incl_ext_wr
        self.args["incl_ext_wr"] = self.incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.args["incl_dir_wr"] = self.incl_dir_wr
        self.incl_fil_wr = incl_fil_wr
        self.args["incl_fil_wr"] = self.incl_fil_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denied by default.
        self.writeRight = "x"

        # Validate attributes parameters.
        self.validate()

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

        try:
            self.scanService = Scan(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Scan service.")
            raise

        try:
            self.formatService = Format() # Format does not take Crawlect instance as parameter.
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Format service.")
            raise

        try:
            self.outputService = Output(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Output service.")
            raise

        try:
            self.files = self.scanService.listFilesIn()
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and proceed to paths listing.")
            raise

    # To be enhanced. State patern?
    def validate(self):
        """Validate attributes and regenerate dynamic attributes."""

        # Max depth adaptation if recur is False.
        if not self.recur:
            self.depth = 1

        # Interactive mode.
        if __name__ == "__main__":

            while self.path is None:
                self.path = input(f"\n# Missing argument #\n{type(self).__name__} require a path to crawl. Please enter the desired path (e.g.: '.') or [Ctrl]+[C] then [Enter] to abort.\n")

            while not Path(self.path).exists():
                self.path = input(f"\n# Path error #\n{type(self).__name__} could not find {repr(self.path)}, please enter the path to crawl.\n")

            while self.output is None and self.output_prefix is None:
                print(f"\n# Missing argument #\n{type(self).__name__} require an output file-name for static output file-name (e.g.: './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: './descript' as prefix, and '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'")
                while True:
                    _ = input("Please choose between 'static' and 'unique', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
                    if _ == "static":
                        while self.output is None or not self.output:
                            self.output = input("Please enter a static output file-name, e.g.: './output.md' or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    elif _ == "unique":
                        while self.output_prefix is None or not self.output_prefix:
                            self.output_prefix = input("Please enter a prefix, e.g.: './output' or [Ctrl]+[C] then [Enter] to abort.\n")
                        while self.output_suffix is None:
                            self.output_suffix = input("Please enter a suffix, e.g.: '.md' (suffix can be empty) or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    else:
                        continue

            if self.output is not None:
                if Path(self.output).exists():
                        print(f"\n# File overwrite #\n{type(self).__name__} is about to overwrite {repr(self.output)}. Its content will be lost!")
                        while True:
                            _ = input("Please choose between 'proceed' and 'change', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
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
                    raise IOError(f"\n# Permission error #\n{type(self).__name__} do not allow file {repr(self.output)} to be overwrited in module mode. Please errase the file first if you want to keep this output path.")

            validationMessage = ""
            if self.path is None:
                validationMessage += "- A path to crawl, e.g.: path = '.'\n"
            elif not Path(self.path).exists():
                validationMessage += f"A valid path to crawl, {self.path} cannot be found.\n"
            if self.output is None and self.output_prefix is None:
                validationMessage += "- An output file-name for static output file-name (e.g.: --output = './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: --output_prefix = './descript', --output_suffix = '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'\n"
            if validationMessage:
                raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires:\n{validationMessage}Got: {self}")

    def getTitle(self):
        return self.title

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
            epilog = "Filtering rules allow you to forcibly include or exclude certain directories, files names or file extensions. All files will be listed if there are no rules. Inclusion overrules exclusion on same caracteristics and file-name rules takes precedence against extension rules."
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
            help = "Output markdown digest file prefix ('description' by default) associated with --output_suffix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-os", "--output_suffix", "--output_file_suffix",
            type = str,
            default = ".md",
            
            help = "Output markdown digest file prefix ('.md' by default) associated with --output_prefix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-r", "--recur", "--recursive_crawling",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Enable recursive crawling (default is True).")

        parser.add_argument(
            "-d", "--depth", "--recursive_crawling_depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite).")

        parser.add_argument(
            "-xel", "--excl_ext_li", "--excluded_xtensions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_xtensions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_xtensions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include in listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to include in listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to include in listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_xtensions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to include for writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to include for writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xen", "--xenv", "--randomize_env_variables",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Randomize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(path = args.path, output = args.output, output_prefix = args.output_prefix, output_suffix = args.output_suffix, recur = args.recur, depth = args.depth, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_li = args.excl_fil_li, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, excl_fil_wr = args.excl_fil_wr, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_li = args.incl_fil_li, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, incl_fil_wr = args.incl_fil_wr, xenv = args.xenv, tree = args.tree)

        # Launch output file composition
        crawlect.outputService.compose()

        # Confirm.
        print(f"\n{type(crawlect.outputService).__name__} processed {repr(crawlect.getTitle())} and stored description in {repr(crawlect.outputService.currentOutputName)}.")

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)
```
### **[README.md](README.md)**  
`README.md`
````````````markdown
# Crawlect – Crawl, Collect & Document Your Codebase in Markdown

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

## Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Traversing your project directory (recursively if needed),
- Filtering files and directories with powerful inclusion/exclusion rules,
- Masking sensitive data (like `.env` values),
- Embedding file contents in Markdown-formatted code blocks,
- Automatically generating a well-organized, shareable `.md` file.

## Use cases

- Quickly understand an unfamiliar codebase
- Auto-document your projects
- Share code context with collaborators (or *LLM*!)
- Safely include `.env` files without leaking sensitive values

***Think of Crawlect as your markdown-minion — obedient, efficient, and allergic to messy folders.***

## Crawlect – User Guide
**Crawlect**, the tool that turns your project folder into a beautifully structured Markdown digest — effortlessly.

## Installation
Crawlect currently runs as a standalone module. To use it, simply clone the repo or copy the files:

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
python3 crawlect.py
```
*(Packaging for pip? Let us know. We'll help you make it pip-installable!)*

## Quick Start
Generate a Markdown description of the current directory:

```bash
python3 crawlect.py -p . -o ./description.md
```
This will scan the current folder recursively and write a structured `description.md` including the contents of most files.

## Usage Overview
You can run Crawlect via the CLI with plenty of flexible options:

```bash
python3 crawlect.py --path ./my-project --output ./my-doc.md
```
Or dynamically generate unique filenames:

```bash
python3 crawlect.py --path ./my-project --output_prefix ./docs/crawl --output_suffix .md
```
You can filter files and folders:

```bash
# Exclude .png and .jpg files from listing
--excl_ext_li .png .jpg

# Include only .py and .md files for writing
--incl_ext_wr .py .md
```
You can also:

- Limit depth (`--depth 2`)
- Disable recursive crawling (`--recur no`)
- Enable the directory tree overview (`--tree yes`)
- Sanitize .env files (`--xenv yes`)

### Example Command
```bash
python3 crawlect.py \
  --path ./awesome-project \
  --output_prefix ./docs/snapshot \
  --output_suffix .md \
  --excl_ext_li .log .png .jpg \
  --incl_ext_wr .py .json \
  --tree yes \
  --xenv yes
Creates a structured markdown file (with a unique name), ignoring noisy files and including `.py` and `.md` contents.
```
### Tips

- `.env` files are *auto-sanitized* — values are replaced by `YourValueFor_<varname>`
- Inclusion rules overrule exclusion
- File name rules take precedence over extension rules

### Module Mode

You can use Crawlect as a **Python module** too:

```python
from crawlect import Crawlect

myCrawler = Crawlect(path=".", output="./project_overview.md")
myCrawler.outputService.compose()
```

## Planned Features (ideas welcome!)
- *Git* related filtering.
- *HTML* output
- *LLM* API integration.
- Optional syntax highlighting themes
- GUI launcher (who knows?)

## Architecture:

```text
                           +-----------------+
                           | User CLI        |
                           +--------+--------+
                                    |
                                    v
                           +-----------------+
                           | Crawlect        |  <== Main class
                           +--------+--------+
                                    |
          +-------------------------+-------------------------+
          |                         |                         |
          v                         v                         v
  +----------------+       +--------------- -+       +-----------------+
  |  Scan          |       | Format          |       | Output          |
  |  (List files)  |       | (Detect type &  |       | (Compose final  |
  |                |       | insert codebox) |       |  Markdown file) |
  +-------+--------+       +--------+------- +       +--------+--------+
          |                         |                         |
          v                         v                         v
    Files to list            Codebox strings         Markdown composition
       (Path)                      (MD)                     (MD)
```

- **Scan**: Crawls the directories based on inclusion/exclusion rules
- **Format**: Detects file type & builds Markdown-friendly code blocks
- **Output**: Writes everything to a nicely structured `.md` file

***"Documentation is like a love letter you write to your future self."***  
*— Damian Conway, we believe. Or some other wise code-wizard.*

## References and thanks
### Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
| language | ext1 | ext2 | ext3 | ext4 | ext5 | ext6 | ext7 | ext8 | ext9 |
|---|---|---|---|---|---|---|---|---|---|
| cucumber | .feature |  |  |  |  |  |  |  |  |
| abap | .abap |  |  |  |  |  |  |  |  |
| ada | .adb | .ads | .ada |  |  |  |  |  |  |
| ahk | .ahk | .ahkl |  |  |  |  |  |  |  |
| apacheconf | .htaccess | apache.conf | apache2.conf |  |  |  |  |  |  |
| applescript | .applescript |  |  |  |  |  |  |  |  |
| as | .as |  |  |  |  |  |  |  |  |
| as3 | .as |  |  |  |  |  |  |  |  |
| asy | .asy |  |  |  |  |  |  |  |  |
| bash | .sh | .ksh | .bash | .ebuild | .eclass |  |  |  |  |
| bat | .bat | .cmd |  |  |  |  |  |  |  |
| befunge | .befunge |  |  |  |  |  |  |  |  |
| blitzmax | .bmx |  |  |  |  |  |  |  |  |
| boo | .boo |  |  |  |  |  |  |  |  |
| brainfuck | .bf | .b |  |  |  |  |  |  |  |
| c | .c | .h |  |  |  |  |  |  |  |
| cfm | .cfm | .cfml | .cfc |  |  |  |  |  |  |
| cheetah | .tmpl | .spt |  |  |  |  |  |  |  |
| cl | .cl | .lisp | .el |  |  |  |  |  |  |
| clojure | .clj | .cljs |  |  |  |  |  |  |  |
| cmake | .cmake | CMakeLists.txt |  |  |  |  |  |  |  |
| coffeescript | .coffee |  |  |  |  |  |  |  |  |
| console | .sh-session |  |  |  |  |  |  |  |  |
| control | control |  |  |  |  |  |  |  |  |
| cpp | .cpp | .hpp | .c++ | .h++ | .cc | .hh | .cxx | .hxx | .pde |
| csharp | .cs |  |  |  |  |  |  |  |  |
| css | .css |  |  |  |  |  |  |  |  |
| cython | .pyx | .pxd | .pxi |  |  |  |  |  |  |
| d | .d | .di |  |  |  |  |  |  |  |
| delphi | .pas |  |  |  |  |  |  |  |  |
| diff | .diff | .patch |  |  |  |  |  |  |  |
| dpatch | .dpatch | .darcspatch |  |  |  |  |  |  |  |
| duel | .duel | .jbst |  |  |  |  |  |  |  |
| dylan | .dylan | .dyl |  |  |  |  |  |  |  |
| erb | .erb |  |  |  |  |  |  |  |  |
| erl | .erl-sh |  |  |  |  |  |  |  |  |
| erlang | .erl | .hrl |  |  |  |  |  |  |  |
| evoque | .evoque |  |  |  |  |  |  |  |  |
| factor | .factor |  |  |  |  |  |  |  |  |
| felix | .flx | .flxh |  |  |  |  |  |  |  |
| fortran | .f | .f90 |  |  |  |  |  |  |  |
| gas | .s | .S |  |  |  |  |  |  |  |
| genshi | .kid |  |  |  |  |  |  |  |  |
| gitignore | .gitignore |  |  |  |  |  |  |  |  |
| glsl | .vert | .frag | .geo |  |  |  |  |  |  |
| gnuplot | .plot | .plt |  |  |  |  |  |  |  |
| go | .go |  |  |  |  |  |  |  |  |
| groff | .(1234567) | .man |  |  |  |  |  |  |  |
| haml | .haml |  |  |  |  |  |  |  |  |
| haskell | .hs |  |  |  |  |  |  |  |  |
| html | .html | .htm | .xhtml | .xslt |  |  |  |  |  |
| hx | .hx |  |  |  |  |  |  |  |  |
| hybris | .hy | .hyb |  |  |  |  |  |  |  |
| ini | .ini | .cfg |  |  |  |  |  |  |  |
| io | .io |  |  |  |  |  |  |  |  |
| ioke | .ik |  |  |  |  |  |  |  |  |
| irc | .weechatlog |  |  |  |  |  |  |  |  |
| jade | .jade |  |  |  |  |  |  |  |  |
| java | .java |  |  |  |  |  |  |  |  |
| js | .js |  |  |  |  |  |  |  |  |
| jsp | .jsp |  |  |  |  |  |  |  |  |
| lhs | .lhs |  |  |  |  |  |  |  |  |
| llvm | .ll |  |  |  |  |  |  |  |  |
| logtalk | .lgt |  |  |  |  |  |  |  |  |
| lua | .lua | .wlua |  |  |  |  |  |  |  |
| make | .mak | Makefile | makefile | Makefile. | GNUmakefile |  |  |  |  |
| mako | .mao |  |  |  |  |  |  |  |  |
| maql | .maql |  |  |  |  |  |  |  |  |
| mason | .mhtml | .mc | .mi | autohandler | dhandler |  |  |  |  |
| markdown | .md |  |  |  |  |  |  |  |  |
| modelica | .mo |  |  |  |  |  |  |  |  |
| modula2 | .def | .mod |  |  |  |  |  |  |  |
| moocode | .moo |  |  |  |  |  |  |  |  |
| mupad | .mu |  |  |  |  |  |  |  |  |
| mxml | .mxml |  |  |  |  |  |  |  |  |
| myghty | .myt | autodelegate |  |  |  |  |  |  |  |
| nasm | .asm | .ASM |  |  |  |  |  |  |  |
| newspeak | .ns2 |  |  |  |  |  |  |  |  |
| objdump | .objdump |  |  |  |  |  |  |  |  |
| objectivec | .m |  |  |  |  |  |  |  |  |
| objectivej | .j |  |  |  |  |  |  |  |  |
| ocaml | .ml | .mli | .mll | .mly |  |  |  |  |  |
| ooc | .ooc |  |  |  |  |  |  |  |  |
| perl | .pl | .pm |  |  |  |  |  |  |  |
| php | .php | .php(345) |  |  |  |  |  |  |  |
| postscript | .ps | .eps |  |  |  |  |  |  |  |
| pot | .pot | .po |  |  |  |  |  |  |  |
| pov | .pov | .inc |  |  |  |  |  |  |  |
| prolog | .prolog | .pro | .pl |  |  |  |  |  |  |
| properties | .properties |  |  |  |  |  |  |  |  |
| protobuf | .proto |  |  |  |  |  |  |  |  |
| py3tb | .py3tb |  |  |  |  |  |  |  |  |
| pytb | .pytb |  |  |  |  |  |  |  |  |
| python | .py | .pyw | .sc | SConstruct | SConscript | .tac |  |  |  |
| r | .R |  |  |  |  |  |  |  |  |
| rb | .rb | .rbw | Rakefile | .rake | .gemspec | .rbx | .duby |  |  |
| rconsole | .Rout |  |  |  |  |  |  |  |  |
| rebol | .r | .r3 |  |  |  |  |  |  |  |
| redcode | .cw |  |  |  |  |  |  |  |  |
| rhtml | .rhtml |  |  |  |  |  |  |  |  |
| rst | .rst | .rest |  |  |  |  |  |  |  |
| sass | .sass |  |  |  |  |  |  |  |  |
| scala | .scala |  |  |  |  |  |  |  |  |
| scaml | .scaml |  |  |  |  |  |  |  |  |
| scheme | .scm |  |  |  |  |  |  |  |  |
| scss | .scss |  |  |  |  |  |  |  |  |
| smalltalk | .st |  |  |  |  |  |  |  |  |
| smarty | .tpl |  |  |  |  |  |  |  |  |
| sourceslist | sources.list |  |  |  |  |  |  |  |  |
| splus | .S | .R |  |  |  |  |  |  |  |
| sql | .sql |  |  |  |  |  |  |  |  |
| sqlite3 | .sqlite3-console |  |  |  |  |  |  |  |  |
| squidconf | squid.conf |  |  |  |  |  |  |  |  |
| ssp | .ssp |  |  |  |  |  |  |  |  |
| tcl | .tcl |  |  |  |  |  |  |  |  |
| tcsh | .tcsh | .csh |  |  |  |  |  |  |  |
| tex | .tex | .aux | .toc |  |  |  |  |  |  |
| text | .txt |  |  |  |  |  |  |  |  |
| v | .v | .sv |  |  |  |  |  |  |  |
| vala | .vala | .vapi |  |  |  |  |  |  |  |
| vbnet | .vb | .bas |  |  |  |  |  |  |  |
| velocity | .vm | .fhtml |  |  |  |  |  |  |  |
| vim | .vim | .vimrc |  |  |  |  |  |  |  |
| xml | .xml | .xsl | .rss | .xslt | .xsd | .wsdl |  |  |  |
| xquery | .xqy | .xquery |  |  |  |  |  |  |  |
| xslt | .xsl | .xslt |  |  |  |  |  |  |  |
| yaml | .yaml | .yml |  |  |  |  |  |  |  |

### Arpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
````````````
### **[format.py](format.py)**  
`format.py`
```python
import json

from pathlib import Path

class Format:
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox

    """

    def __init__(self):

        try:

            with open("languages.json", "rt") as f:
                self.languages = json.load(f)
        except:
            print("Tables de mapage introuvables")

    def insertCodebox(self, file):
        """
        cette méthode prends en entrée un chemin de fichier avec son extention fourni par searchType()
        et retourne une variable string avec tous le code corresponding dans un codbox
        """

        extention = self.searchType(file)
        if extention == None:
            return None
        bloc = "`"
        with open(file, "rt") as f:
            code = f.read()

        # sources des commandes trouvées pour la gestion des textes : https://www.w3schools.com/python/python_ref_string.asp
        # Afficher un .env n'est pas souhaitable il faut masquer les valeurs
        if file.name == ".env":
            contenu = ""
            for ligne in code.splitlines():
                newlinge = ligne.lstrip(" ")

                # remplacement des valeurs des variables d'environnement par une valeur générique
                if newlinge and newlinge[0] != "#":
                    newlinge = newlinge.split("=")
                    variable_env = newlinge[0]
                    newlinge[1] = f"YourValueFor_{variable_env.lower()}"
                    newlinge = "=".join(newlinge)

                contenu += newlinge + "\n"
            # print(contenu)
            return f"{3*bloc}{extention}\n{contenu}\n{3*bloc}"

        # vérifie que l'extention est pas du markdown car ce type de fichier dispose de codebox
        elif extention != "markdown":
            res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
            # print(res)
            # print("")
            return res

        else:
            counter = 1
            maxrep = 1

            for l in range(1, len(code) - 1):
                if code[l] == code[l + 1] == "`":
                    counter += 1

                else:
                    if counter > maxrep:
                        maxrep = counter
                        counter = 1

            if counter > maxrep:
                maxrep = counter

            if maxrep >= 3:
                maxrep += 1
                res = f"{maxrep*bloc}{extention}\n{code}\n{maxrep*bloc}"
                # print(res)
                # print("")
                return res

            else:
                res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
                # print(res)
                # print("")
                return res
            

    def searchType(self, file):
        """
        Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox
        """

        # recherche sur le nom de fichier
        if file.name in self.languages:
            # print(f"voici le fichier trouvée : {self.languages[file.name]}")
            return self.languages[file.name]

        elif file.suffix in self.languages:
            # print(f"voici l'extention trouvée : {self.languages[file.suffix]}")
            return self.languages[file.suffix]

        else:
            # print(f"fichier introuvés pour {file}")
            return None
        

    def makeTreeMd(self, chemin,  chemin_ignorer= [], deep = 20, level=0, racine = True):
        if level >= deep + 1 :
            return ""
        #print(chemin_ignorer)
        
        if chemin.name in chemin_ignorer:
            return ""
        
        if chemin.is_file in chemin_ignorer:
            return ""
        
        tree = ""
        indentation = "    "*level

        #print(f"{indentation}|__ {chemin.name}{fin}")
        if level == 0 and racine:
            tree += f"- **{chemin.resolve().name}/**  \n"
        elif level>0:
            if chemin.is_file():
                tree += f"{indentation}- [{chemin.name}](#{chemin.stem.replace(".","") + chemin.suffix[1:]})  \n"
            if chemin.is_dir():
                tree += f"{indentation}- `{chemin.name}/`  \n"

        if chemin.is_dir():
            fichier_iterables = chemin.iterdir()
            fichier_liste = []
            dossier_liste = []
            for item in fichier_iterables:
                if item.is_file():
                    fichier_liste.append(item)
                if item.is_dir():
                    dossier_liste.append(item)
            
            dossiers = sorted(dossier_liste)
            fichiers = sorted(fichier_liste)
            
            for fichier in fichiers:
                try:
                #appel récursif 
                    tree += self.makeTreeMd(fichier, chemin_ignorer,deep,level +1, False)
                except PermissionError:
                    tree += ""
            for dossier in dossiers:
                try:
                    tree += self.makeTreeMd(dossier, chemin_ignorer,deep, level +1, False)

                except PermissionError:
                    tree += ""
        #print(tree)
        return tree

        




```
### **[misc.xml](.idea/misc.xml)**  
`.idea/misc.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Black">
    <option name="sdkName" value="Python 3.12" />
  </component>
  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12" project-jdk-type="Python SDK" />
</project>
```
### **crawlect.iml**  
`.idea/crawlect.iml`

### **[profiles_settings.xml](.idea/inspectionProfiles/profiles_settings.xml)**  
`.idea/inspectionProfiles/profiles_settings.xml`
```xml
<component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>
```
### **[modules.xml](.idea/modules.xml)**  
`.idea/modules.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/crawlect.iml" filepath="$PROJECT_DIR$/.idea/crawlect.iml" />
    </modules>
  </component>
</project>
```
### **[workspace.xml](.idea/workspace.xml)**  
`.idea/workspace.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="SELECTIVE" />
  </component>
  <component name="ChangeListManager">
    <list default="true" id="ad321e4d-22a0-440b-b0d9-c7a852fce0b5" name="Changes" comment="">
      <change afterPath="$PROJECT_DIR$/languages.json" afterDir="false" />
      <change beforePath="$PROJECT_DIR$/crawlect.py" beforeDir="false" afterPath="$PROJECT_DIR$/crawlect.py" afterDir="false" />
    </list>
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="Git.Settings">
    <option name="RECENT_GIT_ROOT_PATH" value="$PROJECT_DIR$" />
  </component>
  <component name="GitHubPullRequestSearchHistory">{
  &quot;lastFilter&quot;: {
    &quot;state&quot;: &quot;OPEN&quot;,
    &quot;assignee&quot;: &quot;Alex141298&quot;
  }
}</component>
  <component name="GithubPullRequestsUISettings">{
  &quot;selectedUrlAndAccountId&quot;: {
    &quot;url&quot;: &quot;git@github.com:yvesguillo/crawlect.git&quot;,
    &quot;accountId&quot;: &quot;2343b8f7-62f1-41aa-8154-f61445de79cb&quot;
  }
}</component>
  <component name="ProjectColorInfo">{
  &quot;associatedIndex&quot;: 3
}</component>
  <component name="ProjectId" id="2uw50MjxGABUJIjb0FJnelAcmgg" />
  <component name="ProjectViewState">
    <option name="hideEmptyMiddlePackages" value="true" />
    <option name="showLibraryContents" value="true" />
  </component>
  <component name="PropertiesComponent"><![CDATA[{
  "keyToString": {
    "Python.crawlect.executor": "Run",
    "RunOnceActivity.ShowReadmeOnStart": "true",
    "RunOnceActivity.git.unshallow": "true",
    "git-widget-placeholder": "main",
    "last_opened_file_path": "/home/alexandre/Documents/MAS_RAD/01_IDD/02_Developpement_POO_python/07_POO/02_Exercices "
  }
}]]></component>
  <component name="RunManager">
    <configuration name="crawlect" type="PythonConfigurationType" factoryName="Python" temporary="true" nameIsGenerated="true">
      <module name="crawlect" />
      <option name="ENV_FILES" value="" />
      <option name="INTERPRETER_OPTIONS" value="" />
      <option name="PARENT_ENVS" value="true" />
      <envs>
        <env name="PYTHONUNBUFFERED" value="1" />
      </envs>
      <option name="SDK_HOME" value="" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="IS_MODULE_SDK" value="true" />
      <option name="ADD_CONTENT_ROOTS" value="true" />
      <option name="ADD_SOURCE_ROOTS" value="true" />
      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/crawlect.py" />
      <option name="PARAMETERS" value="" />
      <option name="SHOW_COMMAND_LINE" value="false" />
      <option name="EMULATE_TERMINAL" value="false" />
      <option name="MODULE_MODE" value="false" />
      <option name="REDIRECT_INPUT" value="false" />
      <option name="INPUT_FILE" value="" />
      <method v="2" />
    </configuration>
    <recent_temporary>
      <list>
        <item itemvalue="Python.crawlect" />
      </list>
    </recent_temporary>
  </component>
  <component name="SharedIndexes">
    <attachedChunks>
      <set>
        <option value="bundled-python-sdk-14705d77f0bb-aa17d162503b-com.jetbrains.pycharm.community.sharedIndexes.bundled-PC-243.25659.43" />
      </set>
    </attachedChunks>
  </component>
  <component name="SpellCheckerSettings" RuntimeDictionaries="0" Folders="0" CustomDictionaries="0" DefaultDictionary="application-level" UseSingleDictionary="true" transferred="true" />
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="ad321e4d-22a0-440b-b0d9-c7a852fce0b5" name="Changes" comment="" />
      <created>1743146571563</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1743146571563</updated>
    </task>
    <servers />
  </component>
</project>
```
### **[.gitignore](.idea/.gitignore)**  
`.idea/.gitignore`
```gitignore
# Default ignored files
/shelf/
/workspace.xml

```
### **[vcs.xml](.idea/vcs.xml)**  
`.idea/vcs.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="" vcs="Git" />
  </component>
</project>
```
### **[.gitignore](.gitignore)**  
`.gitignore`
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

```
### **[note.md](note.md)**  
`note.md`
```markdown
lancer crawlect sans etre dans dans le dossier ou le script se situe 

uv add --script 

```
### **[languages.json](languages.json)**  
`languages.json`
```json

{
  ".abap": "abap",
  ".ada": "ada",
  ".adb": "ada",
  ".ads": "ada",
  ".ahk": "ahk",
  ".ahkl": "ahk",
  ".htaccess": "apacheconf",
  "apache.conf": "apacheconf",
  "apache2.conf": "apacheconf",
  ".applescript": "applescript",
  ".as": "as",
  ".asy": "asy",
  ".bash": "bash",
  ".ebuild": "bash",
  ".eclass": "bash",
  ".env.example": "bash",
  ".env.local": "bash",
  ".env": "bash",
  ".ksh": "bash",
  ".sh": "bash",
  ".bat": "bat",
  ".cmd": "bat",
  ".befunge": "befunge",
  ".bmx": "blitzmax",
  ".boo": "boo",
  ".b": "brainfuck",
  ".bf": "brainfuck",
  ".c": "c", ".h": "c",
  ".cfc": "cfm",
  ".cfm": "cfm",
  ".cfml": "cfm",
  ".spt": "cheetah",
  ".tmpl": "cheetah",
  ".cl": "cl",
  ".el": "cl",
  ".lisp": "cl",
  ".clj": "clojure",
  ".cljs": "clojure",
  ".cmake": "cmake",
  "CMakeLists.txt": "cmake",
  ".coffee": "coffeescript",
  ".sh-session": "console",
  "control": "control",
  ".c++": "cpp",
  ".cc": "cpp",
  ".cpp": "cpp",
  ".cxx": "cpp",
  ".h++": "cpp",
  ".hh": "cpp",
  ".hpp": "cpp",
  ".hxx": "cpp",
  ".pde": "cpp",
  ".cs": "csharp",
  ".css": "css",
  ".feature": "cucumber",
  ".pxd": "cython",
  ".pxi": "cython",
  ".pyx": "cython",
  ".d": "d",
  ".di": "d",
  ".pas": "delphi",
  ".diff": "diff",
  ".patch": "diff",
  "Dockerfile.": "dockerfile",
  "Dockerfile": "dockerfile",
  ".darcspatch": "dpatch",
  ".dpatch": "dpatch",
  ".duel": "duel",
  ".jbst": "duel",
  ".dyl": "dylan",
  ".dylan": "dylan",
  ".erb": "erb",
  ".erl-sh": "erl",
  ".erl": "erlang",
  ".hrl": "erlang",
  ".evoque": "evoque",
  ".factor": "factor",
  ".flx": "felix",
  ".flxh": "felix",
  ".f": "fortran",
  ".f90": "fortran",
  ".s": "gas",
  ".kid": "genshi",
  ".gitignore": "gitignore",
  ".frag": "glsl",
  ".geo": "glsl",
  ".vert": "glsl",
  ".plot": "gnuplot",
  ".plt": "gnuplot",
  ".go": "go",
  ".(1234567)": "groff",
  ".man": "groff",
  ".haml": "haml",
  ".hs": "haskell",
  ".htm": "html",
  ".html": "html",
  ".xhtml": "html",
  ".hx": "hx",
  ".hy": "hybris",
  ".hyb": "hybris",
  ".cfg": "ini",
  ".conf": "ini",
  ".editorconfig": "ini",
  ".flake8": "ini",
  ".ini": "ini",
  ".npmrc": "ini",
  ".io": "io",
  ".ik": "ioke",
  ".weechatlog": "irc",
  ".jade": "jade",
  ".java": "java",
  ".js": "js",
  ".babelrc": "json",
  ".eslintrc": "json",
  ".json": "json",
  ".json5": "json",
  ".prettierrc": "json",
  ".jsp": "jsp",
  ".lhs": "lhs",
  ".ll": "llvm",
  ".lgt": "logtalk",
  ".lua": "lua",
  ".wlua": "lua",
  ".mak": "make",
  "GNUmakefile": "make",
  "Makefile.": "make",
  "Makefile": "make",
  "makefile": "make",
  ".mao": "mako",
  ".maql": "maql",
  ".md": "markdown",
  ".mc": "mason",
  ".mhtml": "mason",
  ".mi": "mason",
  "autohandler": "mason",
  "dhandler": "mason",
  ".mo": "modelica",
  ".def": "modula2",
  ".mod": "modula2",
  ".moo": "moocode",
  ".mu": "mupad",
  ".mxml": "mxml",
  ".myt": "myghty",
  "autodelegate": "myghty",
  ".asm": "nasm",
  ".ASM": "nasm",
  ".ns2": "newspeak",
  ".objdump": "objdump",
  ".m": "objectivec",
  ".j": "objectivej",
  ".ml": "ocaml",
  ".mli": "ocaml",
  ".mll": "ocaml",
  ".mly": "ocaml",
  ".ooc": "ooc",
  ".pl": "perl",
  ".pm": "perl",
  ".php(345)": "php",
  ".php": "php",
  ".eps": "postscript",
  ".ps": "postscript",
  ".po": "pot",
  ".pot": "pot",
  ".inc": "pov",
  ".pov": "pov",
  ".pro": "prolog",
  ".prolog": "prolog",
  ".properties": "properties",
  ".proto": "protobuf",
  ".py3tb": "py3tb",
  ".pytb": "pytb",
  ".py": "python",
  ".pyw": "python",
  ".sc": "python",
  ".tac": "python",
  "SConscript": "python",
  "SConstruct": "python",
  ".R": "r",
  ".duby": "rb",
  ".gemspec": "rb",
  ".rake": "rb",
  ".rb": "rb",
  ".rbw": "rb",
  ".rbx": "rb",
  "Rakefile": "rb",
  ".Rout": "rconsole",
  ".r": "rebol",
  ".r3": "rebol",
  ".cw": "redcode",
  ".rhtml": "rhtml",
  ".rest": "rst",
  ".rst": "rst",
  "Vagrantfile": "ruby",
  ".sass": "sass",
  ".scala": "scala",
  ".scaml": "scaml",
  ".scm": "scheme",
  ".scss": "scss",
  ".st": "smalltalk",
  ".tpl": "smarty",
  "sources.list": "sourceslist",
  ".S": "splus",
  ".sql": "sql",
  ".sqlite3-console": "sqlite3",
  "squid.conf": "squidconf",
  ".ssp": "ssp",
  ".tcl": "tcl",
  ".csh": "tcsh",
  ".tcsh": "tcsh",
  ".aux": "tex",
  ".tex": "tex",
  ".toc": "tex",
  ".log": "text",
  ".txt": "text",
  "requirements.txt": "text",
  ".toml": "toml",
  "Pipfile.lock": "toml",
  "Pipfile": "toml",
  "pyproject.toml": "toml",
  ".sv": "v",
  ".v": "v",
  ".vala": "vala",
  ".vapi": "vala",
  ".bas": "vbnet",
  ".vb": "vbnet",
  ".fhtml": "velocity",
  ".vm": "velocity",
  ".vim": "vim",
  ".vimrc": "vim",
  ".rss": "xml",
  ".wsdl": "xml",
  ".xml": "xml",
  ".xsd": "xml",
  ".xslt": "xml",
  ".xquery": "xquery",
  ".xqy": "xquery",
  ".xsl": "xslt",
  ".yaml": "yaml",
  ".yarnrc": "yaml",
  ".yml": "yaml"
}
```
### **[scan.py](scan.py)**  
`scan.py`
```python
#! /usr/bin/env python3

from pathlib import Path

class Scan:
    """
    Scan class contains Crawlect directories tree scan utilities.
    It require and only accept one instance of Crawlect as argument.
    """

    def __init__(self, crawler = None):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler

    def listFilesIn(self, path = None, depth = None, files = None):
        """Append all eligible paths from `crawler.path` as Path object in a list and return it."""
        if files is None:
            files = []

        if depth is None:
            depth = self.crawler.depth

        if path is None:
            path = self.crawler.pathObj

        for candidatePath in path.iterdir():
            try:
                if candidatePath.is_file() and self.isFileToInclude(candidatePath):
                    files.append(candidatePath)
                elif candidatePath.is_dir() and self.crawler.recur and depth >= 1 and self.isDirToInclude(candidatePath):
                    files.append(candidatePath)
                    self.listFilesIn(path = candidatePath, depth = depth-1, files = files)
            except PermissionError as err:
                print(f"\n!! {type(err) .__name__} :\n{type(self) .__name__} Could not list path {repr(candidatePath)}: {err} ")
        return files

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """

        # Always exclude output file.
        if str(path) == self.crawler.output:
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_li == () and self.crawler.excl_fil_li == () and self.crawler.incl_ext_li == () and self.crawler.incl_fil_li == ():
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_li:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_li and path.name not in self.crawler.excl_fil_li:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_li and path.name not in self.crawler.incl_fil_li:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_li:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_li != () or self.crawler.incl_fil_li != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isDirToInclude(self, path):
        """
        Filter directory `path` according to filtering rules.
        All directories pass if there are no rules.
        Inclusion overrules exclusion.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_dir_li == () and self.crawler.incl_dir_li == ():
            return True

        # Is forcibly included:
        if path.name in self.crawler.incl_dir_li:
            return True

        # Is forcibly excluded:
        if path.name in self.crawler.excl_dir_li:
            return False

        # Is neither forcibly included or excluded but a directory inclusion is overruling:
        if self.crawler.incl_dir_li != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
### **[.env](.env)**  
`.env`
```bash
# variables d'environnement mysql
MYSQL_ROOT_PASSWORD=YourValueFor_mysql_root_password
MYSQL_USER=YourValueFor_mysql_user
MYSQL_PASSWORD=YourValueFor_mysql_password
MYSQL_DATABASE=YourValueFor_mysql_database

```

``````````````````````
<h3 id="6">crawlect.py](crawlect.py)</h3> 
`crawlect.py`
```python
#! /usr/bin/env python3

from pathlib import Path
from math import inf

# Custom modules.
from scan import Scan
from format import Format
from output import Output

class Crawlect:
    """
    Client Crawlect class.
    Crawlect is a module intended to describe files from a given path and transcribe and save these into a single markdown file.
    """

    def __init__(self, path = None, output = None, output_prefix = None, output_suffix = None, recur = True, depth = inf, excl_ext_li = (), excl_dir_li = (), excl_fil_li = (), excl_ext_wr = (), excl_dir_wr = (), excl_fil_wr = (), incl_ext_li = (), incl_dir_li = (), incl_fil_li = (), incl_ext_wr = (), incl_dir_wr = (), incl_fil_wr = (), xenv = True, tree = True):

        # Store the class arguments for __repr__.
        self.args = dict()

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

        # Files and xtensions inclusion/exclusions parameters.
        self.excl_ext_li = excl_ext_li
        self.args["excl_ext_li"] = self.excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.args["excl_dir_li"] = self.excl_dir_li
        self.excl_fil_li = excl_fil_li
        self.args["excl_fil_li"] = self.excl_fil_li
        self.excl_ext_wr = excl_ext_wr
        self.args["excl_ext_wr"] = self.excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.args["excl_dir_wr"] = self.excl_dir_wr
        self.excl_fil_wr = excl_fil_wr
        self.args["excl_fil_wr"] = self.excl_fil_wr
        self.incl_ext_li = incl_ext_li
        self.args["incl_ext_li"] = self.incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.args["incl_dir_li"] = self.incl_dir_li
        self.incl_fil_li = incl_fil_li
        self.args["incl_fil_li"] = self.incl_fil_li
        self.incl_ext_wr = incl_ext_wr
        self.args["incl_ext_wr"] = self.incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.args["incl_dir_wr"] = self.incl_dir_wr
        self.incl_fil_wr = incl_fil_wr
        self.args["incl_fil_wr"] = self.incl_fil_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denied by default.
        self.writeRight = "x"

        # Validate attributes parameters.
        self.validate()

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

        try:
            self.scanService = Scan(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Scan service.")
            raise

        try:
            self.formatService = Format() # Format does not take Crawlect instance as parameter.
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Format service.")
            raise

        try:
            self.outputService = Output(self)
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and initiate its Output service.")
            raise

        try:
            self.files = self.scanService.listFilesIn()
        except:
            print(f"Error: on {type(self).__name__}:\ncould not refresh and proceed to paths listing.")
            raise

    # To be enhanced. State patern?
    def validate(self):
        """Validate attributes and regenerate dynamic attributes."""

        # Max depth adaptation if recur is False.
        if not self.recur:
            self.depth = 1

        # Interactive mode.
        if __name__ == "__main__":

            while self.path is None:
                self.path = input(f"\n# Missing argument #\n{type(self).__name__} require a path to crawl. Please enter the desired path (e.g.: '.') or [Ctrl]+[C] then [Enter] to abort.\n")

            while not Path(self.path).exists():
                self.path = input(f"\n# Path error #\n{type(self).__name__} could not find {repr(self.path)}, please enter the path to crawl.\n")

            while self.output is None and self.output_prefix is None:
                print(f"\n# Missing argument #\n{type(self).__name__} require an output file-name for static output file-name (e.g.: './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: './descript' as prefix, and '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'")
                while True:
                    _ = input("Please choose between 'static' and 'unique', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
                    if _ == "static":
                        while self.output is None or not self.output:
                            self.output = input("Please enter a static output file-name, e.g.: './output.md' or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    elif _ == "unique":
                        while self.output_prefix is None or not self.output_prefix:
                            self.output_prefix = input("Please enter a prefix, e.g.: './output' or [Ctrl]+[C] then [Enter] to abort.\n")
                        while self.output_suffix is None:
                            self.output_suffix = input("Please enter a suffix, e.g.: '.md' (suffix can be empty) or [Ctrl]+[C] then [Enter] to abort.\n")
                        break
                    else:
                        continue

            if self.output is not None:
                if Path(self.output).exists():
                        print(f"\n# File overwrite #\n{type(self).__name__} is about to overwrite {repr(self.output)}. Its content will be lost!")
                        while True:
                            _ = input("Please choose between 'proceed' and 'change', or [Ctrl]+[C] then [Enter] to abort.\n").lower()
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
                    raise IOError(f"\n# Permission error #\n{type(self).__name__} do not allow file {repr(self.output)} to be overwrited in module mode. Please errase the file first if you want to keep this output path.")

            validationMessage = ""
            if self.path is None:
                validationMessage += "- A path to crawl, e.g.: path = '.'\n"
            elif not Path(self.path).exists():
                validationMessage += f"A valid path to crawl, {self.path} cannot be found.\n"
            if self.output is None and self.output_prefix is None:
                validationMessage += "- An output file-name for static output file-name (e.g.: --output = './description.md')\nOR\nan output prefix and output suffix for unique output file-name (e.g.: --output_prefix = './descript', --output_suffix = '.md' as suffix), this will create a path similar to: './descript-202506041010-g5ef9h.md'\n"
            if validationMessage:
                raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires:\n{validationMessage}Got: {self}")

    def getTitle(self):
        return self.title

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
            epilog = "Filtering rules allow you to forcibly include or exclude certain directories, files names or file extensions. All files will be listed if there are no rules. Inclusion overrules exclusion on same caracteristics and file-name rules takes precedence against extension rules."
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
            help = "Output markdown digest file prefix ('description' by default) associated with --output_suffix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-os", "--output_suffix", "--output_file_suffix",
            type = str,
            default = ".md",
            
            help = "Output markdown digest file prefix ('.md' by default) associated with --output_prefix can be use as an alternative to '--output' argument to generate a unique file-name (e.g.: --output_prefix = './descript', output_suffix = '.md' will create './descript-202506041010-g5ef9h.md').")

        parser.add_argument(
            "-r", "--recur", "--recursive_crawling",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Enable recursive crawling (default is True).")

        parser.add_argument(
            "-d", "--depth", "--recursive_crawling_depth",
            type = int,
            default = inf,
            help = "Scan depth limit (default is infinite).")

        parser.add_argument(
            "-xel", "--excl_ext_li", "--excluded_xtensions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_xtensions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_xtensions_from_listing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include in listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_from_listing",
            nargs = "*",
            default = (),
            help = "List of directories to include in listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_from_listing",
            nargs = "*",
            default = (),
            help = "List of files to include in listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_xtensions_from_writing",
            nargs = "*",
            default = (),
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_from_writing",
            nargs = "*",
            default = (),
            help = "List of directories to include for writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_from_writing",
            nargs = "*",
            default = (),
            help = "List of files to include for writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xen", "--xenv", "--randomize_env_variables",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Randomize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(path = args.path, output = args.output, output_prefix = args.output_prefix, output_suffix = args.output_suffix, recur = args.recur, depth = args.depth, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_li = args.excl_fil_li, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, excl_fil_wr = args.excl_fil_wr, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_li = args.incl_fil_li, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, incl_fil_wr = args.incl_fil_wr, xenv = args.xenv, tree = args.tree)

        # Launch output file composition
        crawlect.outputService.compose()

        # Confirm.
        print(f"\n{type(crawlect.outputService).__name__} processed {repr(crawlect.getTitle())} and stored description in {repr(crawlect.outputService.currentOutputName)}.")

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)
```
<h3 id="7">README.md](README.md)</h3> 
`README.md`
````````````markdown
# Crawlect – Crawl, Collect & Document Your Codebase in Markdown

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

## Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Traversing your project directory (recursively if needed),
- Filtering files and directories with powerful inclusion/exclusion rules,
- Masking sensitive data (like `.env` values),
- Embedding file contents in Markdown-formatted code blocks,
- Automatically generating a well-organized, shareable `.md` file.

## Use cases

- Quickly understand an unfamiliar codebase
- Auto-document your projects
- Share code context with collaborators (or *LLM*!)
- Safely include `.env` files without leaking sensitive values

***Think of Crawlect as your markdown-minion — obedient, efficient, and allergic to messy folders.***

## Crawlect – User Guide
**Crawlect**, the tool that turns your project folder into a beautifully structured Markdown digest — effortlessly.

## Installation
Crawlect currently runs as a standalone module. To use it, simply clone the repo or copy the files:

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
python3 crawlect.py
```
*(Packaging for pip? Let us know. We'll help you make it pip-installable!)*

## Quick Start
Generate a Markdown description of the current directory:

```bash
python3 crawlect.py -p . -o ./description.md
```
This will scan the current folder recursively and write a structured `description.md` including the contents of most files.

## Usage Overview
You can run Crawlect via the CLI with plenty of flexible options:

```bash
python3 crawlect.py --path ./my-project --output ./my-doc.md
```
Or dynamically generate unique filenames:

```bash
python3 crawlect.py --path ./my-project --output_prefix ./docs/crawl --output_suffix .md
```
You can filter files and folders:

```bash
# Exclude .png and .jpg files from listing
--excl_ext_li .png .jpg

# Include only .py and .md files for writing
--incl_ext_wr .py .md
```
You can also:

- Limit depth (`--depth 2`)
- Disable recursive crawling (`--recur no`)
- Enable the directory tree overview (`--tree yes`)
- Sanitize .env files (`--xenv yes`)

### Example Command
```bash
python3 crawlect.py \
  --path ./awesome-project \
  --output_prefix ./docs/snapshot \
  --output_suffix .md \
  --excl_ext_li .log .png .jpg \
  --incl_ext_wr .py .json \
  --tree yes \
  --xenv yes
Creates a structured markdown file (with a unique name), ignoring noisy files and including `.py` and `.md` contents.
```
### Tips

- `.env` files are *auto-sanitized* — values are replaced by `YourValueFor_<varname>`
- Inclusion rules overrule exclusion
- File name rules take precedence over extension rules

### Module Mode

You can use Crawlect as a **Python module** too:

```python
from crawlect import Crawlect

myCrawler = Crawlect(path=".", output="./project_overview.md")
myCrawler.outputService.compose()
```

## Planned Features (ideas welcome!)
- *Git* related filtering.
- *HTML* output
- *LLM* API integration.
- Optional syntax highlighting themes
- GUI launcher (who knows?)

## Architecture:

```text
                           +-----------------+
                           | User CLI        |
                           +--------+--------+
                                    |
                                    v
                           +-----------------+
                           | Crawlect        |  <== Main class
                           +--------+--------+
                                    |
          +-------------------------+-------------------------+
          |                         |                         |
          v                         v                         v
  +----------------+       +--------------- -+       +-----------------+
  |  Scan          |       | Format          |       | Output          |
  |  (List files)  |       | (Detect type &  |       | (Compose final  |
  |                |       | insert codebox) |       |  Markdown file) |
  +-------+--------+       +--------+------- +       +--------+--------+
          |                         |                         |
          v                         v                         v
    Files to list            Codebox strings         Markdown composition
       (Path)                      (MD)                     (MD)
```

- **Scan**: Crawls the directories based on inclusion/exclusion rules
- **Format**: Detects file type & builds Markdown-friendly code blocks
- **Output**: Writes everything to a nicely structured `.md` file

***"Documentation is like a love letter you write to your future self."***  
*— Damian Conway, we believe. Or some other wise code-wizard.*

## References and thanks
### Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
| language | ext1 | ext2 | ext3 | ext4 | ext5 | ext6 | ext7 | ext8 | ext9 |
|---|---|---|---|---|---|---|---|---|---|
| cucumber | .feature |  |  |  |  |  |  |  |  |
| abap | .abap |  |  |  |  |  |  |  |  |
| ada | .adb | .ads | .ada |  |  |  |  |  |  |
| ahk | .ahk | .ahkl |  |  |  |  |  |  |  |
| apacheconf | .htaccess | apache.conf | apache2.conf |  |  |  |  |  |  |
| applescript | .applescript |  |  |  |  |  |  |  |  |
| as | .as |  |  |  |  |  |  |  |  |
| as3 | .as |  |  |  |  |  |  |  |  |
| asy | .asy |  |  |  |  |  |  |  |  |
| bash | .sh | .ksh | .bash | .ebuild | .eclass |  |  |  |  |
| bat | .bat | .cmd |  |  |  |  |  |  |  |
| befunge | .befunge |  |  |  |  |  |  |  |  |
| blitzmax | .bmx |  |  |  |  |  |  |  |  |
| boo | .boo |  |  |  |  |  |  |  |  |
| brainfuck | .bf | .b |  |  |  |  |  |  |  |
| c | .c | .h |  |  |  |  |  |  |  |
| cfm | .cfm | .cfml | .cfc |  |  |  |  |  |  |
| cheetah | .tmpl | .spt |  |  |  |  |  |  |  |
| cl | .cl | .lisp | .el |  |  |  |  |  |  |
| clojure | .clj | .cljs |  |  |  |  |  |  |  |
| cmake | .cmake | CMakeLists.txt |  |  |  |  |  |  |  |
| coffeescript | .coffee |  |  |  |  |  |  |  |  |
| console | .sh-session |  |  |  |  |  |  |  |  |
| control | control |  |  |  |  |  |  |  |  |
| cpp | .cpp | .hpp | .c++ | .h++ | .cc | .hh | .cxx | .hxx | .pde |
| csharp | .cs |  |  |  |  |  |  |  |  |
| css | .css |  |  |  |  |  |  |  |  |
| cython | .pyx | .pxd | .pxi |  |  |  |  |  |  |
| d | .d | .di |  |  |  |  |  |  |  |
| delphi | .pas |  |  |  |  |  |  |  |  |
| diff | .diff | .patch |  |  |  |  |  |  |  |
| dpatch | .dpatch | .darcspatch |  |  |  |  |  |  |  |
| duel | .duel | .jbst |  |  |  |  |  |  |  |
| dylan | .dylan | .dyl |  |  |  |  |  |  |  |
| erb | .erb |  |  |  |  |  |  |  |  |
| erl | .erl-sh |  |  |  |  |  |  |  |  |
| erlang | .erl | .hrl |  |  |  |  |  |  |  |
| evoque | .evoque |  |  |  |  |  |  |  |  |
| factor | .factor |  |  |  |  |  |  |  |  |
| felix | .flx | .flxh |  |  |  |  |  |  |  |
| fortran | .f | .f90 |  |  |  |  |  |  |  |
| gas | .s | .S |  |  |  |  |  |  |  |
| genshi | .kid |  |  |  |  |  |  |  |  |
| gitignore | .gitignore |  |  |  |  |  |  |  |  |
| glsl | .vert | .frag | .geo |  |  |  |  |  |  |
| gnuplot | .plot | .plt |  |  |  |  |  |  |  |
| go | .go |  |  |  |  |  |  |  |  |
| groff | .(1234567) | .man |  |  |  |  |  |  |  |
| haml | .haml |  |  |  |  |  |  |  |  |
| haskell | .hs |  |  |  |  |  |  |  |  |
| html | .html | .htm | .xhtml | .xslt |  |  |  |  |  |
| hx | .hx |  |  |  |  |  |  |  |  |
| hybris | .hy | .hyb |  |  |  |  |  |  |  |
| ini | .ini | .cfg |  |  |  |  |  |  |  |
| io | .io |  |  |  |  |  |  |  |  |
| ioke | .ik |  |  |  |  |  |  |  |  |
| irc | .weechatlog |  |  |  |  |  |  |  |  |
| jade | .jade |  |  |  |  |  |  |  |  |
| java | .java |  |  |  |  |  |  |  |  |
| js | .js |  |  |  |  |  |  |  |  |
| jsp | .jsp |  |  |  |  |  |  |  |  |
| lhs | .lhs |  |  |  |  |  |  |  |  |
| llvm | .ll |  |  |  |  |  |  |  |  |
| logtalk | .lgt |  |  |  |  |  |  |  |  |
| lua | .lua | .wlua |  |  |  |  |  |  |  |
| make | .mak | Makefile | makefile | Makefile. | GNUmakefile |  |  |  |  |
| mako | .mao |  |  |  |  |  |  |  |  |
| maql | .maql |  |  |  |  |  |  |  |  |
| mason | .mhtml | .mc | .mi | autohandler | dhandler |  |  |  |  |
| markdown | .md |  |  |  |  |  |  |  |  |
| modelica | .mo |  |  |  |  |  |  |  |  |
| modula2 | .def | .mod |  |  |  |  |  |  |  |
| moocode | .moo |  |  |  |  |  |  |  |  |
| mupad | .mu |  |  |  |  |  |  |  |  |
| mxml | .mxml |  |  |  |  |  |  |  |  |
| myghty | .myt | autodelegate |  |  |  |  |  |  |  |
| nasm | .asm | .ASM |  |  |  |  |  |  |  |
| newspeak | .ns2 |  |  |  |  |  |  |  |  |
| objdump | .objdump |  |  |  |  |  |  |  |  |
| objectivec | .m |  |  |  |  |  |  |  |  |
| objectivej | .j |  |  |  |  |  |  |  |  |
| ocaml | .ml | .mli | .mll | .mly |  |  |  |  |  |
| ooc | .ooc |  |  |  |  |  |  |  |  |
| perl | .pl | .pm |  |  |  |  |  |  |  |
| php | .php | .php(345) |  |  |  |  |  |  |  |
| postscript | .ps | .eps |  |  |  |  |  |  |  |
| pot | .pot | .po |  |  |  |  |  |  |  |
| pov | .pov | .inc |  |  |  |  |  |  |  |
| prolog | .prolog | .pro | .pl |  |  |  |  |  |  |
| properties | .properties |  |  |  |  |  |  |  |  |
| protobuf | .proto |  |  |  |  |  |  |  |  |
| py3tb | .py3tb |  |  |  |  |  |  |  |  |
| pytb | .pytb |  |  |  |  |  |  |  |  |
| python | .py | .pyw | .sc | SConstruct | SConscript | .tac |  |  |  |
| r | .R |  |  |  |  |  |  |  |  |
| rb | .rb | .rbw | Rakefile | .rake | .gemspec | .rbx | .duby |  |  |
| rconsole | .Rout |  |  |  |  |  |  |  |  |
| rebol | .r | .r3 |  |  |  |  |  |  |  |
| redcode | .cw |  |  |  |  |  |  |  |  |
| rhtml | .rhtml |  |  |  |  |  |  |  |  |
| rst | .rst | .rest |  |  |  |  |  |  |  |
| sass | .sass |  |  |  |  |  |  |  |  |
| scala | .scala |  |  |  |  |  |  |  |  |
| scaml | .scaml |  |  |  |  |  |  |  |  |
| scheme | .scm |  |  |  |  |  |  |  |  |
| scss | .scss |  |  |  |  |  |  |  |  |
| smalltalk | .st |  |  |  |  |  |  |  |  |
| smarty | .tpl |  |  |  |  |  |  |  |  |
| sourceslist | sources.list |  |  |  |  |  |  |  |  |
| splus | .S | .R |  |  |  |  |  |  |  |
| sql | .sql |  |  |  |  |  |  |  |  |
| sqlite3 | .sqlite3-console |  |  |  |  |  |  |  |  |
| squidconf | squid.conf |  |  |  |  |  |  |  |  |
| ssp | .ssp |  |  |  |  |  |  |  |  |
| tcl | .tcl |  |  |  |  |  |  |  |  |
| tcsh | .tcsh | .csh |  |  |  |  |  |  |  |
| tex | .tex | .aux | .toc |  |  |  |  |  |  |
| text | .txt |  |  |  |  |  |  |  |  |
| v | .v | .sv |  |  |  |  |  |  |  |
| vala | .vala | .vapi |  |  |  |  |  |  |  |
| vbnet | .vb | .bas |  |  |  |  |  |  |  |
| velocity | .vm | .fhtml |  |  |  |  |  |  |  |
| vim | .vim | .vimrc |  |  |  |  |  |  |  |
| xml | .xml | .xsl | .rss | .xslt | .xsd | .wsdl |  |  |  |
| xquery | .xqy | .xquery |  |  |  |  |  |  |  |
| xslt | .xsl | .xslt |  |  |  |  |  |  |  |
| yaml | .yaml | .yml |  |  |  |  |  |  |  |

### Arpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
````````````
<h3 id="8">format.py](format.py)</h3> 
`format.py`
```python
import json

from pathlib import Path

class Format:
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox

    """
    # attribut de classe
    counter_idmd = 0
    def __init__(self):

        try:

            with open("languages.json", "rt") as f:
                self.languages = json.load(f)
        except:
            print("Tables de mapage introuvables")
        
        

    def insertCodebox(self, file):
        """
        cette méthode prends en entrée un chemin de fichier avec son extention fourni par searchType()
        et retourne une variable string avec tous le code corresponding dans un codbox
        """

        extention = self.searchType(file)
        if extention == None:
            return None
        bloc = "`"
        with open(file, "rt") as f:
            code = f.read()

        # sources des commandes trouvées pour la gestion des textes : https://www.w3schools.com/python/python_ref_string.asp
        # Afficher un .env n'est pas souhaitable il faut masquer les valeurs
        if file.name == ".env":
            contenu = ""
            for ligne in code.splitlines():
                newlinge = ligne.lstrip(" ")

                # remplacement des valeurs des variables d'environnement par une valeur générique
                if newlinge and newlinge[0] != "#":
                    newlinge = newlinge.split("=")
                    variable_env = newlinge[0]
                    newlinge[1] = f"YourValueFor_{variable_env.lower()}"
                    newlinge = "=".join(newlinge)

                contenu += newlinge + "\n"
            # print(contenu)
            return f"{3*bloc}{extention}\n{contenu}\n{3*bloc}"

        # vérifie que l'extention est pas du markdown car ce type de fichier dispose de codebox
        elif extention != "markdown":
            res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
            # print(res)
            # print("")
            return res

        else:
            counter = 1
            maxrep = 1

            for l in range(1, len(code) - 1):
                if code[l] == code[l + 1] == "`":
                    counter += 1

                else:
                    if counter > maxrep:
                        maxrep = counter
                        counter = 1

            if counter > maxrep:
                maxrep = counter

            if maxrep >= 3:
                maxrep += 1
                res = f"{maxrep*bloc}{extention}\n{code}\n{maxrep*bloc}"
                # print(res)
                # print("")
                return res

            else:
                res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"
                # print(res)
                # print("")
                return res
            

    def searchType(self, file):
        """
        Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox
        """

        # recherche sur le nom de fichier
        if file.name in self.languages:
            # print(f"voici le fichier trouvée : {self.languages[file.name]}")
            return self.languages[file.name]

        elif file.suffix in self.languages:
            # print(f"voici l'extention trouvée : {self.languages[file.suffix]}")
            return self.languages[file.suffix]

        else:
            # print(f"fichier introuvés pour {file}")
            return None
        

    def makeTreeMd(self, chemin,  chemin_ignorer= [], deep = 20, level=0, racine = True):
        if level >= deep + 1 :
            return ""
        #print(chemin_ignorer)
        
        if chemin.name in chemin_ignorer:
            return ""
        
        if chemin.is_file in chemin_ignorer:
            return ""
        
        
        tree = ""
        indentation = "    "*level

        #print(f"{indentation}|__ {chemin.name}{fin}")
        if level == 0 and racine:
            self.counter_idmd = 0
            tree += f"- **{chemin.resolve().name}/**  \n"
        
        idmd = "{" + str(self.counter_idmd) + "}"
        
        if level>0:
            if chemin.is_file():
                tree += f"{indentation}- [{chemin.name}](#{idmd})  \n"
            if chemin.is_dir():
                tree += f"{indentation}- `{chemin.name}/`  \n"

        if chemin.is_dir():
            fichier_iterables = chemin.iterdir()
            fichier_liste = []
            dossier_liste = []
            for item in fichier_iterables:
                if item.is_file():
                    fichier_liste.append(item)
                if item.is_dir():
                    dossier_liste.append(item)
            
            dossiers = sorted(dossier_liste)
            fichiers = sorted(fichier_liste)
             
            for fichier in fichiers:
                try:
                #appel récursif 
                    self.counter_idmd += 1
                    tree += self.makeTreeMd(fichier, chemin_ignorer,deep,level +1, False)
                except PermissionError:
                    tree += ""
            for dossier in dossiers:
                try:
                    tree += self.makeTreeMd(dossier, chemin_ignorer,deep, level +1, False)

                except PermissionError:
                    tree += ""
        #print(tree)
        return tree

        




```
<h3 id="10">misc.xml](.idea/misc.xml)</h3> 
`.idea/misc.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Black">
    <option name="sdkName" value="Python 3.12" />
  </component>
  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12" project-jdk-type="Python SDK" />
</project>
```
### **crawlect.iml**{11}   
`.idea/crawlect.iml`

<h3 id="13">profiles_settings.xml](.idea/inspectionProfiles/profiles_settings.xml)</h3> 
`.idea/inspectionProfiles/profiles_settings.xml`
```xml
<component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>
```
<h3 id="14">modules.xml](.idea/modules.xml)</h3> 
`.idea/modules.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/crawlect.iml" filepath="$PROJECT_DIR$/.idea/crawlect.iml" />
    </modules>
  </component>
</project>
```
<h3 id="15">workspace.xml](.idea/workspace.xml)</h3> 
`.idea/workspace.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="SELECTIVE" />
  </component>
  <component name="ChangeListManager">
    <list default="true" id="ad321e4d-22a0-440b-b0d9-c7a852fce0b5" name="Changes" comment="">
      <change afterPath="$PROJECT_DIR$/languages.json" afterDir="false" />
      <change beforePath="$PROJECT_DIR$/crawlect.py" beforeDir="false" afterPath="$PROJECT_DIR$/crawlect.py" afterDir="false" />
    </list>
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="Git.Settings">
    <option name="RECENT_GIT_ROOT_PATH" value="$PROJECT_DIR$" />
  </component>
  <component name="GitHubPullRequestSearchHistory">{
  &quot;lastFilter&quot;: {
    &quot;state&quot;: &quot;OPEN&quot;,
    &quot;assignee&quot;: &quot;Alex141298&quot;
  }
}</component>
  <component name="GithubPullRequestsUISettings">{
  &quot;selectedUrlAndAccountId&quot;: {
    &quot;url&quot;: &quot;git@github.com:yvesguillo/crawlect.git&quot;,
    &quot;accountId&quot;: &quot;2343b8f7-62f1-41aa-8154-f61445de79cb&quot;
  }
}</component>
  <component name="ProjectColorInfo">{
  &quot;associatedIndex&quot;: 3
}</component>
  <component name="ProjectId" id="2uw50MjxGABUJIjb0FJnelAcmgg" />
  <component name="ProjectViewState">
    <option name="hideEmptyMiddlePackages" value="true" />
    <option name="showLibraryContents" value="true" />
  </component>
  <component name="PropertiesComponent"><![CDATA[{
  "keyToString": {
    "Python.crawlect.executor": "Run",
    "RunOnceActivity.ShowReadmeOnStart": "true",
    "RunOnceActivity.git.unshallow": "true",
    "git-widget-placeholder": "main",
    "last_opened_file_path": "/home/alexandre/Documents/MAS_RAD/01_IDD/02_Developpement_POO_python/07_POO/02_Exercices "
  }
}]]></component>
  <component name="RunManager">
    <configuration name="crawlect" type="PythonConfigurationType" factoryName="Python" temporary="true" nameIsGenerated="true">
      <module name="crawlect" />
      <option name="ENV_FILES" value="" />
      <option name="INTERPRETER_OPTIONS" value="" />
      <option name="PARENT_ENVS" value="true" />
      <envs>
        <env name="PYTHONUNBUFFERED" value="1" />
      </envs>
      <option name="SDK_HOME" value="" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="IS_MODULE_SDK" value="true" />
      <option name="ADD_CONTENT_ROOTS" value="true" />
      <option name="ADD_SOURCE_ROOTS" value="true" />
      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/crawlect.py" />
      <option name="PARAMETERS" value="" />
      <option name="SHOW_COMMAND_LINE" value="false" />
      <option name="EMULATE_TERMINAL" value="false" />
      <option name="MODULE_MODE" value="false" />
      <option name="REDIRECT_INPUT" value="false" />
      <option name="INPUT_FILE" value="" />
      <method v="2" />
    </configuration>
    <recent_temporary>
      <list>
        <item itemvalue="Python.crawlect" />
      </list>
    </recent_temporary>
  </component>
  <component name="SharedIndexes">
    <attachedChunks>
      <set>
        <option value="bundled-python-sdk-14705d77f0bb-aa17d162503b-com.jetbrains.pycharm.community.sharedIndexes.bundled-PC-243.25659.43" />
      </set>
    </attachedChunks>
  </component>
  <component name="SpellCheckerSettings" RuntimeDictionaries="0" Folders="0" CustomDictionaries="0" DefaultDictionary="application-level" UseSingleDictionary="true" transferred="true" />
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="ad321e4d-22a0-440b-b0d9-c7a852fce0b5" name="Changes" comment="" />
      <created>1743146571563</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1743146571563</updated>
    </task>
    <servers />
  </component>
</project>
```
<h3 id="16">.gitignore](.idea/.gitignore)</h3> 
`.idea/.gitignore`
```gitignore
# Default ignored files
/shelf/
/workspace.xml

```
<h3 id="17">vcs.xml](.idea/vcs.xml)</h3> 
`.idea/vcs.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="" vcs="Git" />
  </component>
</project>
```
<h3 id="18">.gitignore](.gitignore)</h3> 
`.gitignore`
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

```
<h3 id="19">note.md](note.md)</h3> 
`note.md`
```markdown
lancer crawlect sans etre dans dans le dossier ou le script se situe 

uv add --script 

```
<h3 id="20">languages.json](languages.json)</h3> 
`languages.json`
```json

{
  ".abap": "abap",
  ".ada": "ada",
  ".adb": "ada",
  ".ads": "ada",
  ".ahk": "ahk",
  ".ahkl": "ahk",
  ".htaccess": "apacheconf",
  "apache.conf": "apacheconf",
  "apache2.conf": "apacheconf",
  ".applescript": "applescript",
  ".as": "as",
  ".asy": "asy",
  ".bash": "bash",
  ".ebuild": "bash",
  ".eclass": "bash",
  ".env.example": "bash",
  ".env.local": "bash",
  ".env": "bash",
  ".ksh": "bash",
  ".sh": "bash",
  ".bat": "bat",
  ".cmd": "bat",
  ".befunge": "befunge",
  ".bmx": "blitzmax",
  ".boo": "boo",
  ".b": "brainfuck",
  ".bf": "brainfuck",
  ".c": "c", ".h": "c",
  ".cfc": "cfm",
  ".cfm": "cfm",
  ".cfml": "cfm",
  ".spt": "cheetah",
  ".tmpl": "cheetah",
  ".cl": "cl",
  ".el": "cl",
  ".lisp": "cl",
  ".clj": "clojure",
  ".cljs": "clojure",
  ".cmake": "cmake",
  "CMakeLists.txt": "cmake",
  ".coffee": "coffeescript",
  ".sh-session": "console",
  "control": "control",
  ".c++": "cpp",
  ".cc": "cpp",
  ".cpp": "cpp",
  ".cxx": "cpp",
  ".h++": "cpp",
  ".hh": "cpp",
  ".hpp": "cpp",
  ".hxx": "cpp",
  ".pde": "cpp",
  ".cs": "csharp",
  ".css": "css",
  ".feature": "cucumber",
  ".pxd": "cython",
  ".pxi": "cython",
  ".pyx": "cython",
  ".d": "d",
  ".di": "d",
  ".pas": "delphi",
  ".diff": "diff",
  ".patch": "diff",
  "Dockerfile.": "dockerfile",
  "Dockerfile": "dockerfile",
  ".darcspatch": "dpatch",
  ".dpatch": "dpatch",
  ".duel": "duel",
  ".jbst": "duel",
  ".dyl": "dylan",
  ".dylan": "dylan",
  ".erb": "erb",
  ".erl-sh": "erl",
  ".erl": "erlang",
  ".hrl": "erlang",
  ".evoque": "evoque",
  ".factor": "factor",
  ".flx": "felix",
  ".flxh": "felix",
  ".f": "fortran",
  ".f90": "fortran",
  ".s": "gas",
  ".kid": "genshi",
  ".gitignore": "gitignore",
  ".frag": "glsl",
  ".geo": "glsl",
  ".vert": "glsl",
  ".plot": "gnuplot",
  ".plt": "gnuplot",
  ".go": "go",
  ".(1234567)": "groff",
  ".man": "groff",
  ".haml": "haml",
  ".hs": "haskell",
  ".htm": "html",
  ".html": "html",
  ".xhtml": "html",
  ".hx": "hx",
  ".hy": "hybris",
  ".hyb": "hybris",
  ".cfg": "ini",
  ".conf": "ini",
  ".editorconfig": "ini",
  ".flake8": "ini",
  ".ini": "ini",
  ".npmrc": "ini",
  ".io": "io",
  ".ik": "ioke",
  ".weechatlog": "irc",
  ".jade": "jade",
  ".java": "java",
  ".js": "js",
  ".babelrc": "json",
  ".eslintrc": "json",
  ".json": "json",
  ".json5": "json",
  ".prettierrc": "json",
  ".jsp": "jsp",
  ".lhs": "lhs",
  ".ll": "llvm",
  ".lgt": "logtalk",
  ".lua": "lua",
  ".wlua": "lua",
  ".mak": "make",
  "GNUmakefile": "make",
  "Makefile.": "make",
  "Makefile": "make",
  "makefile": "make",
  ".mao": "mako",
  ".maql": "maql",
  ".md": "markdown",
  ".mc": "mason",
  ".mhtml": "mason",
  ".mi": "mason",
  "autohandler": "mason",
  "dhandler": "mason",
  ".mo": "modelica",
  ".def": "modula2",
  ".mod": "modula2",
  ".moo": "moocode",
  ".mu": "mupad",
  ".mxml": "mxml",
  ".myt": "myghty",
  "autodelegate": "myghty",
  ".asm": "nasm",
  ".ASM": "nasm",
  ".ns2": "newspeak",
  ".objdump": "objdump",
  ".m": "objectivec",
  ".j": "objectivej",
  ".ml": "ocaml",
  ".mli": "ocaml",
  ".mll": "ocaml",
  ".mly": "ocaml",
  ".ooc": "ooc",
  ".pl": "perl",
  ".pm": "perl",
  ".php(345)": "php",
  ".php": "php",
  ".eps": "postscript",
  ".ps": "postscript",
  ".po": "pot",
  ".pot": "pot",
  ".inc": "pov",
  ".pov": "pov",
  ".pro": "prolog",
  ".prolog": "prolog",
  ".properties": "properties",
  ".proto": "protobuf",
  ".py3tb": "py3tb",
  ".pytb": "pytb",
  ".py": "python",
  ".pyw": "python",
  ".sc": "python",
  ".tac": "python",
  "SConscript": "python",
  "SConstruct": "python",
  ".R": "r",
  ".duby": "rb",
  ".gemspec": "rb",
  ".rake": "rb",
  ".rb": "rb",
  ".rbw": "rb",
  ".rbx": "rb",
  "Rakefile": "rb",
  ".Rout": "rconsole",
  ".r": "rebol",
  ".r3": "rebol",
  ".cw": "redcode",
  ".rhtml": "rhtml",
  ".rest": "rst",
  ".rst": "rst",
  "Vagrantfile": "ruby",
  ".sass": "sass",
  ".scala": "scala",
  ".scaml": "scaml",
  ".scm": "scheme",
  ".scss": "scss",
  ".st": "smalltalk",
  ".tpl": "smarty",
  "sources.list": "sourceslist",
  ".S": "splus",
  ".sql": "sql",
  ".sqlite3-console": "sqlite3",
  "squid.conf": "squidconf",
  ".ssp": "ssp",
  ".tcl": "tcl",
  ".csh": "tcsh",
  ".tcsh": "tcsh",
  ".aux": "tex",
  ".tex": "tex",
  ".toc": "tex",
  ".log": "text",
  ".txt": "text",
  "requirements.txt": "text",
  ".toml": "toml",
  "Pipfile.lock": "toml",
  "Pipfile": "toml",
  "pyproject.toml": "toml",
  ".sv": "v",
  ".v": "v",
  ".vala": "vala",
  ".vapi": "vala",
  ".bas": "vbnet",
  ".vb": "vbnet",
  ".fhtml": "velocity",
  ".vm": "velocity",
  ".vim": "vim",
  ".vimrc": "vim",
  ".rss": "xml",
  ".wsdl": "xml",
  ".xml": "xml",
  ".xsd": "xml",
  ".xslt": "xml",
  ".xquery": "xquery",
  ".xqy": "xquery",
  ".xsl": "xslt",
  ".yaml": "yaml",
  ".yarnrc": "yaml",
  ".yml": "yaml"
}
```
<h3 id="21">scan.py](scan.py)</h3> 
`scan.py`
```python
#! /usr/bin/env python3

from pathlib import Path

class Scan:
    """
    Scan class contains Crawlect directories tree scan utilities.
    It require and only accept one instance of Crawlect as argument.
    """

    def __init__(self, crawler = None):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        # Store the class arguments for __repr__.
        self.args = dict()

        self.crawler = crawler
        self.args["crawler"] = self.crawler

    def listFilesIn(self, path = None, depth = None, files = None):
        """Append all eligible paths from `crawler.path` as Path object in a list and return it."""
        if files is None:
            files = []

        if depth is None:
            depth = self.crawler.depth

        if path is None:
            path = self.crawler.pathObj

        for candidatePath in path.iterdir():
            try:
                if candidatePath.is_file() and self.isFileToInclude(candidatePath):
                    files.append(candidatePath)
                elif candidatePath.is_dir() and self.crawler.recur and depth >= 1 and self.isDirToInclude(candidatePath):
                    files.append(candidatePath)
                    self.listFilesIn(path = candidatePath, depth = depth-1, files = files)
            except PermissionError as err:
                print(f"\n!! {type(err) .__name__} :\n{type(self) .__name__} Could not list path {repr(candidatePath)}: {err} ")
        return files

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isFileToInclude(self, path):
        """
        Filter file `path` according to filtering rules.
        All files pass if there are no rules.
        Inclusion overrules exclusion.
        File-name rules takes precedence against extension rules.
        """

        # Always exclude output file.
        if str(path) == self.crawler.output:
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_li == () and self.crawler.excl_fil_li == () and self.crawler.incl_ext_li == () and self.crawler.incl_fil_li == ():
            return True

        # Forcibly included by file-name always wins:
        if path.name in self.crawler.incl_fil_li:
            return True

        # Forcibly included by extension and not excluded by file-name wins:
        if path.suffix in self.crawler.incl_ext_li and path.name not in self.crawler.excl_fil_li:
            return True

        # Forcibly excluded by extension looses if not saved by file-name inclusion:
        if path.suffix in self.crawler.excl_ext_li and path.name not in self.crawler.incl_fil_li:
            return False

        # Forcibly excluded by file-name always looses:
        if path.name in self.crawler.excl_fil_li:
            return False

        # Is neither forcibly included or excluded but an extension or file inclusion is overruling:
        if self.crawler.incl_ext_li != () or self.crawler.incl_fil_li != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    # Almost identical methode in Scan and Output classes. Assess if this should be sent to a common class ("Filter" class ?).
    def isDirToInclude(self, path):
        """
        Filter directory `path` according to filtering rules.
        All directories pass if there are no rules.
        Inclusion overrules exclusion.
        """
        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_dir_li == () and self.crawler.incl_dir_li == ():
            return True

        # Is forcibly included:
        if path.name in self.crawler.incl_dir_li:
            return True

        # Is forcibly excluded:
        if path.name in self.crawler.excl_dir_li:
            return False

        # Is neither forcibly included or excluded but a directory inclusion is overruling:
        if self.crawler.incl_dir_li != ():
            return False

        # If I forgot some case scenario, you may pass Mr Tuttle:
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
```
<h3 id="24">.env](.env)</h3> 
`.env`
```bash
# variables d'environnement mysql
MYSQL_ROOT_PASSWORD=YourValueFor_mysql_root_password
MYSQL_USER=YourValueFor_mysql_user
MYSQL_PASSWORD=YourValueFor_mysql_password
MYSQL_DATABASE=YourValueFor_mysql_database

```
