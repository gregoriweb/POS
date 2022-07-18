-- Para o schema Employees, responda as seguintes perguntas construindo os comandos SQL
-- 1 – Quantidade de empregados alocados por setor em cada um dos anos, separando em dois 
-- comandos diferentes, que podem ser views, funcionários ativos e inativos conforme o modelo. 
-- 2 – Quantidade de cargos ocupada por cada funcionário no histórico de prestação de serviços 
-- de cada um deles na empresa. 
-- 3 – Média de cargos ocupada por cada funcionário e geral da empresa demonstrado, em 
-- comandos separados, que podem ser views, quais deles ficaram abaixo da média geral de cargos 
-- e quais ficaram acima da média geral de cargos. 
-- 4 – Qual a média de salários de cada departamento e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views, quais focaram acima e abaixo da média por 
-- ano.


-- DROP PROCEDURE IF EXISTS filldates;
-- DELIMITER |
-- CREATE PROCEDURE filldates(dateStart DATE, dateEnd DATE)
-- BEGIN
--   drop table if exists _date_aux;
--   create table _date_aux (date date);
--   WHILE dateStart <= dateEnd DO
--     INSERT INTO _date_aux VALUES (dateStart);
--     SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
--   END WHILE;
-- 	INSERT INTO _date_aux VALUES ('9999-01-01');
-- END;
-- |
-- DELIMITER ;
-- CALL `employees`.`filldates`( (SELECT min(from_date) FROM `employees`.`dept_emp` ), (SELECT max(to_date) FROM `employees`.`dept_emp` where to_date < '9999-01-01'));
-- 
CALL `employees`.`filldates`( (SELECT min(from_date) FROM `employees`.`dept_emp` ), DATE_SUB(date(NOW()), INTERVAL 1 YEAR)); -- NOW  -- 95.781 sec


use employees;

-- 1 – Quantidade de empregados alocados por setor em cada um dos anos, separando em dois 
-- comandos diferentes, que podem ser views, funcionários ativos e inativos conforme o modelo. 

-- Comando 1
SELECT dept_name,  year(dept_emp.from_date), count(*)
FROM dept_emp 
inner join departments on departments.dept_no = dept_emp.dept_no 
inner join employees on employees.emp_no = dept_emp.emp_no 
-- where to_date {} -- ativo { = '9999-01-01'} inativo {< '9999-01-01'}
group by 
dept_name,
year(dept_emp.from_date)
order by 1

-- Comando 2 - Com tabela auxiliar de datas
SELECT dept_name,  year(vdam.month), count(*)
FROM dept_emp 
join departments on departments.dept_no = dept_emp.dept_no 
join employees on employees.emp_no = dept_emp.emp_no 
join _date_aux_months vdam 
	on 	vdam.month >= last_day(from_date) 
		and vdam.month <= ( IF(last_day(to_date) = '9999-01-01', last_day(date(now())), last_day(to_date)) ) 
        and MONTH(vdam.month) = 12
group by 
dept_name,
year(vdam.month)


-- Comando 2 - Com tabela auxiliar de datas - Apenas empregados ativos
SELECT dept_name,  year(vdam.month), count(*)
FROM dept_emp 
join departments on departments.dept_no = dept_emp.dept_no 
join employees on employees.emp_no = dept_emp.emp_no 
join _date_aux_months vdam 
	on 	vdam.month >= last_day(from_date) 
		and vdam.month <= ( IF(last_day(to_date) = '9999-01-01', last_day(date(now())), last_day(to_date)) ) 
        and MONTH(vdam.month) = 12
where to_date = '9999-01-01'
-- where to_date {} -- ativo { = '9999-01-01'} inativo {< '9999-01-01'}
group by 
dept_name,
year(vdam.month)

-- Comando 2 - Com tabela auxiliar de datas - Apenas empregados inativos
SELECT dept_name,  year(vdam.month), count(*)
FROM dept_emp 
join departments on departments.dept_no = dept_emp.dept_no 
join employees on employees.emp_no = dept_emp.emp_no 
join _date_aux_months vdam 
	on 	vdam.month >= last_day(from_date) 
		and vdam.month <= ( IF(last_day(to_date) = '9999-01-01', last_day(date(now())), last_day(to_date)) ) 
        and MONTH(vdam.month) = 12
where to_date < '9999-01-01'
-- where to_date {} -- ativo { = '9999-01-01'} inativo {< '9999-01-01'}
group by 
dept_name,
year(vdam.month)


-- 2 – Quantidade de cargos ocupada por cada funcionário no histórico de prestação de serviços 
-- de cada um deles na empresa. 

SELECT 
	concat(employees.first_name, ' ', employees.last_name) as Employee,
    employees.emp_no,
	count(*) as 'Cargos'
FROM employees.titles
INNER JOIN
    employees ON employees.emp_no = titles.emp_no
group by employees.emp_no
order by Employee


-- select * from employees 
-- where emp_no in ('422538','42199')

-- SELECT 
--     employees.emp_no, concat(employees.last_name, ',', employees.first_name) as Employee, count(*) as 'Dept_Ns.'
-- FROM
--     dept_emp
--         INNER JOIN
--     departments ON departments.dept_no = dept_emp.dept_no
--         INNER JOIN
--     employees ON employees.emp_no = dept_emp.emp_no
-- GROUP BY employees.emp_no
-- order by 3 desc


-- 3 – Média de cargos ocupada por cada funcionário e geral da empresa demonstrado, em 
-- comandos separados, que podem ser views, quais deles ficaram abaixo da média geral de cargos 
-- e quais ficaram acima da média geral de cargos. 

