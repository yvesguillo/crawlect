import json
class Format:
    
    '''
    La classe prend en entrée une liste triée par la classe scan, identifie le type de fichier 

    '''
    def __init__(self, filesToformat):

        self.files = filesToformat
        
        try:
            
            with open("languages.json","rt") as f:
                self.languages = json.load(f)
        except:
            print("Tables de mapage introuvables")


    
    
    def typeCodeBox(self):
        print(self.files)
        for file in self.files.files:
            extension = self.searchType(file)
            if extension == None:
                continue
            self.insertCodebox(file,extension)
            #fonction 

    

    def insertCodebox(self, file, extention):
        # vérifie que l'extention est pas du markdown
        if extention == "markdown":
            print("md")
        else:
            with open(file,"rt") as f:
                code = f.read()
            
            res = f"```{extention}\n{code}\n```"
            print(res)
            print("")
            return res


    def searchType(self,file):
        
        #recherche sur le nom de fichier 
        if file.name in self.languages:
            print(f"voici le fichier trouvée : {self.languages[file.name]}")
            #self.insertCodebox(file, self.languages[file.name])
            return self.languages[file.name]
        
        elif file.suffix in self.languages:
            print(f"voici l'extention trouvée : {self.languages[file.suffix]}")
            return self.languages[file.suffix]
        
        else:
            print(f"fichier introuvés pour {file}")

            return None 
        