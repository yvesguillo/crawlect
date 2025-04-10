# crawlect
2025.04.10 18:42

Generated with Crawlect.

## File structure

Directory tree.

- **crawlect/**  
    - [.dockerignore](#c8afa7b75b1bf37901032864cc7810cd)  
    - [.env](#24168ec10bb7aade3906df7c1f0ab474)  
    - [.gitignore](#e101f98f081015323159f80dae4e45dc)  
    - [README.md](#80155230161f05644d9c479c20cc4d83)  
    - [crawlect.py](#3a757f80aa67508e877bc9cca631b169)  
    - [format.py](#b44a25a826390ab7857b179af707833a)  
    - [languages.json](#ed8cdd9ebc9ae67db84fd34509297816)  
    - [note.md](#772251ee0d5df1069012ad3c5c143be2)  
    - [output.py](#9fc1b4d738efcafb5d63a5e68173eb5f)  
    - [scan.py](#e19de777b1f613263660214c18e73172)  
    - `.idea/`  
        - [.gitignore](#69c22fe3142ec35ef675e6e4d809f041)  
        - [crawlect.iml](#7afff84d55eb7500b4b6a1de7980f11c)  
        - [misc.xml](#3d4510e5fd7ed56e184f64cc456cae21)  
        - [modules.xml](#9533fee8ad08e07fc37fd1a45686a893)  
        - [vcs.xml](#94e383f33062cc36c3ffb5f385ef4c8a)  
        - [workspace.xml](#6f9dad7539ab677424085e0ec5682092)  
        - `inspectionProfiles/`  
            - [profiles_settings.xml](#421b102c49df6804ada1973926864531)  
    - `__pycache__/`  
        - [format.cpython-312.pyc](#cb5f708e7aab3f5f628fd7a933eff620)  
        - [output.cpython-312.pyc](#cb413b8ce545a75635246fdcaa438c61)  
        - [scan.cpython-312.pyc](#6dad589541fcb2b38e5c843a76690f17)  
    - `tata/`  
        - `toto1/`  
    - `toto/`  
        - `toto1/`  


## Files:

<h3 id="c8afa7b75b1bf37901032864cc7810cd">.dockerignore</h3>  
`.dockerignore`


<h3 id="3a757f80aa67508e877bc9cca631b169">crawlect.py</h3>  
`crawlect.py`

```python
#! /usr/bin/env python3

from pathlib import Path
from fnmatch import fnmatch
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

    def __init__(self, path = None, output = None, output_prefix = None, output_suffix = None, recur = True, depth = inf, crawlectignore = None, gitignore = True, dockerignore = True, excl_pat_li = [], excl_fil_li = [], excl_ext_li = [], excl_dir_li = [], excl_fil_wr = [], excl_ext_wr = [], excl_dir_wr = [], incl_fil_li = [], incl_ext_li = [], incl_dir_li = [], incl_fil_wr = [], incl_ext_wr = [], incl_dir_wr = [], xenv = True, tree = True):

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

        # Ignore files handling.
        self.crawlectignore = crawlectignore
        self.args["crawlectignore"] = self.crawlectignore
        self.gitignore = gitignore
        self.args["gitignore"] = self.gitignore
        self.dockerignore = dockerignore
        self.args["dockerignore"] = self.dockerignore
        self.mergedIgnore = []

        # Files and xtensions inclusion/exclusions parameters.
        self.excl_pat_li = excl_pat_li
        self.args["excl_pat_li"] = self.excl_pat_li
        self.excl_fil_li = excl_fil_li
        self.args["excl_fil_li"] = self.excl_fil_li
        self.excl_ext_li = excl_ext_li
        self.args["excl_ext_li"] = self.excl_ext_li
        self.excl_dir_li = excl_dir_li
        self.args["excl_dir_li"] = self.excl_dir_li
        self.incl_fil_li = incl_fil_li
        self.args["incl_fil_li"] = self.incl_fil_li
        self.incl_ext_li = incl_ext_li
        self.args["incl_ext_li"] = self.incl_ext_li
        self.incl_dir_li = incl_dir_li
        self.args["incl_dir_li"] = self.incl_dir_li
        self.excl_fil_wr = excl_fil_wr
        self.args["excl_fil_wr"] = self.excl_fil_wr
        self.excl_ext_wr = excl_ext_wr
        self.args["excl_ext_wr"] = self.excl_ext_wr
        self.excl_dir_wr = excl_dir_wr
        self.args["excl_dir_wr"] = self.excl_dir_wr
        self.incl_fil_wr = incl_fil_wr
        self.args["incl_fil_wr"] = self.incl_fil_wr
        self.incl_ext_wr = incl_ext_wr
        self.args["incl_ext_wr"] = self.incl_ext_wr
        self.incl_dir_wr = incl_dir_wr
        self.args["incl_dir_wr"] = self.incl_dir_wr

        # Advanced features parameters.
        self.xenv = xenv
        self.args["xenv"] = self.xenv
        self.tree = tree
        self.args["tree"] = self.tree

        # File overwrite denied by default.
        self.writeRight = "x"

        self.validateParam()

        self.warmUp()

        self.initServices()

        self.processIgnoreFiles()

        self.generatePathList()

    # To be enhanced. State patern for interactive/module mode?
    def validateParam(self):
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
        if self.crawlectignore is not None:
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.crawlectignore))

        if self.gitignore and Path(self.path + "/.gitignore").exists():
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.path + "/.gitignore"))
            self.mergedIgnore.append(".git")

        if self.dockerignore and Path(self.path + "/.dockerignore").exists():
            self.mergedIgnore.extend(self.getIgnoreListFromFile(self.path + "/.dockerignore"))

        # Get unique ignore path values.
        self.mergedIgnore = list(set(self.mergedIgnore))

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

    def getIgnoreListFromFile(self, file = None):
        """Try to get ignore file and parse its ignore rules in a list."""

        # Does not support advanced .gitignore syntax such as the "!" for not ignoring at the moment. It will probably not be handled here but in the *Scan* class thought.

        ignoreList = []
        try:
            with open(file) as ignoreFile:
                for line in ignoreFile.read().splitlines():
                     if line and "#" not in line:
                        ignoreList.append(line)
        except Exception as error:
            print(f"\n!! - {type(error).__name__}:\n{type(self).__name__} could not process getIgnoreListFromFile({repr(file)}): {error}")
        return ignoreList

    # Assess if this should be sent to a common class ("Filter" class ?).
    def isPathIgnored(self, path):
        """Check if path match any .gitignore pattern or path include/exclude list parameter item."""

        # Does not support advanced .gitignore syntax such as the "!" for not ignoring at the moment.

        for ignored in self.mergedIgnore:
            if fnmatch(path, ignored):
                return True

        # Check if path is in path ignore list parameter.
        for excludedPath in self.excl_pat_li:
            if path == Path(excludedPath):
                return True

        return False

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

        # Ignore files handling.
        parser.add_argument(
            "-crawlig", "--crawlectignore", "--crawlectignore_use",
            type = str,
            default = None,
            help = "Use custom file as Crawlect exclusion rules (default is None).")

        parser.add_argument(
            "-gitig", "--gitignore", "--gitignore_use",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Use .gitignore exclusion rules if exist (default is True).")

        parser.add_argument(
            "-dokig", "--dockerignore", "--dockerignore_use",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Use .dockerignore exclusion rules if exist (default is True).")

        # Files and xtensions inclusion/exclusions parameters.
        parser.add_argument(
            "-xpl", "--excl_pat_li", "--excluded_paths_from_listing",
            nargs = "*",
            default = [],
            help = "List of paths to exclude from listing (e.g.: ./messy_folder/, ./album/vacation_56.png).")

        parser.add_argument(
            "-xfl", "--excl_fil_li", "--excluded_files_from_listing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xel", "--excl_ext_li", "--excluded_xtensions_from_listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdl", "--excl_dir_li", "--excluded_directories_from_listing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from listing (e.g.: bin, render).")

        parser.add_argument(
            "-ifl", "--incl_fil_li", "--include_files_for_listing",
            nargs = "*",
            default = [],
            help = "List of files to include for listing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iel", "--incl_ext_li", "--include_xtensions_for_listing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for listing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idl", "--incl_dir_li", "--include_directories_for_listing",
            nargs = "*",
            default = [],
            help = "List of directories to include for listing (e.g.: bin, render).")

        parser.add_argument(
            "-xfw", "--excl_fil_wr", "--excluded_files_from_writing",
            nargs = "*",
            default = [],
            help = "List of files to exclude from writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-xew", "--excl_ext_wr", "--excluded_xtensions_from_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to exclude from writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-xdw", "--excl_dir_wr", "--excluded_directories_from_writing",
            nargs = "*",
            default = [],
            help = "List of directories to exclude from writing (e.g.: bin, render).")

        parser.add_argument(
            "-ifw", "--incl_fil_wr", "--include_files_for_writing",
            nargs = "*",
            default = [],
            help = "List of files to include for writing (e.g.: README.md, profile.png).")

        parser.add_argument(
            "-iew", "--incl_ext_wr", "--include_xtensions_for_writing",
            nargs = "*",
            default = [],
            help = "List of file extensions to include for writing (e.g.: .jpg, .png).")

        parser.add_argument(
            "-idw", "--incl_dir_wr", "--include_directories_for_writing",
            nargs = "*",
            default = [],
            help = "List of directories to include for writing (e.g.: bin, render).")

        # Advanced features parameters.
        parser.add_argument(
            "-xen", "--xenv", "--sanitize_env_variables",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Sanitize .env variables to mitigate sensitive info leak risk (default is True).")

        parser.add_argument(
            "-tre", "--tree", "--visualize_directory_tree",
            type = str,
            choices = ["Yes", "yes", "No", "no", "Y", "y", "N", "n", "True", "true", "False", "false", "T", "t", "F", "f", "1", "0"],
            action = BooleanAction,
            default = True,
            help = "Visualize directory tree in the output file (default is True).")

        args = parser.parse_args()

        crawlect = Crawlect(path = args.path, output = args.output, output_prefix = args.output_prefix, output_suffix = args.output_suffix, recur = args.recur, depth = args.depth, excl_pat_li = args.excl_pat_li, excl_fil_li = args.excl_fil_li, excl_ext_li = args.excl_ext_li, excl_dir_li = args.excl_dir_li, excl_fil_wr = args.excl_fil_wr, excl_ext_wr = args.excl_ext_wr, excl_dir_wr = args.excl_dir_wr, incl_fil_li = args.incl_fil_li, incl_ext_li = args.incl_ext_li, incl_dir_li = args.incl_dir_li, incl_fil_wr = args.incl_fil_wr, incl_ext_wr = args.incl_ext_wr, incl_dir_wr = args.incl_dir_wr, crawlectignore = args.crawlectignore, gitignore = args.gitignore, dockerignore = args.dockerignore,xenv = args.xenv, tree = args.tree)

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
<h3 id="b44a25a826390ab7857b179af707833a">format.py</h3>  
`format.py`

```python
#! /usr/bin/env python3


import json
import hashlib
from pathlib import Path

class Format():
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox

    """

    
    def __init__(self, crawler):
        self.args = dict()
        self.crawler = crawler
        self.args["crawler"] = self.crawler = crawler

        # récupérer l'emplacement du script (pour les fichiers de config )
        sciptPath = Path(__file__).resolve().parent

        #création du lien 
        langPath = sciptPath /"languages.json"
        try:

            with langPath.open("rt") as f:
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
                #compte le nombre de fois que le caractère "`" est présent à la suite 
                if code[l] == code[l + 1] == "`":
                    counter += 1

                else:
                    if counter > maxrep:
                        maxrep = counter
                        counter = 1

            if counter > maxrep:
                maxrep = counter

            # le nombre minimal pour une codebox est de 3 si on en compte 3 --> ajouter occurances afin d'englober la totalité
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
        """
        prend un Path en entrée, des nom de fichier à ignorer, une profondeur de recherche
        retourne une arboressance des fichiers 
        ajoute un hashage afin de crée des liens dans le fichier markdown
        """
        if level >= deep + 1 :
            return ""
        
        
        
        
        if chemin.name in chemin_ignorer:
            return ""
        
        if chemin.is_file in chemin_ignorer:
            return ""
        
        
        tree = ""
        indentation = "    "*level

        # Récupération du nom du dossier parent du dossier racine 
        if level == 0 and racine:
            tree += f"- **{chemin.resolve().name}/**  \n"
        


        # On vérifie que nous ne somme pas dans la première occurence de récursivité
        if level>0:
            if chemin.is_file():
                chemin_id = hashlib.md5(str(chemin.resolve()).encode()).hexdigest()
                tree += f"{indentation}- [{chemin.name}](#{chemin_id})  \n"

            if chemin.is_dir():
                if self.crawler.isPathIgnored(chemin):
                    return ""
                tree += f"{indentation}- `{chemin.name}/`  \n"

        if chemin.is_dir():
            fichier_iterables = chemin.iterdir()
            fichier_liste = []
            dossier_liste = []

            # séparation des dossier et des fichiers afin de les trier. 
            # le but est d'afficher les fichiers avant les dossier dans un répertoire 
            for item in fichier_iterables:
                if item.is_file():
                    fichier_liste.append(item)
                if item.is_dir():
                    dossier_liste.append(item)
            
            dossiers = sorted(dossier_liste)
            fichiers = sorted(fichier_liste)
              
            for fichier in fichiers:
                try:
                #appel récursif pour chaque fichier de la liste 
                    tree += self.makeTreeMd(fichier, chemin_ignorer,deep,level +1, False)

                #gestion en cas de fichier inaccessible pour cause de manque de privilège 
                except PermissionError:
                    tree += ""
            for dossier in dossiers:
                try:
                #appel récursif pour chaque dossier de la liste 
                    tree += self.makeTreeMd(dossier, chemin_ignorer,deep, level +1, False)

                # gestion en cas de dossier inacessible cause de manque de privilège 
                except PermissionError:
                    
                    tree += ""
        #print(tree)
        return tree

        




```
<h3 id="ed8cdd9ebc9ae67db84fd34509297816">languages.json</h3>  
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
<h3 id="772251ee0d5df1069012ad3c5c143be2">note.md</h3>  
`note.md`

```markdown
lancer crawlect sans etre dans dans le dossier ou le script se situe 

uv add --script 

crawlect.py -p . -xdl .git venv __pycache__ .volumes -o test.md -gitig f --dockerignore f 


```
<h3 id="9fc1b4d738efcafb5d63a5e68173eb5f">output.py</h3>  
`output.py`

```python
#! /usr/bin/env python3

from pathlib import Path
from datetime import datetime
from random import choices
import string
import hashlib

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
                exclude = self.crawler.excl_dir_li
                exclude.append(self.currentOutputName)
                outputFile.write(f"## File structure\n\nDirectory tree.\n\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer = exclude, deep = self.crawler.depth)}\n\n")

            # Files list

            # sort file
            sorted_files = self.crawler.files
            sorted_files.sort(key = lambda p: (p.parent, p.name))

            outputFile.write("## Files:\n\n")
            for file in sorted_files:

                chemin_id = hashlib.md5(str(file.resolve()).encode()).hexdigest()

                if file.is_file() and str(file) != self.currentOutputName:
                    outputFile.write(f"<h3 id=\"{chemin_id}\">{file.name}</h3>  \n")
                    outputFile.write(f"`{file}`\n\n")
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

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_wr == [] and self.crawler.excl_fil_wr == [] and self.crawler.incl_ext_wr == [] and self.crawler.incl_fil_wr == []:
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
        if self.crawler.incl_ext_wr != [] or self.crawler.incl_fil_wr != []:
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
<h3 id="e19de777b1f613263660214c18e73172">scan.py</h3>  
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

    def listPathIn(self, path = None, depth = None, files = None):
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
                    self.listPathIn(path = candidatePath, depth = depth-1, files = files)
            except PermissionError as err:
                print(f"\n!! - {type(err).__name__} :\n{type(self) .__name__} Could not list path {repr(candidatePath)}: {err} ")
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

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_ext_li == [] and self.crawler.excl_fil_li == [] and self.crawler.incl_ext_li == [] and self.crawler.incl_fil_li == []:
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
        if self.crawler.incl_ext_li != [] or self.crawler.incl_fil_li != []:
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

        # Ignore files such as `.gitignore` rules above all.
        if self.crawler.isPathIgnored(path):
            return False

        # No rules at all, everything pass. This is Anarchy!:
        if self.crawler.excl_dir_li == [] and self.crawler.incl_dir_li == []:
            return True

        # Is forcibly included:
        if path.name in self.crawler.incl_dir_li:
            return True

        # Is forcibly excluded:
        if path.name in self.crawler.excl_dir_li:
            return False

        # Is neither forcibly included or excluded but a directory inclusion is overruling:
        if self.crawler.incl_dir_li != []:
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
<h3 id="69c22fe3142ec35ef675e6e4d809f041">.gitignore</h3>  
`.idea/.gitignore`

```gitignore
# Default ignored files
/shelf/
/workspace.xml

```
<h3 id="7afff84d55eb7500b4b6a1de7980f11c">crawlect.iml</h3>  
`.idea/crawlect.iml`


<h3 id="3d4510e5fd7ed56e184f64cc456cae21">misc.xml</h3>  
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
<h3 id="9533fee8ad08e07fc37fd1a45686a893">modules.xml</h3>  
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
<h3 id="94e383f33062cc36c3ffb5f385ef4c8a">vcs.xml</h3>  
`.idea/vcs.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="" vcs="Git" />
  </component>
</project>
```
<h3 id="6f9dad7539ab677424085e0ec5682092">workspace.xml</h3>  
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
<h3 id="421b102c49df6804ada1973926864531">profiles_settings.xml</h3>  
`.idea/inspectionProfiles/profiles_settings.xml`

```xml
<component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>
```
