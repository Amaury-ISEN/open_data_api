from pymongo import MongoClient

class DataAccess :
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
        id = str(id)
        cls.db.conso.delete_one({"record_id":id})

    @classmethod
    def get_filiere(cls, q):
        """Affiche toute la filière Electricité/Gaz selon la query passée en Get dans l'URL à l'api."""
        q = str(q)
        if q == "electricite" :
            cur = cls.db.conso.aggregate([
                { '$match': {
                    "fields.filiere":"Electricité"}
                },
                { '$unset' : "_id" } # Ne pas prendre les ObjectId
            ])
            resultat = [doc for doc in cur]
            return resultat


        elif q == "gaz" :
            cur = cls.db.conso.aggregate([
                { '$match': {
                    "fields.filiere":"Gaz"}
                },
                { '$unset' : "_id" } # Ne pas prendre les ObjectId
            ])
            resultat = [doc for doc in cur]
            return resultat

        # cur = cls.db.conso.find({"_id":q})
        # cur = cls.db.conso.find({ "fields.filiere" : "Electricité" }) # Utilisation de la dot notation mongodb pour les champs nestés
        # doc = []
        # for el in cur :
        #     doc.append(el)
        # print(doc)
        # doc = jsonable_encoder(doc[0])
        else :

            return "Donnée Inexistante"
##################################FONCTIONS-LUIGI########################################################################
          
    @classmethod
    def get_conso_total_departement(cls,code_dep,filiere):

        if filiere == "gaz":
            resultat = cls.db.conso.aggregate([{'$match':{"fields.filiere":"Gaz","fields.code_departement":code_dep}},
                                    {"$group": {"_id" :(code_dep,"Gaz"), "total": { "$sum": "$fields.conso" }}}])
            return list(resultat)
            
        elif filiere == "électricité":
            resultat = cls.db.conso.aggregate([{'$match':{"fields.filiere":"Electricité","fields.code_departement":code_dep}},
                                    {"$group": {"_id" :(code_dep,"Electricité"), "total": {"$sum":"$fields.conso"}}}])       
            return list(resultat)

        else:
            return "Données Inexisantes"
    
    @classmethod
    def put_update_document(cls,recordid,champs,donnee):
        
        recordid = str(recordid)
        champs = str(champs)
        
        before_update = cls.db.conso.find({"recordid":recordid})
        #list(before_update)
        
        
        champs = "fields." + str(champs)
        
        cls.db.conso.update_one({"recordid":recordid},{"$set":{champs:donnee}})

        after_update = cls.db.conso.find({"recordid":recordid})
        #list(after_update)
        
        #return before_update,after_update

