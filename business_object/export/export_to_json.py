import json
from business_object.export.export import Export
import json

class export_to_json(Export):
    def __init__(self,chemin:str,name:str) -> None:
        '''Constructeur
        Attributes
        ----------
        chemin : str 
                 Chemin sur lequel le jeu de données va être sauvegardé
        name : str
               Nom du fichier sur lequel le jeu de données va être sauvegardé
        '''
        super().__init__(chemin, name)
    def export(self,json_dict:dict) -> None:
        '''
        Exporte le jeu de données généré sous format json 

        Parameters
        ----------
        json_dict : dict  
                Le jeu de données généré         


        '''
        with open("{}/{}.json".format(self.chemin,self.name), "w") as out_file:
            json.dump(json_dict, out_file)
        

        

      