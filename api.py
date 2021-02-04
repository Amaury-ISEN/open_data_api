from typing import Optional
from fastapi import FastAPI
import uvicorn # ASGI server
from data import DataAccess as da
from fastapi.encoders import jsonable_encoder
from urllib.parse import urlparse

# from models import Item

app = FastAPI(redoc_url=None)

@app.get("/")
async def read_root():
    return {"Hello":"World"}

# Renvoyer les données pour toute une filière (gaz/électricite) :
@app.get("/items")
def get_filiere_reg(fil: str = None, reg: int = None):
    print(fil)
    print(reg)
    if reg == None : # Ne récupérer que la filière complète si pas de code région
        da.connexion()
        data = da.get_filiere(fil = str(fil))
        da.deconnexion()
        return data

    elif fil != None and reg != None : # Récupérer la filière pour une région si filière et code région sont renseignés
        print("coucou")
        da.connexion()
        data = da.get_filiere_region(fil = str(fil), reg = int(reg))
        da.deconnexion()
        return data

# # Renvoyer les données pour toute une filière (gaz/électricite) et pour une région donnée (code région insee) :
# @app.get("/items")
# def get_filiere_region(fil: str, reg:int):
#     da.connexion()
#     data = da.get_filiere_region(fil = str(fil), reg = str(reg))
#     da.deconnexion()
#     return data

# Supprimer un document particulier :
@app.delete("/items/{item_id}")
def del_doc(item_id: str):
    da.connexion()
    da.del_doc(item_id)
    da.deconnexion()
    return {"Document supprimé"}

@app.get("/items/conso")
def get_somme_fil(fil: str):
    da.connexion()
    data = da.get_somme_fil(fil)
    da.deconnexion()
    return data

# # Run avec auto-reload dès que l'on sauvegarde le code :
# if __name__ == "__main__":
#     uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

# Run sans auto-reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)