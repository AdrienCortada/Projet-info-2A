import json
from fastapi import FastAPI
import uvicorn
import random
import pandas as pd
from typ import Type

app = FastAPI()

@app.get("/add_type/")
async def add_type(nom : str, tx_remplissage : float):
    t = Type(tx_remplissage, nom)
    t.add_type()
    return Type.dict_type


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)