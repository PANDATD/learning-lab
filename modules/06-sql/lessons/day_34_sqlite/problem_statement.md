
# Day 34 — SQLite Transactions

## Problem Statement

Using the existing `learning.db` SQLite database, demonstrate how database transactions provide atomicity when multiple database operations belong to the same logical unit of work.

Write a Python program using the standard-library `sqlite3` module that:

1. Connects to `learning.db`.
2. Starts an explicit database transaction.
3. Inserts a new employee.
4. Updates that employee within the same transaction.
5. Commits the transaction when all operations succeed.
6. Handles a database failure using exception handling.
7. Rolls back the transaction when an operation fails.
8. Verifies that changes made before the failure are not persisted after the rollback.
9. Closes the database connection regardless of whether the transaction succeeds or fails.

For the failure scenario, deliberately violate the existing employee salary constraint:

```sql
CHECK(salary >= 0)
```

The program should demonstrate the difference between:

```text
Successful transaction
    BEGIN
      ↓
    INSERT
      ↓
    UPDATE
      ↓
    COMMIT
```

and:

```text
Failed transaction
    BEGIN
      ↓
    INSERT
      ↓
    UPDATE → constraint failure
      ↓
    ROLLBACK
```

## Learning Objective

The objective is to understand that multiple database operations can form one transaction and that `ROLLBACK` can discard uncommitted changes made earlier in the same transaction.

The implementation should remain simple and use only Python's `sqlite3` module. Do not introduce SQLAlchemy, repository patterns, or unnecessary abstractions.
