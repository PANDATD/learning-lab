import sqlite3

conn = sqlite3.connect("learning.db")

# Enable foreign key constraints.
conn.execute("PRAGMA foreign_keys = ON")


# 1. Return employee name and department name for every employee.
rows = conn.execute(
    """
    SELECT
        e.employee_name,
        d.department_name
    FROM employee AS e
    INNER JOIN department AS d
        ON e.department_id = d.department_id
    """
).fetchall()

print("\nAll employees:")
for row in rows:
    print(row)


# 2. Return employees belonging to HR.
rows = conn.execute(
    """
    SELECT
        e.employee_name,
        d.department_name
    FROM employee AS e
    INNER JOIN department AS d
        ON e.department_id = d.department_id
    WHERE d.department_name = ?
    """,
    ("HR",),
).fetchall()

print("\nEmployees belonging to HR:")
for row in rows:
    print(row)


# 3. Return employees from department 1 whose salary is at least 50,000.
rows = conn.execute(
    """
    SELECT
        e.employee_name,
        e.salary
    FROM employee AS e
    INNER JOIN department AS d
        ON e.department_id = d.department_id
    WHERE d.department_id = ?
      AND e.salary >= ?
    """,
    (1, 50000),
).fetchall()

print("\nDepartment 1 — employees with salary at least 50,000:")
for row in rows:
    print(row)


# 4. Return employee name, email, salary, and department name.
rows = conn.execute(
    """
    SELECT
        e.employee_name,
        e.employee_email,
        e.salary,
        d.department_name
    FROM employee AS e
    INNER JOIN department AS d
        ON e.department_id = d.department_id
    """
).fetchall()

print("\nAll employees with details including department:")
for row in rows:
    print(row)


conn.close()
