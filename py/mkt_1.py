# fonction MKT_1: Voir les depenses par categorie de vetement en fonction de la classe socio-professionnelle

import duckdb
from textwrap import dedent

def mkt_1():

    db = duckdb.connect("mysite/db/db.duckdb")

    mkt_1_ouvrier = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'ouvrier'
        GROUP BY classe
    """).fetchone()

    mkt_1_employe = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'employe'
        GROUP BY classe
    """).fetchone()

    mkt_1_cadre = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'cadre'
        GROUP BY classe
    """).fetchone()

    mkt_1_dirigeant = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'dirigeant'
        GROUP BY classe
    """).fetchone()

    # préparation des éléments graphiques

    def titre(t):
        return f"""<div class="alg_row_center">{t}</div>"""

    def bar(color,height,value):
        return f"""<div class="bar {color}" style="height:{int(height*0.01)}px;"><p>{int(value)}€</p></div>"""

    def legend(l):
        return f"""<div class="legend"><p>{l}</p></div>"""

    # 3 histogrammes sur mesure en reponse au besoin MKT_1

    mkt_1_graph = f"""
        <div class="alg_column_center">

            <!-- Histogramme Enfant -->

            {titre(t="Enfant")}
            <br>
            <div class="alg_row_bar">
                {bar(color="blue",height=mkt_1_ouvrier[1],value=mkt_1_ouvrier[1])}
                {bar(color="red",height=mkt_1_employe[1],value=mkt_1_employe[1])}
                {bar(color="green",height=mkt_1_cadre[1],value=mkt_1_cadre[1])}
                {bar(color="purple",height=mkt_1_dirigeant[1],value=mkt_1_dirigeant[1])}
            </div>
            <div class="alg_row_center">
                {legend(l=mkt_1_ouvrier[0])}
                {legend(l=mkt_1_employe[0])}
                {legend(l=mkt_1_cadre[0])}
                {legend(l=mkt_1_dirigeant[0])}
            </div>

            <!-- Histogramme Jeune -->

            {titre(t="Jeune")}
            <br>
            <div class="alg_row_bar">
                {bar(color="blue",height=mkt_1_ouvrier[2],value=mkt_1_ouvrier[2])}
                {bar(color="red",height=mkt_1_employe[2],value=mkt_1_employe[2])}
                {bar(color="green",height=mkt_1_cadre[2],value=mkt_1_cadre[2])}
                {bar(color="purple",height=mkt_1_dirigeant[2],value=mkt_1_dirigeant[2])}
            </div>
            <div class="alg_row_center">
                {legend(l=mkt_1_ouvrier[0])}
                {legend(l=mkt_1_employe[0])}
                {legend(l=mkt_1_cadre[0])}
                {legend(l=mkt_1_dirigeant[0])}
            </div>

            <!-- Histogramme Adulte -->

            {titre(t="Adulte")}
            <br>
            <div class="alg_row_bar">
                {bar(color="blue",height=mkt_1_ouvrier[3],value=mkt_1_ouvrier[3])}
                {bar(color="red",height=mkt_1_employe[3],value=mkt_1_employe[3])}
                {bar(color="green",height=mkt_1_cadre[3],value=mkt_1_cadre[3])}
                {bar(color="purple",height=mkt_1_dirigeant[3],value=mkt_1_dirigeant[3])}
            </div>
            <div class="alg_row_center">
                {legend(l=mkt_1_ouvrier[0])}
                {legend(l=mkt_1_employe[0])}
                {legend(l=mkt_1_cadre[0])}
                {legend(l=mkt_1_dirigeant[0])}
            </div>

        </div>
    """

    return dedent(mkt_1_graph)