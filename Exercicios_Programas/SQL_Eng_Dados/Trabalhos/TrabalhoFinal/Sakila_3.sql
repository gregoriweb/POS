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

-- View Lista de Filmes
	use sakila;
	create or replace view v_sakila_filmes as	
        select f.film_id AS film_id,
        f.title AS title,
        f.description AS description,
        f.release_year as release_year,
        f.length,
        f.rating
        from film f;
        
-- View Lista de Filmes e atores
	use sakila;
	create or replace view v_sakila_filmes_atores as	
	select f.film_id AS film_id,
			f.title AS title,
			f.description AS description,
            f.release_year as release_year,
			f.length AS length,
			f.rating AS rating,
			group_concat(concat(a.first_name,_utf8mb4' ',a.last_name) separator ', ') AS actors
			from film f
				left join film_actor fa on f.film_id = fa.film_id 
				left join actor a on fa.actor_id = a.actor_id
			group by film_id;

-- View Lista de Filmes, atores e categorias
	use sakila;
	create or replace view v_sakila_filmes_atores_categorias as	
	select f.film_id AS film_id,
			f.title AS title,
			f.description AS description,
            c.category_id AS category_id,
			c.name AS category,
			f.length AS length,
			f.rating AS rating,
			group_concat(concat(a.first_name,_utf8mb4' ',a.last_name) separator ', ') AS actors
			from category c
				left join film_category fc on c.category_id = fc.category_id
				left join film f on fc.film_id = f.film_id 
				left join film_actor fa on f.film_id = fa.film_id 
				left join actor a on fa.actor_id = a.actor_id 
			group by f.film_id,c.name;
	

-- View Locacoes, Ids Filmes, Ids Category
	create or replace view v_sakila_filmes_locacoes as
	select rental_id, rental_date, f.film_id, fc.category_id from rental r
		JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
		JOIN sakila.film f ON i.film_id = f.film_id
		JOIN sakila.film_category fc ON f.film_id = fc.film_id;
        
-- View Ids Locacoes, Ids Filmes, Ids Category Agrupado por ano
	create or replace view v_sakila_filmes_locacoes_ano as 
	select year(rental_date)  ano, fc.category_id, count(*) qtde_filmes_locados from rental r
		JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
		JOIN sakila.film f ON i.film_id = f.film_id
		JOIN sakila.film_category fc ON f.film_id = fc.film_id
        group by year(rental_date), fc.category_id;

-- Views Locacoes por ano e categoria
	create or replace view v_sakila_locacoes_ano_categoria as
	select year(rental_date) ano, fc.category_id, count(*) qtde_locacao from rental r
		JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
		JOIN sakila.film f ON i.film_id = f.film_id
		JOIN sakila.film_category fc ON f.film_id = fc.film_id
	group by fc.category_id;

 -- Quantidade de Filmes locados por categoria em cada ano
	use sakila;
	SELECT 
		YEAR(rental_date) ano,
		c.name AS category,
		COUNT(*) n_locacoes
	FROM
		sakila.payment p
		JOIN sakila.rental r ON p.rental_id = r.rental_id
		JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
		JOIN sakila.film f ON i.film_id = f.film_id
		JOIN sakila.film_category fc ON f.film_id = fc.film_id
		JOIN sakila.category c ON fc.category_id = c.category_id
	GROUP BY c.name , YEAR(r.rental_date)
	ORDER BY n_locacoes DESC;
    

 -- Quantidade de Filmes locados por categoria em cada ano com as views
 -- v_sakila_locacoes_ano_categoria e  v_sakila_filmes_locacoes_ano
    select lac.ano, c.name as 'Categoria', qtde_locacao as 'Qtde de Locações', qtde_filmes_locados 'Qtde Filmes Locados' from v_sakila_locacoes_ano_categoria lac
    join v_sakila_filmes_locacoes_ano laf on lac.category_id = laf.category_id and lac.ano = laf.ano
    join category c on laf.category_id = c.category_id
    group by  lac.ano, laf.category_id
    order by ano, categoria
    

