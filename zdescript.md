# crawlect
2025.04.08 16:23

Generated with Crawlect.

## File structure

Directory tree.
```text
# crawlect
   |__ .gitignore
   |__ crawlect.py
   |__ format.py
   |__ languages.json
   |__ output.py
   |__ README.md
   |__ scan.py
   |__ zdescript.md
   |__ __pycache__/
      |__ format.cpython-312.pyc
      |__ output.cpython-312.pyc
      |__ scan.cpython-312.pyc

```

## Files:

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
        indentation = "   "*level
        if chemin.is_dir():
            fin = "/"
        else:
            fin = ""

        #print(f"{indentation}|__ {chemin.name}{fin}")
        if level == 0 and racine:
            tree += f"# {chemin.absolute().name}\n"
        elif level>0:
            tree += f"{indentation}|__ {chemin.name}{fin}\n"

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
                #appel récursif 
                tree += self.makeTreeMd(fichier, chemin_ignorer,deep,level +1, False)

            for dossier in dossiers:
                tree += self.makeTreeMd(dossier, chemin_ignorer,deep, level +1, False)
        #print(tree)
        return tree

        




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
                outputFile.write(f"## File structure\n\nDirectory tree.\n```text\n{self.crawler.formatService.makeTreeMd(self.crawler.pathObj, chemin_ignorer= self.crawler.excl_dir_li, deep = self.crawler.depth, level = 0, racine = True)}\n```\n\n")

            # Files list
            outputFile.write("## Files:\n\n")
            for file in self.crawler.files:

                fileDepth = len(file.parents) -1

                if file.is_file() and str(file) != self.currentOutputName:
                    outputFile.write(f"### **[{file.name}]({file})**  \n")
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
            if candidatePath.is_file() and self.isFileToInclude(candidatePath):
                files.append(candidatePath)
            elif candidatePath.is_dir() and self.crawler.recur and depth >= 1 and self.isDirToInclude(candidatePath):
                files.append(candidatePath)
                self.listFilesIn(path = candidatePath, depth = depth-1, files = files)
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
### **[format.cpython-312.pyc](__pycache__\format.cpython-312.pyc)**  
`__pycache__\format.cpython-312.pyc`

### **[output.cpython-312.pyc](__pycache__\output.cpython-312.pyc)**  
`__pycache__\output.cpython-312.pyc`

### **[scan.cpython-312.pyc](__pycache__\scan.cpython-312.pyc)**  
`__pycache__\scan.cpython-312.pyc`

