## `notes.md`

```markdown
# Day 29 — SQLite CRUD: INSERT + SELECT

## INSERT

Insert one record:

```python
connection.execute(
    """
    INSERT INTO department (department_id, department_name)
    VALUES (?, ?)
    """,
    (1, "Engineering"),
)
````

Use `?` placeholders for values.

```text
SQL structure
     +
parameters
     ↓
SQLite
```

## Parameterized Queries

Avoid constructing SQL with user or external values:

```python
f"INSERT INTO ... '{value}'"
```

Use parameters:

```python
connection.execute(
    "INSERT INTO department (department_name) VALUES (?)",
    (name,),
)
```

This separates SQL structure from data and helps prevent SQL injection.

## `executemany()`

Use `executemany()` when applying the same SQL operation to multiple records:

```python
connection.executemany(
    """
    INSERT INTO department (department_id, department_name)
    VALUES (?, ?)
    """,
    [
        (2, "HR"),
        (3, "Content"),
        (4, "Technical"),
    ],
)
```

## `commit()`

```python
connection.commit()
```

Persists changes made in the transaction.

```text
INSERT
  ↓
Transaction
  ↓
commit()
  ↓
Persisted data
```

## SELECT

Retrieve records:

```python
rows = connection.execute(
    "SELECT * FROM employee"
).fetchall()
```

## `fetchone()` vs `fetchall()`

```text
fetchone()
→ one row or None

fetchall()
→ list of all matching rows
```

For a primary-key lookup:

```python
employee = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE employee_id = ?
    """,
    (104,),
).fetchone()
```

Because `employee_id` is a primary key:

```text
employee_id
    ↓
PRIMARY KEY
    ↓
0 or 1 matching row
    ↓
fetchone()
```

For multiple employees:

```python
employees = connection.execute(
    "SELECT * FROM employee"
).fetchall()
```

## `WHERE`

`WHERE` restricts which rows are returned:

```sql
SELECT *
FROM employee
WHERE employee_id = ?;
```

No matching record:

```text
fetchone() → None
fetchall() → []
```

## Constraint + CRUD

```text
INSERT
  ↓
Database constraints
  ↓
Valid → persisted
Invalid → rejected
```

Examples:

```text
Duplicate employee_id
→ PRIMARY KEY violation

Duplicate employee_email
→ UNIQUE violation

Nonexistent department_id
→ FOREIGN KEY violation
```

## SQLite Foreign Keys

Foreign-key enforcement must be enabled for the connection:

```python
connection.execute("PRAGMA foreign_keys = ON")
```

## Key Principles

* Use parameterized SQL.
* Commit intentional changes.
* Use `WHERE` for targeted queries.
* Use `fetchone()` when the schema guarantees at most one result.
* Use `fetchall()` when multiple rows are expected.
* Let database constraints reject invalid data.

## Checkpoint

```text
Day 28
Schema + Constraints
        ↓
Day 29
INSERT + SELECT
        ↓
Parameterized SQL
        ↓
commit()
        ↓
fetchone() / fetchall()
        ↓
Constraint enforcement
```

```
```
