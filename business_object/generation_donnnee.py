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
        
    def generer_jeu_donnee(self):
        dict_ = """{}"""
        for n in range(Nb):
            indivivu_n = {}
            for k in self.types:
                tx_r = int(self.types[k]["remplissage"])
                if 100*random.random() < tx_r :
                    mod_list = self.types[k].values()
                
                
            
            
    def print_data(self):
    
    def clear_data(self):
        