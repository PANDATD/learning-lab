import sqlite3

connection = sqlite3.connect("learning.db")


# Employees earning more than 50,000.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE salary > ?
    """,
    (50000,),
).fetchall()

print("\nEmployees earning more than 50,000:")
for row in rows:
    print(row)


# Employees belonging to department 1.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE department_id = ?
    """,
    (1,),
).fetchall()

print("\nEmployees belonging to department 1:")
for row in rows:
    print(row)


# Employees belonging to departments 1, 2, or 4.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE department_id IN (?, ?, ?)
    """,
    (1, 2, 4),
).fetchall()

print("\nEmployees belonging to departments 1, 2, or 4:")
for row in rows:
    print(row)


# Employees earning between 40,000 and 60,000.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE salary BETWEEN ? AND ?
    """,
    (40000, 60000),
).fetchall()

print("\nEmployees earning between 40,000 and 60,000:")
for row in rows:
    print(row)


# Find the two highest-paid employees.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    ORDER BY salary DESC
    LIMIT 2
    """
).fetchall()

print("\nTwo highest-paid employees:")
for row in rows:
    print(row)


# Find the two highest-paid employees from departments 1 or 2
# whose salary is at least 50,000.
rows = connection.execute(
    """
    SELECT *
    FROM employee
    WHERE department_id IN (?, ?)
      AND salary >= ?
    ORDER BY salary DESC
    LIMIT 2
    """,
    (1, 2, 50000),
).fetchall()

print("\nTwo highest-paid employees from departments 1 or 2:")
for row in rows:
    print(row)
