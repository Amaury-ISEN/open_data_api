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
    reg = flaskrequest.form['reg']
    dep = flaskrequest.form['dep']
    fil = flaskrequest.form['fil']
    
    print(reg, dep, fil)

    # Consommation par filière
    if reg == '0' and dep == '0' and fil != '0':
        print("coucou")
        print(fil)
        reponse = requests.get(URL_API+"/conso?fil="+fil)
        print(reponse)
        contenu = json.loads(reponse.content.decode("utf-8"))
        print(contenu)
        contenu = contenu[0]["conso_totale"]
        return render_template("index.html", contenu = contenu)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)