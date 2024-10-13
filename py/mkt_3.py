# fonction MKT_3: Exporter un nombre de collectes des depenses pour chaque categorie de vetement

from flask import send_file, request
import duckdb
from io import BytesIO

def mkt_3():

    mkt_3 = int(request.get_json()["mkt_3"])

    db = duckdb.connect("mysite/db/db.duckdb")

    df_collecte = db.execute("""
        SELECT * from collecte
    """).fetch_df().head(mkt_3)

    db.close()

    in_memory_data = BytesIO()

    df_collecte.to_csv(in_memory_data,index=None)

    in_memory_data.seek(0)

    return send_file(path_or_file=in_memory_data,download_name="collecte.csv",mimetype="text/csv",as_attachment=True)

