from unittest import TestCase
from unittest.mock import patch
import csv
import os.path
import json

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
    # Vérifier si le fichier existe ou non
        if os.path.isfile("D:/Projet_Informatique_2A/table_csv.csv"):
            print("Fichier trouvé")
            tablecsv = export_to_csv("D:\Projet_Informatique_2A\Projet-info-2A" , "table_csv.csv")
            csvfile = csv.reader("D:/Projet_Informatique_2A/Projet-info-2A/table_csv.csv")
            table_csv1 = tablecsv.export(json.dumps(table))
            table_csv = csv.reader(table_csv1)
            self.assertEqual(csvfile,table_csv )
        else:
            print("Fichier non trouvé")
        
TestExport_to_csv().test_export_to_csv()
        
        
        