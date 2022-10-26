import json
from fastapi import FastAPI
import uvicorn
import random
import pandas as pd
from typ import Type
from modality import Modality

app = FastAPI()

@app.put("/add_type/")
async def add_type(nom : str, tx_remplissage : float):
    t = Type(tx_remplissage, nom)
    return t.add_type()

@app.delete("/delete_type/")
async def delete_type(nom : str):
    return Type.delete_type(nom)

@app.put("/add_modality/")
async def add_modality(nom_type, proba_apparition, value):
    m = Modality(nom_type, proba_apparition, value)
    return m.add_modality()

@app.delete("/delete_modality")
async def delete_modality(nom_type : str, value):
    return Modality.delete_modality(nom_type, value)

    

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)