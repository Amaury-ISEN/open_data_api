from typing import Optional
from fastapi import FastAPI
from flask.json import jsonify
import uvicorn # ASGI server
from data import DataAccess as da
from fastapi.encoders import jsonable_encoder



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}


# Renvoyer les données pour toute une filière (gaz/électricité) :
@app.get("/items/{q}")
def get_filiere(q: str):
    da.connexion()
    data = da.get_filiere(q)
    da.deconnexion()
    return data

##################################API-LUIGI########################################################################

@app.get("/items/conso/{code_departement}/{filiere}")
def get_conso_total_departement(code_departement: str,filiere: str):
    da.connexion()
    data = da.get_conso_total_departement(code_departement,filiere)
    da.deconnexion()
    return data

@app.put("/items/conso/update/{recordid}/{champs}/{donnee}")
http://127.0.0.1:9000/items/conso/update/e24759abc1075f7b9ca22823383298c241cba54e/libelle_grand_secteur/petpet
def put_update_document(recordid: str,champs: str,donnee):
    da.connexion()
    da.put_update_document(recordid,champs,donnee)
    da.deconnexion()
    

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=9000,reload=True)