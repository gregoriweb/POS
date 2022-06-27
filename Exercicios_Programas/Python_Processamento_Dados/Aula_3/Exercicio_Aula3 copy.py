'''

'''

import pandas as pd
import mysql.connector


def converte_csv_json(nomeArquivo):
    df = pd.read_csv(r'ArquivoCSV.csv')
    df.to_json(r'ArquivoJson.json')


def converte_json_csv(nomeArquivo):
    df = pd.read_json(r'ArquivoJson.json')
    df.to_csv(r'ArquivoCSVConvertido.csv', orient='table')

def converte_df_csv(df, nomeArquivo):
    df.to_csv(r'ArquivoCSVPaises.csv')

def converte_df_json(df, nomeArquivo):
    df.to_json(r'ArquivoJSONPaises.json', orient='table')

###-------------------------------------------------------------------

def le_arquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    tamanho = arquivo.readlines()
    cont = 0
    dados = []

    while(len(tamanho) > cont):
        linha = tamanho[cont]
        print(linha)
        dados.append(linha)
        cont += 1

    arquivo.close()
    return linha


def grava_arquivo(nomeArquivo, dados):
    arquivo = open(nomeArquivo + ".txt", "w+")
    for dado in dados:
        arquivo.write(dado)
        print(dado)
    arquivo.close()

def mysql_connection (host='localhost', database='sakila', user='root', password='MySQL_2022'):
    conn = mysql.connector.connect(
        host=host, database=database, user=user, password=password)
    return conn

def get_dataframe (query="", connection=mysql_connection()):
    df = pd.DataFrame(pd.read_sql_query(query, connection))
    return df

# get_dataframe("SELECT * FROM sakila.country")

query =  r'''SELECT * FROM sakila.country CO 
            left join sakila.city CI on CO.country_id = CI.country_id'''

df = get_dataframe(query)

converte_df_csv(df,nomeArquivo="")
converte_df_json(df,nomeArquivo="")

#def get_dataframe (query="SELECT * FROM sakila.country CO left join sakila.city CI on CO.country_id = CI.country_id"):
#    conn = mysql.connector.connect(
#        host='localhost', database='sakila', user='root', password='MySQL_2022')
#    df = pd.DataFrame(pd.read_sql_query(query, conn), columns=['actor_id', 'first_name', 'last_name', 'last_update'])
#    return df




## nomeArquivo = "ArquivoCSV.csv"
## ##dados = le_arquivo(nomeArquivo)
## converte_csv_json("")
## converte_json_csv("")
## 
## file_name = 'Exemplo Pandas SQl.xlsx'
## df.to_excel(file_name)
## print("ok")
## 