-- 2  – Quantidade de filmes por categoria e os valores totais de locação de cada filme, separando 
-- em dois comandos diferentes, que podem ser views, valores por filme e valores por categoria. 
        
	-- View Qtd Locações e Valor Locação por Filme
		use sakila;
		create or replace view v_sakila_qtd_valor_por_filme as
			select 
			f.film_id, 
            c.category_id, 
            f.title AS title, 
            c.name as category,
			COUNT(*) n_locacoes,
			sum(p.amount) AS valor_locado_filme 
			from sakila.payment p 
			join sakila.rental r on p.rental_id = r.rental_id 
			join sakila.inventory i on r.inventory_id = i.inventory_id  
			join sakila.film f on i.film_id = f.film_id  
			join sakila.film_category fc on f.film_id = fc.film_id  
			join sakila.category c on fc.category_id = c.category_id  
			group by f.film_id;

	-- View Qtd e Valor de Locacao por categoria
		use sakila;
        create or replace view v_sakila_qtd_valor_por_categoria as
			select c.category_id, c.name as category,
			COUNT(*) locacoes_categoria,
			sum(p.amount) AS valor_locacaocategoria 
			from sakila.payment p 
			join sakila.rental r on p.rental_id = r.rental_id 
			join sakila.inventory i on r.inventory_id = i.inventory_id 
			join sakila.film f on i.film_id = f.film_id 
			join sakila.film_category fc on f.film_id = fc.film_id 
			join sakila.category c on fc.category_id = c.category_id 
			group by c.category_id;

-- Quantidade de filmes por categoria e os valores totais de locação de cada filme
	-- Quantidade de filmes por categoria e com quantidades e valores de locação para cada categoria
		select vc.category as Categoria, locacoes_categoria QtdeLocacoes, valor_locacaocategoria ValorEmLocacaoCategoria, count(*) QtdFilmesNaCategoria from v_sakila_qtd_valor_por_filme vf
		join v_sakila_qtd_valor_por_categoria vc on vc.category_id = vf.category_id
		group by vc.category_id;

	-- e os valores totais de locação de cada filme
		select title as Filme, n_locacoes QtdeLocacoes, valor_locado_filme ValorEmLocacaoFilme from v_sakila_qtd_valor_por_filme;

-- 3  –  Média de  atuação  de cada  ator  em  filmes  geral  do  inventário de  filmes, em  comandos 
-- separados, que podem ser views, quais deles ficaram abaixo da média geral de atuações e quais 
-- ficaram acima da média geral de atuações.  

-- Total de atores 
SELECT COUNT(*) FROM actor;

-- Total de atuações
select COUNT(*) from film_actor;

-- Media de Atuacoes por ator
select (select COUNT(*) from film_actor) / (SELECT COUNT(*) FROM actor);

-- N. de atuacoes por ator
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, COUNT(*) n_filmes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id;

