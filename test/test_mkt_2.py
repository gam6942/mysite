# fonction MKT_2: Voir le panier moyen des depenses en fonction de la classe socio-professionnelle

import unittest
import duckdb

def mkt_2():

    # test db in memory - création

    db = duckdb.connect(":memory:")
    db.execute("""
        CREATE TABLE IF NOT EXISTS test_data (
            classe VARCHAR,
            panier FLOAT
        )
    """)

    # valeurs définies car on focus le test sur la régression vs output attendu

    db.execute("""
        INSERT INTO test_data
        VALUES
        ('ouvrier', 50.5),
        ('employe', 60.5),
        ('cadre', 70.5),
        ('dirigeant', 80.5)               
    """)

    # données brutes marketing // db.sql.fetchone()

    mkt_2_ouvrier = db.execute("""
        SELECT classe,AVG(panier) FROM test_data 
        WHERE classe == 'ouvrier' 
        GROUP BY classe
    """).fetchone()

    mkt_2_employe = db.execute("""
        SELECT classe,AVG(panier) FROM test_data 
        WHERE classe == 'employe'
        GROUP BY classe
    """).fetchone()

    mkt_2_cadre = db.execute("""
        SELECT classe,AVG(panier) FROM test_data 
        WHERE classe == 'cadre'
        GROUP BY classe
    """).fetchone()

    mkt_2_dirigeant = db.execute("""
        SELECT classe,AVG(panier) FROM test_data 
        WHERE classe == 'dirigeant'
        GROUP BY classe
    """).fetchone()

    # test db in memory - fermeture

    db.close()

    # préparation des éléments graphiques

    def titre(t):
        return f"""<div class="alg_row_center">{t}</div>"""
    
    def bar(color,height,value):
        return f"""<div class="bar {color}" style="height:{int(height)}px;"><p>{int(value)}€</p></div>"""
    
    def legend(l):
        return f"""<div class="legend"><p>{l}</p></div>"""

    # structuration des données pour output

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

# output attendu

def output():

    expected_output = f"""
<div class="alg_column_center">

    <div class="alg_row_center">Panier moyen</div>
    <br> 
    <div class="alg_row_bar">
        <div class="bar blue" style="height:50px;"><p>50€</p></div>
        <div class="bar red" style="height:60px;"><p>60€</p></div>
        <div class="bar green" style="height:70px;"><p>70€</p></div>
        <div class="bar purple" style="height:80px;"><p>80€</p></div>
    </div>
    <div class="alg_row_center">
        <div class="legend"><p>ouvrier</p></div>
        <div class="legend"><p>employe</p></div>
        <div class="legend"><p>cadre</p></div>
        <div class="legend"><p>dirigeant</p></div>
    </div>

</div>
    """

    return expected_output

# test: structuration des données pour output == output attendu ?

class TestMKT2(unittest.TestCase):

    def test_mkt_2(self):

        self.assertMultiLineEqual(mkt_2(),output())

unittest.main()