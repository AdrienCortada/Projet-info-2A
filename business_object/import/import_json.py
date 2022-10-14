import pandas as pd

class IMPORTJSON :
    def __init__(self, chemin_str) :
        self.chemin = chemin_str

    def import_dict(self) :
        metadonnees = pd.DataFrame.transpose(pd.read_json(self.chemin)) # importer le fichier JSON et le mettre en dataFrame         
        try: 
            for i in range(metadonnees.shape[0]) :
                metadonnees.iloc[i,0] = metadonnees.iloc[i,0].split("|") # spliter les différentes modalités pour avoir une liste des modalités
        except :
            texte = """Veuillez entrer un fichier JSON sous un format correct.\n
Le nom de chaque variable doit être mis comme clé, et la valeur de cette clé doit être un dictionnaire contenant les clés 'type' et 'remplissage' dans cet ordre.\n
la valeur de type contient les différentes modalités de la variable séparées par "|" et celle de remplissage contient le taux de remplissage de la variable.
La première clé de chaque variable doit être le 'type' et doit être une chaine de caractères\n
Par exemple, le fichier json peut se présenter comme suit\n
{
    "sexe": {
        "type": "SEXE",
        "remplissage": 100
    },
    "age": {
        "type": "18|19|20",
        "remplissage": 100
    },
    "prenom": {
        "type": "NAME",
        "remplissage": 88.4
    },
    "nom": {
        "type": "NAME|'dupont'",
        "remplissage": 85
    }
}
            """
            raise Exception(texte) # préciser la forme du fichier attendue en cas d'erreur
        return metadonnees

if __name__ == "__main__" :
    imp = IMPORTJSON("C:/Users\HP/Documents/GitHub/Projet-info-2A/json_test.json")
    print(imp.import_dict())