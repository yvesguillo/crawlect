#! /usr/bin/env python3

# Standard modules.
from pathlib import Path
import json
import importlib.resources
import re

class Format():
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox
    """

    def __init__(self, crawler):
        self.args = dict()
        self.crawler = crawler
        self.args["crawler"] = self.crawler

        self.languages = {}

        # récupérer l'emplacement du script (pour les fichiers de config )
        try:
            with importlib.resources.files("crawlect").joinpath("languages.json").open("rt") as f:
                self.languages = json.load(f)
        except FileNotFoundError:
            print("Could not find languages.json in Crawlect package.")
            raise
        except Exception as error:
            print(f"Unexpected error loading languages.json: {error}")
            raise


    def insert_codebox(self, file):
        """
        cette méthode prends en entrée un chemin de fichier avec son extention fourni par search_type()
        et retourne une variable string avec tous le code corresponding dans un codbox
        """

        extention = self.search_type(file)

        if extention == None:
            return None

        bloc = "`"
        with open(file, "rt", encoding = "utf-8") as f:
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

            return f"{3 * bloc}{extention}\n{contenu}\n{3 * bloc}"

        # vérifie que l'extention est pas du markdown car ce type de fichier dispose de codebox
        elif extention != "markdown":
            res = f"{3 * bloc}{extention}\n{code}\n{3 * bloc}"

            return res

        else:
            # Count the maximum amount of consecutive "`" in the file and retur the ammount in maxrep. maxrep will be 2 if none ar found.
            matches = re.findall(r"`+", code)
            maxrep = max((len(m) for m in matches), default = 2)

            # le nombre minimal pour une codebox est de 3 si on en compte 3 --> ajouter occurances afin d'englober la totalité
            if maxrep >= 3:
                maxrep += 1
                res = f"{maxrep * bloc}{extention}\n{code}\n{maxrep * bloc}"

                return res

            else:
                res = f"{3 * bloc}{extention}\n{code}\n{3 * bloc}"

                return res


    def search_type(self, file):
        """Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox."""

        # recherche sur le nom de fichier
        if file.name in self.languages:
            return self.languages[file.name]

        elif file.suffix in self.languages:
            return self.languages[file.suffix]

        else:
            return None


    def makeTreeMd(self, chemin = None, crawler = None, level = 0, racine = True, prefix = ""):
        """
        Build a text file tree.
        """

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(
                f"{type(self).__name__} requires exactly one instance of Crawlect as argument."
            )

        if chemin is None:
            chemin = crawler.pathObj

        # Depth guard (level=0 is root).
        if level > crawler.depth:
            return ""

        # Ignore guard.
        if crawler.is_path_ignored(chemin):
            return ""

        lines = []

        # Root line
        if racine:
            # use resolved name.
            lines.append(f"{chemin.resolve().name}/")

        def safe_listdir(dir_path: Path):
            try:
                items = list(dir_path.iterdir())
            except PermissionError:
                return []
            # Filter ignored.
            items = [p for p in items if not crawler.is_path_ignored(p)]
            # Sort: directories first, then files.
            items.sort(key = lambda p: (p.is_file(), p.name.lower()))
            return items

        def walk(node: Path, current_prefix: str, current_level: int):
            if current_level > crawler.depth:
                return

            if crawler.is_path_ignored(node):
                return

            if node.is_dir():
                children = safe_listdir(node)
            else:
                children = []

            # Iterate children and dcheck for last ( `└─` or `├─` ).
            for idx, child in enumerate(children):
                is_last = (idx == len(children) - 1)
                branch = " └─ " if is_last else " ├─ "
                name = child.name + ("/" if child.is_dir() else "")

                lines.append(f"{current_prefix}{branch}{name}")

                # Build and pass next prefix. (keep │ only if THIS level still has siblings after).
                next_prefix = current_prefix + ("    " if is_last else " │  ")

                if child.is_dir():
                    walk(child, next_prefix, current_level + 1)

        # Start recursion.
        if chemin.is_dir():
            walk(chemin, prefix, level + 1)

        # Agregate lines.
        return "\n".join(lines) + "\n"