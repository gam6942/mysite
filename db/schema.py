# script schema pour la bdd

import duckdb

db = duckdb.connect("db/db.duckdb")

db.execute("""DROP TABLE client""")
db.execute("""DROP TABLE collecte""")
db.commit()

db.execute("""
    CREATE TABLE IF NOT EXISTS utilisateur (
        role VARCHAR NOT NULL UNIQUE,
        password VARCHAR NOT NULL,
        switch INT NOT NULL
    )
""")
db.execute("""
    CREATE TABLE IF NOT EXISTS collecte (
        collecte_id INT NOT NULL PRIMARY KEY,
        montant_enfant INT,
        montant_jeune INT,
        montant_adulte INT
    )
""")
db.execute("""
    CREATE TABLE IF NOT EXISTS client (
        client_id VARCHAR NOT NULL PRIMARY KEY,
        nb_enfant INT NOT NULL,
        classe VARCHAR NOT NULL,
        montant_total INT NOT NULL,
        id_collecte INT NOT NULL UNIQUE,
        FOREIGN KEY (id_collecte) REFERENCES collecte(collecte_id)
    )
""")

utilisateur = db.execute("""SELECT * FROM utilisateur""").fetch_df()
collecte = db.execute("""SELECT * FROM collecte""").fetch_df()
client = db.execute("""SELECT * FROM client""").fetch_df()
print(utilisateur,collecte,client)
db.close()