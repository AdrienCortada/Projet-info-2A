class Type:

    dict_type = {}


    def __init__(self, tx_remplissage : float, nom : str):
        self.tx_remplissage = tx_remplissage
        self.nom = nom

    def add_type(self):
        if self.tx_remplissage <= 100 and self.tx_remplissage >= 0:
            id = len(Type.dict_type) + 1
            d = {self.nom : {"remplissage" : self.tx_remplissage, "id" : id}}
            Type.dict_type.update(d)
            print(Type.dict_type)
        else : 
            return "Please select a value between 0 and 100 for tx_remplissage "

    def delete_type(self):
        if self.nom in Type.dict_type:
            del Type.dict_type[self.nom]
            print(Type.dict_type)
        else:
            return "The type you selected hasn't been added yet please check your spelling"

test = Type(100, "test")
test2 = Type(0, "test2")
test3 = Type(50, "test3")
Type.add_type(test)
Type.add_type(test2)
Type.add_type(test3)

Type.delete_type(test)