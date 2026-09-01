# Day 32 — SQL JOINs

## Lesson Goal

Understand and apply SQL `JOIN` operations to retrieve related data from multiple tables.

## What I Learned

- A `FOREIGN KEY` establishes a relationship between tables.
- A `JOIN` retrieves related data from those tables.
- `INNER JOIN` returns rows where matching records exist in both tables.
- `ON` defines how the tables are related for the query.
- `WHERE` filters the joined result.
- Table aliases make queries shorter and easier to read.
- Specific columns should be selected when the application does not need every column.
- A valid SQL query still needs correct result handling in Python.

## Tables Used

```text
department
├── department_id (PRIMARY KEY)
└── department_name

employee
├── employee_id (PRIMARY KEY)
├── employee_name
├── employee_email
├── department_id (FOREIGN KEY)
└── salary
````

Relationship:

```text
department.department_id
          ↑
          │
          │ referenced by
          │
employee.department_id
```

## Basic JOIN

```sql
SELECT
    e.employee_name,
    d.department_name
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id;
```

## JOIN with Filtering

```sql
SELECT
    e.employee_name,
    d.department_name
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE d.department_name = ?;
```

Python parameter:

```python
("HR",)
```

## JOIN with Multiple Conditions

```sql
SELECT
    e.employee_name,
    e.salary
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE d.department_id = ?
  AND e.salary >= ?;
```

Parameters:

```python
(1, 50000)
```

## Key Mental Model

```text
FOREIGN KEY
    ↓
Defines relationship and protects integrity

JOIN
    ↓
Connects related rows for a query

ON
    ↓
Defines how rows match

WHERE
    ↓
Filters the result

SELECT
    ↓
Chooses the data to return
```

## Practice Completed

1. Return every employee with their department name.
2. Return employees belonging to HR.
3. Return employees from department 1 earning at least 50,000.
4. Return employee name, email, salary, and department name.
5. Use table aliases and parameterized queries.
6. Correctly assign query results to `rows` before processing them in Python.

## Important Distinction

```text
FOREIGN KEY ≠ JOIN

FOREIGN KEY
→ database relationship/integrity rule

JOIN
→ query operation for retrieving related data
```

## Status

**Day 32 — Complete**

````

``
