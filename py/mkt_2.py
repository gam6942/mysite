# fonction MKT_2: Voir le panier moyen des depenses en fonction de la classe socio-professionnelle

import duckdb

def mkt_2():

    db = duckdb.connect("mysite/db/db.duckdb")

    mkt_2_ouvrier = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'ouvrier'
        GROUP BY classe
    """).fetchone()

    mkt_2_employe = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'employe'
        GROUP BY classe
    """).fetchone()

    mkt_2_cadre = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'cadre'
        GROUP BY classe
    """).fetchone()

    mkt_2_dirigeant = db.execute("""
        SELECT classe,AVG(montant_total) FROM client
        WHERE client.classe == 'dirigeant'
        GROUP BY classe
    """).fetchone()

    # préparation des éléments graphiques

    def titre(t):
        return f"""<div class="alg_row_center">{t}</div>"""

    def bar(color,height,value):
        return f"""<div class="bar {color}" style="height:{int(height)}px;"><p>{int(value)}€</p></div>"""

    def legend(l):
        return f"""<div class="legend"><p>{l}</p></div>"""

    # 1 histogramme sur mesure en reponse au besoin MKT_2

    mkt_2_graph = f"""
<div class="alg_column_center">

    {titre(t="Panier moyen")}
    <br>
    <div class="alg_row_bar">
        {bar(color="blue",height=mkt_2_ouvrier[1],value=mkt_2_ouvrier[1])}
        {bar(color="red",height=mkt_2_employe[1],value=mkt_2_employe[1])}
        {bar(color="green",height=mkt_2_cadre[1],value=mkt_2_cadre[1])}
        {bar(color="purple",height=mkt_2_dirigeant[1],value=mkt_2_dirigeant[1])}
    </div>
    <div class="alg_row_center">
        {legend(l=mkt_2_ouvrier[0])}
        {legend(l=mkt_2_employe[0])}
        {legend(l=mkt_2_cadre[0])}
        {legend(l=mkt_2_dirigeant[0])}
    </div>

</div>
    """

    return mkt_2_graph
