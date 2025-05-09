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

            return f"{3*bloc}{extention}\n{contenu}\n{3*bloc}"

        # vérifie que l'extention est pas du markdown car ce type de fichier dispose de codebox
        elif extention != "markdown":
            res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"

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

                return res

            else:
                res = f"{3*bloc}{extention}\n{code}\n{3*bloc}"

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


    def makeTreeMd(self, crawler = None):

        # Validate.
        if type(crawler).__name__ != "Crawlect":
            raise TypeError(f"{type(self).__name__} class require and only accept one instance of Crawlect as argument.")

        tree = ""

        for path in crawler.files:
            tree += "- " + str(path) + "\n"

        return tree
