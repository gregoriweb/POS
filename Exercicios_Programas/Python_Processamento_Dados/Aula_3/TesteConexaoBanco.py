import mysql.connector

con = mysql.connector.connect(host='localhost', database='puc', user='root', password='MySQL_2022')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()