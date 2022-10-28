from business_object.export.export import Export
import json 
import xml
import pandas as pd 

class export_to_xml(Export):
    def __init__(self,chemin,name):
        super().__init__(chemin, name)
    def export(self,json_obj):
        data_json = pd.DataFrame.transpose(pd.read_json(json_obj))
        chemin_f = "{}/{}".format(self.chemin,self.name)
        file = data_json.to_xml(chemin_f)
    
if __name__=="__main__":
    res = Export("D:/Ensai 2e annees/Apprentissage_supervise/TP 3", "data.xml")
    res.export("json_test.json")