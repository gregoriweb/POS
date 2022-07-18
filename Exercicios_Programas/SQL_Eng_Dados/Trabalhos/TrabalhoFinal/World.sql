-- 
-- Para o schema world, responda as seguintes perguntas construindo os comandos SQL 
--  
-- 1  – Top 3 continentes em quantidade populacional registrados na base de dados.  
-- 2  – Expectativa de vida média por país e geral do planeta, de acordo com os dados registrados 
-- em comandos separados, que podem ser views, quais deles ficaram abaixo e quais ficaram acima 
-- da média geral da expectativa de vida. 
-- 3  – Média de quantidade populacional de cada país por continente, em comandos separados, 
-- que podem ser views, quais deles ficaram  abaixo da média geral de atuações e quais ficaram 
-- acima da média geral da população levando em consideração o agrupamento dos  continentes.  
-- 4 – Qual o valor médio de locações de cada categoria e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views,  quais filmes ficaram acima e abaixo da média 
-- da categoria por ano. 


-- 1  – Top 3 continentes em quantidade populacional registrados na base de dados.  
SELECT Continent, sum(Population) FROM world.country
group by Continent
limit 3

-- 2  – Expectativa de vida média por país e geral do planeta, de acordo com os dados registrados 
-- em comandos separados, que podem ser views, quais deles ficaram abaixo e quais ficaram acima 
-- da média geral da expectativa de vida. 

-- Expectativa media por pais
SELECT -- Code, 
	Name, LifeExpectancy FROM world.country

-- Expectativa media do planeta
SELECT sum(LifeExpectancy) / count(*)  FROM world.country

-- Paises com Expectativa de Vida maior que a media
select * from (
select Name, LifeExpectancy FROM world.country ) lew
where lew.LifeExpectancy > (SELECT sum(LifeExpectancy) / count(*)  FROM world.country)

-- Paises com Expectativa de Vida menor que a media
select * from (
select Name, LifeExpectancy FROM world.country ) lew
where lew.LifeExpectancy < (SELECT sum(LifeExpectancy) / count(*)  FROM world.country)


-- 3  – Média de quantidade populacional de cada país por continente, em comandos separados, 
-- que podem ser views, quais deles ficaram  abaixo da média geral de atuações e quais ficaram 
-- acima da média geral da população levando em consideração o agrupamento dos  continentes.  

-- Media populacional de cada continente
SELECT 	Continent, Name, LifeExpectancy, count(*), sum(LifeExpectancy), sum(LifeExpectancy)/count(*) FROM world.country
group by Continent

-- Paises com expectativa de vida maior que a média de seu continente
select Name Pais from (
(SELECT 	Continent, sum(LifeExpectancy)/count(*) exp_vida_continente FROM world.country
group by Continent) continente
join (SELECT Continent, Name, LifeExpectancy as exp_vida_pais FROM world.country) pais
on pais.Continent = continente.Continent
)
where exp_vida_pais >= exp_vida_continente

-- Paises com expectativa de vida menor que a média de seu continente
select Name Pais from (
(SELECT 	Continent, sum(LifeExpectancy)/count(*) exp_vida_continente FROM world.country
group by Continent) continente
join (SELECT Continent, Name, LifeExpectancy as exp_vida_pais FROM world.country) pais
on pais.Continent = continente.Continent
)
where exp_vida_pais < exp_vida_continente




