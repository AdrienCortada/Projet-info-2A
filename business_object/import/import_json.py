import pandas as pd

class IMPORTJSON :
    def __init__(self, chemin_str) :
        self.chemin = chemin_str

    def import_dict(self) :
        metadonnees = pd.DataFrame.transpose(pd.read_json(self.chemin))
        if type(metadonnees.iloc[:,0]) != "str" :
            texte = """La première clé de chaque variable doit être le 'type' et doit être une chaine de caractères\nPar exemple, 
            le fichier json peut se présenter comme suit\n
            """
            raise Exception(texte)
        for i in range(metadonnees.shape[0]) :
            metadonnees.iloc[i,0] = metadonnees.iloc[i,0].split("|")
        return metadonnees

if __name__ == "__main__" :
    imp = IMPORTJSON("C:/Users\HP/Documents/GitHub/Projet-info-2A/json_test.json")
    print(imp.import_dict())