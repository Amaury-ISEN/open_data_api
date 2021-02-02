from pymongo import MongoClient, DESCENDING
import werkzeug


class DataAccess:
    @classmethod
    def connexion(cls):
        cls.client = MongoClient("localhost", 27017)
        cls.db = cls.client["db"]

    @classmethod
    def deconnexion(cls):
        cls.client.close()

    @classmethod
    def del_doc(cls, id):
        """Supprime un document en base"""
        print(id)
        id = str(id)
        print(id)
        cls.db.conso.delete_one({"record_id": id})

    @classmethod
    def get_filiere(cls, q):
        """Affiche toute la filière Electricité/Gaz selon la query passée en Get dans l'URL à l'api."""
        q = str(q)
        if q == "electricite":
            cur = cls.db.conso.aggregate([
                {'$match': {
                    "fields.filiere": "Electricité"}
                },
                {'$unset': "_id"}  # Ne pas prendre les ObjectId
            ])
            resultat = [doc for doc in cur]
            return resultat

        elif q == "gaz":
            cur = cls.db.conso.aggregate([
                {'$match': {
                    "fields.filiere": "Gaz"}
                },
                {'$unset': "_id"}  # Ne pas prendre les ObjectId
            ])
            resultat = [doc for doc in cur]
            return resultat

        else:
            return None

    ## Données pour une région
    @classmethod
    def get_region(cls, id):
        result = cls.collection.aggregate([
            {'$match': {
                "fields.code_region": id}
            }])
        return result
