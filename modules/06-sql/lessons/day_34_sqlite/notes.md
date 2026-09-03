
# Day 34 — SQLite Transactions

## Objective

Understand database transactions and implement transaction handling using Python's built-in `sqlite3` module.

The main concepts covered were:

* Transactions
* Atomicity
* `BEGIN TRANSACTION`
* `COMMIT`
* `ROLLBACK`
* Transaction boundaries
* Python `sqlite3` connection transaction handling
* Exception handling around database operations

---

## What Is a Transaction?

A transaction is a logical unit of database work containing one or more database operations.

The operations are treated together:

```text
BEGIN
  ↓
Operation A
  ↓
Operation B
  ↓
Operation C
  ↓
COMMIT
```

If the transaction fails and is rolled back:

```text
BEGIN
  ↓
Operation A ✓
  ↓
Operation B ✓
  ↓
Operation C ✗
  ↓
ROLLBACK
```

The uncommitted changes from the transaction are discarded.

---

## Atomicity

Atomicity is one of the ACID properties.

The practical idea is:

> A transaction should be completed as a whole, or its uncommitted changes should be rolled back.

Example:

```text
Create employee
      +
Assign employee to project
```

If these operations represent one business operation, allowing only one of them to persist could leave the database in an undesirable state.

Think:

```text
Business operation
       ↓
Transaction
       ↓
 ┌───────────────┐
 │               │
Success        Failure
 │               │
COMMIT        ROLLBACK
```

---

## COMMIT

`COMMIT` successfully ends the transaction and makes its changes permanent.

Example:

```sql
BEGIN TRANSACTION;

INSERT INTO employee (...);

UPDATE employee
SET salary = 65000
WHERE employee_id = 106;

COMMIT;
```

After `COMMIT`, the changes are persisted.

Important distinction:

```text
COMMIT
  ↓
transaction completed
  ↓
changes are permanent
```

A later `ROLLBACK` cannot undo an already committed transaction.

---

## ROLLBACK

`ROLLBACK` discards changes made by the current uncommitted transaction.

Example:

```sql
BEGIN TRANSACTION;

INSERT INTO employee (...);

UPDATE employee
SET salary = -90000
WHERE employee_id = 107;

ROLLBACK;
```

If the update violates:

```sql
CHECK(salary >= 0)
```

the transaction can be rolled back.

The earlier successful `INSERT` is also discarded because it had not been committed.

---

## Important Distinction

A failed SQL statement and a rollback are not the same thing.

Example:

```text
BEGIN
  ↓
INSERT ✓
  ↓
UPDATE ✗
  ↓
ROLLBACK
```

The `UPDATE` failed, but the `INSERT` had already executed inside the transaction.

`ROLLBACK` is what discards the earlier uncommitted `INSERT`.

Therefore:

```text
Transaction
    ↓
SQL operations
    ↓
failure
    ↓
ROLLBACK
```

is different from:

```text
Operation A
    ↓
COMMIT

Operation B
    ↓
COMMIT

Operation C
    ↓
FAIL
```

If A and B were already committed, rolling back C cannot undo A and B.

---

## Transaction Boundary

A transaction boundary should correspond to a meaningful logical or business operation.

For example:

```text
POST /employees
       ↓
Create employee
Assign employee
Create audit record
       ↓
one logical operation
```

These operations may need to share one transaction:

```text
BEGIN

Create employee
Assign employee
Create audit record

COMMIT
```

If one operation fails:

```text
ROLLBACK
```

The important question is not simply:

> "Should I use a transaction?"

Instead ask:

> "Which operations must succeed or fail together?"

---

## Python sqlite3

The SQLite connection is the object used to manage the transaction.

Conceptually:

```text
connection
    ├── execute()
    ├── commit()
    └── rollback()
```

Example:

```python
import sqlite3

conn = sqlite3.connect("../learning.db")

try:
    conn.execute("BEGIN TRANSACTION")

    conn.execute(...)
    conn.execute(...)

    conn.commit()

except Exception as e:
    conn.rollback()
    print(f"Exception: {e}")

finally:
    conn.close()
```

The cursor is used to execute SQL, while the connection provides transaction control.

---

## Successful Transaction Practiced

The first implementation performed:

```text
BEGIN TRANSACTION
      ↓
INSERT employee 106
      ↓
UPDATE employee 106
      ↓
COMMIT
```

The employee was inserted with an initial salary and then updated before the transaction was committed.

The final database state confirmed the changes persisted.

---

## Failed Transaction Practiced

The second implementation deliberately violated:

```sql
CHECK(salary >= 0)
```

by attempting:

```sql
UPDATE employee
SET salary = -90000
WHERE employee_id = 109;
```

The update failed.

Python caught the exception:

```python
except Exception as e:
    conn.rollback()
```

The earlier `INSERT` was therefore discarded.

The verification query confirmed that employee `109` did not exist.

---

## Exception Handling Pattern

The basic pattern practiced was:

```text
try
    ↓
transactional operations
    ↓
commit

except
    ↓
rollback

finally
    ↓
close connection
```

Each section has a different responsibility:

| Section      | Responsibility                 |
| ------------ | ------------------------------ |
| `try`        | Execute transaction            |
| `commit()`   | Persist successful transaction |
| `except`     | Handle failure                 |
| `rollback()` | Discard uncommitted changes    |
| `finally`    | Release connection             |

---

## Common Mistakes

### 1. Committing each operation independently

```text
INSERT → COMMIT
UPDATE → COMMIT
```

This can allow a business operation to become partially committed.

### 2. Assuming a failed statement automatically means rollback

A statement failure and transaction rollback are separate concepts.

### 3. Trying to rollback already committed changes

`ROLLBACK` cannot undo changes from an already completed transaction.

### 4. Making the transaction boundary arbitrary

The transaction should represent a meaningful unit of work rather than simply grouping unrelated SQL statements.

### 5. Catching an error without resolving the transaction

When application code owns transaction handling, failure paths need deliberate rollback behavior.

---

## Key Mental Model

```text
             TRANSACTION
                  │
        ┌─────────┴─────────┐
        │                   │
    SUCCESS              FAILURE
        │                   │
     COMMIT              ROLLBACK
        │                   │
   Changes persist    Uncommitted changes
                      are discarded
```

---

## Day 34 Takeaway

The most important lesson was not the SQL syntax.

It was understanding **transaction boundaries and atomicity**:

```text
Multiple related operations
          ↓
      Transaction
          ↓
   ┌──────┴──────┐
 Success       Failure
    ↓              ↓
 COMMIT         ROLLBACK
```

This foundation will later map directly to transaction management in SQLAlchemy and backend service operations.
