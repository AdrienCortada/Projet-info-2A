import pandas as pd
from business_object.regle_generation.typ import Type
from business_object.regle_generation.modality import Modality

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
la valeur de type contient les différentes modalités de la variable séparées par "|" et celle de remplissage contient le taux de remplissage de la variable.\n
Puis pour chaque modalité est associée une proba d'apparition. La pobra d'apparition est une liste (la première proba d'apparition correspond à la première modalité). \n
Si la liste des probas d'apparition commence par "same" alors toutes les proba d'apparition de toutes les modalités seront les mêmes.\n
La première clé de chaque variable doit être le 'type' et doit être une chaine de caractères\n
Par exemple, le fichier json peut se présenter comme suit\n
{
    "sexe": {
        "type": "M|F",
        "remplissage": 100,
        "proba d'apparition": ["same"]
    },
    "age": {
        "type": "uniform|borne1|borne2",
        "remplissage": 100,
        "proba d'apparition": [1,0,100]
    },
    "prenom": {
        "type": "Adrien|Abdoul|Laurène|Isaac|Nathan",
        "remplissage": 88.4,
        "proba d'apparition": ["same"]

    },
    "nom": {
        "type": "Cortada|Toure|Villacampa|Sandja",
        "remplissage": 85,
        "proba d'apparition": [20,20,20,20]
    },

    "taille": {
        "type": "normal|mean|variance",
        "remplissage": 100,
        "proba d'apparition": [1,177,5]
    },

    "nb_chevaux": {
        "type": "binomiale|individu|proba",
        "remplissage": 100,
        "proba d'apparition": [1,250,0.4]
    },

    "marque": {
        "type": "mercedes|tesla|citroein|peugeot|audi|ferrari|ford",
        "remplissage": 86,
        "proba d'apparition": ["same"]
    }
    ,

    "vitesse_max": {
        "type": "exponential|lambda",
        "remplissage": 86,
        "proba d'apparition": [1,8]
    }
}
            """
            raise Exception(texte) # préciser la forme du fichier attendue en cas d'erreur
        number_row = -1
        for k in metadonnees.index.values:
            number_row = number_row + 1 
            t = Type(metadonnees.iloc[number_row][1], k)
            t.add_type()
            modality = metadonnees.iloc[number_row][0]
            n = len(modality)
            if metadonnees.iloc[number_row][2][0] == "same":
                for i in range (0,n):
                    m = Modality(k , 1, modality[i])
                    m.add_modality()
            else :
                for i in range (0,n):
                    m = Modality(k , metadonnees.iloc[number_row][2][i], modality[i])
                    m.add_modality()

        return [Type.dict_type, Modality.dict_modality]

if __name__ == "__main__" :
    imp = IMPORTJSON("C:/Users/adrie/OneDrive - GENES/Documents/ENSAI 2A/Projet info 2/Projet-info-2A/json_test.json")
    print(imp.import_dict())