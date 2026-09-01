
# Day 31 — SQLite Filtering + Sorting

## `WHERE`

Filters rows based on a condition.

```sql
SELECT *
FROM employee
WHERE salary > ?;
````

## Comparison Operators

```text
=   equal
!=  not equal
>   greater than
>=  greater than or equal
<   less than
<=  less than or equal
```

## `AND`

Both conditions must be true.

```sql
WHERE department_id = ?
  AND salary >= ?
```

## `OR`

At least one condition must be true.

```sql
WHERE department_id = ?
   OR department_id = ?
```

## `IN`

Matches one of multiple values.

```sql
WHERE department_id IN (?, ?, ?)
```

Equivalent to multiple equality conditions joined with `OR`.

## `BETWEEN`

Matches an inclusive range.

```sql
WHERE salary BETWEEN ? AND ?
```

```text
40000 <= salary <= 60000
```

## `LIKE`

Matches text patterns.

```sql
WHERE employee_name LIKE ?
```

Common patterns:

```text
D%   → starts with D
%D   → ends with D
%D%  → contains D
```

## `ORDER BY`

Sorts query results.

```sql
ORDER BY salary ASC
```

```text
low → high
```

```sql
ORDER BY salary DESC
```

```text
high → low
```

## `LIMIT`

Restricts the number of returned rows.

```sql
ORDER BY salary DESC
LIMIT 2
```

This returns the two highest-paid employees.

## Combining Conditions

Business requirement:

> Find the two highest-paid employees from departments 1 or 2 whose salary is at least 50,000.

```sql
SELECT *
FROM employee
WHERE department_id IN (?, ?)
  AND salary >= ?
ORDER BY salary DESC
LIMIT 2;
```

Parameters:

```python
(1, 2, 50000)
```

## Query Thinking

```text
WHERE
→ Which rows qualify?

ORDER BY
→ In what order?

LIMIT
→ How many?
```

## Parameterized Queries

Use placeholders for values:

```python
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE salary > ?
    """,
    (50000,),
).fetchall()
```

Do not construct SQL by directly inserting values into the query string.

## Key Principles

* Translate the business requirement before writing SQL.
* Use `WHERE` to filter.
* Use `AND` / `OR` to combine conditions.
* Use `IN` for multiple accepted values.
* `BETWEEN` includes both boundaries.
* Use `ORDER BY` to control result order.
* Use `LIMIT` to control result count.
* Use parameterized SQL for values.
* Keep the query direct while learning; avoid unnecessary abstractions.

## Day 31 Flow

```text
Day 29
INSERT + SELECT
        ↓
Day 30
UPDATE + DELETE
        ↓
Day 31
WHERE + Filtering
        ↓
AND / OR / IN / BETWEEN / LIKE
        ↓
ORDER BY
        ↓
LIMIT
```

**Status:** Complete


