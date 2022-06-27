'''

'''
import pandas as pd
import mysql.connector



def converte_df_csv(df, nomeArquivo):
    df.to_csv(r'ArquivoCSVPaises.csv', sep=";")

def converte_df_json(df, nomeArquivo):
    df.to_json(r'ArquivoJSONPaises.json', orient='records')



def mysql_connection (host='localhost', database='sakila', user='root', password='MySQL_2022'):
    conn = mysql.connector.connect(
        host=host, database=database, user=user, password=password)
    return conn

def get_dataframe (query="", connection=mysql_connection(), columns=['country', 'city']):
    df = pd.DataFrame(pd.read_sql_query(query, connection), columns=columns)
    return df

query =  r'''SELECT CO.country_id, country, city_id, city FROM sakila.country CO 
                left join sakila.city CI on CO.country_id = CI.country_id
            '''

df = get_dataframe(query)

converte_df_csv(df,nomeArquivo="")
converte_df_json(df,nomeArquivo="")