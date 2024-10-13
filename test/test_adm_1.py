# fonction ADM_1: Gerer l'acces aux fonctionnalites marketing

import duckdb
import unittest
from werkzeug.security import generate_password_hash as hash

def adm_1(value_check):

    # test db in memory - création

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
        ('marketing','{hash("marketing")}',1),
        ('administrateur','{hash("administrateur")}',1)
    """)

    # request.get_json()

    json_request = {"adm_1":value_check}

    # case 1

    if json_request["adm_1"] == "autoriser":

        db.execute("""
            UPDATE utilisateur
            SET switch = 1
            WHERE utilisateur.role == 'marketing'       
        """)
        db.commit()

        # on récupère la valeur du switch dans l'intêret du test unitaire

        switch_check = db.execute("""
            SELECT switch FROM utilisateur 
            WHERE utilisateur.role == 'marketing'
        """).fetchone()

        db.close()

        # on retourne également la valeur du switch toujours dans l'intêret du test unitaire

        return f"acces marketing: autorisation {switch_check[0]}"
    
    # case 2
    
    if json_request["adm_1"] == "interdire":

        db.execute("""
            UPDATE utilisateur
            SET switch = 0
            WHERE utilisateur.role == 'marketing'            
        """)
        db.commit()

        # on récupère la valeur du switch dans l'intêret du test unitaire

        switch_check = db.execute("""
            SELECT switch FROM utilisateur 
            WHERE utilisateur.role == 'marketing'
        """).fetchone()

        db.close()

        # on retourne également la valeur du switch toujours dans l'intêret du test unitaire

        return f"acces marketing: interdiction {switch_check[0]}"
    
# test: case 1,case 2: output + switch == output attendu?
    
class TestADM1(unittest.TestCase):

    def test_adm_1(self):

        self.assertMultiLineEqual(adm_1("autoriser"),"acces marketing: autorisation 1")
        self.assertMultiLineEqual(adm_1("interdire"),"acces marketing: interdiction 0")

unittest.main()
