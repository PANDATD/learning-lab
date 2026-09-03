
# Day 34 — SQLite Transactions

## Overview

Day 34 focused on database transactions and atomicity using SQLite and Python's standard-library `sqlite3` module.

The lesson progressed from manually controlling transactions in the SQLite CLI to implementing transaction handling in Python.

## Topics Covered

* Database transactions
* ACID atomicity
* `BEGIN TRANSACTION`
* `COMMIT`
* `ROLLBACK`
* Transaction boundaries
* Python `sqlite3` transaction handling
* Exception handling
* Connection cleanup

## Successful Transaction

A successful transaction was implemented as:

```text
BEGIN TRANSACTION
      ↓
INSERT employee
      ↓
UPDATE employee
      ↓
COMMIT
```

The changes were verified after committing.

## Failed Transaction

A failure was deliberately introduced by violating the existing salary constraint:

```sql
CHECK(salary >= 0)
```

The transaction followed:

```text
BEGIN TRANSACTION
      ↓
INSERT employee 109
      ↓
UPDATE salary → -90000
      ↓
CHECK constraint failure
      ↓
ROLLBACK
```

The inserted employee was not present after the rollback.

This demonstrated that an operation can succeed inside a transaction but still be discarded if the transaction is subsequently rolled back.

## Python Transaction Pattern

The Python implementation used:

```python
try:
    # transactional operations
    conn.commit()

except Exception:
    conn.rollback()

finally:
    conn.close()
```

The `sqlite3.Connection` object was used for:

* executing SQL
* committing transactions
* rolling back transactions
* closing the database connection

## Key Concept

### Atomicity

Multiple related database operations can be treated as one logical unit:

```text
BEGIN
  ↓
Operation A
Operation B
Operation C
  ↓
success → COMMIT
failure → ROLLBACK
```

The transaction boundary should correspond to the logical business operation whose changes need to succeed or fail together.

## Important Distinction

`ROLLBACK` only affects the current uncommitted transaction.

If operations have already been committed:

```text
A → COMMIT
B → COMMIT
C → FAIL
```

a rollback of C cannot undo A or B.

## Day 34 Status

**Completed**

The following capabilities were demonstrated:

* [x] Understand transactions
* [x] Understand atomicity
* [x] Use `BEGIN TRANSACTION`
* [x] Use `COMMIT`
* [x] Use `ROLLBACK`
* [x] Handle transaction failure
* [x] Use `sqlite3` transaction methods
* [x] Verify rollback behavior
* [x] Close database connections safely

## Next

**Day 35 — SQLite + Python Error Handling**

Day 35 will build on today's transaction/error-handling work and focus specifically on handling SQLite exceptions and database failures cleanly in Python.
