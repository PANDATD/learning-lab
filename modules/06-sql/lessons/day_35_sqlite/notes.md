
# Day 35 Notes — SQLite + Python Error Handling

## 1. Core Concept

Python's `sqlite3` module provides exceptions specifically for database-related failures.

The important hierarchy for this lesson:

```text
sqlite3.Error
├── sqlite3.IntegrityError
├── sqlite3.OperationalError
├── sqlite3.ProgrammingError
└── ...
```

`sqlite3.Error` is the broad parent for SQLite database errors.

---

## 2. `sqlite3.IntegrityError`

`IntegrityError` occurs when a database constraint is violated.

Examples:

```text
UNIQUE
CHECK
FOREIGN KEY
```

Example:

```python
try:
    conn.execute(
        """
        INSERT INTO employee(
            employee_id,
            employee_name,
            employee_email,
            department_id,
            salary
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (107, "Atish", "existing@email.com", 2, 56000),
    )

    conn.commit()

except sqlite3.IntegrityError as e:
    conn.rollback()
    print(e)
```

A duplicate employee ID produced:

```text
UNIQUE constraint failed: employee.employee_id
```

---

## 3. `sqlite3.OperationalError`

`OperationalError` represents operational problems with the database operation.

Example:

```python
try:
    conn.execute(
        """
        SELECT * FROM employees;
        """
    )

except sqlite3.OperationalError as e:
    print(e)
```

Output:

```text
no such table: employees
```

`employees` and `employee` are different table names, so SQLite reports the missing table as an operational error.

This is not an `IntegrityError`.

---

## 4. `sqlite3.Error`

`sqlite3.Error` can be used when we want a general fallback for SQLite errors.

```python
except sqlite3.Error as e:
    conn.rollback()
    print(e)
```

It can catch more specific SQLite exceptions such as:

```text
IntegrityError
OperationalError
ProgrammingError
```

The general handler should come after specific handlers.

---

## 5. Specific Before General

Correct:

```python
except sqlite3.IntegrityError:
    ...

except sqlite3.Error:
    ...
```

Incorrect:

```python
except sqlite3.Error:
    ...

except sqlite3.IntegrityError:
    ...
```

The first version allows the specific `IntegrityError` handler to run before the general fallback.

If the handlers have exactly the same behavior, keeping both provides little practical benefit.

Use separate handlers when the application needs different behavior for different error categories.

---

## 6. Transactions + Exceptions

Employee creation was implemented as one transaction:

```python
try:
    conn.execute("BEGIN TRANSACTION")

    conn.execute(insert_sql, data)

    conn.commit()

except sqlite3.IntegrityError as e:
    conn.rollback()
    print(e)

except sqlite3.Error as e:
    conn.rollback()
    print(e)

finally:
    conn.close()
```

Flow:

```text
BEGIN TRANSACTION
       ↓
     INSERT
       ↓
   ┌───┴────┐
 success   failure
   ↓          ↓
 COMMIT    ROLLBACK
   ↓          ↓
persist     discard
```

---

## 7. Why Rollback Matters

Suppose one business operation contains several database changes:

```text
BEGIN
  ↓
Operation 1 → success
  ↓
Operation 2 → success
  ↓
Operation 3 → IntegrityError
```

If the transaction is rolled back:

```text
ROLLBACK
   ↓
Changes from the transaction are discarded
```

This maintains atomicity.

The important idea is:

> A transaction represents one logical unit of work.

---

## 8. `finally` and Cleanup

The connection was closed in `finally`:

```python
finally:
    conn.close()
```

`finally` is appropriate for cleanup because it runs regardless of whether the operation succeeds or raises an exception.

---

## 9. Application Validation vs Database Constraints

Application validation and database constraints have different responsibilities.

For example:

```text
Application validation
        ↓
Check input before database operation

Database constraint
        ↓
Protect database integrity
```

Database exceptions should not be treated as the only form of input validation.

The database still needs constraints because the database itself must protect its data integrity.

---

## 10. `except Exception` vs `sqlite3.Error`

Avoid using:

```python
except Exception as e:
    print(e)
```

when the purpose is specifically to handle SQLite errors.

Prefer:

```python
except sqlite3.Error as e:
    print(e)
```

This makes the intended failure domain clearer.

`Exception` is much broader and can also catch unrelated Python errors.

---

## 11. Verification Performed

### Successful insert

```text
108|Test Employee|test.employee@gmail.com|2|50000
```

Confirmed that the transaction was committed.

### Duplicate employee ID

The second insert used employee ID `108`.

SQLite returned:

```text
UNIQUE constraint failed: employee.employee_id
```

This was caught by:

```python
except sqlite3.IntegrityError as e:
```

### Rollback verification

Query:

```sql
SELECT * FROM employee
WHERE employee_name = 'Should Not Be Inserted';
```

Returned no rows.

Therefore, the failed insert did not remain in the database.

---

## 12. Backend Mental Model

```text
Database operation
       ↓
SQLite detects failure
       ↓
Specific SQLite exception
       ↓
Python exception handler
       ↓
Rollback transaction
       ↓
Application-level handling
       ↓
Eventually → API response
```

The final API response mapping is intentionally left for the FastAPI stage.

---

## 13. Key Lessons

* `IntegrityError` → constraint violation.
* `OperationalError` → operational/database problem.
* `sqlite3.Error` → general SQLite error category.
* Specific exceptions should come before broad parent exceptions.
* Rollback protects transaction atomicity.
* Commit persists successful work.
* `finally` is suitable for cleanup.
* Avoid unnecessarily broad `except Exception`.
* Keep exception handling as simple as the current requirement allows.
* Different handlers should have different behavior when possible.

## Day 35 Status

**Complete**

```text
Remember       ✓
Understand     ✓
Apply          ✓
Analyze        ✓
Evaluate       ✓
Create         ✓
Verify         ✓
Backend link   ✓
```
