class Type:

    dict_type = {}


    def __init__(self, tx_remplissage : float, nom : str):
        self.tx_remplissage = tx_remplissage
        self.nom = nom

    def add_type(self):
        id = len(Type.dict_type) + 1
        d = {str(id) : {"remplissage" : self.tx_remplissage, "nom": self.nom }}
        Type.dict_type.update(d)

    
test = Type(85, "test")
test2 = Type(89, "test2")

test.add_type()
test2.add_type()

print(Type.dict_type)