-- View Quais Atores estão abaixo da media de atuações
create or replace view v_sakila_atores_abaixo_media_atuacao as
select ator, n_atuacoes from (
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, COUNT(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id )  a where n_atuacoes < round((select COUNT(*) from film_actor) / (SELECT COUNT(*) FROM actor));

-- View Quais Atores estão acima da media de atuações
create or replace view v_sakila_atores_acima_media_atuacao as
select ator, n_atuacoes from (
SELECT a.actor_id, concat(a.first_name, ' ', a.last_name) ator, COUNT(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id )  a where n_atuacoes >= round((select COUNT(*) from film_actor) / (SELECT COUNT(*) FROM actor));

-- Atores acima da média de atuações:
select * from v_sakila_atores_acima_media_atuacao;

-- Atores abaixo da média de atuações:
select * from v_sakila_atores_abaixo_media_atuacao;

-- 4 – Qual o valor médio de locações de cada categoria e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views,  quais filmes ficaram acima e abaixo da média 
-- da categoria por ano. 

-- Valor medio por locação
create or replace view v_sakila_valor_medio_locacao as
select sum(amount)/COUNT(*) from sakila.payment;



-- Valor medio de locacao por categoria
create or replace view v_sakila_valor_medio_locacao_por_categoria as
select c.category_id, c.name,
COUNT(*) n_locacoes_categoria,
 sum(p.amount) AS valor_total_em_locacoes_categoria,
 sum(p.amount) / COUNT(*) as valor_medio_por_locacao_por_categoria
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id 
join sakila.film f on i.film_id = f.film_id 
join sakila.film_category fc on f.film_id = fc.film_id 
join sakila.category c on fc.category_id = c.category_id 
group by c.category_id;

-- Valor medio de locacao por categoria por ano
create or replace view v_sakila_valor_medio_locacao_por_categoria_por_ano as
select year(rental_date) ano_locacao,
c.category_id, c.name,
COUNT(*) n_locacoes_categoria,
 sum(p.amount) AS valor_total_em_locacoes_categoria_por_ano,
 sum(p.amount) / COUNT(*) as valor_medio_por_locacao_por_categoria_por_ano
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id 
join sakila.film f on i.film_id = f.film_id 
join sakila.film_category fc on f.film_id = fc.film_id 
join sakila.category c on fc.category_id = c.category_id 
group by c.category_id, year(rental_date);


-- Valor medio de locacao por filme
create or replace view v_sakila_valor_medio_locacao_por_filme as
select 
f.film_id , f.title AS title, c.category_id, c.name as category,
COUNT(*) n_locacoes_filme,
sum(p.amount) AS valor_total_em_locacoes_filme ,
sum(p.amount) / COUNT(*) as valor_medio_por_locacao_por_filme
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id  
join sakila.film f on i.film_id = f.film_id  
join sakila.film_category fc on f.film_id = fc.film_id  
join sakila.category c on fc.category_id = c.category_id  
group by f.film_id;

-- Valor medio de locacao por filme por ano
create or replace view v_sakila_valor_medio_locacao_por_filme_por_ano as
select year(rental_date) ano_locacao,
f.film_id , f.title AS title, c.category_id, c.name as category,
COUNT(*) n_locacoes_filme,
sum(p.amount) AS valor_total_em_locacoes_filme_por_ano ,
sum(p.amount) / COUNT(*) as valor_medio_por_locacao_por_filme_por_ano
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id  
join sakila.film f on i.film_id = f.film_id  
join sakila.film_category fc on f.film_id = fc.film_id  
join sakila.category c on fc.category_id = c.category_id  
group by f.film_id,year(rental_date);


-- View Filmes abaixo da media da categoria
create or replace view v_sakila_filmes_abaixo_media_locacao_da_categoria as 
SELECT mf.category as 'Categoria', title as Filme, valor_medio_por_locacao_por_filme as 'Valor Medio por Filme', valor_medio_por_locacao_por_categoria as 'Valor Medio por Categoria' FROM v_sakila_valor_medio_locacao_por_filme mf
join v_sakila_valor_medio_locacao_por_categoria mc 
	on mf.category_id = mc.category_id and mf.valor_medio_por_locacao_por_filme < mc.valor_medio_por_locacao_por_categoria
order by Categoria, `Valor Medio por Filme` asc;

-- View Filmes abaixo da media da categoria por ano
create or replace view v_sakila_filmes_abaixo_media_locacao_da_categoria_ano as 
SELECT mfa.category as 'Categoria', mca.ano_locacao,  title as Filme, valor_medio_por_locacao_por_filme_por_ano as 'Valor Medio por Filme/Ano', 
	   valor_medio_por_locacao_por_categoria_por_ano as 'Valor Medio por Categoria/Ano' 
FROM v_sakila_valor_medio_locacao_por_filme_por_ano mfa
join v_sakila_valor_medio_locacao_por_categoria_por_ano mca
	on mfa.category_id = mca.category_id and mfa.ano_locacao = mca.ano_locacao and mfa.valor_medio_por_locacao_por_filme_por_ano < mca.valor_medio_por_locacao_por_categoria_por_ano
-- order by ano_locacao, Categoria, `Valor Medio por Filme/Ano` asc;
order by Filme, ano_locacao;


-- View Filmes acima da media da categoria
create or replace view v_sakila_filmes_acima_media_locacao_da_categoria as 
SELECT mf.category as 'Categoria', title as Filme, valor_medio_por_locacao_por_filme as 'Valor Medio por Filme', valor_medio_por_locacao_por_categoria as 'Valor Medio por Categoria' FROM v_sakila_valor_medio_locacao_por_filme mf
join v_sakila_valor_medio_locacao_por_categoria mc 
	on mf.category_id = mc.category_id and mf.valor_medio_por_locacao_por_filme >= mc.valor_medio_por_locacao_por_categoria
order by Categoria, `Valor Medio por Filme` asc;

-- View Filmes acima da media da categoria por ano
create or replace view v_sakila_filmes_acima_media_locacao_da_categoria_ano as 
SELECT mfa.category as 'Categoria', mca.ano_locacao,  title as Filme, valor_medio_por_locacao_por_filme_por_ano as 'Valor Medio por Filme/Ano', 
	   valor_medio_por_locacao_por_categoria_por_ano as 'Valor Medio por Categoria/Ano' 
FROM v_sakila_valor_medio_locacao_por_filme_por_ano mfa
join v_sakila_valor_medio_locacao_por_categoria_por_ano mca
	on mfa.category_id = mca.category_id and mfa.ano_locacao = mca.ano_locacao and mfa.valor_medio_por_locacao_por_filme_por_ano >= mca.valor_medio_por_locacao_por_categoria_por_ano
-- order by ano_locacao, Categoria, `Valor Medio por Filme/Ano` asc;
order by Filme, ano_locacao;


-- Filmes acima da media de locacao de sua categoria:
select * from v_sakila_filmes_acima_media_locacao_da_categoria;

-- Filmes acima da media de locacao de sua categoria por ano
select * from v_sakila_filmes_acima_media_locacao_da_categoria_ano;

-- Filmes abaixo da media de locacao de sua categoria:
select * from v_sakila_filmes_abaixo_media_locacao_da_categoria;

-- Filmes abaixo da media de locacao de sua categoria por ano:
select * from v_sakila_filmes_abaixo_media_locacao_da_categoria_ano;


-- ----------------------------------------------------------------------------------------------------------------------------------

select title from (

select 
f.title AS title, c.category_id, 
sum(p.amount) / COUNT(*) as valor_medio_locacao
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id  
join sakila.film f on i.film_id = f.film_id  
join sakila.film_category fc on f.film_id = fc.film_id  
join sakila.category c on fc.category_id = c.category_id  
group by f.film_id ) f_locacao
join 
(
select c.category_id, c.name,
COUNT(*) locacoes_categoria,
 sum(p.amount) AS valor_locacaocategoria,
 sum(p.amount) / COUNT(*) as ValorMedioLocacao
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id 
join sakila.film f on i.film_id = f.film_id 
join sakila.film_category fc on f.film_id = fc.film_id 
join sakila.category c on fc.category_id = c.category_id 
group by c.category_id )
 c_locacao on c_locacao.category_id = f_locacao.category_id

where f_locacao.valor_medio_locacao < c_locacao.ValorMedioLocacao



-- Filmes acima da media da categoria

select title from 

select 
f.title AS title, c.category_id, 
sump.amount / COUNT(*) as valor_medio_locacao
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id  
join sakila.film f on i.film_id = f.film_id  
join sakila.film_category fc on f.film_id = fc.film_id  
join sakila.category c on fc.category_id = c.category_id  
group by f.film_id  f_locacao
join 

select c.category_id, c.name,
COUNT(*) locacoes_categoria,
 sump.amount AS valor_locacaocategoria,
 sump.amount / COUNT(*) as ValorMedioLocacao
from sakila.payment p 
join sakila.rental r onp.rental_id = r.rental_id 
join sakila.inventory i onr.inventory_id = i.inventory_id 
join sakila.film f oni.film_id = f.film_id 
join sakila.film_category fc onf.film_id = fc.film_id 
join sakila.category c onfc.category_id = c.category_id 
group by c.category_id
 c_locacao on c_locacao.category_id = f_locacao.category_id

where f_locacao.valor_medio_locacao >= c_locacao.ValorMedioLocacao