
# `README.md`

# Day 31 — SQLite Filtering + Sorting

## Goal

Practice filtering, sorting, and limiting SQLite query results.

## What I Learned

- `WHERE` filters rows.
- Comparison operators: `=`, `>`, `>=`, `<`, `<=`, `!=`.
- `AND` requires multiple conditions to be true.
- `OR` allows either condition to be true.
- `IN` matches multiple possible values.
- `BETWEEN` matches an inclusive range.
- `LIKE` matches text patterns.
- `ORDER BY` sorts query results.
- `ASC` sorts low to high.
- `DESC` sorts high to low.
- `LIMIT` restricts the number of returned rows.
- Business requirements can be translated into SQL conditions.

## Practice

Implemented queries for:

1. Employees earning more than 50,000.
2. Employees belonging to department 1.
3. Employees belonging to departments 1, 2, or 4.
4. Employees earning between 40,000 and 60,000.
5. Two highest-paid employees.
6. Two highest-paid employees from departments 1 or 2 earning at least 50,000.

## Key Pattern

```text
Business requirement
        ↓
WHERE condition
        ↓
ORDER BY
        ↓
LIMIT
        ↓
Query result
````

## Checkpoint

Completed SQLite filtering, sorting, and limiting practice.

**Status:** Complete

````

```markdown

