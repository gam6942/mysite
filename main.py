# API processing back-end

from flask import Flask, render_template, request, session
from os import urandom as r_byte
from py.login import login
from py.mkt_1 import mkt_1
from py.mkt_2 import mkt_2
from py.mkt_3 import mkt_3
from py.adm_1 import adm_1

app = Flask(__name__, template_folder="html", static_folder="static")
app.secret_key = r_byte(50).hex()

@app.get("/")
def get():

    return render_template("login.html")

@app.post("/")
def post():

    #fonction d'authentification
    try:
        if request.get_json()["login"] and request.get_json()["password"]:

            session["mkt"] = r_byte(20).hex()
            session["adm"] = r_byte(20).hex()
            return login(session.get("mkt"),session.get("adm"))
    except:
        pass

    #fonction mkt_1

    try:
        if request.get_json()["mkt_1"] == "afficher" and request.cookies.get("marketing") == session.get("mkt"):

            return mkt_1()
    except:
        pass

    #fonction mkt_2
    try:
        if request.get_json()["mkt_2"] == "afficher" and request.cookies.get("marketing") == session.get("mkt"):

            return mkt_2()
    except:
        pass

    #fonction mkt_3
    try:
        if 0 < int(request.get_json()["mkt_3"]) < 10000000 and request.cookies.get("marketing") == session.get("mkt"):

            return mkt_3()
    except:
        pass

    #fonction adm_1

    try:
        if request.get_json()["adm_1"] and request.cookies.get("administrateur") == session.get("adm"):

            return adm_1()
    except:
        pass

    #requête non conforme aux attentes de l'API, retour d'information

    return """<div class="alg_row_center">refus: droit ou perimetre d'application.</div>"""

