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

        



