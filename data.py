from pymongo import MongoClient
import werkzeug

class DataAccess :
    @classmethod
    def connexion(cls):
        cls.client = MongoClient("localhost", 27017)
        cls.db = cls.client["db"]

    @classmethod
    def deconnexion(cls):
        cls.client.close()

    # Récupérer les données pour toute une filière :
    @classmethod
    def get_filiere(cls, fil):
        """Affiche toute la filière Electricité/Gaz selon la query passée en Get dans l'URL à l'api."""
        fil = str(fil)
        if fil == "gaz": fil = "Gaz"
        if fil == "electricite": fil = "Electricité"
        cur = cls.db.conso.aggregate([
            { '$match': {
                "fields.filiere":fil}
            },
            { '$unset' : "_id" } # Ne pas prendre les ObjectId
        ])
        resultat = [doc for doc in cur]

        if len(resultat) != 0:
            return resultat
        else : return {"Les deux filières possibles sont 'gaz' et 'electricite' en minuscules et sans accent."}

    # Récupérer les données pour toute une région
    @classmethod
    def get_region(cls, reg):
        reg = int(reg)
        resultat = cls.db.conso.aggregate([
            {'$match': {
                "fields.code_region": reg}
            }])
        return resultat

    @classmethod
    def get_filiere_region(cls, fil, reg):
        """Renvoie tous les documents pour une filière ainsi qu'une région donnée (avec son code région INSEE)"""
        fil = str(fil)
        if fil == "gaz": fil = "Gaz"
        if fil == "electricite": fil = "Electricité"
        reg = int(reg)
        resultat = cls.db.conso.aggregate([
                    {'$match': {
                        "fields.code_region": reg,
                        "fields.filiere": fil}
                    },
                    {"$unset":"_id"}
                    ])
        resultat = [r for r in resultat]
        return resultat
    
    @classmethod
    def del_doc(cls, id):
        """Supprime un document en base"""
        print(id)
        id = str(id)
        print(id)
        cls.db.conso.delete_one({"record_id":id})

    # Récupérer la consommation totale pour toute une filière
    @classmethod
    def get_somme_fil(cls, fil):
        fil = str(fil)
        if fil == "gaz": fil = "Gaz"
        if fil == "electricite": fil = "Electricité"
        result = cls.db.conso.aggregate([
            {"$match": {"fields.filiere":fil}},
            {"$group": {"_id":fil,
                       "conso_totale":{"$sum":"$fields.conso"}}
            }
            ])
        result = [r for r in result]
        return result
