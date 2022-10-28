from business_object.export.export import Export
import json 
import csv 
import pandas as pd 

class export_to_csv(Export):
    def __init__(self,chemin,name):
        super().__init__(chemin, name)
    def export1(self,json_obj):
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
