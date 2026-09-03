SELECT 
    d.department_name,
    COUNT(e.employee_id) AS employee_count
FROM employee as e
INNER JOIN department as d
    ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) >=2
ORDER BY employee_count DESC;
