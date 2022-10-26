from business_object.regle_generation.typ import Type

class Meta_type:

    dict_meta_type = {}

    def __init__(self, nom : str, list_type : list[Type]):
        self.nom = nom
        self.list_type = self.list_type
    
    def add_meta_type(self):
        n = len(self.list_type)
        res = 0
        for k in range(0, n):
            if self.list_type[k] in Type.dict_type:
                res = res + 1
        if res == n :
            dic = {self.nom : self.list_type}
            Meta_type.dict_meta_type.update(dic)
        else : 
            return "All type selected are nom define please check the spelling"
            
            
    def delete_meta_type(self):
        if self.nom in Meta_type.dict_meta_type : 
            del Meta_type.dict_meta_type[self.nom]
        else : 
            return "Please check youre spelling" 