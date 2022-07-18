-- A  partir  de  nossa  prática  restaurando  os  bancos  de  dados  de  exemplo  do  MYSQL,  vamos 
-- responder as perguntas abaixo apresentando os comandos necessários que retornem os dados 
-- solicitados.  
-- Caso você não tenha feito o restore disponibilizando os schemas está registrado em nossa aula 
-- no Microsoft Teams (será necessário assistir novamente). 
--  
-- Problema 1  Utilizando o sakila database 
--  
-- Cada uma das instruções a seguir contém erros corrija-os e execute-os no MySQL Workbench: 
-- a) SELECT category id  FROM film category; 
-- b) SELECT payment_id, rentalid, amount, payment_date  FROM amount 
-- c) SELECT * FROM address WHERE district BETWEEN ('Georgia', 'Tete', 'Gois') AND 
-- ('Georgia', 'Tete', 'Gois'); 
-- d) SELECT address_id, last_name  FROM actor WHERE first name like 'J%'; 
--   
-- Problema 2  Utilizando o sakila database 
--  
-- Construir as instruções SQL que respondam as seguintes perguntas: 
-- a) Calcule os valores das multas das locações na tabela payment considerando que todos 
-- estão atrasados e aplicando um percentual de 20% para todos pelo atraso.  
-- b) Listar as cidades que contém parte do nome com a sequência de caracteres ana. 
-- c) Listar  os  países  que  iniciam  seus  nomes  com  a  letra  R  e  que  terminam  com  a  letra  A 
-- (desconsiderar maiúsculas e minúsculas). 
-- d) Listar os nomes dos filmes que fazem alguma menção ao assunto feminismo. 
-- e) Listas as locações que foram feitas pelos clientes cadastrados entre os números 100 e 
-- 300. 
-- f) Listar os funcionários cujas senhas registradas para utilização dos sistemas são nulas. 
-- Problema 3  Utilizando o sakila database 
--  
-- Criar a cópia da tabela pagamentos e a tabela que registra a participação dos atores em filmes 
-- e popular com os dados das tabelas originais. 
-- Proceder as seguintes alterações: 
-- a) Alterar o valor dos aluguéis menores do que 1.99 para 19.99. 
-- b) Listar os valores dos aluguéis que estão entre 6.00 e 10.00. 
-- c) Listar os nomes dos filmes que contém o ator com id 36 
-- d) Substituir o ator com id 36 nos filmes em que ele atua pelo ator com id 44 
-- e)  

use sakila;

-- Problema 1  Utilizando o sakila database 
--  
-- Cada uma das instruções a seguir contém erros corrija-os e execute-os no MySQL Workbench: 
-- a) SELECT category id  FROM film category; 
SELECT category_id  FROM category;

-- b) SELECT payment_id, rentalid, amount, payment_date  FROM amount 
SELECT payment_id, rental_id, amount, payment_date  FROM payment

-- c) SELECT * FROM address WHERE district BETWEEN ('Georgia', 'Tete', 'Gois') AND 
-- ('Georgia', 'Tete', 'Gois'); 
SELECT * FROM address WHERE district in ('Georgia', 'Tete', 'Gois')

-- d) SELECT address_id, last_name  FROM actor WHERE first name like 'J%'; 
SELECT actor_id, last_name  FROM actor WHERE first_name like 'J%'; 


-- Problema 2  Utilizando o sakila database 
--  
-- Construir as instruções SQL que respondam as seguintes perguntas: 
-- a) Calcule os valores das multas das locações na tabela payment considerando que todos 
-- estão atrasados e aplicando um percentual de 20% para todos pelo atraso.  
select payment_id,customer_id,rental_id, amount*0.20 as multa from payment

-- b) Listar as cidades que contém parte do nome com a sequência de caracteres ana. 
select * from city where city like '%ana%'

-- c) Listar  os  países  que  iniciam  seus  nomes  com  a  letra  R  e  que  terminam  com  a  letra  A 
-- (desconsiderar maiúsculas e minúsculas). 
select * from country where UPPER(country) like UPPER('R%A')

-- d) Listar os nomes dos filmes que fazem alguma menção ao assunto feminismo. 
select title, description from film where UPPER(description) like UPPER ('% feminis%')

-- e) Listas as locações que foram feitas pelos clientes cadastrados entre os números 100 e 
-- 300. 
select * from rental where customer_id between 100 and 300

-- f) Listar os funcionários cujas senhas registradas para utilização dos sistemas são nulas. 
-- Problema 3  Utilizando o sakila database 
select * from staff where password is null


