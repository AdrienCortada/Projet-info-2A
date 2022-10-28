from unittest import TestCase
from unittest.mock import patch
import csv
import os.path

from business_object.export.export_to_csv import export_to_csv

class TestExport_to_csv(TestCase):
    
    

    def test_export_to_csv(self):
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
    if os.path.isfile("D:/Projet_Informatique_2A/table_csv.csv"):
        print("Fichier trouvé")
        
    else:
        print("Fichier non trouvé")
        

        
        
        