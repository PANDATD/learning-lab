
# Day 35 — SQLite + Python Error Handling

## Objective

Learn how to handle SQLite database errors in Python using the `sqlite3` exception hierarchy and combine exception handling with transaction management.

## Topics Covered

* SQLite exception hierarchy
* `sqlite3.IntegrityError`
* `sqlite3.OperationalError`
* `sqlite3.Error`
* Specific vs. general exception handling
* Exception handler ordering
* `commit()` and `rollback()` with exceptions
* `finally` for database connection cleanup
* Backend-oriented database error handling

## Exception Hierarchy

The important part of the SQLite exception hierarchy used in this lesson:

```text
sqlite3.Error
├── sqlite3.IntegrityError
├── sqlite3.OperationalError
├── sqlite3.ProgrammingError
└── ...
```

### `sqlite3.IntegrityError`

Used for database constraint violations.

Examples:

* Duplicate value violating `UNIQUE`
* Invalid value violating `CHECK`
* Foreign-key constraint violation

Example:

```python
except sqlite3.IntegrityError as e:
    conn.rollback()
    print(e)
```

### `sqlite3.OperationalError`

Used for operational/database problems.

Example:

```text
no such table: employees
```

This is different from an integrity violation.

### `sqlite3.Error`

`sqlite3.Error` is a broader SQLite exception that can be used as a general database-error fallback.

```python
except sqlite3.Error as e:
    conn.rollback()
    print(e)
```

## Exception Ordering

Specific exceptions should be handled before their broader parent exception.

Correct:

```python
except sqlite3.IntegrityError:
    ...

except sqlite3.Error:
    ...
```

The `sqlite3.Error` handler acts as the fallback for other SQLite errors.

## Transactions + Error Handling

The employee creation operation was implemented with an explicit transaction:

```python
conn.execute("BEGIN TRANSACTION")

conn.execute(
    """
    INSERT INTO employee(
        employee_id,
        employee_name,
        employee_email,
        department_id,
        salary
    )
    VALUES(?,?,?,?,?)
    """,
    (
        employee_id,
        employee_name,
        employee_email,
        department_id,
        salary,
    ),
)

conn.commit()
```

If an error occurs:

```python
except sqlite3.IntegrityError as e:
    conn.rollback()
    print(e)
```

The rollback prevents the failed transaction from leaving its uncommitted changes in the database.

## Cleanup

The connection is closed in `finally`:

```python
finally:
    conn.close()
```

This ensures cleanup occurs whether the operation succeeds or fails.

## Verification

### Successful transaction

A new employee was inserted:

```text
108|Test Employee|test.employee@gmail.com|2|50000
```

The row remained in the database after `commit()`.

### Failed transaction

A second attempt using the same employee ID produced:

```text
UNIQUE constraint failed: employee.employee_id
```

The failure was handled by `sqlite3.IntegrityError`.

Verification confirmed that the failed employee was not inserted.

## Backend Connection

The error-handling flow can be viewed as:

```text
SQL operation
     ↓
SQLite detects failure
     ↓
sqlite3 exception
     ↓
Python exception handler
     ↓
ROLLBACK
     ↓
Application handles the failure
```

Different database failures should remain distinguishable:

```text
Duplicate email / CHECK violation
        ↓
IntegrityError

Missing table / operational problem
        ↓
OperationalError
```

In a real backend application, the application layer can later map these database failures to appropriate API responses.

## Key Takeaways

1. Database errors should be handled using the `sqlite3` exception hierarchy.
2. `IntegrityError` handles constraint violations.
3. `OperationalError` handles operational database problems.
4. `sqlite3.Error` can provide a general SQLite error fallback.
5. Specific exception handlers should come before general handlers.
6. `rollback()` is important when a transaction fails.
7. `finally` is appropriate for connection cleanup.
8. `except Exception` is broader than necessary for SQLite-specific error handling.
9. Specific and general handlers are useful when they have different behavior.
10. Do not introduce additional abstractions before they are required.

## Completion Status

**Day 35 — Complete**

Covered:

* [x] SQLite exception hierarchy
* [x] `IntegrityError`
* [x] `OperationalError`
* [x] `sqlite3.Error`
* [x] Specific → general exception ordering
* [x] Transaction error handling
* [x] Rollback verification
* [x] Connection cleanup
* [x] Backend connection
