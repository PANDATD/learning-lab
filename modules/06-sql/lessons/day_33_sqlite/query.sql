-- Find all departments that have at least 2 employees earning ₹40,000 or more. For each qualifying department, display:
--
-- department name
-- number of qualifying employees
-- average salary of those qualifying employees
--
-- Only include departments whose average salary is at least ₹50,000.
--
-- Sort the results by average salary descending. 

select
    d.department_name as department_name,
    count(e.employee_id) as qualifying_employees,
    avg(e.salary) as average_salary
from employee as e
inner join department as d
    on e.department_id = d.department_id
where (e.salary) >= 40000
group by d.department_name
having (qualifying_employees) >=2 and (average_salary) >= 50000
order by average_salary desc;

-- +-----------------+----------------------+----------------+
-- | department_name | qualifying_employees | average_salary |
-- +-----------------+----------------------+----------------+
-- | Engineering     | 2                    | 55000.0        |
-- +-----------------+----------------------+----------------+

