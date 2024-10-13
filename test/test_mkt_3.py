# fonction MKT_3: Exporter un nombre de collectes des depenses pour chaque categorie de vetement

import unittest
import duckdb
from io import StringIO

def mkt_3(value_check):

    # requête POST json

    json_request = {"mkt_3":value_check}

    # request.get_json()
    
    mkt_3 = int(json_request["mkt_3"])

    # test db in memory - création
    
    db = duckdb.connect(":memory:")
    db.execute("""
        CREATE TABLE IF NOT EXISTS test_data (
            id INT,
            enfant INT,
            jeune INT,
            adulte INT
        )
    """)

    db.execute("""
        INSERT INTO test_data
        VALUES
        (1,10,20,30),
        (2,0,0,30),
        (3,10,0,50),
        (4,0,0,70),
        (5,50,20,0)
    """)

    # données brutes marketing // db.sql.fetch_df().head()

    df_collecte = db.execute("""
        SELECT * FROM test_data
    """).fetch_df().head(mkt_3)

    # test db in memory - fermeture

    db.close()

    # structuration des données pour output

    in_memory_str = StringIO()

    df_collecte.to_csv(in_memory_str, index=None)

    csv_data = in_memory_str.getvalue()

    in_memory_str.close()

    # on ignore l'objet réponse sendfile() en renvoyant directement un output de type string afin de maintenir le test unitaire isolé 

    return csv_data

# output attendu pour une requête POST == {"mkt_3":1} soit 1 ligne

csv_1 = 'id,enfant,jeune,adulte\r\n1,10,20,30\r\n'

# output attendu pour une requête POST == {"mkt_3":2} soit 2 lignes

csv_2 = 'id,enfant,jeune,adulte\r\n1,10,20,30\r\n2,0,0,30\r\n'

# output attendu pour une requête POST == {"mkt_3":3} soit 3 lignes

csv_3 = 'id,enfant,jeune,adulte\r\n1,10,20,30\r\n2,0,0,30\r\n3,10,0,50\r\n'

# test: structuration des données pour output == output attendu ?

class TestMKT3(unittest.TestCase):
    
    def test_mkt_3(self):

        self.assertMultiLineEqual(mkt_3(1),csv_1)
        self.assertMultiLineEqual(mkt_3(2),csv_2)
        self.assertMultiLineEqual(mkt_3(3),csv_3)

unittest.main()