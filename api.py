from typing import Optional
from fastapi import FastAPI
import uvicorn  # ASGI server
from data import DataAccess as da
from fastapi.encoders import jsonable_encoder

# from models import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Supprimer un document particulier :
@app.delete("/items/{item_id}")
def del_doc(item_id: str):
    da.connexion()
    da.del_doc(item_id)
    da.deconnexion()
    return {"Document supprimé"}


# Renvoyer les données pour toute une filière (gaz/électricité) :
@app.get("/items/{q}")
def get_filiere(q: str):
    da.connexion()
    data = da.get_filiere(q)
    da.deconnexion()
    return data


# Données d'une région
@app.get("/items/{id}")
def get_region(id: int):
    da.connexion()
    da.del_doc(id)
    data = da.get_region(id)
    da.deconnexion()
    return data


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
