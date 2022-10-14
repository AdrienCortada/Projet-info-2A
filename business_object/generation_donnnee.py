import json
from business_object.regle_generation.meta_type import Meta_type
from business_object.regle_generation.modality import Modality
from business_object.regle_generation.type import Type
import random
class Generation_donnee:
    def __init__(self,Nb : int, meta_type : Meta_type, Mod : Modality, types : Type):
        self.Nb = Nb
        self.Mod = Mod
        self.meta_type = meta_type
        self.types = types
        
    def generer_jeu_donnee(self, jeu_donnee):
        if len(self.jeu_donnee) == 0 :
            for n in range(Nb):
                indivivu_n = {}
                for k in self.types:
                    tx_r = int(self.types[k]["remplissage"])
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
            return jeu_donnee
        else :
            return json.dumps(jeu_donnee)            

if __name__ == "__main__":
    import doctest
    doctest.testmod()