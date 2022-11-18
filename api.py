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
from business_object.export.export_to_xml import Export_to_xml
from business_object.export.export_to_csv import Export_to_csv
from business_object.export.export_to_json import Export_to_json
from factory.data_factory import DataFactory
from factory.meta_factory import MetaFactory
from factory.modality_factory import ModalityFactory
from factory.typ_factory import TypeFactory
from dao.data_dao import DataDao
from dao.db_connection import DBConnection
from dao.meta_dao import MetaDao
from dao.modality_dao import ModalityDao
from dao.typ_dao import TypeDao



tags_metadata = [{"name" : "Type"},{"name" : "Modality"},{"name": "Import"},{"name" : "Meta-Type"},{"name" : "Génération"},{"name" : "Export"}, {"name" : "Dao"}]


app = FastAPI(openapi_tags=tags_metadata)

@app.get("/get_dict_type", tags = ["Type"])
async def get_type():
    return Type.dict_type

@app.put("/add_type/", tags = ["Type"])
async def add_type(nom : str, tx_remplissage : float):
    t = Type(tx_remplissage, nom)
    return t.add_type()

@app.delete("/delete_type/", tags = ["Type"])
async def delete_type(nom : str):
    return Type.delete_type(nom)

@app.get("/get_dict_modality", tags = ["Modality"])
async def get_modality():
    return Modality.dict_modality

@app.put("/add_modality/", tags = ["Modality"])
async def add_modality(nom_type : str, proba_apparition : float, value):
    m = Modality(nom_type, proba_apparition, value)
    return m.add_modality()

@app.delete("/delete_modality", tags = ["Modality"])
async def delete_modality(nom_type : str, value):
    return Modality.delete_modality(nom_type, value)

@app.put("/import_json/", tags = ["Import"])
async def import_json(chemin : "str"):
    imp = IMPORTJSON(chemin)
    return imp.import_dict()

@app.get("/get_dict_meta_type", tags = ["Meta-Type"])
async def get_meta_type():
    return Meta_type.dict_meta_type

@app.put("/add_meta_type/", tags = ["Meta-Type"])
async def add_meta_type(nom : str, list_type : list):
    mt = Meta_type(nom, list_type)
    return mt.add_meta_type()

@app.delete("/delete_meta_type/", tags = ["Meta-Type"])
async def delete_meta_type(nom_meta_type : str):
    return Meta_type.delete_meta_type(nom_meta_type)


@app.put("/generation_de_donnee/", tags = ["Génération"])
async def generation_donnee(Nb : int, meta_type ):
    gd = Generation_donnee(Nb, meta_type)
    return gd.generer_jeu_donnee()

@app.get("/export/", tags = ["Export"])
async def export(chemin : str, name : str):
    return None

@app.get("/export_donnees_to_json/", tags = ["Export"])
async def export_json(chemin : str , name : str):
    x = Export_to_json(chemin, name)
    dic = json.dumps(Generation_donnee.jeu_donnee)
    return x.export(dic)

@app.get("/export_donnees_to_xml/", tags = ["Export"])
async def export_xml(chemin : str , name : str):
    x = Export_to_xml(chemin, name)
    dic = json.dumps(Generation_donnee.jeu_donnee)
    return x.export(dic)

@app.get("/export_donnees_to_csv/", tags = ["Export"])
async def export_csv(chemin : str , name : str):
    c = Export_to_csv(chemin, name)
    dic = json.dumps(Generation_donnee.jeu_donnee)
    return c.export(dic)

@app.put("/sauvegarder_en_base_de_donnees/", tags = ["Dao"])
async def save_data_dao():
    donnee = DataDao()
    meta = MetaDao()
    typ = TypeDao()
    modalite = ModalityDao()
    meta.save_meta(Meta_type(Meta_type.meta_type1[-1], Meta_type.dict_meta_type[Meta_type.meta_type1[-1]]))
    for elt in Meta_type.dict_meta_type[Meta_type.meta_type1[-1]] : 
        typ.save_type(Type(Type.dict_type[elt]["remplissage"], elt))
    for mod in Modality.dict_modality :
        modalite.save_modality(Modality(mod["id_modality"]["type"], mod["id_modality"]["proba d'apparition"], mod["id_modality"]["value"]))
    donnee.save_data(Generation_donnee.jeu_donnee)

    




if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)