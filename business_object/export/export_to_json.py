import json
from business_object.export.export import Export
import json

class export_to_json(Export):
    def __init__(self,chemin, name) -> None:
        super().__init__(chemin, name)
    def export1(self, json_obj):
        with open("{}/{}.json".format(self.chemin,self.name), "w") as out_file:
            json.dump(json_file, out_file)
        

        

      