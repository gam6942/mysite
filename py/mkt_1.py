# fonction MKT_1: Voir les depenses par categorie de vetement en fonction de la classe socio-professionnelle

import duckdb

def mkt_1():

    db = duckdb.connect("mysite/db/db.duckdb")

    mkt_1_ouvrier = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'ouvrier'
        GROUP BY classe
    """).fetchall()

    mkt_1_employe = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'employe'
        GROUP BY classe
    """).fetchall()

    mkt_1_cadre = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'cadre'
        GROUP BY classe
    """).fetchall()

    mkt_1_dirigeant = db.execute("""
        SELECT classe,SUM(montant_enfant),SUM(montant_jeune),SUM(montant_adulte) from client
        LEFT JOIN collecte ON client.id_collecte = collecte.collecte_id
        WHERE client.classe == 'dirigeant'
        GROUP BY classe
    """).fetchall()

    # 3 histogrammes sur mesure en reponse au besoin MKT_1

    mkt_1_graph = f"""
        <div class="alg_column_center">

            <div class="alg_row_center">Enfant</div>
            <br>
            <div class="alg_row_bar">
                <div class="bar blue" style="height:{int(mkt_1_ouvrier[0][1])*0.01}px;"><p>{int(mkt_1_ouvrier[0][1])}€</p></div>
                <div class="bar red" style="height:{int(mkt_1_employe[0][1])*0.01}px;"><p>{int(mkt_1_employe[0][1])}€</p></div>
                <div class="bar green" style="height:{int(mkt_1_cadre[0][1])*0.01}px;"><p>{int(mkt_1_cadre[0][1])}€</p></div>
                <div class="bar purple" style="height:{int(mkt_1_dirigeant[0][1])*0.01}px;"><p>{int(mkt_1_dirigeant[0][1])}€</p></div>
            </div>
            <div class="alg_row_center">
                <div class="legend"><p>ouvrier</p></div>
                <div class="legend"><p>employe</p></div>
                <div class="legend"><p>cadre</p></div>
                <div class="legend"><p>dirigeant</p></div>
            </div>

            <div class="alg_row_center">Jeune</div>
            <br>
            <div class="alg_row_bar">
                <div class="bar blue" style="height:{int(mkt_1_ouvrier[0][2])*0.01}px;"><p>{int(mkt_1_ouvrier[0][2])}€</p></div>
                <div class="bar red" style="height:{int(mkt_1_employe[0][2])*0.01}px;"><p>{int(mkt_1_employe[0][2])}€</p></div>
                <div class="bar green" style="height:{int(mkt_1_cadre[0][2])*0.01}px;"><p>{int(mkt_1_cadre[0][2])}€</p></div>
                <div class="bar purple" style="height:{int(mkt_1_dirigeant[0][2])*0.01}px;"><p>{int(mkt_1_dirigeant[0][2])}€</p></div>
            </div>
            <div class="alg_row_center">
                <div class="legend"><p>ouvrier</p></div>
                <div class="legend"><p>employe</p></div>
                <div class="legend"><p>cadre</p></div>
                <div class="legend"><p>dirigeant</p></div>
            </div>

            <div class="alg_row_center">Adulte</div>
            <br>
            <div class="alg_row_bar">
                <div class="bar blue" style="height:{int(mkt_1_ouvrier[0][3])*0.01}px;"><p>{int(mkt_1_ouvrier[0][3])}€</p></div>
                <div class="bar red" style="height:{int(mkt_1_employe[0][3])*0.01}px;"><p>{int(mkt_1_employe[0][3])}€</p></div>
                <div class="bar green" style="height:{int(mkt_1_cadre[0][3])*0.01}px;"><p>{int(mkt_1_cadre[0][3])}€</p></div>
                <div class="bar purple" style="height:{int(mkt_1_dirigeant[0][3])*0.01}px;"><p>{int(mkt_1_dirigeant[0][3])}€</p></div>
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

    return mkt_1_graph