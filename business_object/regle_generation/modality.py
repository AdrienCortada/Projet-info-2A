from type import Type

class Modality:

    dict_modality = {}


    def __init__(self, nom_type : str, proba_apparition : float, value):
        self.proba_apparition = proba_apparition
        self.value = value
        self.type = nom_type

    def add_modality(self):
        if self.type in Type.dict_type :
            id_modality = len(Type.dict_modality) + 1
            d = {id_modality : {"type" : self.nom_type , "value" : self.value, "proba d'apparition" : self.proba_apparition}}
            Modality.dict_modality.update(d)
            print(dict_modality)
        else : 
            return "The modality has no type associated please check your spelling"
        

    def delete_modality(self):
        n = len(Modality.dict_modality)
        for k in range(0 , n):
            if Modality.dict_modality[str(k)]["value"] == self.value and Modality.dict_modality[str(k)]["type"] == self.nom_type:
                self.proba_apparition = 0
        

