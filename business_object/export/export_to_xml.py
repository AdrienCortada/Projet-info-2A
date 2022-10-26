from export.py import Export

class Export_to_xml(Export) : 
    def __init__(self, chemin, json_file) :
        super().__init__(chemin, json_file)
    
    def export(self) :
        