-- Média de cargos por funcionário na companhia
(select distinct Title from titles)
(select distinct emp_no from titles)

(select title, count(*) from titles group by title) 


-- Media de cargos ocupados por cada funcionário
select concat(employees.last_name, ',', employees.first_name) as Employee, count(*) as Titles  from employees
INNER JOIN
    titles ON titles.emp_no = employees.emp_no
group by employees.emp_no
having count(*) > (select count(*) total_titles from titles)/(select count(*) total_employees from employees)





-- Acima da média
select concat(employees.last_name, ',', employees.first_name) as Employee, count(*) as Titles  from employees
INNER JOIN
    titles ON titles.emp_no = employees.emp_no
group by employees.emp_no
having count(*) > (select count(*) total_titles from titles)/(select count(*) total_employees from employees)

-- Abaixo da média
select concat(employees.last_name, ',', employees.first_name) as Employee, count(*) as Titles  from employees
INNER JOIN
    titles ON titles.emp_no = employees.emp_no
group by employees.emp_no
having count(*) < (select count(*) total_titles from titles)/(select count(*) total_employees from employees)

-- select (select count(*) total_titles from titles)/(select count(*) total_employees from employees)
-- 
-- SELECT 
-- 	concat(employees.last_name, ',', employees.first_name) as Employee,
--     employees.emp_no,
-- 	count(*) as 'Titles'
-- FROM employees.titles
-- INNER JOIN
--     employees ON employees.emp_no = titles.emp_no
-- group by employees.emp_no
-- order by Employee

-- 4 – Qual a média de salários de cada departamento e a média geral da empresa demonstrando 
-- em comandos separados, que podem ser views, quais focaram acima e abaixo da média por 
-- ano.
-- Feito com empregados atualmente contratados (where de.to_date = '9999-01-01').
-- Os salário na base parecem ser anuais, um calculo *12 não é necessário

-- Media Salarial Companhia - Funcionarios com contratos vigentes
select  sum(salary)/count(*) as MediaSalarial FROM employees.current_dept_emp de
inner join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
where de.to_date = '9999-01-01'

-- Media Salarial Companhia - Funcionarios com contratos vigentes
SELECT d.dept_name, 
sum(salary)/count(*) MediaSalarial
FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no


-- Departamentos com medias salariais menores
select * from (
SELECT d.dept_name, 
sum(salary)/count(*) MediaSalarial
FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no
) media_dept
where MediaSalarial < 
 (
select  sum(salary)/count(*) as MediaSalarial FROM employees.current_dept_emp de
									inner join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
									where de.to_date = '9999-01-01'
                                    )
                                    
-- Departamentos com medias salariais maiores ou iguais a media
select * from (
SELECT d.dept_name, 
sum(salary)/count(*) MediaSalarial
FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no
) media_dept
where MediaSalarial >= 
 (
select  sum(salary)/count(*) as MediaSalarial FROM employees.current_dept_emp de
									inner join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
									where de.to_date = '9999-01-01'
                                    )




SELECT d.dept_no, 
sum(salary)/count(*) MediaSalarial, 
case when sum(salary)/count(*) < (	select  sum(salary)/count(*) as MediaSalarial FROM employees.current_dept_emp de
									inner join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
									where de.to_date = '9999-01-01' )
then 'Menor que a média'
else 'Maior ou igual a média'
end as ResultadoMedia

FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date 
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no












SELECT 
departments.dept_name, sum(salary), sum(salary)/12 as MediaAnual -- year(dept_emp.from_date)
-- dept_emp.dept_no, employees.emp_no
--    salaries.from_date sfd , dept_emp.from_date dfs , salaries.to_date std , dept_emp.to_date dtd
    -- dept_emp.emp_no, dept_name,  concat(employees.last_name, ',', employees.first_name) as Employee, salary, YEAR(dept_emp.from_date)
FROM
    dept_emp
        INNER JOIN
    departments ON departments.dept_no = dept_emp.dept_no
        INNER JOIN
    employees ON employees.emp_no = dept_emp.emp_no
--		INNER JOIN
--    salaries ON salaries.emp_no = employees.emp_no and salaries.from_date between dept_emp.from_date and dept_emp.to_date and salaries.to_date between dept_emp.from_date and dept_emp.to_date -- salaries.from_date >= dept_emp.from_date and salaries.to_date <= dept_emp.to_date
-- left join  salaries ON salaries.emp_no = employees.emp_no and salaries.from_date >= dept_emp.from_date and salaries.to_date <= dept_emp.to_date
--	left join  salaries ON salaries.emp_no = employees.emp_no and salaries.from_date >= dept_emp.from_date and salaries.to_date <= dept_emp.to_date
left join  salaries ON salaries.emp_no = dept_emp.emp_no 
			and last_day(salaries.from_date) >= last_day(dept_emp.from_date) and last_day(salaries.to_date) <= last_day(dept_emp.to_date)
            
group by dept_emp.dept_no


























SELECT 
    dept_name,  concat(employees.last_name, ',', employees.first_name) as Employee, salary, YEAR(dept_emp.from_date)
FROM
    dept_emp
        INNER JOIN
    departments ON departments.dept_no = dept_emp.dept_no
        INNER JOIN
    employees ON employees.emp_no = dept_emp.emp_no
            INNER JOIN
    salaries ON salaries.emp_no = employees.emp_no and salaries.from_date >= dept_emp.from_date and salaries.to_date <= dept_emp.to_date

GROUP BY YEAR(salaries.from_date)
ORDER BY 1

--media geral da empresa:
total_salario/total_empregado

--media departamento
total_salario/total_empregado (por departamento)

--demonstrando quais ficaram acima e abaixo da media
flag 