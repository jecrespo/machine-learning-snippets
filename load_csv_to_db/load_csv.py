import pandas as pd
import sqlalchemy
import secrets_example

df = pd.read_csv ('dataset.csv',sep=',')
#print(df)
#print(df.pu_id)

#import con alchemy
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                 format(secrets_example.database_username, secrets_example.database_password, 
                                                 secrets_example.database_ip, secrets_example.database_name))
df.to_sql(con=database_connection, name=secrets_example.table_name, if_exists='replace',chunksize=1000)