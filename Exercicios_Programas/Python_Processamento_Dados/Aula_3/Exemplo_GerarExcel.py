'''
Instruções
Com base nas tabelas abaixos:
CREATE TABLE city (
  city_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  city VARCHAR(50) NOT NULL,
  country_id SMALLINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (city_id),
  KEY idx_fk_country_id (country_id),
  CONSTRAINT `fk_city_country` FOREIGN KEY (country_id) REFERENCES country (country_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `country`
--

CREATE TABLE country (
  country_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  country VARCHAR(50) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (country_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


Criar uma planilha em excel com os dados das cidades e qual pais ele pertence.
Gerar o arquivo em formato Json

'''

import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost', database='sakila', user='root', password='MySQL_2022')


sql_query = pd.read_sql_query('''

                               SELECT

                               *

                               FROM actor order by first_name

                               ''', conn)


df = pd.DataFrame(sql_query, columns=[
                  'actor_id', 'first_name', 'last_name', 'last_update'])

file_name = 'Exemplo Pandas SQl.xlsx'

df.to_excel(file_name)

print("ok")
