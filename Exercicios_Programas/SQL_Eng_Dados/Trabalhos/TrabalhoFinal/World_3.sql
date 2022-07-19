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

use world;

-- 1  – Top 3 continentes em quantidade populacional registrados na base de dados. 
	use world;
	SELECT Continent, sum(Population) Population FROM world.country
	group by Continent
	order by Population desc
	limit 3;

-- 2  – Expectativa de vida média por país e geral do planeta, de acordo com os dados registrados 
-- em comandos separados, que podem ser views, quais deles ficaram abaixo e quais ficaram acima 
-- da média geral da expectativa de vida. 

	-- Expectativa media por pais
		-- Query origem:
			use world;
			SELECT Code, Name, LifeExpectancy FROM world.country;
		-- View derivada:
			use world;
			CREATE VIEW v_world_country_lifeexpectancy AS
				SELECT Code, Name, LifeExpectancy FROM world.country;

	-- Expectativa media do planeta
		-- Query origem:
			use world;
			SELECT sum(LifeExpectancy) / count(*) as WorldLifeExpectancy FROM world.country;
		-- View derivada:
			use world;
			CREATE VIEW v_world_world_lifeexpectancy AS
				SELECT sum(LifeExpectancy) / count(*) as WorldLifeExpectancy  FROM world.country;
        
	-- Paises com Expectativa de Vida maior que a media
		-- Sem as views:
			use world;
			select * from (
			select Name, LifeExpectancy FROM world.country ) lew
			where lew.LifeExpectancy >= (SELECT sum(LifeExpectancy) / count(*)  FROM world.country);
		
		-- Com as Views 
			use world;
			SET @world_lifeexpectancy = (select WorldLifeExpectancy from v_world_world_lifeexpectancy);
			select * FROM  v_world_country_lifeexpectancy
			where LifeExpectancy >= @world_lifeexpectancy;

	-- Paises com Expectativa de Vida menor que a media
		-- Sem as views: 
			use world;
			select * from (
			select Name, LifeExpectancy FROM world.country ) lew
			where lew.LifeExpectancy < (SELECT sum(LifeExpectancy) / count(*)  FROM world.country);
            
		-- Com as Views 
			use world;
			SET @world_lifeexpectancy = (select WorldLifeExpectancy from v_world_world_lifeexpectancy);
			select * FROM  v_world_country_lifeexpectancy
			where LifeExpectancy < @world_lifeexpectancy;


-- 3  – Média de quantidade populacional de cada país por continente, em comandos separados, 
-- que podem ser views, quais deles ficaram  abaixo da média geral de atuações e quais ficaram 
-- acima da média geral da população levando em consideração o agrupamento dos  continentes.  

	-- Media populacional de cada continente
		use world;
		SELECT 	Continent, count(*) 'N. Countries', sum(LifeExpectancy)/count(*) as ContinentLifeExpectancy FROM world.country
		group by Continent;
        
	-- View Derivada
		use world;
		CREATE VIEW v_world_continent_lifeexpectancy AS
			SELECT 	Continent, count(*) 'N. Countries', sum(LifeExpectancy)/count(*) as ContinentLifeExpectancy FROM world.country
			group by Continent;
	
	-- Paises com expectativa de vida maior que a média de seu continente
		-- Sem views
			use world;
			select Name Pais from (
				(SELECT 	Continent, sum(LifeExpectancy)/count(*) exp_vida_continente FROM world.country
				group by Continent) continente
				join (SELECT Continent, Name, LifeExpectancy as exp_vida_pais FROM world.country) pais
				on pais.Continent = continente.Continent
				)
			where exp_vida_pais >= exp_vida_continente;
		
        -- Com views
			use world;
			SELECT 
				*
			FROM
				country c
					JOIN
				v_world_continent_lifeexpectancy cm ON c.Continent = cm.Continent
					AND c.LifeExpectancy >= cm.ContinentLifeExpectancy;

	-- Paises com expectativa de vida menor que a média de seu continente
		-- Sem views
			use world;
			select Name Pais from (
			(SELECT 	Continent, sum(LifeExpectancy)/count(*) exp_vida_continente FROM world.country
			group by Continent) continente
			join (SELECT Continent, Name, LifeExpectancy as exp_vida_pais FROM world.country) pais
			on pais.Continent = continente.Continent
			)
			where exp_vida_pais < exp_vida_continente;
            
		-- Com views
			use world;
			SELECT 
				*
			FROM
				country c
					JOIN
				v_world_continent_lifeexpectancy cm ON c.Continent = cm.Continent
					AND c.LifeExpectancy < cm.ContinentLifeExpectancy;