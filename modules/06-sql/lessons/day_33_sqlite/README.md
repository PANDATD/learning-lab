# Day 33 — SQL Aggregation & GROUP BY

## Status

**Complete**

## What I Practiced

- Aggregate functions
- `GROUP BY`
- `HAVING`
- `JOIN` + aggregation
- `WHERE` + aggregation
- `ORDER BY` aggregated results
- Translating business requirements into SQL

## Key Distinction

| Clause | Purpose | Timing |
|---|---|---|
| `WHERE` | Filter individual rows | Before grouping |
| `GROUP BY` | Create groups | Before aggregation |
| `COUNT()` / `AVG()` | Calculate group values | During aggregation |
| `HAVING` | Filter groups | After aggregation |
| `ORDER BY` | Sort final results | Final result |

## Query-Building Checklist

When given a SQL business requirement:

```text
What do I SELECT?
        ↓
What tables do I need?
        ↓
Do I need JOIN?
        ↓
What rows should be filtered?
        ↓
Do I need GROUP BY?
        ↓
What aggregate do I need?
        ↓
Do I need HAVING?
        ↓
How should the result be ordered?
```

## Final Query

```sql
SELECT
    d.department_name,
    COUNT(e.employee_id) AS qualifying_employees,
    AVG(e.salary) AS average_salary
FROM employee AS e
INNER JOIN department AS d
    ON e.department_id = d.department_id
WHERE e.salary >= 40000
GROUP BY d.department_name
HAVING COUNT(e.employee_id) >= 2
   AND AVG(e.salary) >= 50000
ORDER BY average_salary DESC;
```

## Verified Result

```text
Engineering | 2 | 55000.0
```

The query was executed successfully against `learning.db`.

## Main Takeaway

> `WHERE` decides which rows participate in aggregation; `HAVING` decides
> which aggregated groups survive.

## Engineering Note

Use explicit aggregate expressions in `HAVING` for portability:

```sql
HAVING COUNT(e.employee_id) >= 2
   AND AVG(e.salary) >= 50000
```

rather than relying on SQLite's acceptance of aggregate aliases in `HAVING`.

## Previous / Next

- Previous: **Day 32 — SQL JOINs**
- Current: **Day 33 — Aggregation + GROUP BY / HAVING**
- Next: **Day 34 — Transactions**

## Day 33 Checkpoint

- [x] Understand `WHERE` vs `HAVING`
- [x] Build grouped queries
- [x] Use `COUNT()` and `AVG()`
- [x] Combine JOIN + WHERE + GROUP BY + HAVING + ORDER BY
- [x] Run and verify the query
- [x] Identify SQLite-specific convenience vs portable SQL

**Next lesson:** Transactions and atomic database operations.
