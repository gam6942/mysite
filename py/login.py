# fonction d'authentification

from flask import request, make_response
from werkzeug.security import check_password_hash as check
import duckdb

def login(mkt_cookie_value,adm_cookie_value):

    login = request.get_json()["login"]
    password = request.get_json()["password"]

    db = duckdb.connect("mysite/db/db.duckdb")

    user = db.execute("""
        SELECT * from utilisateur
    """).fetchall()

    db.close()

    if login == user[0][0] and check(pwhash=user[0][1],password=password) == True and user[0][2] == 1: # marketing

        with open("mysite/html/mkt_1.html","rt") as html: # intégration des composants d'interface suite à l'authentification en marketing
            mkt_1_html = html.read()
        with open("mysite/html/mkt_2.html","rt") as html:
            mkt_2_html = html.read()
        with open("mysite/html/mkt_3.html","rt") as html:
            mkt_3_html = html.read()

        db = duckdb.connect("mysite/db/db.duckdb")
        nb_collecte = db.execute("""SELECT COUNT(*) from collecte""").fetchone() #nombre de collecte, référence utile pour pondérer et segmenter
        db.close()
        nb_collecte_info = f"""<br><div id="nb_collecte" class="alg_column_center">nombre de collectes: {nb_collecte[0]}</div><br>"""

        marketing_ui = f"""
            {nb_collecte_info}
            {mkt_1_html}
            {mkt_2_html}
            {mkt_3_html}
        """

        ui = make_response(marketing_ui) # intégration d'un cookie d'authentification temporaire suite à l'authentification en marketing
        ui.set_cookie(key = "marketing", value = mkt_cookie_value, max_age = 60, samesite = "strict", secure = True, httponly= True)

        return ui

    if login == user[0][0] and check(pwhash=user[0][1],password=password) == True and user[0][2] == 0: # accès marketing bloqué

        return """<div class="alg_row_center">refus: restriction administrateur</div"""

    elif login == user[1][0] and check(pwhash=user[1][1],password=password) == True: # administrateur

        with open("mysite/html/adm_1.html","rt") as html: # intégration des composants d'interface suite à l'authentification en administrateur
            adm_1_html = html.read()

        db = duckdb.connect("mysite/db/db.duckdb")
        switch = db.execute("""
            SELECT switch from utilisateur
            WHERE utilisateur.role == 'marketing'
        """).fetchone()

        db.close()

        if switch[0] == 1: # référence pour l'administrateur indiquant l'état actuel sur l'autorisation marketing
            acces_mkt = """<br><p id="acces_mkt" class="alg_row_center">acces marketing: autorisation</p><br>"""
        if switch[0] == 0:
            acces_mkt = """<br><p id="acces_mkt" class="alg_row_center">acces marketing: interdiction</p><br>"""

        administrateur_ui = f"""
            {acces_mkt}
            {adm_1_html}
        """

        ui = make_response(administrateur_ui) # intégration d'un cookie d'authentification temporaire suite à l'authentification en administrateur
        ui.set_cookie(key = "administrateur", value = adm_cookie_value, max_age = 60, samesite = "strict", secure = True, httponly= True)

        return ui

    else:

        return """<div class="alg_row_center">authentification invalide</div>""" # échec d'authentification
