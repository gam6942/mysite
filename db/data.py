# script dataset pour la bdd

import duckdb
import pandas as pd
from os import urandom as r_byte
from random import randint as r_int
from random import choice as r_str
from werkzeug.security import generate_password_hash as hash

db = duckdb.connect("db/db.duckdb")

try: # données utilisateur

    db.execute(f"""
        INSERT INTO utilisateur (role,password,switch)
        VALUES ('marketing','{hash(password="market")}',1)
    """)
    db.execute(f"""
        INSERT INTO utilisateur (role,password,switch)
        VALUES ('administrateur','{hash(password="admin")}',1)
    """)

    db.commit()

except:
    pass

table = db.execute("""
    SELECT * FROM utilisateur
""").fetch_df()

print(table)

# données client

client_id = []
nb_enfant = []
classe = []
for i in range(1000):
    client_id.append(r_byte(10).hex())
    nb_enfant.append(r_int(a=0,b=3))
    classe.append(r_str(["ouvrier","ouvrier","employe","employe","employe","employe","employe","cadre","cadre","cadre","dirigeant"]))

montant_total = []
for i in classe:
    if i == "ouvrier":
        montant_total.append(r_int(a=10,b=100))
    if i == "employe":
        montant_total.append(r_int(a=10,b=150))
    if i == "cadre":
        montant_total.append(r_int(a=10,b=200))
    if i == "dirigeant":
        montant_total.append(r_int(a=10,b=250))

id_collecte = []
for i in range(1000):
    i+=1
    id_collecte.append(i)

df_client_id = pd.DataFrame(client_id)
df_client_id.columns = ["client_id"]

df_nb_enfant = pd.DataFrame(nb_enfant)
df_nb_enfant.columns = ["nb_enfant"]

df_classe = pd.DataFrame(classe)
df_classe.columns = ["classe"]

df_montant_total = pd.DataFrame(montant_total)
df_montant_total.columns = ["montant_total"]

df_id_collecte = pd.DataFrame(id_collecte)
df_id_collecte.columns = ["id_collecte"]

df_client = pd.concat([df_client_id, df_nb_enfant, df_classe, df_montant_total, df_id_collecte], axis=1)

# données collecte

collecte_id = []
for i in range(1000):
    i+=1
    collecte_id.append(i)

df_collecte_id = pd.DataFrame(collecte_id)
df_collecte_id.columns = ["collecte_id"]

montant_enfant = []
montant_jeune = []
montant_adulte = []

trick = duckdb.sql("SELECT nb_enfant,montant_total FROM df_client").fetchall()
print(trick)

for i in trick:
    if i[0] == 0:
        montant_enfant.append(0)
        montant_jeune.append(0)
        montant_adulte.append(i[1])
    else:
        r_montant_1 = r_int(a=0,b=i[1])
        r_montant_2 = r_int(a=0,b=i[1])
        r_montant_3 = r_int(a=0,b=i[1])
        while r_montant_1+r_montant_2+r_montant_3 != i[1]:
            r_montant_1 = r_int(a=0,b=i[1])
            r_montant_2 = r_int(a=0,b=i[1])
            r_montant_3 = r_int(a=0,b=i[1])
        montant_enfant.append(r_montant_1)
        montant_jeune.append(r_montant_2)
        montant_adulte.append(r_montant_3)


df_montant_enfant = pd.DataFrame(montant_enfant)
df_montant_enfant.columns = ["montant_enfant"]
df_montant_jeune = pd.DataFrame(montant_jeune)
df_montant_jeune.columns = ["montant_jeune"]
df_montant_adulte = pd.DataFrame(montant_adulte)
df_montant_adulte.columns = ["montant_adulte"]

df_collecte = pd.concat([df_collecte_id,df_montant_enfant,df_montant_jeune,df_montant_adulte], axis=1)

#integration bdd

db.append(table_name="collecte",df=df_collecte)
db.append(table_name="client",df=df_client)
db.close()