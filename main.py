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

    json = request.get_json()

    #fonction d'authentification
        
    if "login" in json and "password" in json:

        session["mkt"] = r_byte(20).hex()
        session["adm"] = r_byte(20).hex()

        return login(session.get("mkt"),session.get("adm"))
    
    #fonction mkt_1

    if "mkt_1" in json and request.cookies.get("marketing") == session.get("mkt"):
        
        return mkt_1() 

    #fonction mkt_2

    if "mkt_2" in json and request.cookies.get("marketing") == session.get("mkt"):            
        
        return mkt_2() 

    #fonction mkt_3

    if "mkt_3" in json and request.cookies.get("marketing") == session.get("mkt"):    
        
        if 0 < int(json["mkt_3"]) < 10000000:        
            
            return mkt_3() 

    #fonction adm_1 

    if "adm_1" in json and request.cookies.get("administrateur") == session.get("adm"):
        
        return adm_1()

    #requête non conforme aux attentes de l'API, retour d'information

    return """<div class="alg_row_center">refus: droit ou perimetre d'application.</div>"""