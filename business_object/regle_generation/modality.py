from business_object.regle_generation.typ import Type

class Modality:

    dict_modality = {}


    def __init__(self, nom_type : str, proba_apparition : float, value):
        self.proba_apparition = proba_apparition
        self.value = value
        self.nom_type = nom_type

    def add_modality(self):
        if self.type in Type.dict_type :
            id_modality = len(Type.dict_modality) + 1
            d = {id_modality : {"nom_modality": nom_modality, "type" : self.nom_type , "value" : self.value, "proba d'apparition" : self.proba_apparition}}
            Modality.dict_modality.update(d)
            return dict_modality 
        else : 
            return "The modality has no type associated please check your spelling"
        

    def delete_modality(nom_type : str, value):
        for k in Modality.dict_modality :
            if Modality.dict_modality[k]["value"] == value and Modality.dict_modality[k]["type"] == nom_type:
                Modality.dict_modality[k]["proba d'apparition"] = 0
                return Modality.dict_modality
            else : 
                return "please check your spelling"

