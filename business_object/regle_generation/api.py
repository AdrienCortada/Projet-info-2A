import json
from fastapi import FastAPI
import uvicorn
import random
import pandas as pd
import json 
import xml
from business_object.regle_generation.typ import Type
from business_object.regle_generation.modality import Modality
from business_object.regle_generation.meta_type import Meta_type
from business_object.generation_donnee import Generation_donnee
from business_object.impor.import_json import IMPORTJSON
from business_object.export.export import Export
from business_object.export.export_to_xml import export_to_xml
from business_object.export.export_to_csv import export_to_csv


app = FastAPI()

@app.put("/add_type/")
async def add_type(nom : str, tx_remplissage : float):
    t = Type(tx_remplissage, nom)
    return t.add_type()

@app.delete("/delete_type/")
async def delete_type(nom : str):
    return Type.delete_type(nom)

@app.put("/add_modality/")
async def add_modality(nom_type : str, proba_apparition : float, value):
    m = Modality(nom_type, proba_apparition, value)
    return m.add_modality()

@app.delete("/delete_modality")
async def delete_modality(nom_type : str, value):
    return Modality.delete_modality(nom_type, value)

@app.put("/add_meta_type/")
async def add_meta_type(nom : str, list_type : list):
    mt = Meta_type(nom, list_type)
    return mt.add_meta_type()

@app.delete("/delete_meta_type/")
async def delete_meta_type(nom_meta_type : str):
    return Meta_type.delete_meta_type(nom_meta_type)

@app.put("/import_json/")
async def import_json(chemin : str):
    imp = IMPORTJSON(chemin)
    return imp.import_dict()

@app.put("/generation_de_donnee/")
async def generation_donnee(Nb : int, meta_type ):
    gd = Generation_donnee(Nb, meta_type)
    return gd.generer_jeu_donnee()

@app.put("/import_json/")
async def import_json(chemin : str ):
    imp = IMPORTJSON(chemin)
    return imp.import_dict()
    

@app.get("/export/")
async def export(chemin : str, name : str):
    return None

@app.get("/export_donnees_to_xml/")
async def export_xml(chemin : str , name : str):
    x = export_to_xml(chemin, name)
    dic = json.dumps(Generation_donnee.jeu_donnee)
    return x.export1(dic)

@app.get("/export_donnees_to_csv/")
async def export_csv(chemin : str , name : str):
    c = export_to_csv(chemin, name)
    dic = json.dumps(Generation_donnee.jeu_donnee)
    return c.export1(dic)


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)