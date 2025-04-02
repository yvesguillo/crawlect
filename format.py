import json


class Format:
    """
    La classe prend en entrée un chemin de fichier path fourni par la classe scan.
    Va identifier le type de fichier et le placer dans un codbox 

    """

    def __init__(self, filesToformat):

        self.files = filesToformat

        try:

            with open("languages.json", "rt") as f:
                self.languages = json.load(f)
        except:
            print("Tables de mapage introuvables")

    def typeCodeBox(self):
        '''
        boucle qui simule le code 
        '''
        print(self.files)
        for file in self.files.files:
            extension = self.searchType(file)
            if extension == None:
                continue
            self.insertCodebox(file, extension)
            # fonction

    def insertCodebox(self, file, extention):
        '''
        cette méthode prends en entrée un chemin de fichier avec son extention fourni par searchType()
        et retourne une variable string avec tous le code corespondant dans un codbox
        '''

        bloc = "`"
        with open(file, "rt") as f:
            code = f.read()

        # vérifie que l'extention est pas du markdown
        if extention != "markdown":
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
        '''
        Prend le chemin d'un fichier et retourne le type de fichier à inscrire dans la codebox 
        '''

        # recherche sur le nom de fichier
        if file.name in self.languages:
            print(f"voici le fichier trouvée : {self.languages[file.name]}")
            return self.languages[file.name]

        elif file.suffix in self.languages:
            print(f"voici l'extention trouvée : {self.languages[file.suffix]}")
            return self.languages[file.suffix]

        else:
            print(f"fichier introuvés pour {file}")
            return None
