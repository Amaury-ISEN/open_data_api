from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import requests
from fastapi import FastAPI
import uvicorn

URL_API = "http://127.0.0.1:5000/items"

app = Flask(__name__)


@app.route("/items")
def index():
    reponse = requests.get(URL_API)
    content = json.load(reponse.content.decode("utf-8"))
    return render_template("index.html", donnees=content)


# Supprimer un document particulier :
@app.route("/items/{item_id}")
def del_doc(item_id):
    url = URL_API + "/" + item_id
    requests.delete(url)
    return redirect(url_for('index'), code=302)


# Renvoyer les données pour toute une filière (gaz/électricité) :
@app.route("/")
def get_filiere(item_id):
    url = URL_API + "/" + item_id
    reponse = requests.get(url)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template(".html", contenu=content)


# Données d'une région
@app.route("/")
def get_region(item_id):
    url = URL_API + "/" + item_id
    reponse = requests.get(url)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template(".html", contenu=content)


# Total consommation d'une filière
@app.get("/items/consofil/{fil}")
def get_somme_fil(fil):
    url = URL_API + "/" + fil
    reponse = requests.get(url)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template(".html", contenu=content)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
