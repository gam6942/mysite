# fonction d'authentification

from werkzeug.security import generate_password_hash as hash
from werkzeug.security import check_password_hash as check
import duckdb
import unittest

def login(login_data,password_data,switch):

    # requête POST en json

    json_request = {"login":login_data,"password":password_data}

    # request.get_json()

    login = json_request["login"]
    password = json_request["password"]

    # test db in memory - ouverture

    db = duckdb.connect(":memory:")
    db.execute("""
        CREATE TABLE IF NOT EXISTS utilisateur (
            role VARCHAR,
            password VARCHAR,
            switch INT
        )
    """)
    db.execute(f"""
        INSERT INTO utilisateur
        VALUES
        ('marketing','{hash("marketing")}',{switch}),
        ('administrateur','{hash("administrateur")}',1)
    """)


    db.execute("""
        CREATE TABLE IF NOT EXISTS collecte (
            id INT
        )
    """)
    db.execute("""
        INSERT INTO collecte
        VALUES
        (1),(2),(3),(4),(5)
    """)

    user = db.execute("""
        SELECT * from utilisateur  
    """).fetchall()

    # case 1

    if login == user[0][0] and check(pwhash=user[0][1],password=password) == True and user[0][2] == 1: # marketing

        # intégration des composants d'interface suite à l'authentification en marketing
        
        # on intègre des strings explicites plutot que de open.read() les modules.html pour maintenir l'isolation du test unitaire

        mkt_1_html = "composant html mkt_1"
        mkt_2_html = "composant html mkt_2"
        mkt_3_html = "composant html mkt_3"
        
        nb_collecte = db.execute("""SELECT COUNT(*) from collecte""").fetchone() #nombre de collecte, référence utile pour pondérer et segmenter
        nb_collecte_info = f"""<br><div id="nb_collecte" class="alg_column_center">nombre de collectes: {nb_collecte[0]}</div><br>"""

        marketing_ui = f"""
{nb_collecte_info}
{mkt_1_html}
{mkt_2_html}
{mkt_3_html}
        """

        db.close()

        # on ignore l'objet réponse intégrant un cookie en testant directement l'output pour maintenir l'isolation du test unitaire

        return marketing_ui
    
    # case 2
    
    if login == user[0][0] and check(pwhash=user[0][1],password=password) == True and user[0][2] == 0: # accès marketing bloqué

        return """<div class="alg_row_center">refus: restriction administrateur</div"""
    
    # case 3 & 4
    
    if login == user[1][0] and check(pwhash=user[1][1],password=password) == True: # administrateur

        # intégration des composants d'interface suite à l'authentification en administrateur
        
        # on intègre des strings explicites plutot que de open.read() les modules.html pour maintenir le test unitaire isolé
        
        adm_1_html = "composant html adm_1"

        switch = db.execute("""
            SELECT switch from utilisateur
            WHERE utilisateur.role == 'marketing'
        """).fetchone()

        # case 3
        if switch[0] == 1: # référence pour l'administrateur indiquant l'état actuel sur l'autorisation marketing
            acces_mkt = """<br><p id="acces_mkt" class="alg_row_center">acces marketing: autorisation</p><br>"""

        # case 4
        if switch[0] == 0:
            acces_mkt = """<br><p id="acces_mkt" class="alg_row_center">acces marketing: interdiction</p><br>""" 

        administrateur_ui = f"""
{acces_mkt}
{adm_1_html}
        """

        db.close()

        # on ignore l'objet réponse intégrant un cookie en testant directement l'output pour maintenir le test unitaire isolé

        return administrateur_ui
    
    else:

        db.close()

        # case 5 & 6
        # à partir du moment où les credentials ne matchent pas la base, on ignore le switch en renvoyant la même réponse d'échec

        return """<div class="alg_row_center">authentification invalide</div>""" # échec d'authentification
    
# output attendu par case

case_1 = """
<br><div id="nb_collecte" class="alg_column_center">nombre de collectes: 5</div><br>
composant html mkt_1
composant html mkt_2
composant html mkt_3
        """

case_2 = """<div class="alg_row_center">refus: restriction administrateur</div"""

case_3 = """
<br><p id="acces_mkt" class="alg_row_center">acces marketing: autorisation</p><br>
composant html adm_1
        """

case_4 = """
<br><p id="acces_mkt" class="alg_row_center">acces marketing: interdiction</p><br>
composant html adm_1
        """

case_5 = """<div class="alg_row_center">authentification invalide</div>"""

case_6 = """<div class="alg_row_center">authentification invalide</div>"""

# test: login case output == output attendu ?

class TestLogin(unittest.TestCase):

    def test_login(self):

        self.assertMultiLineEqual(login('marketing','marketing',1),case_1)
        self.assertMultiLineEqual(login('marketing','marketing',0),case_2)
        self.assertMultiLineEqual(login('administrateur','administrateur',1),case_3)
        self.assertMultiLineEqual(login('administrateur','administrateur',0),case_4)
        self.assertMultiLineEqual(login('any','any',1),case_5)
        self.assertMultiLineEqual(login('any','any',0),case_6)


unittest.main()
