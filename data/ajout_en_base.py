from pymongo import MongoClient
import json

chemin = './data/conso-elec-gaz-annuelle-par-naf-agregee-iris.json'

def ajout_documents_en_base (chemin) :
    # Création de l'objet client avec le port :
    client = MongoClient('localhost', 27017)

    # Création de la liste de documents à partir du fichier json :
    with open(chemin) as f:
        donnees = json.load(f)
        
    client.db.conso.insert_many(donnees)
    
ajout_documents_en_base(chemin)