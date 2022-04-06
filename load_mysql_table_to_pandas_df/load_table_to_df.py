#Copiar a un df de pandas desde una tabla MYSQL con los nombres de campos igual que las tabla

import mysql.connector as my_dbapi
import pandas as pd
import secrets_example

cnx_my = my_dbapi.connect(user=secrets_example.database_username, password=secrets_example.database_password, host=secrets_example.database_ip, database=secrets_example.database_name)
cursor_my = cnx_my.cursor()
query = "SELECT * FROM {tabla}".format(tabla = secrets_example.table_name)

cursor_my.execute(query)
df = pd.DataFrame(cursor_my.fetchall())
df.columns = [item[0] for item in cursor_my.description] #nombres de las columnas
print(df)

cursor_my.close()
cnx_my.close()