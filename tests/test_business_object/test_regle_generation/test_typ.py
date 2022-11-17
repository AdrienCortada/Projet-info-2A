from business_object.regle_generation.typ import Type

t = Type(100, "age")
dic1 = t.add_type()
dic3  =  Type.delete_type("prenom")

if __name__ == "__main__":
    if dic1 == {'age': {'remplissage': 100, 'id': 1}}:
        print("True") 
    else:
        print("False")
    dic2 = Type.delete_type("age")
    if dic2 == {}:
        print("True") 
    else:
        print("False")
    dic3  =  Type.delete_type("prenom")
    if dic3 == "The type you selected hasn't been added yet please check your spelling":
        print("True") 
    else:
        print("False")
