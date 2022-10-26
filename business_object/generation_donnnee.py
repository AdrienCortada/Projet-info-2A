import json
from business_object.regle_generation.typ import Type
from business_object.regle_generation.modality import Modality
from business_object.regle_generation.meta_type import Meta_type
import random
class Generation_donnee:
    jeu_donnee = {}

    def __init__(self,Nb : int, meta_type ):
        self.Nb = Nb
        self.meta_type = meta_type
       
        
    def generer_jeu_donnee(self):
        for n in range(self.Nb):
            indivivu_n = {}
            for k in Meta_type.dict_meta_type[self.meta_type]:
                type_individu_n = Type.dict_type
                tx_r = int(type_individu_n[k]["remplissage"])
                if 100*random.random() < tx_r :
                    mod_list = []
                    for i in Modality.dict_modality:
                        if Modality.dict_modality[i]["type"] == k:
                            mod_list.append([Modality.dict_modality[i]["value"],Modality.dict_modality[i]["proba d'apparition"]])
                    m = len(mod_list)
                    weight = 0
                    for i in range(0, m):
                        weight = mod_list[i][1]+weight
                    mod_list[0][1] = (mod_list[i][1]/weight)*100
                    for i in range(1, m):
                        mod_list[i][1] = (mod_list[i][1]/weight)*100 + mod_list[i-1][1]
                    randfloat = random.uniform(0,100)
                    for i in range(0, m):
                        if randfloat < mod_list[0][1]:
                            mod = mod_list[0][0]
                        else:
                            if randfloat > mod_list[i-1][1] and randfloat < mod_list[i][1] :
                                mod = mod_list[i][0]
                    indivivu_n[k] = mod
                else :
                    indivivu_n[k] = str(mq)
                Generation_donnee.jeu_donnee = {n : indivivu_n}
                Generation_donnee.jeu_donnee.update(Generation_donnee.jeu_donnee)
            Generation_donnee.jeu_donnee = json.dumps(Generation_donnee.jeu_donnee)
        return Generation_donnee.jeu_donnee           
