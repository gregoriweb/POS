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


-- 1  –  Quantidade de filmes  locados  por  categoria  em  cada  um  dos  anos, separando em  dois 
-- comandos  diferentes, que podem ser  views, a  lista  de  filmes  e  a  lista  de  filmes  com  seus 
-- respectivos atores.  


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



select 
year(r.rental_date) ano,
`c`.`name` AS `category`,
f.title,
count(*) n_locacoes
-- sum(`p`.`amount`) AS `total_sales` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by `c`.`name` , f.title, year(r.rental_date) 
order by ano, category, n_locacoes desc
-- order by `total_sales` desc;




select 
year(r.rental_date) ano,
`c`.`name` AS `category`,
f.title,
group_concat(
			concat(
				concat(
					upper(substr(`a`.`first_name`,1,1)),
					lower(substr(`a`.`first_name`,2,length(`a`.`first_name`))),
                    _utf8mb4' ',
                    concat(
						upper(substr(`a`.`last_name`,1,1)),
                        lower(substr(`a`.`last_name`,2,length(`a`.`last_name`)))
                        )
                        )
                        ) separator ', ') AS `actors` ,
count(*) n_locacoes
-- sum(`p`.`amount`) AS `total_sales` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
join `sakila`.`film_actor` fa on((`f`.`film_id` = `fa`.`film_id`)) 
join `sakila`.`actor` a on((`fa`.`actor_id` = `a`.`actor_id`)) 
group by `c`.`name` , f.title, year(r.rental_date) 
order by ano, category, n_locacoes desc
-- order by `total_sales` desc;



-- 2  – Quantidade de filmes por categoria e os valores totais de locação de cada filme, separando 
-- em dois comandos diferentes, que podem ser views, valores por filme e valores por categoria. 


-- Qtd Filmes Categoria
select c.category_id, c.name,
count(*) qtd_filmes_categoria
from `sakila`.`film` `f` 
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id` 
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id` 
group by c.category_id

-- Valor Filmes Categoria
select 
c.category_id, c.name,
sum(p.amount) valor_locado_categoria
from `sakila`.`payment` `p` 
join `sakila`.`rental` `r`  on `p`.`rental_id` = `r`.`rental_id` 
join `sakila`.`inventory` `i` on `r`.`inventory_id` = `i`.`inventory_id` 
join `sakila`.`film` `f` on `i`.`film_id` = `f`.`film_id` 
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id` 
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id` 
group by c.category_id


-- Qtd e Valor de Locacao por filme
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


--  Quantidade de filmes por categoria e os valores totais de locação de cada filme

select * from (
select c.category_id, c.name,
count(*) qtd_filmes_categoria
from `sakila`.`film` `f` 
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id` 
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id` 
group by c.category_id ) qtd_filmes_categoria
join 




select * from sakila.rental where rental_id = 1109


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




-- Filmes Categoria
select c.category_id, c.name,
count(*) filmes_categoria
from `sakila`.`film` `f` 
join `sakila`.`film_category` `fc` on `f`.`film_id` = `fc`.`film_id` 
join `sakila`.`category` `c` on `fc`.`category_id` = `c`.`category_id` 
group by c.category_id







select `c`.`name` AS `category`,
count(*) n_locacoes,
count(`f`.`film_id`) n_films,
 sum(`p`.`amount`) AS `total_sales` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by `c`.`name` order by `n_locacoes` desc;

select `f`.`title` AS `title`, c.category_id, c.name,
count(*) n_rentals,
 sum(`p`.`amount`) AS `total_sales` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by `f`.`title`, c.name order by `name` desc;


select c.category_id, c.name,
count(*) n_films,
 sum(`p`.`amount`) AS `total_sales` 
from (((((`sakila`.`payment` `p` 
join `sakila`.`rental` `r` on((`p`.`rental_id` = `r`.`rental_id`))) 
join `sakila`.`inventory` `i` on((`r`.`inventory_id` = `i`.`inventory_id`))) 
join `sakila`.`film` `f` on((`i`.`film_id` = `f`.`film_id`))) 
join `sakila`.`film_category` `fc` on((`f`.`film_id` = `fc`.`film_id`))) 
join `sakila`.`category` `c` on((`fc`.`category_id` = `c`.`category_id`))) 
group by c.name, c.name order by `n_films` desc;




select film_rentals.name as Categoria, locacoes_categoria, valor_locacaocategoria, title as Filme,  locacoes_filme, valor_locafilmes  from 
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


