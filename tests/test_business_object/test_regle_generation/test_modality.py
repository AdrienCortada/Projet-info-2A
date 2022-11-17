from business_object.regle_generation.typ import Type
from business_object.regle_generation.modality import Modality

if __name__ == "__main__":
    m = Modality("age", 100, 22)
    m1 = m.add_modality()
    if m1 == "The modality has no type associated please check your spelling":
        print("True")
    else:
        print("False")
    t = Type(100, "age")
    t.add_type()
    m2 = m.add_modality()
    if m2 == {1: {'type': 'age', 'value': 22, "proba d'apparition": 100}}: 
        print("True")
    else:
        print("False")
    m3 = Modality.delete_modality("age", 22)
    if m3 == {1: {'type': 'age', 'value': 22, "proba d'apparition": 0}}:
        print("True")
    else :
        print("False")
