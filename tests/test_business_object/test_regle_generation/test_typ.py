from business_object.regle_generation.typ import Type



if __name__ == "__main__":
    t = Type(100, "age")
    dic1 = t.add_type()
    if dic1 == {'age': {'remplissage': 100, 'id': 1}}:
        print("True") 
    else:
        print("False")
    dic2 = Type.delete_type("age")
    if dic2 == {}:
        print("True") 
    else:
        print("False")

