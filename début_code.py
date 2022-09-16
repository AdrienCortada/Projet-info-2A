import json
from fastapi import FastAPI
import uvicorn
import random
import pandas as pd

app = FastAPI()

dict = '''{}'''
jeu_donnée = '''{}'''
type_list = []

@app.get("/")
async def hello():
    return "hello"

@app.get("/add_type/")
async def add_type(type : str, remplissage : int):
    if remplissage <= 100 and remplissage >= 0:
        global dict
        type_list.append(type)
        dict = json.loads(dict)
        d = {type : {"remplissage" : remplissage }}
        dict.update(d)
        dict = json.dumps(dict)
        return dict
    else:
        return "Please select a value between 0 and 100 for remplissage"

@app.get("/add_modality/")
async def add_modality(type : str, clef: str,  modality):
    global dict
    if type in type_list:
        dict = json.loads(dict)
        d = {clef: modality}
        dict[type].update(d)
        dict = json.dumps(dict)
        return dict
    else:
        return "sorry the type you selected doesn't exist please check the spelling"
        

@app.get("/delete_type/")
async def delete_type(type : str):
    global dict
    dict = json.loads(dict)
    if type in type_list:
        del dict[type]
    else:
        return "sorry the type you selected doesn't exist please check the spelling"
    dict = json.dumps(dict)
    return dict

@app.get("/delete_modality/")
async def delete_type(type : str, clef : str):
    global dict
    dict = json.loads(dict)
    if type in type_list:
        if clef in dict[type]:
            del dict[type][clef]
        else : 
            return "sorry the modality you selected doesn't exist please check the spelling"
    else:
        return "sorry the type you selected doesn't exist please check the spelling"
    dict = json.dumps(dict)
    return dict

@app.get("/import_dict/")
async def import_dict(chemin):
    global dict
    with open(chemin, 'r') as j:
        dict = json.loads(j.read())
        dict = json.dumps(dict, indent = 2, sort_keys = True)

@app.get("/print_dict/")
async def print_dict():
    global dict
    dict = json.loads(dict)
    dict = json.dumps(dict, indent = 2, sort_keys = True)
    return dict

@app.get("/clear_dict/")
async def clear_dict():
    global dict
    dict = '''{}'''
    return dict 

@app.get("/générer_jeu_donnée/")
async def générer_jeu_donnée(Nb, mq):
    Nb = int(Nb)
    global dict
    dict = json.loads(dict)
    global jeu_donnée
    jeu_donnée = json.loads(jeu_donnée)
    for n in range(0, Nb-1):
        n = int(n)
        individu_n = {}
        for k in dict:
            type = k
            tx_r = dict[type]["remplissage"]
            tx_r = int(tx_r)
            if 100*random.random() < tx_r :
                mod_list = dict[type].values()
                mod_list = list(mod_list)
                mod_list.remove(str(tx_r))
                m = len(mod_list)
                nb = random.randint(0, m-1)
                mod = mod_list[nb]
                individu_n[type] = mod
            else : 
                individu_n[type] = str(mq)
            donnée = {n : individu_n}
            jeu_donnée.update(donnée)
    dict = json.dumps(dict)
    jeu_donnée = json.dumps(jeu_donnée)
    return jeu_donnée

@app.get("/export_to_csv/")
async def export_to_csv(chemin):
    global jeu_donnée
    df = pd.read_json(jeu_donnée)
    df.to_csv(chemin , header= ",")

@app.get("/export_to_json/")
async def export_to_json(name):
    global jeu_donnée
    with open(name + ".json", 'w') as out_file:
        json.dump(jeu_donnée, out_file, indent = 4)


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)