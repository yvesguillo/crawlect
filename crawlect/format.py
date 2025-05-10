#! /usr/bin/env python3

import json
import hashlib
from pathlib import Path
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


    def searchType(self, file):
        """Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox."""

        # recherche sur le nom de fichier
        if file.name in self.languages:
            return self.languages[file.name]

        elif file.suffix in self.languages:
            return self.languages[file.suffix]

        else:
            return None


    def makeTreeMd(self, chemin = None, crawler = None, level = 0, racine = True):
        """
        prend un Path en entrée, des nom de fichier à ignorer, une profondeur de recherche
        retourne une arboressance des fichiers 
        ajoute un hashage afin de crée des liens dans le fichier markdown
        """

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        if chemin is None:
            chemin = crawler.pathObj

        if level >= crawler.depth + 1 :
            return ""

        if crawler.isPathIgnored(chemin):
            return ""

        tree = ""
        indentation = "    " * level

        # Récupération du nom du dossier parent du dossier racine 
        if level == 0 and racine:
            tree += f"- **{chemin.resolve().name}/**  \n"

        # On vérifie que nous ne somme pas dans la première occurence de récursivité
        if level > 0:
            if chemin.is_file():
                tree += f"{indentation}- [{chemin.name.replace(".", "&period;")}](#{chemin.name.replace(" ", "-").replace(".", "&period;")})  \n"

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
                    tree += str(self.makeTreeMd(chemin = fichier, crawler = crawler, level = level + 1, racine = False))

                #gestion en cas de fichier inaccessible pour cause de manque de privilège 
                except PermissionError:
                    tree += ""

            for dossier in dossiers:
                try:
                #appel récursif pour chaque dossier de la liste 
                    tree += str(self.makeTreeMd(chemin = dossier, crawler = crawler, level = level + 1, racine = False))

                # gestion en cas de dossier inacessible cause de manque de privilège 
                except PermissionError:
                    tree += ""

                except Exception as error:
                    print(f"\n!! - {type(error).__name__} :\n{type(self) .__name__} Could not list path due unexpected error {repr(chemin)}: {error} ")
                    tree += ""

        return tree