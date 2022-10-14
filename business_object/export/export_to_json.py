from export import Export 
from generation_donnnee import Generation_donnee
import json

class Export_to_json(self):
    def __init__(self) -> None:
        super().__init__()
    def export(self, chemin, name):
        f = open(self.generer_jeu_donnee())
        data = json.load(f)
        with open("{}{}.json".format(chemin,name), "w") as out_file:
        json.dump(f, out_file)
        out_file.close()

        

      