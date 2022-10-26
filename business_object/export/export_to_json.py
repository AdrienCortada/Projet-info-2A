import json
from export import Export 
from generation_donnnee import Generation_donnee
import json

class Export_to_json(Export):
    def __init__(self,chemin) -> None:
        super().__init__(chemin)
    def export(self, json_file, chemin, name):
        with open("{}/{}.json".format(chemin,name), "w") as out_file:
            json.dump(json_file, out_file)
        

        

      