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

# Renvoyer les données pour toute une filière (gaz/électricite) et ou toute une région :
@app.get("/items")
async def get_filiere_reg(fil: str = None, reg: int = None):

    if reg == None : # Ne récupérer que la filière complète si pas de code région
        da.connexion()
        data = da.get_filiere(fil = str(fil))
        da.deconnexion()
        return data

    elif fil != None and reg != None : # Récupérer la filière pour une région si filière et code région sont renseignés
        da.connexion()
        data = da.get_filiere_region(fil = str(fil), reg = int(reg))
        da.deconnexion()
        return data


    elif fil == None and reg != None : # Récupérer toute une région si un code région est renseigné
        da.connexion()
        data = da.get_region(reg = int(reg))
        da.deconnexion()
        return data


# Total consommation d'une filière
@app.get("/items/conso")
async def get_conso(fil: str = None, reg: int = None, dep: int = None):

    da.connexion()
    data = da.get_conso(fil = fil, reg = reg, dep = dep)
    da.deconnexion()
    return data





################################## AMAURY ########################################################################

# Renvoyer les données pour toute une filière (gaz/électricite) et pour une région donnée (code région insee) :
@app.get("/items")
def get_filiere_region(fil: str, reg:int):
    da.connexion()
    data = da.get_filiere_region(fil = str(fil), reg = str(reg))
    da.deconnexion()
    return data


@app.get("/items/conso/{code_departement}/{filiere}")
def get_conso_total_departement(code_departement: str,filiere: str):
    da.connexion()
    data = da.get_conso_total_departement(code_departement,filiere)
    da.deconnexion()
    return data

# Supprimer un document particulier :
@app.delete("/items/del={item_id}")
async def del_doc(item_id: str):
    da.connexion()
    da.del_doc(item_id)
    da.deconnexion()
    return {"Document supprimé"}

################################## LUIGI ########################################################################

@app.get("/items/conso/{code_departement}/{filiere}")
def get_conso_total_departement(code_departement: str,filiere: str):
    da.connexion()
    data = da.get_conso_total_departement(code_departement,filiere)
    da.deconnexion()
    return data

@app.put("/items/conso/update/{recordid}/{champs}/{donnee}")
def put_update_document(recordid: str,champs: str,donnee):
    da.connexion()
    da.put_update_document(recordid,champs,donnee)
    da.deconnexion()

################################## CHRISTIAN ########################################################################

# # Données d'une région
@app.get("/items/region/{id}")
def get_region(id: int):
    da.connexion()
    da.del_doc(id)
    data = da.get_region(id)
    da.deconnexion()
    return data


# # Total consommation d'une filière
@app.get("/items/consofil/{fil}")
def get_somme_fil(fil: str):
    da.connexion()
    data = da.get_somme_fil(fil)
    da.deconnexion()
    return data

##########################################################################################################################################################################


# # Run avec auto-reload dès que l'on sauvegarde le code :
# if __name__ == "__main__":
#     uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

# Run sans auto-reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)