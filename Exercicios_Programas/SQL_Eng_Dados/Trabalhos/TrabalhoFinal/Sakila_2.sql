-- 
-- Para o schema sakila, responda as seguintes perguntas construindo os comandos SQL 
--  
-- 1  –  Quantidade de filmes  locados  por  categoria  em  cada  um  dos  anos, separando em  dois 
-- comandos  diferentes, que podem ser  views, a  lista  de  filmes  e  a  lista  de  filmes  com  seus 
-- respectivos atores.  

-- 2  – Quantidade de filmes por categoria e os valores totais de locação de cada filme, separando 
-- em dois comandos diferentes, que podem ser views, valores por filme e valores por categoria. 


-- 3  –  Média de  atuação  de cada  ator  em  filmes  geral  do  inventário de  filmes, em  comandos 
-- separados, que podem ser views, quais deles ficaram abaixo da média geral de atuações e quais 
-- ficaram acima da média geral de atuações.  

-- 4 – Qual o valor médio de locações de cada categoria e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views,  quais filmes ficaram acima e abaixo da média 
-- da categoria por ano. 

use sakila;

-- 1  –  Quantidade de filmes  locados  por  categoria  em  cada  um  dos  anos, separando em  dois 
-- comandos  diferentes, que podem ser  views, a  lista  de  filmes  e  a  lista  de  filmes  com  seus 
-- respectivos atores.  

 -- Qunatidade de Filmes locados por categoria
select `c`.`name` AS `category`,
year(r.rental_date) ano,
count(*) n_locacoes
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by `c`.`name` , year(r.rental_date) order by `n_locacoes` desc;

-- Lista de filmes 
SELECT title as 'Titulo Filme' FROM sakila.film_list;


-- Lista de filmes com Atores 0.031 sec / 0.000 sec
SELECT title, actors FROM sakila.film_list;


-- 2  – Quantidade de filmes por categoria e os valores totais de locação de cada filme, separando 
-- em dois comandos diferentes, que podem ser views, valores por filme e valores por categoria. 


-- Qtd Filmes Categoria
select c.category_id, c.name,
count(*) qtd_filmes_categoria
from `sakila`.`film` `f` 
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id` 
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id` 
group by c.category_id

-- Qtd e Valor de Locacao de cada filme
select 
-- *
`f`.`film_id` , `f`.`title` AS `title`, c.category_id, c.name as category,
count(*) n_locacoes,
sum(`p`.`amount`) AS `valor_locado_filme` 
from `sakila`.`payment` `p` 
join `sakila`.`rental` `r` on `p`.`rental_id` = `r`.`rental_id` 
join `sakila`.`inventory` `i` on `r`.`inventory_id` = `i`.`inventory_id`  
join `sakila`.`film` `f` on `i`.`film_id` = `f`.`film_id`  
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id`  
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id`  
group by `f`.`film_id` 

-- Qtd e Valor de Locacao paor categoria
select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id

-- valores por filme e valores por categoria
select 
-- ROW_NUMBER() OVER (PARTITION BY film_rentals.name ) AS row_num,
film_rentals.name as Categoria, locacoes_categoria, valor_locacaocategoria, title as Filme,  locacoes_filme, valor_locafilmes 
from 
(
select `f`.`title` AS `title`, c.category_id, c.name,
count(*) locacoes_filme,
 sum(`p`.`amount`) AS `valor_locafilmes` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by `f`.`title`, c.name) film_rentals
join 
(select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id ) category_films on film_rentals.category_id = category_films.category_id


-- 3  –  Média de  atuação  de cada  ator  em  filmes  geral  do  inventário de  filmes, em  comandos 
-- separados, que podem ser views, quais deles ficaram abaixo da média geral de atuações e quais 
-- ficaram acima da média geral de atuações.  

-- Total de atores 
SELECT count(*) FROM actor 

-- Total de atuações
select count(*) from film_actor

-- Media de Atuacoes por ator
select (select count(*) from film_actor) / (SELECT count(*) FROM actor )

-- N. de atuacoes por ator
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, count(*) n_filmes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id

-- Quais Atores estão abaixo da media de atuações
select ator, n_atuacoes from (
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, count(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id )  a where n_atuacoes < round((select (select count(*) from film_actor) / (SELECT count(*) FROM actor )))

-- Quais Atores estão acima da media de atuações
select ator, n_atuacoes from (
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, count(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id )  a where n_atuacoes > round((select (select count(*) from film_actor) / (SELECT count(*) FROM actor )))

-- 4 – Qual o valor médio de locações de cada categoria e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views,  quais filmes ficaram acima e abaixo da média 
-- da categoria por ano. 

-- Valor medio por locação
select sum(amount)/count(*) from `sakila`.`payment`

-- Valor medio de locacao por categoria
select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria`,
 sum(`p`.`amount`) / count(*) as ValorMedioLocacao
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id


-- Valor medio de locacao por categoria
select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria`,
 sum(`p`.`amount`) / count(*) as ValorMedioLocacao
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id

-- Valor medio de locacao por filme
select 
`f`.`film_id` , `f`.`title` AS `title`, c.category_id, c.name as category,
count(*) n_locacoes,
sum(`p`.`amount`) AS `valor_locado_filme` ,
sum(`p`.`amount`) / count(*) as valor_medio_locacao
from `sakila`.`payment` `p` 
join `sakila`.`rental` `r` on `p`.`rental_id` = `r`.`rental_id` 
join `sakila`.`inventory` `i` on `r`.`inventory_id` = `i`.`inventory_id`  
join `sakila`.`film` `f` on `i`.`film_id` = `f`.`film_id`  
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id`  
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id`  
group by `f`.`film_id` 


-- Filmes abaixo da media da categoria

select title from (
(
select 
`f`.`title` AS `title`, c.category_id, 
sum(`p`.`amount`) / count(*) as valor_medio_locacao
from `sakila`.`payment` `p` 
join `sakila`.`rental` `r` on `p`.`rental_id` = `r`.`rental_id` 
join `sakila`.`inventory` `i` on `r`.`inventory_id` = `i`.`inventory_id`  
join `sakila`.`film` `f` on `i`.`film_id` = `f`.`film_id`  
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id`  
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id`  
group by `f`.`film_id` ) f_locacao
join 
(
select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria`,
 sum(`p`.`amount`) / count(*) as ValorMedioLocacao
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id
) c_locacao on c_locacao.category_id = f_locacao.category_id
)
where f_locacao.valor_medio_locacao < c_locacao.ValorMedioLocacao


-- Filmes acima da media da categoria

select title from (
(
select 
`f`.`title` AS `title`, c.category_id, 
sum(`p`.`amount`) / count(*) as valor_medio_locacao
from `sakila`.`payment` `p` 
join `sakila`.`rental` `r` on `p`.`rental_id` = `r`.`rental_id` 
join `sakila`.`inventory` `i` on `r`.`inventory_id` = `i`.`inventory_id`  
join `sakila`.`film` `f` on `i`.`film_id` = `f`.`film_id`  
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id`  
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id`  
group by `f`.`film_id` ) f_locacao
join 
(
select c.category_id, c.name,
count(*) locacoes_categoria,
 sum(`p`.`amount`) AS `valor_locacaocategoria`,
 sum(`p`.`amount`) / count(*) as ValorMedioLocacao
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.category_id
) c_locacao on c_locacao.category_id = f_locacao.category_id
)
where f_locacao.valor_medio_locacao >= c_locacao.ValorMedioLocacao