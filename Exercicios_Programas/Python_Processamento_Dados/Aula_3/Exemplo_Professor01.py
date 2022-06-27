import mysql.connector
from faker import Faker



class Actor:
    def __init__(self):
        self.actor_id = 0
        self.first_name = ""
        self.last_name = ""
        self.last_update = None

fake = Faker('pt_BR')
con = mysql.connector.connect(host='localhost', database='sakila', user='root', password='MySQL_2022')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()

def fecha_conexao():
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")

def incluir_actor(actor):
    url = "INSERT INTO actor (actor_id, first_name, last_name) VALUES ( " + str(actor.actor_id) + ",' " + actor.first_name + "', '" + actor.last_name + "'" + " )"
    cursor.execute(url)
    con.commit()

actor = Actor()
actor.first_name = fake.name()
actor.last_name = fake.name()
incluir_actor(actor)
fecha_conexao()