# fonction MKT_2: Voir le panier moyen des depenses en fonction de la classe socio-professionnelle

import duckdb

def mkt_2():

    db = duckdb.connect("mysite/db/db.duckdb")

    mkt_2_ouvrier = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'ouvrier'
        GROUP BY classe
    """).fetchall()

    mkt_2_employe = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'employe'
        GROUP BY classe
    """).fetchall()

    mkt_2_cadre = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'cadre'
        GROUP BY classe
    """).fetchall()

    mkt_2_dirigeant = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'dirigeant'
        GROUP BY classe
    """).fetchall()

    # 1 histogramme sur mesure en reponse au besoin MKT_2

    mkt_2_graph = f"""
        <div class="alg_column_center">

            <div class="alg_row_center">Panier moyen</div>
            <br>
            <div class="alg_row_bar">
                <div class="bar blue" style="height:{int(mkt_2_ouvrier[0][1])}px;"><p>{int(mkt_2_ouvrier[0][1])}€</p></div>
                <div class="bar red" style="height:{int(mkt_2_employe[0][1])}px;"><p>{int(mkt_2_employe[0][1])}€</p></div>
                <div class="bar green" style="height:{int(mkt_2_cadre[0][1])}px;"><p>{int(mkt_2_cadre[0][1])}€</p></div>
                <div class="bar purple" style="height:{int(mkt_2_dirigeant[0][1])}px;"><p>{int(mkt_2_dirigeant[0][1])}€</p></div>
            </div>
            <div class="alg_row_center">
                <div class="legend"><p>ouvrier</p></div>
                <div class="legend"><p>employe</p></div>
                <div class="legend"><p>cadre</p></div>
                <div class="legend"><p>dirigeant</p></div>
            </div>

        </div>
    """

    db.close()

    return mkt_2_graph
