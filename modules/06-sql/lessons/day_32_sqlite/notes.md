# Day 32 — SQL JOINs

## 1. Why JOIN?

Data is often normalized into multiple related tables.

Example:

```text
department
    │
    │ department_id
    ↓
employee
````

The employee table stores `department_id`, while the department table stores the department details.

A `JOIN` allows us to retrieve information from both tables.

---

## 2. Foreign Key Relationship

The relationship is:

```text
department.department_id
        ↑
        │
        │ referenced by
        │
employee.department_id
```

`employee.department_id` is a foreign key referencing `department.department_id`.

The foreign key:

* Establishes the relationship.
* Helps protect referential integrity.
* Does not itself retrieve data from both tables.

---

## 3. INNER JOIN

Basic syntax:

```sql
SELECT ...
FROM table_a
INNER JOIN table_b
    ON table_a.column = table_b.column;
```

Example:

```sql
SELECT *
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id;
```

`INNER JOIN` returns rows where the `ON` condition has a matching row in both tables.

---

## 4. JOIN with Selected Columns

Instead of:

```sql
SELECT *
```

select only the required columns:

```sql
SELECT
    e.employee_name,
    d.department_name
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id;
```

Possible result:

```text
Data Kale       | HR
Himali Nalawade | Content
Kavita Kamat    | Technical
```

---

## 5. Table Aliases

Aliases provide shorter names for tables:

```sql
FROM employee AS e
INNER JOIN department AS d
```

Therefore:

```text
e → employee
d → department
```

Example:

```sql
e.employee_name
d.department_name
```

Use aliases when they improve readability.

---

## 6. ON

`ON` defines how rows from the two tables should match.

```sql
ON e.department_id = d.department_id
```

Think:

```text
employee.department_id
          =
department.department_id
```

---

## 7. WHERE

`WHERE` filters the rows.

Example:

```sql
SELECT
    e.employee_name,
    d.department_name
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE d.department_name = ?;
```

Python:

```python
("HR",)
```

Mental model:

```text
JOIN
→ connect related rows

WHERE
→ filter those rows
```

---

## 8. JOIN + WHERE + AND

Business requirement:

> Return employees from department 1 whose salary is at least 50,000.

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

Requirement translation:

```text
department 1
    ↓
d.department_id = 1

AND

salary at least 50,000
    ↓
e.salary >= 50000
```

---

## 9. INNER JOIN and Missing Relationships

Suppose:

```text
employee
107 | Yashraj | department_id = 9
```

but:

```text
department
(no department_id = 9)
```

An `INNER JOIN` will not return employee `107` because there is no matching department row.

This is separate from foreign-key enforcement.

```text
PRAGMA foreign_keys = ON
        ↓
controls whether invalid FK data can be stored

INNER JOIN
        ↓
controls which matching rows appear in the result
```

---

## 10. JOIN vs FOREIGN KEY

### FOREIGN KEY

```text
Database integrity
```

Protects the relationship between tables.

### JOIN

```text
Query operation
```

Retrieves related data.

They are related concepts but serve different purposes.

---

## 11. JOIN vs WHERE

```text
JOIN ... ON
→ How are these tables related?

WHERE
→ Which rows do I want?
```

Example:

```sql
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE d.department_name = ?;
```

---

## 12. Python Result Handling

A correct SQL query is not enough.

Incorrect:

```python
connection.execute(
    """
    SELECT ...
    """
).fetchall()

for row in rows:
    print(row)
```

The query result was not assigned to `rows`.

Correct:

```python
rows = connection.execute(
    """
    SELECT ...
    """
).fetchall()

for row in rows:
    print(row)
```

Important backend lesson:

```text
SQL correctness
      +
Python result handling
      =
Correct database operation
```

---

## 13. Parameterized JOIN Queries

Use placeholders for supplied values:

```python
rows = conn.execute(
    """
    SELECT
        e.employee_name,
        d.department_name
    FROM employee AS e
    INNER JOIN department AS d
        ON e.department_id = d.department_id
    WHERE d.department_name = ?
    """,
    ("HR",),
).fetchall()
```

Do not construct SQL by directly inserting user-provided values into the query string.

---

## 14. Day 32 Query Pattern

```text
SELECT
    ↓
FROM
    ↓
INNER JOIN
    ↓
ON
    ↓
WHERE
    ↓
fetchall()
    ↓
process rows
```

Example:

```sql
SELECT
    e.employee_name,
    e.salary,
    d.department_name
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE d.department_id = ?
  AND e.salary >= ?;
```

---

## 15. Key Takeaways

* `FOREIGN KEY` defines and protects a relationship.
* `JOIN` retrieves related data.
* `INNER JOIN` requires a matching row in both tables.
* `ON` defines the matching relationship for the query.
* `WHERE` filters rows.
* `AS` creates table aliases.
* Select only the columns required by the application.
* Parameterize supplied values.
* Always assign query results before processing them.
* A query can be syntactically valid while the surrounding Python code is still incorrect.

## Status

**Day 32 — Complete**

