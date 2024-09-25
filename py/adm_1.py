# fonction ADM_1: Gerer l'acces aux fonctionnalites marketing

from flask import request
import duckdb


def adm_1():

    if request.get_json()["adm_1"] == "autoriser":

        db = duckdb.connect("mysite/db/db.duckdb")
        db.execute("""
            UPDATE utilisateur
            SET switch = 1
            WHERE utilisateur.role == 'marketing'
        """)
        db.commit()
        db.close()

        return "acces marketing: autorisation"

    if request.get_json()["adm_1"] == "interdire":

        db = duckdb.connect("mysite/db/db.duckdb")
        db.execute("""
            UPDATE utilisateur
            SET switch = 0
            WHERE utilisateur.role == 'marketing'
        """)
        db.commit()
        db.close()

        return "acces marketing: interdiction"
