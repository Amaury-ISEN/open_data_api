# Pour gérer les ObjectId Mongo :
from pydantic import BaseModel, Field
from bson import ObjectId

# Création d'un modèle d'objet pour nos documents, héritant de la classe BaseModel de Pydantic 
class Item (BaseModel):
    id: ObjectId = Field(alias='_id') # Création d'un alias (Pydantic n'accepte pas les _ en début de field name)
    datasetid: str
    recordid: str
    fields_: object = Field(alias="fields") # "fields" étant réservé par un attribut de BaseModel, il faut un alias
    libelle_epci: str
    libelle_region: str
    filiere: str
    code_region: int
    libelle_iris: str
    partr: float
    libelle_grand_secteur: str
    operateur: str
    code_naf: str
    conso: float
    code_epci: str
    code_grand_secteur: str
    code_commune: str
    libelle_commune: str
    annee: str
    thermor: float
    libelle_departement: str
    indqual: int
    pdl:int
    code_departement: str
    code_iris: str
    nombre_mailles_secretisees: int

    class Config: # Sous-classe de configuration de notre modèle
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
# Pour gérer les id sur une base mongo existante avec des ObjectId (que Pydantic ne supporte pas nativement),
# créons une classe de validation personnalisée pour que Pydantic sache gérer ces objets :

class PyObjectId(ObjectId): # Hérite de la classe ObjectID de bson

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Vérifie que la data reçue est valide pour la classe PyObjectId? Un string devient aussi un ObjectId valide."""
        if not ObjectId.is_valid(v):
            raise ValueError("ObjectId non valide")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        """Cette méthode sert à éviter une erreur lors de l'accès à la documentation."""
        field_schema.update(type="string")
