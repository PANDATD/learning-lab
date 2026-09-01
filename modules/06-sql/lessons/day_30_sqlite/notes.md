

# Day 30 — SQLite UPDATE + DELETE

## Goal

Practice modifying and deleting SQLite records safely.

## What I Learned

- `UPDATE` modifies existing rows.
- `DELETE` removes existing rows.
- `WHERE` controls which rows are affected.
- `rowcount` shows affected rows.
- `fetchone()` verifies a specific record.
- Parameterized SQL should be used for values.
- A missing record can result in `rowcount = 0` without an error.
- `DELETE` removes rows but does not remove the table.

## Operations Practiced

### UPDATE

```sql
UPDATE employee
SET salary = ?
WHERE employee_id = ?;
````

### DELETE

```sql
DELETE FROM employee
WHERE employee_id = ?;
```

### Verification

```sql
SELECT *
FROM employee
WHERE employee_id = ?;
```

## Safety Principle

> `WHERE` is the safety boundary for `UPDATE` and `DELETE`.

Without `WHERE`, the operation can affect every row.

## Testing

Verified:

* Updating employee `104`.
* Updating a nonexistent employee and receiving `rowcount = 0`.
* Deleting employee `106`.
* Verifying the deleted employee with `fetchone()` returning `None`.

## Checkpoint

```text
UPDATE
  ↓
commit()
  ↓
SELECT + fetchone()
  ↓
verify

DELETE
  ↓
commit()
  ↓
SELECT + fetchone()
  ↓
verify
```


