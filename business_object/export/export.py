from abc import ABC, abstractmethod
class Export(ABC):
    def __init__(self,chemin : str, json_file):
        self.chemin = chemin
        self.json_file = json_file
        
    @abstractmethod
    def export(self):
        pass