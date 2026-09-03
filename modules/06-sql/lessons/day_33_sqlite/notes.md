# Day 33 — Aggregation, GROUP BY, HAVING

## Objective

Combine `JOIN`, `WHERE`, `GROUP BY`, aggregate functions, `HAVING`, and
`ORDER BY` in a single business-oriented SQL query.

## Core Concepts

### WHERE vs HAVING

- `WHERE` filters individual rows **before grouping and aggregation**.
- `HAVING` filters groups **after grouping and aggregation**.

Mental model:

```text
Individual rows
      ↓
    WHERE
      ↓
  GROUP BY
      ↓
 Aggregate
 COUNT / AVG / SUM
      ↓
   HAVING
      ↓
  ORDER BY
```

## Query Construction Method

When translating a business requirement into SQL, decompose it:

1. What information must be displayed? → `SELECT`
2. Which tables contain that information? → `FROM` / `JOIN`
3. Which individual rows qualify? → `WHERE`
4. What should form each group? → `GROUP BY`
5. What values must be calculated? → aggregate functions
6. Which groups qualify? → `HAVING`
7. How should the final result be ordered? → `ORDER BY`

## Final Challenge

Requirement:

> Find all departments that have at least 2 employees earning ₹40,000 or
> more. For each qualifying department, display the department name, number
> of qualifying employees, and average salary of those qualifying employees.
> Only include departments whose average salary is at least ₹50,000. Sort by
> average salary descending.

## Final Query

```sql
SELECT
    d.department_name,
    COUNT(e.employee_id) AS qualifying_employees,
    AVG(e.salary) AS average_salary
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE e.salary >= 40000
GROUP BY d.department_name
HAVING COUNT(e.employee_id) >= 2
   AND AVG(e.salary) >= 50000
ORDER BY average_salary DESC;
```

## Why It Works

```sql
WHERE e.salary >= 40000
```

Only employees earning at least ₹40,000 participate in the aggregation.

```sql
GROUP BY d.department_name
```

Creates one group per department.

```sql
COUNT(e.employee_id)
```

Counts the qualifying employees in each department.

```sql
AVG(e.salary)
```

Calculates the average salary using those qualifying employees.

```sql
HAVING COUNT(e.employee_id) >= 2
   AND AVG(e.salary) >= 50000
```

Filters the resulting departmental groups.

```sql
ORDER BY average_salary DESC
```

Places the highest average salary first.

## Test Result

Executed successfully against `learning.db`.

```text
+-----------------+----------------------+----------------+
| department_name | qualifying_employees | average_salary |
+-----------------+----------------------+----------------+
| Engineering     | 2                    | 55000.0        |
+-----------------+----------------------+----------------+
```

## Important Lesson

`WHERE` and `HAVING` solve different problems.

For:

> employees earning at least ₹40,000

use:

```sql
WHERE e.salary >= 40000
```

For:

> departments whose average salary is at least ₹50,000

use:

```sql
HAVING AVG(e.salary) >= 50000
```

Removing the `HAVING` condition would allow departments whose average salary
is below ₹50,000 to appear.

## SQLite vs PostgreSQL Note

SQLite accepted the alias-based form:

```sql
HAVING qualifying_employees >= 2
   AND average_salary >= 50000
```

For backend work targeting PostgreSQL and portability, prefer the explicit
aggregate expressions:

```sql
HAVING COUNT(e.employee_id) >= 2
   AND AVG(e.salary) >= 50000
```

## Common Mistake

Do not try to use `WHERE` for aggregate conditions such as:

```sql
WHERE AVG(e.salary) >= 50000
```

The aggregate condition belongs after grouping, in `HAVING`.

## Checkpoint

- [x] JOIN
- [x] WHERE
- [x] GROUP BY
- [x] COUNT()
- [x] AVG()
- [x] HAVING
- [x] ORDER BY
- [x] Combined business-requirement query
- [x] Executed against SQLite
- [x] Verified output

**Day 33 status: Complete**

Next: **Day 34 — Transactions**
