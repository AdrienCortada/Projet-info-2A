from business_object.export.export import Export
import json 
import xml
import pandas as pd 

class export_to_xml(Export):
    def __init__(self,chemin,name):
        super.__init__(chemin, name)
    def export(self):
        data_json = pd.DataFrame.transpose(Export.json_obj)
        chemin_f = "{}\\{}".format(self.chemin,self.name)
        file = data_json.to_xml(chemin_f)