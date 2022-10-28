from business_object.export.export import Export
import json 
import xml
import pandas as pd 

class export_to_xml(Export):
    def __init__(self,chemin,name) -> None:
        '''Constructeur
        Attributes
        ----------
        chemin : str 
                 Chemin sur lequel le jeu de données va être sauvegardé
        name : str
               Nom du fichier sur lequel le jeu de données va être sauvegardé
        '''
        super().__init__(chemin, name)
    def export(self,json_dict) -> None:
        """Exporte le jeu de données généré sous format xml

        Parameters
        ----------
        json_dict : dict  
                Le jeu de données généré         


        """
       
        data_json = pd.DataFrame.transpose(pd.read_json(json_obj))
        chemin_f = "{}/{}".format(self.chemin,self.name)
        file = data_json.to_xml(chemin_f)
    
if __name__=="__main__":
    res = export_to_xml("C:/Users/natha/OneDrive/Documents/ENSAI 1A/UE8 Programmation avec Python/Introduction à la programmation orientée objet", "data.xml")
    res.export("json_test.json")