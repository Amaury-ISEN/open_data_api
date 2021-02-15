from flask import Flask, render_template, redirect, request as flaskrequest
# Pour les requêtes EXTERNES à flask :
import requests
import json

app = Flask(__name__)

URL_API = "http://127.0.0.1:8000/items"


@app.route("/")
def index():
    return render_template("index.html")

def recup_data(fil, reg):
    reponse = requests.get(URL_API+"/conso?reg="+reg)
    contenu = json.loads(reponse.content.decode("utf-8"))
    if contenu == []:
        contenu = 0
    else:
        contenu = contenu[0]["conso_totale"]
        contenu = round(contenu, 2)
    donnees.append(contenu)


@app.route("/filtrer", methods=["POST"])
def filtrer():
    reg = flaskrequest.form['reg']
    donnees = []

    titre = "Consommation en énergie de la région " + reg + " (en 2020)"
    donnees.append(titre)

    # Récup données toutes filières pour la région choisie
    reponse = requests.get(URL_API+"/conso?reg="+reg)
    contenu = json.loads(reponse.content.decode("utf-8"))
    if contenu == []:
        contenu = 0
    else:
        contenu = contenu[0]["conso_totale"]
        contenu = round(contenu, 2)
    donnees.append(contenu)

    # Récupération des données filière gaz pour la région choisie
    fil = "gaz"
    reponse = requests.get(URL_API+"/conso?fil="+fil+"&reg="+reg)
    contenu = json.loads(reponse.content.decode("utf-8"))
    if contenu == []:
        contenu = 0
    else:
        contenu = contenu[0]["conso_totale"]
        contenu = round(contenu, 2)
    donnees.append(contenu)

    # Récupération des données filière élec pour la région choisie
    fil = "electricite"
    reponse = requests.get(URL_API+"/conso?fil="+fil+"&reg="+reg)
    contenu = json.loads(reponse.content.decode("utf-8"))
    if contenu == []:
        contenu = 0
    else:
        contenu = contenu[0]["conso_totale"]
        contenu = round(contenu, 2)
    donnees.append(contenu)

    print("donnees", donnees)

    return render_template("index.html", donnees = donnees)


if __name__ == "__main__":
    app.run(debug=True, port=5000)