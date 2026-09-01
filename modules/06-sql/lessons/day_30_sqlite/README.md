
# Day 30 — SQLite UPDATE + DELETE

## Goal

Modify and remove existing records safely.

## UPDATE

Modify a specific record:

```python
connection.execute(
    """
    UPDATE employee
    SET salary = ?
    WHERE employee_id = ?
    """,
    (65000, 104),
)
````

`WHERE` determines which rows are modified.

Without `WHERE`:

```sql
UPDATE employee
SET salary = 75000;
```

Every employee is updated.

## DELETE

Delete a specific record:

```python
connection.execute(
    """
    DELETE FROM employee
    WHERE employee_id = ?
    """,
    (106,),
)
```

Without `WHERE`:

```sql
DELETE FROM employee;
```

All rows are deleted, but the table remains.

```text
DELETE → rows
DROP   → table
```

## `rowcount`

`rowcount` shows the number of rows affected by `UPDATE` or `DELETE`.

```python
cursor = connection.execute(...)
print(cursor.rowcount)
```

Examples:

```text
UPDATE employee_id = 104
→ rowcount = 1

UPDATE employee_id = 999
→ rowcount = 0

DELETE employee_id = 106
→ rowcount = 1
```

A nonexistent record does not automatically cause an error.

```text
SQL valid
    ↓
No matching row
    ↓
rowcount = 0
```

## Verify Changes

Use `SELECT` with `fetchone()` to verify a specific record.

```python
row = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE employee_id = ?
    """,
    (104,),
).fetchone()
```

After deleting employee `106`:

```python
row = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE employee_id = ?
    """,
    (106,),
).fetchone()

print(row)
```

Expected:

```text
None
```

Do not use `rowcount` to verify a `SELECT` result. Use `fetchone()` or `fetchall()`.

## Transaction Flow

```text
UPDATE / DELETE
      ↓
commit()
      ↓
SELECT
      ↓
verify
```

## Parameterized SQL

Use parameters for values:

```python
connection.execute(
    """
    UPDATE employee
    SET salary = ?
    WHERE employee_id = ?
    """,
    (65000, 104),
)
```

Do not construct SQL by interpolating values into the SQL string.

## Key Principles

* Always think about the `WHERE` clause before `UPDATE` or `DELETE`.
* Use primary keys for targeted single-record operations.
* Use parameterized SQL.
* Check `rowcount` when the number of affected rows matters.
* Verify changes with `SELECT`.
* `rowcount = 0` means no row matched; it is not necessarily a database error.
* `DELETE` removes rows; `DROP TABLE` removes the table.

## Checkpoint

```text
Day 29
INSERT + SELECT
        ↓
Day 30
UPDATE + DELETE
        ↓
WHERE safety
        ↓
rowcount
        ↓
Verification
```

````

```
```
