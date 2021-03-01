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
        print("data 1")
        reg = int(reg)
        print("data 2")
        resultat = cls.db.conso.aggregate([
                {'$match': {
                    "fields.code_region": reg}
                },
                { '$unset' : "_id" } # Ne pas prendre les ObjectId
            ])
        print("data 3")
        print(resultat)
        return list(resultat)

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
        cls.db.conso.delete_one({"recordid":id})

    # Récupérer la consommation totale pour toute une filière
    @classmethod
    def get_conso_fil(cls, fil):
        fil = str(fil)
        if fil == "gaz": fil = "Gaz"
        if fil == "electricite": fil = "Electricité"
        resultat = cls.db.conso.aggregate([
            {"$match": {"fields.filiere":fil}},
            {"$group": {"_id":fil,
                       "conso_totale":{"$sum":"$fields.conso"}}
            }
            ])
        resultat = [r for r in resultat]
        return resultat

    @classmethod
    def get_conso(cls, reg, dep, fil):

        if dep != None : dep = str(dep)
        if reg != None : reg = int(reg)

        if fil != None :
            fil = str(fil)
            if fil == "gaz": fil = "Gaz"
            if fil == "electricite": fil = "Electricité"

        print("reg", reg)
        print("dep", dep)
        print("fil", fil)

        if fil!= None and dep == None and reg == None :
            print("a")
            resultat = cls.db.conso.aggregate([
                {'$match':{"fields.filiere":fil}},
                {"$group": {"_id" :fil,
                            "conso_totale": { "$sum": "$fields.conso" }}
                }
                ])
            return list(resultat)

        if fil != None and dep != None :
            print("b")
            resultat = cls.db.conso.aggregate([
                {'$match':{"fields.filiere":fil,
                            "fields.code_departement":dep}},
                {"$group": {"_id" :(dep,fil),
                            "conso_totale": { "$sum": "$fields.conso" }}
                }
                ])
            return list(resultat)

        if fil != None and reg != None :
            print("c")
            resultat = cls.db.conso.aggregate([
                {'$match':{"fields.filiere":fil,
                            "fields.code_region":reg}},
                {"$group": {"_id" :(reg,fil),
                            "conso_totale": { "$sum": "$fields.conso" }}
                }
                ])
            return list(resultat)

        if fil == None :
            if reg != None: 
                print("d")
                resultat = cls.db.conso.aggregate([
                    {'$match':{"fields.code_region":reg}},
                    {"$group": {"_id" :(reg),
                                "conso_totale": { "$sum": "$fields.conso" }}
                    }
                    ])
                return list(resultat)

            if dep != None: 
                print("e")
                resultat = cls.db.conso.aggregate([
                    {'$match':{"fields.code_departement":dep}},
                    {"$group": {"_id" :(dep),
                                "conso_totale": { "$sum": "$fields.conso" }}
                    }
                    ])
                return list(resultat)

        return list(resultat)




################################## LUIGI ########################################################################

    @classmethod
    def put_update_document(cls,recordid,champs,donnee):
        
        recordid = str(recordid)
        champs = str(champs)
        
        before_update = cls.db.conso.find({"recordid":recordid})
        #list(before_update)
        
        
        champs = "fields." + str(champs)
        
        cls.db.conso.update_one({"recordid":recordid},{"$set":{champs:donnee}})

        after_update = cls.db.conso.find({"recordid":recordid})
        list(after_update)
        
        return before_update,after_update


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