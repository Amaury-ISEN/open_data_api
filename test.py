from flask import Flask, render_template, redirect, request as flaskrequest
# Pour les requêtes EXTERNES à flask :
import requests
import json

app = Flask(__name__)

URL_API = "http://127.0.0.1:8000/items"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filtrer", methods=["POST"])
def filtrer():
    reg = flaskrequest.form['reg'] # Récup du form html
    donnees = [] # Liste qu'on va envoyer au graphique highchart 

    if reg == '0': # Si l'utilisateur choisit toutes les régions :
        titre = "Consommation en énergie des régions (en 2020)"
        donnees.append(titre)

        liste_reg = ["11 - Île-De-France","24 - Centre-Val de Loire","27 - Bourgogne-Franche-Comté",
                    "28 - Normandie","32 - Hauts-de-France","44 - Grand Est","52 - Pays de la Loire",
                    "53 - Bretagne","75 - Nouvelle-Aquitaine","76 - Occitanie","84 - Auvergne-Rhône-Alpes",
                    "93 - Provence-Alpes-Côte d'Azur","94 - Corse"]

        for reg in liste_reg: # On va récupérer les données ttes fils, gaz et elec pour chaque région

            # Ajout de 3 slots vides à la liste de données :
            donnees.append([])
            donnees.append([])
            donnees.append([])

            # Récup de tous les noms et codes régions :
            reg_nom, reg_code = traitement_reg(reg)

            # Récup données toutes filières pour la région choisie
            donnees_ttes_fil = recup_data(fil = None, reg_code = reg_code)

            # Récupération des données filière gaz pour la région choisie
            donnees_gaz = recup_data(fil = "gaz", reg_code = reg_code)

            # Récupération des données filière élec pour la région choisie
            donnees_elec = recup_data(fil = "electricite", reg_code = reg_code)

            donnees[1].append(donnees_ttes_fil)
            donnees[2].append(donnees_gaz)
            donnees[3].append(donnees_elec)
            donnees.append(liste_reg) # Donnees[4] sert à contenir les noms de régions à afficher en axe y

    else : # Si l'utilisateur choisit une région en particulier : 

        reg_nom, reg_code = traitement_reg(reg)

        titre = "Consommation en énergie de la région " + reg_nom + " (en 2020)"
        donnees.append(titre)

        # Récup données toutes filières pour la région choisie
        donnees_ttes_fil = recup_data(fil = None, reg_code = reg_code)
        donnees_ttes_fil = [donnees_ttes_fil]
        donnees.append(donnees_ttes_fil)

        # Récupération des données filière gaz pour la région choisie
        donnees_gaz = recup_data(fil = "gaz", reg_code = reg_code)
        donnees_gaz = [donnees_gaz] # Passage de la donnée sous forme de liste pour l'injecter plus facilement dans highchart
        donnees.append(donnees_gaz)

        # Récupération des données filière élec pour la région choisie
        donnees_elec = recup_data(fil = "electricite", reg_code = reg_code)
        donnees_elec = [donnees_elec] # Passage de la donnée sous forme de liste pour l'injecter plus facilement dans highchart
        donnees.append(donnees_elec)

        donnees.append(" ") # Donnees[4] sert à contenir les noms de régions à afficher en axe y, ici " " permet de ne rien afficher.

    return render_template("index.html", donnees = donnees)

############################
# Méthodes supplémentaires #
############################

def recup_data(fil, reg_code):
    """Récupération des données via l'API."""

    if fil == None: # Si toutes filières :
        reponse = requests.get(URL_API+"/conso?reg="+reg_code)
    else : # Si filière particulière :
        reponse = requests.get(URL_API+"/conso?fil="+fil+"&reg="+reg_code)

    contenu = json.loads(reponse.content.decode("utf-8"))

    if contenu == []: # Si la requête ne renvoie pas de valeur (ex gaz en Corse) :
        contenu = 0
    else: 
        contenu = contenu[0]["conso_totale"] # Récup de la valeur dans le dico json renvoyé par l'API
        contenu = round(contenu, 2) # Arondi à 2 des décimales de la conso
    return contenu

    

def traitement_reg(reg):
    '''Récupère une value de form de type "12 - Région-Machin" et renvoie le code à 2 chiffres et le nom de la région dans deux variables séparées.'''
    # Récupération du nom de région pour l'envoyer au graphique Highchart
    reg_nom = reg[4:]
    # Récupération du code de région en deux chiffres pour l'envoyer à l'API
    reg_code = reg[0:3]
    return reg_nom, reg_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)