# Day 29 — SQLite CRUD: INSERT + SELECT

## Goal

Practice inserting and retrieving persistent data with SQLite.

## What I Learned

- `INSERT` records into SQLite.
- Parameterized SQL using `?`.
- `executemany()` for multiple records.
- `commit()` to persist changes.
- `SELECT` to retrieve records.
- `fetchone()` for a single expected record.
- `fetchall()` for multiple records.
- `WHERE` for targeted queries.
- SQLite constraint enforcement during data insertion.

## Implementation

Worked with:

- `department`
- `employee`

Relationship:

```text
department 1 ───── N employee
```


## Query Patterns

```python
connection.execute(
    """
    INSERT INTO department (department_id, department_name)
    VALUES (?, ?)
    """,
    (1, "Engineering"),
)
```

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

## Constraint Testing

Verified that invalid inserts are rejected for:

* Duplicate primary key.
* Duplicate unique email.
* Invalid foreign key.

## Key Principle

> Use parameterized SQL for values and let database constraints protect data integrity.

## Checkpoint

Successfully inserted and retrieved SQLite records using Python's `sqlite3` module.

````
