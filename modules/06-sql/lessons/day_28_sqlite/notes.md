
# Day 28 — SQLite Fundamentals

## Core Model

```text
Business Requirement
        ↓
Entity
        ↓
Table
        ↓
Constraints
        ↓
Database-enforced Integrity
````

## Constraints

| Constraint    | Purpose                        |
| ------------- | ------------------------------ |
| `PRIMARY KEY` | Uniquely identifies a row      |
| `FOREIGN KEY` | Maintains a valid relationship |
| `NOT NULL`    | Requires a value               |
| `UNIQUE`      | Prevents duplicate values      |
| `CHECK`       | Enforces a condition           |

## Foreign Key

```text
employee.department_id
        ↓
department.department_id
```

A foreign key protects the relationship between the child and parent tables.

SQLite foreign-key enforcement is enabled per connection:

```sql
PRAGMA foreign_keys = ON;
```

## Schema

```sql
CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    employee_email TEXT UNIQUE,
    department_id INTEGER NOT NULL,
    salary INTEGER CHECK (salary >= 0),
    FOREIGN KEY (department_id)
        REFERENCES department(department_id)
);
```

## Constraint Behavior

```text
PRIMARY KEY
→ identifies a row

FOREIGN KEY
→ references a row in another table

UNIQUE
→ prevents duplicate values

NOT NULL
→ prevents missing values

CHECK
→ prevents values that violate a condition
```

## Referential Integrity

```text
Employee.department_id = 999
        ↓
Department 999 does not exist
        ↓
FOREIGN KEY constraint failed
```

## Foreign-Key Enforcement

Foreign-key definition and enforcement are separate:

```text
FOREIGN KEY (...)
REFERENCES (...)
        ↓
Defines the relationship
```

```text
PRAGMA foreign_keys = ON
        ↓
Enables enforcement for the connection
```

## Transaction

```python
connection.commit()
```

`commit()` persists the changes made in the transaction.

## Constraint Testing

Verified that SQLite rejects:

* Invalid foreign-key references.
* `NULL` values on `NOT NULL` columns.
* Duplicate values on `UNIQUE` columns.
* Values violating `CHECK`.
* Duplicate primary keys.

## Key Principle

> Application validation protects the application path. Database constraints protect persisted data.

## Checkpoint

Implemented and tested:

* SQLite database creation
* Table creation
* Primary keys
* Foreign keys
* `NOT NULL`
* `UNIQUE`
* `CHECK`
* Referential integrity
* Foreign-key enforcement
* Basic transaction commit

