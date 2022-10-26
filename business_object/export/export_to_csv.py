from business_object.export.export import Export
import json 
import csv 
import pandas as pd 


class export_to_csv(Export):
    def __init__(self,chemin,name):
        self.chemin = chemin
        self.name = name
    def export(self, json_obj):
        data_json = pd.DataFrame.transpose(json_obj)
        chemin_f = "{}/{}".format(self.chemin,self.name)
        file = data_json.to_csv(chemin_f)
        

        

if __name__ == "__main__":
    exportation = export_to_csv(r"C:\Users\natha\OneDrive\Documents\ENSAI 2A\UE3 Informatique pour la data science\Projet Informatique","test.csv")
    json_test = pd.read_json(r"C:\Users\natha\OneDrive\Documents\ENSAI 2A\UE3 Informatique pour la data science\Projet Informatique\Projet-info-2A\json_test.json")
    exportation.export(json_test)