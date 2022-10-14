from abc import ABC, abstractmethod
class Export(ABC):
    def __init__(self,chemin):
        self.chemin = chemin
    @abstractmethod
    def export(self):
        pass