import json
from business_object.regle_generation.meta_type import Meta_type
from business_object.regle_generation.modality import Modality
from business_object.regle_generation.typ import Type
import random
class Generation_donnee:
    def __init__(self,Nb : int, meta_type : Meta_type):
        self.Nb = Nb
        self.meta_type = meta_type
       
        
    def generer_jeu_donnee(self):
        donnee = {}
        for n in range(Nb):
            indivivu_n = {}
            for k in self.meta_type:
                type_individu_n = Type()
                tx_r = int(type_individu_n[k]["remplissage"])
                if 100*random.random() < tx_r :
                    mod_list = list(self.Mod[k].values())
                    mod_list.remove(tx_r)
                    m = len(mod_list)
                    nb = random.randint(0, m-1)
                    mod = mod_list[nb]
                    indivivu_n[k] = mod
                else :
                    indivivu_n[k] = str(mq)
                donnee = {n : indivivu_n}
                jeu_donnee.update(donnee)
        jeu_donnee = json.dumps(jeu_donnee)
        return json.dumps(jeu_donnee)            

if __name__ == "__main__":
    import doctest
    doctest.testmod()