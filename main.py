from xml.etree.ElementTree import Element,tostring
from business_object.export.export import Export
from business_object.generation_donnee import Generation_donnee
# define a function to
# convert a simple dictionary
# of key/value pairs into XML
class Dict_to_xml:
    def __init__(self,tag):
        self.tag = tag
    def dict_to_xml(self,d : Generation_donnee.jeu_donnee):
        elem = Element(self.tag)
        for key, val in d.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
                
        return tostring(elem)

if __name__ == "__main__":
    s={
  "0": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "1": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "2": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "3": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "4": {
    "a": "aaaa",
    "aa": "aaaaaaaaaa"
  },
  "5": {
    "a": "aaaa",
    "aa": "aaaaaaaaaa"
  },
  "6": {
    "a": "aaaa",
    "aa": "aaaaaaaaaa"
  },
  "7": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaa"
  },
  "8": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "9": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaa"
  },
  "10": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "11": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "12": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaa"
  },
  "13": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "14": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "15": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaa"
  },
  "16": {
    "a": "aaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "17": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  },
  "18": {
    "a": "aaaa",
    "aa": "aaaaaaaaaa"
  },
  "19": {
    "a": "aaaaaaa",
    "aa": "aaaaaaaaaaaaa"
  }
}
    res = Dict_to_xml('data')
    print(res.dict_to_xml(s))
