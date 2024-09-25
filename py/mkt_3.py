# fonction MKT_3: Exporter un nombre de collectes des depenses pour chaque categorie de vetement

from flask import send_file, request
import duckdb

def mkt_3():

    mkt_3 = int(request.get_json()["mkt_3"])

    db = duckdb.connect("mysite/db/db.duckdb")

    df_collecte = db.execute("""
        SELECT * from collecte
    """).fetch_df().head(mkt_3)

    db.close()

    df_collecte.to_csv("mysite/db/collecte.csv",index=None)

    return send_file("db/collecte.csv",mimetype="text/csv",as_attachment=True)

