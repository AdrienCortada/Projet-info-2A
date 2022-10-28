from abc import ABC, abstractmethod
import json

class Export(ABC):
    def __init__(self,chemin : str, name:str):
        self.chemin = chemin
        self.name = name

    @abstractmethod
    def export(self):
        pass