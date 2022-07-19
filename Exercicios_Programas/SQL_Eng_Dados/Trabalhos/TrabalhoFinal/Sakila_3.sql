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

-- Lista de Filmes e atores
	use sakila;
	select f.film_id AS FID,
			f.title AS title,
			f.description AS description,
			c.name AS category,
			f.rental_rate AS price,
			f.length AS length,
			f.rating AS rating,
			group_concat(concat(a.first_name,_utf8mb4' ',a.last_name) separator ', ') AS actors 
			from category c
				left join film_category fc on c.category_id = fc.category_id
				left join film f on fc.film_id = f.film_id 
				left join film_actor fa on f.film_id = fa.film_id 
				left join actor a on fa.actor_id = a.actor_id 
			group by f.film_id,c.name;
        
-- View Lista de Filmes e atores
	use sakila;
	create view v_sakila_filmes_atores as	
        select f.film_id AS film_id,
        f.title AS title,
        f.description AS description,
        c.name AS category,
        f.rental_rate AS price,
        f.length AS length,
        f.rating AS rating,
        group_concat(concat(a.first_name,_utf8mb4' ',a.last_name) separator ', ') AS actors 
        from category c
			left join film_category fc on c.category_id = fc.category_id
            left join film f on fc.film_id = f.film_id 
            left join film_actor fa on f.film_id = fa.film_id 
            left join actor a on fa.actor_id = a.actor_id 
		group by f.film_id,c.name;

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


 -- Quantidade de Filmes locados por categoria com View
	use sakila;
	SELECT 
		YEAR(rental_date) ano,
		vfa.category as category,
		COUNT(*) n_locacoes
	FROM
		sakila.payment p
		JOIN sakila.rental r ON p.rental_id = r.rental_id
		JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
		JOIN v_sakila_filmes_atores vfa on i.film_id = vfa.film_id
	GROUP BY vfa.category , YEAR(r.rental_date)
    ORDER BY n_locacoes DESC;
    

-- 2  – Quantidade de filmes por categoria e os valores totais de locação de cada filme, separando 
-- em dois comandos diferentes, que podem ser views, valores por filme e valores por categoria. 

	-- Qtd Locações e Valor Locação por Filme
		use sakila;
		select 
		f.film_id , f.title AS title, c.category_id, c.name as category,
		COUNT(*) n_locacoes,
		sum(p.amount) AS valor_locado_filme 
		from sakila.payment p 
		join sakila.rental r on p.rental_id = r.rental_id 
		join sakila.inventory i on r.inventory_id = i.inventory_id  
		join sakila.film f on i.film_id = f.film_id  
		join sakila.film_category fc on f.film_id = fc.film_id  
		join sakila.category c on fc.category_id = c.category_id  
		group by f.film_id;
        
	-- View Qtd Locações e Valor Locação por Filme
		use sakila;
		create view v_sakila_qtd_valor_por_filme as
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


	-- Qtd e Valor de Locacao por categoria
		use sakila;
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
        
	-- Qtd e Valor de Locacao por categoria
		use sakila;
        create view v_sakila_qtd_valor_por_categoria as
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
SELECT COUNT(*) FROM actor 

-- Total de atuações
select COUNT(*) from film_actor

-- Media de Atuacoes por ator
select select COUNT(*) from film_actor / SELECT COUNT(*) FROM actor 

-- N. de atuacoes por ator
SELECT a.actor_id, concata.first_name, ' ', a.last_name ator, COUNT(*) n_filmes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id

-- Quais Atores estão abaixo da media de atuações
select ator, n_atuacoes from 
SELECT a.actor_id, concata.first_name, ' ', a.last_name ator, COUNT(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id   a where n_atuacoes < roundselect select COUNT(*) from film_actor / SELECT COUNT(*) FROM actor 

-- Quais Atores estão acima da media de atuações
select ator, n_atuacoes from 
SELECT a.actor_id, concata.first_name, ' ', a.last_name ator, COUNT(*) n_atuacoes
FROM film_actor fa
join film f on f.film_id = fa.film_id
join actor a on a.actor_id = fa.actor_id
group by a.actor_id   a where n_atuacoes > roundselect select COUNT(*) from film_actor / SELECT COUNT(*) FROM actor 

-- 4 – Qual o valor médio de locações de cada categoria e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views,  quais filmes ficaram acima e abaixo da média 
-- da categoria por ano. 

-- Valor medio por locação
select sumamount/COUNT(*) from sakila.payment

-- Valor medio de locacao por categoria
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


-- Valor medio de locacao por categoria
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

-- Valor medio de locacao por filme
select 
f.film_id , f.title AS title, c.category_id, c.name as category,
COUNT(*) n_locacoes,
sump.amount AS valor_locado_filme ,
sump.amount / COUNT(*) as valor_medio_locacao
from sakila.payment p 
join sakila.rental r on p.rental_id = r.rental_id 
join sakila.inventory i on r.inventory_id = i.inventory_id  
join sakila.film f on i.film_id = f.film_id  
join sakila.film_category fc on f.film_id = fc.film_id  
join sakila.category c on fc.category_id = c.category_id  
group by f.film_id 


-- Filmes abaixo da media da categoria

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