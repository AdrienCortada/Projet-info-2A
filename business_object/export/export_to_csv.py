from business_object.export.export import Export
import json 
import csv 
import pandas as pd 

class export_to_csv(Export):
    def __init__(self,chemin:str,name:str) -> None:
        '''Constructeur
        Attributes
        ----------
        chemin : str 
                 Chemin sur lequel le jeu de données va être sauvegardé
        name : str
               Nom du fichier sur lequel le jeu de données va être sauvegardé
        '''
        super().__init__(chemin, name)
    def export(self,json_dict:dict) -> None:
        """Exporte le jeu de données généré sous format csv

        Parameters
        ----------
        json_dict : dict  
                Le jeu de données généré        


        """
        data_json = pd.DataFrame.transpose(pd.read_json(json_obj))
        chemin_f = "{}/{}".format(self.chemin,self.name)
        file = data_json.to_csv(chemin_f)
        

table = {
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
