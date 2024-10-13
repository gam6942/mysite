# fonction MKT_1: Voir les depenses par categorie de vetement en fonction de la classe socio-professionnelle

import unittest
import duckdb

def mkt_1():

    # test db in memory - création

    db = duckdb.connect(":memory:")
    db.execute("""
        CREATE TABLE IF NOT EXISTS test_data (
            classe VARCHAR,
            enfant INT,
            jeune INT,
            adulte INT
        )    
    """)

    # valeurs définies car on focus le test sur la régression vs output attendu

    db.execute("""
        INSERT INTO test_data
        VALUES 
        ('ouvrier', 10000, 20000, 30000),
        ('employe', 10000, 20000, 30000),
        ('cadre', 10000, 20000, 30000),
        ('dirigeant', 10000, 20000, 30000)
    """)

    # données brutes marketing // db.sql.fetchone()

    mkt_1_ouvrier = db.execute("""
        SELECT classe,SUM(enfant),SUM(jeune),SUM(adulte) FROM test_data 
        WHERE classe == 'ouvrier'
        GROUP BY classe
    """).fetchone()

    mkt_1_employe = db.execute("""
        SELECT classe,SUM(enfant),SUM(jeune),SUM(adulte) FROM test_data 
        WHERE classe == 'employe'
        GROUP BY classe
    """).fetchone()

    mkt_1_cadre = db.execute("""
        SELECT classe,SUM(enfant),SUM(jeune),SUM(adulte) FROM test_data 
        WHERE classe == 'cadre'
        GROUP BY classe
    """).fetchone()

    mkt_1_dirigeant = db.execute("""
        SELECT classe,SUM(enfant),SUM(jeune),SUM(adulte) FROM test_data 
        WHERE classe == 'dirigeant'
        GROUP BY classe
    """).fetchone()

    # test db in memory - fermeture

    db.close()

    # préparation des éléments graphiques

    def titre(t):
        return f"""<div class="alg_row_center">{t}</div>"""
    
    def bar(color,height,value):
        return f"""<div class="bar {color}" style="height:{int(height*0.01)}px;"><p>{int(value)}€</p></div>"""
    
    def legend(l):
        return f"""<div class="legend"><p>{l}</p></div>"""
    
    # structuration des données pour output

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
    
    return mkt_1_graph

# output attendu

expected_output = f"""
<div class="alg_column_center">

<!-- Histogramme Enfant -->

    <div class="alg_row_center">Enfant</div>
    <br> 
    <div class="alg_row_bar">
        <div class="bar blue" style="height:100px;"><p>10000€</p></div>
        <div class="bar red" style="height:100px;"><p>10000€</p></div>
        <div class="bar green" style="height:100px;"><p>10000€</p></div>
        <div class="bar purple" style="height:100px;"><p>10000€</p></div>
    </div>
    <div class="alg_row_center">
        <div class="legend"><p>ouvrier</p></div>
        <div class="legend"><p>employe</p></div>
        <div class="legend"><p>cadre</p></div>
        <div class="legend"><p>dirigeant</p></div>
    </div>

<!-- Histogramme Jeune -->
    
    <div class="alg_row_center">Jeune</div>
    <br>
    <div class="alg_row_bar">
        <div class="bar blue" style="height:200px;"><p>20000€</p></div>
        <div class="bar red" style="height:200px;"><p>20000€</p></div>
        <div class="bar green" style="height:200px;"><p>20000€</p></div>
        <div class="bar purple" style="height:200px;"><p>20000€</p></div>
    </div>
    <div class="alg_row_center">
        <div class="legend"><p>ouvrier</p></div>
        <div class="legend"><p>employe</p></div>
        <div class="legend"><p>cadre</p></div>
        <div class="legend"><p>dirigeant</p></div>
    </div>

<!-- Histogramme Adulte -->
    
    <div class="alg_row_center">Adulte</div>
    <br>
    <div class="alg_row_bar">
        <div class="bar blue" style="height:300px;"><p>30000€</p></div>
        <div class="bar red" style="height:300px;"><p>30000€</p></div>
        <div class="bar green" style="height:300px;"><p>30000€</p></div>
        <div class="bar purple" style="height:300px;"><p>30000€</p></div>
    </div>
    <div class="alg_row_center">
        <div class="legend"><p>ouvrier</p></div>
        <div class="legend"><p>employe</p></div>
        <div class="legend"><p>cadre</p></div>
        <div class="legend"><p>dirigeant</p></div>
    </div>

</div>
    """

# test: structuration des données pour output == output attendu ?

class TestMKT1(unittest.TestCase):

    def test_mkt_1(self):

        self.assertMultiLineEqual(mkt_1(),expected_output)

unittest.main()





        