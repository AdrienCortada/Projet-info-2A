from business_object.regle_generation.typ import Type
from business_object.regle_generation.meta_type import Meta_type

if __name__ == "__main__":
    mt = Meta_type("individu", ["nom","age"])
    t1 = Type(100, "age")
    t2 = Type(100, "nom")
    t2.add_type()
    t1.add_type()
    mt1 = mt.add_meta_type()
    if mt1 == {'individu': ['nom', 'age']}:
        print("True")
    else:
        print("False")
    mt2 = Meta_type.delete_meta_type("individu")
    if mt2 == {}:
        print("True")
    else:
        print("False")