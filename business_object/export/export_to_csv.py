from business_object.export.export import Export
import json 
import csv 
import pandas as pd 

class export_to_csv(Export):
    def __init__(self,chemin,name):
        super().__init__(chemin, name)
    def export1(self):
        data_json = pd.DataFrame.transpose(Export.json_obj)
        chemin_f = "{}/{}".format(self.chemin,self.name)
        file = data_json.to_csv(chemin_f)
        



