from abc import ABC, abstractmethod
from business_object.generation_donnee import Generation_donnee

class Export(ABC):
    json_obj = Generation_donnee.jeu_donnee
    def __init__(self,chemin : str, name:str):
        self.chemin = chemin
        self.name = name

    @abstractmethod
    def export1(self):
        pass