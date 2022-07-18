SELECT 
*
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
where dept_emp.emp_no = 11092




-- Usando views

-- -- Total atual de salarios por departamento
SELECT d.dept_no, sum(salary) FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no

-- -- Total atual de empregados por
SELECT d.dept_no, count(*) FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no

-- -- Total atual de empregados por
SELECT d.dept_no, count(*) FROM employees.current_dept_emp de
left join  salaries s ON s.emp_no = de.emp_no and s.to_date = de.to_date
left join departments d on d.dept_no = de.dept_no
where de.to_date = '9999-01-01'
group by d.dept_no


